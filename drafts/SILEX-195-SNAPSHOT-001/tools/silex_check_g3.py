#!/usr/bin/env python3
"""SILEX universal checker (candidate r1; written by C). ONE program, four layers.  Run with:  python3 -I silex_check.py ...

It wraps the pinned reference checker (ucl_check.py, c1) and adds what c1 does not look at. It does not replace c1,
changes nothing in D3, D5 or L0, and does not edit any pinned file. A PASS is evidence about FORM, protocol and plausibility.
It is not evidence that two readers recover the same meaning. Only a blind reader can show that.

LAYERS
  1 FORM          each message, line by line, on the pinned checker c1 and a table (the pinned base table, or an extension
                  of it with --table). Errors: the E-codes of D3 Appendix B. Also reports the basis of every line (weakest status).
  2 SESSION       the mechanical part of the standing rules of L0 (CP-1 to CP-17) over the whole conversation: header and ids,
                  declarations first, force on every line, tiers, qualified references, answer links, one question per message,
                  request and outcome, tense under a context, withdrawal, receipt, scaffolds for referent names, proposals.
                  ERR makes the run fail. WARN is a writer-rule or style finding. NOTE is information.
  3 PLAUSIBILITY  warnings only, never a failure: a message that supplies P and not-P, a duplicated line, an undeclared zE name,
                  a trivial comparison, an unused declaration. With an extended table that holds the roots of the open-build
                  track, also: a probability outside 0 to 1, an undertaking and a refusal of the same act in one message,
                  a count equated with a quantity, a closed range with its ends in the wrong order. Those rules are inactive
                  for the pinned base table.
  4 ENGLISH       a measure, not a verdict: how much of the text is English inside scaffolds. Two figures: the gate-pack measure
                  (a mention with a space in it) so that old figures stay comparable, and a strict measure (a mention whose
                  content does not parse as SILEX, so one-word and digit scaffolds count too). Also: restated scaffolds.

COMMANDS
  check FILE [--table T] [--base DIR] [--layers 1234] [--json] [--strict]
        FILE is a session file: messages start with a line "=== <message id> <sender> ===" (the gate-pack format), lines starting
        with # are comments. A file whose first line is m▤(...) is read as ONE message.
        Exit code 0 = no ERR (and, with --strict, no WARN); 1 = fail; 2 = usage or integrity error.
  line  "<expression>" [--table T] [--base DIR]     one expression, layer 1 and the tier of every root in it
  selftest                                          the built-in tests (cases that must pass and cases that must fail)

PINS (G3 COPY: ucl_check.py is checker g3 and data_table.json is the n0 table; the run stops if the base files differ)
  ucl_check.py    3ec4e639fc9bda9de5293af87f636d7f2e1086bd5dc4e9758a9c8ba058bbf484
  data_table.json d144c3830d4221500fd9a87f25d2050948de72449f00bc4b3fbcbb13d6e24e94
  The base files are looked for in --base, next to this file, in ./registry/base and in ../registry/base.

WHAT IT DOES NOT CHECK (blind spots, stated so that nobody assumes otherwise)
  meaning; units; whether a number is plausible for its quantity; whether a scaffold says what the writer means; whether a
  claim is true; whether the other participant understood; the order and delivery of messages (the record keeper's job,
  D3 11.3); the checkpoint rules of Change 13; identity merging by i≡ (Change 11); relayed reports (Change 12); level S.
"""
import sys, os, re, json, hashlib, shutil, tempfile, importlib.util
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK_SHA = '3ec4e639fc9bda9de5293af87f636d7f2e1086bd5dc4e9758a9c8ba058bbf484'   # G3: checker g3 (n0 is the placeholder), not the pinned c1 and not the rulebook candidate
TABLE_SHA = 'd144c3830d4221500fd9a87f25d2050948de72449f00bc4b3fbcbb13d6e24e94'   # G3: the table with n0 as the placeholder atom
FORCE = ('g←', 'h◇', 'p◇', 'u?', 'u~')
TENSE = ('t≺', 't●', 't▷')
QUESTION = ('?=', '?⊤')
CORE_BY_L0 = ('m▤', 'r>')          # status U in D3, CORE in L0 (Keep U-12)


class Usage(Exception):
    pass


# ---------------------------------------------------------------- loading the pinned checker
def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def find_base(base=None):
    cands = [base] if base else [HERE, os.path.join(HERE, 'registry', 'base'), os.path.join(HERE, '..', 'registry', 'base'),
                                 os.path.join(os.getcwd(), 'registry', 'base'), os.getcwd()]
    for d in cands:
        if d and os.path.isfile(os.path.join(d, 'ucl_check.py')) and os.path.isfile(os.path.join(d, 'data_table.json')):
            return os.path.abspath(d)
    raise Usage('cannot find ucl_check.py and data_table.json (use --base DIR)')


def load(base=None, table=None, tag='sc'):
    """Return (module, entries, info). Refuses to run if a pinned base file differs."""
    d0 = find_base(base)
    if sha(os.path.join(d0, 'ucl_check.py')) != CHECK_SHA:
        raise Usage('ucl_check.py differs from the pinned c1: refusing to run')
    if sha(os.path.join(d0, 'data_table.json')) != TABLE_SHA:
        raise Usage('data_table.json differs from the pinned base table: refusing to run')
    base_entries = json.load(open(os.path.join(d0, 'data_table.json'), encoding='utf-8'))
    entries = base_entries
    info = {'table': 'pinned base table', 'table_sha': TABLE_SHA, 'extra': []}
    if table:
        entries = json.load(open(table, encoding='utf-8'))
        if entries[:len(base_entries)] != base_entries:
            raise Usage('the extension table must keep the 195 base entries unchanged and only add entries after them')
        info = {'table': 'EXTENDED table %s (not the pinned table)' % os.path.basename(table), 'table_sha': sha(table),
                'extra': [e['root'] for e in entries[len(base_entries):]]}
    tmp = tempfile.mkdtemp(prefix='silexcheck_')
    try:
        shutil.copy(os.path.join(d0, 'ucl_check.py'), tmp)
        json.dump(entries, open(os.path.join(tmp, 'data_table.json'), 'w', encoding='utf-8'), ensure_ascii=False)
        spec = importlib.util.spec_from_file_location('ucl_%s_%d' % (tag, abs(hash(tmp))), os.path.join(tmp, 'ucl_check.py'))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return mod, entries, info


