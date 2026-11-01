#!/usr/bin/env python3
"""UCL reference consistency checker, RULEBOOK CANDIDATE (ucl_check_rb.py). It is the pinned ucl_check.py plus the grammar of the rulebook:
(1) one-line declarations d≔(n1,..,nk,def1,..,defk); (2) n0 (in r2: the word null) for an argument that is not available; (3) up to 8 arguments, the core places then
role markers (each at most once) on every root except the joiners, binders and the action roots (which already have them); (4) ?⊙ binds its variable.
NOT the project checker, NOT adopted. The pinned checker is unchanged.
G3 (Owner ruling, 1 Nov 07:29): the placeholder is written n0, not the word null. g3 = g2 + this one change in the tokenizer + three message texts; the table entry n0 is an atom. g2 = the rulebook candidate + NO_DETAIL for m▤ and r>.
Implements the type and composition rules of the Candidate Master Draft so that the document's own examples can be
validated against the document's own signature table. A PASS means: the expression is well-formed under the CANDIDATE rules.
It is not evidence that two readers would recover the same meaning.
Usage:  python3 -I ucl_check.py check "<expression>"        python3 -I ucl_check.py file <file>  (lines share declarations)
"""
import re, sys, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
TABLE = json.load(open(os.path.join(HERE, 'data_table.json'), encoding='utf-8'))
RANK = {'E': 5, 'Ep': 4, 'P': 3, 'U': 2, 'N': 1, 'X': 0}
PARENTS = {'Ag': ['Ref'], 'Ob': ['Ref'], 'Va': ['Ref'], 'Ct': ['Va'], 'Co': ['Ref'], 'Pm': ['Co'], 'Me': ['Ref', 'Act'], 'Tm': ['Ref'], 'Cr': ['Ref'],
           'Ms': ['Ref'], 'Mn': ['Ref'], 'Var': ['Ref'], 'Dir': ['Ln'], 'CDir': ['Dir'], 'Req': ['Ln'], 'Dc': ['Ln'], 'Q': ['Ln'], 'Cx': ['Ln']}
PREFIX = [('zcr', 'Cr'), ('zk', 'Ag'), ('zm', 'Me'), ('zo', 'Ob'), ('zv', 'Va'), ('zS', 'Co'), ('zE', 'Ex'), ('zt', 'Tm'), ('zU', 'Ms'),
          ('zp', 'P'), ('zq', 'P'), ('zr', 'P'), ('zh', 'P')]
NAME = re.compile(r'z(?:cr|k|m|o|v|S|E|t|U|p|q|r|h)[A-Za-z0-9]*')
class Err(Exception):
    def __init__(self, code, msg): self.code = code; self.msg = msg; super().__init__('%s: %s' % (code, msg))
def anc(c):
    out = {c}; todo = [c.split('[')[0] if c.startswith('Mn[') else c]
    if c.startswith('Mn['): out.add('Mn')
    while todo:
        x = todo.pop()
        for p in PARENTS.get(x, []):
            if p not in out: out.add(p); todo.append(p)
    return out
def fits(cat, slot):
    if cat == 'Null': return True   # RB: null fits every place
    if slot in ('Any', None): return True
    for s in slot.split('|'):
        if s == 'Any' or s in anc(cat): return True
        if s.startswith('Mn[') and cat == s: return True
    return False
# ---------- signature table ----------
SIG = {}
def parse_sig(s, default_status):
    alts = []
    s = s.strip()
    if s.startswith('atom'):
        m = re.match(r'atom(?::(\w+))?$', s); alts.append(dict(atom=True, res=m.group(1) or 'Ref', status=default_status, args=[])); return alts
    poly = None
    m = re.search(r'\s+@=\{([^}]*)\}\s*$', s)
    if m: poly = m.group(1).split(','); s = s[:m.start()]
    for part in s.split(' / '):
        st = default_status
        m = re.match(r'^(Ep|E|P|U|N|X):(\(.*)$', part.strip())
        if m: st, part = m.group(1), m.group(2)
        m = re.match(r'^\((.*)\)->(\S+)$', part.strip())
        if not m: raise ValueError('bad sig ' + part)
        args = []
        if m.group(1).strip():
            for a in re.split(r',(?![^\[]*\])', m.group(1)):
                role, cat = a.split(':', 1); rep = ''
                if cat.endswith('*') or cat.endswith('+'): rep = cat[-1]; cat = cat[:-1]
                args.append(dict(role=role, cat=cat, rep=rep))
        alts.append(dict(atom=False, args=args, res=m.group(2), status=st, poly=poly))
    return alts
for e in TABLE:
    if e['sig'] and e['root'] != '✠': SIG[e['root']] = (e, parse_sig(e['sig'], e['status']))
