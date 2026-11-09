#!/usr/bin/env python3
"""Checker for the SILEX-0 symbol edition (an extra tool, not part of the language).

It learns the language from the guide itself: the roots and their places from
section 6, the packs from section 7. It needs only Python 3 (no packages). Its
name carries no version: give it the guide you want it to read.

    python3 silex_check.py GUIDE.md
        Checks the guide against its own rules: tables, root and pack counts,
        the claims the text makes about itself, and every fenced silex /
        silex-bad example in the file (each must give the verdict written in
        its comment).

    python3 silex_check.py GUIDE.md --messages FILE
        Checks a conversation. FILE holds the messages in the order they were
        sent, with a line of --- between messages. If FILE has fenced code
        blocks (``` ... ```), only their contents are read, all as one
        conversation (blocks tagged silex-bad are skipped).
        Prints each header or line that is not ok, with its verdict (section 9
        of the guide), and a count. The exit code is 1 if anything is wrong.

    python3 silex_check.py GUIDE.md --blocks FILE
        Checks every fenced silex / silex-bad block of FILE as a conversation
        of its own, like the examples of the guide. Use it for the practice
        answers of the guide's practice set.

Add -v to print every header and line. It judges form only: whether a line is
well formed in SILEX-0, not whether it is true or wise.

Since guide 0.8s: a line  ⊨(N,nln,M)  is checked against the number of lines of
message M (E-COUNT); a gloss that breaks the hygiene rule is reported with the
substitute from the table in section 3 of the guide; and in a conversation a
failing line that its own sender takes back later with ⌫ is printed as retracted
and is not counted as a problem. Older guides still work: without the table in
section 3 there is no substitute to name.

Since guide 0.9s: the first place of ≋ may name a word in scope (kind Wd: one flag
for every line that uses the word), and ⚂ may take a third place, the condition:
⚂(P,n,Q). The checker learns both from the root tables of the guide you give it,
so an older guide still refuses them.

Since guide 0.10s: a formula is parsed as section 8 describes it (E-MATH). A missing operator
('2x+1'), a character that is not formula text ('2**3'), two comparisons in one claim ('1<2<3'),
a function without its brackets ('sqrt 16') or with the wrong number of places, and a chain of
=> or <=> without brackets are refused, and so is a number where a claim is needed and the reverse. A free name,
or a call of the writer's own function, may stand for a number or for a claim: section 8 does not say which.
Before 0.10s only brackets and characters were tested.

AI changes (A, 10 Nov 2026), taken into 0.10s: three small aids for a conversation that people
relay by hand. They add no rule to the language, and they change no verdict except the last one:
  - an unknown word (E-LEX) says where it is defined, in an earlier message of the
    conversation or in a pack, and which ⇩ would bring it in;
  - a wrong line count (E-COUNT) says which way it is wrong: lines after the count line
    (a tail that came from another message), lines lost, or lines added;
  - a message that has lnrl in scope by an import must carry its own count line ⊨(N,nln,M)
    (a sender who imports the message that defines lnrl is taken to follow it), so a message
    that was cut short is caught even when the cut took the count line itself.
"""
import re
import sys
import io
import argparse
import contextlib
import datetime
import textwrap
import ast as pyast
from collections import defaultdict, Counter

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

ap = argparse.ArgumentParser(description='Checker for the SILEX-0 symbol edition.',
                             epilog='See the top of this file for the three ways to run it.')
ap.add_argument('doc', metavar='GUIDE', help='the SILEX-0 guide (for example SILEX-0-GRAMMAR-0_10s.md)')
ap.add_argument('--messages', metavar='FILE', help='check one conversation')
ap.add_argument('--blocks', metavar='FILE', help='check each fenced silex block of FILE on its own')
ap.add_argument('-v', action='store_true', help='print every header and line')
A = ap.parse_args()
A.atoms, A.label, A.packname, A.serial_required, A.agent1 = 'symbols', 'class', True, True, True
REPORT = bool(A.messages)
BADTAG = '   <-- problem'

_redir = None
if A.messages or A.blocks:
    _redir = contextlib.redirect_stdout(io.StringIO())   # the guide's own checks stay quiet
    _redir.__enter__()

TEXT = open(A.doc, encoding='utf-8').read()
LINES = TEXT.split('\n')
for _n in (1, 2, 6, 7, 10):
    if not any(l.startswith('## %d.' % _n) for l in LINES):
        sys.exit('This does not look like the SILEX-0 symbol-edition guide (section %d not found). Give the guide file first.' % _n)
PROBLEMS = []


def problem(where, msg):
    PROBLEMS.append((where, msg))
    print('  PROBLEM [%s] %s' % (where, msg))


# ---------------------------------------------------------------- structure
def heads():
    return [(i, l) for i, l in enumerate(LINES) if l.startswith('## ')]


def section_range(num):
    hs = heads()
    for n, (i, l) in enumerate(hs):
        if re.match(r'## %s\.' % num, l):
            return i, (hs[n + 1][0] if n + 1 < len(hs) else len(LINES))
    raise KeyError(num)


def split_row(line):
    s = line.strip()
    s = s[1:-1] if s.startswith('|') and s.endswith('|') else s
    cells, cur, incode = [], '', False
    for ch in s:
        if ch == '`':
            incode = not incode
            cur += ch
        elif ch == '|' and not incode:
            cells.append(cur.strip())
            cur = ''
        else:
            cur += ch
    cells.append(cur.strip())
    return cells


print('== GUIDE')
print('  ' + next((l for l in LINES if l.startswith('Version ')), 'no version line found'))
print('== TABLES (markdown validity)')
i = 0
ntables = 0
while i < len(LINES):
    if LINES[i].startswith('|'):
        j = i
        while j < len(LINES) and LINES[j].startswith('|'):
            j += 1
        block = LINES[i:j]
        ntables += 1
        hdr = split_row(block[0])
        if len(block) < 2 or not re.match(r'^\|\s*:?-{3,}', block[1]):
            problem('line %d' % (i + 1), 'table without delimiter row')
        else:
            d = split_row(block[1])
            if len(d) != len(hdr):
                problem('line %d' % (i + 2), 'delimiter row has %d cells, header has %d' % (len(d), len(hdr)))
        for k, row in enumerate(block[2:], start=i + 3):
            c = split_row(row)
            if len(c) != len(hdr):
                problem('line %d' % k, 'row has %d cells, header has %d' % (len(c), len(hdr)))
        i = j
    else:
        i += 1
print('  tables seen: %d' % ntables)


# ---------------------------------------------------------------- roots
def parse_slot(tok):
    mode = 'one'
    if tok.startswith('*'):
        mode = 'plus'
        tok = tok[1:]
    if tok.startswith('['):
        close = tok.index(']')
        inner, rest = tok[1:close], tok[close + 1:]
        if inner.endswith('…') or rest == '…':
            mode = 'star'
            inner = inner.rstrip('…')
        else:
            mode = 'opt'
        tok = inner
    elif tok.endswith('…'):
        mode = 'plus'
        tok = tok[:-1]
    return {'kinds': set(tok.split('/')), 'mode': mode}


def parse_sig(s):
    left, right = s.split('→')
    return {'slots': [parse_slot(t) for t in left.split()], 'right': right.strip(), 'raw': s.strip()}


ROOTS = {}
ROWS = []
a6, b6 = section_range(6)
for k in range(a6, b6):
    l = LINES[k]
    if l.startswith('| `'):
        c = split_row(l)
        if len(c) != 4:
            continue
        sym = c[0].strip('`')
        sigs = [parse_sig(x) for x in re.findall(r'`([^`]*)`', c[2])]
        ROWS.append((sym, c[1], sigs, c[3], k + 1))
        if sym in ROOTS:
            problem('line %d' % (k + 1), 'duplicate root symbol %r' % sym)
        ROOTS[sym] = {'name': c[1], 'sigs': sigs, 'says': c[3]}