def tiers(entries):
    """root -> (status, tier). CORE = E or Ep, plus the header and answer link; CANDIDATE = P; PARKED = U or X."""
    out = {}
    for e in entries:
        s = e.get('status')
        t = 'CORE' if s in ('E', 'Ep') else 'CANDIDATE' if s == 'P' else 'PARKED'
        if e['root'] in CORE_BY_L0: t = 'CORE'
        out[e['root']] = (s, t)
    return out


# ---------------------------------------------------------------- reading a session file
def parse_file(path):
    text = open(path, encoding='utf-8').read()
    msgs, cur = [], None
    for n, raw in enumerate(text.split('\n'), 1):
        m = re.match(r'^=== (\S+) (\S+) ===\s*$', raw)
        if m:
            cur = {'id': m.group(1), 'sender': m.group(2), 'lines': [], 'nos': []}
            msgs.append(cur)
        elif cur is not None and raw.strip() and not raw.lstrip().startswith('#'):
            cur['lines'].append(raw.strip()); cur['nos'].append(n)
    if msgs:
        return msgs
    lines = [(n, l.strip()) for n, l in enumerate(text.split('\n'), 1) if l.strip() and not l.lstrip().startswith('#')]
    if lines and lines[0][1].startswith('m▤('):
        h = re.match(r'm▤\((zU[A-Za-z0-9]+),(zk[A-Za-z0-9]+)\)', lines[0][1])
        if h:
            return [{'id': h.group(1), 'sender': h.group(2), 'lines': [l for _, l in lines], 'nos': [n for n, _ in lines]}]
    return []


# ---------------------------------------------------------------- small helpers on text and trees
def norm(s):
    return re.sub(r'\s+', '', s)


def split_top(s):
    """Split the inside of an argument list at top-level commas (parentheses, mentions and ✠( ) all nest)."""
    out, cur, dp, dm = [], '', 0, 0
    for ch in s:
        if ch == '⌜': dm += 1
        elif ch == '⌝': dm -= 1
        elif dm == 0 and ch == '(': dp += 1
        elif dm == 0 and ch == ')': dp -= 1
        if ch == ',' and dp == 0 and dm == 0:
            out.append(cur); cur = ''
        else:
            cur += ch
    out.append(cur)
    return out


def inner(line, root):
    """The text inside root( ... ) when the line is exactly one application of root, else None."""
    if not (line.startswith(root + '(') and line.endswith(')')): return None
    s = line[len(root) + 1:-1]
    dp = dm = 0
    for ch in s:
        if ch == '⌜': dm += 1
        elif ch == '⌝': dm -= 1
        elif dm == 0 and ch == '(': dp += 1
        elif dm == 0 and ch == ')':
            dp -= 1
            if dp < 0: return None
    return s if dp == 0 and dm == 0 else None


def top_mentions(s):
    """Top-level mention segments of a text (their content, nested mentions kept inside)."""
    out, d, start = [], 0, 0
    for i, ch in enumerate(s):
        if ch == '⌜':
            if d == 0: start = i + 1
            d += 1
        elif ch == '⌝' and d:
            d -= 1
            if d == 0: out.append(s[start:i])
    return out


def inner_mentions(s):
    return re.findall(r'⌜([^⌜⌝]*)⌝', s)


def walk(n, stack=()):
    """Yield (node, ancestors) over a parsed tree. Mentioned content is not descended into (it is talked about, not used)."""
    yield n, stack
    if n[0] == 'app':
        for a in n[2]: yield from walk(a, stack + (n[1],))
    elif n[0] == 'attr':
        yield from walk(n[1], stack + ('attr',)); yield from walk(n[2], stack + ('attr',))


def roots_used(tree):
    return [n[1] for n, _ in walk(tree) if n[0] in ('app', 'atom')]


def declared_names(tree):
    out = []
    for n, _ in walk(tree):
        if n[0] == 'app' and n[1] == 'd≔' and n[2] and n[2][0][0] == 'name': out.append(n[2][0][1])
    return out


def num_value(node):
    """Value of a literal ✠ term made of integers and ÷ − + × (else None)."""
    if node[0] != 'math': return None
    def ev(t):
        t = t.strip()
        if re.fullmatch(r'0|[1-9][0-9]*', t): return Fraction(int(t))
        m = re.match(r'^(\+|−|×|÷)\((.*)\)$', t, re.S)
        if not m: return None
        a = split_top(m.group(2))
        if len(a) != 2: return None
        x, y = ev(a[0]), ev(a[1])
        if x is None or y is None: return None
        if m.group(1) == '+': return x + y
        if m.group(1) == '−': return x - y
        if m.group(1) == '×': return x * y
        return None if y == 0 else x / y
    return ev(node[1])


# ---------------------------------------------------------------- the report
class Report:
    def __init__(self):
        self.items = []

    def add(self, layer, sev, code, msg, mid=None, ln=None, text=None):
        self.items.append({'layer': layer, 'sev': sev, 'code': code, 'msg': msg, 'message': mid, 'line': ln, 'text': text})

    def count(self, sev, layer=None):
        return sum(1 for i in self.items if i['sev'] == sev and (layer is None or i['layer'] == layer))


