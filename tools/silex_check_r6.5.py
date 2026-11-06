#!/usr/bin/env python3
"""silex_check.py -- the checker for SILEX, rules of SILEX-r6.5.

One file, Python 3 standard library only.  It checks messages written in SILEX:
  every line      brackets, roots, places and kinds, names and labels, quotes (no "the", no words that depend on who speaks
                  or when, braces only as references), times, the header                               (Parts 1 and 3)
  code(...)       the language is on the list; a Python program must parse (Python's own syntax check)  (1.4.6)
  'formula'       the formula is well formed: numbers, names, + - * / ^, brackets, functions, one comparison in a claim,
                  claims joined by & | => <=>  (1.4.6)
  across messages serial numbers, the roster, re/saw name earlier messages, every line reference (Ana3.2, in whatever root)
                  names a line that exists, ans answers a question, a label reached as Ana3.o1 is defined in Ana3
                                                                                                      (2.2, 2.3, 2.5, 1.5.4)
It does not run anything, does not judge whether a message is true or wise, and does not read the English inside quotes
beyond the word rules of 1.4.5.  `ok` means well formed: nothing more.

Use
  python3 silex_check.py chat.txt          messages one after another; each begins with its msg(...) header (or divide them with a line ---)
  python3 silex_check.py -                 the same, read from standard input
  python3 silex_check.py --lines x.txt     loose lines, no header needed
  python3 silex_check.py SILEX-r6.5.md     run every example of a markdown file against its "# ok" / "# E-..." comments (the file verifier of 6.1)
  python3 silex_check.py --selftest        run the built-in tests
  python3 silex_check.py --root ent        show the places of a root;  --roots lists all;  --kinds explains the kinds
  options: -v every line, -q only problems, --json machine-readable report, --per-message no checks across messages
Exit status: 0 all ok, 1 problems found, 2 could not run.

Verdicts (1.9): ok  E-SYN  E-LEX  E-ARITY  E-KIND  E-NAME  E-REDEF  E-HEAD  E-TIME  E-QUOTE  E-CODE  E-MATH
Line numbers in reports are the grammar's: line 1 is the first line after the header (the header is never a line).
Ana1.2 is line 2 of message Ana1; #3.2 is line 2 of the third message when its header has no serial number.

As a module:  check(text, need_header=False) -> [{line, last, verdict, diags}] for the lines of one message;
              check_dialogue([text, ...]) -> [problem, ...] across messages;  check_conversation(split_messages(text)) -> report dict.
"""
import re, sys, os, json, datetime, ast, textwrap, warnings

__version__ = 'r6.5'

# ==================================================================================================
#  1. THE LEXICON  (Part 3 of the grammar: root | places -> kind returned | reading | example)
# ==================================================================================================
LEXICON = r'''
## Logic
not | Cl -> Cl ; Ac -> Ac ; Cr -> Cr | not P (for an act: not doing A; for a criterion: not being c) | not(is("server","patched"))
and | Cl Cl... -> Cl ; Ac Ac... -> Ac | P, Q, … all hold (for acts: do all of them) | and(is("web server","patched"),is("database server","patched"))
or | Cl Cl... -> Cl ; Ac Ac... -> Ac | at least one of P, Q, … holds (for acts: do one or more) | or(is("web server","down"),is("database server","down"))
eith | Cl Cl... -> Cl | exactly one of P, Q, … holds | eith(is("web server","down"),is("database server","down"))
if | Cl X -> =2 | if P then X (X is a claim, an act or a line) | if(is("web server","patched"),is("database server","patched"))
## Quantifiers
all | Gr Cr -> Cl | every member of G is c | all("production servers","patched")
most | Gr Cr -> Cl | most members of G are c | most("production servers","patched")
half | Gr Cr -> Cl | half of the members of G are c | half("production servers","patched")
many | Gr [Cr] -> Cl | G has many members (that are c) | many("production servers")
few | Gr [Cr] -> Cl | G has few members (that are c) | few("production servers","patched")
some | Gr [Cr] -> Cl | G has at least one member (that is c) | some("production servers","patched")
none | Gr [Cr] -> Cl | G has no member (that is c) | none("production servers","patched")
crit | Vr Cl -> Cr | the criterion of being an x such that P | all("servers",crit(o1,is(o1,"hosts","payment service")))
def | Nm Va -> Ln | the label stands for the expression | def(g1,filt("servers","patched"))
## Numbers
plus | Nu Nu... -> Nu ; Tm Du -> Tm ; Du Du... -> Du ; Gr Va -> Gr | a plus b (a time plus a duration; a group with a member added) | plus(2,3)
minus | Nu Nu -> Nu ; Tm Du -> Tm ; Tm Tm -> Du ; Du Du -> Du ; Gr Va -> Gr | a minus b (a time minus a duration; the gap between two times; a group without a member) | minus(now,P1D)
times | Nu Nu... -> Nu ; Du Nu -> Du | a times b | times(3,4)
div | Nu Nu -> Nu ; Du Nu -> Du ; Du Du -> Nu | a divided by b | div(10,4)
pow | Nu Nu -> Nu | a to the power b | pow(2,10)
sum | Gr Cr -> Nu | total, over the members of G, of their c | sum("invoices","amount in euros")
cnt | Gr -> Nu | the number of members of G | cnt("production servers")
avg | Gr Cr -> Nu ; Nu Nu... -> Nu | the average of the c of the members of G (or of the numbers) | avg(3,5,10)
max | Gr Cr -> Nu ; Nu Nu... -> Nu | the largest | max("invoices","amount in euros")
min | Gr Cr -> Nu ; Nu Nu... -> Nu | the smallest | min(3,5,10)
pct | Nu Nu -> Nu | a as a percentage of b | pct(19,20)
val | Va Cr -> Va ; Va Cr Va -> Cl | the c of x (a value); with a third place: the c of x is V | val("server","RAM in GB",16)
func | Cr Va... -> Va | apply the function named c to the arguments | func("square root",2)
rng | Nu Nu -> Gr ; Du Du -> Gr ; Tm Tm -> Gr | the range from a to b | rng(3,5)
## Comparison
eq | Va Va -> Cl | x and y are the same, or equal | eq("web server","database server")
over | Nu Nu -> Cl ; Du Du -> Cl | a is greater than b | over(cnt("production servers"),10)
under | Nu Nu -> Cl ; Du Du -> Cl | a is less than b | under(3,5)
atleast | Nu Nu -> Cl ; Du Du -> Cl | a is at least b | atleast(cnt("approvals"),2)
atmost | Nu Nu -> Cl ; Du Du -> Cl | a is at most b | atmost(3,5)
apx | Va Va -> Cl | x is approximately y | apx(val("migration","duration"),PT20M)
more | Va Va Cr -> Cl | x has more of c than y | more("new version","old version","fast")
best | Gr Cr -> Va | the best member of G by c | best("candidates","cheap")
## Groups and relations
grp | Va... -> Gr | the group of x, y, … | grp("web server","database server")
filt | Gr Cr -> Gr | the members of G that are c | filt("production servers","patched")
pick | Gr [Cr] -> Th | one member of G (that is c) | pick("production servers","patched")
mem | Va Gr -> Cl | x is a member of G | mem("audit log","production logs")
is | Va Cr -> Cl ; Va Cr Va -> Cl | x is c; with a third place: x stands in the relation c to y | is("web server","depends on","database")
loc | Va Va -> Cl ; Va -> Th | x is in or at y; the place of x | loc("config file","/etc folder")
## Acts
act | Th|Gr Ac -> Cl | x performs the act A | act(Ana,"send report to Ben")
fin | Ac [Cr] -> Cl | the act A is finished (with the outcome c) | fin("deployment to production","successfully")
then | Ac Ac... -> Ac | A, then B, then … | then("run migration","restart service")
par | Ac Ac... -> Ac | A and B together | par("run migration","notify team")
tell | Th Va -> Ac | tell x the claim or value V | tell(Ana,fin("backup"))
ask | Th Q -> Ac | ask x the question Q | ask(Cy,yn(fin("backup")))
chk | Cl -> Ac | check whether P | chk(is("release build","passes","smoke test"))
code | Rw Rw... -> Ac | the program written in these lines (first the language, then one quote for each line), as the act of running it | code("python","def add(a,b):","    return a+b")
## Modality and mind
must | Th|Gr Ac -> Cl ; Cl -> Cl | x is required to do A (or: P is required) | must(You,not("delete backup"))
should | Th|Gr Ac -> Cl ; Cl -> Cl | x ought to do A (or: P ought to hold) | should(You,"review changes")
may | Th|Gr Ac -> Cl ; Cl -> Cl | x is allowed to do A (or: P is allowed) | may(Me,"write to job scheduler")
can | Th|Gr Ac -> Cl ; Cl -> Cl | x is able to do A (or: P is possible) | can(Me,"run test suite")
want | Th|Gr Cl|Ac -> Cl | x wants P to hold (or wants to do A) | want(Me,fin("migration"))
need | Th|Gr Va -> Cl | x needs V | need(Me,"API key for staging environment")
plan | Th|Gr Ac -> Cl | x plans to do A | plan(Ana,at(2026-11-06,"ship"))
bel | Th|Gr Cl -> Cl | x believes P | bel(Me,cause("cache layer","outage"))
know | Th|Gr Cl|Q -> Cl | x knows P (or the answer to Q) | know(Ben,is("build","green"))
say | Th|Gr Cl|Q|Ln -> Cl | x says P (reported speech) | say(Ben,is("build","green"))
prob | Cl [Nu] -> Cl | P is probable (with probability n) | prob(is("build","broken"))
## Lines (speech acts)
unk | Cl|Q|Rf -> Ln | the sender does not know whether P (or the answer to Q) | unk(what(val("outage","cause")))
hyp | Cl -> Ln | P is offered as a hypothesis, not asserted | hyp(cause("cache layer","outage"))
assume | Cl -> Ln | suppose P: take it as given for what follows | assume(is("cache","empty"))
pls | Th|Gr Ac|Cl -> Ln ; Ac|Cl -> Ln | please: x (or each receiver) is asked to do A or to bring P about | pls(Ben,"run smoke test")
will | Ac|Cl -> Ln | the sender undertakes to do A (or to see to P) | will("run smoke test")
rej | Ac|Cl [Cl] -> Ln | the sender declines A, or the request or proposal in the message or line M (because P, which is asserted) | rej("run full regression suite",not(may(Me,"write to job scheduler")))
ans | Rf|Q Va -> Ln | the answer to the question is V (yes, no, a value or a claim) | ans(Ana7.1,yes)
sug | Cl|Ac -> Ln | the sender proposes P (or A) to the receivers and itself: let us | sug(at(2026-11-06,"ship"))
agree | Rf -> Ln | the sender agrees with the message, line or proposal | agree(Ana3)
retr | Rf -> Ln | the sender takes back the message or line | retr(Ana3.2)
ack | Rf... -> Ln | the sender received these messages | ack(Ana3,Cy1)
err | Rf [Cl] -> Ln | there is an error in the message or line (P says what, and is asserted) | err(Ana3.2)
clr | Rf [Cl] -> Ln | the message or line is unclear (P names what is unclear, and is not asserted) | clr(Ana3.2)
## Time
at | Tm|Cl X -> =2 | at time t, X (throughout t when t is a stretch) | at(2026-11-04T15:00,fin("deployment to production"))
before | Tm|Cl X -> =2 | before t, X | before(2026-11-04T17:00,is("server","frozen"))
after | Tm|Cl X -> =2 | after t, X | after(fin("migration"),act(Ben,"restart service"))
by | Tm|Cl X -> =2 | at or before t, X | by(2026-11-06T17:00,act(Ana,"send report to Ben"))
until | Tm|Cl X -> =2 | X until t | until(2026-11-06,is("server","frozen"))
from | Tm|Cl X -> =2 | X from t onward | from(2026-11-04,is("server","frozen"))
during | Tm|Cl X -> =2 | X at some time within t | during(2026-11-03T22:00/2026-11-04T06:00,fin("restart"))
for | Du X -> =2 | X for the length of time d | for(PT3H,is("service","down"))
each | Du X -> =2 | X every d | each(P1D,fin("backup"))
rep | Nu X -> =2 | X happens n times | rep(2,fin("restart"))
always | X -> =1 | X at all times | always(is("daemon","listening"))
still | Cl -> Cl | P still holds | still(is("server","down"))
when | Cl -> Tm | the time at which P happens | when(fin("build"))
## Cause and reason
cause | Va Va -> Cl | x (a thing, an act or a claim) causes y | cause(fin("review"),is("report","ready"))
supp | Cl Cl -> Cl | P is a reason or evidence for believing Q | supp(is("light","on"),is("Bob","home"))
ent | Gr|Rf Cl [Cr] -> Cl | Q follows from the premises G (under the rules c); G is a group, or one line reference | ent("test results",is("release build","safe"))
would | Cl Cl -> Cl | if P had held, Q would have held | would(not(fin("review")),not(is("report","ready")))
why | Cl -> Q | why is it so that P? | why(fin("deployment"))
## Questions
yn | Cl -> Q | is it so that P? | yn(is("cache","enabled"))
what | Va -> Q | what is E? | what(cnt("production servers"))
which | Vr Cl -> Q | which x makes P hold? | which(o1,and(mem(o1,"tests"),is(o1,"failed")))
## Protocol
msg | Ag *Ag [Nu] [Tm] [Hd]... -> Hd | header: from, to (one or more), serial, send time, details | msg(Ana,Ben,3)
re | Rf... -> Hd | header detail: in reply to these messages | msg(Ben,Ana,4,re(Ana3))
saw | Rf... -> Hd | header detail: the latest messages seen from others | msg(Ben,Ana,5,saw(Ana3,Cy1))
pri | Dg -> Hd | header detail: the priority of the message (hi, mid or lo) | msg(Ana,Ben,1,pri(hi))
to | *Ag Ln -> Ln | the line is addressed to these receivers (the others still receive it) | to(Cy,pls("run full regression suite"))
join | Ag... -> Ln | these agents join the conversation | join(Dan)
leave | Ag... -> Ln | these agents leave the conversation | leave(Dan)
'''