print('== ROOTS')
print('  rows: %d' % len(ROWS))
composite = [r for r in ROWS if ',' in r[1]]
print('  composite-name rows (extra forms): %s' % [r[0] for r in composite])
ROOT_NAMES = {r[1] for r in ROWS if ',' not in r[1]}
print('  root names (reserved words): %d' % len(ROOT_NAMES))
ascii_roots = sorted(s for s in ROOTS if len(s) == 1 and s.isascii())
print('  ASCII root symbols: %s (%d)' % (' '.join(ascii_roots), len(ascii_roots)))
for s in ROOTS:
    if s.startswith('f('):
        continue
    if len(s) != 1:
        problem('root', 'symbol %r is not one code point' % s)
names = Counter(r[1] for r in ROWS)
for n_, c_ in names.items():
    if c_ > 1:
        problem('root', 'name %r used by %d rows' % (n_, c_))
print('  symbols that are not one code point: %s' % [s for s in ROOTS if len(s) != 1])
for s in ROOTS:
    if len(s) == 1 and not s.isascii():
        import unicodedata
        cat = unicodedata.category(s)
        if cat in ('Mn', 'Me', 'Cf'):
            problem('root', 'symbol %r (U+%04X) is a combining/format character' % (s, ord(s)))
minus = [s for s in ROOTS if s in ('−', '-', '–')]
for bad_sym in ('−', '※', '✦'):
    if bad_sym in ROOTS:
        problem('root', 'symbol %r should not be a root in the symbol edition' % bad_sym)
for atom_ch in '~*!_':
    if atom_ch in ROOTS:
        problem('root', 'atom %r is also a root' % atom_ch)
print('  minus symbol code points: %s' % ['U+%04X' % ord(m) for m in minus])

# ---------------------------------------------------------------- packs
PACKS = {}
a7, b7 = section_range(7)
cur = None
for k in range(a7, b7):
    l = LINES[k]
    m = re.match(r'### (\w+):', l)
    if m:
        cur = m.group(1)
        PACKS[cur] = {}
        continue
    if cur and l.startswith('| `'):
        c = split_row(l)
        if len(c) < 4:
            problem('line %d' % (k + 1), 'pack row with %d cells' % len(c))
            continue
        PACKS[cur][c[0].strip('`')] = {'reading': c[1], 'kind': c[2], 'gloss': c[3]}
print('== PACKS')
for p, d in PACKS.items():
    print('  %s: %d terms' % (p, len(d)))
READING = set()
for p, d in PACKS.items():
    for code, v in d.items():
        READING.add(v['reading'])
print('  reading names: %d' % len(READING))
PACK_NAMES = set(PACKS)

KIND_OF_CLASS = {'o': 'Th', 'g': 'Gr', 'a': 'Ac', 'n': 'Nu', 'c': 'Cr', 'q': 'Cl', 't': 'Tm', 'd': 'Du'}
AN = set()
ATOMS = set()   # the atoms are the symbols ~ * ! _ and are not words
LABEL_RE = re.compile(r'[ogantcqd]\d+') if A.label == 'class' else re.compile(r'[a-z]\d+')
BANNED = set('''i me my mine myself you your yours we our ours us this here today tonight tomorrow
yesterday own that these those such same next last previous earlier later above below then soon
recently currently already again'''.split())
BRACE_OK = re.compile(r'[A-Z][a-z]*|\d+(?:\.\d+)?|\d{4}-\d{2}-\d{2}(?:T[\d:]+)?|P[\dYMWDTHS.]+|[A-Z][a-z]*\d+(?:\.\d+)?')
if A.agent1:
    BRACE_OK = re.compile(r'[A-Z]|\d+(?:\.\d+)?|\d{4}-\d{2}-\d{2}(?:T[\d:]+)?|P[\dYMWDTHS.]+|[A-Z]\d+(?:\.\d+)?')

# what to write instead of each banned word: a table in section 3 of the guide (0.8s and later)
SUBS = {}
try:
    a3, b3 = section_range(3)
    for k in range(a3, b3):
        if LINES[k].startswith('| Banned words'):
            for l in LINES[k + 2:b3]:
                if not l.startswith('| `'):
                    break
                c = split_row(l)
                sub = re.match(r'`([^`]+)`', c[1]) if len(c) > 1 else None
                for w in re.findall(r'`([a-z]+)`', c[0]):
                    if w in SUBS:
                        problem('claims', 'banned word %s is in the substitute table twice' % w)
                    SUBS[w] = sub.group(1) if sub else None
            break
except KeyError:
    pass
if SUBS and set(SUBS) != BANNED:
    problem('claims', 'the substitute table of section 3 and the banned words differ: %s' % sorted(set(SUBS) ^ BANNED))

for p, d in PACKS.items():
    for code, v in d.items():
        w = v['gloss'].split()
        if len(w) > 6:
            problem('pack %s' % p, '%s gloss has %d words' % (code, len(w)))
        low = set(re.findall(r"[a-z']+", v['gloss'].lower()))
        if 'the' in low or (BANNED & low):
            problem('pack %s' % p, '%s gloss uses a banned word: %s' % (code, sorted(({'the'} & low) | (BANNED & low))))
        if not re.fullmatch(r'[a-z][a-z0-9]{1,5}', code):
            problem('pack %s' % p, 'code %s has a bad shape' % code)
        if code in ROOT_NAMES or code in ATOMS or LABEL_RE.fullmatch(code) or code in READING and code != v['reading']:
            problem('pack %s' % p, 'code %s is reserved or label-shaped' % code)
        if v['kind'] not in ('Cr', 'Ac', 'Th', 'Gr'):
            problem('pack %s' % p, 'code %s has odd kind %s' % (code, v['kind']))
        if v['kind'] == 'Cr' and not re.match(r'^(is|has) ', v['gloss']):
            pass  # reported in aggregate below
allcodes = Counter(c for d in PACKS.values() for c in d)
for c_, n_ in allcodes.items():
    if n_ > 1:
        problem('pack', 'code %s appears in several packs' % c_)
non_is = [(p, c) for p, d in PACKS.items() for c, v in d.items()
          if v['kind'] == 'Cr' and not re.match(r'^(is|has) ', v['gloss'])]
print('  criterion glosses that do not read "is ..." or "has ...": %d of %d' % (
    len(non_is), sum(1 for d in PACKS.values() for v in d.values() if v['kind'] == 'Cr')))



# ---------------------------------------------------------------- what the text claims about itself
WORDNUM = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}


def _num(w):
    w = w.lower()
    return int(w) if w.isdigit() else WORDNUM[w]


def claim(pattern, actual, what):
    found = re.findall(pattern, TEXT)
    if not found:
        problem('claims', 'no statement found for %s' % what)
        return
    for f in found:
        if _num(f) != actual:
            problem('claims', '%s: the text says %s, the tables give %d' % (what, f, actual))


print('== CLAIMS')
claim(r'There are (\d+) roots', len(ROOT_NAMES), 'number of roots')
claim(r'the tables have (\d+) rows', len(ROWS), 'number of table rows')
claim(r'\*\*(\w+) ASCII symbols\*\* are roots', len(ascii_roots), 'number of ASCII root symbols')
claim(r'one of the (\d+) root names', len(ROOT_NAMES), 'root names in the term rule')
claim(r'one of the (\d+) reading names', len(READING), 'reading names')
for pk, d in PACKS.items():
    claim(r'### %s:[^\n]*\((\d+) terms\)' % pk, len(d), 'size of pack %s' % pk)