# ---------------------------------------------------------------- the checker proper
def run(msgs, mod, entries, info, layers='1234', rep=None):
    rep = rep or Report()
    T = tiers(entries)
    extra = set(info['extra'])
    order = {m['id']: i for i, m in enumerate(msgs)}
    sender = {m['id']: m['sender'] for m in msgs}
    basis_count = {}
    trees, res, decl = {}, {}, {}
    # ---- layer 1 (also fills trees, results and declarations for the other layers)
    for m in msgs:
        env = mod.Env()
        for ln, no, in zip(m['lines'], m['nos']):
            key = (m['id'], no)
            try: trees[key] = mod.parse(ln)
            except mod.Err: trees[key] = None
            try:
                cat, basis, lv, warns = mod.check_line(ln, env)
                res[key] = ('OK', cat, basis, warns)
                weakest = basis[-1] if basis else 'E'
                basis_count[weakest] = basis_count.get(weakest, 0) + 1
            except mod.Err as e:
                res[key] = ('ERR', e.code, str(e))
                if '1' in layers: rep.add(1, 'ERR', e.code, e.msg, m['id'], no, ln)
            except Exception as e:                                   # the pinned checker failed on this line
                res[key] = ('ERR', 'E-CRASH', type(e).__name__)
                if '1' in layers: rep.add(1, 'ERR', 'E-CRASH', 'the pinned checker raised %s' % type(e).__name__, m['id'], no, ln)
        decl[m['id']] = set()
        for ln, no in zip(m['lines'], m['nos']):
            t = trees.get((m['id'], no))
            if t is not None: decl[m['id']] |= set(declared_names(t))
    if '1' in layers:
        nl = sum(len(m['lines']) for m in msgs)
        rep.add(1, 'NOTE', 'L1-SUMMARY', '%d messages, %d lines; weakest basis per line: %s' % (
            len(msgs), nl, ', '.join('%s %d' % (k, basis_count[k]) for k in sorted(basis_count, key=lambda b: -mod.RANK[b]))))
    if '2' in layers: layer2(msgs, mod, T, trees, res, decl, order, sender, rep)
    if '3' in layers: layer3(msgs, mod, T, extra, trees, res, decl, rep)
    if '4' in layers: layer4(msgs, mod, trees, rep)
    return rep


