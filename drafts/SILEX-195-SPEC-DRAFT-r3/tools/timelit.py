#!/usr/bin/env python3
"""timelit.py - validator for the text inside t◷( ... ): a closed subset of ISO 8601-1:2004, extended format only.

  date         YYYY | YYYY-MM | YYYY-MM-DD                         (digits 0-9 only; year 0000 is allowed)
  week         YYYY-Www | YYYY-Www-D                              (D = 1 Monday .. 7 Sunday; 01..52 or 01..53)
  time of day  Thh:mm | Thh:mm:ss [zone]                          (no date)
  instant      date-or-week-date 'T' hh:mm[:ss] [zone]            (hh 00-23, or 24:00 / 24:00:00 for the end of a day)
  zone         Z | +hh | +hh:mm | -hh | -hh:mm                    (hh 00-23, mm 00-59)
  duration     PnYnMnDTnHnMnS (any components in this order, at least one) | PnW (alone)
  interval     start/end | start/duration | duration/end           (start, end: date, week date or instant)
  repeat       R/ or Rn/ (n = 1 or more) followed by an interval or a duration

It is narrower than the standard on purpose. Refused although ISO 8601 has them or leaves them open:
  - the basic format (20261101), names (noon, Friday), 'now', fractions of a second or of a duration component;
  - the leap second (second 60): write 23:59:59, or the next 00:00;
  - a minus-zero zone (-00, -00:00): write Z or +00:00;
  - an interval whose two ends are different forms (a date with an instant, a date with a week date, a year with a month,
    a month with a day) or whose end is before its start (checked when both ends have a zone, or neither has);
  - a repeat with count 0; a time of day (no date) as an end of an interval.
Everything this module accepts is valid ISO 8601-1:2004 text in the extended format.

Returns (type, None) when valid, (None, message) when not. Types: date, week, tod, instant, duration, interval, repeat.
No imports besides re: the calendar arithmetic is done here, so that year 0000 works and no locale or library is involved.
"""
import re

_A = re.ASCII
_ZONE = r'(?P<z>Z|[+-](?:[01][0-9]|2[0-3])(?::[0-5][0-9])?)'
_TIME = r'(?P<h>[01][0-9]|2[0-4]):(?P<mi>[0-5][0-9])(?::(?P<s>[0-5][0-9]))?'
_RE_DATE = re.compile(r'(?P<y>[0-9]{4})(?:-(?P<mo>[0-9]{2})(?:-(?P<d>[0-9]{2}))?)?', _A)
_RE_WEEK = re.compile(r'(?P<y>[0-9]{4})-W(?P<w>[0-9]{2})(?:-(?P<wd>[1-7]))?', _A)
_RE_TOD = re.compile(r'T' + _TIME + _ZONE + '?', _A)
_RE_INST = re.compile(r'(?:(?P<y>[0-9]{4})-(?P<mo>[0-9]{2})-(?P<d>[0-9]{2})|(?P<wy>[0-9]{4})-W(?P<w>[0-9]{2})-(?P<wd>[1-7]))T'
                      + _TIME + _ZONE + '?', _A)
_RE_DUR = re.compile(r'P(?:([0-9]+)Y)?(?:([0-9]+)M)?(?:([0-9]+)D)?(?:T(?:([0-9]+)H)?(?:([0-9]+)M)?(?:([0-9]+)S)?)?', _A)
_RE_WDUR = re.compile(r'P[0-9]+W', _A)
_RE_REPEAT = re.compile(r'R([0-9]*)/(.+)', _A | re.DOTALL)