ATOMS = [  # atom | kind | reading
    ('now', 'Tm', 'the time this message was sent'),
    ('Me', 'Ag', 'the sender of this message'),
    ('You', 'Ag', 'each receiver of this message'),
    ('All', 'Ag', 'every agent on the roster'),
    ('yes', 'An', 'the answer yes'),
    ('no', 'An', 'the answer no'),
    ('hi', 'Dg', 'a high degree'),
    ('mid', 'Dg', 'a middle degree'),
    ('lo', 'Dg', 'a low degree'),
    ('_', 'Un', 'unspecified: some value that is not given'),
]

def parse_sig(s):
    """'Th Ac -> Cl ; Cl -> Cl' -> [(args, result)]; args: list of (kinds tuple, opt, rep, star)"""
    out = []
    for alt in s.split(';'):
        left, right = alt.split('->')
        args = []
        for tok in left.split():
            star = tok.startswith('*'); tok = tok.lstrip('*')
            rep = tok.endswith('...')
            if rep: tok = tok[:-3]
            opt = tok.startswith('[') and tok.endswith(']')
            if opt: tok = tok[1:-1]
            args.append((tuple(tok.split('|')), opt, rep, star))
        out.append((args, right.strip()))
    return out


def load_lexicon():
    ents = []
    sec = ''
    for ln in LEXICON.split('\n'):
        ln = ln.rstrip()
        if not ln.strip():
            continue
        if ln.startswith('## '):
            sec = ln[3:].strip()
            continue
        parts = [p.strip() for p in ln.split(' | ')]
        assert len(parts) == 4, ln
        root, sig, reading, ex = parts
        ents.append(dict(root=root, sig=sig, sigs=parse_sig(sig), reading=reading, example=ex, section=sec))
    return ents


def dl(a, b):
    """Damerau-Levenshtein (optimal string alignment)"""
    la, lb = len(a), len(b)
    d = [[0] * (lb + 1) for _ in range(la + 1)]
    for i in range(la + 1): d[i][0] = i
    for j in range(lb + 1): d[0][j] = j
    for i in range(1, la + 1):
        for j in range(1, lb + 1):
            c = 0 if a[i-1] == b[j-1] else 1
            d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + c)
            if i > 1 and j > 1 and a[i-1] == b[j-2] and a[i-2] == b[j-1]:
                d[i][j] = min(d[i][j], d[i-2][j-2] + 1)
    return d[la][lb]

# ==================================================================================================
#  2. THE LEXER AND PARSER  (1.1, 1.2, 1.4)
# ==================================================================================================
class N:
    """node: t = app | atom | str | num | time | dur | label | agent | ref.   A str node with pre == "'" is a formula quote 'F'."""
    __slots__ = ('t', 'v', 'args', 'pre', 'line', 'col', 'end')
    def __init__(self, t, v, args=None, pre='', line=0, col=0):
        self.t, self.v, self.args, self.pre, self.line, self.col, self.end = t, v, args or [], pre, line, col, line
    def __repr__(self):
        if self.t == 'app':
            return '%s(%s)' % (self.v, ','.join(map(repr, self.args)))
        if self.t == 'str':
            if self.pre == "'":                       # the formula quote 'F'
                return "'%s'" % self.v
            return '%s"%s"' % (self.pre, self.v)
        return str(self.v)

class SynErr(Exception):
    def __init__(self, code, msg, line):
        Exception.__init__(self, msg); self.code, self.msg, self.line = code, msg, line

_EXT = r'\d{4}-\d{2}(?:-\d{2})?(?:T\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:Z|[+-]\d{2}:?\d{2})?)?'
_BASIC = r'\d{8}T\d{4}(?:\d{2})?(?:Z|[+-]\d{2}:?\d{2})?'      # 20261106T1700
_TIMEPART = '(?:' + _EXT + '|' + _BASIC + ')'
TOK = [
    ('COMMENT', re.compile(r'#[^\n]*')),
    ('WS', re.compile(r'[ \t\r]+')),
    ('NL', re.compile(r'\n')),
    ('PQ', re.compile(r'[ogacnqtd][0-9]*(?=")')),
    ('STR', re.compile(r'"(?:[^"]|"")*"')),
    ('FQ', re.compile(r"'[^'\n]*'")),                 # a formula in single quotes, 'x^2=4'
    ('TIME', re.compile(_TIMEPART + r'(?:/' + _TIMEPART + r')?')),
    ('DUR', re.compile(r'P(?=\d|T\d)(?:\d+Y)?(?:\d+M)?(?:\d+W)?(?:\d+D)?(?:T(?:\d+H)?(?:\d+M)?(?:\d+S)?)?')),
    ('NUM', re.compile(r'-?\d+(?:\.\d+)?')),
    ('REF', re.compile(r'[A-Z][a-z]*\d+(?:\.(?:\d+|[ogacnqtd]\d+))?')),
    ('AGENT', re.compile(r'[A-Z][a-z]*')),
    ('LABEL', re.compile(r'[ogacnqtd]\d+')),
    ('WORD', re.compile(r'[a-z]+|_')),
    ('PUNCT', re.compile(r'[(),]')),
    ('BAD', re.compile(r'[^\s]')),
]

def lex(text):
    """-> list of (type, value, line, col); NL tokens kept"""
    toks, pos, line, ls = [], 0, 1, 0
    n = len(text)
    while pos < n:
        for name, rx in TOK:
            m = rx.match(text, pos)
            if not m:
                continue
            s = m.group(0)
            if name == 'DUR' and (s == 'P' or s.endswith('T')):
                continue
            break
        else:  # pragma: no cover
            raise AssertionError
        col = pos - ls + 1
        if name == 'NL':
            toks.append(('NL', '\n', line, col)); line += 1; ls = m.end()
        elif name in ('WS', 'COMMENT'):
            pass
        else:
            toks.append((name, s, line, col))
            if name == 'STR' and '\n' in s:       # a quote may not run over a line
                toks[-1] = ('BAD', s, line, col)
        pos = m.end()
    return toks

class Parser:
    def __init__(self, toks):
        self.toks = [t for t in toks]
        self.i = 0

    def peek(self, skipnl=False):
        j = self.i
        while skipnl and j < len(self.toks) and self.toks[j][0] == 'NL':
            j += 1
        return self.toks[j] if j < len(self.toks) else ('EOF', '', 0, 0)

    def next(self, skipnl=False):
        while skipnl and self.i < len(self.toks) and self.toks[self.i][0] == 'NL':
            self.i += 1
        t = self.peek()
        if t[0] != 'EOF':
            self.i += 1
        return t

    def expr(self, depth):
        """one expression; inside brackets newlines are white space"""
        t = self.next()
        k, v, ln, col = t
        if k in ('EOF', 'NL'):
            raise SynErr('E-SYN', 'the line ends where an expression is needed (a line is closed on its own line)', ln or 0)
        if k == 'PQ':
            s = self.next()
            if s[0] != 'STR':
                raise SynErr('E-SYN', 'a class letter must be followed by a quote', ln)
            return N('str', s[1][1:-1].replace('""', '"'), pre=v, line=ln, col=col)
        if k == 'STR':
            return N('str', v[1:-1].replace('""', '"'), pre='', line=ln, col=col)
        if k == 'FQ':
            return N('str', v[1:-1], pre="'", line=ln, col=col)
        if k in ('NUM', 'TIME', 'DUR', 'LABEL', 'AGENT', 'REF'):
            nd = N({'NUM': 'num', 'TIME': 'time', 'DUR': 'dur', 'LABEL': 'label', 'AGENT': 'agent', 'REF': 'ref'}[k], v, line=ln, col=col)
            if k in ('AGENT',) and self.peek()[1] == '(':
                raise SynErr('E-LEX', '%s is a name, not a root; roots are lower-case' % v, ln)
            return nd
        if k == 'WORD':
            if self.peek()[1] == '(':
                self.next()
                args = []
                if self.peek()[1] == ')' and self.peek()[0] == 'PUNCT':
                    self.next()
                    nd = N('app', v, args, line=ln, col=col); nd.end = self.toks[self.i - 1][2]
                    return nd
                while True:
                    args.append(self.expr(depth + 1))
                    t2 = self.next()
                    if t2[1] == ',' and t2[0] == 'PUNCT':
                        continue
                    if t2[1] == ')' and t2[0] == 'PUNCT':
                        break
                    if t2[0] in ('EOF', 'NL'):
                        raise SynErr('E-SYN', 'the line ends inside a bracket', ln)
                    raise SynErr('E-SYN', 'expected "," or ")" but found %r' % (t2[1],), t2[2])
                nd = N('app', v, args, line=ln, col=col); nd.end = t2[2]
                return nd
            return N('atom', v, line=ln, col=col)
        if k == 'BAD' and v.startswith('"'):
            raise SynErr('E-SYN', 'a quote ends on the line where it starts; in code(...) give each line of the program its own quote', ln)
        if k == 'BAD' and v.startswith("'"):
            raise SynErr('E-SYN', "a formula in single quotes ends on the line where it starts, and holds no quote mark: 'x^2=4'", ln)
        if k == 'PUNCT':
            raise SynErr('E-SYN', 'unexpected %r' % (v,), ln)
        raise SynErr('E-SYN', 'unexpected %r' % (v,), ln)

    def top(self):
        """-> list of ('ok', node) | ('err', SynErr); one entry per top-level expression"""
        out = []
        while True:
            while self.i < len(self.toks) and self.toks[self.i][0] == 'NL':
                self.i += 1
            if self.i >= len(self.toks):
                break
            start = self.i
            try:
                nd = self.expr(0)
                nt = self.peek()
                if nt[0] not in ('NL', 'EOF'):
                    raise SynErr('E-SYN', 'two expressions on one line (%r follows)' % (nt[1],), nt[2])
                out.append(('ok', nd))
            except SynErr as e:
                out.append(('err', e))
                # resync: skip to the end of the line that holds the error, at depth 0
                self.i = start
                while self.peek()[0] not in ('NL', 'EOF'):
                    self.i += 1
        return out

def parse(text):
    return Parser(lex(text)).top()

# ==================================================================================================
#  3. THE CHECKER FOR ONE MESSAGE  (kinds, names, quotes, times, header; code and formulas)
# ==================================================================================================
ENT = {e['root']: e for e in load_lexicon()}
ATOMK = {a: k for a, k, _ in ATOMS}
CLASSK = dict(o='Th', g='Gr', a='Ac', n='Nu', c='Cr', q='Cl', t='Tm', d='Du')
VALUE = {'Ag', 'Th', 'Gr', 'Ac', 'Nu', 'Dg', 'Tm', 'Du', 'Cr', 'Cl', 'An', 'Rf'}
PRON = ('Me', 'You', 'All')

def fits(k, place):
    if isinstance(k, frozenset):
        return any(fits(x, place) for x in k)
    if k in ('Un', 'ERR'):
        return True
    for pk in place:
        if pk == 'Va' and k in VALUE: return True
        if pk == 'X' and k in ('Cl', 'Ac', 'Ln', 'Q', 'Rf'): return True
        if pk == 'Th' and k in ('Th', 'Ag'): return True
        if pk == 'Nu' and k in ('Nu', 'Dg'): return True
        if pk == 'Cl' and k in ('Cl', 'Rf'): return True
        if pk == 'Q' and k in ('Q', 'Rf'): return True
        if pk == 'Ln' and k in ('Ln', 'Cl', 'Q', 'Rf'): return True
        if pk == k: return True
        if k == 'Va' and pk in ('Nu', 'Tm', 'Du', 'Gr', 'Th', 'Cr'): return True
    return False

def bare_kind(place):
    """kind a bare quote takes in this place, or None when the place is not single-kind"""
    if len(place) == 1:
        pk = place[0]
        if pk in ('Va', 'Th'): return 'Th'
        if pk == 'X': return 'Ac'
        if pk in ('Gr', 'Ac', 'Cr', 'Nu', 'Tm', 'Du'): return pk
        return None
    if 'Ac' in place: return 'Ac'
    if 'Tm' in place: return 'Tm'
    if 'Th' in place: return 'Th'
    if 'Gr' in place: return 'Gr'
    return None

