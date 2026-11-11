#!/usr/bin/env python3
"""Numbers for the SILEX-0 conversation of C, D, G, M and H (11 Nov 2026).

Usage:  python3 -I analyze_record.py RECORD.md

RECORD.md is the record file: one fenced block, messages separated by a line of ---.
The script reads only the record. It does not check SILEX (silex_check.py does that); it
counts what the messages did: who asked what, who answered, who changed an answer, who
made which fault (from the ✗ lines), which words were agreed, and what each agent said.
Standard library only.
"""
import re
import sys
from collections import OrderedDict, defaultdict, Counter

AI = ['C', 'M', 'D', 'G']
ALL = ['C', 'M', 'D', 'G', 'H']
QROOTS = '?¿⍰∵'


# ------------------------------------------------------------------ parsing
def split_top(s):
    out, depth, cur, inq = [], 0, '', False
    for ch in s:
        if ch == '"':
            inq = not inq
        if not inq:
            if ch == '(':
                depth += 1
            elif ch == ')':
                depth -= 1
            elif ch == ',' and depth == 0:
                out.append(cur)
                cur = ''
                continue
        cur += ch
    out.append(cur)
    return out


def args_of(text):
    k = text.index('(')
    assert text.endswith(')'), text
    return split_top(text[k + 1:-1])


def parse(path):
    raw = open(path, encoding='utf-8').read()
    raw = re.sub(r'^```[a-z]*\n|\n```\s*$', '', raw.strip() + '\n').strip('\n')
    msgs = OrderedDict()
    for pos, block in enumerate(re.split(r'\n---\n', raw)):
        rows = block.strip('\n').split('\n')
        a = args_of(rows[0])
        sender, i, recv = a[0], 1, []
        while not a[i].isdigit():
            recv.append(a[i])
            i += 1
        serial = int(a[i])
        time, reply, imports = None, [], []
        for x in a[i + 1:]:
            if re.match(r'20\d\d-', x):
                time = x
            elif x.startswith('⟲('):
                reply = split_top(x[2:-1])
            elif x.startswith('⇩('):
                imports = split_top(x[2:-1])
        lines = []
        for r in rows[1:]:
            m = re.match(r'(\d+): (.*)$', r)
            assert m, r
            lines.append((int(m.group(1)), m.group(2)))
        name = '%s%d' % (sender, serial)
        msgs[name] = dict(name=name, pos=pos, sender=sender, recv=recv, serial=serial, time=time,
                          reply=reply, imports=imports, lines=lines)
    return msgs


def resolve(ref, msg):
    m = re.fullmatch(r'([CMDGH]\d+)\.(\d+)', ref)
    if m:
        return m.group(1), int(m.group(2))
    if re.fullmatch(r'\d+', ref) and len(msg['reply']) == 1:
        return msg['reply'][0], int(ref)
    return None


def num(x):
    try:
        return float(x)
    except ValueError:
        return None


def fmt(v):
    if v is None:
        return '-'
    return ('%g' % v)


def pct(a, b):
    return '%d%%' % round(100.0 * a / b) if b else '-'


import hashlib
print('record: %s, sha256 %s' % (sys.argv[1].split('/')[-1], hashlib.sha256(open(sys.argv[1], 'rb').read()).hexdigest()))
M = parse(sys.argv[1])
LINE = {(m['name'], k): t for m in M.values() for k, t in m['lines']}
ROOT = {key: t[0] for key, t in LINE.items()}
SENDER = {m['name']: m['sender'] for m in M.values()}
POS = {m['name']: m['pos'] for m in M.values()}
MSG_OF_SENDER = defaultdict(list)
for m in M.values():
    MSG_OF_SENDER[m['sender']].append(m)


def later_msgs(sender, pos):
    return [m for m in MSG_OF_SENDER[sender] if m['pos'] > pos]


