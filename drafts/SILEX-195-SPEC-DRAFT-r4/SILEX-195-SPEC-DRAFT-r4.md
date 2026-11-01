# SILEX-195 | SPECIFICATION | DRAFT r4 | NOT ADOPTED | NOT FROZEN

**The 207-root language in one file: grammar, lexicon with its language gaps, and the open points.**

| Item | Value |
| --- | --- |
| Name | SILEX-195 SPEC DRAFT r4. SILEX-195 names the family of 195 base roots; r2 entered two roots (197), r3 ten more (207), and r4 enters none. The name is kept for continuity; whether to rename is the Owner's call. |
| Date | 2026-11-01 |
| Compiled by | C (Claude), at the Owner's word of 1 Nov 22:45: make r4 from his proposal of 22:26 (names that both sides accept last for the session), and amend it if needed (5.1) |
| Built from | `SILEX-195-SPEC-DRAFT-r3` (SHA-256 `93d448ef…`, the file as merged on 1 Nov); the Owner's proposal and questions of 1 Nov 22:26 to 22:45 (5.1); the Sustained-Conversation Profile, candidate r1f, for what it already says about proposal, acceptance and scaffolds (1.9.8); probes run on the prototype checker of r3 (5.2) |
| Status | **DRAFT. Not adopted, not frozen, no checksum record.** r4 differs from r3 by: a new section 1.9.8, *Shared names*, with the rules S1 to S6, and the changes to N5, N6 and 1.9.6 that go with it (marked [r4]); two conventions in 1.13 (C23 names of things, C24 kinds); two new gaps (G-22, G-23); P-11 applied as a draft, and three new open points (P-15 to P-17). **No root, no table entry and no checker changes**: Part 2 has the same 207 roots, and the lines that r3 printed give the same verdicts. The new rules are tier P and have not been tested: no reader and no session has met them. The Owner has not ruled on them word by word, and has not answered the question about U-31 (P-17). What differs is listed in Part 5.4. Only the Owner decides what is adopted, frozen or added. |
| Checker | The **prototype checker** of this draft: `ucl_check.py` (release g3 with the rule changes of the gap report), `timelit.py` (the check of a time text, from the gap report) and the 207-entry `data_table.json` (Part 5.5). It is intermediate: the Owner has said that the checker will change again and by much more, and that the measure is how much meaning is recovered, not a pass. Every line of SILEX printed in Part 1 carries the prototype's verdict after `# ` and was run on it. r4 does not change it. The shared names of 1.9.8 are not enforced by it: it reads one message at a time. `silex_check_g3.py`, the separate session checker of the snapshot, does not know the roots added in r3 and was not run. |
| Language of the file | English, for the AI participants. Relay notes to the Owner are sent separately, in Bengali. |

## How to read this file

1. **This file is your only source.** If your memory disagrees with it, follow the file and say so.
2. **One notation only.** If you have seen SILEX written in another way (the earlier word-token form, the Greek role markers, the 183-entry line), do not mix it in. If you notice yourself reaching for it, mark the point `a?` and carry on.
3. **Do not guess.** A line outside the rules, a parked root, a root without a signature, or an incomplete claim is marked `a?` and left (1.11). A reading marked † is a guess, given as such.
4. **A gap is not a failure.** If a sentence cannot be said with the roots at hand, say what you tried and mark the point. Part 3 records such gaps.
5. **English lives only inside `⌜ ⌝`**, as a scaffold, and is never part of the language.
6. **A pass of the checker shows form, not shared meaning** (1.11). Only blind readers can show that.
7. **Do not add or adopt.** You may propose a word through the entry steps in 3.2. Adoption is the Owner's alone; agreement among AIs is not adoption.

**Tags.** A rule with no tag restates what checker g3 does, and the prototype checker still does it (5.3). That is not a ruling: only the rulings of 5.1 are the Owner's, and some untagged rules rest on proposals the Owner has not ruled on one by one. **[r3]** marks a rule, reading or root that is new in r3 or changed from r2. It comes from the blind gap report, was run on the prototype checker, and is tier P: no reader has been tested on it in use. **[CANDIDATE]** marks a rule where the checker was changed by a choice put to the Owner as open (Part 4). No rule carries it in r3. **†** marks a reading that the table's gloss does not fix. **E, Ep, P, U, X** are the evidence tiers of 1.10.

**[r4]** marks a rule or convention that is new in r4 or changed from r3. It comes from the Owner's proposal of 1 Nov 22:26, was drafted by C, and is tier P: nothing in it has been tested by a reader or in a session.

**Contents.** Part 1 Grammar, with the shared names of 1.9.8 and the conventions of 1.13 · Part 2 Lexicon, 207 roots in 25 families, each family followed by its gaps · Part 3 Language gaps, and how a new word enters · Part 4 Open grammar points · Part 5 Rulings, evidence and record.

---

# PART 1. GRAMMAR

The rules, in order: tokens, kinds, application, details, joiners and binders, names, `n0`, time, criteria and number, lines and force, evidence, and (new in r3) conventions. Rule IDs (T, K, A, D, J, V, N, Z, M, the E-codes) are those of grammar r3; the rules M5 to M17 and 1.13 are new in r3, and a rule changed in r3 is marked [r3].

## 1.1 The language on one screen

SILEX is written as nested applications of roots. Every expression has one shape:

```
expression  =  root ( expression , expression , … )
            |  name  |  atom  |  n0    |  ⌜ mention ⌝  |  agent : expression
            |  ✠( math )  |  t◷( ISO 8601 time text )
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
| **T2** | **Roots.** The 207 symbols of the table. The reader takes the longest root that matches (`s@*` before `s@`). A root with places is followed at once by `(`. The atoms are `t 0 ⊤ x w n`; they take no `(`. |
| **T3** | **Names.** `z`, a class prefix, then letters and digits. The prefix is the class and the whole meaning (table below). A name is never applied: no `(` follows it. Names are opaque and need not be declared, except a time name (N5). |
| **T4** | **`n0`.** The two characters `n0`, when no letter, digit or `(` follows them. The word `null` is not read (E-SYNTAX). |
| **T5** | **Mention.** `⌜ … ⌝`, nestable. If the inside is SILEX it is read as SILEX, otherwise as raw English. A mention remembers what it mentions (1.3). |
| **T6** | [r3] **Math term, time text.** `✠(` … `)`: the inside is the math sublanguage of 1.8.3. `t◷(` … `)`: the inside is an ISO 8601 text (M5), not SILEX; it ends at the first `)`. |
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

A variable is not a separate class: it is a name of class `zk zm zo zv zS` that a binder binds (1.6); [r3] in `∃` and `?=` it may also be a `zE` name (V2).

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
| **K1** | A place of kind `K` accepts an expression of kind `K` or any subkind. A place written `K\|L` accepts either. A place of kind `Any` accepts every kind except a role marker (D6). |
| **K2** | `n0` fits every place (1.7). |
| **K3** | A root with several signatures (`m▤ r> h◇ p◇ u? u~ c■ d↦ v✓ i⇒ c⊃ r□ ~ m> r@ ∃ d⊖ c⌗ m⌗ s⌗`) is read by the place it stands in: the first signature whose result fits the kind expected there. At the top of a line, the first that checks. |
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
| **D4** | Core places and details together are at most **eight** (E-ARITY). [r3] The joiners (J1) and `d≔` (N1) have no such limit: they take as many operands as they list. |
| **D5** | A detail is a role marker or `n0`. After the core places `n0` stands for a role that was not given (the placeholder is the Owner's ruling, 1 Nov 01:57; what follows is checker behaviour). It counts toward the eight, means the same as leaving the role out, and prints no warning. In an action root, where the roles belong to the signature, and inside a marker (`⚓(n0)`), it prints NU. |
| **D6** | (Ruled by the Owner, 1 Nov 14:23.) A role marker stands only as a detail or, in the three action roots, as a role. It never fills a core place. |
| **D7** | (Ruled by the Owner, 1 Nov 14:23.) The protocol roots `m▤` and `r>` take no details. |
| **D8** | [r3] These take no details: the joiners `∧ a\| s≺`, the binders `∃ ?= ?⊙ l↦ ∀`, `r@`, `d≔`, `⌜ ⌝`, `✠`, `t◷`, the atoms, the seven markers, and the protocol roots of D7. |
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

### 1.6.2 Binders `∃  ?=  ?⊙  ∀  l↦`

| # | Rule |
| --- | --- |
| **V1** | `∃(v,φ)`: some `v` satisfies the claim `φ`. `?=(v,φ)`: which `v` satisfies `φ`? `?⊙(v,S,φ)`: which `v` of the collection `S` satisfies `φ`? The bare form `∃(x)` says that the item `x` exists in a stated domain. [r3] `∀(v,S,φ)`: every member `v` of the collection `S` satisfies the claim `φ` (M13). `l↦(v,φ)`: the criterion of being a `v` such that `φ` (M10). |
| **V2** | `v` is a name of class `zk zm zo zv zS` (E-BIND). [r3] In `∃` and `?=` it may also be a `zE` name, which stands for a number, so that *how many* can be asked: `?=(zEx,r→(c⌗(zS1),zEx))`. `l↦` and `∀` keep the five classes. It was not declared by `d≔` and is not already bound: no shadowing (E-BIND). |
| **V3** | [r3] A question binds one variable of its own and holds no other question (E-BIND). A claim inside it may bind further variables of its own with `∃` or `∀`. Its variable occurs in the body (E-BIND) and is not reused by another question in the same message (E-BIND). |
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
| **N1** | `d≔(n₁,…,nₖ,def₁,…,defₖ)` declares `k` names and then gives their `k` definitions in the same order. An odd number of arguments is E-ARITY. A definition may use a name declared earlier in the same line. [r3] There is no limit on `k`: the eight of D4 does not apply to `d≔`. |
| **N2** | The first half are names (E-DEF). A name already declared in the message is E-REDECL, whether it was declared by an earlier line or earlier in the same line. |
| **N3** | The class decides what may be defined: `zp zq zr zh` a claim; `zm` an act or method; `zo` an item; `zv` a value; `zS` a collection; `zk` an agent; `zcr` a criterion; `zE` a `✠` term or another `zE` name; `zt` the atom `t`, an imported qualified time, [r3] a time text `t◷(…)` or the time of an event `e◷(…)`. A `zU` name is declared only by the header (E-DEF). |
| **N4** | A definition that is quoted English is a scaffold (warning SCAFFOLD): it fixes nothing in SILEX and gives the reader English to go on. A scaffold may define a name of any class except `zt`, `zE` and `zU`. |
| **N5** | A name that is used but not declared means only its class. This is allowed for every class except `zt`: a time name must be declared first (E-UNDECL). [r4] A bound name (S2) is the exception: it means its definition, and a reader takes it so. The line checker does not know which names are bound and still reads it as its class. |
| **N6** | [r4] Names are local to their message, with two exceptions. The roster names: a `zk` name that is the sender in a header means that participant in every message. So `zkA` in `m▤(zUa1,zkA)` is the same agent in every message of the session. And the bound names of 1.9.8: a name that has been proposed and accepted keeps its definition in every later message of the session (S2). |

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

Many declarations in one line (N1), as many as are listed:

```silex
d≔(zS1,zS2,zS3,zS4,zS5,zS6,zS7,zS8,zS9,zS10,⌜a⌝,⌜b⌝,⌜c⌝,⌜d⌝,⌜e⌝,⌜f⌝,⌜g⌝,⌜h⌝,⌜i⌝,⌜j⌝)     # ok SCAFFOLD
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
| **M1** | A reference time is a declared time name: `d≔(zt1,t)`. [r3] It may also be defined by a time text, `d≔(zt1,t◷(2026-12-08T10:30+05:30))` (M5), or by the time of an event, `d≔(zt1,e◷(φ))` (M6). |
| **M2** | `c⊃(zt,φ)` considers the claim `φ` within the time `zt`; it is the only source of a reference time. `t≺ t● t▷` say that a claim holds before, at or after the reference time of the nearest enclosing `c⊃`; [r3] `t≼` says at or before it (M8). A tense with no enclosing `c⊃` warns RT: unresolved. |
| **M3** | A tense over a negation needs a state predicate under the negation (E-KIND): `h⊡` (established), or `⊡ v⊨ ∈ s= k✓ i≡` (new). For events put the negation outside: `n¬(t≺(▶(zm1)))`. |
| **M4** | `c⊃(ctx,φ)` takes an assumption `~(P)`, a time name, or a criterion as its context. [r3] A criterion may be made by `l↦` (M10); a time made by `t◷` or `e◷` is not itself a context (M7). |

```silex
d≔(zt1,t)                                       # ok
g←(c⊃(zt1,t≺(▶(zm1))))                          # ok
g←(t≺(▶(zm1)))                                  # ok RT
g←(c⊃(zt1,t≺(n¬(▶(zm1)))))                      # E-KIND
g←(c⊃(zt1,n¬(t≺(▶(zm1)))))                      # ok
```

*New in r3, tier P: rules M5 to M9 and the roots `t◷ e◷ t≼`. They come from the blind gap report and have not been read blind.*

| # | Rule |
| --- | --- |
| **M5** | [r3] **Time text.** `t◷(text)` makes a time (kind `Tm`) from an ISO 8601 text, the way `✠( )` makes a number from a math text. The text is checked, not read as SILEX, and ends at the first `)`. It is one of: a date (`2026`, `2026-11`, `2026-12-01`); a week (`2026-W50`, `2026-W50-1`); a time of day (`T14:30`, `T14:30:05Z`); an instant, date and time of day (`2026-12-08T10:30+05:30`); a duration (`P1Y2M3DT4H5M6S`, `PT10M`, `P2W`); an interval (`start/end`, `start/duration`, `duration/end`); a repeat (`R/` or `R3/` and an interval or a duration). A zone is `Z` or `+hh:mm` or `-hh:mm`. Only the extended form is read (with hyphens and colons). Anything else is E-TIME: a name (`noon`, `Friday`, `now`, `tonight`), a date that does not exist (`2026-02-30`), `20261208`, a space inside the text. An instant, a time of day, an interval or a repeat with no zone warns TZ: it is read in the sender's zone only. |
| **M6** | [r3] **Time of an event.** `e◷(φ)` makes the time at which the event of the claim `φ` happens. For an act that is when it occurs; for a state it is the moment the state begins to hold, so `e◷(c■(zm1))` is the moment the run of `zm1` is complete, not the stretch after it. It does not say that `φ` is true. |
| **M7** | [r3] **Where a time stands.** A time made by `t◷` or `e◷` fills a time place: the definition of a `zt` name (N3) or the time argument of `c⌗ m⌗ s⌗` (M14). Under a force root it is E-CAT; alone on a line it is E-LINE. As the context of `c⊃` it is accepted but supplies no reference time (warning RT): name it first (M1). |
| **M8** | [r3] **By.** `t≼(φ)` says that `φ` holds at or before the reference time. It is a tense root like `t≺ t● t▷`: M2 and M3 apply to it. It is definable, `a\|(t≺(φ),t●(φ))`, and the checker does not expand it. |
| **M9** | [r3] **A stretch.** When the reference time is a stretch (a date, a week, an interval), `t●(φ)` reads: `φ` falls within it. This is a reading, not a check. *On Friday* and *last week* are written so. |

A day name, *today*, *noon*, *now* are not ISO 8601. The sender works out the date or the hour from its own clock and writes that (1.13). The checker orders and compares nothing yet: the times are carried so that two readers read the same one.

```silex
d≔(zt1,t◷(2026-12-08T10:30+05:30))                          # ok
d≔(zt2,t◷(2026-W50))                                        # ok
d≔(zt3,e◷(c■(zm1)))                                         # ok
g←(c⊃(zt1,t≼(c■(zm1))))                                     # ok
g←(c⊃(zt2,t●(c■(zm1))))                                     # ok
g←(c⊃(zt3,∧(t▷(zq1),n¬(t≺(zq1)))))                          # ok
d≔(zt4,t◷(2026-12-08T10:30))                                # ok TZ
d≔(zt5,t◷(noon))                                            # E-TIME
d≔(zt6,t◷(2026-02-30))                                      # E-TIME
d≔(zt7,t◷(2026-12-08 10:30))                                # E-TIME
t◷(2026-12-01)                                              # E-LINE
g←(t◷(2026-12-01))                                          # E-CAT
g←(c⊃(zt1,t≼(n¬(c■(zm1)))))                                 # E-KIND
g←(c⊃(t◷(2026-12-08T10:30+05:30),t≼(c■(zm1))))             # ok RT
```

### 1.8.2 Criteria

A criterion is a declared `zcr` name [r3] or a term made by `l↦` (M10). Sameness roots `s= s≈ m≡ d≢` are relative to one; with none in context they warn CR (underspecified). A criterion is supplied by `c⊃(zcr,φ)`.

```silex
g←(c⊃(zcr1,s=(zo1,zo2)))                        # ok
g←(s=(zo1,zo2))                                 # ok CR
```

*New in r3, tier P: rules M10 to M13 and the roots `l↦ ∀ b⊤`, with a reading for `c↓`. They come from the blind gap report and have not been read blind.*

| # | Rule |
| --- | --- |
| **M10** | [r3] **A criterion from a rule.** `l↦(v,φ)` makes a criterion: the criterion of being a `v` such that `φ`. `v` is a variable (V1, V2) and occurs in `φ`. An item meets it when `φ` holds of that item, so `v⊨(zo1,l↦(zox,φ))` says that `φ` holds with `zo1` for `zox`. The checker binds `v` and checks `φ`; it does not substitute. The result has kind `Cr`: it fills a criterion place (`v⊨`, `c↓`, `b≻`, `b⊤`, a criterion context of `c⊃`), and a `zcr` name may be defined by it (N3). A criterion made this way names no label: the label stays in a scaffold (gap G-20). |
| **M11** | [r3] A value claim in the body of `l↦` is atemporal (1.8.3). A rule about a moment gives `m⌗` its time argument (M14). `l↦` says nothing about time itself. |
| **M12** | [r3] **Narrowing.** `c↓(S,crit)` is read as exactly the members of `S` that meet `crit`: nothing outside `S`, and every member of `S` that meets `crit`. This is a reading (it keeps its †); the form check is unchanged. A count of the narrowed collection is then the count of those members. |
| **M13** | [r3] **Every and the best.** `∀(v,S,φ)`: every member `v` of the collection `S` satisfies `φ`; true of an empty `S`. It is definable, `n¬(∃(v,∧(∈(v,S),n¬(φ))))`, and the domain is the second argument. `b⊤(x,S,crit)`: `x` is a member of `S` and no other member of `S` is better than `x` under `crit` (ties allowed). It is definable, `∧(∈(x,S),n¬(∃(zoq,∧(∈(zoq,S),n¬(s=(zoq,x)),b≻(zoq,x,crit)))))`, so a line whose own variable is `zoq` clashes with it. The direction (the most, the least) is in the criterion: *having more of the quantity* and *having less of it* are two criteria. The checker expands neither. |

```silex
d≔(zS1,zv1,⌜the files⌝,⌜length, in meters⌝)                       # ok SCAFFOLD
d≔(zcr2,l↦(zox,m>(m⌗(zox,zv1),✠(7))))                       # ok
d≔(zS2,c↓(zS1,zcr2))                                        # ok
g←(v⊨(zo1,l↦(zoy,m>(m⌗(zoy,zv1),✠(7)))))                    # ok
g←(∀(zoz,zS1,v⊨(zoz,zcr2)))                                 # ok
?=(zox,b⊤(zox,zS1,zcr2))                                    # ok
g←(∀(zoz,zS1))                                              # E-ARITY
g←(l↦(zoz,v⊨(zoz,zcr2)))                                    # E-CAT
d≔(zcr3,l↦(zoz,v⊨(zo1,zcr2)))                               # E-BIND
g←(b⊤(zo1,zS1))                                             # E-ARITY
```

### 1.8.3 Number

[r3] Numbers live in `✠( )`, in the number terms `c⌗ m⌗ s⌗` (M14), as counts `#(S)`, or as `zv` names. `✠` is a term and stands only in a closed list of places: the object of `cƒ`, an argument of `r→` or `m>`, the number of `p◑`, the definiens of a `zE` name (E-MATHPLACE). A term of `c⌗ m⌗ s⌗` is of the same kind and stands in the same places, except that it does not define a `zE` name (E-DEF). Inside the brackets of `✠`:

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

*New in r3, tier P: rules M14 to M17 and the roots `c⌗ m⌗ s⌗ p◑`. They are the Cb2 cards 1, 2, 9 and 7 (Part 3.4), taken as the project record has them. D read all four blind once, from their cards; none has been tested in use.*

| # | Rule |
| --- | --- |
| **M14** | [r3] **Number terms.** `c⌗(S)`, `m⌗(x,q)` and `s⌗(S,q)` make math terms (kind `Ex`), each with an optional last argument, a time. `c⌗(S)`: the number of members of the collection `S`. `m⌗(x,q)`: the number that the quantity `q` (a `zv` name) has for `x`. `s⌗(S,q)`: the sum, over the members of `S`, of the number that `q` has for each. Like `✠` they stand where a math term is asked (1.8.3), and so beside `✠` in `r→` and `m>`. A count `#(S)` stays a count (kind `Ct`); `m>` takes two counts or two math terms, never one of each. |
| **M15** | [r3] **Units.** The unit lives in the English name of the quantity, once: `d≔(zv1,⌜length, in meters⌝)`. The number is a term and carries no unit. The checker does not compare units; two quantity names are one quantity only if their scaffolds are identical. A sum of a quantity that cannot be added (percentages, temperatures) is not meaningful: a reader marks `a?`. |
| **M16** | [r3] **Time of a number.** Without its time argument a number term is read at the time the claim is evaluated: the sender's now for a statement, the answerer's now for an answer. A sender who means another time, or a quantity that changes between sending and reading, writes the time argument. The claim stays atemporal: a tense or a `c⊃` time around it is E-ATEMP (1.8.3). |
| **M17** | [r3] **Probability.** `p◑(φ,p,basis)`: relative to `basis`, the probability of the claim `φ` is the number `p`, from 0 to 1 (a fraction, `✠(÷(9,10))`). `basis` is an item, the data or method the figure rests on; when it is a set of cases it is a `zS` name. It is a claim and does not say that `φ` is true, or whether the figure is a frequency or a belief. The checker does not test 0 to 1, or that `p` is defined, and raises no E-ATEMP; a reader marks `a?` for a `p` outside 0 to 1, and reads the claim as atemporal. `l≥` and `pℙ` stay parked (G-10). |

A number term does not define a `zE` name (E-DEF) and does not stand inside `✠( )` (E-MATH): arithmetic inside `✠` takes literals only (gap G-18).

```silex
d≔(zS1,zS2,zv1,⌜the first files⌝,⌜the second files⌝,⌜length, in meters⌝)    # ok SCAFFOLD
g←(m>(c⌗(zS1),✠(10)))                                       # ok
g←(m>(c⌗(zS1),c⌗(zS2)))                                     # ok
g←(r→(m⌗(zo1,zv1),✠(2)))                                    # ok
g←(r→(s⌗(zS1,zv1),✠(96)))                                   # ok
g←(p◑(zq1,✠(÷(9,10)),zS2))                                  # ok
?=(zEx,r→(c⌗(zS1),zEx))                                     # ok
g←(m>(#(zS1),✠(10)))                                        # E-CAT
g←(c⌗(zS1))                                                 # E-CAT
g←(r→(c⌗(zo1),✠(10)))                                       # E-CAT
g←(r→(s⌗(zS1),✠(96)))                                       # E-ARITY
d≔(zE1,c⌗(zS1))                                             # E-DEF
g←(r→(m⌗(zo1,zv1),✠(0.95)))                                 # E-MATH
g←(p◑(zq1,zv1,zS2))                                         # E-CAT
```

```silex
d≔(zt1,t)                                                   # ok
g←(m>(m⌗(zo1,zv1,zt1),✠(2)))                                # ok
g←(c⊃(zt1,m>(m⌗(zo1,zv1,zt1),✠(2))))                        # E-ATEMP
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

**1.9.6 Questions and answers.** `?⊤(P)` is answered in exactly one of three ways, `g←(P)`, `g←(n¬(P))`, `u?(P)`. `?=` and `?⊙` ask for a value. There is one answer per question, and a question with no target is marked `a?`. An answer is given by the answer link `r>(zUk,⌜Q⌝,W)`: it answers question `Q` of message `zUk`, and `W` is exactly `g←(A)` or `u?(A)` (E-FORCE). [r4] Names are local to their message (N6) unless they are bound (1.9.8), so the answering message does not share its other names with the question's message. Inside an answer, `zq1` is the answerer's own name; the claim as it stands in the question's message is written `r@(zq1,zUk)`. Both forms pass the form check. Use `r@` when the answer must be about the question's own claim.

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

## 1.9.7 Undertaking and declining

*New in r2. Tier P: the pair was read blind once, from a card (Part 5.2), and has not been tested as a pair.*

`u⊕(a)` says that the sender undertakes the act `a`. `d⊖(a)` and `d⊖(a,why)` say that the sender declines the act `a`, with the claim `why` as its reason. Both make a line (kind Ln) and take an act. A named method is an act, but write `▶(zm1)` where the running of the method is meant (1.9.5).

| # | Rule |
| --- | --- |
| **W1** | `u⊕` and `d⊖` are lines, like a force root. A claim place does not accept them, so `g←`, `n¬`, `r□`, `h◇`, `p↗` or `?⊤` around them is E-CAT. As an answer inside `r>` they are E-FORCE (the answer is `g←` or `u?`). |
| **W2** | The sender is the performer. If the act names another performer with `♙`, the reader marks `a?`. |
| **W3** | `u⊕` says that the sender takes the act on. It does not say that the act is done (that is `c■`), that it can be done, that it is binding, or that anyone may demand it. |
| **W4** | `d⊖` says that the sender will not do the act. It does not say that the sender cannot (gap G-17), that the act is wrong, or that the refusal is final. Not doing the act and saying nothing is silence, not `d⊖`. |
| **W5** | The reason of `d⊖` is a claim given as the reason. It is not thereby asserted. To have it taken as fact, supply it on its own line, `g←(P)`. |
| **W6** | `u⊕(a)` and `d⊖(a)` for the same act in one message conflict: the reader marks `a?`. The checker does not catch this. Across messages see P-9. |
| **W7** | A line answers a request `r<(zkX,a)` when it is about the same act. In another message the act is written with its qualified name, `r@(zm1,zUa1)` (1.6.3). It may also stand without a request (P-10). |

A asks B to run the check; B declines and gives a reason. In another message B takes the act on instead.

```silex
m▤(zUa1,zkA)                                                         # ok
d≔(zm1,⌜run the check⌝)                                              # ok SCAFFOLD
r<(zkB,▶(zm1))                                                       # ok
```

```silex
m▤(zUb1,zkB)                                                         # ok
d≔(zo2,⌜write permission on the job scheduler⌝)                      # ok SCAFFOLD
d⊖(▶(r@(zm1,zUa1)),n¬(h⊡(zkB,zo2)))                                  # ok
```

```silex
m▤(zUb2,zkB)                                                         # ok
u⊕(▶(r@(zm1,zUa1)))                                                  # ok
```

Lines that are refused:

```silex
g←(u⊕(▶(zm1)))                                                       # E-CAT
n¬(d⊖(▶(zm1)))                                                       # E-CAT
u⊕(▶(zm1),▶(zm1))                                                    # E-ARITY
d⊖(▶(zm1),?⊤(zq1))                                                   # E-CAT
r>(zUa1,⌜?⊤(zq1)⌝,u⊕(▶(zm1)))                                        # E-FORCE
```

## 1.9.8 Shared names

*New in r4. Tier P: the Owner's proposal of 1 Nov 22:26, drafted here. No reader has met it and no session has run on it.*

A session needs to say what a name stands for once, and then to use the name alone. The proposal is made with the dialogue acts that 1.9.4 already has: one side proposes names with their definitions, the other side accepts, and from then on both use the names without English. The rules below add only how long an accepted name lasts.

| # | Rule |
| --- | --- |
| **S1** | [r4] **Proposal.** `p↗(d≔(…))` offers the names of a declaration with their definitions (N1). Until it is accepted it binds nothing: the names stay local to its message (N6). |
| **S2** | [r4] **Acceptance.** A line `a=(d≔(…))` from another participant, restating names with exactly the same definitions (a scaffold word for word, a SILEX definition symbol for symbol), **binds** the restated names. Restating only some of the names binds only those. From the next message of the session on, both participants use a bound name without declaring it, and it means its definition. |
| **S3** | [r4] **What is not acceptance.** `a?` (unclear), `a.` (received, not agreed), a different declaration offered in turn with `p↗`, silence, and any other line that only uses the name bind nothing. Silence is never acceptance. A refusal has no form of its own (P-16): the other side sends `a.` or `a?`, and may offer its own alternative as a new proposal. |
| **S4** | [r4] **A bound name keeps its meaning** to the end of the session. A second, different declaration of a bound name is a clash: the reader keeps the first and marks `a?`. A new meaning gets a new name. Repeating the same declaration is harmless. Who may pick which names is a session agreement (the Sustained-Conversation Profile has one); the grammar only says that two senders who pick the same name for different things have a clash. |
| **S5** | [r4] **Reach.** A bound name is used in any later message by either participant, also inside `r@`. It binds the participants who proposed it or accepted it (P-15 for more than two). It ends with the session and is not carried to another. A name of any class is bound, except a time name defined by the atom `t`, which means the time of its own message (M1) and is declared in each message that needs it. |
| **S6** | [r4] **What a pass shows.** The line checker reads one message at a time and does not know what is bound: a bound name passes as its class, as in N5. Whether a name is bound, and whether a clash has happened, is for the reader and for a session checker. No tool tests S2 or S4. |

The Sustained-Conversation Profile (candidate r1f, rule U-31, accepted by the Owner on 31 October for the profile) keeps scaffolds to the names of referents (classes `zo zk zS zv zm zcr`) and writes claims in roots. N4 of this file is wider: any class except `zt zE zU`. r4 leaves both as they are, and the examples below follow the profile (P-17).

A proposes the names of a parabola, its two tangents, a property and a quantity. B accepts. In A's next message the names are used without a declaration; the claim `zq1` is written in roots from the bound names.

```silex
m▤(zUa1,zkA)                                                         # ok
p↗(d≔(zo1,zS1,zcr1,zv1,⌜the parabola⌝,⌜the two tangents drawn to it⌝,⌜being perpendicular to each other⌝,⌜the curvature of the parabola⌝))   # ok SCAFFOLD
```

```silex
m▤(zUb1,zkB)                                                         # ok
a=(d≔(zo1,zS1,zcr1,zv1,⌜the parabola⌝,⌜the two tangents drawn to it⌝,⌜being perpendicular to each other⌝,⌜the curvature of the parabola⌝))   # ok SCAFFOLD
```

```silex
m▤(zUa2,zkA)                                                         # ok
d≔(zq1,v⊨(zS1,zcr1))                                                 # ok
g←(zq1)                                                              # ok
?=(zEx,r→(m⌗(zo1,zv1),zEx))                                          # ok
```

A proposes one more name. B does not follow it, or has received it and does not agree. In both cases nothing is bound.

```silex
m▤(zUa3,zkA)                                                         # ok
p↗(d≔(zo2,⌜the directrix⌝))                                          # ok SCAFFOLD
```

```silex
m▤(zUb2,zkB)                                                         # ok
a?(d≔(zo2,⌜the directrix⌝))                                          # ok SCAFFOLD
```

```silex
m▤(zUb2,zkB)                                                         # ok
a.(d≔(zo2,⌜the directrix⌝))                                          # ok SCAFFOLD
```

Lines that do not do what the rules ask:

```silex
m▤(zUb3,zkB)                                                         # ok
d≔(zS2,⌜two tangents are perpendicular⌝)                             # ok SCAFFOLD
g←(zS2)                                                              # E-CAT
g←(a=(d≔(zo2,⌜the directrix⌝)))                                      # E-CAT
n¬(a=(d≔(zo2,⌜the directrix⌝)))                                      # E-CAT
r−(d≔(zo2,⌜the directrix⌝))                                          # E-ARITY
```

The first of these is a claim hidden under a collection name: a claim name is `zp zq zr zh`, and a claim goes in roots (U-31). The last two show that acceptance is a line and cannot be negated, and that `r−` refuses an item, not a declaration (P-16).

## 1.10 Evidence

Every root carries a **status**, and every expression the set of statuses of what it is built from.

| Status | Meaning | Roots |
| --- | --- | --- |
| **E** | established | 40 |
| **Ep** | established with open parts | 26 |
| **P** | proposed: a signature and a gloss, no test yet | 109 |
| **U** | parked: not applied | 31 |
| **N** | a new reading or a new design suggestion | (readings, not roots) |
| **X** | excluded | 1 |

The **level** of a line is the weakest status in it, ranked E > Ep > P > U > N > X. Two roots of status U, `m▤` and `r>`, are core by use: sessions use them as header and answer link.

**Tiers.** *Core*: status E or Ep (66 roots) with `m▤` and `r>`. *Trial*: status P (109). *Parked*: the other 29 roots of status U and the excluded `a>` (30 roots; `a>` and five of the others have no signature). A parked root is not applied: a reader who meets one answers `a?`. Core is 68 roots, trial 109, parked 30.

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
| E-TIME | M5 | [r3] a time text outside the closed ISO 8601 subset |
| NU · FU · RT · CR · SCAFFOLD · TZ | Z2 · 1.9.1 · M2 · 1.8.2 · N4 · M5 | warnings: n0 supplied; force unspecified; reference time missing; criterion missing; quoted English; [r3] a clock time with no zone |

## 1.13 Conventions: saying more with the roots at hand

*New in r3, tier P. Written from the blind gap report; every line was run on the prototype checker; no reader has been tested on them.*

A **convention** says a word with roots that already exist. It adds no symbol and changes no rule. It is not yet a word: nothing makes two senders choose the same line until the Owner adopts it as the way to say that thing, and a convention that loses part of a word says so below. A reader who meets a line that follows a convention reads it that way, and marks `a?` where the convention does not reach. In the lines, `zq1 zq2 zq3` are claims, `zm1` a method, `zS1 zS2` collections, `zo1 zo2` items, `zv1` a quantity (M15), `zcr1` a criterion, `zkA zkB` agents, `zt1` a time.

**Logic words.** *But, however, although, whereas* (C1): two lines, or one `∧`; the contrast is not carried, only that both hold. *Rather than, instead of* (C2): the denial and the replacement. *Both … and, neither … nor* (C6): `∧` of the claims, `∧` of the denials.

```silex
g←(∧(zq1,zq2))                                              # ok
g←(∧(n¬(zq1),zq2))                                          # ok
g←(∧(n¬(zq1),n¬(zq2)))                                      # ok
```

*Only* (C3): the claim, and its denial for every other member of an explicit domain; without the domain it is E-DOMAIN. With `∀` the denial is shorter. *Except, but for* (C4): both halves, the rest satisfy and the exceptions do not.

```silex
g←(∧(c■(a+(zo1,♙(zkB))),n¬(∃(zkx,∧(∈(zkx,zS1),c■(a+(zo1,♙(zkx))),n¬(s=(zkx,zkB)))))))     # ok CR
g←(∧(c■(a+(zo1,♙(zkB))),∀(zkx,zS1,i→(c■(a+(zo1,♙(zkx))),s=(zkx,zkB)))))                   # ok CR
g←(∧(c■(a+(zo1,♙(zkB))),n¬(∃(zkx,∧(c■(a+(zo1,♙(zkx))),n¬(s=(zkx,zkB)))))))                # E-DOMAIN
g←(∧(∀(zox,zS1,i→(n¬(∈(zox,zS2)),v⊨(zox,zcr1))),∀(zoy,zS2,n¬(v⊨(zoy,zcr1)))))              # ok
```

*Unless* (C5), in a prohibition (*do not do it unless both hold*): the requirement that the act happens only if both claims hold. Then, in this order: *exclusive or*, *otherwise*, *if and only if*, *notify me when* (C19). (*A only if B* is `i→(A,B)`.)

```silex
r□(i→(▶(zm1),∧(zq2,zq3)))                                   # ok
g←(∧(a|(zq1,zq2),n¬(∧(zq1,zq2))))                           # ok
g←(∧(i⇒(zq1,zq2),i⇒(n¬(zq1),zq3)))                          # ok
g←(∧(i→(zq1,zq2),i→(zq2,zq1)))                              # ok
i⇒(zq1,r<(zkB,▶(zm1)))                                      # ok
```

**Time.** *Today, tomorrow, Friday, last week, noon* (C14): the sender works the date or the hour out of its own clock and writes it as a time text (M5); *on Friday* and *last week* are read as in M9. *Not yet, no longer* (C7): the sender declares its own clock reading once, as a time name, and uses it as the reference time. *Never* (C8): the denial of the event before that reading. Both hold only up to the reading: a message replayed later is stale. *Still* is not carried (`y⋯` has no signature, P-3). Nothing in the line marks that time as the clock reading rather than a deadline: a reader needs this convention to know, and C7b below is an alternative (P-12).

```silex
d≔(zt1,t◷(2026-12-01T09:00+05:30))                          # ok
g←(c⊃(zt1,n¬(c■(zm1))))                                     # ok
g←(c⊃(zt1,n¬(t≺(c■(zm1)))))                                 # ok
```

The same, with the deadline and the stretch (C14), and the alternative C7b, the time of the message itself, which says *now* without a value that can go stale:

```silex
d≔(zt2,t◷(2026-12-04))                                      # ok
d≔(zt3,t◷(2026-12-07T12:00+05:30))                          # ok
g←(c⊃(zt2,t●(c■(zm1))))                                     # ok
r□(c⊃(zt3,t≼(c■(zm1))))                                     # ok
d≔(zt4,e◷(m▤(zkA,zkB,zUa1)))                                # ok
```

**Numbers.** *At least 2, at most 2, exactly 2, more than 2, fewer than 2* (C9), in this order, with `c⌗`. *Higher, faster, larger, above, over* (C10): `m>` on two `m⌗` of one quantity; swap the arguments for *lower, slower, smaller*. *About 90* (C20): a closed range, written with two denials, ends included. *In all, a total* (C21): `s⌗`; a bound on it is a requirement. *Decimals and percent* (C22): a fraction; `✠(0.95)` is E-MATH. *Ninety percent sure*: `p◑`, with its basis (M17).

```silex
g←(n¬(m>(✠(2),c⌗(zS1))))                                    # ok
g←(n¬(m>(c⌗(zS1),✠(2))))                                    # ok
g←(r→(c⌗(zS1),✠(2)))                                        # ok
g←(m>(c⌗(zS1),✠(2)))                                        # ok
g←(m>(✠(2),c⌗(zS1)))                                        # ok
g←(m>(m⌗(zo1,zv1),m⌗(zo2,zv1)))                             # ok
g←(∧(n¬(m>(✠(85),m⌗(zo1,zv1))),n¬(m>(m⌗(zo1,zv1),✠(95)))))  # ok
g←(r→(s⌗(zS1,zv1),✠(96)))                                   # ok
r□(n¬(m>(s⌗(zS1,zv1),✠(100))))                              # ok
g←(r→(m⌗(zo1,zv1),✠(÷(95,100))))                            # ok
g←(r→(m⌗(zo1,zv1),✠(0.95)))                                 # E-MATH
g←(p◑(zq1,✠(÷(9,10)),zS2))                                  # ok
```

**Acts and questions.** *Act verbs* (C13): send, tell, alert are `o→`; run is `▶`; finish is `c■`; check is `v✓`; approve is `a+`; retry is `⤿`. Withdraw is not carried: `r↻` is *revised*, and withdrawing across messages is P-9. *Rephrase*: mark the point unclear and ask for it again; *differently* is not said. *Question words* (C18), in this order: who, whether, when, where, why, which of a collection by a criterion, which is the most, how many. A question holds one variable of its own (V3).

```silex
r<(zkB,o→(zo1,↣(zkA)))                                      # ok
i!(▶(zm1))                                                  # ok
g←(c■(a+(zo1,♙(zkB))))                                      # ok
i!(v✓(zq1,zcr1))                                            # ok
i!(⤿(zm1))                                                  # ok
a?(zq1)                                                     # ok
?=(zkx,c■(a+(zo1,♙(zkx))))                                  # ok
?⊤(c■(zm1))                                                 # ok
?◷(c■(zm1))                                                 # ok
?@(zq1)                                                     # ok
?∵(zq1)                                                     # ok
?=(zox,∧(∈(zox,zS1),v⊨(zox,zcr1)))                          # ok
?=(zoy,b⊤(zoy,zS1,zcr1))                                    # ok
?=(zEx,r→(c⌗(zS1),zEx))                                     # ok
```

**Names of things** [r4]. *Proper names* (C23): a person, an organisation, a place, an agent, a work. Each is a name of its referent class with a scaffold of the name as written, in any script; two things with one name get two names and a phrase in the scaffold that tells them apart. The scaffold holds the name and nothing else. The same spelling is the same text, hence the same thing; another spelling is another name until the senders restate it. A named time (*Diwali*) takes no scaffold (N4): it is written as a date (C14). Nothing in the line says which person or place is meant; a pass shows that the structure was recovered, not the referent (1.11). *Kinds* (C24): a circle, a triangle, a tangent. Each is a criterion `zcr` with a scaffold (*being a circle*), used as `v⊨(x,zcr1)`; many things of a kind are a `zS`, narrowed with `c↓` and counted with `c⌗`. The meaning stays in the scaffold, because no root defines it. A relation between two things (*tangent to*, *perpendicular to*) has no root (G-22); the nearest is a criterion with the second thing fixed inside its scaffold. Names and kinds are proposed once and then bound (1.9.8), so a session says them once.

```silex
m▤(zUa4,zkA)                                                         # ok
d≔(zk3,zo3,⌜Dr. Example⌝,⌜the bridge at Howrah⌝)                     # ok SCAFFOLD
d≔(zk4,⌜ডক্টর নমুনা⌝)                                                  # ok SCAFFOLD
g←(c■(a+(zo3,♙(zk3))))                                               # ok
d≔(zcr2,zS3,⌜being a circle⌝,⌜the curves drawn on the board⌝)        # ok SCAFFOLD
g←(m>(c⌗(c↓(zS3,zcr2)),✠(1)))                                        # ok
d≔(zt1,⌜Diwali⌝)                                                     # E-DEF
```

**Not written, not carried.** *Please, thank you, well* and the other politeness and discourse particles (C16), and articles and copulas (C17), are not written: they have no truth conditions. *Probably* and *certainly* are not carried: `h◇` says *as a hypothesis*, not a likelihood, and `p◑` needs a number (G-10). *Should* and *ought* are not carried: `r□` says a requirement, and the difference between advice and requirement is lost (G-21). *Still*, *withdraw*, *inability* (*cannot*) and *in a folder* have no form (P-3, P-9, G-17, G-12).

---

# PART 2. LEXICON WITH ITS GAPS

The 207 roots, in 25 families. Each family table is followed by the language gaps recorded for it; a new word enters at its gap, by the steps of 3.2. Family numbers are written with an F (F2.5), so that they are not taken for section numbers.

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
| F1.4 Quantity and mathematics | 7 | `✠` `#` | `c∑` `dΔ` `c⌗` `m⌗` `s⌗` | — |
| F2.1 Logical core: negation, joining, quantification, implication, context | 10 | `n¬` `∧` `a\|` `∃` `i→` `i⇒` `c⊃` | `l↦` `∀` | `c⇒` |
| F2.2 Reasons, support, inference and evidence | 12 | `s∵` `d⊢` | `∵` `r∵` `j∵` `e∵` `l⊢` | `c∴` `∴` `i⊢` `p⊢` `e▤` |
| F2.3 Causation, condition, constraint and necessity | 4 | `c↝` | `l⊣` `n□` | `c⊣` |
| F2.4 Sameness, difference, comparison and order | 17 | `s=` `i≡` `m>` | `r≡` `c≡` `c≠` `d≠` `b≻` `≈` `o≺` `v=` `m∥` `n−` `b⊤` | `s≈` `m≡` `d≢` |
| F2.5 Epistemic status, verification, probability and absence | 14 | `v⊨` `n0` | `f⊥` `✓` `✗` `r✓` `s✓` `p⇢` `p◑` | `f⊤` `k✓` `u±` `l≥` `pℙ` |
| F2.6 Provenance and reference | 5 | `s@` `s@*` `r@` `⊛` | — | `r:` |
| F2.7 Time and sequence | 12 | `t≺` `t●` `t▷` `s≺` | `b₀` `s◷` `s▷` `t◷` `e◷` `t≼` | `▷` `y⋯` |
| F2.8 Structure, description, classification and relation | 18 | `∈` `⊡` | `e∈` `o\|` `c◉` `d⋮` `p▦` `s▦` `s⊞` `m⊞` `m↦` `k#` `l↔` `↔` `r∩` `s≔` `p?` `i←` | — |
| F2.9 Agents: holding, attitude and interaction states | 15 | `h⊡` | `b~` `t~` `i◎` `o◎` `n!` `r−` `g▷` `f▷` `h+` `s◇` `f↩` `o▤` `u✓` | `g◎` |
| F3.1 Action constructors and role markers | 10 | `cƒ` `o→` `a+` `⌘` `⚙` `↣` `☞` `☼` `⚓` `♙` | — | — |
| F3.2 Act verbs | 11 | — | `c?` `c≶` `e⋯` `i?` `t⋯` `u↦` `l↻` `i↑` `t⚖` `a<` | `q<` |
| F3.3 Execution, completion, retry, decision and result | 8 | `▶` `c■` `⤿` `d↦` `v✓` `r→` | — | `d⊙` `c✓` |
| F3.4 Directives and requirements | 3 | `i!` `r<` `r□` | — | — |
| F4.1 Question formers | 7 | `?=` `?⊤` | `?◷` `?@` `?⊙` `?∵` | `?` |
| F4.2 Answer forms | 3 | — | `y✓` | `n⊘` `a>` |
| F5.1 Status force | 5 | `g←` `h◇` `p◇` `u?` `u~` | — | — |
| F5.2 Dialogue acts | 10 | `a.` `a=` `a?` `p↗` `e✗` `r↻` `~` | `p▁` `u⊕` `d⊖` | — |
| F6.1 Messages: identity, transmission and answer links | 3 | `m▤` `r>` | `r←` | — |

A signature is written `root : K₁, K₂, … → R`: the kinds of the core places in order, then the kind the root makes. `v⊨ : Ref, Cr → P` says that `v⊨` takes an item and a criterion and makes a claim. 2.2 prints the shapes in words.

### 2.2 The roots, by family

Tier: **E** established, **Ep** established with open parts, **P** proposed, **U** parked, **X** excluded, **use** core by use. Shape lists the core places in order, then what the root makes; `(+k)` is the number of details that fit after the core places, within the limit of eight. P, Q, R, … in the reading are the places in order. † marks a reading that the table's gloss does not fix.

**F0.1 Application, names and definition**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `d≔` | Ep | P1 … Pk names, then Q1 … Qk definitions (k ≥ 1) → declaration | let the names P stand for the definitions Q |

| Gap | Kind | What cannot be said yet |
| --- | --- | --- |
| G-20 | cannot say | A label tied to a rule: “let us call a thing P if …”, so that the label can be used in later messages. |

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
| `c↓` | P | P collection, Q criterion → collection (+6) | exactly the members of P that meet Q † |
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
| `c⌗` | P | P collection; or P collection, Q time → math term (+7; +6 with the time) | the number of members of P (at the time Q) |
| `m⌗` | P | P item, Q value; or P item, Q value, R time → math term (+6; +5 with the time) | the number that the quantity Q has for P (at the time R), in the unit that Q names |
| `s⌗` | P | P collection, Q value; or P collection, Q value, R time → math term (+6; +5 with the time) | the sum, over the members of P, of the number that the quantity Q has for each (at the time R) |

| Gap | Kind | What cannot be said yet |
| --- | --- | --- |
| G-02 | cannot say | Filled in r3 by `m⌗` and `s⌗` (tier P): a number with a unit, compared; a total. The unit is in the name of the quantity (M15). |
| G-03 | cannot say | Filled in r3 by `c⌗` (tier P): a count compared with a number: “at least 3 tests failed”, “at most 5 attempts”. |
| G-18 | cannot say | Arithmetic over measured terms: an average, a share or percentage of a collection, “two hours after the start” (a time plus a duration); an ordinal (“the third”), “rises”, “plus or minus”. |
| G-23 | cannot say | “The product of the slopes is minus one”, “x squared plus y squared is nine”: a claim with free letters, an equation or an identity. |

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
| `l↦` | P | P variable, Q claim → criterion | the criterion of being a P such that Q |
| `∀` | P | P variable, Q collection, R claim → claim | every member P of Q satisfies R |

| Gap | Kind | What cannot be said yet |
| --- | --- | --- |
| G-05 | long to say | Filled in r3 by `∀` (tier P, definable): the short form of “every”. |
| G-08 | cannot say | Carried in r3 by conventions on existing roots (1.13): “only”, “but”, “rather”, “instead”, “unless”. The contrast of “but” is not carried. |

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
| `b⊤` | P | P item, Q collection, R criterion → claim (+5) | P is a best member of Q under R |

| Gap | Kind | What cannot be said yet |
| --- | --- | --- |
| G-04 | cannot say | Filled in r3 by `b⊤` (tier P, definable): a superlative, “the most”, “the least”. |
| G-11 | cannot say | Filled in r3 by `l↦` (F2.1, tier P): a criterion defined from roots: “heavy if more than N a day”. |
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
| `p◑` | P | P claim, Q math term, R item → claim (+5) | relative to R, the probability of P is the number Q, from 0 to 1 |

| Gap | Kind | What cannot be said yet |
| --- | --- | --- |
| G-10 | parked | Filled in r3 for a probability given as a number, by `p◑` (tier P). Plain “probably” and a likelihood are not carried; `l≥` and `pℙ` stay parked. |
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
| `t●` | E | P claim → claim (+7) | at the reference time, P; when that time is a stretch, P falls within it |
| `t▷` | E | P claim → claim (+7) | after the reference time, P |
| `▷` | U | P item, Q item → claim (+6) | P is followed by Q † |
| `b₀` | P | P method, Q claim → claim (+6) | the start state of P is Q † |
| `y⋯` | U | no signature (E-UNSIG) | — |
| `s≺` | Ep | P, Q, … (two or more: claims, acts or items) → claim, act, or claim about the order of items | {*} (in this order) |
| `s◷` | P | P item, Q item → claim (+6) | P is in the condition Q † |
| `s▷` | P | P method, Q item, R method → claim (+5) | in the process P, the stage Q leads to R † |
| `t◷` | P | P time text (ISO 8601, not SILEX) → time | the time given by the text P |
| `e◷` | P | P claim → time (+7) | the time at which the event of P happens (a state: the moment it begins) |
| `t≼` | P | P claim → claim (+7) | at or before the reference time, P |

| Gap | Kind | What cannot be said yet |
| --- | --- | --- |
| G-01 | cannot say | Filled in r3 by `t◷` `e◷` `t≼` (tier P, blind test pending): a clock time, a date, a day name, a deadline, a zone, an interval; “today”, “last week”, “noon”, written as dates and hours (1.13). Not filled: *now* (P-12), G-19. |
| G-09 | long to say | “Not yet”, “still running”; “never”. |
| G-19 | cannot say | Time ideas with no reading: recurrence (“every night”), since, for, throughout, until, always, a quarter or a season, and ten of Allen’s thirteen interval relations (before, after and equals are sayable). |

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
| G-22 | cannot say | “Tangent to”, “perpendicular to”, “parallel to”, “adjacent to”: a relation between two things, named by a word of a field. |

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

| Gap | Kind | What cannot be said yet |
| --- | --- | --- |
| G-21 | cannot say | The strength of advice: “should”, “ought”, as against “must”. |

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
| `u⊕` | P | P act → line (+7) | the sender undertakes P |
| `d⊖` | P | P act → line (+7); or P act, Q claim → line (+6) | the sender declines P; the reason is Q |

| Gap | Kind | What cannot be said yet |
| --- | --- | --- |
| G-13 | cannot say | Filled in r2 by `u⊕` and `d⊖` (tier P, blind test pending): decline a request; take on a request (refusal, undertaking). |
| G-17 | cannot say | Inability: “cannot” (not able), as against “will not” and “not allowed”. |

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

Lines marked ✔ were run on the prototype checker of this draft. The Evidence column cites records outside this file (the test records and Cb2’s cards); no rule of this file depends on them. **The first reader** is one reader who was given an earlier text of grammar r3 alone, wrote eight English sentences as SILEX and listed what it could not say (grammar r3, section 14). The register holds what two tests, that reader and the gap report found. Absence from it means nothing was recorded, not that nothing is missing. No word in it is established; the words that entered are tier P: two in r2 (G-13) and ten in r3 (G-01 to G-05, G-10, G-11).

## 3.2 How a new word enters (proposed; the Owner may change it)

1. **Evidence.** A sentence that blind participants tried to say with the roots at hand: who tried, and what they wrote instead.
2. **Card.** The nearest existing line and what it loses; then the candidate: root, family, signature (the kinds of its places in order, and the kind it makes), gloss, examples that pass, non-examples with the error each must give, and what the word does not say. This is the form of Cb2’s cards.
3. **Gates.** The card’s examples and non-examples are run on the checker, and the candidate on the regression lines, before anyone reads it. (Done for the ten words of r3: 5.3.)
4. **The Owner’s ruling**, word by word: add, do not add, or a convention on existing roots instead. Agreement among AIs does not add a word.
5. **Entry.** A new revision of this file, never an overwrite. The root gets a row in its family in Part 2 with tier P, shape and reading; its gap in Part 3 changes to “filled by …” and is not deleted.
6. **Test.** A blind reader test of the word before it is called established.

## 3.3 The register

| ID | Family | Kind | What cannot be said | Evidence | Tried with | Candidate | State |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G-01 | F2.7 | cannot say | A clock time, a date, a day name, a deadline, a zone, an interval; “today”, “last week”, “noon”. | Test 2 round 1: C, M, D. The gap report: 13 of its 46 gap places are time. The time rules of r2 gave only a declared time name and the reference time of `c⊃`. | A time name `d≔(zt1,t)` with `c⊃(zt1,…)`; the time itself stayed in an English scaffold or went unsaid. With the new roots: `d≔(zt2,t◷(2026-12-08T10:30+05:30))` ✔, `d≔(zt3,e◷(c■(zm1)))` ✔, `g←(c⊃(zt1,t≼(c■(zm1))))` ✔. | The gap report: `t◷` (a time from ISO 8601 text), `e◷` (the time of an event), `t≼` (at or before). | filled in r3 by `t◷`, `e◷` and `t≼` (tier P; blind test pending). Not filled: *now* (P-12) and the other time ideas (G-19) |
| G-02 | F1.4 | cannot say | A number with a unit (percent, GB, seconds, “per hour”), as something that can be compared; “faster than” on a measured quantity. | Test 2 round 1: C, M, D. The first reader (“faster than”). Cb2 cards 2 and 9. The gap report: 14 of its 46 places are number. | A `zv` name whose scaffold carries the number and the unit. `m>` takes two math terms or two counts; `r→` takes math terms only (a count gives E-CAT ✔). A value held in a scaffold is neither, so it could not be compared. The first reader used `b≻`, a † reading. With the new roots: `g←(r→(m⌗(zo1,zv1),✠(2)))` ✔ and `g←(m>(m⌗(zo1,zv1),m⌗(zo2,zv1)))` ✔. | Cb2 `m⌗` (the number a quantity has for an item, in its unit) and `s⌗` (the total over a collection). | filled in r3 by `m⌗` and `s⌗` (tier P; D read both as needed); the unit lives in the name of the quantity and is not checked (M15); blind test of use pending |
| G-03 | F1.4 | cannot say | A count compared with a number: “at least 3 tests failed”, “at most 5 attempts”. | Test 2 round 1: C, D (“at least k”). Cb2 card 1. | Two counts compare: `g←(n¬(m>(#(zS2),#(zS1))))` passes ✔. A count against a number did not: `g←(m>(#(zS1),✠(3)))` is E-CAT ✔. With `c⌗`: `g←(n¬(m>(✠(3),c⌗(zS1))))` ✔ says *at least 3*. | Cb2 `c⌗` (the number of members of a collection, as a math term). | filled in r3 by `c⌗` (tier P; D read it as useful); blind test of use pending |
| G-04 | F2.4 | cannot say | A superlative: “the most”. | Test 2 round 1: C, D. The gap report. | The Test 2 record does not say what was written instead. The nearest long form is a question with a negated existence and `b≻` (79 characters in the gap report). With the new root: `?=(zox,b⊤(zox,zS1,zcr1))` ✔ asks which member is a best one; the direction is in the criterion (M13). | The gap report: `b⊤`. | filled in r3 by `b⊤` (tier P, definable); blind test pending |
| G-05 | F2.1 | long to say | “Every” (a universal). | Test 2 round 1: C. The gap report. | A double negation over a domain passes: `g←(n¬(∃(zox,∧(∈(zox,zS1),n¬(v⊨(zox,zcr1))))))` ✔. The meaning can be said; only a short form was missing. With the new root: `g←(∀(zox,zS1,v⊨(zox,zcr1)))` ✔. | The gap report: `∀`. | filled in r3 by `∀` (tier P, definable): the short form of what could already be said; blind test pending |
| G-06 | F3.2 | cannot say | Act verbs: send, tell, approve, withdraw, rephrase, alert, restart, skip. | The first reader (send, tell, approve). Test 2 round 1: C, M, D. Test 2 round 2: C (item 16, “skip”). The gap report: 3 of its 46 places are act verbs. | `o→` (output), `a+` (accept), `r−`, `r↻`, `m↻`; or the act named by a scaffold (M wrote “skip the second test” as a method). In r3, convention C13 (1.13): `r<(zkB,o→(zo1,↣(zkA)))` ✔ for send, tell, alert. | None. | partly carried by convention C13 (1.13): send, tell, alert, approve. Not carried: withdraw (P-9), rephrase (in part), restart, skip |
| G-07 | F3.3 | cannot say | An event as something that happened, not an act someone does: “the crash”. | Test 2 round 2: C (item 3). | The running of a named act, `▶(zm2)`. It reads oddly, because K4 lifts an act to “an act of this kind occurs”. | None. | open |
| G-08 | F2.1 | cannot say | “Only”, “but”, “rather”, “instead”, “unless”. | Test 2 round 1: C, M, D, in various combinations (the record groups with these words “never”, “not yet” and a prohibition). The first reader (“but”). The gap report: 12 of its 46 places are logic words. | The Test 2 record does not say which lines were written for these words. A prohibition (“must not”) is a different sentence and can be said: `r□(n¬(zq1))` passes ✔; whether readers take it as “forbidden” is untested. In r3, conventions C1 to C6 and C19 (1.13) say them with `∧`, `n¬`, `∀`, `i→`, `i⇒`: `g←(∧(n¬(zq1),zq2))` ✔ for *rather than*. | The gap report: conventions on existing roots, no new symbol. | carried by conventions (1.13), no new symbol; not read by a reader; the contrast of “but” is not carried |
| G-09 | F2.7 | long to say | “Not yet”, “still running”; “never”. | Test 2 round 1: C, M, D, in various combinations (with the words of G-08). `y⋯` (“still”) has no signature: `g←(y⋯(zm1))` is E-UNSIG ✔. | “Triggered before the time and not completed”, `g←(∧(c⊃(zt1,t≺(▶(zm1))),n¬(c■(zm1))))`, passes ✔ (with `zt1` declared). “Never” is `n¬(t≺(…))` inside `c⊃` (the example in 1.8.1). In r3, with a declared clock reading, `g←(c⊃(zt1,n¬(c■(zm1))))` ✔ says “not yet” (convention C7, 1.13). | Cb2 `y▸` (triggered before a time and not completed), definable; not entered in r3. | carried by conventions C7 and C8 (1.13), not read by a reader; “still” is not carried (`y⋯` has no signature, P-3); `y▸` is not entered (D read it as misleading) |
| G-10 | F2.5 | parked | “Probably”; a likelihood; a probability as a number. | Test 2 round 1: C, M, D. | `l≥` (likely) and `pℙ` (probability) exist but are parked (tier U): a reader answers `a?`. With the new root, a probability given as a number: `g←(p◑(zq1,✠(÷(9,10)),zS2))` ✔. | Cb2 `p◑` (the probability of a claim as a number, relative to a basis). | filled in r3 for a probability given as a number, by `p◑` (tier P; D read it as useful); plain “probably” is not carried. `l≥` and `pℙ` stay parked (C’s decision, left to C by the Owner on 1 Nov 12:06): `l≥` has no stated threshold, and `pℙ` overlaps `p◑`; what happens to `pℙ` is the Owner’s decision |
| G-11 | F2.4 | cannot say | A criterion defined from roots: “heavy if more than N a day”. | Test 2 round 1: C, M, D. The rulebook (r3, B-43) counts 26 places that take a criterion among the 153 roots outside tier E and the two core-by-use roots, and no root makes one. The gap report: 2 of its 46 places. | A `zcr` name with a scaffold. With the new root: `d≔(zcr2,l↦(zox,m>(m⌗(zox,zv1),✠(30))))` ✔. | The gap report: `l↦` (the criterion of being a v such that …), the root that the rulebook asked for. | filled in r3 by `l↦` (tier P); blind test pending. A label for the criterion is G-20 |
| G-12 | F2.8 | cannot say | “Is in”, “is located at”. | Test 2 round 1 record: “found afterwards”. | The nearest is `r@(x,y)` with an item `y`: a pointer from `x` to `y` (1.6.3), read “P is found at Q” in Part 2. It passes in a line ✔, but the session checker refuses it in a session (S06), so it cannot be used there. `?@` asks for a location; no root states one. | None. | open |
| G-13 | F5.2 | cannot say | Decline a request; take on a request (refusal, undertaking). | Test 2 round 2, item 18: all three writers declared the requested act as a method and wrote the refusal as `r−` on that method, which declines the method, not the request; two of five readers hedged or disclaimed the link and a third gave only the literal “declines zm1”. Cb2 cards 3 and 4 (they cite refusal, commitment and intent as unsolved in an earlier lexicon). | `g←(r−(zkB,zm1))` passes ✔; it declines a candidate method, not the request. With the roots of r2, `d⊖(▶(zm1))` ✔ and `u⊕(▶(zm1))` ✔ say that the sender declines or takes on the act. | Cb2 `d⊖` (the sender declines an act) and `u⊕` (the sender undertakes an act), cards 4 and 3. | filled in r2 by `u⊕` and `d⊖` (tier P, 1.9.7) on the Owner’s ruling of 1 Nov 14:23; a blind test of the pair is pending |
| G-14 | F2.5 | cannot say | “The field P has no value in Q”: the table’s former reading of `n0`. | The ruling of 1 Nov 07:29 made `n0` the placeholder (1.7, Z4); the table’s former reading then had no root. That consequence is not itself ruled. | Not tried: the reading was dropped from the glyph, not found missing in use. | None: a root and a symbol of its own, if the claim is wanted. | open |
| G-15 | F2.8 | long to say | A sub-collection that is exactly the members satisfying a criterion: “3 of the 40 lines break the rule”. | Cb2 card 5 (DEFINABLE: its definition uses existing roots and is 294 characters expanded). D’s blind reading: PARTIAL, useful. The gap report. | `s∃` seeks an entity; it does not give the exact set. Cb2’s definition says it with `∧`, `n¬` and `∃` over the two collections. | Cb2 `f⊂`, definable; not entered in r3. | not filled by a new word: `f⊂` is not entered. `c↓(S,crit)` is read as exactly the members of S that meet crit (M12), which is what `f⊂` would say; blind test of the reading pending |
| G-16 | F2.4 | long to say | A number within a closed range: “between 9 and 15”. | Cb2 card 6. D’s blind reading: MATCH, redundant. | Two `n¬(m>(…))` joined by `∧` pass under `g←` ✔. In r3 *about* is written so (convention C20, 1.13). | Cb2 `b≬`, definable; not entered in r3. | candidate, not entered (D read it as redundant); the long form serves |
| G-17 | F5.2 | cannot say | Inability: “cannot” (not able), as against “will not” and “not allowed”. | Cb2 card 4: `d⊖` is refusal only, and the card says inability has no form (it cites D3 11.1). The gap report. | A reason given with a refusal, `d⊖(▶(zm1),n¬(h⊡(zkB,zo2)))` ✔, says why the sender declines. It does not say that the sender is unable. | The gap report: `a◇` (able to); not entered in r3: no sentence needs it alone and nobody has read it. | open |
| G-18 | F1.4 | cannot say | Arithmetic over measured terms: an average, a share or percentage of a collection, “two hours after the start” (a time plus a duration); an ordinal (“the third”), “rises”, “plus or minus”. | The gap report: concepts N16, N19, N21, N25, N29 and N32 of its inventory, deferred. Not found in a test. | `✠( )` takes literals only: a number term inside it, as in `g←(r→(✠(÷(c⌗(zS1),2)),✠(3)))`, is E-MATH ✔. `s⌗` gives a total and `c⌗` a count; their quotient cannot be said inside `✠`. | None. | open; the gap report advises no change for now (P-14) |
| G-19 | F2.7 | cannot say | Time ideas with no reading: recurrence (“every night”), since, for, throughout, until, always, a quarter or a season, and ten of Allen’s thirteen interval relations (before, after and equals are sayable). | The gap report: concepts T06, T09, T19, T20, T26 and T39 of its inventory, deferred. Not found in a test. | `t◷` accepts the text of a repeat, `d≔(zt2,t◷(R/2026-12-01T02:00+05:30/P1D))` ✔, but `c⊃` over a set of times has no reading, so a repeat can be named and not used. | None. | open |
| G-20 | F0.1 | cannot say | A label tied to a rule: “let us call a thing P if …”, so that the label can be used in later messages. | The gap report: R07 of its inventory, deferred; it ties the case to the shared-glossary idea D-11 of the Owner’s earlier list. | A criterion can be proposed with its rule, `p↗(d≔(zcr1,l↦(zox,m>(m⌗(zox,zv1),✠(30)))))` ✔, and reached from another message with `r@(zcr1,zUa1)`. The label itself stays in a scaffold, tied to the rule only by standing in one message. Names are local to their message (N6). | None. P-11 (names that last) is the nearest proposal. | open |
| G-21 | F3.4 | cannot say | The strength of advice: “should”, “ought”, as against “must”. | The gap report: its convention for “should” loses the strength. | `r□(▶(zm1))` ✔ says a requirement; “should” and “must” then look alike. | None. The gap report suggests a root for the strength of advice as a later card. | open |
| G-22 | F2.8 | cannot say | “Tangent to”, “perpendicular to”, “parallel to”, “adjacent to”: a relation between two things, named by a word of a field. | The Owner’s questions of 1 Nov 22:37 (kinds such as *tangent*). Nobody has written it. | A criterion with the second thing fixed inside its scaffold works for one fixed thing: `d≔(zcr3,⌜touching the parabola at exactly one point⌝)` ✔ and `g←(v⊨(zo1,zcr3))` ✔. No root takes two open items for a named relation, and `l↦` makes a criterion of one item only. | None proposed. One option is a root for a named relation between two items, defined by a scaffold. | open |
| G-23 | F1.4 | cannot say | “The product of the slopes is minus one”, “x squared plus y squared is nine”: a claim with free letters, an equation or an identity. | The Owner’s proposal of 1 Nov 22:26 (a critical mathematics problem solved in a session). Nobody has written it. | A value claim takes no free letter: `g←(r→(✠(×(m,n)),✠(−(0,1))))` is E-FREE ✔. Numerals alone pass: `g←(r→(✠(×(2,3)),✠(6)))` ✔. An equation can sit in a scaffold under a claim name (N4 allows it), but the profile keeps scaffolds off claim names (U-31, P-17). | None proposed. Options: letters bound by a binder inside a value claim; a root for an equation. | open |

## 3.4 Candidate words offered so far, and what became of them

Two sets of cards have been offered. No word from either is frozen: a word in tier P is a draft entry, and the Owner decides what is adopted.

**Cb2’s nine cards.** Cb2 is a fresh blind Claude session, memory off, given the OPEN BUILD package. D read each blind from its card; the column “D’s blind reading” is that reading as scored in the record. Cb2’s own tier letters are not carried. The Owner ruled on cards 3 and 4 (1 Nov 14:23): they entered in r2 as tier P. In r3 cards 1, 2, 7 and 9 enter on the Owner’s word of 21:52 (5.1), as tier P; cards 5, 6 and 8 do not.

| Card | Word | Cb2 family | Cb2 kind | Reading | D’s blind reading | Gap | In this file |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `c⌗` | F1.4 | primitive | the number of members of a collection (at a time, if given), as a math term | MATCH, useful | G-03 | in Part 2 (r3, tier P) |
| 2 | `m⌗` | F1.4 | primitive | the number a quantity has for an item (at a time, if given), in the unit the quantity names | MATCH, needed | G-02 | in Part 2 (r3, tier P) |
| 3 | `u⊕` | F5.2 | primitive | the sender undertakes an act | MATCH, needed | G-13 | in Part 2 (r2, tier P) |
| 4 | `d⊖` | F5.2 | primitive | the sender declines an act, with an optional reason (a claim) | MATCH, needed | G-13 | in Part 2 (r2, tier P) |
| 5 | `f⊂` | F2.8 | definable | a collection holds exactly the members of another that meet a criterion | PARTIAL, useful | G-15 | not entered: `c↓` is read exactly (M12) |
| 6 | `b≬` | F2.4 | definable | a number lies between two bounds, ends included | MATCH, redundant | G-16 | not entered: the long form serves (C20) |
| 7 | `p◑` | F2.5 | primitive | relative to a basis, the probability of a claim is a number from 0 to 1 | MATCH, useful | G-10 | in Part 2 (r3, tier P) |
| 8 | `y▸` | F3.3 | definable | the method was triggered before the time and is not completed | PARTIAL, misleading | G-09 | not entered: C7 and C8 serve |
| 9 | `s⌗` | F1.4 | primitive | the sum over the members of a collection of the quantity (at a time, if given) | MATCH, needed | G-02 | in Part 2 (r3, tier P) |

**The gap report’s seven cards** (`zkCgap-1` to `zkCgap-7`; the report’s section 4). They were written by a second blind session, memory off, from the 21 sentences of Test 2’s production paper. No reader has read them. Six enter in r3 as tier P; `a◇` does not (5.4).

| Card | Word | Family | Kind | Reading | Gap | In this file |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `t◷` | F2.7 | primitive | the time given by an ISO 8601 text | G-01 | in Part 2 (r3, tier P) |
| 2 | `e◷` | F2.7 | primitive | the time at which the event of a claim happens | G-01 | in Part 2 (r3, tier P) |
| 3 | `t≼` | F2.7 | definable | at or before the reference time | G-01 | in Part 2 (r3, tier P) |
| 4 | `l↦` | F2.1 | primitive | the criterion of being a v such that … | G-11 | in Part 2 (r3, tier P) |
| 5 | `∀` | F2.1 | definable | every member of a collection satisfies a claim | G-05 | in Part 2 (r3, tier P) |
| 6 | `b⊤` | F2.4 | definable | x is a best member of a collection under a criterion | G-04 | in Part 2 (r3, tier P) |
| 7 | `a◇` | F2.9 | primitive | who is able to do what | G-17 | not entered: no sentence needs it alone |

---

# PART 4. OPEN GRAMMAR POINTS

These are points of grammar, not missing words (those are in Part 3). Each needs a ruling or a test; this file does not pretend otherwise. Until the Owner rules, the text of Part 1 stands, with the rules marked [r3] as drafted.

| # | Point | State |
| --- | --- | --- |
| P-3 | **Six roots have no signature:** `c⇒ ∴ y⋯ g◎ ? a>` (E-UNSIG). Each needs a signature, or removal from the table. The 30 parked roots stay parked. The gap report proposed the signature `(c:P)->P` for `y⋯` (*still*); it is not taken: `y⋯` is parked, no sentence needed it, and its reading is not fixed. | open |
| P-4 | **An act among joiner claims.** K4 lets an act stand as a claim, so `∧(claim, act)` is accepted today although J2 says operands are of one kind. Keep as it is, or make it E-MIX. | open |
| P-5 | **Roots of one shape, and the † readings.** Form cannot tell roots of one shape apart; the gloss decides, and no root is merged or dropped before blind readers show whether two readers keep neighbours apart. 57 readings are marked †. Whether a marker suits its root (D10) is a reader's `a?`, not a form rule. | open, needs blind tests |
| P-6 | **Where a role marker sits** when a request carries an act: on `r<` or on its inner act. Both are accepted today. | open |
| P-7 | **Whether `s≺` is a time order.** Today it is an order, of claims, acts or items. | open |
| P-8 | **How a question is put to one named agent.** `r<(zkB,…)` asks an agent for an act or information; a question with a named addressee has no settled form. | open |
| P-9 | **Undertaking and declining across messages.** W6 settles one message only. A `d⊖` for an act the sender undertook with `u⊕` earlier (a withdrawal), and a `u⊕` after a `d⊖`, are not defined: which line stands, and whether a withdrawal needs a root of its own. D asked for the difference between refusing and withdrawing. | open, needs a test |
| P-10 | **Which request a `u⊕` or `d⊖` answers.** W7 says: the same act, by its qualified name when the request is in another message. No blind reader has been tested on it yet. | open, needs blind tests |
| P-11 | **Names that last.** Applied in r4 as 1.9.8 (S1 to S6), tier P, from the Owner's proposal of 1 Nov 22:26 and the gap report's version of it. Still open: no session has run it; the line checker reads one message and does not enforce S2 or S4; the wording of S2 (exact restatement, partial acceptance) and S4 (a clash keeps the first) is C's choice and the Owner may change it. | applied as a draft, needs a session test |
| P-12 | **The clock reading, *now*.** Convention C7 (1.13) has the sender declare a clock reading as a time name defined by `t◷`; nothing in the line marks it as the clock reading rather than a deadline. C7b names the time of the message itself with `e◷(m▤(…))` and says *now* without a value that can go stale. The first is what the gap report took from the Owner's answers; the second is its alternative. Neither has been read by a reader. | open |
| P-13 | **The ternary `?⊙`.** The gap report recommends parking it, because the pinned registry checker (c1) rejects it. Checker g3 and the prototype accept it (1.6.2), and no rule of this file marks it open. Left as it is. | open |
| P-14 | **Arithmetic over measured terms inside `✠`.** An average, a share of a collection, a time plus a duration would need `c⌗ m⌗ s⌗` inside `✠( )`, which is E-MATH (M14). The gap report recommends no change for now: `s⌗` covers totals (G-18). | open |
| P-15 | **Shared names with more than two participants.** S5 binds the participants who proposed a name or accepted it. What a third participant who has not accepted may do with a name that two others have bound, and whether a name accepted by one but not by another binds at all, is not settled. | open |
| P-16 | **Refusing a declaration.** There is no form. `r−` takes an agent and an item (`r−(d≔(…))` is E-ARITY), `d⊖` refuses an act, and `a.` says only *received, not agreed*. The profile says to send an alternative as a new proposal. A root for refusing a declaration is possible; none is proposed. | open |
| P-17 | **Claims under a scaffold.** N4 of this file lets a scaffold define a name of any class except `zt zE zU`. The Sustained-Conversation Profile (U-31, accepted by the Owner on 31 October for the profile) allows scaffolds for referent names only, and writes claims in roots. r4 keeps both and follows the profile in its examples. The Owner was asked in the chat of 1 Nov, after his proposal of 22:26, whether a claim may also be named by a scaffold; he has not answered. | open, the Owner's call |

**Ruled by the Owner, so not open:**
- A root with an act shape listed first and a claim shape (`c■ d↦ v✓`), alone on a line, stays E-LINE (1 Nov 07:24).
- The placeholder is `n0` (1 Nov 07:29).
- **D6** (a role marker never fills a core place) and **D7** (`m▤` and `r>` take no details) stand as rules (1 Nov 14:23). They were P-1 and P-2 of SPEC DRAFT r1. The Owner asked whether they cost anything; the answer was that D6 refuses 28 meaningless lines and D7 88 lines of the test set, and that the Test 2 record shows no line refused by either (its refusals were E-CAT and E-MIX).

---

# PART 5. RULINGS, EVIDENCE AND RECORD

## 5.1 Rulings of the Owner that the text rests on

The Owner's words, shortened, 1 November (India time). Where a rule of Part 1 cites a ruling, it is one of these. The two rows marked *(reported)* are as the gap report states them; their wording is not in the project record.

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
| 12:06 | Gap words will enter, but only after thought. Whether to un-park `l≥` and `pℙ` is left to C (C's decision: they stay parked, G-10). "Decline a request" gets a new root, not a convention. |
| 14:23 | Go ahead on C's proposal: D6 and D7 stand as rules; `u⊕` and `d⊖`, the symbols of Cb2's cards 3 and 4, enter as tier P in a new revision. |
| 20:49 *(reported)* | A name declared in a scaffold and accepted by the other AI should replace the English for the rest of the conversation (P-11). |
| before 21:20 *(reported)* | Four answers given to the gap report: function words only; an ISO 8601 text inside one root; the sender writes absolute times and declares its own clock reading when it needs *now*; a unit goes into the English name of the quantity. |
| 21:52 | (1) The checker fails in places where SILEX itself is fine and compact, for example many declarations in one `d≔`. (2) The checker will change anyway: today's is an intermediate change, a much larger one will come; so do not give it weight, judge how much meaning can be recovered. (3) Where meaning is recovered, the checker is not a concern; the final checker will be quite different. **Build r3: apply the rules that the blind gap report proposed, and leave out any that has a problem.** |
| 22:26 | A proposal. For sustained AI-to-AI conversation the first message carries declarations with scaffolds (`zm1`, `zS4`, …); the other AI answers with an acceptance, a rejection or *not understood*; once accepted, the two use the names alone for the rest of the session, without English. His example: two AIs on a critical mathematics problem, with shared names for *the curvature of the parabola* and for *two tangents drawn to the parabola are orthogonal*. |
| 22:34, 22:37 | Questions: can proper nouns (the names of people, places, agents) be handled, and kind words (*circle*, *triangle*, *tangent*)? (C answered in the chat: yes, as scaffolds of referent names and as criteria; the relation between two things and the equation with letters are gaps, G-22 and G-23.) |
| 22:40 | The proposal is his own; work on it later. |
| 22:45 | Make r4; it will be amended if needed. |

The word of 21:52 is an instruction to build a draft, not a ruling on each word (3.2, step 4). The ten roots are therefore tier P, and every rule they bring is marked [r3]. The words of 22:26 and 22:45 are likewise an instruction to draft: 1.9.8, C23 and C24 are tier P and marked [r4]. The Owner has not ruled on U-31 for this proposal (P-17).

## 5.2 Evidence so far

Test items and answer keys are not part of this file or of the repository. Summary only:

- **Blind test 1** (on grammar r1; four readers, two Claude instances, Gemini, ChatGPT; 72 items): form verdicts 25 of 26 for each of the three readers on the full paper (the one miss, an act-and-claim root alone on a line, is the same for all three and is now ruled, 5.1); readings of 26 lines recovered in full bar one element; 20 of 20 English sentences written as SILEX. A ceiling: the items sat close to the grammar's own examples, and two readers share the author's model family.
- **First reader** (one reader, an earlier text of grammar r3 alone, eight English sentences written as SILEX): all eight messages (26 lines) passed the checker for form. Its own list of what it could not say gave the words marked “first reader” in Part 3.
- **Test 2, first round** (21 ordinary English sentences, three writers): the sentences could not be said in the lexicon. The writers themselves flagged a gap in 18, 16 and 16 of the 21 items. These gaps are the evidence of Part 3. Stage 2 was not run on that set.
- **Test 2, second round** (18 simple one-relation sentences, three writers, five blind readings): every writer's SILEX passed the checker bar one stray plain-English line (17 of 18 for one writer as written); the five readings recovered at least 97% of the key elements, two scorers agreeing on all but 4 of 245 judgments, no contradiction. Different encodings of one sentence were each read correctly. A ceiling again: it shows a floor, not capacity. The roots carried force, negation, cause, questions and requests; the scaffolds carried every predicate. "Decline a request" was the least stable item (G-13).
- **OPEN BUILD, D's blind reading of Cb2's nine cards** (one reader, from cards stripped of the author's description; then 16 held-out lines read and 11 sentences written): seven of the nine words matched the author's gloss. D rated `u⊕` and `d⊖` NEEDED and asked three things: what `u⊕` binds, whether the reason of `d⊖` is asserted, and refusing against withdrawing. The first two are answered in 1.9.7; the third is P-9. D's verdicts on the other seven are in 3.4. A ceiling: one reader, one run, one model family, a key written by C, and write items close in shape to the card examples.
- **The gap report** (one blind Claude session, memory off, given the 197-root grammar and the 21 sentences of Test 2's production paper; no reader took part). It wrote the 21 sentences twice, with the 197 roots and with its proposals, and listed 46 places where the sentences meet a gap. By its own count the proposals cut the English kept in scaffolds by 13% (1,108 to 966 characters) and make the messages 3.0% longer; 21 of the 46 places are carried by a new root, 19 by a convention, 6 stay English. A partial review by a second reader, stopped early, graded 9 sentences as carried with small differences, 9 with a material shift and 3 not well. The report says of itself that the encodings are its own, the measure counts English and not meaning, and the sample is small. It ran no exchange between two AIs.
- **C's check of the gap report** (1 Nov, evening): its characters, checksums and time-text tests were re-run (`timelit.py`, 227 cases, none fails); the 21 encodings with the new roots were run on the prototype checker (5.3). C found two differences: the report says its Cb2 cards are unchanged, but its copies of cards 2 and 7 differ from the project record (three examples instead of four, and some paragraphs missing), so r3 follows the project record; and its base checker lacks D7 (83 of 18,319 lines differ), which does not affect its results. Meaning was not tested: no reader has seen any of the ten roots in use.
- **Probes of 1 Nov, 22:26 to 22:37** (C, on the prototype checker of r3; not a reader test): the lines `p↗(d≔(…))`, `a=(d≔(…))` and `a?(d≔(…))` pass; `r−` with a declaration is E-ARITY; a name used in a later message without a declaration passes as its class only (N5); scaffolds for a person, a place and an agent pass, in Latin and in Bengali script; a time name takes no scaffold (E-DEF); a claim put under a collection name is E-CAT; a free letter in a value claim is E-FREE. They show that the form is there and that the one thing missing is how long a name lasts (1.9.8).

A pass of the checker shows form, not shared meaning. Only blind readers can show that.

## 5.3 Verification of this file

r4 adds no root and changes neither the table nor the prototype checker (same SHA-256, 5.5). The rows below about the 207-entry table, the 18,319-line comparison, the cards and the 21 encodings are those of r3, unchanged. The counts of lines and gaps are those of this file.

| Check | Result |
| --- | --- |
| Every `silex` line of Part 1, run on the prototype `ucl_check.py` with the 207-entry table | 221 of 221 lines give the verdict printed beside them, warnings included (blocks: 45) |
| The 207 roots of Part 2 | 207 rows in 25 family tables, each root once |
| Tiers counted from Part 2 | E 40, Ep 26, P 109, U 31 (29 parked, plus `m▤` and `r>` “core by use”: 2), X 1; core 68, trial 109, parked 30; 57 readings marked † |
| Every gap of Part 3 appears once in Part 2 and once in Part 3 | 23 gaps in 11 families, each once in each place |
| Lines of Part 3 said to pass or fail the checker (marked ✔) | 34 of 34 give the stated result on the prototype checker (the 30 of r3, unchanged, and the 4 of G-22 and G-23) |
| The prototype with the 207-entry table against g3 with the 197-entry table, on the test set of 18,319 lines of r2 (the regression lines, the rulebook's example lines, and their mutations: a marker appended, an argument replaced or dropped or doubled) | 18,319 lines give the same verdict, kind, basis and warning codes: the new roots and rules change none of the old verdicts. The test set is not in the repository |
| Examples and non-examples of the cards of the ten roots (Cb2's cards 1, 2, 7, 9 as the project record has them; the gap report's cards 1 to 6), run on the prototype | 78 of 78 give the result the card states |
| The 21 encodings of the gap report that use the new roots, run on the prototype | 105 lines, 0 failures. The sentences and their encodings are test material and are not in this file or the repository |
| `timelit.py`, the check of a time text | byte-identical to the gap report's file; its 227 cases pass |

Not checked by a tool: that the prose of Part 1 says what the checker does, and that a convention says what it is meant to say. The rules S2 to S6, W1 to W7 and M9, M11, M12, M15, M16 and M17 (in part) are rules for the reader and no tool tests them. `silex_check_g3.py`, the separate line checker of the snapshot, does not know the ten new roots and was not run on them. Nothing here shows that two readers recover the same meaning from the new lines; that is the blind test of 3.2, step 6, and it has not been run.

## 5.4 What differs

**From SPEC DRAFT r3.**

1. No root enters. Part 2 has the same 207 roots, trial 109; core (68) and parked (30) are as before. The table and the prototype checker are those of r3.
2. Part 1: the new section 1.9.8 (S1 to S6). Changed, each marked [r4]: N5, N6, one sentence of 1.9.6. Part 1.13 gains C23 (proper names) and C24 (kinds).
3. Part 3: G-22 (a named relation between two things) and G-23 (a claim with free letters) are new.
4. Part 4: P-11 is applied as a draft; P-15 (more than two participants), P-16 (refusing a declaration) and P-17 (claims under a scaffold) are new.
5. Part 5: four rows in 5.1, one bullet in 5.2, this list and the new files in 5.5.
6. Corrected: the Date row of r3 read 2026-12-01 by mistake, because an example date was substituted for it. It is 2026-11-01. Nothing else of r3 is wrong for this reason: the other dates changed in r3 are example dates inside lines.

**From SPEC DRAFT r2 to r3** (unchanged from the r3 text).

1. Ten roots enter, tier P: `c⌗ m⌗ s⌗` (F1.4), `l↦ ∀` (F2.1), `b⊤` (F2.4), `p◑` (F2.5), `t◷ e◷ t≼` (F2.7). Part 2 has 207 roots, trial 109; core (68) and parked (30) are as before.
2. Part 1: new rules M5 to M17 and the conventions of 1.13. Changed, each marked [r3]: T2 (207), T6 (time text), K3 (the list of multi-signature roots gains `c⌗ m⌗ s⌗`, and `d⊖`, which r2 omitted), D4 and N1 (the joiners and `d≔` take as many operands as they list; stated, not new), D8, V1, V2, V3, N3, M1, M2, M4, the text of 1.8.3, the table of 1.12 (E-TIME, TZ), the counts in 1.10. The `c↓` reading changes (M12).
3. Part 3: the register states change for G-01 to G-05, G-08 to G-11, G-15, G-16; G-18 to G-21 are new; 3.4 lists the seven words of the gap report as well as Cb2's nine, with what became of each.
4. Part 4: P-3 says why `y⋯` gets no signature; P-11 to P-14 are new.
5. Part 5: three rows in 5.1, two bullets in 5.2, new rows in 5.3, this list, the new files in 5.5.
6. The header and the name.

**Left out of the gap report, and why.**

1. `a◇` (*able to*): no sentence needs it alone, and nobody has read it. Inability stays G-17.
2. `b≬` (*between*): D read it as redundant. *About* (C20) is written with two denials.
3. `f⊂`: not added. `c↓` is read as exactly the members that meet the criterion (M12), as the report proposes in its ruling R1.
4. `y▸`: D read it as misleading. *Not yet* is C7.
5. The signature for `y⋯` (the report's ruling R2): see P-3.
6. Conventions C11 (*probably* as `h◇`, *certainly* as `⊛`) and C12 (*should* as `r□`): `h◇` says *as a hypothesis* and `r□` says a requirement, so each says something other than the word (G-10, G-21). C13 is changed: *withdraw* as `r↻` is dropped (P-9), *rephrase* is added with *differently* not said. C20 uses the long form without `b≬`.
7. The report's proposal for names that last (P-11): not applied; the proposal is in Part 4. Its question 13 (`?⊙`) and question 14 (arithmetic inside `✠`) change nothing (P-13, P-14).

The reword of V3, which lets `∃` or `∀` stand inside a question, is applied: g3 already accepts it, so the rule now says what the checker does. From the report's list of rule changes, these are applied: a `zE` variable in a question or a quantifier (its P-V1) is V2, the binder list (P-V2) is V1, the definition of a time name (P-N3) is N3, and the error and warning for time text (P-E1) are in 1.12. Its ruling R1 is M12 and its ruling R3 is M9.

**From SPEC DRAFT r1, grammar r3 and rulebook r3** see 5.4 of SPEC DRAFT r2; nothing there is undone.

## 5.5 Files

| File | SHA-256 |
| --- | --- |
| `SILEX-195-SPEC-DRAFT-r3.md` (the draft this one follows) | `93d448ef95d11c7947df0d640d79f0eda301ceff1ba52f72db9134972fc088e5` |
| `SILEX-195-SPEC-DRAFT-r2.md` | `7a529f7a465229629f22eab1db889a10900c866da36ff793c931b8f8a9743ba0` |
| `REPORT.md` of `SILEX-GAP-r1` (the gap report) | `5a79dad149e9e82d2ab6ea64db102fd5788f1a41c933b00d625fcff7c8da93a8` |
| `timelit.py` (the same bytes as the gap report's) | `bf057e32f485aa754f8123ef7021694f2e622ba84b80baf7ef916a0d6d29a99b` |
| `ucl_check.py` (the prototype: g3 with the rule changes of the gap report) | `c30ef121fca65200199c0f89db6a0d248ce55dc9b6f2540b0972a0fb60858129` |
| `data_table.json` (r3 table, 207 entries: the r2 table plus the ten roots) | `4d0c725a131c9cb354492d8986d55dce31bc03420d0a30f6034bcd83cfb2e522` |
| `SILEX-195-SPEC-DRAFT-r1.md` | `094bcdb38b6be7046c5d4690643f2fe64c0d626573012719eac238506731441f` |
| `SILEX-GRAMMAR-C-r3.md` | `723229b3c2c5442efbbe80a26594e72e702b67931bba87babf0b4c5b29916d7e` |
| `SILEX-RULEBOOK-r3.md` | `0573a32c3e9d71df12d94bbc4655c74562f8281dc0a86d12260ee5a286d4984b` |
| `ucl_check.py` (g3) | `3ec4e639fc9bda9de5293af87f636d7f2e1086bd5dc4e9758a9c8ba058bbf484` |
| `data_table.json` (n0 table, 195 entries) | `d144c3830d4221500fd9a87f25d2050948de72449f00bc4b3fbcbb13d6e24e94` |
| `data_table.json` (r2 table, 197 entries) | `3dd116b009c13b37aff91011e4c0f4c496b8eefd87701cb2e1b05e9c75799e35` |
| `silex_check_g3.py` | `09486de038dce9510c1a1c1dc158ca3557ae8554c8c790d95d484757dcfd18df` |

In the repository, the prototype checker, `timelit.py` and the 207-entry table are in `tools/` of the folder of SPEC DRAFT r3 (r4 has no tools of its own and changes none); the grammar, the rulebook, g3, the 195-entry table and `silex_check_g3.py` are in `drafts/SILEX-195-SNAPSHOT-001/`; SPEC DRAFT r1, r2 and r3 are in their own folders, r2 with its 197-entry table. To run the line checker on Part 1, put the three files of `tools/` in one folder. A SHA-256 identifies the bytes of a file. It does not make the file authoritative.

---

End of SILEX-195 SPEC DRAFT r4. Not adopted. Not frozen. No checksum record.