# kinds: every kind used in a signature is declared, and every declared kind is used
SIGKINDS = set()
for sym, name, sigs, says, ln in ROWS:
    for sg in sigs:
        for sl in sg['slots']:
            SIGKINDS |= sl['kinds']
        r = sg['right']
        if r not in ('=1', '=2'):
            SIGKINDS.add(r)
SIGKINDS -= {'k', 'k"gloss"'}   # the class-letter notation of the term root, not kinds
a2, b2 = section_range(2)
TABLEKINDS = set()
for k_ in range(a2, b2):
    if LINES[k_].startswith('| `'):
        TABLEKINDS.add(split_row(LINES[k_])[0].strip('`'))
more_m = re.search(r'(\w+) more kinds appear only in the root tables:(.*?)The written form', TEXT, re.S)
MOREKINDS = set(re.findall(r'`([A-Z][a-z]?)` \(', more_m.group(2))) if more_m else set()
if more_m and _num(more_m.group(1)) != len(MOREKINDS):
    problem('claims', 'more kinds: the text says %s, it lists %d' % (more_m.group(1), len(MOREKINDS)))
a1, b1 = section_range(1)
ATOMKINDS = set()
for k_ in range(a1, b1):
    c_ = split_row(LINES[k_]) if LINES[k_].startswith('| `') else []
    if len(c_) == 3 and c_[0].strip('`') in ('~', '*', '!', '_'):
        ATOMKINDS.add(c_[1])
DECLARED = TABLEKINDS | MOREKINDS
print('  kinds in signatures: %s' % sorted(SIGKINDS))
print('  kinds declared: %s' % sorted(DECLARED))
if SIGKINDS - DECLARED:
    problem('claims', 'kinds used but not declared: %s' % sorted(SIGKINDS - DECLARED))
if DECLARED - SIGKINDS - ATOMKINDS:
    problem('claims', 'kinds declared but never used: %s' % sorted(DECLARED - SIGKINDS - ATOMKINDS))


# ---------------------------------------------------------------- errors / kinds
class SErr(Exception):
    def __init__(self, code, msg=''):
        Exception.__init__(self, code + ' ' + msg)
        self.code = code
        self.msg = msg


VALUEKINDS = {'Ag', 'Th', 'Gr', 'Ac', 'Nu', 'Tm', 'Du', 'Cr', 'Cl', 'Rf', 'LV', 'Un'}


def kbase(k):
    return k.split(':')[0]


def fits(k, S):
    k = kbase(k)
    if k == 'Un':
        return True
    if 'Va' in S and k in VALUEKINDS:
        return True
    if k in S:
        return True
    if k == 'Ag' and 'Th' in S:
        return True
    if k in ('Cl', 'Q') and 'Ln' in S:
        return True
    if k == 'LV' and S & {'Nu', 'Tm', 'Du', 'Gr', 'Th', 'Cr'}:
        return True
    if k == 'Rf' and S & {'Cl', 'Q', 'Ln', 'Va'}:
        return True
    if 'X' in S and k in ('Cl', 'Ac', 'Ln', 'Q'):
        return True
    if k == 'St' and 'Rw' in S:
        return True
    return False


def match_slots(slots, argk):
    def rec(i, j):
        if i == len(slots):
            return j == len(argk)
        s = slots[i]
        mode = s['mode']
        if mode == 'one':
            return j < len(argk) and fits(argk[j], s['kinds']) and rec(i + 1, j + 1)
        if mode == 'opt':
            if j < len(argk) and fits(argk[j], s['kinds']) and rec(i + 1, j + 1):
                return True
            return rec(i + 1, j)
        mn = 1 if mode == 'plus' else 0
        maxn = 0
        while j + maxn < len(argk) and fits(argk[j + maxn], s['kinds']):
            maxn += 1
        for take in range(maxn, mn - 1, -1):
            if rec(i + 1, j + take):
                return True
        return False
    return rec(0, 0)


def arity_ok(sig, n):
    mn = sum(1 for s in sig['slots'] if s['mode'] in ('one', 'plus'))
    unbounded = any(s['mode'] in ('plus', 'star') for s in sig['slots'])
    mx = 10 ** 6 if unbounded else sum(1 for s in sig['slots'] if s['mode'] in ('one', 'opt'))
    return mn <= n <= mx


# ---------------------------------------------------------------- lexing
TIME_PART = r'\d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:Z|[+-]\d{2}:\d{2})?)?'
TIME_RE = re.compile(TIME_PART + r'(?:/' + TIME_PART + r')?|\d{8}T\d{4}(?:\d{2})?(?:Z|[+-]\d{4})?')
DUR_RE = re.compile(r'P(?:\d+(?:\.\d+)?[YMWD])*(?:T(?:\d+(?:\.\d+)?[HMS])*)?')
NUM_RE = re.compile(r'-?\d+(?:\.\d+)?')
ROOTCHARS = {s for s in ROOTS if len(s) == 1}


def valid_one_time(s):
    m = re.fullmatch(r'(\d{4})-(\d{2})-(\d{2})(?:T(\d{2}):(\d{2})(?::(\d{2})(?:\.\d+)?)?(Z|[+-]\d{2}:\d{2})?)?', s)
    if m:
        try:
            datetime.date(int(m[1]), int(m[2]), int(m[3]))
        except ValueError:
            return False
        if m[4] is not None and not (int(m[4]) <= 23 and int(m[5]) <= 59):
            return False
        if m[6] is not None and int(m[6]) > 59:
            return False
        if m[7] and m[7] != 'Z':
            if int(m[7][1:3]) > 14 or int(m[7][4:6]) > 59:
                return False
        return True
    m = re.fullmatch(r'(\d{4})(\d{2})(\d{2})T(\d{2})(\d{2})(\d{2})?(Z|[+-]\d{4})?', s)
    if m:
        try:
            datetime.date(int(m[1]), int(m[2]), int(m[3]))
        except ValueError:
            return False
        return int(m[4]) <= 23 and int(m[5]) <= 59 and (m[6] is None or int(m[6]) <= 59)
    return False


def valid_time(s):
    return all(valid_one_time(p) for p in s.split('/'))


def valid_dur(s):
    return len(s) > 1 and not s.endswith('T') and bool(DUR_RE.fullmatch(s)) and re.search(r'\d', s) is not None


def strip_comment(line):
    q = None
    i = 0
    while i < len(line):
        c = line[i]
        if q:
            if c == q:
                if q == '"' and line[i + 1:i + 2] == '"':
                    i += 2
                    continue
                q = None
        else:
            if c in '"\'':
                q = c
            elif c == '#' and line[i + 1:i + 2] != '(':
                return line[:i], line[i + 1:]
        i += 1
    return line, ''


def read_string(s, i):
    n = len(s)
    j = i + 1
    buf = []
    while True:
        if j >= n:
            raise SErr('E-SYN', 'open quote')
        if s[j] == '"':
            if s[j + 1:j + 2] == '"':
                buf.append('"')
                j += 2
                continue
            break
        buf.append(s[j])
        j += 1
    return ''.join(buf), j + 1