# ------------------------------------------------------------------ 1. overview
print('== 1. OVERVIEW')
nl = sum(len(m['lines']) for m in M.values())
print('messages %d, lines %d (not counting the %d header lines)' % (len(M), nl, len(M)))
times = [m['time'] for m in M.values() if m['time']]
print('timed messages: %d, first %s, last %s' % (len(times), times[0], times[-1]))
print('%-3s %8s %6s %10s' % ('', 'messages', 'lines', 'lines/msg'))
for a in ALL:
    ms = MSG_OF_SENDER[a]
    n = sum(len(m['lines']) for m in ms)
    print('%-3s %8d %6d %10.1f' % (a, len(ms), n, n / len(ms)))

# ------------------------------------------------------------------ 2. what the lines do
print('\n== 2. LINES BY ROOT (header and count line left out)')
names = [('✓', 'agree'), ('⌫', 'retract'), ('⊡', 'seen'), ('✗', 'fault'), ('≋', 'unclear'), ('↵', 'answer'),
         ('‽', 'do-not-know'), ('?', 'yes/no ask'), ('¿', 'which ask'), ('⍰', 'how many'), ('∵', 'why'),
         ('≝', 'define'), ('≔', 'define-phrase'), ('⚂', 'probability'), ('≟', 'hypothesis'),
         ('⇨', 'request'), ('⇉', 'proposal'), ('⊨', 'claim')]
cnt = defaultdict(Counter)
for m in M.values():
    for k, t in m['lines']:
        if k == len(m['lines']) and t.startswith('⊨(%d,nln' % k):
            continue
        cnt[m['sender']][t[0]] += 1
print('%-3s ' % '' + ' '.join('%5s' % r for r, _ in names))
print('%-3s ' % '' + ' '.join('%5s' % n[:5] for _, n in names))
for a in ALL:
    print('%-3s ' % a + ' '.join('%5d' % cnt[a][r] for r, _ in names))
other = Counter()
for a in ALL:
    for r in cnt[a]:
        if r not in [x for x, _ in names]:
            other[r] += cnt[a][r]
print('other roots:', dict(other))

# ------------------------------------------------------------------ 3. faults (from the ✗ lines)
print('\n== 3. FAULTS (every ✗ line is a flag; kinds: brt bad root, bknd bad kind, baty bad arity)')
retract = {}
for m in M.values():
    for k, t in m['lines']:
        if t.startswith('⌫('):
            tgt = resolve(args_of(t)[0], m)
            if tgt:
                retract[tgt] = (m['name'], k)
rows = []
for m in M.values():
    for k, t in m['lines']:
        if t.startswith('✗('):
            a = args_of(t)
            tgt = resolve(a[0], m)
            kind = re.search(r',(\w+)\)\)$', t).group(1)
            rows.append((tgt, kind, (m['name'], k)))
print('%-8s %-5s %-8s %-6s %-9s %-9s %-10s %s' % ('line', 'author', 'kind', 'flag', 'msgs-late', 'own-msgs', 'retracted', 'text'))
by_author = defaultdict(lambda: [0, 0])
for tgt, kind, flag in sorted(rows, key=lambda r: POS[r[0][0]]):
    au = SENDER[tgt[0]]
    late = POS[flag[0]] - POS[tgt[0]]
    own = len([x for x in MSG_OF_SENDER[au] if POS[tgt[0]] < x['pos'] < POS[flag[0]]])
    r = retract.get(tgt)
    by_author[au][0] += 1
    if r:
        by_author[au][1] += 1
    print('%-8s %-5s %-8s %-6s %-9d %-9d %-10s %s' % ('%s.%d' % tgt, au, kind, '%s.%d' % flag, late, own,
                                                      ('%s.%d' % r) if r else 'LIVE', LINE[tgt]))
print()
for a in ALL:
    f, rt = by_author[a]
    n = sum(len(m['lines']) for m in MSG_OF_SENDER[a])
    print('%-3s faults %d, retracted %d, live %d, per 100 lines %.1f' % (a, f, rt, f - rt, 100.0 * f / n))