def expand(specs, n):
    """signature specs -> list of n place tuples, or None when n arguments do not fit.
       spec = (kinds, optional, repeat, star): plain = exactly one; [K] = zero or one; K... = one or more (last); *K = one or more (first)."""
    req = [s for s in specs if not s[1] and not s[2] and not s[3]]
    star = [s for s in specs if s[3]]
    rep = [s for s in specs if s[2] and not s[3]]
    opt = [s for s in specs if s[1]]
    extra = n - len(req) - len(star) - len(rep)
    if extra < 0:
        return None
    optbudget = min(extra, len(opt))
    rest = extra - optbudget
    if rest and not star and not rep:
        return None
    places = []
    for s in specs:
        if s[3]:
            places += [s[0]] * (1 + rest); rest = 0
        elif s[2]:
            places += [s[0]] * (1 + rest); rest = 0
        elif s[1]:
            if optbudget > 0:
                places.append(s[0]); optbudget -= 1
        else:
            places.append(s[0])
    return places if len(places) == n else None

BASIC = re.compile(r'(\d{4})(\d{2})(\d{2})T(\d{2})(\d{2})(\d{2})?(.*)$')

def ext_time(s):
    """20261106T1700 -> 2026-11-06T17:00 (the same time); other spellings unchanged"""
    out = []
    for p in s.split('/'):
        m = BASIC.match(p)
        if m:
            y, mo, d, h, mi, se, tz = m.groups()
            p = '%s-%s-%sT%s:%s' % (y, mo, d, h, mi) + (':' + se if se else '') + tz
        out.append(p)
    return '/'.join(out)

def valid_time(s):
    parts = ext_time(s).split('/')
    out = []
    for p in parts:
        m = re.match(r'(\d{4})-(\d{2})(?:-(\d{2}))?(?:T(\d{2}):(\d{2})(?::(\d{2}))?)?', p)
        y, mo, d, h, mi, se = m.groups()
        try:
            datetime.date(int(y), int(mo), int(d or 1))
        except ValueError:
            return False
        if h is not None and (int(h) > 23 or int(mi) > 59 or (se is not None and int(se) > 59)):
            return False
        out.append((int(y), int(mo), int(d or 1), int(h or 0), int(mi or 0)))
    return len(out) < 2 or out[0] <= out[1]

class Ctx:
    def __init__(self):
        self.env = {}            # label -> kind
        self.diags = []          # (line, code, msg)
        self.header = None       # (sender, receivers set, serial) or None
        self.retarget = None     # the one whole message that re(...) names, or None
        self.first = True
    def err(self, nd, code, msg):
        d = (nd.line if nd is not None else 0, code, msg)
        if d not in self.diags:              # the same complaint twice on one line is said once
            self.diags.append(d)

def near(word):
    best = sorted(((dl(word, r), r) for r in ENT), key=lambda x: x[0])[:3]
    return [r for d, r in best if d <= 2]

def ev(nd, ctx):
    t = nd.t
    if t == 'num': return 'Nu'
    if t == 'dur': return 'Du'
    if t == 'time':
        if not valid_time(nd.v):
            ctx.err(nd, 'E-TIME', '%s is not a real time (dates and times follow ISO 8601; an interval ends after it starts)' % nd.v)
            return 'ERR'
        return 'Tm'
    if t == 'agent': return 'Ag'
    if t == 'ref':
        m = re.match(r'[A-Z][a-z]*\d+\.([ogacnqtd])\d+$', nd.v)
        return CLASSK[m.group(1)] if m else 'Rf'
    if t == 'label':
        if nd.v not in ctx.env:
            ctx.err(nd, 'E-NAME', 'the label %s is not defined: define it where it is first used (%s"…") or bind it with crit/which/def' % (nd.v, nd.v))
            return 'ERR'
        return ctx.env[nd.v]
    if t == 'str':
        pre = nd.pre
        if pre == "'":
            return ev_formula(nd, ctx)                 # 'formula' is raw text, never read as English
        scan_quote(nd, ctx)
        if not pre:
            return 'BARE'
        k = CLASSK[pre[0]]
        if len(pre) > 1:
            if pre in ctx.env:
                ctx.err(nd, 'E-REDEF', 'the label %s is already defined in this message' % pre)
                return 'ERR'
            ctx.env[pre] = k
        return k
    if t == 'atom':
        if nd.v in ATOMK: return ATOMK[nd.v]
        if nd.v in ENT:
            ctx.err(nd, 'E-ARITY', '%s is a root and needs brackets: %s(…)' % (nd.v, nd.v))
        else:
            ctx.err(nd, 'E-LEX', '%s is not a SILEX word%s' % (nd.v, (' (near: ' + ', '.join(near(nd.v)) + ')') if near(nd.v) else ''))
        return 'ERR'
    if t == 'app':
        return ev_app(nd, ctx)
    raise AssertionError(t)

REFRX = re.compile(r'\{\{|\}\}|\{([^{}]*)\}|[{}]')
MSGNAME = re.compile(r'[A-Z][a-z]*\d+')

INDEX_WORDS = {'me', 'my', 'mine', 'myself', 'you', 'your', 'yours', 'we', 'our', 'ours', 'this', 'here', 'today', 'yesterday', 'tomorrow', 'tonight'}

def lint_quote(nd, ctx):
    """the two word rules of 1.4.5: no "the"; no word that depends on who speaks or when"""
    text = re.sub(r'\{\{|\}\}|\{[^{}]*\}', ' ', nd.v)
    words = re.findall(r"[A-Za-z]+", text)
    for w in words:
        lw = w.lower()
        if lw == 'the':
            ctx.err(nd, 'E-QUOTE', 'a quote has no "the" (write "production servers", not "the production servers")')
            return
        if lw in INDEX_WORDS or w == 'I' or w == 'us':
            ctx.err(nd, 'E-QUOTE', 'the word "%s" depends on who speaks or when: write {Me}, {You}, {Ana} or a date inside the quote' % w)
            return

def scan_quote(nd, ctx):
    """references inside a quote: {o1} {Ben5.o1} {Bob} {Me} {12} {2026-11-06} {PT5M}; {{ and }} are literal braces"""
    lint_quote(nd, ctx)
    for m in REFRX.finditer(nd.v):
        g = m.group(0)
        if g in ('{{', '}}'):
            continue
        if m.group(1) is None:
            ctx.err(nd, 'E-QUOTE', 'a single brace in a quote must open a reference such as {o1}; write {{ or }} for a literal brace')
            continue
        r = m.group(1).strip()
        if re.fullmatch(r'[ogacnqtd]\d+', r):
            if r not in ctx.env:
                ctx.err(nd, 'E-NAME', 'the label %s inside a quote is not defined yet' % r)
        elif re.fullmatch(r'[A-Z][a-z]*\d+\.[ogacnqtd]\d+', r) or re.fullmatch(r'[A-Z][a-z]*', r) or re.fullmatch(r'-?\d+(\.\d+)?', r):
            pass
        elif re.fullmatch(r'\d{4}-\d{2}(-\d{2})?(T[0-9:]+(Z|[+-]\d{2}:?\d{2})?)?', r) or re.fullmatch(r'\d{8}T\d{4}(\d{2})?(Z|[+-]\d{2}:?\d{2})?', r) or re.fullmatch(r'P[0-9YMWDTHS]+', r):
            pass
        else:
            ctx.err(nd, 'E-QUOTE', '{%s} is not a reference (a label, Name2.o1, an agent, a number, a time or a duration)' % r)

def describe(k):
    if isinstance(k, frozenset):
        return '/'.join(sorted(k))
    return {'BARE': 'a quote', 'ERR': '?'}.get(k, k)

def ev_app(nd, ctx):
    root, args = nd.v, nd.args
    ent = ENT.get(root)
    if ent is None:
        if root == 'math':
            ctx.err(nd, 'E-LEX', "math is not a root: a formula is written in single quotes, as 'x^2=4' (1.4.6)")
            return 'ERR'
        ctx.err(nd, 'E-LEX', '%s is not a SILEX root%s' % (root, (' (near: ' + ', '.join(near(root)) + ')') if near(root) else ''))
        return 'ERR'
    if root in ('crit', 'which', 'def'):
        return ev_binder(nd, ctx)
    if root in ('msg', 're', 'saw', 'pri'):
        if root == 'msg':
            ctx.err(nd, 'E-HEAD', 'msg is the header: it is the first line of a message and appears once')
        else:
            ctx.err(nd, 'E-HEAD', '%s is a header detail: it stands inside msg(…)' % root)
        return 'ERR'
    if root == 'to':
        return ev_to(nd, ctx)
    if root == 'code':
        return ev_code(nd, ctx)
    kinds = [ev(a, ctx) for a in args]
    cands = []
    for spec, res in ent['sigs']:
        pl = expand(spec, len(args))
        if pl is not None:
            cands.append((pl, res))
    if not cands:
        ar = sorted({(sum(1 for s in spec if not s[1] and not s[2] and not s[3]), 'n' if any(s[2] or s[3] for s in spec) else sum(1 for s in spec if not s[3] and not s[2])) for spec, res in ent['sigs']}, key=str)
        ctx.err(nd, 'E-ARITY', '%s takes %s, not %d' % (root, ' or '.join(sig_text(spec) for spec, res in ent['sigs']), len(args)))
        return 'ERR'
    best = None
    matched = []
    for pl, res in cands:
        ok, bad = True, []
        for i, (k, p) in enumerate(zip(kinds, pl)):
            if k == 'BARE':
                if bare_kind(p) is None:
                    ok = False; bad.append((i, k, p))
            elif not fits(k, p):
                ok = False; bad.append((i, k, p))
        if ok:
            matched.append(resolve(res, kinds, pl))
        elif best is None or len(bad) < len(best[1]):
            best = (pl, bad)
    if matched:
        if root == 'ent' and args[0].t == 'ref' and MSGNAME.fullmatch(args[0].v):
            ctx.err(args[0], 'E-KIND', 'the premises of ent are a group, or one line (Ana1.2); a whole message is not a premise: name its lines, as grp(Ana1.1,Ana1.2)')
            return 'ERR'
        flat = set()
        for r in matched:
            flat |= set(r) if isinstance(r, frozenset) else {r}
        return next(iter(flat)) if len(flat) == 1 else frozenset(flat)
    pl, bad = best
    for i, k, p in bad[:1]:
        want = '|'.join(p)
        if k == 'BARE':
            ctx.err(args[i], 'E-KIND', 'argument %d of %s takes %s: a bare quote cannot stand here; write a class letter first (o g a n c q t d), as in q"…" or a"…"' % (i + 1, root, want))
        elif i == 0 and root in RELROOTS and args[0].t == 'num':
            ctx.err(args[0], 'E-KIND', 'a bare number in the first place of %s is a line of the message answered; it needs a header with exactly one re(...) that names a whole message, and a whole number from 1 (otherwise write the reference in full, as Ana1.3)' % root)
        else:
            ctx.err(args[i], 'E-KIND', 'argument %d of %s takes %s, but this is %s' % (i + 1, root, want, describe(k)))
    return 'ERR'

def sig_text(spec):
    out = []
    for kinds, opt, rep, star in spec:
        s = '|'.join(kinds)
        if rep: s += '…'
        if star: s = s + '…'
        out.append('[' + s + ']' if opt else s)
    return '(' + ', '.join(out) + ')'

def resolve(res, kinds, places):
    if res.startswith('='):
        i = int(res[1:]) - 1
        k = kinds[i]
        if k == 'BARE': k = bare_kind(places[i])
        if k == 'Rf': k = 'Ln'
        return k
    return res

def ev_binder(nd, ctx):
    root, args = nd.v, nd.args
    want = 2
    if len(args) != want:
        ctx.err(nd, 'E-ARITY', '%s takes (label, %s), not %d arguments' % (root, 'value' if root == 'def' else 'claim', len(args)))
        for a in args: ev(a, ctx)
        return 'ERR'
    lab = args[0]
    if lab.t != 'label':
        ctx.err(lab, 'E-KIND', 'the first place of %s is a new label (a class letter and digits, as in o1)' % root)
        return 'ERR'
    if lab.v in ctx.env:
        ctx.err(lab, 'E-REDEF', 'the label %s is already defined in this message' % lab.v)
        return 'ERR'
    k = CLASSK[lab.v[0]]
    if root == 'def':
        v = ev(args[1], ctx)
        if v == 'BARE': v = 'Th'
        if v not in ('ERR', 'Un') and not fits(v, (k,)) and not (k == 'Th' and v == 'Ag'):
            ctx.err(args[1], 'E-KIND', 'the label %s has the class of a %s, but the expression is %s' % (lab.v, k, describe(v)))
            return 'ERR'
        ctx.env[lab.v] = k
        return 'Ln'
    ctx.env[lab.v] = k
    v = ev(args[1], ctx)
    del ctx.env[lab.v]
    if v == 'BARE':
        ctx.err(args[1], 'E-KIND', 'argument 2 of %s takes a claim: write q"…" for a claim in English' % root)
    elif not fits(v, ('Cl',)):
        ctx.err(args[1], 'E-KIND', 'argument 2 of %s takes Cl, but this is %s' % (root, describe(v)))
    return 'Cr' if root == 'crit' else 'Q'

# ---------------------------------------------------------------- text that is carried as it is (1.4.6)
LANGS = ('python', 'javascript', 'typescript', 'bash', 'sql', 'json', 'yaml', 'html', 'css', 'c', 'cpp', 'java', 'go', 'rust', 'diff', 'text')