def tokenize(s):
    toks = []
    i = 0
    n = len(s)
    while i < n:
        c = s[i]
        if c.isspace():
            i += 1
            continue
        if c == '"':
            text, i = read_string(s, i)
            toks.append(('str', text))
            continue
        if c == "'":
            j = s.find("'", i + 1)
            if j < 0:
                raise SErr('E-SYN', 'open formula quote')
            toks.append(('formula', s[i + 1:j]))
            i = j + 1
            continue
        if c in '(),':
            toks.append((c, c))
            i += 1
            continue
        if c.isdigit() or (c == '-' and s[i + 1:i + 2].isdigit()):
            m = TIME_RE.match(s, i) if c.isdigit() else None
            if m and not s[m.end():m.end() + 1].isalnum():
                toks.append(('time', m.group(0)))
                i = m.end()
                continue
            m = NUM_RE.match(s, i)
            if s[m.end():m.end() + 1].isalpha() or s[m.end():m.end() + 1] == '.':
                raise SErr('E-LEX', 'number followed by letters near %r' % s[i:i + 12])
            toks.append(('num', m.group(0)))
            i = m.end()
            continue
        if c == 'P' and (s[i + 1:i + 2].isdigit() or s[i + 1:i + 2] == 'T'):
            m = DUR_RE.match(s, i)
            if m and valid_dur(m.group(0)) and not s[m.end():m.end() + 1].isalnum():
                toks.append(('dur', m.group(0)))
                i = m.end()
                continue
        if c.isupper():
            m = re.match(r'[A-Z][A-Za-z]*', s[i:])
            word = m.group(0)
            if not re.fullmatch(r'[A-Z][a-z]*', word):
                raise SErr('E-LEX', 'bad agent name %s' % word)
            if len(word) > 1:
                raise SErr('E-LEX', 'agent name %s is not one capital letter' % word)
            j = i + len(word)
            m2 = re.match(r'\d+(?:\.\d+)?', s[j:])
            if m2 and A.agent1 and len(word) > 1:
                raise SErr('E-LEX', '%s cannot carry a serial' % word)
            if m2:
                d = m2.group(0)
                j += len(d)
                if '.' in d:
                    a_, b_ = d.split('.')
                    toks.append(('line', word + a_, int(b_)))
                else:
                    toks.append(('msg', word + d))
            else:
                toks.append(('agent', word))
            i = j
            continue
        if c in '~*!':
            if s[i + 1:i + 2] == '(':
                raise SErr('E-LEX', 'atom %s followed by a bracket' % c)
            toks.append(('atom', c))
            i += 1
            continue
        if c == '_':
            if s[i + 1:i + 2].isalnum() or s[i + 1:i + 2] in ('_', '('):
                raise SErr('E-LEX', 'underscore word or atom with a bracket')
            toks.append(('us', '_'))
            i += 1
            continue
        if c.isalpha() and c.islower() and c.isascii():
            m = re.match(r'[a-z][a-z0-9_]*', s[i:])
            word = m.group(0)
            j = i + len(word)
            if len(word) == 1 and s[j:j + 1] == '"':
                text, j2 = read_string(s, j)
                toks.append(('gloss', word, text))
                i = j2
                continue
            toks.append(('word', word))
            i = j
            continue
        if c in ROOTCHARS:
            if s[i + 1:i + 2] == '(':
                toks.append(('root', c))
                i += 1
                continue
            raise SErr('E-ARITY', 'root %s without bracket' % c)
        raise SErr('E-LEX', 'symbol %r (U+%04X) is not a root' % (c, ord(c)))
    return toks


def parse(toks):
    pos = [0]

    def peek():
        return toks[pos[0]] if pos[0] < len(toks) else None

    def take():
        t = toks[pos[0]]
        pos[0] += 1
        return t

    def arglist():
        args = []
        if peek() and peek()[0] == ')':
            raise SErr('E-ARITY', 'empty bracket')
        while True:
            args.append(expr())
            t = peek()
            if t is None:
                raise SErr('E-SYN', 'bracket not closed')
            if t[0] == ',':
                take()
                continue
            if t[0] == ')':
                take()
                return args
            raise SErr('E-SYN', 'expected , or )')

    def expr():
        t = peek()
        if t is None:
            raise SErr('E-SYN', 'unexpected end')
        k = t[0]
        if k == 'root':
            take()
            lp = peek()
            if not lp or lp[0] != '(':
                raise SErr('E-ARITY', 'no bracket')
            take()
            return ('root', t[1], arglist())
        if k == 'word':
            take()
            nx = peek()
            if nx and nx[0] == '(':
                take()
                return ('func', t[1], arglist())
            return ('word', t[1])
        if k in ('str', 'formula', 'gloss', 'time', 'dur', 'num', 'agent', 'msg', 'line', 'us', 'atom'):
            take()
            return (k,) + tuple(t[1:])
        raise SErr('E-SYN', 'unexpected %r' % (t,))

    e = expr()
    if pos[0] != len(toks):
        raise SErr('E-SYN', 'extra tokens after expression')
    return e


# ---------------------------------------------------------------- messages
class Term:
    def __init__(self, kind, gloss, src):
        self.kind, self.gloss, self.src = kind, gloss, src


class Line:
    def __init__(self, raw, code, comment, expected):
        self.raw, self.code, self.comment, self.expected = raw, code, comment, expected
        self.ast = None
        self.err = None
        self.kind = None
        self.verdict = None


class Msg:
    pass


class Block:
    pass


def check_braces(t):
    i = 0
    while i < len(t):
        c = t[i]
        if c == '{':
            if t[i:i + 2] == '{{':
                i += 2
                continue
            j = t.find('}', i)
            if j < 0:
                raise SErr('E-QUOTE', 'open brace')
            if not BRACE_OK.fullmatch(t[i + 1:j]):
                raise SErr('E-QUOTE', 'bad brace {%s}' % t[i + 1:j])
            i = j + 1
            continue
        if c == '}':
            if t[i:i + 2] == '}}':
                i += 2
                continue
            raise SErr('E-QUOTE', 'stray }')
        i += 1


def check_text(text, limit):
    words = text.split()
    if len(words) > limit:
        raise SErr('E-BUDGET', '%d words > %d' % (len(words), limit))
    # brace references ({Me}, {A}, {12}, ...) stand in for the words the hygiene rule bans,
    # so they are removed before the scan; a bad brace is still caught by check_braces
    stripped = re.sub(r'\{\{|\}\}', ' ', text)
    stripped = re.sub(r'\{[^{}]*\}', ' ', stripped)
    low = re.findall(r"[a-z']+", stripped.lower())
    said = []
    if 'the' in low:
        said.append("'the' (leave it out)")
    bad = BANNED & set(low)
    if bad:
        said.append('context word ' + ', '.join(
            "'%s'%s" % (w, (' (write %s)' % SUBS[w]) if SUBS.get(w) else '') for w in sorted(bad)))
    if said:
        raise SErr('E-QUOTE', '; '.join(said))
    check_braces(text)


class Ctx:
    def __init__(self, msg, block):
        self.msg, self.block = msg, block
        self.stage = {}
        self.labels = []
        self.stage_new = 0
        self.stage_notes = 0


def lookup(name, ctx, mark=True):
    if name in ctx.stage:
        return ctx.stage[name]
    if name in ctx.msg.terms:
        t = ctx.msg.terms[name]
        if mark:
            ctx.msg.used.add(t.src)
        return t
    return None


def check_term_name(name, ctx):
    if not re.fullmatch(r'[a-z][a-z0-9]{1,5}', name):
        raise SErr('E-LEX', 'term %r has a bad shape' % name)
    if name in ROOT_NAMES or name in ATOMS or name in READING or LABEL_RE.fullmatch(name) \
            or (A.packname and name in PACK_NAMES):
        raise SErr('E-LEX', 'term %r is a reserved word' % name)
    if lookup(name, ctx, mark=False) or name in ctx.labels:
        raise SErr('E-REDEF', name)