# ---------------------------------------------------------------- layer 2: the session rules
def layer2(msgs, mod, T, trees, res, decl, order, sender, rep):
    S = lambda sev, code, msg, m, no=None, text=None: rep.add(2, sev, code, msg, m['id'], no, text)
    ids = [m['id'] for m in msgs]
    if not msgs:
        rep.add(2, 'ERR', 'S01', 'no message found; each message starts with a line "=== <message id> <sender> ==="'); return
    for i in sorted({i for i in ids if ids.count(i) > 1}): rep.add(2, 'ERR', 'S01', 'duplicate message id %s' % i)
    cand_use, free_ref = {}, {}
    questions = {}                         # (message id, normalized text) -> [answered?, text]
    sent_p = []                            # (index, sender, name) for p↗(d≔(name, ...))
    for mi, m in enumerate(msgs):
        mid, snd = m['id'], m['sender']
        # S01 ids and header
        if not re.fullmatch(r'zU[A-Za-z]+\d+', mid) or not snd.startswith('zk'):
            S('ERR', 'S01', 'message id must look like zUa1 and sender like zkA', m)
        if not m['lines'] or norm(m['lines'][0]) != 'm▤(%s,%s)' % (mid, snd):
            S('ERR', 'S01', 'the first line must be m▤(%s,%s), matching the separator' % (mid, snd), m, m['nos'][0] if m['nos'] else None)
        body = list(zip(m['lines'], m['nos']))[1:]
        # S02 declarations right after the header (writer rule CP-1, U-35)
        seen_other = False
        for ln, no in body:
            if ln.startswith('d≔('):
                if seen_other:
                    S('WARN', 'S02', 'd≔ after the body began: writers put every d≔ right after the header (CP-1, U-35)', m, no, ln); break
            else: seen_other = True
        qtexts = {}
        for ln, no in body:
            t = trees.get((mid, no))
            if t is None: continue
            r = res.get((mid, no))
            head = t[1] if t[0] == 'app' else None
            # S03 force on every line (CP-2): the pinned checker marks a bare content line with FU
            if r and r[0] == 'OK' and any(w.startswith('FU:') for w in r[3]):
                S('ERR', 'S03', 'bare claim line: every claim line carries its own force root g← h◇ p◇ u? u~ (CP-2)', m, no, ln)
            # S04 conjunction directly under a force root (CP-3)
            if head in FORCE and t[2] and t[2][0][0] == 'app' and t[2][0][1] == '∧':
                S('WARN', 'S04', 'one claim per line: ∧ directly under a force root (CP-3). Name the claim with d≔ or write two lines', m, no, ln)
            # S05 tiers (CP-4, Change 15)
            for root in sorted(set(roots_used(t))):
                if root not in T: continue
                st, tier = T[root]
                if tier == 'PARKED':
                    S('ERR', 'S05', 'root %s is PARKED (status %s): not applied in a session; a reader answers a? (Change 15)' % (root, st), m, no, ln)
                elif tier == 'CANDIDATE':
                    cand_use[root] = cand_use.get(root, 0) + 1
            # S06 qualified references (CP-6, U-43)
            for n, _ in walk(t):
                if n[0] == 'app' and n[1] == 'r@' and len(n[2]) == 2:
                    tgt = n[2][1]
                    if tgt[0] != 'name' or not tgt[1].startswith('zU'):
                        S('ERR', 'S06', 'in a session r@ is only the qualified reference: its second argument is a message name (U-43)', m, no, ln)
                    elif tgt[1] not in order or order[tgt[1]] >= mi:
                        S('ERR', 'S06', 'r@ points to %s, which is not an earlier message' % tgt[1], m, no, ln)
                    elif n[2][0][0] == 'name' and n[2][0][1] not in decl.get(tgt[1], ()) and not n[2][0][1].startswith(('zk', 'zU')):
                        free_ref.setdefault((n[2][0][1], tgt[1]), (m, no))
            # S07 answer links (CP-9)
            if head == 'r>' and len(t[2]) == 3:
                parts = split_top(ln[3:-1])
                tg = t[2][0][1] if t[2][0][0] == 'name' else None
                qt = parts[1].strip() if len(parts) > 1 else ''
                if tg not in order or order[tg] >= mi:
                    S('ERR', 'S07', 'answer link points to %s, which is not an earlier message' % tg, m, no, ln)
                else:
                    if sender[tg] == snd: S('WARN', 'S07', 'answer link to a question of the same sender (%s)' % snd, m, no, ln)
                    if not (qt.startswith('⌜') and qt.endswith('⌝')):
                        S('ERR', 'S07', 'the second operand of r> must be a mention of the question', m, no, ln)
                    else:
                        q = norm(qt[1:-1])
                        if (tg, q) not in questions:
                            S('ERR', 'S07', 'the quoted question does not occur, letter for letter, as a question line of %s: a question with no target is marked a?, not answered (CP-9, CP-15)' % tg, m, no, ln)
                        else:
                            questions[(tg, q)][0] = True
                            # answers to ?= accumulate (Change 7); a yes-or-no question gets one answer per message
                            if (tg, q) in qtexts and q.startswith('?⊤'): S('ERR', 'S07', 'two answers to one yes-or-no question in one message (CP-9)', m, no, ln)
                            qtexts[(tg, q)] = no
            # S08 one question expression per message (CP-8, U-07); remember questions for later answer links
            if head in QUESTION:
                q = norm(ln)
                if (mid, q) in questions:
                    S('ERR', 'S08', 'the same question expression twice in one message (CP-8, U-07)', m, no, ln)
                else:
                    questions[(mid, q)] = [False, ln]
            # S09 request and outcome (CP-10)
            if head == 'r<' and len(t[2]) == 2 and t[2][1][0] == 'app' and t[2][1][1] == '▶':
                act = t[2][1][2]
                paired = False
                for ln2, no2 in body:
                    t2 = trees.get((mid, no2))
                    if t2 is None: continue
                    for n2, _ in walk(t2):
                        if n2[0] == 'app' and n2[1] == 'c■' and n2[2] == act and t2[0] == 'app' and t2[1] == '?⊤': paired = True
                if not paired:
                    S('WARN', 'S09', 'request without its outcome question ?⊤(c■(…)) in the same message (CP-10)', m, no, ln)
            # S10 tense outside a context (CP-14, CP-15 cause 1)
            for n, stk in walk(t):
                if n[0] == 'app' and n[1] in TENSE and 'c⊃' not in stk:
                    S('WARN', 'S10', 'tense root %s outside c⊃(zt,…): no reference time, the reader answers a? (CP-14)' % n[1], m, no, ln); break
            # S11 withdrawal (CP-13, Change 3)
            if head == 'r↻':
                a = t[2][0] if t[2] else None
                if a is None or a[0] != 'name' or not a[1].startswith('zU'):
                    S('WARN', 'S11', 'r↻ in a session names a whole message (CP-13)', m, no, ln)
                elif a[1] not in order or order[a[1]] >= mi:
                    S('ERR', 'S11', 'r↻ names %s, which is not an earlier message' % a[1], m, no, ln)
                elif sender[a[1]] != snd:
                    S('ERR', 'S11', 'only the sender of %s may revise it (CP-13)' % a[1], m, no, ln)
            # S14 scaffolds for referent names only (CP-7, U-31)
            if head == 'd≔' and len(t[2]) == 2 and t[2][0][0] == 'name' and t[2][1][0] == 'mention' and t[2][1][1][0] == 'raw':
                nm = t[2][0][1]
                if nm.startswith(('zp', 'zq', 'zr', 'zh')):
                    S('WARN', 'S14', 'scaffold (quoted English) for the claim name %s: Level G allows scaffolds for referent names only (CP-7, U-31)' % nm, m, no, ln)
            # S16 attribution of the sender's own line (U-39)
            for n, _ in walk(t):
                if n[0] == 'attr' and n[1][0] == 'name' and n[1][1] == snd:
                    S('WARN', 'S16', 'attribution to the sender itself (%s): the header already says who sent it (U-39)' % snd, m, no, ln); break
            # S15 acceptance of a definition (CP-12)
            for n, stk in walk(t):
                if n[0] == 'app' and n[1] == 'a=' and n[2] and n[2][0][0] == 'app' and n[2][0][1] == 'd≔' and n[2][0][2] and n[2][0][2][0][0] == 'name':
                    nm = n[2][0][2][0][1]
                    if not any(p[0] < mi and p[1] != snd and p[2] == nm for p in sent_p):
                        S('WARN', 'S15', 'a=(d≔(%s,…)) without an earlier p↗(d≔(%s,…)) by another participant (CP-12)' % (nm, nm), m, no, ln)
            for n, stk in walk(t):
                if n[0] == 'app' and n[1] == 'p↗' and n[2] and n[2][0][0] == 'app' and n[2][0][1] == 'd≔' and n[2][0][2] and n[2][0][2][0][0] == 'name':
                    sent_p.append((mi, snd, n[2][0][2][0][1]))
        # S12 receipt only when nothing else refers to the previous message (Change 9)
        if mi > 0:
            prev = msgs[mi - 1]['id']
            has_receipt = any((trees.get((mid, no)) or ('',))[0] == 'app' and trees[(mid, no)][1] == 'a.' for _, no in body)
            refs_prev = any(('r>(' + prev) in norm(ln) or ('r@' in ln and (',' + prev + ')') in norm(ln)) for ln, _ in body)
            if has_receipt and refs_prev:
                S('WARN', 'S12', 'a receipt line next to other lines that refer to the previous message (Change 9)', m)
    if cand_use:
        rep.add(2, 'NOTE', 'S05', 'CANDIDATE roots used (status P, read as candidate, no recorded reader agreement): ' + ', '.join('%s x%d' % (k, v) for k, v in sorted(cand_use.items())))
    if free_ref:
        rep.add(2, 'NOTE', 'S06', 'r@ names that the target message does not declare with d≔ (free standing names are allowed): ' + ', '.join('%s in %s' % k for k in sorted(free_ref)))
    # unanswered questions (information)
    last = msgs[-1]['id']
    un = [v[1] for (mid, _), v in questions.items() if not v[0] and mid != last]
    if un: rep.add(2, 'NOTE', 'S17', '%d question(s) of earlier messages have no answer link, for example: %s' % (len(un), un[0][:70]))
    if len(msgs) < 10:
        rep.add(2, 'NOTE', 'S18', '%d messages; sessions beyond nine messages have not been exercised (L0 evidence status)' % len(msgs))