def check_python(lines):
    """None when the lines read as Python 3 (a fragment may be indented as a whole), else the reason"""
    src = textwrap.dedent('\n'.join(lines))
    try:
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            ast.parse(src)
    except SyntaxError as e:
        return 'python does not read this: line %s: %s' % (e.lineno, e.msg)
    except (ValueError, RecursionError, MemoryError) as e:
        return 'python does not read this: %s' % (e.args[0] if e.args else e.__class__.__name__)
    return None

def ev_code(nd, ctx):
    """code(language, line, line …): the program, one raw quote per source line.  Kind Ac: the act of running it."""
    args = nd.args
    if len(args) < 2:
        ctx.err(nd, 'E-ARITY', 'code takes (language, line, …): the language, then one quote for each line of the program; not %d arguments' % len(args))
        return 'ERR'
    bad = [a for a in args if a.t != 'str' or a.pre]
    if bad:
        ctx.err(bad[0], 'E-KIND', 'code takes plain quotes only: the language, then one quote for each line of the program (no class letter, label, number or other root)')
        return 'ERR'
    lang = args[0].v
    if lang not in LANGS:
        ctx.err(args[0], 'E-CODE', 'the language "%s" is not on the list (%s)' % (lang, ', '.join(LANGS)))
        return 'ERR'
    if lang == 'python':
        why = check_python([a.v for a in args[1:]])
        if why:
            ctx.err(args[1], 'E-CODE', why)
            return 'ERR'
    return 'Ac'

class MathErr(Exception):
    pass

_MTOK = re.compile(r'\s*(?:(?P<num>\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)|(?P<name>[A-Za-z][A-Za-z0-9_]*)|(?P<op><->|==>|<=>|=>|->|&&|\|\||==|\*\*|<=|>=|!=|[-+*/^()=<>,&|]))')
_MRELS = ('=', '!=', '<', '>', '<=', '>=')
_MCONN = ('&', '|', '=>', '<=>')
_MBAD = {'==': 'write = for equality', '**': 'write ^ for a power', '&&': 'write & once for and', '||': 'write | once for or',
         '->': 'write => for if', '==>': 'write => for if', '<->': 'write <=> for if and only if'}
_MCONNHINT = {'&': '& joins claims (each has a comparison such as = < >), but an operand here is a number',
              '|': '| joins claims (each has a comparison such as = < >), but an operand here is a number; for an absolute value write abs(x)',
              '=>': '=> joins claims (each has a comparison such as = < >), but an operand here is a number; for greater or equal write >=, for less or equal <=',
              '<=>': '<=> joins claims (each has a comparison such as = < >), but an operand here is a number'}
_MWORDS = {'and': '&', 'or': '|', 'if': '=>', 'implies': '=>', 'then': '=>', 'iff': '<=>'}
_MHINT = {'%': 'write mod(a,b) for a remainder', '!': 'write fact(n) for a factorial; for not, write not(\'…\') round the formula, or use != < > <= >=',
          '~': 'for not, write not(\'…\') round the formula, or use != < > <= >=',
          '[': 'use round brackets only', ']': 'use round brackets only', '{': 'use round brackets only', '}': 'use round brackets only',
          '.': 'a number has digits on both sides of the point, as in 0.5', '"': 'a quote mark cannot stand in a formula', "'": 'write x_1 rather than a prime or a quote mark'}

def parse_math(s):
    """kind of a formula in ordinary written form: 'Cl' for a claim, 'Nu' for a number; raises MathErr.
       A claim is one comparison (= != < > <= >=), or claims joined by & | => <=>, with round brackets to group.
       Binding, tightest first: + -  *  /  ^ , then a comparison, then &, then |, then =>, then <=>.
       => and <=> take exactly two claims (a chain reads two ways: use brackets); & and | may be chained."""
    if not s.isascii():
        raise MathErr('only ASCII characters: write sqrt(x), pi, <=, >=, !=, =>, <=> instead of the symbols')
    toks, pos = [], 0
    while s[pos:].strip():
        m = _MTOK.match(s, pos)
        if not m:
            ch = s[pos:].lstrip()[0]
            raise MathErr('%r cannot stand in a formula%s' % (ch, ('; ' + _MHINT[ch]) if ch in _MHINT else ' (a formula has numbers, names, + - * / ^ ( ) , = != < > <= >= & | => <=>)'))
        k = m.lastgroup
        toks.append((k, m.group(k), m.start(k)))
        pos = m.end()
    if not toks:
        raise MathErr('the formula is empty')
    for k, v, p in toks:
        if v in _MBAD: raise MathErr('%s (position %d)' % (_MBAD[v], p + 1))
    st = {'i': 0}
    def peek():
        return toks[st['i']] if st['i'] < len(toks) else ('end', '', len(s))
    def take():
        t = peek(); st['i'] += 1; return t
    def fail(msg, t=None):
        t = t or peek()
        raise MathErr('%s (position %d)' % (msg, t[2] + 1) if t[0] != 'end' else '%s (at the end)' % msg)
    def isop(t, *ops):
        return t[0] == 'op' and t[1] in ops
    def claim(kind, t):
        if kind != 'Cl':
            fail(_MCONNHINT[t[1]], t)
    def num(kind, t):
        if kind != 'Nu':
            fail('%s works on numbers, but this is a claim' % t[1], t)
    def formula():
        a = implication()
        if isop(peek(), '<=>'):
            t = take(); claim(a, t)
            b = implication(); claim(b, t)
            if isop(peek(), '<=>'):
                fail('a chain of <=> reads two ways: put brackets round each pair', peek())
            return 'Cl'
        return a
    def implication():
        a = disjunction()
        if isop(peek(), '=>'):
            t = take(); claim(a, t)
            b = disjunction(); claim(b, t)
            if isop(peek(), '=>'):
                fail('a chain of => reads two ways: put brackets, as in A => (B => C) or (A => B) & (B => C)', peek())
            return 'Cl'
        return a
    def disjunction():
        a = conjunction()
        while isop(peek(), '|'):
            t = take(); claim(a, t)
            b = conjunction(); claim(b, t)
            a = 'Cl'
        return a
    def conjunction():
        a = comparison()
        while isop(peek(), '&'):
            t = take(); claim(a, t)
            b = comparison(); claim(b, t)
            a = 'Cl'
        return a
    def comparison():
        a = expr()
        t = peek()
        if t[0] == 'op' and t[1] in _MRELS:
            take()
            if a != 'Nu': fail('%s compares numbers, but its left side is a claim' % t[1], t)
            b = expr()
            if b != 'Nu': fail('%s compares numbers, but its right side is a claim' % t[1], t)
            u = peek()
            if u[0] == 'op' and u[1] in _MRELS:
                fail('only one comparison in a claim: join comparisons with & or |, as in 0<x & x<1', u)
            return 'Cl'
        return a
    def expr():
        a = term()
        while isop(peek(), '+', '-'):
            t = take(); num(a, t)
            b = term(); num(b, t)
            a = 'Nu'
        return a
    def term():
        a = unary()
        while True:
            t = peek()
            if isop(t, '*', '/'):
                take(); num(a, t)
                b = unary(); num(b, t)
                a = 'Nu'
            elif t[0] in ('num', 'name') or isop(t, '('):
                if t[0] == 'name' and t[1].lower() in _MWORDS:
                    fail('write %s, not the word %s' % (_MWORDS[t[1].lower()], t[1]), t)
                if a == 'Cl':
                    fail('claims are joined by & | => <=>', t)
                fail('write * between factors, as in 2*x or (a+b)*(c+d)', t)
            else:
                break
        return a
    def unary():
        if isop(peek(), '-'):
            t = take()
            b = unary(); num(b, t)
            return 'Nu'
        return power()
    def power():
        a = atom()
        if isop(peek(), '^'):
            t = take(); num(a, t)
            b = unary(); num(b, t)
            return 'Nu'
        return a
    def atom():
        t = take()
        if t[0] == 'num':
            return 'Nu'
        if t[0] == 'name':
            if isop(peek(), '('):
                take()
                if isop(peek(), ')'):
                    fail('%s needs at least one argument' % t[1], t)
                while True:
                    a = expr()
                    if a != 'Nu':
                        fail('an argument of %s is a number, not a claim' % t[1], t)
                    u = take()
                    if isop(u, ','):
                        continue
                    if isop(u, ')'):
                        break
                    fail('expected , or ) in the arguments of %s' % t[1], u)
            return 'Nu'
        if isop(t, '('):
            k = formula()
            u = take()
            if not isop(u, ')'):
                fail('a bracket is not closed', t)
            return k
        if t[0] == 'op' and t[1] in _MCONN:
            fail('%s joins two claims and cannot start one%s' % (t[1], '; for an absolute value write abs(x)' if t[1] == '|' else ''), t)
        fail('a number, a name or a bracket is expected here', t)
    kind = formula()
    t = peek()
    if t[0] != 'end':
        fail('%r does not belong here' % t[1], t)
    return kind

def ev_formula(nd, ctx):
    """the kind of a formula quote 'F': Cl with a claim, Nu without one"""
    try:
        return parse_math(nd.v)
    except MathErr as e:
        ctx.err(nd, 'E-MATH', str(e))
        return 'ERR'

def ev_to(nd, ctx):
    args = nd.args
    if len(args) < 2:
        ctx.err(nd, 'E-ARITY', 'to takes (receiver, …, line)')
        return 'ERR'
    for a in args[:-1]:
        if a.t != 'agent' or a.v in ('Me', 'You'):
            ctx.err(a, 'E-KIND', 'to names receivers: agent names or All')
            continue
        if ctx.header and a.v != 'All' and 'All' not in ctx.header[1] and a.v not in ctx.header[1]:
            ctx.err(a, 'E-HEAD', '%s is not a receiver of this message (header: %s)' % (a.v, ','.join(sorted(ctx.header[1]))))
    k = ev(args[-1], ctx)
    if k == 'BARE':
        ctx.err(args[-1], 'E-KIND', 'the last place of to takes a line, not a bare quote')
        return 'ERR'
    if not fits(k, ('Ln',)):
        ctx.err(args[-1], 'E-KIND', 'the last place of to takes a line (claim, question or speech act), but this is %s' % describe(k))
        return 'ERR'
    return 'Ln'

def ev_plain(nd, ctx):
    """a header detail with ordinary places (pri)"""
    ent = ENT[nd.v]
    kinds = [ev(a, ctx) for a in nd.args]
    pl = None
    for spec, res in ent['sigs']:
        pl = expand(spec, len(nd.args))
        if pl is not None:
            break
    if pl is None:
        ctx.err(nd, 'E-ARITY', '%s takes %s' % (nd.v, ' or '.join(sig_text(sp) for sp, r in ent['sigs'])))
        return 'ERR'
    for k, p, a in zip(kinds, pl, nd.args):
        if k != 'BARE' and not fits(k, p):
            ctx.err(a, 'E-KIND', '%s takes %s, but this is %s' % (nd.v, '|'.join(p), describe(k)))
    return 'Hd'

def check_header(nd, ctx):
    args = nd.args
    if not args:
        ctx.err(nd, 'E-HEAD', 'msg needs a sender and at least one receiver'); return
    s = args[0]
    if s.t != 'agent' or s.v in PRON:
        ctx.err(s, 'E-HEAD', 'the first place of msg is the sender, an agent name (not Me, You or All)'); return
    i, recv = 1, []
    while i < len(args) and args[i].t == 'agent':
        r = args[i]
        if r.v in ('Me', 'You'):
            ctx.err(r, 'E-HEAD', '%s cannot be a receiver: name the agent' % r.v)
        elif r.v == s.v:
            ctx.err(r, 'E-HEAD', 'the sender %s cannot be its own receiver' % s.v)
        elif r.v in recv:
            ctx.err(r, 'E-HEAD', 'receiver %s is named twice' % r.v)
        else:
            recv.append(r.v)
        i += 1
    if 'All' in recv and len(recv) > 1:
        ctx.err(args[1], 'E-HEAD', 'All already includes the other receivers')
    if not recv:
        ctx.err(nd, 'E-HEAD', 'msg needs at least one receiver after the sender')
    serial = None
    if i < len(args) and args[i].t == 'num':
        if re.match(r'[1-9]\d*$', args[i].v):
            serial = int(args[i].v)
        else:
            ctx.err(args[i], 'E-HEAD', 'the serial is a whole number from 1')
        i += 1
    if i < len(args) and args[i].t == 'time':
        ev(args[i], ctx); i += 1
    seen = set()
    retarget = None
    own = '%s%d' % (s.v, serial) if serial else None
    while i < len(args):
        a = args[i]
        if a.t == 'app' and a.v == 'pri':
            if a.v in seen:
                ctx.err(a, 'E-HEAD', 'pri appears twice in the header')
            seen.add('pri')
            k = ev_plain(a, ctx)
        elif a.t == 'app' and a.v in ('re', 'saw'):
            if a.v in seen:
                ctx.err(a, 'E-HEAD', '%s appears twice in the header' % a.v)
            seen.add(a.v)
            if not a.args:
                ctx.err(a, 'E-ARITY', '%s takes one or more message names' % a.v)
            for x in a.args:
                if x.t != 'ref':
                    ctx.err(x, 'E-KIND', '%s takes message names such as B2 or B2.3' % a.v)
                elif own and x.v.split('.')[0] == own:
                    ctx.err(x, 'E-HEAD', 'a message cannot refer to itself in its own header')
            if a.v == 're' and len(a.args) == 1 and a.args[0].t == 'ref' and '.' not in a.args[0].v:
                retarget = a.args[0].v
        else:
            ctx.err(a, 'E-HEAD', 'after the receivers the header takes a serial, a send time, re(…) or saw(…); found %r' % (a,))
        i += 1
    ctx.header = (s.v, set(recv), serial)
    ctx.retarget = retarget