# The formula grammar of section 8: numbers, names, + - * / ^ and round brackets; the formula
# functions below; one comparison in each claim; & | => <=> to join claims.
FML_FUNCS = {
    'sqrt': (1, 1), 'abs': (1, 1), 'exp': (1, 1), 'ln': (1, 1), 'floor': (1, 1), 'ceil': (1, 1),
    'sin': (1, 1), 'cos': (1, 1), 'tan': (1, 1), 'fact': (1, 1),
    'log': (2, 2), 'round': (2, 2), 'mod': (2, 2), 'gcd': (2, 2),
    'min': (1, None), 'max': (1, None),
    'sum': (4, 4), 'prod': (4, 4), 'int': (4, 4), 'd': (2, 2), 'lim': (3, 3),
}
FML_BINDER = {'sum': 1, 'prod': 1, 'int': 1, 'd': 1, 'lim': 1}   # the place that names the variable
FML_CONST = {'pi', 'e'}
FML_CMP = {'=', '!=', '<', '>', '<=', '>='}
FML_TOKEN = re.compile(r'(\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|([A-Za-z][A-Za-z0-9_]*)|(<=>|=>|<=|>=|!=|[-+*/^(),=<>&|])')


def fml_tokens(s):
    toks, pos = [], 0
    while True:
        while pos < len(s) and s[pos] == ' ':
            pos += 1
        if pos >= len(s):
            return toks
        m = FML_TOKEN.match(s, pos)
        if not m:
            if s[pos] == '.':
                raise SErr('E-MATH', 'a number has digits on both sides of its point (0.5, not .5)')
            if s[pos] == '!':
                raise SErr('E-MATH', "a '!' stands only in !=; write fact(n) for a factorial, and put ¬(…) round a claim for not")
            raise SErr('E-MATH', 'odd character %r' % s[pos])
        kind = 'num' if m.group(1) else 'name' if m.group(2) else 'op'
        toks.append((kind, m.group(0)))
        pos = m.end()


def ev_formula(s):
    if not s.strip() or s.count('(') != s.count(')'):
        raise SErr('E-MATH', 'brackets')
    if re.search(r"[^A-Za-z0-9_.+\-*/^(),=!<>&| ]", s):
        raise SErr('E-MATH', 'odd character')
    toks = fml_tokens(s)
    pos = [0]

    def peek():
        return toks[pos[0]] if pos[0] < len(toks) else None

    def is_op(*ops):
        t = peek()
        return t is not None and t[0] == 'op' and t[1] in ops

    def take():
        t = peek()
        if t is None:
            raise SErr('E-MATH', 'the formula ends too soon')
        pos[0] += 1
        return t

    # kinds: Nu a number, Cl a claim, Un a free name or a call of the writer's own function:
    # section 8 does not say what a free name stands for, so it may be a number or a claim.
    def num(t, what):
        if t not in ('Nu', 'Un'):
            raise SErr('E-MATH', 'a claim stands where a number is needed (%s)' % what)

    def claim(t, what):
        if t not in ('Cl', 'Un'):
            raise SErr('E-MATH', 'a number stands where a claim is needed (%s)' % what)

    def iff():
        t = imp()
        if is_op('<=>'):
            take()
            claim(t, '<=>')
            claim(imp(), '<=>')
            if is_op('<=>'):
                raise SErr('E-MATH', 'a chain of <=> needs brackets')
            return 'Cl'
        return t

    def imp():
        t = disj()
        if is_op('=>'):
            take()
            claim(t, '=>')
            claim(disj(), '=>')
            if is_op('=>'):
                raise SErr('E-MATH', 'a chain of => needs brackets')
            return 'Cl'
        return t

    def disj():
        t = conj()
        while is_op('|'):
            take()
            claim(t, '|')
            claim(conj(), '|')
        return t

    def conj():
        t = cmp_()
        while is_op('&'):
            take()
            claim(t, '&')
            claim(cmp_(), '&')
        return t

    def cmp_():
        t = total()
        if is_op(*FML_CMP):
            take()
            num(t, 'comparison')
            num(total(), 'comparison')
            if is_op(*FML_CMP):
                raise SErr('E-MATH', 'two comparisons in one claim')
            return 'Cl'
        return t

    def total():
        t = term()
        while is_op('+', '-'):
            take()
            num(t, '+ -')
            num(term(), '+ -')
            t = 'Nu'
        return t

    def term():
        t = unary()
        while is_op('*', '/'):
            take()
            num(t, '* /')
            num(unary(), '* /')
            t = 'Nu'
        return t

    def unary():                      # -x^2 is -(x^2); a second sign in a row is not allowed
        if is_op('-'):
            take()
            num(power(), 'minus')
            return 'Nu'
        return power()

    def power():                      # ^ groups to the right: 2^3^2 is 2^(3^2)
        t = atom()
        if is_op('^'):
            take()
            num(t, '^')
            num(unary(), '^')
            return 'Nu'
        return t

    def atom():
        t = take()
        kind, text = t
        if kind == 'num':
            return 'Nu'
        if kind == 'name':
            if is_op('('):
                take()
                args = []
                while True:
                    start = pos[0]
                    ty = iff()
                    bare = toks[start][1] if (pos[0] - start == 1 and toks[start][0] == 'name') else None
                    args.append((ty, bare))
                    if is_op(','):
                        take()
                        continue
                    break
                if not is_op(')'):
                    raise SErr('E-MATH', 'brackets')
                take()
                call(text, args)
                return 'Nu' if text in FML_FUNCS else 'Un'
            if text in FML_FUNCS and text != 'd':
                raise SErr('E-MATH', 'the function %s needs its brackets' % text)
            return 'Nu' if text in FML_CONST else 'Un'
        if text == '(':
            ty = iff()
            if not is_op(')'):
                raise SErr('E-MATH', 'brackets')
            take()
            return ty
        raise SErr('E-MATH', 'unexpected %s' % text)

    def call(name, args):
        if name in FML_CONST:
            raise SErr('E-MATH', '%s is a constant, not a function' % name)
        if name in FML_FUNCS:
            for ty, _ in args:
                num(ty, 'a place of %s' % name)
            lo, hi = FML_FUNCS[name]
            if len(args) < lo or (hi is not None and len(args) > hi):
                raise SErr('E-MATH', '%s takes %s place(s), not %d'
                           % (name, lo if lo == hi else 'at least %d' % lo, len(args)))
        if name in FML_BINDER and args[FML_BINDER[name]][1] is None:
            raise SErr('E-MATH', 'the place %d of %s must be a name' % (FML_BINDER[name] + 1, name))

    result = iff()
    if peek() is not None:
        raise SErr('E-MATH', 'an operator is missing before %s' % peek()[1])
    return 'Cl' if result == 'Cl' else 'Nu'


COUNT_GLOSS = 'is line count of'
LNRL_GLOSS = 'final line gives total line count'


def gloss_norm(tm):
    return ' '.join(((tm.gloss if tm else '') or '').lower().split())


def is_count_line(ln, m):
    """True if the line is  ⊨(N,nln,M)  with M the message itself (N is checked by check_count)."""
    top = ln.ast
    if not top or top[0] != 'root' or top[1] != '⊨' or len(top[2]) != 3:
        return False
    n, rel, tgt = top[2]
    if n[0] != 'num' or rel[0] != 'word' or tgt[0] != 'msg' or tgt[1] != m.name:
        return False
    return gloss_norm(m.terms.get(rel[1])) == COUNT_GLOSS