# ---- calendar arithmetic (proleptic Gregorian calendar, as ISO 8601 uses it; day 0 = 1970-01-01) ----
def _isleap(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

def _dim(y, m):
    return (31, 29 if _isleap(y) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)[m - 1]

def _dfc(y, m, d):
    """days from civil (Howard Hinnant's algorithm); works for year 0 and below"""
    y -= m <= 2
    era = y // 400
    yoe = y - era * 400
    doy = (153 * (m - 3 if m > 2 else m + 9) + 2) // 5 + d - 1
    doe = yoe * 365 + yoe // 4 - yoe // 100 + doy
    return era * 146097 + doe - 719468

def _dow(days):
    """ISO weekday of a day number: 1 Monday .. 7 Sunday (1970-01-01 was a Thursday)"""
    return (days + 3) % 7 + 1

def _weeks(y):
    """53 when 1 January or 31 December is a Thursday, else 52"""
    return 53 if _dow(_dfc(y, 1, 1)) == 4 or _dow(_dfc(y, 12, 31)) == 4 else 52

def _week_days(y, w, d):
    """day number of ISO week date y-Www-d (week 1 is the week with 4 January)"""
    jan4 = _dfc(y, 1, 4)
    return jan4 - (_dow(jan4) - 1) + (w - 1) * 7 + (d - 1)


# ---- one piece of a time text ----
def _clock(g):
    """(seconds since 00:00, offset in minutes or None, zoned) from the named groups h, mi, s, z; None if refused"""
    h, mi = int(g['h']), int(g['mi'])
    s = int(g['s']) if g['s'] is not None else 0
    if h == 24 and (mi != 0 or s != 0): return None
    z = g['z']
    if z is None: return h * 3600 + mi * 60 + s, None, False
    if z == 'Z': return h * 3600 + mi * 60 + s, 0, True
    if z in ('-00', '-00:00'): return None
    off = (int(z[1:3]) * 60 + (int(z[4:6]) if len(z) > 3 else 0)) * (-1 if z[0] == '-' else 1)
    return h * 3600 + mi * 60 + s, off, True

def _piece(s):
    """-> dict(kind, form, key, zoned) for one date, week date, time of day, instant or duration; None if not valid.
    key orders pieces of the same form: the start of the period (days), or for an instant seconds in UTC when it has a zone."""
    m = _RE_INST.fullmatch(s)
    if m:
        g = m.groupdict()
        if g['y'] is not None:
            y, mo, d = int(g['y']), int(g['mo']), int(g['d'])
            if not (1 <= mo <= 12 and 1 <= d <= _dim(y, mo)): return None
            days = _dfc(y, mo, d)
        else:
            y, w, d = int(g['wy']), int(g['w']), int(g['wd'])
            if not 1 <= w <= _weeks(y): return None
            days = _week_days(y, w, d)
        c = _clock(g)
        if c is None: return None
        sod, off, zoned = c
        return {'kind': 'instant', 'form': ('instant',), 'key': days * 86400 + sod - (off or 0) * 60, 'zoned': zoned}
    m = _RE_TOD.fullmatch(s)
    if m:
        c = _clock(m.groupdict())
        if c is None: return None
        return {'kind': 'tod', 'form': ('tod',), 'key': c[0] - (c[1] or 0) * 60, 'zoned': c[2]}
    m = _RE_WEEK.fullmatch(s)
    if m:
        y, w = int(m.group('y')), int(m.group('w'))
        if not 1 <= w <= _weeks(y): return None
        wd = m.group('wd')
        return {'kind': 'week', 'form': ('week', wd is not None), 'key': _week_days(y, w, int(wd) if wd else 1), 'zoned': False}
    m = _RE_DATE.fullmatch(s)
    if m:
        y = int(m.group('y'))
        mo, d = m.group('mo'), m.group('d')
        if mo is not None and not 1 <= int(mo) <= 12: return None
        if d is not None and not 1 <= int(d) <= _dim(y, int(mo)): return None
        return {'kind': 'date', 'form': ('date', 1 + (mo is not None) + (d is not None)),
                'key': _dfc(y, int(mo) if mo else 1, int(d) if d else 1), 'zoned': False}
    if _RE_WDUR.fullmatch(s): return {'kind': 'duration', 'form': ('duration',), 'key': None, 'zoned': False}
    m = _RE_DUR.fullmatch(s)
    if m and any(g is not None for g in m.groups()) and not s.endswith('T'):
        return {'kind': 'duration', 'form': ('duration',), 'key': None, 'zoned': False}
    return None


# ---- the whole text ----
def validate(text):
    if not isinstance(text, str) or text == '': return None, 'empty time text'
    if any(c.isspace() for c in text): return None, 'a space (or other white space) inside the time text'
    rep = _RE_REPEAT.fullmatch(text)
    if rep:
        if rep.group(1) and int(rep.group(1)) == 0: return None, 'a repeat count must be 1 or more'
        t, msg = validate(rep.group(2))
        if t in ('interval', 'duration'): return 'repeat', None
        return None, msg if msg is not None else 'a repeat needs an interval or a duration after R/'
    if '/' in text:
        parts = text.split('/')
        if len(parts) != 2: return None, 'an interval has two parts: start/end, start/duration or duration/end'
        a, b = _piece(parts[0]), _piece(parts[1])
        if a is None or b is None: return None, 'a part of the interval is not a valid ISO 8601 date, week date, instant or duration'
        if a['kind'] == 'duration' and b['kind'] == 'duration': return None, 'an interval cannot be two durations'
        if 'tod' in (a['kind'], b['kind']): return None, 'a time of day without a date cannot bound an interval'
        if a['kind'] != 'duration' and b['kind'] != 'duration':
            if a['form'] != b['form']:
                return None, 'the two ends of an interval must be the same form (two years, two months, two days, two week dates or two instants)'
            if a['zoned'] == b['zoned'] and b['key'] < a['key']: return None, 'the end of the interval is before its start'
        return 'interval', None
    p = _piece(text)
    if p is None:
        why = 'not a valid ISO 8601 date, week, time of day, instant or duration (extended format only)'
        if re.search(r':60(?![0-9])', text): why += '; the leap second (second 60) is not accepted'
        if re.search(r'-00(?::00)?$', text) and 'T' in text: why += '; a minus-zero zone is not accepted: write Z or +00:00'
        return None, why
    return p['kind'], None

def has_zone(text):
    """True if every instant and every time of day in the text carries a zone (Z, +hh or +hh:mm)"""
    rep = _RE_REPEAT.fullmatch(text)
    for piece in (rep.group(2) if rep else text).split('/'):
        p = _piece(piece)
        if p is not None and p['kind'] in ('instant', 'tod') and not p['zoned']: return False
    return True

if __name__ == '__main__':
    tests = ['2026-11-01T02:00+05:30', 'T12:00', 'PT1H', '2026-W44-5', '2026-11-06', '2026-W43', '2026-02-30', '2026-W54', 'P6W', 'P1W2D',
             '2026-11-01T16:20/PT10M', 'R/T02:00/P1D', 'R5/2026-11-01T14:00:00Z/P1D', 'noon', '20261101', '2026-11-01T25:00', 'PT', 'P', '2026-11-01 02:00', '2026-11-01T24:00Z',
             '2026-11-01/2026-11-07', 'P1D/P2D', '2026-11-01T16:20+05', '0000-W01', '2026-11-06/2026-11-01', '2026-11-01T24:00:30', '2016-12-31T23:59:60Z']
    for t in tests: print('%-34s %s' % (t, validate(t)))