# ---------------------------------------------------------------- layer 3: plausibility (warnings only)
def layer3(msgs, mod, T, extra, trees, res, decl, rep):
    P = lambda code, msg, m, no=None, text=None: rep.add(3, 'WARN', code, msg, m['id'], no, text)
    used_later = {}
    for m in msgs:
        for ln in m['lines']:
            for nm, tg in re.findall(r'r@\((z[A-Za-z0-9]+),(zU[A-Za-z0-9]+)\)', ln):
                used_later.setdefault(tg, set()).add(nm)
    for m in msgs:
        mid = m['id']
        body = list(zip(m['lines'], m['nos']))[1:]
        sup, unk, req, seen = {}, {}, {}, {}
        for ln, no in body:
            t = trees.get((mid, no))
            if t is None or t[0] != 'app': continue
            head = t[1]
            # P02 duplicate line
            if norm(ln) in seen and not ln.startswith('d≔('):
                P('P02', 'the same line twice in one message', m, no, ln)
            seen[norm(ln)] = no
            if head in ('g←', 'u?', 'r□'):
                x = inner(ln, head)
                if x is not None:
                    (sup if head == 'g←' else unk if head == 'u?' else req)[norm(x)] = no
            # P09 trivial comparison
            for n, _ in walk(t):
                if n[0] == 'app' and n[1] in ('m>', 'r→') and len(n[2]) == 2 and n[2][0] == n[2][1] and n[2][0][0] != 'math':
                    P('P09', 'both operands of %s are identical: %s' % (n[1], 'false by definition' if n[1] == 'm>' else 'true by definition'), m, no, ln)
            # P03 zE used without a declaration in this message
            for n, stk in walk(t):
                if n[0] == 'name' and n[1].startswith('zE') and n[1] not in decl[mid] and not (stk and stk[-1] == 'r@'):
                    P('P03', 'the expression name %s is used but not declared with d≔ in this message (D3 3.3)' % n[1], m, no, ln); break
            # plug-ins for the open-build roots, active only when the table holds them
            if 'p◑' in extra:
                for n, _ in walk(t):
                    if n[0] == 'app' and n[1] == 'p◑' and len(n[2]) == 3:
                        v = num_value(n[2][1])
                        if v is not None and not (0 <= v <= 1):
                            P('P05', 'p◑ with the number %s: a probability is from 0 to 1 (the checker does not test it)' % v, m, no, ln)
            if 'b≬' in extra:
                for n, _ in walk(t):
                    if n[0] == 'app' and n[1] == 'b≬' and len(n[2]) == 3:
                        lo, hi = num_value(n[2][1]), num_value(n[2][2])
                        if lo is not None and hi is not None and lo > hi:
                            P('P08', 'b≬ with lo %s above hi %s: the range is empty' % (lo, hi), m, no, ln)
            if 'c⌗' in extra or 'm⌗' in extra:
                for n, _ in walk(t):
                    if n[0] == 'app' and n[1] in ('r→', 'm>') and len(n[2]) == 2:
                        h = [x[1] if x[0] == 'app' else None for x in n[2]]
                        if ('c⌗' in h or '#' in h) and 'm⌗' in h:
                            P('P07', 'a count is %s a quantity with a unit: different kinds of quantity (the checker does not test it)' % ('equated with' if n[1] == 'r→' else 'compared with'), m, no, ln)
        # P01 supplied and not supplied
        def neg(x):
            y = inner(x, 'n¬'); return y
        for x, no in sup.items():
            y = neg(x)
            if y is not None and y in sup: P('P01', 'P and not-P both supplied in one message (lines %d and %d)' % (sup[y], no), m, no)
            if x in unk: P('P01', 'the same claim supplied and marked unknown in one message (lines %d and %d)' % (no, unk[x]), m, no)
        for x, no in req.items():
            y = neg(x)
            if y is not None and y in req: P('P01', 'a requirement and its prohibition in one message (lines %d and %d)' % (req[y], no), m, no)
        # plug-in: undertaking and refusal of the same act
        if 'u⊕' in extra and 'd⊖' in extra:
            und, dec = {}, {}
            for ln, no in body:
                t = trees.get((mid, no))
                if t is None or t[0] != 'app': continue
                if t[1] == 'u⊕' and t[2]: und[repr(t[2][0])] = no
                if t[1] == 'd⊖' and t[2]: dec[repr(t[2][0])] = no
            for a, no in und.items():
                if a in dec: P('P06', 'the same act undertaken (line %d) and declined (line %d) in one message' % (no, dec[a]), m, no)
        # P04 declared names never used (information in the form of a warning only when none of them is used anywhere)
        for ln, no in body:
            t = trees.get((mid, no))
            if t is not None and t[0] == 'app' and t[1] == 'd≔' and t[2] and t[2][0][0] == 'name':
                nm = t[2][0][1]
                others = [l2 for l2, n2 in zip(m['lines'], m['nos']) if n2 != no]
                if not any(re.search(r'(?<![A-Za-z0-9])' + re.escape(nm) + r'(?![A-Za-z0-9])', l2) for l2 in others) and nm not in used_later.get(mid, ()):
                    rep.add(3, 'NOTE', 'P04', 'declared name %s is not used anywhere else' % nm, mid, no, ln)