RELROOTS = ('agree', 'ans', 'err', 'clr', 'rej', 'unk')

def walk(nd):
    yield nd
    for a in nd.args:
        yield from walk(a)

def expand_rel(nd, ctx):
    """relative line numbers (1.5.5): in the first place of agree ans err clr rej unk, a whole number n stands for
       line n of the one message that the header's re(...) names.  Without such a header the number is left alone (E-KIND)."""
    for x in walk(nd):
        if x.t == 'app' and x.v in RELROOTS and x.args and x.args[0].t == 'num' and re.fullmatch(r'[1-9]\d*', x.args[0].v) and ctx.retarget:
            a0 = x.args[0]
            x.args[0] = N('ref', '%s.%s' % (ctx.retarget, a0.v), line=a0.line, col=a0.col)

def check(text, need_header=False):
    """-> list of dict(line, last, verdict, diags) one per top-level expression, in order"""
    items = parse(text)
    ctx = Ctx()
    out = []
    first = True
    for kind, x in items:
        if kind == 'err':
            out.append(dict(line=x.line, last=x.line, verdict=x.code, diags=[(x.line, x.code, x.msg)]))
            first = False
            continue
        nd = x
        ctx.diags = []
        if first and nd.t == 'app' and nd.v == 'msg':
            check_header(nd, ctx)
            k = 'Hd'
        else:
            if first and need_header:
                ctx.err(nd, 'E-HEAD', 'the first line of a message is its header: msg(from, to…)')
            expand_rel(nd, ctx)
            k = ev(nd, ctx)
            if not ctx.diags or all(d[1] != 'E-HEAD' for d in ctx.diags):
                if k == 'BARE':
                    ctx.err(nd, 'E-KIND', 'a quote alone is not a line: write q"…" for a claim in English')
                elif not isinstance(k, frozenset) and k in ('ERR', 'Un'):
                    pass
                elif not fits(k, ('Ln',)):
                    ctx.err(nd, 'E-KIND', 'a line is a claim, a question or a speech act, but this is %s' % describe(k))
        first = False
        verdict = ctx.diags[0][1] if ctx.diags else 'ok'
        out.append(dict(line=nd.line, last=nd.end, verdict=verdict, diags=list(ctx.diags)))
    return out

def kind_of(text):
    """kind and diagnostics of ONE expression (used to test value-kind examples)"""
    items = parse(text)
    ctx = Ctx()
    if not items or items[0][0] == 'err':
        e = items[0][1] if items else None
        return 'ERR', [(1, e.code if e else 'E-SYN', e.msg if e else 'empty')]
    k = ev(items[0][1], ctx)
    if k == 'BARE': k = 'Th'
    if isinstance(k, frozenset): k = sorted(k)[0]
    return k, ctx.diags


# ==================================================================================================
#  4. THE CHECKS ACROSS MESSAGES  (2.2, 2.3, 2.5 and 1.5.4 of the grammar)
#     A conversation is a list of message texts in transcript order (an observer's order: a message
#     comes after every message it names).  Problems are plain strings.
# ==================================================================================================
QUESTIONS = ('yn', 'what', 'which', 'why')
REFARGS = {'ans': 0, 'agree': 0, 'retr': 0, 'rej': 0, 'err': 0, 'clr': 0, 'unk': 0, 'ack': None}
LABREF = re.compile(r'^([A-Z][a-z]*[0-9]+)\.([ogacnqtd][0-9]+)$')
LINEREF = re.compile(r'^([A-Z][a-z]*[0-9]+)\.([0-9]+)$')
MSGREF = re.compile(r'^[A-Z][a-z]*[0-9]+$')
QUOTEREF = re.compile(r'\{\{|\}\}|\{([^{}]*)\}')


def walk_all(nd):
    yield nd
    for a in nd.args:
        yield from walk_all(a)


def walk_text(nd):
    """the nodes of a line, not looking inside code(...): its quotes are raw text, not references.
       (A formula quote 'F' is a leaf; callers that read quotes for {references} skip it.)"""
    yield nd
    if nd.t == 'app' and nd.v == 'code':
        return
    for a in nd.args:
        yield from walk_text(a)


def analyse(text):
    """-> dict(sender, recv, serial, names, lines, labels), or None when the message has no readable header.
       lines has one entry for each line after the header, in order: its tree, or None when it did not parse
       (so that the numbers of the other lines stay true).  labels: the labels this message defines, which
       other messages may reach as Ana3.o1."""
    items = parse(text)
    if not items or items[0][0] != 'ok':
        return None
    h = items[0][1]
    if h.t != 'app' or h.v != 'msg' or not h.args or h.args[0].t != 'agent':
        return None
    args = h.args
    sender = args[0].v
    i, recv = 1, []
    while i < len(args) and args[i].t == 'agent':
        recv.append(args[i].v)
        i += 1
    serial = int(args[i].v) if i < len(args) and args[i].t == 'num' and re.fullmatch(r'[1-9][0-9]*', args[i].v) else None
    names, retarget = [], None
    for a in args[i:]:
        if a.t == 'app' and a.v == 're' and len(a.args) == 1 and a.args[0].t == 'ref' and '.' not in a.args[0].v:
            retarget = a.args[0].v
        if a.t == 'app' and a.v in ('re', 'saw'):
            for x in a.args:
                if x.t == 'ref':
                    names.append(x.v)
    lines = [x if k == 'ok' else None for k, x in items[1:]]
    if retarget:                                  # relative line numbers (1.5.5)
        for ln in lines:
            if ln is None:
                continue
            for x in walk_all(ln):
                if x.t == 'app' and x.v in RELROOTS and x.args and x.args[0].t == 'num' and re.fullmatch(r'[1-9][0-9]*', x.args[0].v):
                    x.args[0] = N('ref', '%s.%s' % (retarget, x.args[0].v), line=x.args[0].line)
    labels = set()
    for ln in lines:
        if ln is None:
            continue
        for x in walk_text(ln):
            if x.t == 'str' and re.fullmatch(r'[ogacnqtd][0-9]+', x.pre or ''):
                labels.add(x.pre)
            elif x.t == 'app' and x.v == 'def' and x.args and x.args[0].t == 'label':
                labels.add(x.args[0].v)
    return dict(sender=sender, recv=recv, serial=serial, names=names, lines=lines, labels=labels)


def label_refs(ln):
    """(message, label) pairs that a line reaches in other messages: Ana3.o1 as a place, {Ana3.o1} inside a quote"""
    out = []
    for nd in walk_text(ln):
        if nd.t == 'ref':
            m = LABREF.match(nd.v)
            if m:
                out.append((m.group(1), m.group(2)))
        elif nd.t == 'str' and nd.pre != "'":
            for q in QUOTEREF.finditer(nd.v):
                if q.group(1) is not None:
                    m = LABREF.match(q.group(1).strip())
                    if m:
                        out.append((m.group(1), m.group(2)))
    return out


def check_dialogue(texts):
    """-> list of problem strings (empty when the conversation is sound)"""
    probs = []
    nextserial = {}
    roster = None
    known = {}         # message name -> analysis
    for n, t in enumerate(texts, 1):
        a = analyse(t)
        if a is None:
            probs.append('message %d has no readable header' % n)
            continue
        who = a['sender']
        if a['serial'] is not None:
            want = nextserial.get(who, 1)
            if a['serial'] != want:
                probs.append('message %d: %s has serial %d, expected %d' % (n, who, a['serial'], want))
            nextserial[who] = a['serial'] + 1
        name = '%s%d' % (who, a['serial']) if a['serial'] else None
        joins = set(x.v for ln in a['lines'] if ln is not None for nd in walk_all(ln) if nd.t == 'app' and nd.v == 'join' for x in nd.args)
        if roster is None:
            if 'All' not in a['recv']:
                roster = set([who] + a['recv'])
        else:
            if who not in roster:
                probs.append('message %d: %s writes but is not on the roster' % (n, who))
            for r in a['recv']:
                if r != 'All' and r not in roster and r not in joins:
                    probs.append('message %d: receiver %s is not on the roster' % (n, r))
        for ref in a['names']:
            base = ref.split('.')[0]
            if base not in known:
                probs.append('message %d: header names %s, which is not an earlier message' % (n, ref))
            elif '.' in ref:
                k = ref.split('.')[1]
                if k.isdigit() and int(k) > len(known[base]['lines']):
                    probs.append('message %d: header names %s but that message has %s lines' % (n, ref, len(known[base]['lines'])))
        for ln_i, ln in enumerate(a['lines'], 1):
            if ln is None:
                continue
            handled = set()
            for nd in walk_all(ln):
                if nd.t == 'app' and nd.v in REFARGS:
                    for x in (nd.args if REFARGS[nd.v] is None else nd.args[:1]):
                        if x.t == 'ref':
                            handled.add(id(x))
                            base = x.v.split('.')[0]
                            if base == name:
                                tgt = a                                   # the sender's own line (retr, or a reference inside the message)
                            elif base not in known:
                                probs.append('message %d line %d: %s(%s) names a message that is not earlier' % (n, ln_i, nd.v, x.v))
                                continue
                            else:
                                tgt = known[base]
                            if '.' in x.v and x.v.split('.')[1].isdigit():
                                k = int(x.v.split('.')[1])
                                if k < 1 or k > len(tgt['lines']):
                                    probs.append('message %d line %d: %s has no line %d%s' % (n, ln_i, base, k,
                                           ' (the header is not a line: line 1 is the first line after it)' if k == len(tgt['lines']) + 1 else ''))
                                elif nd.v == 'ans':
                                    target = tgt['lines'][k - 1]
                                    while target is not None and target.t == 'app' and target.v == 'to' and target.args:
                                        target = target.args[-1]          # a question sent to some receivers is still a question
                                    root = target.v if target is not None and target.t == 'app' else ''
                                    if root not in QUESTIONS:
                                        probs.append('message %d line %d: ans(%s) answers a line that is not a question' % (n, ln_i, x.v))
                if nd.t == 'app' and nd.v in ('join', 'leave') and roster is not None:
                    for x in nd.args:
                        (roster.add if nd.v == 'join' else roster.discard)(x.v)
            for x in walk_text(ln):                                # a line reference in any root (ent, grp, supp, is, …) names a line that exists
                if x.t != 'ref' or id(x) in handled:
                    continue
                m = LINEREF.match(x.v)
                if m:
                    base, k = m.group(1), int(m.group(2))
                    if base == name:
                        tgt = a
                    elif base not in known:
                        probs.append('message %d line %d: %s names a message that is not earlier' % (n, ln_i, x.v))
                        continue
                    else:
                        tgt = known[base]
                    if k < 1 or k > len(tgt['lines']):
                        probs.append('message %d line %d: %s has no line %d%s' % (n, ln_i, base, k,
                               ' (the header is not a line: line 1 is the first line after it)' if k == len(tgt['lines']) + 1 else ''))
                elif MSGREF.match(x.v) and x.v != name and x.v not in known:
                    probs.append('message %d line %d: %s names a message that is not earlier' % (n, ln_i, x.v))
            seen = set()
            for base, lab in label_refs(ln):                       # 1.5.4: a label belongs to the message that defines it
                if base == name or (base, lab) in seen:
                    continue
                seen.add((base, lab))
                if base not in known:
                    probs.append('message %d line %d: %s.%s names a message that is not earlier' % (n, ln_i, base, lab))
                elif lab not in known[base]['labels']:
                    probs.append('message %d line %d: %s.%s: %s defines no label %s (E-NAME; a label belongs to the message that defines it, 1.5.4)' % (n, ln_i, base, lab, base, lab))
        if name:
            known[name] = a
    return probs


def split_dialogue(block_lines):
    """the lines of a dialogue block -> message texts; a line of three hyphens ends a message"""
    msgs, cur = [], []
    for l in block_lines:
        if l.strip() == '---':
            msgs.append('\n'.join(cur))
            cur = []
        else:
            cur.append(l)
    if cur:
        msgs.append('\n'.join(cur))
    return msgs


# ==================================================================================================
#  5. READING A CONVERSATION AND REPORTING
# ==================================================================================================
def meaningful(line):
    s = line.strip()
    return bool(s) and not s.startswith('#')