tot_ret = sum(v[1] for v in by_author.values())
print('total faults %d, retracted %d, live %d' % (len(rows), tot_ret, len(rows) - tot_ret))
flagged_by = Counter(SENDER[f[0]] for _, _, f in rows)
print('flags sent by:', dict(flagged_by))

# ------------------------------------------------------------------ 4. questions and answers
print('\n== 4. QUESTIONS AND ANSWERS')
Q = OrderedDict()
for m in M.values():
    for k, t in m['lines']:
        if t[0] in QROOTS:
            Q[(m['name'], k)] = dict(sender=m['sender'], recv=m['recv'], text=t, pos=m['pos'])
ANS = defaultdict(dict)      # (msg,k) -> {agent: [(root, value, answering-line)]}
for m in M.values():
    for k, t in m['lines']:
        if t[0] in '↵‽':
            a = args_of(t)
            tgt = resolve(a[0], m)
            if tgt in Q:
                ANS[tgt].setdefault(m['sender'], []).append((t[0], a[1] if t[0] == '↵' else None, (m['name'], k)))
misdirected = []
for m in M.values():
    for k, t in m['lines']:
        if t[0] in '↵‽':
            tgt = resolve(args_of(t)[0], m)
            if tgt not in Q:
                misdirected.append(('%s.%d' % (m['name'], k), t, 'target %s' % (('%s.%d' % tgt) if tgt else '?')))
print('question lines: %d (asked by %s)' % (len(Q), dict(Counter(q['sender'] for q in Q.values()))))
print('answer lines whose target is not a question line: %s' % misdirected)
print()
print('%-3s %5s %9s %9s %7s %9s %9s %12s' % ('', 'put', 'answered', 'dont-know', 'skipped', 'unreached', 'reply%', 'extra(non-rcv)'))
cover = {}
for r in ALL:
    put = ans = dk = skip = unre = 0
    for key, q in Q.items():
        if r in q['recv'] and q['sender'] != r:
            put += 1
            got = ANS[key].get(r)
            if got:
                if any(x[0] == '↵' for x in got):
                    ans += 1
                else:
                    dk += 1
            elif later_msgs(r, q['pos']):
                skip += 1
            else:
                unre += 1
    extra = sum(1 for key, q in Q.items() if r not in q['recv'] and r != q['sender'] and r in ANS[key])
    cover[r] = (put, ans, dk, skip, unre)
    print('%-3s %5d %9d %9d %7d %9d %9s %12d' % (r, put, ans, dk, skip, unre, pct(ans + dk, put - unre), extra))
print('(put = question lines sent to it; skipped = it sent a later message and left the question unanswered;')
print(' unreached = it sent no later message; reply%% = (answered + dont-know) / (put - unreached))')
print()
print('by kind of question (only where the agent sent a later message): ¿ = ask every receiver for its own number, ? = yes/no')
print('%-3s %22s %22s' % ('', '¿ put / answered / ‽', '? put / answered / ‽'))
for r in AI:
    res = {}
    for root in '¿?':
        put = ans = dk = 0
        for key, q in Q.items():
            if q['text'][0] != root or r not in q['recv'] or q['sender'] == r or not later_msgs(r, q['pos']):
                continue
            put += 1
            got = ANS[key].get(r)
            if got:
                if any(x[0] == '↵' for x in got):
                    ans += 1
                else:
                    dk += 1
        res[root] = (put, ans, dk)
    print('%-3s %22s %22s' % (r, '%d / %d / %d' % res['¿'], '%d / %d / %d' % res['?']))

# ------------------------------------------------------------------ 5. self-report probabilities
print('\n== 5. WHAT EACH ONE SAID ABOUT ITSELF (the question ¿(n1,⚂(⊨(~,X),n1[,Q])): every receiver gives its own n1)')
SELF = re.compile(r'^¿\(n1,⚂\((.+?),n1(?:,(.+))?\)\)$')