ROOTS = sorted(SIG.keys() | {e['root'] for e in TABLE if e['root'] not in ('⌜ ⌝', '✠')} | {'⌜'}, key=lambda x: -len(x))
SIG['d≔'] = (next(e for e in TABLE if e['root'] == 'd≔'), [])
ACTION_ROOTS = {'cƒ', 'o→', 'a+'}
RMROOTS = {e['root'] for e in TABLE if e['sig'] and e['sig'].endswith('->Rm')}   # RB: the role markers
NO_DETAIL = ACTION_ROOTS | RMROOTS | {'∧', 'a|', 's≺', '∃', '?=', '?⊙', 'r@', 'd≔', 'm▤', 'r>'}   # RB: roots that take no extra role markers
MAXARGS = 8   # RB: core places plus role markers, at most
STATE_E = {'h⊡'}; STATE_N = {'⊡', 'v⊨', '∈', 's=', 'k✓', 'i≡'}
WIT = {('h◇', 'i→', 0), ('h◇', 'p↗', 0), ('p◇', 'n¬', 0)}
# ---------- parser ----------
def parse(src):
    s = src.strip(); pos = [0]
    def ws():
        while pos[0] < len(s) and s[pos[0]] in ' \t': pos[0] += 1
    def mention():
        i = pos[0] + 1; depth = 1
        while i < len(s) and depth:
            if s[i] == '⌜': depth += 1
            if s[i] == '⌝': depth -= 1
            i += 1
        if depth: raise Err('E-SYNTAX', 'unclosed mention')
        inner = s[pos[0]+1:i-1]; pos[0] = i
        try: node = parse(inner)
        except Err: node = ('raw', inner)
        return ('mention', node)
    def math():
        i = pos[0] + 2; depth = 1
        while i < len(s) and depth:
            if s[i] == '(': depth += 1
            if s[i] == ')': depth -= 1
            i += 1
        if depth: raise Err('E-SYNTAX', 'unclosed ✠(')
        raw = s[pos[0]+2:i-1]; pos[0] = i; return ('math', raw)
    def expr():
        ws()
        if pos[0] >= len(s): raise Err('E-SYNTAX', 'expression expected')
        if s[pos[0]] == '⌜': return mention()
        if s.startswith('✠(', pos[0]): return math()
        if s.startswith('n0', pos[0]) and (pos[0] + 2 >= len(s) or not (s[pos[0] + 2].isalnum() or s[pos[0] + 2] == '(')):
            pos[0] += 2; return ('null',)   # G3: n0 is the placeholder (the word null is retired)
        m = NAME.match(s, pos[0])
        if m and not any(s.startswith(r, pos[0]) for r in ROOTS if r[0] == 'z'):
            name = m.group(0)
            pos[0] = m.end()
            if pos[0] < len(s) and s[pos[0]] == ':' and name.startswith('zk'):
                pos[0] += 1; return ('attr', ('name', name), expr())
            return ('name', name)
        for r in ROOTS:
            if s.startswith(r, pos[0]):
                pos[0] += len(r)
                if pos[0] < len(s) and s[pos[0]] == '(':
                    pos[0] += 1; args = []
                    ws()
                    if pos[0] < len(s) and s[pos[0]] == ')': pos[0] += 1; return ('app', r, args)
                    while True:
                        args.append(expr()); ws()
                        if pos[0] >= len(s): raise Err('E-SYNTAX', 'missing )')
                        if s[pos[0]] == ',': pos[0] += 1; continue
                        if s[pos[0]] == ')': pos[0] += 1; break
                        raise Err('E-SYNTAX', 'unexpected %r' % s[pos[0]])
                    return ('app', r, args)
                return ('atom', r)
        raise Err('E-LEX', 'unknown token at %r' % s[pos[0]:pos[0]+8])
    if s.startswith('d≔('):
        pos[0] = 3; items = [expr()]; ws()
        while pos[0] < len(s) and s[pos[0]] == ',':   # RB: d≔ takes 2k arguments (names, then definitions)
            pos[0] += 1; items.append(expr()); ws()
        if pos[0] >= len(s) or s[pos[0]] != ')' or pos[0] + 1 != len(s): raise Err('E-SYNTAX', 'bad d≔')
        if len(items) < 2: raise Err('E-SYNTAX', 'd≔ needs two arguments')
        return ('app', 'd≔', items)
    n = expr(); ws()
    if pos[0] != len(s): raise Err('E-SYNTAX', 'trailing text %r' % s[pos[0]:pos[0]+10])
    return n