def check_count(top, ctx, at=None):
    """A claim alone on a line, ⊨(N,nln,M): N must be the number of lines of message M.
    The word is recognised by its gloss, so it works for the pack word and for a message-defined one.
    `at` is the number of this line in its message: it lets the error say which way the count is wrong."""
    if top[0] != 'root' or top[1] != '⊨' or len(top[2]) != 3:
        return
    n, rel, tgt = top[2]
    if n[0] != 'num' or rel[0] != 'word' or tgt[0] != 'msg':
        return
    tm = lookup(rel[1], ctx, mark=False)
    if not tm or ' '.join((tm.gloss or '').lower().split()) != COUNT_GLOSS:
        return
    m = ctx.block.by_name.get(tgt[1])
    if m is not None and float(n[1]) != len(m.lines):
        have, said, hint = len(m.lines), float(n[1]), ''
        if said == int(said):
            said = int(said)
            if tgt[1] == ctx.msg.name and at == said and said < have:
                hint = ('; line %d comes' % have if have == said + 1 else '; lines %d-%d come' % (said + 1, have)) + \
                    ' after its count line and may belong to another message'
            elif have < said:
                hint = '; %d line(s) lost?' % (said - have)
            elif have > said:
                hint = '; %d line(s) added?' % (have - said)
        raise SErr('E-COUNT', '%s has %d line(s), not %s%s' % (tgt[1], have, n[1], hint))


def check_msgref(name, ctx):
    if name not in ctx.block.by_name:
        raise SErr('E-REF', 'no message %s' % name)


def where_defined(name, ctx):
    """Where a word that is not in scope is defined: an earlier message of the conversation, or a pack.
    It only words the E-LEX message, as a hint; it changes no verdict."""
    found = []
    for m2 in ctx.block.msgs:
        if m2 is ctx.msg:
            break            # only what comes before this message can be imported by it
        if getattr(m2, 'name', None) and name in getattr(m2, 'defs', {}):
            found.append(m2.name)
    found += [p for p, d in PACKS.items() if name in d]
    return found


def unknown_msg(what, name, ctx):
    w = where_defined(name, ctx)
    if not w:
        return 'unknown %s %s' % (what, name)
    if len(w) == 1:
        return 'unknown %s %s (defined in %s: add ⇩(%s)?)' % (what, name, w[0], w[0])
    # two sources of one word must not both be imported (E-REDEF), so the hint names a choice
    return 'unknown %s %s (defined in %s: import one of them, not several)' % (what, name, ', '.join(w))


def ev_word(name, ctx):
    if name in ctx.labels:
        return 'LV'
    t = lookup(name, ctx)
    if t:
        return t.kind
    if LABEL_RE.fullmatch(name):
        raise SErr('E-NAME', name)
    raise SErr('E-LEX', unknown_msg('word', name, ctx))


def ev(node, ctx):
    t = node[0]
    if t == 'num':
        return 'Nu'
    if t == 'time':
        if not valid_time(node[1]):
            raise SErr('E-TIME', node[1])
        return 'Tm'
    if t == 'dur':
        return 'Du'
    if t == 'agent':
        return 'Ag'
    if t == 'msg':
        check_msgref(node[1], ctx)
        return 'Rf'
    if t == 'line':
        m = ctx.block.by_name.get(node[1])
        if not m or node[2] < 1 or node[2] > len(m.lines):
            raise SErr('E-REF', 'no line %s.%s' % (node[1], node[2]))
        k = m.lines[node[2] - 1].kind
        return 'Rf:' + k if k else 'Rf'
    if t in ('str', 'gloss'):
        raise SErr('E-ENGLISH', 'a quote outside a term')
    if t == 'formula':
        return ev_formula(node[1])
    if t == 'us':
        return 'Un'
    if t == 'atom':
        return 'Ag' if node[1] in '~*' else 'Tm'
    if t == 'word':
        return ev_word(node[1], ctx)
    if t == 'func':
        tm = lookup(node[1], ctx)
        if not tm:
            raise SErr('E-LEX', unknown_msg('function/word', node[1], ctx))
        if tm.kind != 'Cr':
            raise SErr('E-KIND', 'function %s is not a criterion' % node[1])
        for a in node[2]:
            if kbase(ev(a, ctx)) not in VALUEKINDS:
                raise SErr('E-KIND', 'function argument')
        return 'LV'
    if t == 'root':
        return ev_root(node, ctx)
    raise SErr('E-SYN', 'node %s' % t)


HEADER_ROOTS = {'§', '⟲', '◉', '⇧', '⇩'}
BARE = {'✓', '↵', '✗', '≋', '⊖', '‽'}


def ev_def(node, ctx):
    args = node[2]
    if len(args) != 2:
        raise SErr('E-ARITY', '≝ takes 2 places')
    nm, gl = args
    if nm[0] != 'word':
        raise SErr('E-KIND', '≝ first place must be a new word')
    if gl[0] != 'gloss':
        raise SErr('E-KIND', '≝ second place must be k"gloss"')
    name, k, text = nm[1], gl[1], gl[2]
    check_term_name(name, ctx)
    if k not in KIND_OF_CLASS:
        raise SErr('E-LEX', 'class letter %s' % k)
    check_text(text, 6)
    norm = ' '.join(text.lower().split())
    for tm in list(ctx.msg.terms.values()) + list(ctx.stage.values()):
        if tm.gloss and ' '.join(tm.gloss.lower().split()) == norm:
            raise SErr('E-REDEF', 'gloss repeats one in scope')
    if ctx.msg.new_terms + ctx.stage_new + 1 > 8:
        raise SErr('E-BUDGET', 'ninth new term')
    ctx.stage_new += 1
    ctx.stage[name] = Term(KIND_OF_CLASS[k], text, 'self')
    return KIND_OF_CLASS[k]


def ev_let(node, ctx):
    args = node[2]
    if len(args) != 2:
        raise SErr('E-ARITY', '≔ takes 2 places')
    nm = args[0]
    if nm[0] != 'word':
        raise SErr('E-KIND', '≔ first place must be a new word')
    check_term_name(nm[1], ctx)
    k = ev(args[1], ctx)
    if kbase(k) in ('Q', 'Ln') or kbase(k).startswith('Rf') and False:
        raise SErr('E-KIND', '≔ value')
    ctx.stage[nm[1]] = Term(kbase(k), None, 'self')
    return 'Ln'


def ev_binder(node, ctx):
    sym, args = node[1], node[2]
    if len(args) != 2:
        raise SErr('E-ARITY', '%s takes 2 places' % sym)
    nm = args[0]
    if nm[0] != 'word' or not LABEL_RE.fullmatch(nm[1]):
        raise SErr('E-KIND', 'binder place needs a label')
    if nm[1] in ctx.labels or lookup(nm[1], ctx, mark=False):
        raise SErr('E-REDEF', 'label %s already defined' % nm[1])
    ctx.labels.append(nm[1])
    try:
        k = ev(args[1], ctx)
    finally:
        ctx.labels.pop()
    if not fits(k, {'Cl'}):
        raise SErr('E-KIND', 'binder body must be a claim')
    return 'Cr' if sym == 'λ' else 'Q'


LANGS = set('python javascript typescript bash sql json yaml html css c cpp java go rust diff text'.split())


def ev_code(node, ctx):
    args = node[2]
    if len(args) < 2:
        raise SErr('E-ARITY', '⌘ takes a language and lines')
    if any(a[0] != 'str' for a in args):
        raise SErr('E-KIND', '⌘ takes quotes')
    lang = args[0][1]
    if lang not in LANGS:
        raise SErr('E-CODE', 'language %s' % lang)
    if lang == 'python':
        src = textwrap.dedent('\n'.join(a[1] for a in args[1:]))
        try:
            pyast.parse(src)
        except SyntaxError:
            raise SErr('E-CODE', 'python does not parse')
    return 'Ac'