def pretty(p):
    p = p.strip()
    m = re.fullmatch(r'¬\(⊨\(~,(\w+)\)\)', p)
    if m:
        return 'not %s' % m.group(1)
    m = re.fullmatch(r'⊨\(~,(\w+)\)', p)
    if m:
        return m.group(1)
    m = re.fullmatch(r'⊨\((\w+),(\w+)\)', p)
    if m:
        return '[%s has %s]' % m.groups()
    m = re.fullmatch(r'∧\(¬\(⊨\(~,(\w+)\)\),¬\(⊨\(~,(\w+)\)\)\)', p)
    if m:
        return 'not %s, not %s' % m.groups()
    return p


def val(key, agent):
    got = ANS[key].get(agent)
    if not got:
        return None
    last = got[-1]
    return '?' if last[0] == '‽' else last[1]


own = {}
for m in M.values():
    for k, t in m['lines']:
        mm = re.fullmatch(r'⚂\(⊨\((\w+),(\w+)\),([\d.]+)\)', t)
        if mm and mm.group(1) in ALL:
            own[(m['name'], k)] = (m['sender'], mm.group(2), mm.group(3))
print('%-8s %-30s %5s %5s %5s %5s   asked by' % ('line', 'item | given', 'M', 'D', 'G', 'H'))
selfrows = []
for key, q in Q.items():
    mm = SELF.match(q['text'])
    if not mm:
        continue
    item = pretty(mm.group(1)) + ((' | ' + pretty(mm.group(2))) if mm.group(2) else '')
    vals = {a: val(key, a) for a in ['M', 'D', 'G', 'H']}
    selfrows.append((key, item, vals))
    print('%-8s %-30s %5s %5s %5s %5s   %s' % ('%s.%d' % key, item, *[('-' if vals[a] is None else vals[a]) for a in ['M', 'D', 'G', 'H']], q['sender']))
print('statements of probability about itself, written by the speaker (⚂(⊨(who,X),n)):')
for key, (who, item, v) in own.items():
    print('  %-8s %s says P(%s has %s) = %s' % ('%s.%d' % key, SENDER[key[0]], who, item, v))

# ------------------------------------------------------------------ 6. relation and other yes/no questions
print('\n== 6. YES/NO QUESTIONS: every answer, one line per question (value 0 = no, 1 = yes)')
REL = re.compile(r'^\?\(⊨\((\w+),(iml|dnd|sw|ctd),(\w+)\)\)$')
PROP = re.compile(r'^\?\(⊨\((H|stn|\w+),(\w+)\)\)$')
yn_rows = []
for key, q in Q.items():
    t = q['text']
    if not t.startswith('?('):
        continue
    kind = 'rel' if REL.match(t) else ('prop' if PROP.match(t) else 'other')
    vals = {a: val(key, a) for a in ALL}
    yn_rows.append((key, q['sender'], kind, t, vals))
print('%-8s %-3s %-5s %-34s %5s %5s %5s %5s %5s' % ('line', 'by', 'kind', 'question', 'C', 'M', 'D', 'G', 'H'))
for key, snd, kind, t, vals in yn_rows:
    print('%-8s %-3s %-5s %-34s %5s %5s %5s %5s %5s' % ('%s.%d' % key, snd, kind, t[2:-1][:34], *[('-' if vals[a] is None else vals[a]) for a in ALL]))

# ------------------------------------------------------------------ 7. answer shapes
print('\n== 7. SHAPE OF THE ANSWERS (every ↵ with a number; last answer per question)')
print('%-3s %6s %6s %6s %7s %9s %s' % ('', 'n', 'zero', 'one', 'between', 'distinct', 'values used'))
for a in ALL:
    vs = []
    for key in Q:
        v = val(key, a)
        if v not in (None, '?'):
            f = num(v)
            if f is not None:
                vs.append(f)
    z = sum(1 for v in vs if v == 0)
    o = sum(1 for v in vs if v == 1)
    d = sorted(set(vs))
    print('%-3s %6d %6d %6d %7d %9d %s' % (a, len(vs), z, o, len(vs) - z - o, len(d), ' '.join(fmt(x) for x in d)))