# ---------- math sublanguage ----------
MHEAD = {'+': 2, '−': 2, '×': 2, '÷': 2, '^': 2, '√': 1, 'sin': 1, 'cos': 1, 'ln': 1, '∫': 4, 'Σ': 4, 'lim': 3}
def mparse(t):
    t = t.strip()
    m = re.match(r'^(\+|−|×|÷|\^|√|sin|cos|ln|∫|Σ|lim)\((.*)\)$', t, re.S)
    if m:
        body = m.group(2); args = []; d = 0; cur = ''
        for ch in body:
            if ch == '(': d += 1
            if ch == ')': d -= 1
            if ch == ',' and d == 0: args.append(cur); cur = ''
            else: cur += ch
        args.append(cur)
        return (m.group(1), [mparse(a) for a in args])
    if re.fullmatch(r'0|[1-9][0-9]*', t): return ('num', t)
    if re.fullmatch(r'[a-z]', t): return ('var', t)
    if t == 'π': return ('pi', t)
    raise Err('E-MATH', 'not a term of S2-S4: %r' % t)
def mcheck(n, bound=frozenset()):
    k = n[0]
    if k in MHEAD:
        if len(n[1]) != MHEAD[k]: raise Err('E-MATH', 'head %s needs %d arguments' % (k, MHEAD[k]))
        if k in ('∫', 'Σ', 'lim'):
            f, v = n[1][0], n[1][1]
            if v[0] != 'var': raise Err('E-MATH', 'binder must be a letter')
            free = mcheck(f, bound | {v[1]})
            return free | set().union(*[mcheck(a, bound) for a in n[1][2:]])
        return set().union(*[mcheck(a, bound) for a in n[1]])
    if k == 'var': return set() if n[1] in bound else {n[1]}
    return set()

from fractions import Fraction
def mval(n, bind=None):
    """Definedness (TF-6 D4 / M12) for the math sublanguage. Returns ('def', Fraction|None) or ('undef', reason)."""
    k = n[0]
    if k == 'num': return ('def', Fraction(int(n[1])))
    if k in ('var', 'pi'): return ('def', None)
    args = [mval(a) if not (k in ('Σ', '∫', 'lim') and i == 0) else ('def', None) for i, a in enumerate(n[1])]
    for a in args:
        if a[0] == 'undef': return a
    v = [a[1] for a in args]
    if k in ('+', '−', '×'):
        if None in v: return ('def', None)
        return ('def', v[0] + v[1] if k == '+' else v[0] - v[1] if k == '−' else v[0] * v[1])
    if k == '÷':
        if v[1] == 0: return ('undef', 'division by zero')
        if None in v: return ('def', None)
        return ('def', v[0] / v[1])
    if k == '√':
        if v[0] is not None and v[0] < 0: return ('undef', 'square root of a negative number')
        return ('def', None)
    if k == 'ln':
        if v[0] is not None and v[0] <= 0: return ('undef', 'logarithm of a non-positive number')
        return ('def', None)
    if k == '^':
        a, b = v
        if a is None or b is None: return ('def', None)
        if a == 0: return ('def', Fraction(0)) if b > 0 else ('undef', '0 to a non-positive power')
        if a > 0:
            return ('def', a ** int(b)) if b.denominator == 1 and abs(b) < 64 else ('def', None)
        if b.denominator % 2 == 1: return ('def', None)
        return ('undef', 'negative base with an even or irrational exponent denominator')
    if k == 'Σ':
        lo, hi = v[2], v[3]
        if lo is not None and hi is not None and (lo.denominator != 1 or hi.denominator != 1): return ('undef', 'non-integer sum bound')
        if lo is not None and hi is not None and lo > hi: return ('def', Fraction(0))
        return ('def', None)
    return ('def', None)

# ---------- checker ----------
class Res:
    def __init__(s, cat, kind='n', basis=None, warns=None, tree=None): s.cat = cat; s.kind = kind; s.basis = set(basis or []); s.warns = list(warns or []); s.tree = tree
def prefix_cat(name):
    for p, c in PREFIX:
        if name.startswith(p): return c
    raise Err('E-LEX', 'name %s has no class prefix' % name)
class Env:
    def __init__(s): s.decl = {}; s.bound = set(); s.qvars = set(); s.nline = 0; s.header = False; s.mdefs = {}
def level(basis):
    return min([RANK[b] for b in basis] or [5])
def contains_var(node, v):
    if node[0] == 'name': return node[1] == v
    if node[0] == 'app': return any(contains_var(a, v) for a in node[2])
    if node[0] == 'attr': return contains_var(node[1], v) or contains_var(node[2], v)
    if node[0] == 'mention': return contains_var(node[1], v) if node[1][0] != 'raw' else False
    return False
def has_domain(body, v):
    if body[0] == 'app' and body[1] == '∈' and body[2] and body[2][0] == ('name', v): return True
    if body[0] == 'app' and body[1] == '∧': return any(has_domain(a, v) for a in body[2])
    return False