def split_messages(text):
    """text -> [(first file line, message text)].
       If a line holds only '---', messages end at those lines; otherwise a message starts at every line that begins with msg(."""
    lines = text.split('\n')
    out, cur, start = [], [], 1
    if any(l.strip() == '---' for l in lines):
        for i, l in enumerate(lines, 1):
            if l.strip() == '---':
                out.append((start, '\n'.join(cur)))
                cur, start = [], i + 1
            else:
                cur.append(l)
    else:
        for i, l in enumerate(lines, 1):
            if l.strip().startswith('msg(') and any(meaningful(x) for x in cur):
                out.append((start, '\n'.join(cur)))
                cur, start = [], i
            cur.append(l)
    out.append((start, '\n'.join(cur)))
    return [(s, t) for s, t in out if any(meaningful(x) for x in t.split('\n'))]


def one_message(index, start, text, need_header=True):
    """check one message -> dict for the report"""
    src = text.split('\n')
    results = check(text, need_header=need_header)
    an = analyse(text)
    first = next((l for l in src if meaningful(l)), '')
    m = dict(index=index, file_line=start, name=None, sender=None, receivers=[], serial=None, header=None, lines=[])
    if an:
        m['sender'], m['receivers'], m['serial'] = an['sender'], an['recv'], an['serial']
        if an['serial']:
            m['name'] = '%s%d' % (an['sender'], an['serial'])
    if first.strip().startswith('msg(') and results:
        h = results.pop(0)
        m['header'] = dict(verdict=h['verdict'], source=src[h['line'] - 1].strip(),
                           diagnostics=[dict(code=d[1], message=d[2]) for d in h['diags']])
    for n, r in enumerate(results, 1):
        m['lines'].append(dict(n=n, file_line=start + r['line'] - 1, source=src[r['line'] - 1].strip(), verdict=r['verdict'],
                               diagnostics=[dict(code=d[1], message=d[2]) for d in r['diags']]))
    return m


def check_conversation(msgs, need_header=True, across=True):
    """msgs: [(first file line, text)] in transcript order -> report dict"""
    ms = [one_message(i, s, t, need_header) for i, (s, t) in enumerate(msgs, 1)]
    dlg = check_dialogue([t for s, t in msgs]) if across and len(msgs) > 1 else []
    def relabel(p):
        def sub(m):
            i = int(m.group(1))
            return (label(ms[i - 1]) if 1 <= i <= len(ms) else m.group(0)) + ('.' + m.group(3) if m.group(3) else '')
        return re.sub(r'^message ([0-9]+)( line ([0-9]+))?', sub, p)
    dlg = [relabel(p) for p in dlg]
    nlines = sum(len(m['lines']) for m in ms)
    bad = sum(1 for m in ms for l in m['lines'] if l['verdict'] != 'ok') + sum(1 for m in ms if m['header'] and m['header']['verdict'] != 'ok') + len(dlg)
    return dict(rules='SILEX-r6.5', ok=(bad == 0), messages=ms, across_messages=dlg,
                counts=dict(messages=len(ms), lines=nlines, problems=bad))


def label(m):
    return m['name'] or '#%d' % m['index']


def clip(s, n=110):
    return s if len(s) <= n else s[:n - 1] + '…'


def format_report(rep, verbose=False, quiet=False):
    out = []
    for m in rep['messages']:
        probs = [l for l in m['lines'] if l['verdict'] != 'ok']
        hp = m['header'] is not None and m['header']['verdict'] != 'ok'
        npr = len(probs) + (1 if hp else 0)
        loose = m.get('loose')
        nl_ = len(m['lines'])
        if not quiet:
            who = 'loose lines' if loose else ('%s -> %s' % (m['sender'], ','.join(m['receivers'])) if m['sender'] else 'no readable header')
            out.append('%-8s %-24s %2d line%s   %s' % ('lines' if loose else label(m), who, nl_, '' if nl_ == 1 else 's', 'ok' if npr == 0 else '%d problem%s' % (npr, '' if npr == 1 else 's')))
        if hp:
            h = m['header']
            out.append('    %s header  %s  %s' % (label(m), h['verdict'], '; '.join(d['message'] for d in h['diagnostics'])))
            out.append('        %s' % clip(h['source']))
        for l in m['lines']:
            if l['verdict'] == 'ok':
                if verbose:
                    out.append('    %s  ok  %s' % ('line %d' % l['n'] if loose else '%s.%d' % (label(m), l['n']), clip(l['source'])))
                continue
            out.append('    %s  %s  %s' % ('line %d' % l['n'] if loose else '%s.%d' % (label(m), l['n']), l['verdict'], '; '.join(d['message'] for d in l['diagnostics'])))
            out.append('        %s    (file line %d)' % (clip(l['source']), l['file_line']))
    if rep['across_messages']:
        out.append('Across messages:')
        for p in rep['across_messages']:
            out.append('    ' + p)
    c = rep['counts']
    what = '%d line%s' % (c['lines'], '' if c['lines'] == 1 else 's')
    if not (rep['messages'] and rep['messages'][0].get('loose')):
        what = '%d message%s, %s' % (c['messages'], '' if c['messages'] == 1 else 's', what)
    out.append('RESULT: %s, %s' % (what, 'all ok' if rep['ok'] else '%d problem%s' % (c['problems'], '' if c['problems'] == 1 else 's')))
    return '\n'.join(out)


def check_loose_lines(text):
    """lines with no header needed (the 'sx' blocks of the grammar)"""
    src = text.split('\n')
    lines = []
    for n, r in enumerate(check(text, need_header=False), 1):
        lines.append(dict(n=n, file_line=r['line'], source=src[r['line'] - 1].strip(), verdict=r['verdict'],
                          diagnostics=[dict(code=d[1], message=d[2]) for d in r['diags']]))
    bad = sum(1 for l in lines if l['verdict'] != 'ok')
    m = dict(index=1, file_line=1, name=None, sender=None, receivers=[], serial=None, header=None, lines=lines, loose=True)
    return dict(rules='SILEX-r6.5', ok=(bad == 0), messages=[m], across_messages=[], counts=dict(messages=1, lines=len(lines), problems=bad))


# ----------------------------------------------------------------------- markdown files: the "file verifier" of 6.1
def md_blocks(text):
    out, i, lines = [], 0, text.split('\n')
    while i < len(lines):
        m = re.match(r'```(silex|sx|dialogue)\s*$', lines[i])
        if m:
            j = i + 1
            while j < len(lines) and not lines[j].startswith('```'):
                j += 1
            out.append((m.group(1), i + 2, lines[i + 1:j]))
            i = j
        i += 1
    return out


def md_expected(src):
    m = re.search(r'#\s*(ok|E-[A-Z]+)\b', src)
    return m.group(1) if m else None


def verify_markdown(text, name='file'):
    """Run every fenced block marked silex (one message, header first), sx (loose lines) or dialogue (messages divided by ---).
       A line that ends in '# ok' or '# E-XXXX' must get exactly that verdict; a line with no such comment must be ok.
       -> dict(blocks, lines, unmarked, problems(list of str))"""
    nb = nl = unmarked = 0
    probs = []
    for kind, first, src in md_blocks(text):
        nb += 1
        if kind == 'dialogue':
            msgs = split_dialogue(src)
            for p in check_dialogue(msgs):
                probs.append('%s:%d: dialogue: %s' % (name, first, p))
            off = 0
            for mtxt in msgs:
                mlines = mtxt.split('\n')
                for x in check(mtxt, need_header=True):
                    ln = x['line']
                    nl += 1
                    exp = md_expected(mlines[ln - 1])
                    if exp is None:
                        unmarked += 1
                        if x['verdict'] != 'ok':
                            probs.append('%s:%d: unmarked line gives %s: %s' % (name, first + off + ln - 1, x['verdict'], mlines[ln - 1][:90]))
                    elif exp != x['verdict']:
                        probs.append('%s:%d: expected %s, got %s (%s): %s' % (name, first + off + ln - 1, exp, x['verdict'], '; '.join(d[2] for d in x['diags'])[:100], mlines[ln - 1][:80]))
                off += len(mlines) + 1
            continue
        for x in check('\n'.join(src), need_header=(kind == 'silex')):
            ln = x['line']
            nl += 1
            exp = md_expected(src[ln - 1])
            if exp is None:
                unmarked += 1
                if x['verdict'] != 'ok':
                    probs.append('%s:%d: unmarked line gives %s: %s' % (name, first + ln - 1, x['verdict'], src[ln - 1][:90]))
            elif exp != x['verdict']:
                probs.append('%s:%d: expected %s, got %s (%s): %s' % (name, first + ln - 1, exp, x['verdict'], '; '.join(d[2] for d in x['diags'])[:100], src[ln - 1][:80]))
    return dict(blocks=nb, lines=nl, unmarked=unmarked, problems=probs)


# ==================================================================================================
#  6. SELF-TEST  (the data are at the end of this file)
# ==================================================================================================
WRAP = {'Nu': 'eq(%s,1)', 'Va': 'eq(%s,"x")', 'Gr': 'many(%s)', 'Th': 'is(%s,"x")', 'Ac': 'will(%s)', 'Tm': 'at(%s,fin("x"))',
        'Cr': 'all("x",%s)', 'Du': 'for(%s,fin("x"))', 'Ag': 'is(%s,"x")'}


def check_example(ex):
    """the example of a root in the lexicon -> (verdict, detail); a value is put inside a line that takes it"""
    if ex.startswith('msg('):
        r = check(ex)
        return r[0]['verdict'], '; '.join(x[2] for x in r[0]['diags'])
    k, d = kind_of(ex.split('\n')[0]) if ex.count('\n') == 0 else ('ERR', [])
    if d:
        return d[0][1], d[0][2]
    if fits(k, ('Ln',)):
        r = check(ex)
        return r[0]['verdict'], '; '.join(x[2] for x in r[0]['diags'])
    if k not in WRAP:
        return 'E-KIND', 'example is a %s' % k
    r = check(WRAP[k] % ex)
    return r[0]['verdict'], '; '.join(x[2] for x in r[0]['diags'])


def selftest(verbose=False):
    fails = total = 0
    def fail(*a):
        nonlocal fails
        fails += 1
        print('FAIL', *a)
    for e in load_lexicon():                                   # 1. each root's own example is accepted
        total += 1
        v, d = check_example(e['example'])
        if v != 'ok':
            fail('example of', e['root'], '|', e['example'], '|', v, d)
    n1 = total
    for want, text in CASES_LINES:                             # 2. single lines, accepted and refused
        total += 1
        got = check(text.replace('<NL>', '\n'))[0]['verdict']
        if got != want:
            fail('line: expected', want, 'got', got, '|', text[:100])
    n2 = total
    for name, text, want, header in CASES_MESSAGES:            # 3. whole messages: bare line numbers, compact times
        total += 1
        got = [r['verdict'] for r in check(text, need_header=header)]
        if got != want:
            fail('message', name, 'expected', want, 'got', got)
    n3 = total
    for name, msgs, want in CASES_CONVERSATIONS:               # 4. conversations: what is found across messages
        total += 1
        got = check_dialogue(msgs)
        lines = [r['verdict'] for t in msgs for r in check(t, need_header=True) if r['verdict'] != 'ok']
        if lines:
            fail('conversation', name, 'has refused lines', lines)
        elif len(got) != len(want) or any(w not in g for w, g in zip(want, got)):
            fail('conversation', name, 'expected', want, 'got', got)
    print('selftest: %d checks (%d root examples, %d lines, %d messages, %d conversations), %d failures' % (
        total, n1, n2 - n1, n3 - n2, total - n3, fails))
    return fails


# ==================================================================================================
#  7. COMMAND LINE
# ==================================================================================================
KINDS = [
    ('Ag', 'an agent: Ana, Me, All'), ('Th', 'a thing: an object, person, place, event, anything talked about as one'),
    ('Gr', 'a group of things'), ('Ac', 'an act (code(...) is an act)'), ('Nu', 'a number'), ('Tm', 'a time'), ('Du', 'a duration'),
    ('Cr', 'a criterion: the name of a property or a relation'), ('Cl', 'a claim: true or false'), ('Q', 'a question'),
    ('Ln', 'a line: a claim, a question or a speech act'), ('Rf', 'a reference to a message or one of its lines'),
    ('Va', 'any value: every kind above except Q and Ln'), ('X', 'a place that takes a claim, an act or a line'),
    ('Vr', 'a new label that the root binds, for use inside its other place'), ('Nm', 'a new label that the root defines'),
    ('Hd', 'a part of a header: msg, re, saw, pri'), ('An', 'an answer to a yes-or-no question: yes, no'), ('Dg', 'a degree: hi, mid, lo'),
    ('Un', 'unspecified: _'), ('Rw', "a quote carried as it is (the lines of code); a formula quote 'F' is a claim or a number, a value of its own"),
    ('=2', 'the result has the kind of the second place'),
]
SIG_NOTES = ('Reading a signature: places are separated by spaces; "A|B" = either kind; "[K]" = optional; "K..." = one or more; '
             '"*K" = one or more, first; ";" separates the forms a root has; "-> R" is the kind the root returns.')


def print_roots(names):
    ents = load_lexicon()
    if names:
        want = set(names)
        ents = [e for e in ents if e['root'] in want]
        missing = sorted(want - set(e['root'] for e in ents))
        if missing:
            print('not roots of this grammar: ' + ', '.join(missing))
            near_ = sorted(set(r for w in missing for r in near(w)))
            if near_:
                print('near: ' + ', '.join(near_))
    sec = None
    for e in ents:
        if not names and e['section'] != sec:
            sec = e['section']
            print('\n## %s' % sec)
        print('%-8s %s' % (e['root'], e['sig']))
        if names:
            print('         %s\n         e.g. %s' % (e['reading'], e['example']))
    if not names:
        print('\n' + SIG_NOTES)
        print('Atoms: ' + ', '.join('%s (%s)' % (a, k) for a, k, _ in ATOMS))