print()
print('answers that are not 0 or 1, by agent, with the share of the agent\'s numeric answers:')
for a in ALL:
    vs = [num(val(k, a)) for k in Q if val(k, a) not in (None, '?') and num(val(k, a)) is not None]
    mid = [v for v in vs if 0 < v < 1]
    print('  %s: %d of %d' % (a, len(mid), len(vs)))

# ------------------------------------------------------------------ 8. who saw whom (order effect)
print('\n== 8. ORDER EFFECT: same question, two agents, both gave a number')
print('Each round the order of messages is C, M, D, G. M saw only the round before; D also saw M; G also saw M and D.')


def final(key, a):
    got = ANS[key].get(a)
    if not got:
        return None, None
    r, v, line = got[-1]
    f = num(v) if r == '↵' else None
    return f, line


pairs = defaultdict(list)
for key in Q:
    for x, y in [('M', 'D'), ('M', 'G'), ('D', 'G'), ('M', 'H'), ('D', 'H'), ('G', 'H')]:
        fx, lx = final(key, x)
        fy, ly = final(key, y)
        if fx is None or fy is None:
            continue
        seen = lx[0] in M[ly[0]]['reply']
        pairs[(x, y)].append((key, fx, fy, seen))
print('%-6s %4s %6s %12s %14s %13s' % ('pair', 'n', 'equal', 'mean |diff|', 'within 0.1', 'y saw x'))
for (x, y), rs in pairs.items():
    n = len(rs)
    eq = sum(1 for _, a, b, _ in rs if a == b)
    md = sum(abs(a - b) for _, a, b, _ in rs) / n
    w1 = sum(1 for _, a, b, _ in rs if abs(a - b) <= 0.1 + 1e-9)
    sn = sum(1 for *_, s in rs if s)
    print('%-6s %4d %6d %12.3f %14d %13d' % ('%s vs %s' % (x, y), n, eq, md, w1, sn))
print()
print('G against M on the questions both gave a number to, and where the numbers sat against 0.5')
tw = 0
rows_gm = [(k, a, b) for k, a, b, s in pairs[('M', 'G')]]
for k, a, b in rows_gm:
    toward = 'toward 0.5' if abs(b - 0.5) < abs(a - 0.5) - 1e-9 else ('same' if a == b else 'away/other')
    if toward == 'toward 0.5':
        tw += 1
    print('  %-8s M %-5s G %-5s %s' % ('%s.%d' % k, fmt(a), fmt(b), toward))
print('G moved toward 0.5 relative to M in %d of %d cases; equal in %d' % (tw, len(rows_gm), sum(1 for k, a, b in rows_gm if a == b)))
for tag, flag in (('G had read M\'s message', True), ('G had not read it', False)):
    sub = [(k, a, b) for k, a, b, sn in pairs[('M', 'G')] if sn == flag]
    eq = sum(1 for k, a, b in sub if a == b)
    toward = sum(1 for k, a, b in sub if a != b and abs(b - a) <= 0.1 + 1e-9 and abs(b - 0.5) < abs(a - 0.5) - 1e-9)
    far = sum(1 for k, a, b in sub if abs(b - a) > 0.1 + 1e-9)
    print('  %-24s n %2d, equal %2d, within 0.1 and nearer 0.5 %2d, further apart than 0.1: %2d' % (tag, len(sub), eq, toward, far))
nonbin = [(k, a, b) for k, a, b in rows_gm if not (a in (0, 1) and b in (0, 1))]
print('  pairs where at least one of the two numbers is neither 0 nor 1: %d; equal in %d; nearer 0.5 within 0.1 in %d' % (
    len(nonbin), sum(1 for k, a, b in nonbin if a == b),
    sum(1 for k, a, b in nonbin if a != b and abs(b - a) <= 0.1 + 1e-9 and abs(b - 0.5) < abs(a - 0.5) - 1e-9)))