def check(node, exp, env, fr, parent=None, trace=None):
    """exp: expected category string (union with |) or None (top level). fr: frame dict (time, inq, in_math_ok)."""
    k = node[0]
    if k == 'name':
        name = node[1]; c = prefix_cat(name)
        if name in env.bound: c = env.bound[name] if isinstance(env.bound, dict) else c
        if c == 'Tm' and name not in env.decl and name not in env.qvars and not fr.get('declaring'): raise Err('E-UNDECL', 'time name %s not declared by d≔(%s,t)' % (name, name))
        r = Res(c, 'n')
        if c == 'Ex': r.mdef = env.mdefs.get(name)
        if exp and not fits(c, exp): raise Err('E-CAT', '%s is %s, a slot needs %s' % (name, c, exp))
        return r
    if k == 'mention':
        inner = node[1]; tag = 'Any'
        if inner[0] == 'app' and inner[1] in SIG:
            rs = {a['res'] for a in SIG[inner[1]][1] if not a.get('atom')}
            if 'Q' in rs: tag = 'Q'
            elif rs and rs <= {'Ln', 'Dir', 'Req', 'Dc', 'Cx', 'CDir'}: tag = 'Ln'
            elif 'P' in rs: tag = 'P'
            elif 'Act' in rs: tag = 'Act'
        elif inner[0] == 'attr': tag = 'P'
        cat = 'Mn[%s]' % tag if tag != 'Any' else 'Mn'
        if exp and not fits(cat, exp): raise Err('E-CAT', 'a mention of %s is not accepted here (slot needs %s)' % (tag, exp))
        return Res(cat, 'n', set())
    if k == 'raw': return Res('Any')
    if k == 'null':
        return Res('Null', 'n', set(), ['NU: n0: this argument is not supplied (not none, not zero)'])
    if k == 'math':
        t = mparse(node[1]); free = mcheck(t)
        r = Res('Ex', 'n', {'Ep'}, tree=None); r.free = free; r.mdef = mval(t)
        if exp and not fits('Ex', exp): raise Err('E-MATHPLACE', '✠ term not allowed here (closed list: cƒ object, r→, m>, zE definiens)')
        return r
    if k == 'atom':
        root = node[1]
        if root not in SIG: raise Err('E-UNSIG', 'root %s has no recorded signature (write a?)' % root)
        e, alts = SIG[root]
        if not alts or not alts[0].get('atom'):
            raise Err('E-UNSIG', 'root %s needs arguments or has no signature (write a?)' % root)
        a = alts[0]; cat = a['res']
        if exp and not fits(cat, exp): raise Err('E-CAT', 'atom %s is %s, slot needs %s' % (root, cat, exp))
        return Res(cat, 'n', {a['status']})
    if k == 'attr':
        ag = check(node[1], 'Ag', env, fr)
        inner = node[2]
        if inner[0] == 'app' and inner[1] in ('r→', 'm>'): raise Err('E-ATTR', 'A: is not authorized before a value claim or comparison (TF-5 T.3.6 M5 item 4)')
        STATUS = ('g←', 'h◇', 'p◇', 'u?', 'u~')
        if inner[0] == 'app' and inner[1] in STATUS and (exp is None or (fits('Ln', exp) and not fits('P', exp))):
            r = check(inner, None, env, fr, parent=('attr', 0))
            return Res('Ln', 'n', r.basis, r.warns)
        r = check(inner, 'P', env, fr, parent=('attr', 0))
        res = Res('P', r.kind, r.basis | ({'N'} if inner[0] == 'attr' else set()), r.warns)
        if exp and not fits('P', exp): raise Err('E-CAT', 'an attributed claim is a claim, slot needs %s' % exp)
        return res
    root, args = node[1], node[2]
    if root == 'd≔': return check_def(args, env, fr)
    if root not in SIG:
        if root in {e['root'] for e in TABLE}: raise Err('E-UNSIG', 'root %s has no recorded signature (write a?; do not invent an arity)' % root)
        raise Err('E-LEX', 'unknown root %s' % root)
    e, alts = SIG[root]
    if not alts: raise Err('E-UNSIG', 'root %s has no recorded signature (write a?)' % root)
    if alts[0].get('atom'): raise Err('E-ARITY', '%s is an atom and takes no arguments' % root)
    if root in ('∧', 'a|', 's≺'): return check_poly(root, alts[0], args, exp, env, fr, parent)
    if root == '?⊙': return check_choice(root, alts, args, exp, env, fr)   # RB
    if root == '∃' or root == '?=': return check_binder(root, alts, args, exp, env, fr)
    if root == 'r@': return check_rat(root, alts, args, exp, env, fr)
    det = []   # RB: trailing role markers are details of any root that takes none in its signature
    if root not in NO_DETAIL:
        kk = len(args); nmax = max([len([x for x in a_['args'] if not x['rep']]) for a_ in alts if not a_.get('atom')] or [0])
        while kk > 0 and ((args[kk-1][0] == 'app' and args[kk-1][1] in RMROOTS) or (args[kk-1][0] == 'null' and kk > nmax)): kk -= 1
        det = args[kk:]; args = args[:kk]
    # choose alternative by expected category
    cands = []
    for a in alts:
        res = a['res']
        if exp is None or fits(res if res != '=1' else 'Ref', exp): cands.append(a)
    lifted = False
    if not cands and exp and fits('P', exp) and any(a['res'] == 'Act' for a in alts) :
        cands = [a for a in alts if a['res'] == 'Act']; lifted = True
    if not cands: raise Err('E-CAT', '%s gives %s; the slot needs %s' % (root, '/'.join(sorted({a["res"] for a in alts})), exp))
    errs = []
    for a in cands:
        try:
            r = apply_alt(root, a, args, env, fr, parent)
            if lifted:
                r = Res('P', 'e', r.basis | {('E' if root in ACTION_ROOTS else 'N')}, r.warns)
            return add_details(root, r, det, len(args), env, fr)
        except Err as ex:
            fx = [x for x in a['args'] if not x['rep']]; rp = [x for x in a['args'] if x['rep']]
            fits_n = len(args) == len(fx) if not rp else len(args) >= len(fx)
            errs.append((0 if fits_n else 1, ex))
    errs.sort(key=lambda t: t[0])
    raise errs[0][1]