# ---------------------------------------------------------------- layer 4: English
def layer4(msgs, mod, trees, rep):
    tot = {'chars': 0, 'seg_gate': 0, 'seg_strict': 0, 'lines': 0, 'lines_en': 0, 'segs': 0}
    seen_text, restated = {}, 0
    rows = []
    for m in msgs:
        body = m['lines'][1:]
        ch = sum(len(l) for l in body)
        g = sum(len(x) for l in body for x in inner_mentions(l) if ' ' in x)
        st = 0; ns = 0; en_lines = 0
        for l in body:
            en_here = False
            for x in top_mentions(l):
                try: mod.parse(x); is_en = False
                except mod.Err: is_en = True
                if is_en:
                    st += len(x); ns += 1; en_here = True
                    key = norm(x)
                    if key in seen_text and seen_text[key] != m['id']: restated += 1
                    seen_text.setdefault(key, m['id'])
            en_lines += en_here
        rows.append((m['id'], len(body), ch, g, st, en_lines))
        tot['chars'] += ch; tot['seg_gate'] += g; tot['seg_strict'] += st; tot['lines'] += len(body); tot['lines_en'] += en_lines; tot['segs'] += ns
    lines = ['%-8s %5s %6s %10s %12s %9s' % ('message', 'lines', 'chars', 'gate-share', 'strict-share', 'EN-lines')]
    for mid, nl, ch, g, st, en in rows:
        lines.append('%-8s %5d %6d %9.0f%% %11.0f%% %9d' % (mid, nl, ch, 100.0 * g / ch if ch else 0, 100.0 * st / ch if ch else 0, en))
    c = tot['chars'] or 1
    lines.append('%-8s %5d %6d %9.0f%% %11.0f%% %9d' % ('TOTAL', tot['lines'], tot['chars'], 100.0 * tot['seg_gate'] / c, 100.0 * tot['seg_strict'] / c, tot['lines_en']))
    rep.english = lines
    rep.add(4, 'NOTE', 'EN1', 'English share of the text: gate-pack measure %.0f%%, strict measure %.0f%%; %d of %d lines hold English text; %d scaffold(s) restated in a later message'
            % (100.0 * tot['seg_gate'] / c, 100.0 * tot['seg_strict'] / c, tot['lines_en'], tot['lines'], restated))


# ---------------------------------------------------------------- output
def print_report(rep, path, info, layers, strict):
    names = {1: 'FORM', 2: 'SESSION', 3: 'PLAUSIBILITY (warnings only)', 4: 'ENGLISH (a measure)'}
    print('SILEX-CHECK  %s' % path)
    print('table: %s  sha256 %s%s' % (info['table'], info['table_sha'][:16], ('  +%d roots: %s' % (len(info['extra']), ' '.join(info['extra']))) if info['extra'] else ''))
    for L in (1, 2, 3, 4):
        if str(L) not in layers: continue
        e, w = rep.count('ERR', L), rep.count('WARN', L)
        verdict = ('FAIL' if e else 'PASS') if L in (1, 2) else ('%d warning(s)' % w if L == 3 else 'measure')
        print('\n[%d %s]  %s   ERR %d  WARN %d  NOTE %d' % (L, names[L], verdict, e, w, rep.count('NOTE', L)))
        for i in rep.items:
            if i['layer'] != L: continue
            where = ('%s:%s ' % (i['message'], i['line'])) if i['message'] else ''
            print('  %-4s %-9s %s%s' % (i['sev'], i['code'], where, i['msg']))
            if i['text'] and i['sev'] in ('ERR', 'WARN'): print('       | %s' % i['text'][:150])
        if L == 4 and hasattr(rep, 'english'):
            for l in rep.english: print('  ' + l)
    fail = rep.count('ERR') > 0 or (strict and rep.count('WARN') > 0)
    print('\nRESULT: %s   (ERR %d, WARN %d)   A pass is evidence of form, protocol and plausibility, not of shared meaning.' % ('FAIL' if fail else 'PASS', rep.count('ERR'), rep.count('WARN')))
    return fail


def cmd_check(args):
    path, table, base, layers, js, strict = None, None, None, '1234', False, False
    i = 0
    while i < len(args):
        a = args[i]
        if a == '--table': table = args[i + 1]; i += 2
        elif a == '--base': base = args[i + 1]; i += 2
        elif a == '--layers': layers = args[i + 1]; i += 2
        elif a == '--json': js = True; i += 1
        elif a == '--strict': strict = True; i += 1
        elif a.startswith('--'): raise Usage('unknown option %s' % a)
        else: path = a; i += 1
    if not path: raise Usage('check needs a FILE')
    mod, entries, info = load(base, table)
    if not os.path.isfile(path): raise Usage('no such file: %s' % path)
    msgs = parse_file(path)
    if not msgs:
        raise Usage('%s has no message: start each message with a line "=== <message id> <sender> ===" or start the file with the header m▤(zU...,zk...)' % path)
    rep = run(msgs, mod, entries, info, layers)
    if js:
        fail = rep.count('ERR') > 0 or (strict and rep.count('WARN') > 0)
        print(json.dumps({'file': path, 'table': info, 'result': 'FAIL' if fail else 'PASS', 'findings': rep.items,
                          'english': getattr(rep, 'english', [])}, ensure_ascii=False, indent=1))
        return 1 if fail else 0
    return 1 if print_report(rep, path, info, layers, strict) else 0


def cmd_line(args):
    table = base = None; expr = None; i = 0
    while i < len(args):
        if args[i] == '--table': table = args[i + 1]; i += 2
        elif args[i] == '--base': base = args[i + 1]; i += 2
        else: expr = args[i]; i += 1
    if not expr: raise Usage('line needs an expression')
    mod, entries, info = load(base, table)
    T = tiers(entries)
    try:
        cat, basis, lv, warns = mod.check_line(expr, mod.Env())
        print('OK  category %s  basis %s%s' % (cat, '+'.join(basis) if basis else '-', ('  ' + ' | '.join(warns)) if warns else ''))
        rc = 0
    except mod.Err as e:
        print('ERR %s' % e); rc = 1
    try:
        t = mod.parse(expr)
        for r in sorted(set(roots_used(t))):
            if r in T: print('  root %-4s status %-3s tier %s' % (r, T[r][0], T[r][1]))
    except mod.Err:
        pass
    return rc