# ------------------------------------------------------------------ 9. changes of answer
print('\n== 9. THE SAME AGENT GAVE TWO DIFFERENT ANSWERS TO ONE QUESTION')
nchg = 0
for key in Q:
    for a, got in ANS[key].items():
        vs = [(r, v, ln) for r, v, ln in got]
        if len(set((r, v) for r, v, _ in vs)) > 1:
            nchg += 1
            print('  %s answered %s.%d: %s' % (a, key[0], key[1], ' then '.join('%s%s (%s.%d)' % (r, '' if v is None else ' ' + v, ln[0], ln[1]) for r, v, ln in vs)))
            if a == 'H':
                print('     (H lines were written by C for H; the ⌫ in H11.1 retracts H9.6)')
print('changed answers: %d' % nchg)
print('retractions of an answer: %s' % ['%s.%d→%s.%d' % (t[0], t[1], r[0], r[1]) for t, r in retract.items() if ROOT.get(t) == '↵'])

# ------------------------------------------------------------------ 10. words
print('\n== 10. WORDS: who defined, who agreed, who used')
defs = []
for m in M.values():
    for k, t in m['lines']:
        if t.startswith('≝(') or t.startswith('≔('):
            a = args_of(t)
            defs.append((m['name'], k, m['sender'], a[0], t[0], a[1], m['recv']))
agree = defaultdict(dict)    # (msg,k) -> {agent: line}
pinned_stmt = defaultdict(list)
for m in M.values():
    for k, t in m['lines']:
        if t.startswith('✓('):
            tgt = resolve(args_of(t)[0], m)
            if tgt:
                agree[tgt].setdefault(m['sender'], (m['name'], k))
        if t.startswith('⊨(') and t.endswith(',pin)'):
            tgt = resolve(args_of(t)[0], m)
            if tgt:
                pinned_stmt[tgt].append((m['name'], k))
USE = defaultdict(lambda: defaultdict(set))
for m in M.values():
    for k, t in m['lines']:
        if t[0] in '≝≔✓⌫⊡✗':
            continue
        for d in defs:
            if re.search(r'(?<![A-Za-z0-9])%s(?![A-Za-z0-9.])' % re.escape(d[3]), t):
                USE[d[3]][m['sender']].add(m['name'])
print('%-5s %-5s %-4s %-4s %-30s %-22s %-12s %s' % ('word', 'where', 'by', 'kind', 'gloss', 'agreed by (receivers)', 'status', 'used in messages by'))
nstrict = nai = 0
status_of = {}
for (mn, k, who, w, kind, gloss, recv) in defs:
    rc = [r for r in recv if r != who]
    ok = [r for r in rc if r in agree[(mn, k)]]
    miss = [r for r in rc if r not in agree[(mn, k)]]
    ai_miss = [r for r in miss if r != 'H']
    if not miss:
        status = 'pinned'
        nstrict += 1
    elif not ai_miss:
        status = 'AI-pinned (H sent no ✓)'
        nai += 1
    else:
        status = 'not pinned (missing %s)' % ','.join(ai_miss + (['H'] if 'H' in miss else []))
    status_of[w] = status
    use = ' '.join('%s%d' % (a, len(USE[w][a])) for a in ALL if USE[w].get(a))
    print('%-5s %-5s %-4s %-4s %-30s %-22s %-12s %s' % (w, '%s.%d' % (mn, k), who, kind, gloss[:30], ','.join(ok) or '-', status.split(' (')[0] if status.startswith('not') else status, use or '-'))