def apply_alt(root, a, args, env, fr, parent):
    sl = a['args']; fixed = [x for x in sl if not x['rep']]; rep = [x for x in sl if x['rep']]
    minn = len(fixed) + (1 if any(x['rep'] == '+' for x in rep) else 0)
    if len(args) < minn or (not rep and len(args) != len(fixed)) : raise Err('E-ARITY', '%s takes %s argument(s), got %d' % (root, len(fixed) if not rep else '%d or more' % minn, len(args)))
    if root in ACTION_ROOTS and len(args) > MAXARGS: raise Err('E-ARITY', '%s takes at most %d arguments, got %d' % (root, MAXARGS, len(args)))
    basis = {a['status']}; warns = []; kinds = []
    if root in ('h◇', 'p◇', 'u?', 'u~') and a['res'] == 'P':
        basis = {'E'} if parent and (root, parent[0], parent[1]) in WIT else {'N'}
    nfr = dict(fr)
    if root in ('s=', 's≈', 'm≡', 'd≢') and not fr.get('crit'): warns.append('CR: no criterion context encloses %s (OG-05): underspecified, mark a?' % root)
    if root in ('t≺', 't●', 't▷'):
        if not fr.get('time'): warns.append('RT: no enclosing c⊃(zt,…) names the reference time (T.3.1 item 2): tense unresolved unless the writer time is recoverable')
    seen_rm = set()
    for i, ar in enumerate(args):
        slot = (sl[i] if i < len(sl) and not sl[i]['rep'] else (rep[0] if rep else sl[-1]))
        cat = slot['cat']
        if root in ('t≺', 't●', 't▷') and ar[0] == 'app' and ar[1] == 'n¬':
            inner = ar[2][0] if ar[2] else None
            if inner is not None:
                ik = inner[1] if inner[0] == 'app' else None
                if ik in STATE_E: basis.add('E')
                elif ik in STATE_N: basis.add('N')
                else: raise Err('E-KIND', 'tense over a negation needs a state predicate (TF-5 T.3.1 item 6; TF-6 D3 allows h⊡ only): %s is not in the state registry' % ik)
        if root == 'c⊃' and i == 0 and ((ar[0] == 'name' and prefix_cat(ar[1]) == 'Cr') or (ar[0] == 'app' and ar[1] == '~' and ar[2] and ar[2][0][0] == 'name' and prefix_cat(ar[2][0][1]) == 'Cr')): nfr['crit'] = True
        if root == 'c⊃' and i == 0 and ((ar[0] == 'name' and prefix_cat(ar[1]) == 'Tm') or (ar[0] == 'app' and ar[1] == 'r@')): nfr['time'] = ar[1] if ar[0] == 'name' else 'r@'
        sub = check(ar, cat, env, nfr, parent=(root, i))
        if root in ACTION_ROOTS and i > 0 and ar[0] != 'null':
            rmroot = ar[1] if ar[0] == 'app' else None
            if rmroot in seen_rm: raise Err('E-ROLE', 'role marker %s occurs twice in one action' % rmroot)
            seen_rm.add(rmroot)
            if rmroot in ('⌘', '⚙', '↣', '☞', '☼', '⚓', '♙') and len(ar[2]) != 1: raise Err('E-ARITY', 'a role marker takes exactly one name')
        if root in ACTION_ROOTS and i > 0 and sub.cat not in ('Rm', 'Null'): raise Err('E-ROLE', 'later arguments of %s must be role markers' % root)
        basis |= sub.basis; warns += sub.warns; kinds.append(sub)
    if root in ('t≺', 't●', 't▷', 'c⊃'):
        for sub in kinds:
            if getattr(sub, 'atemporal', False) and (root != 'c⊃' or (args[0][0] == 'name' and prefix_cat(args[0][1]) == 'Tm')): raise Err('E-ATEMP', 'a value claim or comparison is atemporal: no tense wrapper or time context (TF-5 T.3.6 M9)')
    if root == 'h⊡' and args and args[0][0] == 'name' and prefix_cat(args[0][1]) != 'Ag': raise Err('E-CAT', 'the holder of h⊡ must be an agent name (class zk)')
    if root in ('r→', 'm>') and a['args'] and a['args'][0]['cat'] == 'Ex':
        for sub in kinds:
            md = getattr(sub, 'mdef', None)
            if md and md[0] == 'undef': raise Err('E-UNDEFVAL', 'a term with no defined value (%s) inside a value claim or comparison: report a?, not true, false or unknown (TF-6 D4, M12)' % md[1])
            if getattr(sub, 'free', None): raise Err('E-FREE', 'free letter %s in a value claim or comparison (TF-5 T.3.6 M11)' % ','.join(sorted(sub.free)))
    if root == 'n¬' and args and args[0][0] == 'app' and args[0][1] == '∃' and len(args[0][2]) == 2:
        v = args[0][2][0][1] if args[0][2][0][0] == 'name' else None
        if v and not has_domain(args[0][2][1], v): raise Err('E-DOMAIN', 'negated existence needs an explicit domain: a conjunct ∈(%s,S) in the body (TF-5 Part C 3.5)' % v)
    kind = 'n'
    if a['res'] == 'P':
        if root in STATE_E | STATE_N: kind = 's'
        elif root == 'n¬' and kinds: kind = kinds[0].kind
        elif root == 'c⊃' and len(kinds) > 1: kind = kinds[1].kind
    if root in ACTION_ROOTS: kind = 'e'
    r = Res(a['res'] if a['res'] != '=1' else kinds[0].cat, kind, basis, warns)
    if root in ('r→', 'm>') and a['res'] == 'P': r.atemporal = True
    if root in ('n¬', 'c⊃') and kinds and any(getattr(x, 'atemporal', False) for x in kinds): r.atemporal = True
    if root == 'r>' and a['res'] == 'Ln' and len(args) == 3:
        w = args[2]
        if not (w[0] == 'app' and w[1] in ('g←', 'u?')): raise Err('E-FORCE', 'the third operand of r> must be g←(A) or u?(A) (TF-6 D5 R9)')
    return r
