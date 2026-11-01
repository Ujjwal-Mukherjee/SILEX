# SILEX-195 | SPECIFICATION | DRAFT r1 | NOT ADOPTED | NOT FROZEN

**The 195-root language in one file: grammar, lexicon with its language gaps, and the open points.**

| Item | Value |
| --- | --- |
| Name | SILEX-195 SPEC DRAFT r1 |
| Date | 2026-11-01 |
| Compiled by | C (Claude), at the Owner's request: lexicon with its gaps, and grammar, in one place (1 Nov, 11:38) |
| Built from | `SILEX-GRAMMAR-C-r3` (SHA-256 `723229b3…`), `SILEX-RULEBOOK-r3` (`0573a32c…`), the language gaps recorded by Test 2 and by the first reader of grammar r3 (its section 14), and the nine candidate words of Cb2 (OPEN BUILD) |
| Status | **DRAFT. Not adopted, not frozen, no checksum record.** It adds no root, renames none and changes no rule. The rule text of Part 1 is that of grammar r3. Test 2 was run on grammar r3; Test 1 was run on the earlier r1 (Part 5.2). What differs from r3 is listed in Part 5.4. Only the Owner decides what is adopted, frozen or added. |
| Checker | `ucl_check.py` (release g3) and `silex_check_g3.py` (Part 5.5). Every line of SILEX printed in Part 1 carries the checker's verdict after `# ` and was run on it. |
| Language of the file | English, for the AI participants. Relay notes to the Owner are sent separately, in Bengali. |

## How to read this file

1. **This file is your only source.** If your memory disagrees with it, follow the file and say so.
2. **One notation only.** If you have seen SILEX written in another way (the earlier word-token form, the Greek role markers, the 183-entry line), do not mix it in. If you notice yourself reaching for it, mark the point `a?` and carry on.
3. **Do not guess.** A line outside the rules, a parked root, a root without a signature, or an incomplete claim is marked `a?` and left (1.11). A reading marked † is a guess, given as such.
4. **A gap is not a failure.** If a sentence cannot be said with the roots at hand, say what you tried and mark the point. Part 3 records such gaps.
5. **English lives only inside `⌜ ⌝`**, as a scaffold, and is never part of the language.
6. **A pass of the checker shows form, not shared meaning** (1.11). Only blind readers can show that.
7. **Do not add or adopt.** You may propose a word through the entry steps in 3.2. Adoption is the Owner's alone; agreement among AIs is not adoption.

**Tags.** A rule with no tag restates what checker g3 does (grammar r3 says the same). That is not a ruling: only the rulings of 5.1 are the Owner's, and some untagged rules rest on proposals the Owner has not ruled on one by one. **[CANDIDATE]** marks a rule where the checker was changed by a choice put to the Owner as open (Part 4). **†** marks a reading that the table's gloss does not fix. **E, Ep, P, U, X** are the evidence tiers of 1.10.

**Contents.** Part 1 Grammar · Part 2 Lexicon, 195 roots in 25 families, each family followed by its gaps · Part 3 Language gaps, and how a new word enters · Part 4 Open grammar points · Part 5 Rulings, evidence and record.

---

# PART 1. GRAMMAR

The rules, in order: tokens, kinds, application, details, joiners and binders, names, `n0`, time and number, lines and force, evidence. Rule IDs (T, K, A, D, J, V, N, Z, M, the E-codes) are those of grammar r3.

## 1.1 The language on one screen

SILEX is written as nested applications of roots. Every expression has one shape:

```
expression  =  root ( expression , expression , … )
            |  name  |  atom  |  n0    |  ⌜ mention ⌝  |  ✠( math )  |  agent : expression
line        =  one expression, of a kind that can stand as a line (1.9)
```

Seven laws carry the rest.

1. **One shape.** There is no infix, no precedence, no punctuation but `( ) , :` and the two mention brackets. A root is followed at once by `(`; the six atoms stand bare.
2. **Places have kinds.** A root lists its places in order and the kind each one wants. A name of that kind fills the place; so does any root that makes that kind (1.3).
3. **Details follow the core.** After its core places a root may take role markers, optional, unordered, each at most once, eight arguments in all; a role not given may be written `n0` (1.5).
4. **Content is not force.** A claim is not asserted by being written. Only a force root or a dialogue act turns a claim into a line (1.9).
5. **Names are opaque.** A name means its class and nothing else. English occurs only inside `⌜ ⌝`, as a scaffold, and is never part of the language (1.2).
6. **Not supplied is not none.** `n0` marks a place or a role that was not supplied. It is not zero, not none, not unknown, and it is not a claim about a data field (1.7). The word `null` is no longer read.
7. **A pass is form.** The checker certifies form, kinds and evidence level (1.10). Whether two readers agree on meaning is a separate, empirical question (1.11).

A whole message, read in English beside it:

```silex
m▤(zUa1,zkA)                          # ok
d≔(zo9,⌜the signed contract file⌝)    # ok SCAFFOLD
d≔(zcr1,⌜the published checksum⌝)     # ok SCAFFOLD
d≔(zq1,v⊨(zo9,zcr1))                  # ok
h◇(zq1)                               # ok
```

*Message zUa1 from zkA. Let zo9 stand for “the signed contract file”, zcr1 for “the published checksum”, and zq1 for “zo9 satisfies zcr1”. As a hypothesis: zq1.* Nothing is asserted, no English is part of the language, and each name carries only its class.

## 1.2 Tokens

| # | Rule |
| --- | --- |
| **T1** | A line is one expression. Spaces and tabs may surround any argument; a root and its `(` are written together. In a file, a `#` standing alone between spaces, or at the start of a line, opens a comment to the end of the line; the root `#` is always followed by `(`. |
| **T2** | **Roots.** The 195 symbols of the table. The reader takes the longest root that matches (`s@*` before `s@`). A root with places is followed at once by `(`. The atoms are `t 0 ⊤ x w n`; they take no `(`. |
| **T3** | **Names.** `z`, a class prefix, then letters and digits. The prefix is the class and the whole meaning (table below). A name is never applied: no `(` follows it. Names are opaque and need not be declared, except a time name (N5). |
| **T4** | **`n0`.** The two characters `n0`, when no letter, digit or `(` follows them. The word `null` is not read (E-SYNTAX). |
| **T5** | **Mention.** `⌜ … ⌝`, nestable. If the inside is SILEX it is read as SILEX, otherwise as raw English. A mention remembers what it mentions (1.3). |
| **T6** | **Math term.** `✠(` … `)`. The inside is the math sublanguage of 1.8. |
| **T7** | **Attribution.** An agent name, a colon, then an expression: `zkB:∈(zo1,zS1)` is a claim attributed to `zkB`; before a force root (1.9) it gives a line attributed to `zkB`. Only `zk` names may precede the colon. |
| **T8** | A token that is none of these is E-LEX. A name without a class prefix is E-LEX. |

**Name classes.**

| Prefix | Kind | Prefix | Kind |
| --- | --- | --- | --- |
| `zk` | agent (`Ag`) | `zS` | collection (`Co`) |
| `zo` | object, an item (`Ob`) | `zE` | math term (`Ex`) |
| `zv` | value (`Va`) | `zt` | time (`Tm`) |
| `zm` | method or act name (`Me`) | `zU` | message name (`Ms`) |
| `zcr` | criterion (`Cr`) | `zp zq zr zh` | claim (`P`) |

A variable is not a separate class: it is a name of class `zk zm zo zv zS` that a binder binds (1.6).

```silex
g←(zkB:∈(zo1,zS1))        # ok
zkB:g←(∈(zo1,zS1))        # ok
g←( zq1 )                 # ok
g← (zq1)                  # E-SYNTAX
g←(zx1)                   # E-LEX
```

## 1.3 Kinds

Every expression has a kind. Kinds form a small lattice; a place accepts its own kind and every subkind.

```
Ref (an item: anything referred to)
 ├─ Ag  agent            zk
 ├─ Ob  object           zo
 ├─ Va  value            zv        └─ Ct  count (made by #)
 ├─ Co  collection       zS        └─ Pm  premise set (made by b▁)
 ├─ Me  method           zm        (also an act name)
 ├─ Tm  time             zt
 ├─ Cr  criterion        zcr
 ├─ Ms  message name     zU
 ├─ Mn  mention          ⌜ ⌝       Mn[P]  Mn[Q]  Mn[Ln]  Mn[Act]
 └─ Var bound variable

P    claim               zp zq zr zh        content, not asserted
Act  act                 zm  and  ▶ cƒ o→ a+ …
Ex   math term           zE  and  ✠( )
Rm   role marker         ⌘ ⚙ ↣ ☞ ☼ ⚓ ♙
Ln   line                g←(P) …            a claim put to use
 ├─ Dir  directive       i!  r<              └─ CDir  conditional directive (i⇒)
 ├─ Req  requirement     r□
 ├─ Dc   declaration     d≔  m▤ (header)
 ├─ Q    question        ?= ?⊤ ?◷ ?@ ?⊙ ?∵
 └─ Cx   assumption      ~
```

In the readings of Part 2, “item” means `Ref`.

| # | Rule |
| --- | --- |
| **K1** | A place of kind `K` accepts an expression of kind `K` or any subkind. A place written `K\|L` accepts either. A place of kind `Any` accepts every kind except a role marker **[CANDIDATE, see D6]**. |
| **K2** | `n0` fits every place (1.7). |
| **K3** | A root with several signatures (`m▤ r> h◇ p◇ u? u~ c■ d↦ v✓ i⇒ c⊃ r□ ~ m> r@ ∃`) is read by the place it stands in: the first signature whose result fits the kind expected there. At the top of a line, the first that checks. |
| **K4** | **Lifting.** Where a claim is expected and an act stands, the act is read as the claim *an act of this kind occurs*. It is not asserted. Its evidence level is E for `cƒ o→ a+` and N for every other act. |
| **K5** | A mention has the kind of what it mentions when that is a question, a line, a claim or an act (`Mn[Q]`, `Mn[Ln]`, `Mn[P]`, `Mn[Act]`), and plain `Mn` otherwise. |