def ev_ref_arg(node, ctx):
    a = node[2][0]
    if node[1] == '≋' and a[0] == 'word' and a[1] not in ctx.labels and lookup(a[1], ctx):
        return 'Wd'   # a flag on a word in scope: the guide's kind Wd
    if a[0] == 'num' and re.fullmatch(r'\d+', a[1]):
        m = ctx.msg
        if m.reply_single_whole:
            n = int(a[1])
            tgt = ctx.block.by_name.get(m.reply_single_whole)
            if not tgt or n < 1 or n > len(tgt.lines):
                raise SErr('E-REF', 'no line %s.%s' % (m.reply_single_whole, n))
            k = tgt.lines[n - 1].kind
            return 'Rf:' + k if k else 'Rf'
    return ev(a, ctx)


def ev_to(node, ctx):
    args = node[2]
    if len(args) < 2:
        raise SErr('E-ARITY', '➜ takes agents and a line')
    recv = ctx.msg.receivers or (ctx.block.roster - {ctx.msg.sender})
    for a in args[:-1]:
        if a[0] != 'agent':
            raise SErr('E-KIND', '➜ names agents first')
        if a[1] not in recv:
            raise SErr('E-HEAD', '➜ names a non-receiver %s' % a[1])
    k = ev(args[-1], ctx)
    if kbase(k) not in ('Cl', 'Q', 'Ln'):
        raise SErr('E-KIND', '➜ last place is a line')
    return 'Ln'


def ev_root(node, ctx):
    sym, args = node[1], node[2]
    if sym in HEADER_ROOTS:
        raise SErr('E-HEAD', 'header root %s in the body' % sym)
    if sym == '≝':
        return ev_def(node, ctx)
    if sym == '≔':
        return ev_let(node, ctx)
    if sym in ('λ', '¿'):
        return ev_binder(node, ctx)
    if sym == '⌘':
        return ev_code(node, ctx)
    if sym == '➜':
        return ev_to(node, ctx)
    info = ROOTS.get(sym)
    if not info:
        raise SErr('E-LEX', 'root %s' % sym)
    argk = []
    for i, a in enumerate(args):
        if i == 0 and sym in BARE:
            argk.append(ev_ref_arg(node, ctx))
        else:
            argk.append(ev(a, ctx))
    if sym == '⚂' and len(args) in (2, 3) and args[1][0] == 'num' and not (0 <= float(args[1][1]) <= 1):
        raise SErr('E-KIND', 'a degree is a number from 0 to 1')
    if not any(arity_ok(s, len(args)) for s in info['sigs']):
        raise SErr('E-ARITY', '%s with %d places' % (sym, len(args)))
    for sig in info['sigs']:
        if arity_ok(sig, len(args)) and match_slots(sig['slots'], argk):
            if sym == '↵':
                k0 = argk[0]
                if k0.startswith('Rf:') and k0.split(':')[1] != 'Q':
                    raise SErr('E-KIND', '↵ answers a question; that line is %s' % k0.split(':')[1])
            r = sig['right']
            if r == '=2':
                return kbase(argk[1])
            if r == '=1':
                return kbase(argk[0])
            return r
    raise SErr('E-KIND', '%s with kinds %s' % (sym, argk))


# ---------------------------------------------------------------- blocks
def parse_block(kind, raw_lines):
    b = Block()
    b.kind = kind
    b.msgs = []
    b.by_name = {}
    chunks = [[]]
    for l in raw_lines:
        if re.match(r'^---\s*$', l):
            chunks.append([])
        else:
            chunks[-1].append(l)
    for ch in chunks:
        lines = []
        for l in ch:
            code, comment = strip_comment(l)
            if not code.strip():
                continue
            m = re.match(r'\s*(ok|E-[A-Z]+)\b', comment)
            lines.append(Line(l, code.strip(), comment, m.group(1) if m else None))
        if not lines:
            continue
        m = Msg()
        m.header = lines[0]
        m.lines = lines[1:]
        m.terms = {}
        m.used = set()
        m.new_terms = 0
        m.notes = 0
        m.defs = {}
        b.msgs.append(m)
    b.roster = set()
    # header pass
    counts = Counter()
    for m in b.msgs:
        h = m.header
        try:
            h.ast = parse(tokenize(h.code))
            parse_header(m, h.ast)
        except SErr as e:
            h.err = e
            m.name = None
            continue
        counts[m.sender] += 1
        m.name = m.sender + str(m.serial)
        m.seq = counts[m.sender]
        b.roster |= {m.sender} | set(m.receivers)
        b.by_name[m.name] = m
    return b


def parse_header(m, ast_):
    if ast_[0] != 'root' or ast_[1] != '§':
        raise SErr('E-HEAD', 'first line is not a header')
    args = ast_[2]
    if not args or args[0][0] != 'agent':
        raise SErr('E-HEAD', 'sender')
    m.sender = args[0][1]
    i = 1
    m.receivers = []
    while i < len(args) and args[i][0] == 'agent':
        m.receivers.append(args[i][1])
        i += 1
    m.serial = None
    if i < len(args) and args[i][0] == 'num' and re.fullmatch(r'\d+', args[i][1]):
        m.serial = int(args[i][1])
        i += 1
    if m.serial is None:
        raise SErr('E-HEAD', 'no serial')
    m.time = None
    if i < len(args) and args[i][0] == 'time':
        m.time = args[i][1]
        i += 1
    m.detail = {}
    while i < len(args):
        a = args[i]
        if a[0] == 'root' and a[1] in ('⟲', '◉', '⇩', '⇧') and a[1] not in m.detail:
            m.detail[a[1]] = a[2]
        else:
            raise SErr('E-HEAD', 'unexpected header part %r' % (a[:2],))
        i += 1
    if m.sender in m.receivers:
        raise SErr('E-HEAD', 'sender is its own receiver')
    if len(set(m.receivers)) != len(m.receivers):
        raise SErr('E-HEAD', 'receiver twice')
    m.reply = [a for a in m.detail.get('⟲', [])]
    m.reply_single_whole = None
    if len(m.reply) == 1 and m.reply[0][0] == 'msg':
        m.reply_single_whole = m.reply[0][1]