def check_poly(root, a, args, exp, env, fr, parent):
    allowed = a['poly'] or ['P']
    if len(args) < 2: raise Err('E-ARITY', '%s needs at least two operands' % root)
    resmap = {'P': 'P', 'Act': 'Act', 'Ref': ('P' if root == 's≺' else 'Co')}
    order = [x for x in ('P', 'Act', 'Ref') if x in allowed and (exp is None or fits(resmap[x], exp))]
    if not order: raise Err('E-CAT', '%s over %s gives %s, slot needs %s' % (root, '/'.join(allowed), '/'.join(resmap[x] for x in allowed), exp))
    first = None
    for alpha in order:
        try:
            basis = {a['status']}; warns = []
            for i, ar in enumerate(args):
                if ar[0] == 'null': raise Err('E-NULL', '%s joins operands; n0 is not an operand' % root)
                sub = check(ar, alpha, env, fr, parent=(root, i)); basis |= sub.basis; warns += sub.warns
            return Res(resmap[alpha], 'n', basis, warns)
        except Err as ex:
            if first is None: first = ex
    code = 'E-MIX' if first.code == 'E-CAT' else first.code
    raise Err(code, '%s joins operands of one category (%s); %s' % (root, '/'.join(allowed), first.msg))
def check_binder(root, alts, args, exp, env, fr):
    if root == '∃' and len(args) == 1:
        a = [x for x in alts if len(x['args']) == 1][0]
        if exp and not fits('P', exp): raise Err('E-CAT', '∃ gives P')
        sub = check(args[0], 'Ref', env, fr); return Res('P', 'n', {a['status']} | sub.basis, sub.warns)
    a = alts[0]
    if len(args) != 2: raise Err('E-ARITY', '%s(v,body) takes two arguments' % root)
    v = args[0]
    if v[0] != 'name' or prefix_cat(v[1]) not in ('Ag', 'Me', 'Ob', 'Va', 'Co'): raise Err('E-BIND', 'the variable of %s is a name with prefix zk zm zo zv or zS' % root)
    vn = v[1]
    if vn in env.decl: raise Err('E-BIND', 'the variable %s was declared by d≔ and cannot be bound' % vn)
    if vn in env.bound: raise Err('E-BIND', 'binding %s again inside its own scope (no shadowing)' % vn)
    if root == '?=':
        if fr.get('inq'): raise Err('E-BIND', 'a question may not contain another ?= (nested interrogation excluded)')
        if vn in env.qvars: raise Err('E-BIND', 'the question variable %s is already used by another question in this message' % vn)
    env.bound = dict(env.bound) if isinstance(env.bound, dict) else {}
    env.bound[vn] = prefix_cat(vn)
    nfr = dict(fr)
    if root == '?=': nfr['inq'] = True
    try: sub = check(args[1], 'P', env, nfr, parent=(root, 1))
    finally: del env.bound[vn]
    if root == '?=':
        if not contains_var(args[1], vn): raise Err('E-BIND', 'the variable %s does not occur in the question body' % vn)
        env.qvars.add(vn)
    if exp:
        want = 'Q' if root == '?=' else 'P'
        if not fits(want, exp): raise Err('E-CAT', '%s gives %s; the slot needs %s' % (root, want, exp))
    return Res('Q' if root == '?=' else 'P', 'n', {a['status']} | sub.basis, sub.warns)