# ---------------------------------------------------------------- selftest
GOOD = """=== zUa1 zkA ===
m▤(zUa1,zkA)
d≔(zo1,⌜the release file⌝)
d≔(zcr1,⌜the published checksum of the release file⌝)
d≔(zm1,⌜publish the release file⌝)
d≔(zm2,⌜check the signature of the release file⌝)
d≔(zq1,v⊨(zo1,zcr1))
g←(zq1)
r<(zkB,▶(zm2))
?⊤(c■(zm2))
?⊤(zq1)
=== zUb1 zkB ===
m▤(zUb1,zkB)
r>(zUa1,⌜?⊤(c■(zm2))⌝,u?(c■(r@(zm2,zUa1))))
r>(zUa1,⌜?⊤(zq1)⌝,g←(r@(zq1,zUa1)))
p↗(d≔(zh1,n¬(r@(zq1,zUa1))))
=== zUa2 zkA ===
m▤(zUa2,zkA)
a=(d≔(zh1,n¬(r@(zq1,zUa1))))
"""


def _mut(text, old, new):
    assert old in text, old
    return text.replace(old, new, 1)


def _raises_usage(f):
    try: f()
    except Usage: return True
    return False


def _bad_ext(base_e):
    d = tempfile.mkdtemp(prefix='sc_bad_')
    try:
        bad = list(base_e); bad[0] = dict(bad[0], root='zz')
        p = os.path.join(d, 'bad.json'); json.dump(bad, open(p, 'w', encoding='utf-8'), ensure_ascii=False)
        load(None, p, 'bad')
    finally:
        shutil.rmtree(d, ignore_errors=True)