```silex
g←(▶(zm1))                # ok
?⊤(c■(▶(zm1)))            # ok
d↦(zv1,zo1)               # E-LINE
g←(d↦(zv1,zo1))           # ok
```

*The first line lifts the act `▶(zm1)` to the claim that it is triggered; the second asks whether the completion of that run holds. The third stands alone on a line, where K3 takes the first signature that checks, the act `d↦` (Part 2 lists the act first): an act alone is not a line. Under a force root the claim shape fits, as in the fourth.*

## 1.4 Application

| # | Rule |
| --- | --- |
| **A1** | `r(e₁,…,eₙ)` applies root `r` to `n` arguments. `n` must equal the number of core places in the chosen signature (E-ARITY), except where 1.5 and 1.6 say otherwise. |
| **A2** | Argument `eᵢ` must fit place `i` (E-CAT). |
| **A3** | The application has the result kind of its signature. |
| **A4** | An atom takes no arguments. A root that needs arguments cannot be written bare. |
| **A5** | The six roots `c⇒ ∴ y⋯ g◎ ? a>` have no signature. They are read as tokens and refused (E-UNSIG): they are not applied. |
| **A6** | A root that is not in the table is E-LEX. |

A derivation, kinds at the right. The act is lifted to a claim by K4:

```text
g←(c⊃(zt1,t≺(▶(zm1))))                          Ln   supplied:
└ c⊃(zt1, …)                                    P    within the time zt1,
  ├ zt1                                         Tm   a declared time
  └ t≺(…)                                       P    before the reference time,
    └ ▶(zm1)                                    Act → P   the run of zm1 is triggered
      └ zm1                                     Me
```

Signatures are in Part 2. Roots that share a shape cannot be told apart by form: there only the gloss decides, and a reader takes a root as written and never reads a neighbour into it.

```silex
g←(v⊨(zo1,zcr1))          # ok
g←(v⊨(zo1))               # E-ARITY
g←(v⊨(zo1,zS1))           # E-CAT
```

## 1.5 Details

A root may take role markers after its core places. The seven markers each take exactly one name:

| Marker | Role | Marker | Role |
| --- | --- | --- | --- |
| `♙` | agent: who does it | `↣` | recipient |
| `⌘` | method: by which procedure | `☞` | destination |
| `⚙` | instrument: using which tool | `☼` | source |
| `⚓` | basis: on what ground | | |