def check_rat(root, alts, args, exp, env, fr):
    if len(args) != 2: raise Err('E-ARITY', 'r@ takes two arguments')
    if args[1][0] == 'name' and prefix_cat(args[1][1]) == 'Ms':
        a = alts[1]; x = check(args[0], 'P|Ref', env, dict(fr, declaring=True))  # PROFILE CHANGE 1: was 'Ref'; qualified r@ also accepts a claim name
        r = Res(x.cat, x.kind, {a['status'], 'P'} | x.basis, x.warns)
        if exp and not fits(x.cat, exp): raise Err('E-CAT', 'r@(x,zUk) has the category of x (%s); slot needs %s' % (x.cat, exp))
        return r
    a = alts[0]
    x = check(args[0], 'P|Ref', env, fr); y = check(args[1], 'Ref', env, fr)
    if exp and not fits('P', exp): raise Err('E-CAT', 'r@ pointer gives P; slot needs %s' % exp)
    return Res('P', 'n', {a['status']} | x.basis | y.basis, x.warns + y.warns)
def add_details(root, r, det, ncore, env, fr):
    """RB: the role-marker details of a root application. Each marker at most once; core places plus details at most MAXARGS."""
    if not det: return r
    if ncore + len(det) > MAXARGS: raise Err('E-ARITY', '%s takes at most %d arguments, got %d' % (root, MAXARGS, ncore + len(det)))
    seen = set(); basis = set(r.basis); warns = list(r.warns)
    for ar in det:
        if ar[0] == 'null': continue   # RB: a null in a detail place means: no detail given
        if ar[1] in seen: raise Err('E-ROLE', 'role marker %s occurs twice in one %s' % (ar[1], root))
        seen.add(ar[1])
        sub = check(ar, 'Rm', env, fr)
        basis |= sub.basis; warns += sub.warns
    r.basis = basis; r.warns = warns
    return r
def check_choice(root, alts, args, exp, env, fr):
    """RB: ?⊙(v,S,body): v is bound in body, S is a collection; gives a question."""
    a = alts[0]
    if len(args) != 3: raise Err('E-ARITY', '?⊙(v,S,body) takes three arguments')
    v = args[0]
    if v[0] != 'name' or prefix_cat(v[1]) not in ('Ag', 'Me', 'Ob', 'Va', 'Co'): raise Err('E-BIND', 'the variable of ?⊙ is a name with prefix zk zm zo zv or zS')
    vn = v[1]
    if vn in env.decl: raise Err('E-BIND', 'the variable %s was declared by d≔ and cannot be bound' % vn)
    if vn in env.bound: raise Err('E-BIND', 'binding %s again inside its own scope (no shadowing)' % vn)
    if fr.get('inq'): raise Err('E-BIND', 'a question may not contain another binder (nested interrogation excluded)')
    if vn in env.qvars: raise Err('E-BIND', 'the question variable %s is already used by another question in this message' % vn)
    sset = check(args[1], 'Co', env, fr)
    env.bound = dict(env.bound) if isinstance(env.bound, dict) else {}
    env.bound[vn] = prefix_cat(vn)
    nfr = dict(fr); nfr['inq'] = True
    try: sub = check(args[2], 'P', env, nfr, parent=(root, 2))
    finally: del env.bound[vn]
    if not contains_var(args[2], vn): raise Err('E-BIND', 'the variable %s does not occur in the question body' % vn)
    env.qvars.add(vn)
    if exp and not fits('Q', exp): raise Err('E-CAT', '?⊙ gives Q; the slot needs %s' % exp)
    return Res('Q', 'n', {a['status']} | sset.basis | sub.basis, sset.warns + sub.warns)