def run_block(b, label):
    out = []   # (text, where, is a problem): printed at the end, so a retracted line can be told from a problem

    def say(text, where=None, bad=False):
        out.append((text, where, bad))

    for idx, m in enumerate(b.msgs, start=1):
        h = m.header
        # header evaluation
        herr = h.err
        gap = None
        if herr is None:
            try:
                if A.serial_required and m.serial is None:
                    raise SErr('E-HEAD', 'serial missing')
                if m.serial != m.seq:
                    gap = SErr('GAP', 'serial %s is the sender\'s message number %s' % (m.serial, m.seq))
                for tag in ('⟲', '◉'):
                    for a in m.detail.get(tag, []):
                        nm = a[1]
                        if a[0] not in ('msg', 'line') or nm not in b.by_name:
                            raise SErr('E-HEAD', '%s names a message that is not in the conversation' % tag)
                        if nm == m.name:
                            raise SErr('E-HEAD', 'message answers itself')
                imports = []
                for a in m.detail.get('⇩', []):
                    if a[0] == 'word' and a[1] in PACKS:
                        imports.append(a[1])
                    elif a[0] == 'msg' and a[1] in b.by_name and a[1] != m.name:
                        imports.append(a[1])
                    else:
                        raise SErr('E-HEAD', '⇩ names something that does not exist: %r' % (a[1],))
                m.imports = imports
                for imp in imports:
                    if imp in PACKS:
                        for code, v in PACKS[imp].items():
                            if code in m.terms:
                                raise SErr('E-REDEF', 'imported two ways: %s' % code)
                            m.terms[code] = Term(v['kind'], v['gloss'], imp)
                    else:
                        src = b.by_name[imp]
                        for nme, tm in src.defs.items():
                            if nme in m.terms:
                                raise SErr('E-REDEF', 'imported two ways: %s' % nme)
                            m.terms[nme] = Term(tm.kind, tm.gloss, imp)
                pri = m.detail.get('⇧')
                if pri is not None:
                    if len(pri) != 1:
                        raise SErr('E-ARITY', '⇧ takes one place')
                    if pri[0][0] == 'word':
                        raise SErr('E-LEX', 'unknown word %s in ⇧' % pri[0][1])
                    if pri[0][0] != 'num' or not (0 <= float(pri[0][1]) <= 1):
                        raise SErr('E-KIND', '⇧ takes a degree from 0 to 1')
            except SErr as e:
                herr = e
            if herr is None:
                herr = gap
        hv = herr.code if herr else 'ok'
        if herr and herr.code == 'GAP':
            hv = 'ok'
            say('  note %s%s' % (('[%s] ' % label) if label else '', herr.msg))
        flag = ''
        if h.expected and h.expected != hv:
            flag = '   <-- expected %s' % h.expected
        if b.kind == 'silex' and hv != 'ok':
            flag = flag or (BADTAG if REPORT else '   <-- a good block must be ok')
        if flag or A.v:
            say('  %s %-8s header %s %s%s' % (label, m.name or ('#%d' % idx), hv, (herr.msg if herr else ''), flag),
                None, bool(flag))
        if herr and herr.code != 'GAP':
            continue
        m.imports = getattr(m, 'imports', [])
        for n, ln in enumerate(m.lines, start=1):
            ctx = Ctx(m, b)
            try:
                ln.ast = parse(tokenize(ln.code))
                k = ev(ln.ast, ctx)
                top = ln.ast
                is_def = top[0] == 'root' and top[1] == '≝'
                if not is_def and kbase(k) not in ('Cl', 'Q', 'Ln'):
                    raise SErr('E-KIND', 'a value alone is not a line (kind %s)' % k)
                check_count(top, ctx, n)
                ln.verdict = 'ok'
                ln.kind = 'Cl' if is_def and False else kbase(k)
                for nme, tm in ctx.stage.items():
                    m.terms[nme] = tm
                    m.defs[nme] = tm
                m.new_terms += ctx.stage_new
                m.notes += ctx.stage_notes
            except SErr as e:
                ln.verdict = e.code
                ln.err = e
                ln.kind = None
            exp = ln.expected if b.kind == 'silex-bad' else 'ok'
            if ln.verdict != exp or A.v:
                tag = '' if ln.verdict == exp else (BADTAG if REPORT else '   <-- expected %s' % exp)
                say('  %s %s.%d %-9s %s%s%s' % (label, m.name, n, ln.verdict,
                                                   (ln.err.msg + '  ' if ln.err else ''), ln.code[:60], tag),
                    (m, n) if ln.verdict != exp else None, ln.verdict != exp)
        # AI change: when lnrl is in scope by an import, the message must carry its own count line
        # ⊨(N,nln,M), so a message that was cut short is caught even when the cut took that line itself.
        # A count line that is there but wrong is already an E-COUNT of its own line.
        if m.lines and any(t.src != 'self' and gloss_norm(t) == LNRL_GLOSS for t in m.terms.values()):
            if not any(is_count_line(x, m) for x in m.lines):
                last = len(m.lines)
                say('  %s %s.%d %-9s lnrl is in scope but %s has no count line ⊨(N,nln,%s): lost on the way, or forgotten '
                    '(N would be %d if no other line is lost)  %s%s' % (
                        label, m.name, last, 'E-COUNT', m.name, m.name, last + 1, m.lines[-1].code[:40],
                        BADTAG if REPORT else '   <-- a count line is missing'), (m, last), True)
        unused = [x for x in m.imports if x not in m.used]
        if unused:
            say('  note %s%s imports %s but uses no word from it' % (('[%s] ' % label) if label else '', m.name, unused))
    # A failing line that its own sender takes back in a later message with ⌫ is retracted, not a problem.
    # This applies to a conversation only: the examples of the guide must stay strict.
    retracted = {}
    if REPORT:
        for j, m in enumerate(b.msgs):
            if getattr(m, 'name', None) is None:
                continue
            for n, ln in enumerate(m.lines, start=1):
                top = ln.ast
                if ln.verdict != 'ok' or not top or top[0] != 'root' or top[1] != '⌫' or len(top[2]) != 1:
                    continue
                a = top[2][0]
                if a[0] not in ('msg', 'line'):
                    continue
                tgt = b.by_name.get(a[1])
                if tgt is None or tgt.sender != m.sender or b.msgs.index(tgt) >= j:
                    continue
                key = a[1] if a[0] == 'msg' else '%s.%d' % (a[1], a[2])
                retracted.setdefault(key, '%s.%d' % (m.name, n))
    out_bad = n_retr = 0
    for text, where, bad in out:
        if bad and where is not None:
            by = retracted.get('%s.%d' % (where[0].name, where[1])) or retracted.get(where[0].name)
            if by:
                print(text.split('   <--')[0] + '   (retracted by %s)' % by)
                n_retr += 1
                continue
        print(text)
        if bad:
            out_bad += 1
    run_block.retracted = n_retr
    return out_bad


def fenced_blocks(lines, first=0, last=None, kinds=('silex-bad', 'silex')):
    """(tag, lines, line number) for each fenced block whose tag is in kinds."""
    last = len(lines) if last is None else last
    out, k = [], first
    while k < last:
        if lines[k].startswith('```'):
            tag = lines[k][3:].strip()
            j = k + 1
            while j < len(lines) and not lines[j].startswith('```'):
                j += 1
            if tag in kinds:
                out.append((tag or 'silex', lines[k + 1:j], k + 1))
            k = j + 1
        else:
            k += 1
    return out


def run_blocks(blocks, title):
    total = 0
    print('  blocks: %d' % len(blocks))
    for n, (kind, raw, at) in enumerate(blocks, start=1):
        b = parse_block(kind, raw)
        print(' block %d (%s, line %d)' % (n, kind, at))
        total += run_block(b, 'b%d' % n)
    return total


if A.messages:
    _redir.__exit__(None, None, None)
    if PROBLEMS:
        print('warning: the guide itself has %d problem(s); run without --messages to see them' % len(PROBLEMS))
    raw = open(A.messages, encoding='utf-8').read().split('\n')
    fenced = fenced_blocks(raw, kinds=('', 'silex', 'text', 'plaintext', 'txt'))
    if any(l.startswith('```') for l in raw):
        lines = []
        for _, body, _ in fenced:
            lines += body + ['---']
    else:
        lines = raw
    b = parse_block('silex', lines)
    for m in b.msgs:
        for ln in [m.header] + m.lines:
            ln.expected = None
    bad = run_block(b, '')
    nlines = sum(len(m.lines) for m in b.msgs)
    retr = getattr(run_block, 'retracted', 0)
    print('== %d message(s), %d line(s), %d problem(s)%s' % (len(b.msgs), nlines, bad,
                                                           (', %d retracted' % retr) if retr else ''))
    sys.exit(1 if bad else 0)

if A.blocks:
    _redir.__exit__(None, None, None)
    if PROBLEMS:
        print('warning: the guide itself has %d problem(s); run without --blocks to see them' % len(PROBLEMS))
    raw = open(A.blocks, encoding='utf-8').read().split('\n')
    total_bad = run_blocks(fenced_blocks(raw), 'blocks')
    print('== SUMMARY: %d disagreement(s) with the verdicts written in the comments' % total_bad)
    sys.exit(1 if total_bad else 0)

print('== EXAMPLES')
total_bad = run_blocks(fenced_blocks(LINES), 'examples')   # every silex / silex-bad block in the file
print('== SUMMARY: %d example disagreements, %d document problems' % (total_bad, len(PROBLEMS)))
sys.exit(1 if (total_bad or PROBLEMS) else 0)