| # | Rule |
| --- | --- |
| **D1** | After the core places, further arguments are role markers: details. Details are optional and unordered. An omitted role is unspecified, not absent. |
| **D2** | Each marker at most once in one application (E-ROLE). |
| **D3** | A marker must be given the kind it asks for (E-CAT): `♙` an agent, `⌘` a method, `⚓` a claim or an item, the others an item. |
| **D4** | Core places and details together are at most **eight** (E-ARITY). |
| **D5** | A detail is a role marker or `n0`. After the core places `n0` stands for a role that was not given (the placeholder is the Owner's ruling, 1 Nov 01:57; what follows is checker behaviour). It counts toward the eight, means the same as leaving the role out, and prints no warning. In an action root, where the roles belong to the signature, and inside a marker (`⚓(n0)`), it prints NU. |
| **D6** | **[CANDIDATE]** A role marker stands only as a detail or, in the three action roots, as a role. It never fills a core place. |
| **D7** | **[CANDIDATE]** The protocol roots `m▤` and `r>` take no details. |
| **D8** | These take no details: the joiners `∧ a\| s≺`, the binders `∃ ?= ?⊙`, `r@`, `d≔`, `⌜ ⌝`, `✠`, the atoms, the seven markers, and the protocol roots of D7. |
| **D9** | **Action roots.** `cƒ o→ a+` take one object (an item or a math term) and then role markers only, up to seven. They are the only roots whose details are part of the signature. |
| **D10** | Form does not decide whether a marker suits its root (a recipient on a sameness claim). Such a line is well formed; a reader marks it `a?`. |

```silex
i!(cƒ(zo1,♙(zkA),⌘(zm1)))                       # ok
g←(v⊨(zo1,zcr1,⚓(zq3)))                         # ok
g←(v⊨(zo1,zcr1,⚓(zq3),⚓(zq4)))                  # E-ROLE
g←(v⊨(zo1,zcr1,♙(zS1)))                         # E-CAT
g←(v⊨(zo1,zcr1,♙(zkA),⌘(zm1),⚙(zo2),↣(zo3),☞(zo4),☼(zo5)))                # ok
g←(v⊨(zo1,zcr1,♙(zkA),⌘(zm1),⚙(zo2),↣(zo3),☞(zo4),☼(zo5),⚓(zq3)))        # E-ARITY
a?(♙(zkA))                                      # E-ARITY
```

*The last line is D6: a bare role marker is not "anything", so `a?` has no core argument.*

## 1.6 Roots with their own form

### 1.6.1 Joiners `∧  a|  s≺`

| # | Rule |
| --- | --- |
| **J1** | Two or more operands, no details. Three or more are read as right-nested binary joins. |
| **J2** | All operands are of one kind. `∧`: all claims or all acts. `a\|`: all claims (inclusive "or") or all items (a list of candidates). `s≺`: all claims, all acts or all items (an order). Mixed kinds are E-MIX. |
| **J3** | `n0` is not an operand (E-NULL). |
| **J4** | The result has the operands' kind; `a\|` over items gives a collection of candidates and `s≺` over items gives a claim. |

```silex
g←(∧(v⊨(zo1,zcr1),c↝(zq1,zq2)))                 # ok
r<(zkB,s≺(▶(zm1),▶(zm2),▶(zm3)))                # ok
g←(∧(zq1,zo1))                                  # E-MIX
g←(∧(zq1,n0))                                   # E-NULL
```

### 1.6.2 Binders `∃  ?=  ?⊙`

| # | Rule |
| --- | --- |
| **V1** | `∃(v,φ)`: some `v` satisfies the claim `φ`. `?=(v,φ)`: which `v` satisfies `φ`? `?⊙(v,S,φ)`: which `v` of the collection `S` satisfies `φ`? The bare form `∃(x)` says that the item `x` exists in a stated domain. |
| **V2** | `v` is a name of class `zk zm zo zv zS` (E-BIND). It was not declared by `d≔` and is not already bound: no shadowing (E-BIND). |
| **V3** | A question holds one binder and no other question (E-BIND). Its variable occurs in the body (E-BIND) and is not reused by another question in the same message (E-BIND). |
| **V4** | A negated existence needs an explicit domain: `n¬(∃(v,φ))` requires a conjunct `∈(v,S)` in `φ` (E-DOMAIN). |

```silex
g←(∃(zox,∧(∈(zox,zS1),v⊨(zox,zcr1))))                  # ok
?=(zox,∧(∈(zox,zS1),v⊨(zox,zcr1)))                     # ok
?⊙(zoy,zS1,v⊨(zoy,zcr1))                               # ok
?=(zox,∈(zox,zS1))                                     # E-BIND
?=(zoz,v⊨(zo1,zcr1))                                   # E-BIND
g←(n¬(∃(zox,v⊨(zox,zcr1))))                            # E-DOMAIN
```

*The block counts as one message. `?=(zox,∈(zox,zS1))` is E-BIND only because the first `?=(zox,…)` of the block already used `zox` (V3: a variable is not reused by another question in the same message); alone, with a fresh variable, it would pass. `?=(zoz,v⊨(zo1,zcr1))` is E-BIND because `zoz` does not occur in its body (V3).*

### 1.6.3 Reference `r@`

`r@` has two uses, told apart by the kind of its second argument. `r@(x,y)`, with `y` an item, is a pointer from `x` to `y` (a claim; not provenance, which is `s@`). `r@(x,zUk)`, with `zUk` a message name, is the qualified reference *x as it stands in message zUk*; it has the kind of `x`, and `x` may be a claim or an item. `r@` takes no details.

```silex
g←(c↝(r@(zq1,zUa1),zq2))                        # ok
```

### 1.6.4 Names and declarations `d≔`

| # | Rule |
| --- | --- |
| **N1** | `d≔(n₁,…,nₖ,def₁,…,defₖ)` declares `k` names and then gives their `k` definitions in the same order. An odd number of arguments is E-ARITY. A definition may use a name declared earlier in the same line. |
| **N2** | The first half are names (E-DEF). A name already declared in the message is E-REDECL, whether it was declared by an earlier line or earlier in the same line. |
| **N3** | The class decides what may be defined: `zp zq zr zh` a claim; `zm` an act or method; `zo` an item; `zv` a value; `zS` a collection; `zk` an agent; `zcr` a criterion; `zE` a `✠` term or another `zE` name; `zt` only the atom `t` or an imported qualified time. A `zU` name is declared only by the header (E-DEF). |
| **N4** | A definition that is quoted English is a scaffold (warning SCAFFOLD): it fixes nothing in SILEX and gives the reader English to go on. A scaffold may define a name of any class except `zt`, `zE` and `zU`. |
| **N5** | A name that is used but not declared means only its class. This is allowed for every class except `zt`: a time name must be declared first (E-UNDECL). |
| **N6** | Names are local to their message, with one exception, the roster names: a `zk` name that is the sender in a header means that participant in every message. So `zkA` in `m▤(zUa1,zkA)` is the same agent in every message of the session. |

```silex
d≔(zo1,zo2,⌜the first file⌝,⌜the second file⌝)       # ok SCAFFOLD
d≔(zo1,⌜again⌝)                                       # E-REDECL
d≔(zt1,t)                                             # ok
d≔(zo3,zo4,⌜x⌝)                                       # E-ARITY
d≔(zo8,zo8,⌜a⌝,⌜b⌝)                                    # E-REDECL
d≔(zo5,zo6,⌜a⌝,zo5)                                    # ok SCAFFOLD
d≔(zq5,⌜the build passes⌝)                             # ok SCAFFOLD
d≔(zt2,⌜noon⌝)                                         # E-DEF
d≔(zE2,⌜seven⌝)                                        # E-DEF
d≔(zUa1,⌜a message⌝)                                   # E-DEF
g←(c⊃(zt9,t≺(▶(zm1))))                                # E-UNDECL
```

## 1.7 `n0`

| # | Rule |
| --- | --- |
| **Z1** | `n0` means *not supplied*. It is not none, not zero, not unknown. |
| **Z2** | It fits any **core** place and prints the warning NU. A claim with `n0` in a core place is incomplete: a reader marks it `a?` when it stands under `n¬`, `i→` or `?⊤`. After the core places it is a detail not given (D5). |
| **Z3** | `n0` is not a joiner operand (E-NULL), not a line (E-LINE), not the name in `d≔` (E-DEF), not a bound variable (E-BIND). |
| **Z4** | `n0` is an atom of the table (family F2.5, status E): no arguments, no kind of its own. It replaces the word `null` (Owner ruling, 1 Nov 07:29), which is not read any more (E-SYNTAX). `n0(zo1)` is E-ARITY. The table's former `n0(P,Q)`, *the field P has no value in Q*, is withdrawn from the glyph (gap G-14, Part 3). |

```silex
g←(i→(zq1,n0))                    # ok NU
g←(v⊨(zo1,zcr1,n0))               # ok
g←(c■(zm1,n0))                    # ok
i!(cƒ(zo1,♙(zkA),n0))             # ok NU
g←(s=(zo1,zo2,⚓(n0),⚓(zq1)))      # E-ROLE
n0                                # E-LINE
g←(i→(zq1,n0(zo1,zo2)))           # E-ARITY
g←(i→(zq1,null))                  # E-SYNTAX
```

## 1.8 Time, criteria, number

### 1.8.1 Time

| # | Rule |
| --- | --- |
| **M1** | A reference time is a declared time name: `d≔(zt1,t)`. |
| **M2** | `c⊃(zt,φ)` considers the claim `φ` within the time `zt`; it is the only source of a reference time. `t≺ t● t▷` say that a claim holds before, at or after the reference time of the nearest enclosing `c⊃`. A tense with no enclosing `c⊃` warns RT: unresolved. |
| **M3** | A tense over a negation needs a state predicate under the negation (E-KIND): `h⊡` (established), or `⊡ v⊨ ∈ s= k✓ i≡` (new). For events put the negation outside: `n¬(t≺(▶(zm1)))`. |
| **M4** | `c⊃(ctx,φ)` takes an assumption `~(P)`, a time name, or a criterion as its context. |

```silex
d≔(zt1,t)                                       # ok
g←(c⊃(zt1,t≺(▶(zm1))))                          # ok
g←(t≺(▶(zm1)))                                  # ok RT
g←(c⊃(zt1,t≺(n¬(▶(zm1)))))                      # E-KIND
g←(c⊃(zt1,n¬(t≺(▶(zm1)))))                      # ok
```

### 1.8.2 Criteria

A criterion is a declared `zcr` name. Sameness roots `s= s≈ m≡ d≢` are relative to one; with none in context they warn CR (underspecified). A criterion is supplied by `c⊃(zcr,φ)`.

```silex
g←(c⊃(zcr1,s=(zo1,zo2)))                        # ok
g←(s=(zo1,zo2))                                 # ok CR
```

### 1.8.3 Number

Numbers live only in `✠( )`, as counts `#(S)`, or as `zv` names. `✠` is a term and stands only in a closed list of places: the object of `cƒ`, an argument of `r→` or `m>`, the definiens of a `zE` name (E-MATHPLACE). Inside the brackets:

```
term   =  numeral | letter | π | head ( term , … )
head   =  + − × ÷ ^       (two terms)       √ sin cos ln   (one term)
          ∫ Σ            (four)             lim            (three)
numeral = 0 | [1-9][0-9]*        letter = a single lowercase letter
```

The head's arity is fixed (E-MATH); a binder (`∫ Σ lim`) binds a letter. The value claims `r→` and `m>` are atemporal (E-ATEMP under a tense or a time context; this includes `m>` on counts, `m>(#(zS1),#(zS2))`), take no attribution (E-ATTR), take no free letter (E-FREE) and no undefined value such as a division by zero (E-UNDEFVAL).

```silex
d≔(zE1,✠(×(7,6)))                               # ok
?⊤(r→(zE1,✠(42)))                               # ok
g←(r→(✠(÷(1,0)),✠(0)))                          # E-UNDEFVAL
g←(zkB:r→(✠(×(7,6)),✠(42)))                     # E-ATTR
g←(✠(42))                                       # E-MATHPLACE
```

```silex
d≔(zt6,t)                                       # ok
g←(c⊃(zt6,m>(#(zS1),#(zS2))))                   # E-ATEMP
```

## 1.9 Lines, force, dialogue

**1.9.1 A line.** A line is an expression of kind Ln, Dir, CDir, Req, Dc, Q or Cx. A bare claim is accepted as a line with the warning FU (force unspecified): write the force. Any other kind is E-LINE. This includes a root that has an act shape and a claim shape with the act listed first (`c■ d↦ v✓`, Part 2): alone on a line it is read as its act (K3), so it is E-LINE. Put it under a force root (`g←(c■(zm3))`) or a directive (`i!(c■(zm3))`).

```silex
g←(∈(zo1,zS1))                                  # ok
∈(zo1,zS1)                                      # ok FU
▶(zm1)                                          # E-LINE
i!(▶(zm1))                                      # ok
i⇒(zq1,i!(▶(zm1)))                              # ok
r□(n¬(zq1))                                     # ok
```

**Order and assumptions.** Line order has no meaning of its own. The grammar uses it for two things only: the header comes first (1.9.2) and a name is declared before it is used where N1 and N5 ask. "Then" between acts is written with `s≺` (J2), not with the order of lines. A line `~(P)` is a line of kind Cx; the checker keeps no scope for it and later lines are checked as if it were absent. To tie an assumption to a claim, give it as the context: `c⊃(~(P),Q)` (M4).

```silex
g←(s≺(▶(zm1),▶(zm2)))                           # ok
~(zq1)                                          # ok
g←(c⊃(~(zq1),zq2))                              # ok
```

**1.9.2 Message.** A message is a header `m▤(zUk,zkX)` followed by lines. The header is the first line and occurs once (E-HEADER). Separator lines such as `=== zUa1 zkA ===` belong to the session file, not to the language. The header names the sender only. An addressee is named inside a line: `r<(zkB,…)` asks `zkB`, and `↣` marks a recipient (1.5). `m▤` with three arguments, `m▤(zkP,zkQ,zoR)`, is not a header but a claim, *the message R from P to Q*; it is an ordinary line (FU when bare), and a header written after it is E-HEADER.

```silex
m▤(zkA,zkB,zo1)                                 # ok FU
m▤(zUa1,zkA)                                    # E-HEADER
```

**1.9.3 Force.** A claim is put to use by one of five force roots; none verifies:

| Root | Line reading | | Root | Line reading |
| --- | --- | --- | --- | --- |
| `g←` | supplied | | `u?` | not known |
| `h◇` | as a hypothesis | | `u~` | not established |
| `p◇` | admissible | | | |

`h◇ p◇ u? u~` have also a content reading as a claim (*it is hypothesized that P*). It is established in three places (`h◇` first in `i→`, `h◇` in `p↗`, `p◇` in `n¬`) and new elsewhere. An attributed claim can be supplied, `g←(zkB:P)`: I supply that `zkB` holds `P`. An attributed line, `zkB:g←(P)`, is a line of `zkB`. So:

| You mean | Write |
| --- | --- |
| B said P (B's own line) | `zkB:g←(P)` |
| I supply that B holds P | `g←(zkB:P)` |
| P comes from B (provenance, not speech) | `s@` |

**1.9.4 Dialogue acts.**

| Root | Reading | Root | Reading |
| --- | --- | --- | --- |
| `a.` | received (not agreed) | `e✗` | error in |
| `a=` | agreed (a claim or a declaration) | `r↻` | revised |
| `a?` | unclear | `p▁` | taken as a starting point |
| `p↗` | proposed, not adopted | `~` | assume |

**1.9.5 Directives and requirements.** `i!(act)` do it; `r<(zkB,act)` ask `zkB` to do it; `r□(P)` it is required that `P`. A conditional request is `i⇒(P,i!(act))`, and the act of `i⇒` may be a request: `i⇒(P,r<(zkB,act))`. A named method is itself an act, so `zm1` and `▶(zm1)` both fill an act place; this file writes `▶(zm1)` where the running of the method is meant.

```silex
r<(zkB,zm1)                                     # ok
i!(▶(zm1))                                      # ok
i⇒(zq1,r<(zkB,▶(zm2)))                          # ok
```

**1.9.6 Questions and answers.** `?⊤(P)` is answered in exactly one of three ways, `g←(P)`, `g←(n¬(P))`, `u?(P)`. `?=` and `?⊙` ask for a value. There is one answer per question, and a question with no target is marked `a?`. An answer is given by the answer link `r>(zUk,⌜Q⌝,W)`: it answers question `Q` of message `zUk`, and `W` is exactly `g←(A)` or `u?(A)` (E-FORCE). Names are local to their message (N6), so the answering message does not share names with the question's message. Inside an answer, `zq1` is the answerer's own name; the claim as it stands in the question's message is written `r@(zq1,zUk)`. Both forms pass the form check. Use `r@` when the answer must be about the question's own claim.

```silex
m▤(zUb1,zkB)                                                         # ok
d≔(zq1,v⊨(zo9,zcr1))                                                 # ok
r>(zUa1,⌜?⊤(zq1)⌝,g←(n¬(r@(zq1,zUa1))))                              # ok
r>(zUa1,⌜?⊤(zq1)⌝,a?(zq1))                                           # E-FORCE
r>(zUa1,⌜?⊤(zq1)⌝,u?(r@(zq1,zUa1)))                                  # ok
p↗(d≔(zh9,∧(c■(r@(zm1,zUa1)),n¬(r@(zq1,zUa1)))))                     # ok
a=(d≔(zh9,∧(c■(r@(zm1,zUa1)),n¬(r@(zq1,zUa1)))))                     # E-REDECL
```

*The last line is refused only because `zh9` was already declared in this message by the line above; in its own message it is the acceptance by restatement.*

```silex
m▤(zUa2,zkA)                                      # ok
d≔(zt1,t)                                         # ok
m▤(zUa3,zkA)                                      # E-HEADER
```

## 1.10 Evidence

Every root carries a **status**, and every expression the set of statuses of what it is built from.

| Status | Meaning | Roots |
| --- | --- | --- |
| **E** | established | 40 |
| **Ep** | established with open parts | 26 |
| **P** | proposed: a signature and a gloss, no test yet | 97 |
| **U** | parked: not applied | 31 |
| **N** | a new reading or a new design suggestion | (readings, not roots) |
| **X** | excluded | 1 |

The **level** of a line is the weakest status in it, ranked E > Ep > P > U > N > X. Two roots of status U, `m▤` and `r>`, are core by use: sessions use them as header and answer link.

**Tiers.** *Core*: status E or Ep (66 roots) with `m▤` and `r>`. *Trial*: status P (97). *Parked*: the other 29 roots of status U and the excluded `a>` (30 roots; `a>` and five of the others have no signature). A parked root is not applied: a reader who meets one answers `a?`. Core is 68 roots, trial 97, parked 30.

## 1.11 Reading, and what a pass shows

A root's **reading** is the English pattern in Part 2. A name is read as the English of its scaffold, or as its class when there is none. A pattern marked † is an inference from the gloss, not a reading the table gives; it is not to be relied on until it is ruled on. A reader who meets a line outside the rules, or one it cannot resolve, marks it `a?` and does not guess.

**Form and use are separate.** The form check applies the signature of every root that has one, whatever its status, so a line with a parked root that has a signature is well formed. Use is the reader's: a reader who meets a parked root, a root without a signature, or an incomplete claim (`n0` in a core place) marks `a?`. A † reading is a guess, not a refusal: the reader gives it and marks it †.

```silex
g←(s≈(zo1,zo2))                                 # ok CR
```

A pass certifies the checks of this grammar and nothing more: places, kinds, declared names, details, joiners, binders, time, number, evidence level. It does not show that the line says what its writer meant, nor that two readers recover the same meaning. That is shown only by blind reading, one line at a time, with the writer's intended meaning kept apart from the reader's recovered meaning.

## 1.12 Diagnostics

| Code | Rule | Meaning |
| --- | --- | --- |
| E-SYNTAX | T1–T7 | unclosed bracket, missing `)`, stray text |
| E-LEX | T8, A6 | unknown token, root or class prefix |
| E-UNSIG | A5 | root with no signature |
| E-ARITY | A1, D4, N1 | wrong number of arguments, more than eight, odd `d≔` |
| E-CAT | A2, D3, K1 | an argument of the wrong kind |
| E-ROLE | D2, D9 | a marker twice; a non-marker among an action root's roles |
| E-MIX | J2 | joiner operands of different kinds |
| E-NULL | J3 | `n0` as a joiner operand |
| E-BIND | V2, V3, Z3 | a bad, repeated or unused variable |
| E-DOMAIN | V4 | negated existence without a domain |
| E-DEF · E-REDECL · E-UNDECL | N2, N3, N5 | a bad definition; a name declared twice; an undeclared time name |
| E-LINE | 1.9.1 | an expression that cannot be a line |
| E-HEADER | 1.9.2 | a header that is not first, or is repeated |
| E-FORCE | 1.9.6 | the third operand of `r>` is not `g←` or `u?` |
| E-KIND | M3 | a tense over a negation of a non-state predicate |
| E-ATTR | 1.8.3 | attribution before a value claim or comparison |
| E-ATEMP | 1.8.3 | a value claim under a tense or time context |
| E-MATH · E-MATHPLACE · E-FREE · E-UNDEFVAL | 1.8.3 | a bad math term; `✠` out of place; a free letter; an undefined value |
| NU · FU · RT · CR · SCAFFOLD | Z2 · 1.9.1 · M2 · 1.8.2 · N4 | warnings: n0 supplied; force unspecified; reference time missing; criterion missing; quoted English |

---

# PART 2. LEXICON WITH ITS GAPS

The 195 roots, in 25 families. Each family table is followed by the language gaps recorded for it; a new word enters at its gap, by the steps of 3.2. Family numbers are written with an F (F2.5), so that they are not taken for section numbers.

### 2.1 The 25 families

Every root belongs to one family. *Core* is status E or Ep, plus the header and the answer link; *trial* is status P; *parked* is held back (1.10). The tables of 2.2 give each root's shape and reading.

| Family | Roots | Core | Trial | Parked |
| --- | --- | --- | --- | --- |
| F0.1 Application, names and definition | 1 | `d≔` | — | — |
| F0.2 Mention and attribution | 1 | `⌜ ⌝` | — | — |
| F0.3 Atoms and placeholders | 6 | `t` `0` | — | `⊤` `x` `w` `n` |
| F1.1 Collections and selection | 10 | — | `g∪` `i+` `e−` `a/` `c↓` `s∃` `s⊙` `k▤` `b▁` | `f∃` |
| F1.2 Items, data and transformations | 12 | `⧉` | `d▤` `i▤` `f▦` `fƒ` `g↦` `i↦` `m↻` `o←` `s↦` `u↻` `e⚖` | — |
| F1.3 Methods, processes and tasks | 3 | — | `m▦` `p▷` `t▦` | — |
| F1.4 Quantity and mathematics | 4 | `✠` `#` | `c∑` `dΔ` | — |
| F2.1 Logical core: negation, joining, quantification, implication, context | 8 | `n¬` `∧` `a\|` `∃` `i→` `i⇒` `c⊃` | — | `c⇒` |
| F2.2 Reasons, support, inference and evidence | 12 | `s∵` `d⊢` | `∵` `r∵` `j∵` `e∵` `l⊢` | `c∴` `∴` `i⊢` `p⊢` `e▤` |
| F2.3 Causation, condition, constraint and necessity | 4 | `c↝` | `l⊣` `n□` | `c⊣` |
| F2.4 Sameness, difference, comparison and order | 16 | `s=` `i≡` `m>` | `r≡` `c≡` `c≠` `d≠` `b≻` `≈` `o≺` `v=` `m∥` `n−` | `s≈` `m≡` `d≢` |
| F2.5 Epistemic status, verification, probability and absence | 13 | `v⊨` `n0` | `f⊥` `✓` `✗` `r✓` `s✓` `p⇢` | `f⊤` `k✓` `u±` `l≥` `pℙ` |
| F2.6 Provenance and reference | 5 | `s@` `s@*` `r@` `⊛` | — | `r:` |
| F2.7 Time and sequence | 9 | `t≺` `t●` `t▷` `s≺` | `b₀` `s◷` `s▷` | `▷` `y⋯` |
| F2.8 Structure, description, classification and relation | 18 | `∈` `⊡` | `e∈` `o\|` `c◉` `d⋮` `p▦` `s▦` `s⊞` `m⊞` `m↦` `k#` `l↔` `↔` `r∩` `s≔` `p?` `i←` | — |
| F2.9 Agents: holding, attitude and interaction states | 15 | `h⊡` | `b~` `t~` `i◎` `o◎` `n!` `r−` `g▷` `f▷` `h+` `s◇` `f↩` `o▤` `u✓` | `g◎` |
| F3.1 Action constructors and role markers | 10 | `cƒ` `o→` `a+` `⌘` `⚙` `↣` `☞` `☼` `⚓` `♙` | — | — |
| F3.2 Act verbs | 11 | — | `c?` `c≶` `e⋯` `i?` `t⋯` `u↦` `l↻` `i↑` `t⚖` `a<` | `q<` |
| F3.3 Execution, completion, retry, decision and result | 8 | `▶` `c■` `⤿` `d↦` `v✓` `r→` | — | `d⊙` `c✓` |
| F3.4 Directives and requirements | 3 | `i!` `r<` `r□` | — | — |
| F4.1 Question formers | 7 | `?=` `?⊤` | `?◷` `?@` `?⊙` `?∵` | `?` |
| F4.2 Answer forms | 3 | — | `y✓` | `n⊘` `a>` |
| F5.1 Status force | 5 | `g←` `h◇` `p◇` `u?` `u~` | — | — |
| F5.2 Dialogue acts | 8 | `a.` `a=` `a?` `p↗` `e✗` `r↻` `~` | `p▁` | — |
| F6.1 Messages: identity, transmission and answer links | 3 | `m▤` `r>` | `r←` | — |

A signature is written `root : K₁, K₂, … → R`: the kinds of the core places in order, then the kind the root makes. `v⊨ : Ref, Cr → P` says that `v⊨` takes an item and a criterion and makes a claim. 2.2 prints the shapes in words.

### 2.2 The roots, by family

Tier: **E** established, **Ep** established with open parts, **P** proposed, **U** parked, **X** excluded, **use** core by use. Shape lists the core places in order, then what the root makes; `(+k)` is the number of details that fit after the core places, within the limit of eight. P, Q, R, … in the reading are the places in order. † marks a reading that the table's gloss does not fix.

**F0.1 Application, names and definition**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `d≔` | Ep | P1 … Pk names, then Q1 … Qk definitions (k ≥ 1) → declaration | let the names P stand for the definitions Q |

*No gap recorded for this family. That means nothing was recorded, not that nothing is missing.*

**F0.2 Mention and attribution**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `⌜ ⌝` | E | P any expression → mention | “P” |

*No gap recorded for this family. That means nothing was recorded, not that nothing is missing.*

**F0.3 Atoms and placeholders**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `t` | E | nothing (an atom) → item | a time |
| `0` | E | nothing (an atom) → value | zero |
| `⊤` | U | nothing (an atom) → claim | the true statement |
| `x` | U | nothing (an atom) → item | a placeholder |
| `w` | U | nothing (an atom) → item | a word |
| `n` | U | nothing (an atom) → item | something novel |

*No gap recorded for this family. That means nothing was recorded, not that nothing is missing.*

**F1.1 Collections and selection**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `g∪` | P | P item, Q item → collection (+6) | the collection of P and Q |
| `i+` | P | P collection, Q item → collection (+6) | P with Q added |
| `e−` | P | P collection, Q item → collection (+6) | P without Q |
| `a/` | P | P item, Q criterion → collection (+6) | P broken into its elements by Q |
| `c↓` | P | P collection, Q criterion → collection (+6) | P narrowed by Q † |
| `s∃` | P | P collection, Q criterion → collection (+6) | the entities sought in P under Q |
| `s⊙` | P | P collection, Q criterion → item (+6) | the item chosen from P under Q |
| `f∃` | U | P collection, Q criterion → claim (+6) | an entity of P that meets Q has been found |
| `k▤` | P | P agent → collection (+7) | the information that P holds as supported |
| `b▁` | P | P collection → premise set (+7) | P taken as the foundation set of premises |

*No gap recorded for this family. That means nothing was recorded, not that nothing is missing.*

**F1.2 Items, data and transformations**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `d▤` | P | P item, Q item → item (+6) | the structured content of P and Q † |
| `i▤` | P | P item → item (+7) | the information content of P |
| `f▦` | P | P item, Q item → item (+6) | P turned into the explicit structured form Q † |
| `fƒ` | P | P item, Q item → item (+6) | the function that maps P to Q † |
| `g↦` | P | P item, Q method → item (+6) | what the method Q makes from P |
| `i↦` | P | P item, Q criterion → item (+6) | the meaning of P under the interpretation Q |
| `m↻` | P | P item, Q item → item (+6) | P changed into Q † |
| `o←` | P | P item, Q item → item (+6) | P brought in from Q † |
| `s↦` | P | P item, Q method → item (+6) | the solution to P by the method Q † |
| `u↻` | P | P item, Q item → item (+6) | P updated with the information Q † |
| `e⚖` | P | P item, Q criterion → item (+6) | the judgment of P against Q |
| `⧉` | Ep | P item → same kind as its argument (+7) | a copy of P |

*No gap recorded for this family. That means nothing was recorded, not that nothing is missing.*

**F1.3 Methods, processes and tasks**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `m▦` | P | P claim, Q act → method (+6) | the procedure that does Q under the condition P † |
| `p▷` | P | P act → method (+7) | the process of P |
| `t▦` | P | P act, Q claim → method (+6) | the task P with the condition Q † |

*No gap recorded for this family. That means nothing was recorded, not that nothing is missing.*

**F1.4 Quantity and mathematics**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `✠` | Ep | P a math expression (numbers and + − × ÷ ^ √ and so on) → math term | the number P |
| `#` | Ep | P collection → count (+7) | the count of P |
| `c∑` | P | P collection, Q method → item (+6) | the total of P by the method Q |
| `dΔ` | P | P item, Q item, R criterion → item (+5) | the difference between P and Q under R |

| Gap | Kind | What cannot be said yet |
| --- | --- | --- |
| G-02 | cannot say | A number with a unit (percent, GB, seconds, “per hour”), as something that can be compared; “faster than” on a measured quantity. |
| G-03 | cannot say | A count compared with a number: “at least 3 tests failed”, “at most 5 attempts”. |

**F2.1 Logical core: negation, joining, quantification, implication, context**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `n¬` | E | P claim or requirement → claim (+7) | it is not the case that P |
| `∧` | Ep | P, Q, … (two or more, all claims or all acts) → claim, or act | {*} (all of these) |
| `a\|` | Ep | P, Q, … (two or more, all claims or all items) → claim, or collection of candidates | {*} (alternatives) |
| `∃` | Ep | P variable, Q claim; or P item → claim | some P satisfies Q ; P exists |
| `i→` | E | P claim, Q claim → claim (+6) | if P then Q |
| `i⇒` | Ep | P claim, Q claim; or P claim, Q directive → claim; or conditional directive (+6) | when P, Q applies ; if P, then do Q |
| `c⊃` | Ep | P assumption or time, Q claim; or P criterion, Q claim → claim (+6) | within P, Q ; within the criterion P, Q |
| `c⇒` | U | no signature (E-UNSIG) | — |

| Gap | Kind | What cannot be said yet |
| --- | --- | --- |
| G-05 | long to say | “Every” (a universal). |
| G-08 | cannot say | “Only”, “but”, “rather”, “instead”, “unless”. |

**F2.2 Reasons, support, inference and evidence**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `s∵` | E | P claim, Q claim → claim (+6) | P supports Q |
| `∵` | P | P claim, Q claim → claim (+6) | P is given as a reason for Q † |
| `r∵` | P | P claim, Q claim → claim (+6) | P is the basis given for the inference Q † |
| `j∵` | P | P claim, Q claim → claim (+6) | P justifies Q † |
| `e∵` | P | P claim, Q claim → claim (+6) | P explains Q † |
| `c∴` | U | P premise set, Q claim → claim (+6) | from the premises P it follows that Q |
| `∴` | U | no signature (E-UNSIG) | — |
| `d⊢` | E | P claim or item, Q claim or item → claim (+6) | P is derived from Q |
| `i⊢` | U | P premise set, Q claim, R criterion → claim (+5) | Q is inferred from the premises P by the rules R |
| `l⊢` | P | P premise set, Q claim, R criterion → claim (+5) | Q is derivable from P in the formal system R |
| `p⊢` | U | P premise set, Q claim, R criterion → claim (+5) | Q is established from P under the rules R |
| `e▤` | U | P item, Q claim → claim (+6) | P is evidence bearing on Q |

*No gap recorded for this family. That means nothing was recorded, not that nothing is missing.*

**F2.3 Causation, condition, constraint and necessity**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `c↝` | E | P claim, Q claim → claim (+6) | P causes Q |
| `c⊣` | U | P item, Q claim → claim (+6) | P restricts the possibility that Q † |
| `l⊣` | P | P item, Q item → claim (+6) | P is a limit on Q † |
| `n□` | P | P claim, Q claim → claim (+6) | P is required under Q † |

*No gap recorded for this family. That means nothing was recorded, not that nothing is missing.*

**F2.4 Sameness, difference, comparison and order**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `s=` | Ep | P item, Q item → claim (+6) | P is the same as Q |
| `s≈` | U | P item, Q item → claim (+6) | P is approximately equal to Q |
| `i≡` | Ep | P item, Q item → claim (+6) | P is identified as Q |
| `m≡` | U | P item, Q item → claim (+6) | P matches Q |
| `d≢` | U | P item, Q item → claim (+6) | P is told apart from Q |
| `r≡` | P | P item, Q item, R criterion → claim (+5) | P is recognized as matching Q under R † |
| `c≡` | P | P claim, Q claim → claim (+6) | P is compatible with Q |
| `c≠` | P | P claim, Q claim → claim (+6) | P conflicts with Q |
| `d≠` | P | P agent, Q agent, R claim → claim (+5) | P and Q hold different positions on R † |
| `b≻` | P | P item, Q item, R criterion → claim (+5) | P is better than Q under R † |
| `≈` | P | P item, Q item, R item → claim (+5) | P is estimated as Q within R † |
| `m>` | Ep | P math term, Q math term; or P count, Q count → claim (+6) | P is more than Q |
| `o≺` | P | P item, Q item, R criterion → claim (+5) | P comes before Q under R † |
| `v=` | P | P item, Q item → claim (+6) | P has the value Q † |
| `m∥` | P | P item, Q item, R value, S item → claim (+4) | the Q of P is R on the scale S † |
| `n−` | P | P item, Q criterion → claim (+6) | P is negative under Q † |

| Gap | Kind | What cannot be said yet |
| --- | --- | --- |
| G-04 | cannot say | A superlative: “the most”. |
| G-11 | cannot say | A criterion defined from roots: “noisy if more than 50 an hour”. |
| G-16 | long to say | A number within a closed range: “between 9 and 15”. |

**F2.5 Epistemic status, verification, probability and absence**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `v⊨` | E | P item, Q criterion → claim (+6) | P satisfies Q |
| `f⊤` | U | P claim, Q criterion → claim (+6) | P is held established under Q |
| `f⊥` | P | P claim, Q criterion → claim (+6) | P is false under Q |
| `k✓` | U | P claim → claim (+7) | P is established |
| `✓` | P | P item, Q criterion → claim (+6) | P is correct under Q |
| `✗` | P | P item, Q criterion → claim (+6) | P is incorrect under Q |
| `r✓` | P | P item, Q criterion → claim (+6) | P is resolved under Q |
| `s✓` | P | P item, Q item → claim (+6) | P is a candidate that meets the requirements Q † |
| `u±` | U | P value, Q value → claim (+6) | the estimate P carries the uncertainty Q |
| `l≥` | U | P claim → claim (+7) | the likelihood of P meets its threshold |
| `pℙ` | U | P claim, Q value, R item → claim (+5) | the probability of P is Q under the model R |
| `p⇢` | P | P claim, Q claim → claim (+6) | P predicts Q † |
| `n0` | E | nothing (an atom) → no kind | not supplied |

| Gap | Kind | What cannot be said yet |
| --- | --- | --- |
| G-10 | parked | “Probably”; a likelihood; a probability as a number. |
| G-14 | cannot say | “The field P has no value in Q”: the table’s former reading of `n0`. |

**F2.6 Provenance and reference**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `s@` | E | P claim or item, Q claim or item → claim (+6) | P comes from Q |
| `s@*` | E | P claim or item, Q claim or item → claim (+6) | P descends from Q |
| `r@` | Ep | P claim or item, Q item; or P item, Q message name → claim; or the kind of P | P is found at Q ; P as it stands in the message Q |
| `⊛` | E | P claim → claim (+7) | from stored knowledge, P |
| `r:` | U | P item, Q item, R item → claim (+5) | P is related to Q by R |

*No gap recorded for this family. That means nothing was recorded, not that nothing is missing.*

**F2.7 Time and sequence**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `t≺` | E | P claim → claim (+7) | before the reference time, P |
| `t●` | E | P claim → claim (+7) | at the reference time, P |
| `t▷` | E | P claim → claim (+7) | after the reference time, P |
| `▷` | U | P item, Q item → claim (+6) | P is followed by Q † |
| `b₀` | P | P method, Q claim → claim (+6) | the start state of P is Q † |
| `y⋯` | U | no signature (E-UNSIG) | — |
| `s≺` | Ep | P, Q, … (two or more: claims, acts or items) → claim, act, or claim about the order of items | {*} (in this order) |
| `s◷` | P | P item, Q item → claim (+6) | P is in the condition Q † |
| `s▷` | P | P method, Q item, R method → claim (+5) | in the process P, the stage Q leads to R † |

| Gap | Kind | What cannot be said yet |
| --- | --- | --- |
| G-01 | cannot say | A clock time, a date, a day name, a deadline, a zone, an interval; “today”, “last week”, “noon”. |
| G-09 | long to say | “Not yet”, “still running”; “never”. |

**F2.8 Structure, description, classification and relation**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `∈` | E | P item, Q collection → claim (+6) | P is a member of Q |
| `e∈` | P | P item, Q item → claim (+6) | P is an instance of Q † |
| `o\|` | P | P item, Q collection → claim (+6) | P is one of the candidates Q |
| `c◉` | P | P item, Q collection → claim (+6) | P is a central representation of Q † |
| `d⋮` | P | P item, Q collection → claim (+6) | P has the properties Q † |
| `p▦` | P | P item, Q collection → claim (+6) | P is a pattern among Q † |
| `s▦` | P | P item, Q collection → claim (+6) | P is an arrangement of Q † |
| `s⊞` | P | P item, Q collection, R item → claim (+5) | P is a system of Q with R † |
| `m⊞` | P | P item, Q item → claim (+6) | P is a model of Q † |
| `m↦` | P | P item, Q item → claim (+6) | P is mapped to the meaning Q † |
| `k#` | P | P item, Q item → claim (+6) | P is the key of Q † |
| `l↔` | P | P item, Q item → claim (+6) | P is related to Q † |
| `↔` | P | P item, Q item → claim (+6) | P is connected with Q † |
| `r∩` | P | P item, Q item → claim (+6) | P overlaps with Q † |
| `s≔` | P | P item, Q item, R item → claim (+5) | P is declared to have the state Q in R † |
| `⊡` | Ep | P item → claim (+7) | P is retained and accessible |
| `p?` | P | P claim, Q claim → claim (+6) | P is still open, pending Q † |
| `i←` | P | P item, Q method → claim (+6) | P flows into the process Q † |

| Gap | Kind | What cannot be said yet |
| --- | --- | --- |
| G-12 | cannot say | “Is in”, “is located at”. |
| G-15 | long to say | A sub-collection that is exactly the members satisfying a criterion: “3 of the 40 lines break the rule”. |

**F2.9 Agents: holding, attitude and interaction states**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `h⊡` | E | P agent, Q item → claim (+6) | P has Q |
| `b~` | P | P agent, Q claim → claim (+6) | P holds the stance that Q |
| `t~` | P | P agent, Q item, R item → claim (+5) | P relies on Q for R † |
| `i◎` | P | P agent, Q claim → claim (+6) | P aims at Q |
| `o◎` | P | P method, Q claim → claim (+6) | P is meant to attain Q |
| `g◎` | U | no signature (E-UNSIG) | — |
| `n!` | P | P agent, Q item → claim (+6) | P needs Q |
| `r−` | P | P agent, Q item → claim (+6) | P declines Q |
| `g▷` | P | P agent, Q claim, R method → claim (+5) | P directs, for the target Q, the next operation R † |
| `f▷` | P | P agent, Q method → claim (+6) | P proceeds by Q |
| `h+` | P | P agent, Q agent, R method → claim (+5) | P helps Q by R † |
| `s◇` | P | P agent, Q agent, R item → claim (+5) | P presents R to Q as a candidate † |
| `f↩` | P | P item, Q item → claim (+6) | P is feedback about Q † |
| `o▤` | P | P agent, Q item, R item, S item → claim (+4) | P observes Q, recorded as R and S † |
| `u✓` | P | P agent, Q item, R item → claim (+5) | P has recovered the intended meaning of Q to the standard R † |

*No gap recorded for this family. That means nothing was recorded, not that nothing is missing.*

**F3.1 Action constructors and role markers**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `cƒ` | E | P item or math term, then role markers → act (+7) | compute P |
| `o→` | E | P item or math term, then role markers → act (+7) | output P |
| `a+` | E | P item or math term, then role markers → act (+7) | accept P |
| `⌘` | E | P method → role marker | by the method P |
| `⚙` | E | P item → role marker | using P |
| `↣` | E | P item → role marker | for the recipient P |
| `☞` | E | P item → role marker | to the destination P |
| `☼` | E | P item → role marker | from the source P |
| `⚓` | E | P claim or item → role marker | on the basis of P |
| `♙` | E | P agent → role marker | done by P |

*No gap recorded for this family. That means nothing was recorded, not that nothing is missing.*

**F3.2 Act verbs**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `c?` | P | P item, Q criterion → act (+6) | check whether P meets Q |
| `c≶` | P | P item, Q item, R criterion → act (+5) | compare P and Q on R |
| `e⋯` | P | P item, Q method → act (+6) | explore P using Q |
| `i?` | P | P question, Q method → act (+6) | investigate the question P by Q |
| `t⋯` | P | P agent, Q item → act (+6) | P considers Q |
| `u↦` | P | P agent, Q item, R item → act (+5) | P applies Q to R † |
| `l↻` | P | P agent, Q item, R item → act (+5) | P updates Q based on R † |
| `i↑` | P | P item, Q criterion → act (+6) | improve P in Q |
| `t⚖` | P | P item, Q collection, R criterion → act (+5) | test P with the cases Q against R |
| `a<` | P | P agent, Q question → act (+6) | ask P the question Q |
| `q<` | U | P agent, Q item → act (+6) | demand from P the information Q |

| Gap | Kind | What cannot be said yet |
| --- | --- | --- |
| G-06 | cannot say | Act verbs: send, tell, approve, withdraw, rephrase, alert, restart, skip. |

**F3.3 Execution, completion, retry, decision and result**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `▶` | Ep | P method → act (+7) | run P |
| `c■` | Ep | P act → act or claim (+7) | complete P ; P is completed |
| `⤿` | Ep | P act → act (+7) | retry P |
| `d⊙` | U | P item → act (+7) | decide among P |
| `d↦` | E | P value, Q item → act or claim (+6) | determine the value P from Q ; the value P is determined from Q |
| `v✓` | E | P claim or item, Q criterion → act or claim (+6) | verify P against Q ; P is verified against Q |
| `c✓` | U | P item, Q claim → act (+6) | confirm P with Q † |
| `r→` | Ep | P math term, Q math term → claim (+6) | the value of P equals Q |

| Gap | Kind | What cannot be said yet |
| --- | --- | --- |
| G-07 | cannot say | An event as something that happened, not an act someone does: “the crash”. |

**F3.4 Directives and requirements**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `i!` | Ep | P act → directive (+7) | do P |
| `r<` | Ep | P agent, Q act → directive (+6) | ask P to Q |
| `r□` | Ep | P claim; or P conditional directive → requirement (+7) | it is required that P ; it is required: P |

*No gap recorded for this family. That means nothing was recorded, not that nothing is missing.*

**F4.1 Question formers**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `?=` | E | P variable, Q claim → question | which P satisfies Q? |
| `?⊤` | E | P claim → question (+7) | is it so that P? |
| `?◷` | P | P claim → question (+7) | when is it so that P? |
| `?@` | P | P claim → question (+7) | where is it so that P? |
| `?⊙` | P | P variable, Q collection, R claim → question | which P of Q satisfies R? |
| `?∵` | P | P claim → question (+7) | why is it so that P? |
| `?` | U | no signature (E-UNSIG) | — |

*No gap recorded for this family. That means nothing was recorded, not that nothing is missing.*

**F4.2 Answer forms**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `n⊘` | U | P mentioned question → claim (+7) | no, as to P |
| `y✓` | P | P mentioned question → claim (+7) | yes, as to P |
| `a>` | X | no signature (E-UNSIG) | — |

*No gap recorded for this family. That means nothing was recorded, not that nothing is missing.*

**F5.1 Status force**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `g←` | E | P claim → line (+7) | supplied: P |
| `h◇` | E | P claim → line or claim (+7) | as a hypothesis: P ; it is hypothesized that P |
| `p◇` | E | P claim → line or claim (+7) | admissible: P ; it is admissible that P |
| `u?` | E | P claim → line or claim (+7) | not known: P ; it is not known that P |
| `u~` | E | P claim → line or claim (+7) | not established: P ; it is not established that P |

*No gap recorded for this family. That means nothing was recorded, not that nothing is missing.*

**F5.2 Dialogue acts**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `a.` | Ep | P anything → line (+7) | received: P |
| `a=` | E | P claim or declaration → line (+7) | agreed: P |
| `a?` | E | P anything → line (+7) | unclear: P |
| `p↗` | E | P claim or declaration → line (+7) | proposed, not adopted: P |
| `e✗` | Ep | P anything → line (+7) | error in P |
| `r↻` | Ep | P anything → line (+7) | revised: P |
| `p▁` | P | P claim → line (+7) | taken as a starting point: P |
| `~` | Ep | P claim; or P criterion → assumption (+7) | assume P |

| Gap | Kind | What cannot be said yet |
| --- | --- | --- |
| G-13 | cannot say | Decline a request; take on a request (refusal, undertaking). |

**F6.1 Messages: identity, transmission and answer links**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `m▤` | use | P message name, Q agent; or P agent, Q agent, R item → declaration (the header); or claim | message P from Q ; the message R from P to Q |
| `r←` | P | P agent, Q agent, R item → claim (+5) | R is directed to Q by P † |
| `r>` | use | P message name, Q mentioned question, R line; or P item, Q item → line (the answer link); or claim | answer to Q of message P: R ; P answers Q |

*No gap recorded for this family. That means nothing was recorded, not that nothing is missing.*

---

# PART 3. LANGUAGE GAPS, AND HOW A NEW WORD ENTERS

## 3.1 What a gap is

A **language gap** is the Owner’s term for something SILEX truly cannot say. The Owner’s rule is that nothing is called a gap before it has been tried with the roots at hand, so each entry records, as far as the record has it, who tried and what was written instead; where the record does not say, the entry says so. Three kinds:

- **cannot say**: no line says it.
- **long to say**: a line says it, but only in a long form. A word here would shorten, not add meaning (the Owner raised the idea of symbols for common phrases on 1 Nov; it is not decided).
- **parked**: a root exists but is held back; a reader answers `a?`.

Lines marked ✔ were run on checker g3 for this file. The Evidence column cites records outside this file (the test records and Cb2’s cards); no rule of this file depends on them. **The first reader** is one reader who was given an earlier text of grammar r3 alone, wrote eight English sentences as SILEX and listed what it could not say (grammar r3, section 14). The register holds what two tests and that reader found. Absence from it means nothing was recorded, not that nothing is missing. No word in it is adopted.

## 3.2 How a new word enters (proposed; the Owner may change it)

1. **Evidence.** A sentence that blind participants tried to say with the roots at hand: who tried, and what they wrote instead.
2. **Card.** The nearest existing line and what it loses; then the candidate: root, family, signature (the kinds of its places in order, and the kind it makes), gloss, examples that pass, non-examples with the error each must give, and what the word does not say. This is the form of Cb2’s cards.
3. **Gates.** The card’s examples and non-examples are run on the checker, and the candidate on the regression lines, before anyone reads it.
4. **The Owner’s ruling**, word by word: add, do not add, or a convention on existing roots instead. Agreement among AIs does not add a word.
5. **Entry.** A new revision of this file, never an overwrite. The root gets a row in its family in Part 2 with tier P, shape and reading; its gap in Part 3 changes to “filled by …” and is not deleted.
6. **Test.** A blind reader test of the word before it is called established.

## 3.3 The register

| ID | Family | Kind | What cannot be said | Evidence | Tried with | Candidate | State |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G-01 | F2.7 | cannot say | A clock time, a date, a day name, a deadline, a zone, an interval; “today”, “last week”, “noon”. | Test 2 round 1: C, M, D. The time rules (1.8.1) give only a declared time name and the reference time of `c⊃`. | A time name `d≔(zt1,t)` with `c⊃(zt1,…)`; the time itself stays in an English scaffold or goes unsaid. | None proposed. Default idea: term roots that make a time, with `n0` for a missing part; no symbols chosen. | open |
| G-02 | F1.4 | cannot say | A number with a unit (percent, GB, seconds, “per hour”), as something that can be compared; “faster than” on a measured quantity. | Test 2 round 1: C, M, D. The first reader (“faster than”). Cb2 cards 2 and 9. | A `zv` name whose scaffold carries the number and the unit. `m>` takes two math terms or two counts; `r→` takes math terms only (a count gives E-CAT ✔). A value held in a scaffold is neither, so it cannot be compared. The first reader used `b≻`, a † reading. | Cb2 `m⌗` (the number a quantity has for an item, in its unit) and `s⌗` (the total over a collection). | candidates, none adopted |
| G-03 | F1.4 | cannot say | A count compared with a number: “at least 3 tests failed”, “at most 5 attempts”. | Test 2 round 1: C, D (“at least k”). Cb2 card 1. | Two counts compare: `g←(n¬(m>(#(zS2),#(zS1))))` passes ✔. A count against a number does not: `g←(m>(#(zS1),✠(3)))` is E-CAT ✔. | Cb2 `c⌗` (the number of members of a collection, as a math term). | candidate, not adopted |
| G-04 | F2.4 | cannot say | A superlative: “the most”. | Test 2 round 1: C, D. | The Test 2 record does not say what was written instead. | None. | open; named as a gap by the writers, their tries are not recorded |
| G-05 | F2.1 | long to say | “Every” (a universal). | Test 2 round 1: C. | A double negation over a domain passes: `g←(n¬(∃(zox,∧(∈(zox,zS1),n¬(v⊨(zox,zcr1))))))` ✔. The meaning can be said; only a short form is missing. | None. | sayable; a short form is a wish, not a gap in meaning |
| G-06 | F3.2 | cannot say | Act verbs: send, tell, approve, withdraw, rephrase, alert, restart, skip. | The first reader (send, tell, approve). Test 2 round 1: C, M, D. Test 2 round 2: C (item 16, “skip”). | `o→` (output), `a+` (accept), `r−`, `r↻`, `m↻`; or the act named by a scaffold (M wrote “skip the second test” as a method). | None. | open |
| G-07 | F3.3 | cannot say | An event as something that happened, not an act someone does: “the crash”. | Test 2 round 2: C (item 3). | The running of a named act, `▶(zm2)`. It reads oddly, because K4 lifts an act to “an act of this kind occurs”. | None. | open |
| G-08 | F2.1 | cannot say | “Only”, “but”, “rather”, “instead”, “unless”. | Test 2 round 1: C, M, D, in various combinations (the record groups with these words “never”, “not yet” and a prohibition). The first reader (“but”). | The Test 2 record does not say which lines were written for these words. A prohibition (“must not”) is a different sentence and can be said: `r□(n¬(zq1))` passes ✔; whether readers take it as “forbidden” is untested. | None. | open; named as a gap by the writers, their tries are not recorded |
| G-09 | F2.7 | long to say | “Not yet”, “still running”; “never”. | Test 2 round 1: C, M, D, in various combinations (with the words of G-08). `y⋯` (“still”) has no signature: `g←(y⋯(zm1))` is E-UNSIG ✔. | “Triggered before the time and not completed”, `g←(∧(c⊃(zt1,t≺(▶(zm1))),n¬(c■(zm1))))`, passes ✔ (with `zt1` declared). “Never” is `n¬(t≺(…))` inside `c⊃` (the example in 1.8.1). | Cb2 `y▸` (triggered before a time and not completed), definable. | candidate, not adopted |
| G-10 | F2.5 | parked | “Probably”; a likelihood; a probability as a number. | Test 2 round 1: C, M, D. | `l≥` (likely) and `pℙ` (probability) exist but are parked (tier U): a reader answers `a?`. | Cb2 `p◑` (the probability of a claim as a number, relative to a basis). | the Owner decides: un-park, adopt the candidate, or neither |
| G-11 | F2.4 | cannot say | A criterion defined from roots: “noisy if more than 50 an hour”. | Test 2 round 1: C, M, D. The rulebook (r3, B-43) counts 26 places that take a criterion among the 153 roots outside tier E and the two core-by-use roots, and no root makes one. | A `zcr` name with a scaffold. | None proposed. Default idea: a root that makes a criterion from a claim with a bound variable, and a marker for a criterion detail; no symbols chosen. | open |
| G-12 | F2.8 | cannot say | “Is in”, “is located at”. | Test 2 round 1 record: “found afterwards”. | The nearest is `r@(x,y)` with an item `y`: a pointer from `x` to `y` (1.6.3), read “P is found at Q” in Part 2. It passes in a line ✔, but the session checker refuses it in a session (S06), so it cannot be used there. `?@` asks for a location; no root states one. | None. | open |
| G-13 | F5.2 | cannot say | Decline a request; take on a request (refusal, undertaking). | Test 2 round 2, item 18: all three writers declared the requested act as a method and wrote the refusal as `r−` on that method, which declines the method, not the request; two of five readers hedged or disclaimed the link and a third gave only the literal “declines zm1”. Cb2 cards 3 and 4 (they cite refusal, commitment and intent as unsolved in an earlier lexicon). | `g←(r−(zkB,zm1))` passes ✔; it declines a candidate method, not the request. | Cb2 `d⊖` (the sender declines an act) and `u⊕` (the sender undertakes an act); or a convention for `r−` on a message name. | candidates, none adopted; the Owner may rule a convention instead of a root |
| G-14 | F2.5 | cannot say | “The field P has no value in Q”: the table’s former reading of `n0`. | The ruling of 1 Nov 07:29 made `n0` the placeholder (1.7, Z4); the table’s former reading then had no root. That consequence is not itself ruled. | Not tried: the reading was dropped from the glyph, not found missing in use. | None: a root and a symbol of its own, if the claim is wanted. | open |
| G-15 | F2.8 | long to say | A sub-collection that is exactly the members satisfying a criterion: “3 of the 40 lines break the rule”. | Cb2 card 5 (DEFINABLE: its definition uses existing roots and is 294 characters expanded). D’s blind reading: PARTIAL, useful. | `s∃` seeks an entity; it does not give the exact set. Cb2’s definition says it with `∧`, `n¬` and `∃` over the two collections. | Cb2 `f⊂`, definable. | candidate, not adopted |
| G-16 | F2.4 | long to say | A number within a closed range: “between 9 and 15”. | Cb2 card 6. D’s blind reading: MATCH, redundant. | Two `n¬(m>(…))` joined by `∧` pass under `g←` ✔. | Cb2 `b≬`, definable. | candidate, not adopted |

## 3.4 Candidate words offered so far (Cb2)

Cb2 is a fresh blind Claude session, memory off, given the OPEN BUILD package; its nine cards are candidates only. D read each blind from its card; the column “D’s blind reading” is that reading as scored in the record. Cb2’s own tier letters are not carried. The Owner has ruled on none, and none is in Part 2.

| Card | Word | Cb2 family | Cb2 kind | Reading | D’s blind reading | Gap |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `c⌗` | F1.4 | primitive | the number of members of a collection (at a time, if given), as a math term | MATCH, useful | G-03 |
| 2 | `m⌗` | F1.4 | primitive | the number a quantity has for an item (at a time, if given), in the unit the quantity names | MATCH, needed | G-02 |
| 3 | `u⊕` | F5.2 | primitive | the sender undertakes an act | MATCH, needed | G-13 |
| 4 | `d⊖` | F5.2 | primitive | the sender declines an act, with an optional reason (a claim) | MATCH, needed | G-13 |
| 5 | `f⊂` | F2.8 | definable | a collection holds exactly the members of another that meet a criterion | PARTIAL, useful | G-15 |
| 6 | `b≬` | F2.4 | definable | a number lies between two bounds, ends included | MATCH, redundant | G-16 |
| 7 | `p◑` | F2.5 | primitive | relative to a basis, the probability of a claim is a number from 0 to 1 | MATCH, useful | G-10 |
| 8 | `y▸` | F3.3 | definable | the method was triggered before the time and is not completed | PARTIAL, misleading | G-09 |
| 9 | `s⌗` | F1.4 | primitive | the sum over the members of a collection of the quantity (at a time, if given) | MATCH, needed | G-02 |

---

# PART 4. OPEN GRAMMAR POINTS

These are points of grammar, not missing words (those are in Part 3). Each needs a ruling or a test; this file does not pretend otherwise. Until the Owner rules, the text of Part 1 stands. D6 and D7 are marked [CANDIDATE] (K1 points to D6); they are the behaviour of checker g3 and are not ruled.

| # | Point | State |
| --- | --- | --- |
| P-1 | **D6: a role marker never fills a core place.** The pinned checker accepts `a?(♙(zkA))`, and the same with `a.`, `e✗`, `r↻` (their argument is `Any`); g3 refuses it with E-ARITY. A bare marker means nothing. The only point where Part 1 is not a superset of the pinned checker: 28 meaningless lines (4 roots × 7 markers). | [CANDIDATE] |
| P-2 | **D7: `m▤` and `r>` take no details.** The line checker and the session checker then agree that a header with a detail is refused. Without it, the generic rule (every root takes details) applies and the session checker reports no message. Refuses 88 lines of the test set (78 with a marker, 10 with `n0`). | [CANDIDATE] |
| P-3 | **Six roots have no signature:** `c⇒ ∴ y⋯ g◎ ? a>` (E-UNSIG). Each needs a signature, or removal from the table. The 30 parked roots stay parked. | open |
| P-4 | **An act among joiner claims.** K4 lets an act stand as a claim, so `∧(claim, act)` is accepted today although J2 says operands are of one kind. Keep as it is, or make it E-MIX. | open |
| P-5 | **Roots of one shape, and the † readings.** Form cannot tell roots of one shape apart; the gloss decides, and no root is merged or dropped before blind readers show whether two readers keep neighbours apart. 57 readings are marked †. Whether a marker suits its root (D10) is a reader's `a?`, not a form rule. | open, needs blind tests |
| P-6 | **Where a role marker sits** when a request carries an act: on `r<` or on its inner act. Both are accepted today. | open |
| P-7 | **Whether `s≺` is a time order.** Today it is an order, of claims, acts or items. | open |
| P-8 | **How a question is put to one named agent.** `r<(zkB,…)` asks an agent for an act or information; a question with a named addressee has no settled form. | open |

**Ruled by the Owner, so not open:** a root with an act shape listed first and a claim shape (`c■ d↦ v✓`), alone on a line, stays E-LINE (1 Nov 07:24); the placeholder is `n0` (1 Nov 07:29).

---

# PART 5. RULINGS, EVIDENCE AND RECORD

## 5.1 Rulings of the Owner that the text rests on

The Owner's words, shortened, 1 November (India time). Where a rule of Part 1 cites a ruling, it is one of these.

| When | Ruling |
| --- | --- |
| 01:29 | The roots are usable in the same style and grammar, self-contained, for AI-to-AI conversation with as little English as possible. |
| 01:45 | Roots nest like functions with arguments: one root inside another, some with one argument and some with five or six. |
| 01:57 | Established roots take more roots inside them; a root shown with three arguments can take up to eight; an argument that is not available is written with a placeholder (then `null`, since 07:29 `n0`). |
| 02:42 | Numbers and times are wrapped in term roots. |
| 03:22 | Declarations may be written on one line: all the names first, then all the definitions in the same order. |
| 03:29 | The grammar is primary. The checker is changed later to follow it, never the other way round. |
| 03:48 | Use the established roots too. A failing checker is no problem; what is needed is a rulebook. |
| 07:24 | A root with an act shape listed first and a claim shape (`c■ d↦ v✓`), alone on a line, stays E-LINE. |
| 07:29 | The placeholder is written `n0`, as in the table, not the word `null`. |

## 5.2 Evidence so far

Test items and answer keys are not part of this file or of the repository. Summary only:

- **Blind test 1** (on grammar r1; four readers, two Claude instances, Gemini, ChatGPT; 72 items): form verdicts 25 of 26 for each of the three readers on the full paper (the one miss, an act-and-claim root alone on a line, is the same for all three and is now ruled, 5.1); readings of 26 lines recovered in full bar one element; 20 of 20 English sentences written as SILEX. A ceiling: the items sat close to the grammar's own examples, and two readers share the author's model family.
- **First reader** (one reader, an earlier text of grammar r3 alone, eight English sentences written as SILEX): all eight messages (26 lines) passed the checker for form. Its own list of what it could not say gave the words marked “first reader” in Part 3.
- **Test 2, first round** (21 ordinary English sentences, three writers): the sentences could not be said in the lexicon. The writers themselves flagged a gap in 18, 16 and 16 of the 21 items. These gaps are the evidence of Part 3. Stage 2 was not run on that set.
- **Test 2, second round** (18 simple one-relation sentences, three writers, five blind readings): every writer's SILEX passed the checker bar one stray plain-English line (17 of 18 for one writer as written); the five readings recovered at least 97% of the key elements, two scorers agreeing on all but 4 of 245 judgments, no contradiction. Different encodings of one sentence were each read correctly. A ceiling again: it shows a floor, not capacity. The roots carried force, negation, cause, questions and requests; the scaffolds carried every predicate. "Decline a request" was the least stable item (G-13).

A pass of the checker shows form, not shared meaning. Only blind readers can show that.

## 5.3 Verification of this file

| Check | Result |
| --- | --- |
| Every `silex` line of Part 1, run on `ucl_check.py` (g3) | 93 of 93 lines give the verdict printed beside them, warnings included (blocks: 21) |
| The 195 roots of Part 2 | 195 rows in 25 family tables, each root once |
| Tiers counted from Part 2 | E 40, Ep 26, P 97, U 31 (29 parked, plus `m▤` and `r>` “core by use”: 2), X 1; core 68, trial 97, parked 30; 57 readings marked † |
| Every gap of Part 3 appears once in Part 2 and once in Part 3 | 16 gaps in 9 families, each once in each place |
| Lines of Part 3 said to pass or fail the checker (marked ✔) | 10 of 10 give the stated result on g3 |

Not checked by a tool: that the prose of Part 1 says what the checker does. It is the wording of grammar r3, whose section 14 reports example runs (93 of 93) and line-by-line comparisons of checker versions on large test sets, not a comparison of each prose rule with the checker.

## 5.4 What differs from grammar r3 and rulebook r3

No rule, no root, no example and no verdict. Only:

1. The rule IDs are those of grammar r3 (T, K, A, D, J, V, N, Z, M and the E-codes), so earlier records still point to the right rule. Section numbers are now 1.1 to 1.12, and Part 1 opens with one new paragraph.
2. Marks and notes addressed to the Owner are removed: the diamond marks ◆1 and ◆2 became **[CANDIDATE]** (D6, D7; K1 now says "see D6"), and the references to rulebook rule numbers (B-18, B-19, B-25, B-36, B-37), to "the rulebook's inference", to "the rulebook's English readings" and to OP-14 are gone from Part 1 or point to this file. (The Evidence column of Part 3 still names a few records outside this file, 3.1.) D5 now says which part of it is the Owner's ruling (the placeholder, 01:57) and which is checker behaviour. "Appendix A" is now "Part 2".
3. Grammar r3 section 2 (the family table) and Appendix A (the lexicon) are merged into Part 2, and each family now ends with its recorded gaps. The sentences around the family table are reworded to point to 2.2, and family numbers carry an F (F2.5) so that they are not taken for section numbers. The horizontal rules between sections are dropped.
4. Grammar r3 section 13 (changes and what stays open) is split: open words are Part 3, open grammar is Part 4. Section 14 (verification record) is replaced by 5.3; its checker diffs and the 18,420-line comparison stay in the tooling files. Not carried: the note that the codec cannot read back about 3,000 test-set lines with `n0` among the details. It concerns a tool, not the language.
5. New: Part 3 (gaps and how a new word enters), the "How to read" list, Part 5.1 and 5.2.
6. Not carried from the rulebook: its entries by family (one prose entry per root, about 820 lines), which remain the companion for anyone writing a codec or a checker, and its working notes.

## 5.5 Files

| File | SHA-256 |
| --- | --- |
| `SILEX-GRAMMAR-C-r3.md` | `723229b3c2c5442efbbe80a26594e72e702b67931bba87babf0b4c5b29916d7e` |
| `SILEX-RULEBOOK-r3.md` | `0573a32c3e9d71df12d94bbc4655c74562f8281dc0a86d12260ee5a286d4984b` |
| `ucl_check.py` (g3) | `3ec4e639fc9bda9de5293af87f636d7f2e1086bd5dc4e9758a9c8ba058bbf484` |
| `data_table.json` (n0 table) | `d144c3830d4221500fd9a87f25d2050948de72449f00bc4b3fbcbb13d6e24e94` |
| `silex_check_g3.py` | `09486de038dce9510c1a1c1dc158ca3557ae8554c8c790d95d484757dcfd18df` |

The three tool files, the grammar and the rulebook are in `drafts/SILEX-195-SNAPSHOT-001/` of the repository (the tools in its `tools/` folder). A SHA-256 identifies the bytes of a file. It does not make the file authoritative.

---

End of SILEX-195 SPEC DRAFT r1. Not adopted. Not frozen. No checksum record.