def check_def(args, env, fr):
    if len(args) == 2: return check_def1(args, env, fr)
    if len(args) < 2 or len(args) % 2: raise Err('E-ARITY', 'd≔ takes k names then k definitions in the same order (an even number of arguments), got %d' % len(args))
    k = len(args) // 2; basis = set(); warns = []
    for n, d in zip(args[:k], args[k:]):
        r = check_def1([n, d], env, fr); basis |= r.basis; warns += r.warns
    return Res('Dc', 'n', basis, warns)
def check_def1(args, env, fr):
    if len(args) != 2: raise Err('E-ARITY', 'd≔ takes (name, definiens)')
    nm, df = args
    if nm[0] != 'name': raise Err('E-DEF', 'the first argument of d≔ is a name')
    n = nm[1]; c = prefix_cat(n)
    if n in env.decl: raise Err('E-REDECL', 'name %s is already declared in this message (no silent redeclaration)' % n)
    if c == 'Ms': raise Err('E-DEF', 'a message name zU is declared only by the header m▤(zU,zk)')
    basis = {'Ep'}; warns = []
    if c == 'Tm':
        if df == ('atom', 't'): pass
        elif df[0] == 'app' and df[1] == 'r@': check(df, 'Tm', env, fr); basis.add('N')
        else: raise Err('E-DEF', 'a time name is declared as d≔(%s,t) or as an imported qualified reference' % n)
    elif c == 'Ex':
        if df[0] == 'math': check(df, None, env, fr); env.mdefs[n] = mval(mparse(df[1]))
        elif df[0] == 'name' and prefix_cat(df[1]) == 'Ex': env.mdefs[n] = env.mdefs.get(df[1])
        else: raise Err('E-DEF', 'a zE name takes a ✠ term (T.3.6 M8)')
    elif df[0] == 'math': raise Err('E-MATHPLACE', 'a %s name is not an expression name; ✠(E) is a term and may define only a zE name (T.3.6 M8)' % c)
    else:
        if df[0] == 'mention' and df[1][0] == 'raw': warns.append('SCAFFOLD: quoted English definiens; class stated in EN notes only')
        else:
            want = {'P': 'P', 'Me': 'Act|Me', 'Ob': 'Ref', 'Va': 'Va', 'Co': 'Co', 'Ag': 'Ag', 'Cr': 'Cr'}[c]
            sub = check(df, want, env, fr); basis |= sub.basis; warns += sub.warns
    env.decl[n] = c
    return Res('Dc', 'n', basis, warns)
def check_line(src, env=None):
    env = env or Env()
    if src.startswith('∴ '):
        r = check(parse(src[2:]), 'P', env, {}); env.nline += 1
        return 'Ln', sorted(r.basis | {'U'}, key=lambda b: -RANK[b]), level(r.basis | {'U'}), ['OPEN: prefix form of the therefore glyph (U-07); no signature, basis U']
    node = parse(src)
    is_hdr = node[0] == 'app' and node[1] == 'm▤' and len(node[2]) == 2 and node[2][0][0] == 'name' and node[2][0][1].startswith('zU')
    if is_hdr and (env.nline > 0 or env.header): raise Err('E-HEADER', 'a header m▤(zU,zk) is the first line of its message, at most once (TF-6 D5 R2)')
    if is_hdr: env.header = True
    env.nline += 1
    r = check(node, None, env, {})
    warns = list(r.warns)
    if r.cat == 'P': warns.append('FU: bare content line, force unspecified (CL-1/OG-13); write g←(…) if you mean "supplied"')
    elif r.cat in ('Act', 'Rm', 'Ref', 'Ex', 'Va', 'Co', 'Ob', 'Ag', 'Me', 'Tm', 'Cr', 'Ct', 'Pm', 'Ms', 'Mn', 'Null') or r.cat.startswith('Mn['):
        raise Err('E-LINE', 'a %s is not a line: an act needs i!(…) or r<(who,…); a term needs a wrapper (TF-5 T.3.6 M5 item 2)' % r.cat)
    return r.cat, sorted(r.basis, key=lambda b: -RANK[b]), level(r.basis), warns
def main():
    a = sys.argv[1:]
    if not a: print(__doc__); return 0
    if a[0] == 'check':
        try:
            c, b, lv, w = check_line(a[1]); print('OK', c, 'basis=' + '+'.join(b) if b else 'basis=-', *w, sep='  ')
        except Err as ex: print('ERR', ex); return 1
    if a[0] == 'file':
        env = Env(); rc = 0
        for n, ln in enumerate(open(a[1], encoding='utf-8'), 1):
            ln = re.sub(r'(^|\s)#(\s|$).*', '', ln).strip()
            if not ln: continue
            try: check_line(ln, env)
            except Err as ex: print('line %d: ERR %s' % (n, ex)); rc = 1
        print('done'); return rc
    return 0
if __name__ == '__main__': sys.exit(main())