print('definitions: %d (%s)' % (len(defs), dict(Counter(d[2] for d in defs))))
print('pinned (every receiver ✓): %d; AI-pinned (every AI receiver ✓, H sent no ✓): %d; not pinned: %d' % (nstrict, nai, len(defs) - nstrict - nai))
print('✓ lines sent per agent:', dict(Counter(m['sender'] for m in M.values() for k, t in m['lines'] if t.startswith('✓('))))
print('definitions of other agents that each agent received and ✓-ed:')
for a in AI:
    got = [(d, agree[(d[0], d[1])]) for d in defs if a in d[6] and d[2] != a]
    okc = sum(1 for d, ag in got if a in ag)
    print('  %s: %d of %d' % (a, okc, len(got)))

# ------------------------------------------------------------------ 11. questions about H or not
print('\n== 11. REPLY RATE ON QUESTIONS ABOUT H AND ON OTHERS (an AI cannot know H, so skipping those may be right)')
ABOUT_H = re.compile(r'[(,]H[,)]')
print('%-3s %24s %24s' % ('', 'about H: put/answered/skipped', 'others: put/answered/skipped'))
for r in AI:
    res = {}
    for tag, test in (('H', True), ('O', False)):
        put = ans = skip = 0
        for key, q in Q.items():
            if (bool(ABOUT_H.search(q['text'])) != test) or r not in q['recv'] or q['sender'] == r:
                continue
            if not later_msgs(r, q['pos']):
                continue
            put += 1
            if ANS[key].get(r):
                ans += 1
            else:
                skip += 1
        res[tag] = (put, ans, skip)
    print('%-3s %24s %24s' % (r, '%d / %d / %d' % res['H'], '%d / %d / %d' % res['O']))
print('(counted only where the agent sent a later message; ‽ counts as answered)')

# ------------------------------------------------------------------ 12. agreement of the AIs on relation questions
print('\n== 12. THE THREE OTHER AIs ON RELATION QUESTIONS (iml / dnd / sw / ctd), C included when it answered')
relkeys = [key for key, snd, kind, t, vals in yn_rows if kind == 'rel']
allv = []
splits = []
unan = 0
n3 = 0
for key, snd, kind, t, vals in yn_rows:
    if kind != 'rel':
        continue
    vs = {a: num(vals[a]) for a in AI if a != snd and vals[a] not in (None, '?') and num(vals[a]) is not None}
    allv += list(vs.values())
    if len(vs) >= 3:
        n3 += 1
        xs = list(vs.values())
        if len(set(xs)) == 1:
            unan += 1
        if max(xs) - min(xs) >= 0.5:
            splits.append((key, t[2:-1], vs))
print('relation questions: %d; with at least three AI numbers: %d; all equal: %d; spread of 0.5 or more: %d' % (len(relkeys), n3, unan, len(splits)))
z = sum(1 for v in allv if v == 0)
o = sum(1 for v in allv if v == 1)
print('AI numeric answers on relation questions: %d; no (0): %d (%s); yes (1): %d (%s); between: %d' % (len(allv), z, pct(z, len(allv)), o, pct(o, len(allv)), len(allv) - z - o))
for key, t, vs in splits:
    print('  split %-8s %-26s %s' % ('%s.%d' % key, t, ' '.join('%s=%s' % (a, fmt(v)) for a, v in vs.items())))

# ------------------------------------------------------------------ 13. H against the AIs
print('\n== 13. H AGAINST THE AIs (questions both H and at least one AI answered with a number; H = the owner, written by C)')
print('%-8s %-34s %6s  %s' % ('line', 'question', 'H', 'AIs (M D G C)'))
bigdiff = 0
for key, snd, kind, t, vals in yn_rows:
    hv = num(vals['H']) if vals['H'] not in (None, '?') else None
    if hv is None:
        continue
    ais = {a: num(vals[a]) for a in AI if vals[a] not in (None, '?') and num(vals[a]) is not None and a != snd}
    if not ais:
        continue
    mean = sum(ais.values()) / len(ais)
    flag = '  <-- differs by %.2f from their mean' % abs(hv - mean) if abs(hv - mean) >= 0.5 else ''
    if flag:
        bigdiff += 1
    print('%-8s %-34s %6s  %s%s' % ('%s.%d' % key, t[2:-1][:34], fmt(hv), ' '.join('%s=%s' % (a, fmt(v)) for a, v in ais.items()), flag))