def selftest():
    mod, entries, info = load()
    ok = True
    def case(name, cond):
        nonlocal ok
        print('  %-4s %s' % ('ok' if cond else 'FAIL', name)); ok = ok and cond
    def sess(text, layers='1234', ents=None, inf=None, m=None):
        d = tempfile.mkdtemp(prefix='sc_st_'); p = os.path.join(d, 's.session'); open(p, 'w', encoding='utf-8').write(text)
        try: return run(parse_file(p), m or mod, ents or entries, inf or info, layers)
        finally: shutil.rmtree(d, ignore_errors=True)
    def codes(rep, sev, layer):
        return {i['code'] for i in rep.items if i['sev'] == sev and i['layer'] == layer}
    print('pins and loading')
    case('base files match the pins (load succeeded)', True)
    print('layer 1: must pass')
    for l in ['g←(n¬(v⊨(zo1,zcr1)))', 'g←(i→(v⊨(zo1,zcr1),v⊨(zo1,zcr2)))', 'g←(c↝(zq1,zq2))', 'u?(v⊨(zo1,zcr2))', '?⊤(v⊨(zo1,zcr1))', 'a?(⌜g←(zq1)⌝)']:
        case('pass  ' + l, mod.check_line(l, mod.Env())[0] in ('Ln', 'Q'))
    print('layer 1: must fail')
    for l, c in [('g←(m>(zv1,✠(10)))', 'E-CAT'), ('g←(r→(✠(1.5),✠(1)))', 'E-MATH'), ('d≔(zv2,v=(zo1,zv1))', 'E-CAT'), ('g←(u±(zv1,✠(2)))', 'E-MATHPLACE')]:
        env = mod.Env()
        for pre in ['d≔(zo1,⌜x⌝)', 'd≔(zS1,⌜y⌝)', 'd≔(zv1,#(zS1))']:
            try: mod.check_line(pre, env)
            except mod.Err: pass
        try: mod.check_line(l, env); got = None
        except mod.Err as e: got = e.code
        case('fail  %s -> %s' % (l, c), got == c)
    print('layers 2 to 4 on a good session')
    r = sess(GOOD)
    case('the good session has no ERR in layers 1 and 2', r.count('ERR') == 0)
    case('the good session has no WARN in layers 2 and 3', r.count('WARN', 2) == 0 and r.count('WARN', 3) == 0)
    print('layer 2: each mutation must raise its code')
    muts = [
        ('S01 wrong header', _mut(GOOD, 'm▤(zUb1,zkB)', 'm▤(zUb9,zkB)'), 'ERR', 2, 'S01'),
        ('S03 bare claim line', _mut(GOOD, 'g←(zq1)\nr<', 'zq1\nr<'), 'ERR', 2, 'S03'),
        ('S05 PARKED root', _mut(GOOD, 'g←(zq1)\nr<', 'g←(k✓(zq1))\nr<'), 'ERR', 2, 'S05'),
        ('S06 r@ to a later message', _mut(GOOD, 'a=(d≔(zh1,n¬(r@(zq1,zUa1))))', 'a=(d≔(zh1,n¬(r@(zq1,zUa9))))'), 'ERR', 2, 'S06'),
        ('S06 pointer use of r@', _mut(GOOD, 'a=(d≔(zh1,n¬(r@(zq1,zUa1))))', 'a=(d≔(zh1,n¬(r@(zq1,zo1))))'), 'ERR', 2, 'S06'),
        ('S07 answer to a question that is not there', _mut(GOOD, '⌜?⊤(zq1)⌝', '⌜?⊤(zq2)⌝'), 'ERR', 2, 'S07'),
        ('S07 two answers to one question', _mut(GOOD, 'p↗(d≔(zh1', 'r>(zUa1,⌜?⊤(zq1)⌝,u?(r@(zq1,zUa1)))\np↗(d≔(zh1'), 'ERR', 2, 'S07'),
        ('S08 same question twice', _mut(GOOD, '?⊤(zq1)\n=== zUb1', '?⊤(zq1)\n?⊤(zq1)\n=== zUb1'), 'ERR', 2, 'S08'),
        ('S11 withdrawal of the other sender message', _mut(GOOD, 'a=(d≔(zh1,n¬(r@(zq1,zUa1))))', 'r↻(zUb1)'), 'ERR', 2, 'S11'),
        ('S02 d≔ after the body began', _mut(GOOD, 'g←(zq1)\nr<(zkB,▶(zm2))', 'g←(zq1)\nd≔(zo7,⌜late⌝)\nr<(zkB,▶(zm2))'), 'WARN', 2, 'S02'),
        ('S04 conjunction under a force root', _mut(GOOD, 'g←(zq1)\nr<', 'g←(∧(zq1,zq1))\nr<'), 'WARN', 2, 'S04'),
        ('S09 request without outcome question', _mut(GOOD, '?⊤(c■(zm2))\n?⊤(zq1)', '?⊤(zq1)'), 'WARN', 2, 'S09'),
        ('S10 tense outside a context', _mut(GOOD, 'g←(zq1)\nr<', 'g←(t≺(▶(zm1)))\nr<'), 'WARN', 2, 'S10'),
        ('S14 scaffold for a claim name', _mut(GOOD, 'd≔(zq1,v⊨(zo1,zcr1))', 'd≔(zq1,⌜the file is good⌝)'), 'WARN', 2, 'S14'),
        ('S15 acceptance without a proposal', _mut(GOOD, 'p↗(d≔(zh1,n¬(r@(zq1,zUa1))))', 'g←(r@(zq1,zUa1))'), 'WARN', 2, 'S15'),
        ('S16 attribution to the sender itself', _mut(GOOD, 'g←(zq1)\nr<', 'g←(zkA:zq1)\nr<'), 'WARN', 2, 'S16'),
    ]
    for name, text, sev, layer, code in muts:
        try:
            rr = sess(text)
            case(name, code in codes(rr, sev, layer))
        except Exception as e:
            case(name + '  (raised %s)' % type(e).__name__, False)
    print('layer 3')
    rr = sess(_mut(GOOD, 'g←(zq1)\nr<', 'g←(zq1)\ng←(n¬(zq1))\nr<'), '3')
    case('P01 P and not-P supplied', 'P01' in codes(rr, 'WARN', 3))
    rr = sess(_mut(GOOD, 'g←(zq1)\nr<', 'g←(zq1)\ng←(zq1)\nr<'), '3')
    case('P02 duplicate line', 'P02' in codes(rr, 'WARN', 3))
    rr = sess(_mut(GOOD, 'g←(zq1)\nr<', 'g←(r→(zE9,zE9))\nr<'), '3')
    case('P03 and P09 undeclared zE, trivial comparison', {'P03', 'P09'} <= codes(rr, 'WARN', 3))
    print('layer 4')
    rr = sess(GOOD, '4')
    case('English measure is reported', any(i['code'] == 'EN1' for i in rr.items))
    print('plug-in rules (open-build roots) on a synthetic extension table')
    base_e = json.load(open(os.path.join(find_base(), 'data_table.json'), encoding='utf-8'))
    tpl = [e for e in base_e if e['status'] == 'P'][0]
    sigs = [('c⌗', '(s:Co)->Ex'), ('m⌗', '(x:Ref,q:Va)->Ex'), ('u⊕', '(a:Act)->Ln'), ('d⊖', '(a:Act)->Ln'), ('b≬', '(e:Ex,lo:Ex,hi:Ex)->P'), ('p◑', '(c:P,p:Ex,basis:Ref)->P')]
    ext = list(base_e)
    for k, (root, sg) in enumerate(sigs):
        e = dict(tpl); e.update({'id': 'X%03d' % (k + 1), 'root': root, 'symbol': root, 'sig': sg, 'status': 'P', 'family': '2.5'}); ext.append(e)
    d = tempfile.mkdtemp(prefix='sc_ext_'); tp = os.path.join(d, 'ext.json'); json.dump(ext, open(tp, 'w', encoding='utf-8'), ensure_ascii=False)
    try:
        xmod, xent, xinf = load(None, tp, 'ext')
    finally:
        shutil.rmtree(d, ignore_errors=True)
    pre = "=== zUa1 zkA ===\nm▤(zUa1,zkA)\nd≔(zm1,⌜x⌝)\nd≔(zo1,⌜x⌝)\nd≔(zv1,⌜x⌝)\nd≔(zS1,⌜x⌝)\nd≔(zS4,⌜x⌝)\nd≔(zq1,⌜x⌝)\n"
    def plug(line):
        return codes(sess(pre + line + "\n", '123', xent, xinf, xmod), 'WARN', 3)
    case('P05 probability 9', 'P05' in plug('g←(p◑(zq1,✠(9),zS4))'))
    case('P05 silent for 3/4', 'P05' not in plug('g←(p◑(zq1,✠(÷(3,4)),zS4))'))
    case('P06 undertaking and refusal of one act', 'P06' in plug('u⊕(▶(zm1))\nd⊖(▶(zm1))'))
    case('P06 silent for two different acts', 'P06' not in plug('u⊕(▶(zm1))\nd⊖(▶(zo1))'))
    case('P07 count equated with a quantity', 'P07' in plug('g←(r→(c⌗(zS1),m⌗(zo1,zv1)))'))
    case('P08 range with ends the wrong way', 'P08' in plug('g←(b≬(c⌗(zS1),✠(10),✠(4)))'))
    case('P08 silent for equal ends', 'P08' not in plug('g←(b≬(c⌗(zS1),✠(10),✠(10)))'))
    case('the extension must keep the 195 base entries', _raises_usage(lambda: _bad_ext(base_e)))
    print('plug-in rules need the extended table: inactive without it')
    rr = sess(_mut(GOOD, 'g←(zq1)\nr<', 'g←(r→(zv1,zv1))\nr<'), '3')
    case('P09 still fires on the base table', 'P09' in codes(rr, 'WARN', 3))
    print('SELFTEST ' + ('PASS' if ok else 'FAIL'))
    return 0 if ok else 1


def main(a):
    try:
        if not a or a[0] in ('-h', '--help', 'help'):
            print(__doc__); return 0 if a else 2
        if a[0] == 'check': return cmd_check(a[1:])
        if a[0] == 'line': return cmd_line(a[1:])
        if a[0] == 'selftest': return selftest()
        raise Usage('unknown command %s' % a[0])
    except Usage as e:
        print('USAGE/INTEGRITY: %s' % e); return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