def read_input(path):
    if path == '-':
        data = sys.stdin.read()
    else:
        with open(path, encoding='utf-8-sig', errors='replace') as f:
            data = f.read()
    return data.replace('\r\n', '\n').replace('\r', '\n')


def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser(
        prog='silex_check.py', formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Checker for SILEX messages (rules of SILEX-r6.5).  Nothing is run or sent; the English inside quotes is not read beyond the word rules of 1.4.5.',
        epilog=('examples:\n'
                '  python3 silex_check.py chat.txt          messages one after another (each begins with its msg(...) header, or divide them with a line ---)\n'
                '  python3 silex_check.py -                 the same, from standard input\n'
                '  python3 silex_check.py --lines x.txt     loose lines, no header needed\n'
                '  python3 silex_check.py SILEX-r6.5.md     run every example in a markdown file against its # ok / # E-... comments\n'
                '  python3 silex_check.py --root ent --root code    show the places of roots\n\n'
                'Line numbers are the grammar\'s: line 1 is the first line after the header.  Ana1.2 is line 2 of message Ana1; #3.2 is line 2 of the third\n'
                'message when its header has no serial.  Exit status: 0 all ok, 1 problems found, 2 could not run.'))
    ap.add_argument('files', nargs='*', help='files to check; - is standard input')
    ap.add_argument('--lines', action='store_true', help='the input is loose lines, with no header')
    ap.add_argument('--md', action='store_true', help='the input is a markdown file with fenced silex / sx / dialogue blocks (automatic for names ending in .md)')
    ap.add_argument('--text', action='store_true', help='read a .md file as plain messages instead')
    ap.add_argument('--per-message', action='store_true', help='check each message alone: skip the checks across messages (serials, roster, re/saw, line numbers, labels)')
    ap.add_argument('-v', '--verbose', action='store_true', help='list every line, not only the problems')
    ap.add_argument('-q', '--quiet', action='store_true', help='print only problems and the result')
    ap.add_argument('--json', action='store_true', help='print the report as JSON')
    ap.add_argument('--selftest', action='store_true', help='run the built-in tests')
    ap.add_argument('--roots', action='store_true', help='list every root with its places')
    ap.add_argument('--root', action='append', default=[], metavar='NAME', help='show one root (repeat for more)')
    ap.add_argument('--kinds', action='store_true', help='list the kinds used in the places of roots')
    ap.add_argument('--version', action='store_true')
    a = ap.parse_args(argv)
    if a.version:
        print('silex_check %s: rules of SILEX-r6.5, %d roots' % (__version__, len(ENT)))
        return 0
    if a.selftest:
        return 1 if selftest() else 0
    if a.kinds:
        for k, d in KINDS:
            print('%-3s %s' % (k, d))
        return 0
    if a.roots or a.root:
        print_roots(a.root)
        return 0
    files = a.files
    if not files:
        if sys.stdin.isatty():
            ap.print_help()
            return 2
        files = ['-']
    status = 0
    reports = []
    for path in files:
        try:
            text = read_input(path)
        except (OSError, UnicodeError) as e:
            print('cannot read %s: %s' % (path, e), file=sys.stderr)
            return 2
        is_md = a.md or (not a.text and not a.lines and (path.lower().endswith('.md') or re.search(r'^```', text, re.M) is not None))
        if is_md:
            r = verify_markdown(text, path if path != '-' else 'input')
            reports.append(dict(file=path, mode='markdown', blocks=r['blocks'], lines=r['lines'], without_verdict_comment=r['unmarked'], problems=r['problems']))
            if not a.json:
                for p in r['problems']:
                    print(p)
                print('%s: %d blocks, %d lines checked, %d without a verdict comment, %d problems' % (path if path != '-' else 'input', r['blocks'], r['lines'], r['unmarked'], len(r['problems'])))
            if r['problems']:
                status = max(status, 1)
            if not r['blocks']:
                print('no fenced blocks marked silex, sx or dialogue were found in %s.  Mark each message ```silex (several messages: ```dialogue, divided by ---),\n'
                      'or save the messages in a plain text file without fences (a file whose name ends in .md needs --text).' % (path if path != '-' else 'the input'), file=sys.stderr)
                status = 2
            continue
        if a.lines:
            rep = check_loose_lines(text)
        else:
            rep = check_conversation(split_messages(text), across=not a.per_message)
        if not rep['counts']['lines'] and not any(m['header'] for m in rep['messages']):
            print('nothing to check in %s: no messages or lines found' % (path if path != '-' else 'the input'), file=sys.stderr)
            return 2
        rep['file'] = path
        reports.append(rep)
        if not a.json:
            if len(files) > 1:
                print('== %s' % path)
            print(format_report(rep, verbose=a.verbose, quiet=a.quiet))
        if not rep['ok']:
            status = max(status, 1)
    if a.json:
        print(json.dumps(reports[0] if len(reports) == 1 else reports, indent=2, ensure_ascii=False))
    return status


# ==================================================================================================
#  8. SELF-TEST DATA
# ==================================================================================================
# single lines: expected verdict, line (<NL> stands for a real line break)
CASES_LINES = [('ok', 'will(code("python","print(1)"))'),
 ('ok', 'will(code("python","def f(x):","    return x+1"))'),
 ('ok', 'pls(Ben,code("python","x = {1: 2}","print(f""{x}"")"))'),
 ('ok', 'will(code("python","# set the value of my variable here","x = 1"))'),
 ('ok', 'def(a1,code("python","def f(x):","    return x+1"))'),
 ('ok', 'will(tell(Ben,code("bash","ls -l")))'),
 ('E-KIND', 'tell(Ben,code("bash","ls -l"))'),
 ('ok', 'pls(Ben,then(code("bash","make"),code("bash","make test")))'),
 ('ok', 'will(code("python","    for i in range(3):","        print(i)"))'),
 ('ok', 'will(code("python","return x"))'),
 ('ok', 'will(code("python","def f(x):","","    return x"))'),
 ('ok', 'will(code("text","anything at all {} and the rest"))'),
 ('ok', 'will(code("sql","SELECT * FROM t WHERE a = \'x\';"))'),
 ('ok', 'will(code("python","s = ""a#b"""))'),
 ('ok', 'will(code("python","print(""hi"")","print(\'it\'\'s\')"))'),
 ('ok', 'sug(code("python","x = 1"))'),
 ('ok', 'hyp(is(code("python","x = 1"),"idempotent"))'),
 ('ok', 'fin(code("bash","make"),"successfully")'),
 ('ok', 'will(code("python","import re","m = re.match(r\'\\d+\', s)"))'),
 ('ok', 'will(code("javascript","const f = (x) => ({a: x});"))'),
 ('ok', 'will(code("python",""))'),
 ('E-CODE', 'will(code("python","def f(:"))'),
 ('E-CODE', 'will(code("python","if x:","pass"))'),
 ('E-CODE', 'will(code("cobol","DISPLAY 1"))'),
 ('E-CODE', 'will(code("Python","x = 1"))'),
 ('E-CODE', 'will(code("python","else:"))'),
 ('E-CODE', 'will(code("python","x = ("))'),
 ('E-CODE', 'will(code("python","print \'x\'"))'),
 ('E-CODE', 'will(code("python","x = 1","  y = 2"))'),
 ('E-ARITY', 'will(code("python"))'),
 ('E-ARITY', 'will(code())'),
 ('E-KIND', 'will(code(python,"x = 1"))'),
 ('E-KIND', 'will(code("python",o"x = 1"))'),
 ('E-KIND', 'will(code("python",12))'),
 ('E-KIND', 'will(code("python",plus(1,2)))'),
 ('E-KIND', 'code("python","x = 1")'),
 ('E-KIND', 'all("servers",code("python","x = 1"))'),
 ('E-SYN', 'will(code("python","x = 1<NL>y = 2"))'),
 ('ok', "and('x>0','x<10')"),
 ('ok', "'f(x)=2*x+1'"),
 ('ok', "'x + 1 = 2'"),
 ('ok', "ent(grp('x^2-5*x+6=0'),'(x-2)*(x-3)=0')"),
 ('E-MATH', "'   '"),
 ('E-MATH', "'(x+1'"),
 ('E-MATH', "'x+1)'"),
 ('E-MATH', "'x y=1'"),
 ('E-MATH', "'(a+b)(c+d)=1'"),
 ('E-MATH', "'x==3'"),
 ('E-MATH', "'x**2=4'"),
 ('E-MATH', "'x='"),
 ('E-MATH', "'=3'"),
 ('E-MATH', "'√x=2'"),
 ('E-MATH', "'f()'"),
 ('E-MATH', "'f(x,)'"),
 ('E-MATH', "'f(,x)'"),
 ('E-MATH', "'1..2'"),
 ('E-MATH', "'3.'"),
 ('E-MATH', "'.5'"),
 ('E-MATH', "'a,b'"),
 ('E-MATH', "'+x'"),
 ('E-MATH', "'x^'"),
 ('E-MATH', "'[x]'"),
 ('E-MATH', '\'say "hi"\''),
 ('E-KIND', 'all("servers",\'x\')'),
 ('E-LEX', 'math("x^2=4")'),
 ('E-LEX', "math('x^2=4')"),
 ('E-LEX', 'math()'),
 ('E-LEX', 'eq(math("2^10-1"),1023)'),
 ('E-LEX', 'and(math("x>0"),math("x<10"))'),
 ('E-QUOTE', 'pls(Ben,"restart the server")'),
 ('E-QUOTE', 'pls(Ben,"restart {o9")'),
 ('E-QUOTE', 'pls(Ben,a"print(f\'{x}\')")'),
 ('ok', 'will("review {Dex7.a1}")'),
 ('E-ARITY', 'will(Gds,"review {Dex7.a1}")'),
 ('ok', 'plan(Gds,"review {Dex7.a1}")'),
 ('ok', 'pls(Gds,"review {Dex7.a1}")'),
 ('ok', 'val("average of empty list","result","undefined")'),
 ('ok', 'val("{Dex7.a1}","review result","no change needed")'),
 ('ok', 'val("run of {Dex7.a1}","output","42")'),
 ('ok', 'pls(Ben,"restart service")'),
 ('E-QUOTE', 'pls(Ben,"restart the service")'),
 ('ok', 'will("keep raise form")'),
 ('E-QUOTE', 'will("keep the raise form")')]

# the formula quote 'F', claims joined by & | => <=>, a lone line reference as the premises of ent.  One case a line: verdict, then the text.
_R64_LINES = r'''
ok 'x^2-5*x+6=0'
ok 'x>=3'
ok 'x != 3'
ok eq('2^10-1',1023)
ok over('a*b',10)
ok if('x>0',pls("continue"))
ok prob('x>0',hi)
ok hyp('a^2+b^2=c^2')
ok eq(n"result",'12*15/100')
ok val("rate","value",'3/4')
ok pls(Ben,'x>0')
ok '(-b+sqrt(b^2-4*a*c))/(2*a)=x'
ok 'sum(i^2,i,1,n)=n*(n+1)*(2*n+1)/6'
ok 'f(g(x),h(1,2))=y'
ok 'x_1+x_2=s'
ok '0.5*x=1e-3'
ok '-x^2<0'
ok '2^-3=0.125'
ok '2^3^2=512'
ok will(code("python","x = 'a'"))
ok pls(Ben,"don't restart")
ok ent(grp('x=1'),'y=2',"x's value")
ok '(x+1)*2=4'
ok '(x+1)*(x-1)=x^2-1 & x>0'
ok 'x>0 & x<10'
ok 'x=1 | x=2'
ok 'x>0 => x^2>0'
ok 'x^2=4 <=> x=2 | x=-2'
ok '(x=1 | x=2) & y=3'
ok '0<x & x<1 => x^2<x'
ok 'a=1 & b=2 & c=3'
ok 'a=1 | b=2 | c=3'
ok 'a=1 & b=2 | c=3'
ok '(a=1 => b=2) <=> (c=3 | d=4)'
ok '(a=b)'
ok '((a=b))'
ok and('x>0',is("x","real"))
E-LEX math("x>0 & x<10")
ok ent(Ben1.8,'x=1')
E-KIND ent(Ben1,'x=1')
ok ent(grp(Ben1.8),'x=1')
ok ent(grp(Ben1.8,Ben1.9),'x=1',"Cramer rule")
ok ent(Ben1.8,'x=1',"Cramer rule")
ok ent("test results",is("release build","safe"))
ok ent(Ben1.8,is("release build","safe"))
ok ent(Ben1.g1,'x=1')
E-MATH 'x>0 and x<5'
E-MATH 'x>0 or x<5'
E-MATH 'x=1 & y'
E-MATH 'x & y=1'
E-MATH '|x|>2'
E-MATH 'x=>3'
E-MATH 'x=1 => y=2 => z=3'
E-MATH 'x=1 <=> y=2 <=> z=3'
E-MATH 'x=1 &'
E-MATH '& x=1'
E-MATH '(x=1'
E-MATH 'x=1)'
E-MATH 'x=1 && y=2'
E-MATH 'x=1 || y=2'
E-MATH 'x=1 -> y=2'
E-MATH 'x=1 <-> y=2'
E-MATH '(a=b)+1=2'
E-MATH '(a=b)=c'
E-MATH 'a<b<c'
E-MATH 'x=y=z'
E-MATH 'x ≤ 3'
E-MATH ''
E-MATH '  '
E-MATH '2x=4'
E-MATH 'x%3=1'
E-MATH '!x=1'
E-MATH 'f(x>0)=1'
E-MATH 'the answer is 4'
E-MATH 'x=1 & (y=2'
E-MATH 'x=1,y=2'
E-MATH 'x^2-'
E-KIND 'x+1'
E-KIND not('x+1')
E-KIND pls(Ben,'x+1')
E-KIND all("servers",'x=1')
E-KIND ent('x=1','y=2')
E-LEX math('x=1')
E-KIND code("python",'x=1')
E-KIND ent(12,'x=1')
E-KIND ent(Ben1.8,'x=1','y=2')
E-KIND all("servers",'x>0')
E-SYN pls(Ben,'x=1)
E-SYN 'x=1''y=2'
E-SYN 'x=1' 'y=2'
E-SYN q'x=1'
E-SYN eq('x=1'
E-ARITY ent(Ben1.8)
E-ARITY ent()
'''
CASES_LINES += [tuple(l.split(' ', 1)) for l in _R64_LINES.strip().split('\n')]