print('questions with a difference of 0.5 or more: %d' % bigdiff)
print('self-probes both H and an AI answered:')
for key, item, vals in selfrows:
    if vals['H'] is not None:
        print('  %-8s %-18s H=%s  M=%s D=%s G=%s' % ('%s.%d' % key, item, vals['H'], *[('-' if vals[a] is None else vals[a]) for a in ['M', 'D', 'G']]))

# ------------------------------------------------------------------ 14. does a number move when the condition changes?
print('\n== 14. DOES THE NUMBER MOVE WHEN THE CONDITION CHANGES? (self-probes, same word, with and without a condition)')
base = {}
for key, item, vals in selfrows:
    if ' | ' not in item:
        base.setdefault(item, vals)
print('%-6s %-26s %s' % ('agent', 'word | condition', 'number (base) -> number (condition), change'))
for a in ['M', 'D', 'G']:
    mx = []
    for key, item, vals in selfrows:
        if ' | ' not in item:
            continue
        w = item.split(' | ')[0]
        if w not in base or vals[a] in (None, '?') or base[w][a] in (None, '?'):
            continue
        b, v = num(base[w][a]), num(vals[a])
        mx.append((abs(v - b), w, item.split(' | ')[1], b, v))
    for d, w, c, b, v in mx:
        print('%-6s %-26s %s -> %s  (%+.2f)' % (a, w + ' | ' + c, fmt(b), fmt(v), v - b))
    if mx:
        print('%-6s largest change %.2f, changes of 0.1 or less in %d of %d' % (a, max(x[0] for x in mx), sum(1 for x in mx if x[0] <= 0.1 + 1e-9), len(mx)))

# ------------------------------------------------------------------ 15. the pin lines
print('\n== 15. PIN LINES ⊨(M.k,pin): is each one backed by a ✓ from every receiver of the line it pins?')
npin = nok = 0
pin_by = Counter()
for tgt, stmts in sorted(pinned_stmt.items(), key=lambda kv: (POS[kv[0][0]], kv[0][1])):
    dm = M[tgt[0]]
    need = sorted(dm['recv'])
    have = agree[tgt]
    miss = [r for r in need if r not in have]
    for (mn, k) in stmts:
        npin += 1
        pin_by[SENDER[mn]] += 1
        nok += 0 if miss else 1
        print('  %-8s pins %-8s (written by %s, sent to %s): ✓ from %s -> %s' % (
            '%s.%d' % (mn, k), '%s.%d' % tgt, dm['sender'], ','.join(need), ','.join(sorted(have)) or '-',
            'ok' if not miss else 'MISSING ' + ','.join(miss)))
print('pin lines: %d (written by %s); backed by every receiver: %d' % (npin, dict(pin_by), nok))

# ------------------------------------------------------------------ 16. a word and a question that uses it, in one message
print('\n== 16. A MESSAGE THAT DEFINES A WORD AND ASKS A QUESTION WITH IT (question line = ? ¿ ⍰ ∵)')
by_def = defaultdict(lambda: [0, 0])
for m in M.values():
    dws = [args_of(t)[0] for k, t in m['lines'] if t[0] in '≝≔']
    if not dws:
        continue
    used = [w for w in dws if any(t[0] in QROOTS and re.search(r'(?<![A-Za-z0-9])%s(?![A-Za-z0-9.])' % re.escape(w), t) for k, t in m['lines'])]
    by_def[m['sender']][0] += 1
    by_def[m['sender']][1] += 1 if used else 0
    print('  %-4s defines %-22s a question uses: %s' % (m['name'], ' '.join(dws), ' '.join(used) or '-'))
print('messages with a definition; of those, with a question that uses a word defined in the same message:')
for a in ALL:
    if by_def[a][0]:
        print('  %s: %d; %d' % (a, by_def[a][0], by_def[a][1]))