# whole messages: name, text, expected verdict of each line (the header first), whether a header is required
CASES_MESSAGES = [('relative agree', 'msg(Ben,Ana,2,re(Ana1))\nagree(2)', ['ok', 'ok'], True),
 ('relative ans', 'msg(Ben,Ana,2,re(Ana1))\nans(1,yes)', ['ok', 'ok'], True),
 ('relative ans value number', 'msg(Ben,Ana,2,re(Ana1))\nans(3,12)', ['ok', 'ok'], True),
 ('relative rej with basis', 'msg(Ben,Ana,2,re(Ana1))\nrej(1,not(may(Me,"write to job scheduler")))', ['ok', 'ok'], True),
 ('relative unk', 'msg(Ben,Ana,2,re(Ana1))\nunk(2)', ['ok', 'ok'], True),
 ('relative err', 'msg(Ben,Ana,2,re(Ana1))\nerr(1,q"date is wrong")', ['ok', 'ok'], True),
 ('relative clr', 'msg(Ben,Ana,2,re(Ana1))\nclr(2)', ['ok', 'ok'], True),
 ('relative inside if', 'msg(Ben,Ana,2,re(Ana1))\nif(is("build","green"),agree(1))', ['ok', 'ok'], True),
 ('full reference still fine', 'msg(Ben,Ana,2,re(Ana1))\nagree(Ana1.2)', ['ok', 'ok'], True),
 ('two re targets', 'msg(Ben,Ana,Cy,2,re(Ana1,Cy1))\nagree(1)', ['ok', 'E-KIND'], True),
 ('no re', 'msg(Ben,Ana,2)\nagree(1)', ['ok', 'E-KIND'], True),
 ('saw only', 'msg(Ben,Ana,2,saw(Ana1))\nagree(1)', ['ok', 'E-KIND'], True),
 ('re names a line', 'msg(Ben,Ana,2,re(Ana1.2))\nagree(1)', ['ok', 'E-KIND'], True),
 ('zero', 'msg(Ben,Ana,2,re(Ana1))\nagree(0)', ['ok', 'E-KIND'], True),
 ('negative', 'msg(Ben,Ana,2,re(Ana1))\nagree(-1)', ['ok', 'E-KIND'], True),
 ('decimal', 'msg(Ben,Ana,2,re(Ana1))\nagree(2.5)', ['ok', 'E-KIND'], True),
 ('retr has no short form', 'msg(Ben,Ana,2,re(Ana1))\nretr(1)', ['ok', 'E-KIND'], True),
 ('ack has no short form', 'msg(Ben,Ana,2,re(Ana1))\nack(1)', ['ok', 'E-KIND'], True),
 ('numbers elsewhere are numbers', 'msg(Ben,Ana,2,re(Ana1))\nover(3,2)', ['ok', 'ok'], True),
 ('number in second place', 'msg(Ben,Ana,2,re(Ana1))\nans(1,3)', ['ok', 'ok'], True),
 ('number as a value in val', 'msg(Ben,Ana,2,re(Ana1))\nval("server","RAM in GB",16)', ['ok', 'ok'], True),
 ('loose line, no header', 'agree(1)', ['E-KIND'], False),
 ('compact time', 'msg(Ana,Ben,1)\nby(20261106T1700,fin("smoke test"))', ['ok', 'ok'], True),
 ('compact with seconds', 'msg(Ana,Ben,1)\nat(20261106T170030,fin("backup"))', ['ok', 'ok'], True),
 ('compact with offset', 'msg(Ana,Ben,1)\nat(20261106T1700+0530,fin("backup"))', ['ok', 'ok'], True),
 ('compact with Z', 'msg(Ana,Ben,1)\nat(20261106T1700Z,fin("backup"))', ['ok', 'ok'], True),
 ('compact interval', 'msg(Ana,Ben,1)\nduring(20261103T2200/20261104T0600,fin("restart"))', ['ok', 'ok'], True),
 ('mixed interval', 'msg(Ana,Ben,1)\nduring(2026-11-03T22:00/20261104T0600,fin("restart"))', ['ok', 'ok'], True),
 ('compact month 13', 'msg(Ana,Ben,1)\nat(20261306T1700,fin("backup"))', ['ok', 'E-TIME'], True),
 ('compact day 31 of November', 'msg(Ana,Ben,1)\nat(20261131T1700,fin("backup"))', ['ok', 'E-TIME'], True),
 ('compact hour 25', 'msg(Ana,Ben,1)\nat(20261106T2500,fin("backup"))', ['ok', 'E-TIME'], True),
 ('compact minute 61', 'msg(Ana,Ben,1)\nat(20261106T1761,fin("backup"))', ['ok', 'E-TIME'], True),
 ('compact interval reversed', 'msg(Ana,Ben,1)\nduring(20261104T0600/20261103T2200,fin("restart"))', ['ok', 'E-TIME'], True),
 ('compact header time', 'msg(Ana,Ben,1,20261104T0903)\nis("server","up")', ['ok', 'ok'], True),
 ('date alone in basic form is a number', 'msg(Ana,Ben,1)\nat(20261106,fin("backup"))', ['ok', 'E-KIND'], True),
 ('number with eight digits still a number', 'msg(Ana,Ben,1)\neq(cnt("rows"),12345678)', ['ok', 'ok'], True),
 ('compact time in a quote', 'msg(Ana,Ben,1)\npls(Ben,"restart at {20261106T1700}")', ['ok', 'ok'], True),
 ('compact time without minutes is not a time', 'msg(Ana,Ben,1)\nat(20261106T17,fin("backup"))', ['ok', 'E-SYN'], True),
 ('ack with a bare number (1.5.5)', 'msg(Gds,Dex,2,re(Dex1))\nack(Dex1)\nack(2)', ['ok', 'ok', 'E-KIND'], True),
 ('{a1} that this message did not define (3.8)', 'msg(Gds,Dex,2,re(Dex1))\nwill("review {a1}")', ['ok', 'E-NAME'], True),
 ('{a1} that this message defined', 'msg(Gds,Dex,2,re(Dex1))\ndef(a1,code("bash","make"))\nwill("review {a1}")', ['ok', 'ok', 'ok'], True),
 ('formula claims in a message', "msg(Ana,Ben,1)\n'x^2-5*x+6=0'\nent(Ana1.1,'(x-2)*(x-3)=0',\"factor\")\nassume('x>0 & x<10')", ['ok', 'ok', 'ok', 'ok'], True),
 ('a number formula is not a line', "msg(Ana,Ben,1)\n'2^10-1'", ['ok', 'E-KIND'], True),
 ('a formula with a bad connective', "msg(Ana,Ben,1)\n'x>0 and x<5'", ['ok', 'E-MATH'], True),
 ('relative number still works beside formulas', "msg(Ben,Ana,2,re(Ana1))\nagree(2)\nent(Ana1.2,'x=1')", ['ok', 'ok', 'ok'], True)]

# conversations: name, messages, pieces of the problems expected across messages
CASES_CONVERSATIONS = [('sound', ['msg(Ana,Ben,1)\nyn(is("server","up"))\nis("disk","full")', 'msg(Ben,Ana,1,re(Ana1))\nans(1,yes)\nagree(2)'], []),
 ('a line number past the end', ['msg(Ana,Ben,1)\nyn(is("server","up"))', 'msg(Ben,Ana,1,re(Ana1))\nagree(3)'], ['Ana1 has no line 3']),
 ('ans to a claim',
  ['msg(Ana,Ben,1)\nis("disk","full")', 'msg(Ben,Ana,1,re(Ana1))\nans(1,yes)'],
  ['answers a line that is not a question']),
 ('ans to a question sent with to(...)',
  ['msg(Ana,Ben,Cy,1)\nto(Ben,yn(is("cache","enabled")))', 'msg(Ben,Ana,Cy,1,re(Ana1))\nans(1,yes)'],
  []),
 ('ans to a request',
  ['msg(Ana,Ben,1)\npls(Ben,"restart service")', 'msg(Ben,Ana,1,re(Ana1))\nans(1,yes)'],
  ['answers a line that is not a question']),
 ('a label of another message that exists',
  ['msg(Ana,Ben,1)\ndef(a1,code("bash","make"))\npls(Ben,"review {a1}")', 'msg(Ben,Ana,1,re(Ana1))\nwill("review {Ana1.a1}")'],
  []),
 ('a label that the other message does not define',
  ['msg(Ana,Ben,1)\ndef(a1,code("bash","make"))\npls(Ben,"review {a1}")', 'msg(Ben,Ana,1,re(Ana1))\nwill("review {Ana1.a2}")'],
  ['Ana1 defines no label a2']),
 ('a label of a message that is not there',
  ['msg(Ana,Ben,1)\ndef(a1,code("bash","make"))\npls(Ben,"review {a1}")', 'msg(Ben,Ana,1,re(Ana1))\nwill("review {Dex7.a1}")'],
  ['Dex7.a1 names a message that is not earlier']),
 ('a label as a place, not in a quote',
  ['msg(Ana,Ben,1)\ndef(a1,code("bash","make"))\npls(Ben,"review {a1}")', 'msg(Ben,Ana,1,re(Ana1))\nis(Ana1.a1,"slow")'],
  []),
 ('braces inside code are raw text, not references', ['msg(Ana,Ben,1)\nwill(code("python","print(f""{Ben9.a1}"")"))'], []),
 ('serial out of order', ['msg(Ana,Ben,2)\nis("a","b")'], ['Ana has serial 2, expected 1']),
 ('re names a message that is not earlier', ['msg(Ana,Ben,1,re(Ben1))\nis("a","b")'], ['Ben1, which is not an earlier message']),
 ('a writer who is not on the roster',
  ['msg(Ana,Ben,1)\nis("a","b")', 'msg(Cy,Ana,1)\nis("c","d")'],
  ['Cy writes but is not on the roster']),
 ('a line reference inside ent that exists (own message and an earlier one)',
  ["msg(Ana,Ben,1)\n'x=1'\n'y=2'", "msg(Ben,Ana,1,re(Ana1))\n'z=3'\nent(grp(Ana1.1,Ana1.2,Ben1.1),'w=4')\nent(Ben1.1,'v=5')"],
  []),
 ('a line reference inside ent past the end of an earlier message',
  ["msg(Ana,Ben,1)\n'x=1'", "msg(Ben,Ana,1,re(Ana1))\nent(Ana1.3,'z=3')"],
  ['Ana1 has no line 3']),
 ('a line reference inside grp to the sender\'s own message past its end',
  ["msg(Ana,Ben,1)\n'x=1'\nent(grp(Ana1.1,Ana1.5),'y=2')"],
  ['Ana1 has no line 5']),
 ('line 0 does not exist',
  ["msg(Ana,Ben,1)\n'x=1'\nent(Ana1.0,'y=2')"],
  ['Ana1 has no line 0']),
 ('the header is not a line',
  ["msg(Ana,Ben,1)\n'x=1'\nent(Ana1.3,'y=2')"],
  ['the header is not a line']),
 ('a reference to a message that is not earlier, in a root that has no reference place',
  ["msg(Ana,Ben,1)\nent(Ben1.1,'y=2')"],
  ['Ben1.1 names a message that is not earlier']),
 ('a bare message name that is not earlier',
  ["msg(Ana,Ben,1)\nent(grp(Ben2),'y=2')"],
  ['Ben2 names a message that is not earlier']),
 ('a reference in braces inside a quote is checked as a label (1.5.4), not as a line',
  ["msg(Ana,Ben,1)\npls(Ben,\"look at {Ana1.o1}\")"],
  [])]


if __name__ == '__main__':
    try:
        sys.exit(main())
    except BrokenPipeError:                      # for example:  python3 silex_check.py --roots | head
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
        sys.exit(0)
