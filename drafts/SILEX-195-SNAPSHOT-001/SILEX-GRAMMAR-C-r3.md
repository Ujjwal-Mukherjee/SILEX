# SILEX Grammar (candidate r3)

Nov 1, 2026 · written by C for the Owner · candidate, not adopted, not frozen · r2 followed blind test 1 on r1; r3 writes the placeholder as `n0`, by the Owner's ruling of 1 Nov 07:29 (§7, §14)

**What this is.** The grammar of the 195-root language as it stands in `SILEX-RULEBOOK-r3` and the table with `n0` as the placeholder, written once and in order: tokens, kinds, application, details, joiners and binders, names, `n0`, time and number, lines and force, evidence. It adds no root and renames none. Where the rulebook and the checker left a rule implicit, it is stated here; where I think a rule should change, the change is marked **◆** and listed in section 13 with the exact checker edit. Everything else restates what the pinned or candidate checker already does.

**How it is tested.** Every SILEX line printed below carries its verdict after `# ` and was run through the checker (section 14): `ok` for a line that passes, `ok NU` for one that passes with that warning (section 12), `E-ARITY` and the like for a line that is refused. The lexicon of Appendix A is generated from the table, not typed.

**What it does not do.** It does not say that two readers take the same meaning from a line; only blind readers can show that. It does not repeat the conversation rules of the Sustained-Conversation Profile (CP-1 to CP-17), which are policy for sessions and sit on top of this grammar.

---

## 0. The language on one screen

SILEX is written as nested applications of roots. Every expression has one shape:

```
expression  =  root ( expression , expression , … )
            |  name  |  atom  |  n0    |  ⌜ mention ⌝  |  ✠( math )  |  agent : expression
line        =  one expression, of a kind that can stand as a line (§9)
```

Seven laws carry the rest.

1. **One shape.** There is no infix, no precedence, no punctuation but `( ) , :` and the two mention brackets. A root is followed at once by `(`; the six atoms stand bare.
2. **Places have kinds.** A root lists its places in order and the kind each one wants. A name of that kind fills the place; so does any root that makes that kind (§3).
3. **Details follow the core.** After its core places a root may take role markers, optional, unordered, each at most once, eight arguments in all; a role not given may be written `n0` (§5).
4. **Content is not force.** A claim is not asserted by being written. Only a force root or a dialogue act turns a claim into a line (§9).
5. **Names are opaque.** A name means its class and nothing else. English occurs only inside `⌜ ⌝`, as a scaffold, and is never part of the language (§1).
6. **Not supplied is not none.** `n0` marks a place or a role that was not supplied. It is not zero, not none, not unknown, and it is not a claim about a data field (§7). The word `null` is no longer read.
7. **A pass is form.** The checker certifies form, kinds and evidence level (§10). Whether two readers agree on meaning is a separate, empirical question (§11).

A whole message, read in English beside it:

```silex
m▤(zUa1,zkA)                          # ok
d≔(zo9,⌜the signed contract file⌝)    # ok SCAFFOLD
d≔(zcr1,⌜the published checksum⌝)     # ok SCAFFOLD
d≔(zq1,v⊨(zo9,zcr1))                  # ok
h◇(zq1)                               # ok
```

*Message zUa1 from zkA. Let zo9 stand for “the signed contract file”, zcr1 for “the published checksum”, and zq1 for “zo9 satisfies zcr1”. As a hypothesis: zq1.* Nothing is asserted, no English is part of the language, and each name carries only its class.

---

## 1. Tokens

| # | Rule |
| --- | --- |
| **T1** | A line is one expression. Spaces and tabs may surround any argument; a root and its `(` are written together. In a file, a `#` standing alone between spaces, or at the start of a line, opens a comment to the end of the line; the root `#` is always followed by `(`. |
| **T2** | **Roots.** The 195 symbols of the table. The reader takes the longest root that matches (`s@*` before `s@`). A root with places is followed at once by `(`. The atoms are `t 0 ⊤ x w n`; they take no `(`. |
| **T3** | **Names.** `z`, a class prefix, then letters and digits. The prefix is the class and the whole meaning (table below). A name is never applied: no `(` follows it. Names are opaque and need not be declared, except a time name (N5). |
| **T4** | **`n0`.** The two characters `n0`, when no letter, digit or `(` follows them. The word `null` is not read (E-SYNTAX). |
| **T5** | **Mention.** `⌜ … ⌝`, nestable. If the inside is SILEX it is read as SILEX, otherwise as raw English. A mention remembers what it mentions (§3). |
| **T6** | **Math term.** `✠(` … `)`. The inside is the math sublanguage of §8. |
| **T7** | **Attribution.** An agent name, a colon, then an expression: `zkB:∈(zo1,zS1)` is a claim attributed to `zkB`; before a force root (§9) it gives a line attributed to `zkB`. Only `zk` names may precede the colon. |
| **T8** | A token that is none of these is E-LEX. A name without a class prefix is E-LEX. |

**Name classes.**

| Prefix | Kind | Prefix | Kind |
| --- | --- | --- | --- |
| `zk` | agent (`Ag`) | `zS` | collection (`Co`) |
| `zo` | object, an item (`Ob`) | `zE` | math term (`Ex`) |
| `zv` | value (`Va`) | `zt` | time (`Tm`) |
| `zm` | method or act name (`Me`) | `zU` | message name (`Ms`) |
| `zcr` | criterion (`Cr`) | `zp zq zr zh` | claim (`P`) |

A variable is not a separate class: it is a name of class `zk zm zo zv zS` that a binder binds (§6).

```silex
g←(zkB:∈(zo1,zS1))        # ok
zkB:g←(∈(zo1,zS1))        # ok
g←( zq1 )                 # ok
g← (zq1)                  # E-SYNTAX
g←(zx1)                   # E-LEX
```

---

## 2. The lexicon in 25 families

Every root belongs to one family. *Core* is status E or Ep, plus the header and the answer link; *trial* is status P; *parked* is held back (§10). Appendix A gives each root's shape and reading.

| Family | Roots | Core | Trial | Parked |
| --- | --- | --- | --- | --- |
| 0.1 Application, names and definition | 1 | `d≔` | — | — |
| 0.2 Mention and attribution | 1 | `⌜ ⌝` | — | — |
| 0.3 Atoms and placeholders | 6 | `t` `0` | — | `⊤` `x` `w` `n` |
| 1.1 Collections and selection | 10 | — | `g∪` `i+` `e−` `a/` `c↓` `s∃` `s⊙` `k▤` `b▁` | `f∃` |
| 1.2 Items, data and transformations | 12 | `⧉` | `d▤` `i▤` `f▦` `fƒ` `g↦` `i↦` `m↻` `o←` `s↦` `u↻` `e⚖` | — |
| 1.3 Methods, processes and tasks | 3 | — | `m▦` `p▷` `t▦` | — |
| 1.4 Quantity and mathematics | 4 | `✠` `#` | `c∑` `dΔ` | — |
| 2.1 Logical core: negation, joining, quantification, implication, context | 8 | `n¬` `∧` `a\|` `∃` `i→` `i⇒` `c⊃` | — | `c⇒` |
| 2.2 Reasons, support, inference and evidence | 12 | `s∵` `d⊢` | `∵` `r∵` `j∵` `e∵` `l⊢` | `c∴` `∴` `i⊢` `p⊢` `e▤` |
| 2.3 Causation, condition, constraint and necessity | 4 | `c↝` | `l⊣` `n□` | `c⊣` |
| 2.4 Sameness, difference, comparison and order | 16 | `s=` `i≡` `m>` | `r≡` `c≡` `c≠` `d≠` `b≻` `≈` `o≺` `v=` `m∥` `n−` | `s≈` `m≡` `d≢` |
| 2.5 Epistemic status, verification, probability and absence | 13 | `v⊨` `n0` | `f⊥` `✓` `✗` `r✓` `s✓` `p⇢` | `f⊤` `k✓` `u±` `l≥` `pℙ` |
| 2.6 Provenance and reference | 5 | `s@` `s@*` `r@` `⊛` | — | `r:` |
| 2.7 Time and sequence | 9 | `t≺` `t●` `t▷` `s≺` | `b₀` `s◷` `s▷` | `▷` `y⋯` |
| 2.8 Structure, description, classification and relation | 18 | `∈` `⊡` | `e∈` `o\|` `c◉` `d⋮` `p▦` `s▦` `s⊞` `m⊞` `m↦` `k#` `l↔` `↔` `r∩` `s≔` `p?` `i←` | — |
| 2.9 Agents: holding, attitude and interaction states | 15 | `h⊡` | `b~` `t~` `i◎` `o◎` `n!` `r−` `g▷` `f▷` `h+` `s◇` `f↩` `o▤` `u✓` | `g◎` |
| 3.1 Action constructors and role markers | 10 | `cƒ` `o→` `a+` `⌘` `⚙` `↣` `☞` `☼` `⚓` `♙` | — | — |
| 3.2 Act verbs | 11 | — | `c?` `c≶` `e⋯` `i?` `t⋯` `u↦` `l↻` `i↑` `t⚖` `a<` | `q<` |
| 3.3 Execution, completion, retry, decision and result | 8 | `▶` `c■` `⤿` `d↦` `v✓` `r→` | — | `d⊙` `c✓` |
| 3.4 Directives and requirements | 3 | `i!` `r<` `r□` | — | — |
| 4.1 Question formers | 7 | `?=` `?⊤` | `?◷` `?@` `?⊙` `?∵` | `?` |
| 4.2 Answer forms | 3 | — | `y✓` | `n⊘` `a>` |
| 5.1 Status force | 5 | `g←` `h◇` `p◇` `u?` `u~` | — | — |
| 5.2 Dialogue acts | 8 | `a.` `a=` `a?` `p↗` `e✗` `r↻` `~` | `p▁` | — |
| 6.1 Messages: identity, transmission and answer links | 3 | `m▤` `r>` | `r←` | — |

A signature is written `root : K₁, K₂, … → R`: the kinds of the core places in order, then the kind the root makes. `v⊨ : Ref, Cr → P` says that `v⊨` takes an item and a criterion and makes a claim. Appendix A prints the shapes in words.

---

## 3. Kinds

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

"Item" in the rulebook's English readings means `Ref`.

| # | Rule |
| --- | --- |
| **K1** | A place of kind `K` accepts an expression of kind `K` or any subkind. A place written `K\|L` accepts either. A place of kind `Any` accepts every kind except a role marker **[◆1]**. |
| **K2** | `n0` fits every place (§7). |
| **K3** | A root with several signatures (`m▤ r> h◇ p◇ u? u~ c■ d↦ v✓ i⇒ c⊃ r□ ~ m> r@ ∃`) is read by the place it stands in: the first signature whose result fits the kind expected there. At the top of a line, the first that checks. |
| **K4** | **Lifting.** Where a claim is expected and an act stands, the act is read as the claim *an act of this kind occurs*. It is not asserted. Its evidence level is E for `cƒ o→ a+` and N for every other act. |
| **K5** | A mention has the kind of what it mentions when that is a question, a line, a claim or an act (`Mn[Q]`, `Mn[Ln]`, `Mn[P]`, `Mn[Act]`), and plain `Mn` otherwise. |

```silex
g←(▶(zm1))                # ok
?⊤(c■(▶(zm1)))            # ok
d↦(zv1,zo1)               # E-LINE
g←(d↦(zv1,zo1))           # ok
```

*The first line lifts the act `▶(zm1)` to the claim that it is triggered; the second asks whether the completion of that run holds. The third stands alone on a line, where K3 takes the first signature that checks, the act `d↦` (Appendix A lists the act first): an act alone is not a line. Under a force root the claim shape fits, as in the fourth.*

---

## 4. Application

| # | Rule |
| --- | --- |
| **A1** | `r(e₁,…,eₙ)` applies root `r` to `n` arguments. `n` must equal the number of core places in the chosen signature (E-ARITY), except where §5 and §6 say otherwise. |
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

Signatures are in Appendix A. Roots that share a shape cannot be told apart by form: there only the gloss decides, and a reader takes a root as written and never reads a neighbour into it.

```silex
g←(v⊨(zo1,zcr1))          # ok
g←(v⊨(zo1))               # E-ARITY
g←(v⊨(zo1,zS1))           # E-CAT
```

---

## 5. Details

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
| **D5** | A detail is a role marker or `n0`. After the core places `n0` stands for a role that was not given (B-18, B-19, ruled 1 Nov 01:57). It counts toward the eight, means the same as leaving the role out, and prints no warning. In an action root, where the roles belong to the signature, and inside a marker (`⚓(n0)`), it prints NU. |
| **D6** | **[◆1]** A role marker stands only as a detail or, in the three action roots, as a role. It never fills a core place. |
| **D7** | **[◆2]** The protocol roots `m▤` and `r>` take no details. |
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

---

## 6. Roots with their own form

### 6.1 Joiners `∧  a|  s≺`

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

### 6.2 Binders `∃  ?=  ?⊙`

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

### 6.3 Reference `r@`

`r@` has two uses, told apart by the kind of its second argument. `r@(x,y)`, with `y` an item, is a pointer from `x` to `y` (a claim; not provenance, which is `s@`). `r@(x,zUk)`, with `zUk` a message name, is the qualified reference *x as it stands in message zUk*; it has the kind of `x`, and `x` may be a claim or an item. `r@` takes no details.

```silex
g←(c↝(r@(zq1,zUa1),zq2))                        # ok
```

### 6.4 Names and declarations `d≔`

| # | Rule |
| --- | --- |
| **N1** | `d≔(n₁,…,nₖ,def₁,…,defₖ)` declares `k` names and then gives their `k` definitions in the same order. An odd number of arguments is E-ARITY. A definition may use a name declared earlier in the same line. |
| **N2** | The first half are names (E-DEF). A name already declared in the message is E-REDECL, whether it was declared by an earlier line or earlier in the same line. |
| **N3** | The class decides what may be defined: `zp zq zr zh` a claim; `zm` an act or method; `zo` an item; `zv` a value; `zS` a collection; `zk` an agent; `zcr` a criterion; `zE` a `✠` term or another `zE` name; `zt` only the atom `t` or an imported qualified time. A `zU` name is declared only by the header (E-DEF). |
| **N4** | A definition that is quoted English is a scaffold (warning SCAFFOLD): it fixes nothing in SILEX and gives the reader English to go on. A scaffold may define a name of any class except `zt`, `zE` and `zU`. |
| **N5** | A name that is used but not declared means only its class. This is allowed for every class except `zt`: a time name must be declared first (E-UNDECL). |
| **N6** | Names are local to their message, with one exception, the roster names: a `zk` name that is the sender in a header means that participant in every message (B-25). So `zkA` in `m▤(zUa1,zkA)` is the same agent in every message of the session. |

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

---

## 7. `n0`

| # | Rule |
| --- | --- |
| **Z1** | `n0` means *not supplied*. It is not none, not zero, not unknown. |
| **Z2** | It fits any **core** place and prints the warning NU. A claim with `n0` in a core place is incomplete: a reader marks it `a?` when it stands under `n¬`, `i→` or `?⊤`. After the core places it is a detail not given (D5). |
| **Z3** | `n0` is not a joiner operand (E-NULL), not a line (E-LINE), not the name in `d≔` (E-DEF), not a bound variable (E-BIND). |
| **Z4** | `n0` is an atom of the table (family 2.5, status E): no arguments, no kind of its own. It replaces the word `null` (Owner ruling, 1 Nov 07:29), which is not read any more (E-SYNTAX). `n0(zo1)` is E-ARITY. The table's former `n0(P,Q)`, *the field P has no value in Q*, is withdrawn from the glyph (OP-14). |

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

---

## 8. Time, criteria, number

### 8.1 Time

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

### 8.2 Criteria

A criterion is a declared `zcr` name. Sameness roots `s= s≈ m≡ d≢` are relative to one; with none in context they warn CR (underspecified). A criterion is supplied by `c⊃(zcr,φ)`.

```silex
g←(c⊃(zcr1,s=(zo1,zo2)))                        # ok
g←(s=(zo1,zo2))                                 # ok CR
```

### 8.3 Number

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

---

## 9. Lines, force, dialogue

**9.1 A line.** A line is an expression of kind Ln, Dir, CDir, Req, Dc, Q or Cx. A bare claim is accepted as a line with the warning FU (force unspecified): write the force. Any other kind is E-LINE. This includes a root that has an act shape and a claim shape with the act listed first (`c■ d↦ v✓`, Appendix A): alone on a line it is read as its act (K3), so it is E-LINE. Put it under a force root (`g←(c■(zm3))`) or a directive (`i!(c■(zm3))`).

```silex
g←(∈(zo1,zS1))                                  # ok
∈(zo1,zS1)                                      # ok FU
▶(zm1)                                          # E-LINE
i!(▶(zm1))                                      # ok
i⇒(zq1,i!(▶(zm1)))                              # ok
r□(n¬(zq1))                                     # ok
```

**Order and assumptions.** Line order has no meaning of its own. The grammar uses it for two things only: the header comes first (9.2) and a name is declared before it is used where N1 and N5 ask. "Then" between acts is written with `s≺` (J2), not with the order of lines. A line `~(P)` is a line of kind Cx; the checker keeps no scope for it and later lines are checked as if it were absent. To tie an assumption to a claim, give it as the context: `c⊃(~(P),Q)` (M4).

```silex
g←(s≺(▶(zm1),▶(zm2)))                           # ok
~(zq1)                                          # ok
g←(c⊃(~(zq1),zq2))                              # ok
```

**9.2 Message.** A message is a header `m▤(zUk,zkX)` followed by lines. The header is the first line and occurs once (E-HEADER). Separator lines such as `=== zUa1 zkA ===` belong to the session file, not to the language. The header names the sender only. An addressee is named inside a line: `r<(zkB,…)` asks `zkB`, and `↣` marks a recipient (§5). `m▤` with three arguments, `m▤(zkP,zkQ,zoR)`, is not a header but a claim, *the message R from P to Q*; it is an ordinary line (FU when bare), and a header written after it is E-HEADER.

```silex
m▤(zkA,zkB,zo1)                                 # ok FU
m▤(zUa1,zkA)                                    # E-HEADER
```

**9.3 Force.** A claim is put to use by one of five force roots; none verifies:

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

**9.4 Dialogue acts.**

| Root | Reading | Root | Reading |
| --- | --- | --- | --- |
| `a.` | received (not agreed) | `e✗` | error in |
| `a=` | agreed (a claim or a declaration) | `r↻` | revised |
| `a?` | unclear | `p▁` | taken as a starting point |
| `p↗` | proposed, not adopted | `~` | assume |

**9.5 Directives and requirements.** `i!(act)` do it; `r<(zkB,act)` ask `zkB` to do it; `r□(P)` it is required that `P`. A conditional request is `i⇒(P,i!(act))`, and the act of `i⇒` may be a request: `i⇒(P,r<(zkB,act))`. A named method is itself an act, so `zm1` and `▶(zm1)` both fill an act place; this file writes `▶(zm1)` where the running of the method is meant.

```silex
r<(zkB,zm1)                                     # ok
i!(▶(zm1))                                      # ok
i⇒(zq1,r<(zkB,▶(zm2)))                          # ok
```

**9.6 Questions and answers.** `?⊤(P)` is answered in exactly one of three ways, `g←(P)`, `g←(n¬(P))`, `u?(P)`. `?=` and `?⊙` ask for a value. There is one answer per question, and a question with no target is marked `a?` (B-36). An answer is given by the answer link `r>(zUk,⌜Q⌝,W)`: it answers question `Q` of message `zUk`, and `W` is exactly `g←(A)` or `u?(A)` (E-FORCE). Names are local to their message (N6), so the answering message does not share names with the question's message. Inside an answer, `zq1` is the answerer's own name; the claim as it stands in the question's message is written `r@(zq1,zUk)`. Both forms pass the form check. Use `r@` when the answer must be about the question's own claim.

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

---

## 10. Evidence

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

---

## 11. Reading, and what a pass shows

A root's **reading** is the English pattern in Appendix A. A name is read as the English of its scaffold, or as its class when there is none. A pattern marked † is the rulebook's inference from the gloss, not a reading the table gives; it is not to be relied on until it is ruled on. A reader who meets a line outside the rules, or one it cannot resolve, marks it `a?` and does not guess (B-37).

**Form and use are separate.** The form check applies the signature of every root that has one, whatever its status, so a line with a parked root that has a signature is well formed. Use is the reader's: a reader who meets a parked root, a root without a signature, or an incomplete claim (`n0` in a core place) marks `a?`. A † reading is a guess, not a refusal: the reader gives it and marks it †.

```silex
g←(s≈(zo1,zo2))                                 # ok CR
```

A pass certifies the checks of this grammar and nothing more: places, kinds, declared names, details, joiners, binders, time, number, evidence level. It does not show that the line says what its writer meant, nor that two readers recover the same meaning. That is shown only by blind reading, one line at a time, with the writer's intended meaning kept apart from the reader's recovered meaning.

---

## 12. Diagnostics

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
| E-LINE | 9.1 | an expression that cannot be a line |
| E-HEADER | 9.2 | a header that is not first, or is repeated |
| E-FORCE | 9.6 | the third operand of `r>` is not `g←` or `u?` |
| E-KIND | M3 | a tense over a negation of a non-state predicate |
| E-ATTR | 8.3 | attribution before a value claim or comparison |
| E-ATEMP | 8.3 | a value claim under a tense or time context |
| E-MATH · E-MATHPLACE · E-FREE · E-UNDEFVAL | 8.3 | a bad math term; `✠` out of place; a free letter; an undefined value |
| NU · FU · RT · CR · SCAFFOLD | Z2 · 9.1 · M2 · 8.2 · N4 | warnings: n0 supplied; force unspecified; reference time missing; criterion missing; quoted English |

---

## 13. Changes proposed in this grammar, and what stays open

Two changes, each small, each stated as a rule above; ◆2 is also a one-word edit to the candidate checker `ucl_check_rb.py`. None touches a pinned file. The Owner rules on each; until then the rulebook's defaults stand. The checker that every example here ran on, g3, carries the ◆2 edit and the `n0` spelling that the Owner has ruled; the ◆2 edit is still a proposal.

| # | Change | Why | Cost |
| --- | --- | --- | --- |
| **◆1** | **A role marker never fills a core place** (D6, K1). | The pinned checker accepts `a?(♙(zkA))` and the same with `a.`, `e✗`, `r↻` (their argument is `Any`); the candidate refuses it with E-ARITY, by accident of how it strips details. A bare marker means nothing. | No edit. The only point where this grammar is not a superset of the pinned checker: 28 meaningless lines (4 roots × 7 markers). |
| **◆2** | **`m▤` and `r>` take no details** (D7). | Removes C-11: the line checker and the session checker then agree that a header with a detail is refused. The rulebook's default (OP-8) keeps the generic rule B-15 instead, and the session checker then reports no message. | One word in `NO_DETAIL`. Refuses 88 lines of the test set: a header or an answer link with a marker (78) or with `n0` (10). |

**The checker edits.** The ◆2 edit applied to `ucl_check_rb.py` gave `ucl_check_g2.py`, the checker of r1 and r2 of this file. The ruled `n0` spelling, applied on top of it (one tokenizer line and three message texts; in the table `n0` becomes the atom `atom:Null`), gives `ucl_check_g3.py`, the checker that every example in r3 ran on. First edit:

```diff
-NO_DETAIL = ACTION_ROOTS | RMROOTS | {'∧', 'a|', 's≺', '∃', '?=', '?⊙', 'r@', 'd≔'}
+NO_DETAIL = ACTION_ROOTS | RMROOTS | {'∧', 'a|', 's≺', '∃', '?=', '?⊙', 'r@', 'd≔', 'm▤', 'r>'}
```

Second edit, the `n0` spelling:

```diff
-        if s.startswith('null', pos[0]) and (pos[0] + 4 >= len(s) or not (s[pos[0] + 4].isalnum() or s[pos[0] + 4] == '(')):
-            pos[0] += 4; return ('null',)   # RB: null
+        if s.startswith('n0', pos[0]) and (pos[0] + 2 >= len(s) or not (s[pos[0] + 2].isalnum() or s[pos[0] + 2] == '(')):
+            pos[0] += 2; return ('null',)   # G3: n0 is the placeholder (the word null is retired)
```

**Not changed.** `n0` after the core places stays as you ruled it (B-19, 1 Nov 01:57; spelling 07:29). It carries no information, since a role not given may equally be left out (B-18), but it is your rule, so this grammar keeps it. The cost falls on the codec, not on the grammar: `SILEX-CODEC-r2` cannot read such a line back (§14).

**Ruled by the Owner, 1 Nov 07:24.** A root with an act shape listed first and a claim shape (`c■ d↦ v✓`), alone on a line, stays E-LINE (K3, §9.1). Nothing changes.

**Ruled by the Owner, 1 Nov 07:29.** The placeholder is written `n0`, the symbol of the table, and not the word `null` (§7, Z4). The table's `n0` is an atom; its former claim *the field P has no value in Q* is withdrawn from the glyph (OP-14 below). The rulebook is `SILEX-RULEBOOK-r3`, the tools are `ucl_check_g3.py`, `silex_check_g3.py` and `SILEX-CODEC-r2`.

**What stays open.** These need a ruling or symbols, and this grammar does not pretend otherwise. The ids are the rulebook's.

| Open | What is missing |
| --- | --- |
| C-6, OP-3 | roots for numbers with units, clock times, dates and zones; a *when* detail for an act |
| C-7, OP-4 | a criterion builder and a criterion marker |
| C-8, OP-5 | Cb2's nine words, none adopted |
| C-9, OP-9 | a signature for each of the six unsigned roots, or their removal; the 30 parked roots stay parked |
| C-10, OP-7 | an act among joiner claims: K4 lets an act stand as a claim, so `∧(claim, act)` is accepted today |
| OP-14 | the claim the table gave to `n0`, *the field P has no value in Q*: it has no root now. If it is wanted, it needs a root and a symbol of its own |
| OP-2, OP-10, OP-11 | whether a marker suits its root; neighbours of one shape; the 57 † readings |
| codec | `silex2en.py` (`SILEX-CODEC-r2`) has no pattern for `n0` among the details: 3,000 lines of the test set that the checker accepts cannot be read back (§14) |
| found by the reader test (§14) | no root for *send*, *tell*, *approve*; none for a measured *faster than*; no stated scope for a standalone `~`; whether `s≺` is a time order; where a marker sits, on `r<` or on its inner act (both are accepted today); how a question is put to one named agent |

---

## 14. Verification record

| Check | Result |
| --- | --- |
| Every `silex` line above, run on `ucl_check_g3.py` | 93 of 93 lines give the verdict printed beside them, warnings included (r1 had 88, r2 92) |
| **r3, the `n0` spelling.** `ucl_check_g3.py` against `ucl_check_g2.py` on a test set of 18,420 distinct lines (the OPEN BUILD regress lines, the rulebook's example lines, and their mutations: a marker or `null` appended, an argument replaced by `null` or by a marker, an argument dropped or doubled). Each line is run on g2 as it was, and on g3 with every bare `null` rewritten as `n0` | 18,319 lines give the same verdict, kind, basis and warning codes. The other 101 lines contain the old root `n0(…)`; g3 refuses all of them with E-ARITY. The word `null` is E-SYNTAX on g3 |
| `silex_check_g3.py` (the session checker with the g3 pins) | its self-test passes; the six pilot sessions pass layers 1 to 3 |
| `SILEX-CODEC-r2` (`silexlib.py` reads `n0`; `n0` is an atom in `silex_roots.json`; the checker is g3) | its 26 tests pass, failures 0. `g←(s=(n0,zo2))` reads *Supplied: [unspecified is the same as zo2]*; the word `null` is unreadable, as intended |
| `SILEX-RULEBOOK-r3` (the Doc) | sections 7 and 8.2 were regenerated by the rulebook's own script from the changed data; the only differences from r2 are the `n0` lines and the counts they move (established 39 to 40, parked 30 to 29, claim-makers 108 to 107, and the kind table). The inline examples with `n0` give the verdicts the text states |
| The 38 example lines of the rulebook's sections 3 to 6 that state a result (E-CAT, E-MIX, E-NULL, passes, …), run on `ucl_check_g2.py` and on the candidate | all 38 give the stated result, on both |
| `ucl_check_g2.py` against the candidate, on a test set of 31,571 lines: the rulebook's 478 examples, the 81 regress lines, and their mutations (a marker or `null` appended, an argument replaced by `null` or by a marker, an argument dropped or doubled, at every depth) | the candidate accepts 12,924; g2 refuses 88 of them (a detail on `m▤` or `r>`: 78 markers, 10 `null`) and accepts 12,836; no line is newly accepted |
| `ucl_check_g2.py` against the pinned checker, same test set | the pinned checker accepts 361 lines; g2 gives the same verdict, kind, basis and warnings on every one except the 28 lines of ◆1 |
| Lines accepted by g2, read back in exact English and rewritten to SILEX by `SILEX-CODEC-r1` | 9,836 of 12,836 give back the same line. The other 3,000 all have `null` among the details, and the codec has no pattern for them (it stops with "no pattern of the table fits this text"). That is a gap in the codec against B-19, not in the grammar |
| Appendix A | generated from the n0 table and the changed `entries.json`; 195 roots; its only change from r2 is the row of `n0` |
| A first reader, given an earlier text of this file alone, wrote eight English sentences as SILEX messages (ask-and-report, hypothesis, a *which* question, suppose-then, reported speech with a doubt, before a reference time, a requirement, a request with recipient, instrument and basis) | all eight messages (26 lines) pass `ucl_check_g2.py`, so the form rules were enough to write valid lines. The reader's own list of what it could not decide is in the next paragraph |
| **Blind test 1**, on r1: four readers (two Claude instances, Gemini, ChatGPT), each given the grammar and a paper of 72 items, no key. Part A: 26 form verdicts. Part B: 26 SILEX lines read into English. Part C: 20 English sentences written as SILEX | Part A: 25 of 26 for each of the three readers who sat the full paper; the one miss is the same for all three (item A26, a root with an act shape and a claim shape alone on a line; r1 says E-LINE by K3, all three said `ok`). A fourth reader, on a shorter pilot paper, 21 of 21. Part B: every key element recovered by every reader, bar one element missed once ("within the declared time"); two scorers agree. Part C: 20 of 20 for each reader against the key (one reader's C9 used the message-qualified `r@` form, an accepted alternate; one reader named a bound variable differently, which is accepted). **This is a ceiling.** The items sit close to this file's own examples, and two of the four readers share the author's model family. It shows that the form rules can be learned and applied from this text. It does not show shared meaning, and the † readings are inference |

**The rows above that name `ucl_check_g2.py` were measured on r2 of this file, with the word `null`;** they stay as measured. The r3 row shows that rewriting `null` as `n0` changes no verdict.

**What the reader could not decide.** One reader is one sample, and a pass shows form only. The reader's gaps fall in three groups. *Closed in this file:* whether names must be declared (T3), the header's addressee and the three-argument `m▤` (9.2), the meaning of line order and of a standalone `~` (9.1). *Words the lexicon lacks:* *send*, *tell* and *approve* (the reader used `o→` "output" and `a+` "accept"), *faster than* on a measured quantity (the reader used `b≻`, whose reading is †), *but*. These are for the Owner and are listed in section 13. *Choices the gloss must decide* (B-45): `?⊙` or `?=`; `v⊨` or `s✓`; `c⊃(~(P),Q)` or `i→`; `zkB:g←(P)`, `g←(zkB:P)` or `s@` for *B said*; `v✓`, `c?` or `u~` for *checked*.

**What the four readers flagged, and what r2 does about it.** Five points came back in the readers' notes (two of them from both M and D; Claude 2 gave no notes). (1) *A root with an act shape and a claim shape, alone on a line* (`c■`, `d↦`, `v✓`): all three full-paper readers said `ok FU` where K3 gives E-LINE, and two of them (M, D) said K3 was unclear. r2 states the consequence in §9.1; the Owner has ruled that it stays E-LINE (§13), so the rule is not changed. (2) *The E-BIND example in §6.2* fails only because of the line above it; r2 says so. (3) *E-ATEMP on counts* (`m>` on `#`): r2 adds the case in §8.3. (4) *Form against use for parked roots and †*: r2 separates them in §11 (the form check applies every signature; the reader marks `a?` on a parked or unsigned root, and a † reading is given as a guess, not refused). (5) *Names across messages in an answer*, and *B said* against *I supply that B holds*: r2 adds the `r@(zq1,zUk)` form to §9.6 and a three-row table to §9.3. No rule of the grammar changed, and no root.

**Concordance.** The rulebook is answered by number, so here is where each of its rules sits in this file.

| This file | Rulebook |
| --- | --- |
| §1 tokens, §0 laws | B-1, B-19, B-29 |
| §3 kinds | B-2 to B-5, B-44 |
| §4 application | B-1, B-7, B-10 |
| §5 details | B-13 to B-18 |
| §6.1 joiners, §6.2 binders | B-8, B-21; B-9 |
| §6.4 names and declarations | B-23 to B-28 |
| §7 `n0` | B-19 to B-22 |
| §8 time, criteria, number | B-39; B-43; B-38, B-40, B-41 |
| §9 lines, force, dialogue | B-12, B-30 to B-37 |
| §10 evidence | B-10, B-11 |
| §11 reading, Appendix A | B-37, B-45, B-46 |
| §13 | section 9 (C-1 to C-13) and section 10 (OP-1 to OP-14) of the rulebook |

Files used: pinned `ucl_check.py` `5b9823b0…`, table `07a31dec…`, candidate `ucl_check_rb.py` `96785cf8…`, `ucl_check_g2.py` `e420ead4d0fca905…` (r1 and r2 of this file); for r3: `ucl_check_g3.py` `3ec4e639fc9bda9d…`, the n0 table `d144c3830d422150…`, `silex_check_g3.py` `09486de038dce951…`.

---

## Appendix A. The lexicon, 195 roots

Tier: **E** established, **Ep** established with open parts, **P** proposed, **U** parked, **X** excluded, **use** core by use. Shape lists the core places in order, then what the root makes; `(+k)` is the number of details that fit after the core places, within the limit of eight. P, Q, R, … in the reading are the places in order. † marks a reading that the table's gloss does not fix.

**0.1 Application, names and definition**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `d≔` | Ep | P1 … Pk names, then Q1 … Qk definitions (k ≥ 1) → declaration | let the names P stand for the definitions Q |

**0.2 Mention and attribution**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `⌜ ⌝` | E | P any expression → mention | “P” |

**0.3 Atoms and placeholders**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `t` | E | nothing (an atom) → item | a time |
| `0` | E | nothing (an atom) → value | zero |
| `⊤` | U | nothing (an atom) → claim | the true statement |
| `x` | U | nothing (an atom) → item | a placeholder |
| `w` | U | nothing (an atom) → item | a word |
| `n` | U | nothing (an atom) → item | something novel |

**1.1 Collections and selection**

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

**1.2 Items, data and transformations**

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

**1.3 Methods, processes and tasks**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `m▦` | P | P claim, Q act → method (+6) | the procedure that does Q under the condition P † |
| `p▷` | P | P act → method (+7) | the process of P |
| `t▦` | P | P act, Q claim → method (+6) | the task P with the condition Q † |

**1.4 Quantity and mathematics**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `✠` | Ep | P a math expression (numbers and + − × ÷ ^ √ and so on) → math term | the number P |
| `#` | Ep | P collection → count (+7) | the count of P |
| `c∑` | P | P collection, Q method → item (+6) | the total of P by the method Q |
| `dΔ` | P | P item, Q item, R criterion → item (+5) | the difference between P and Q under R |

**2.1 Logical core: negation, joining, quantification, implication, context**

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

**2.2 Reasons, support, inference and evidence**

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

**2.3 Causation, condition, constraint and necessity**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `c↝` | E | P claim, Q claim → claim (+6) | P causes Q |
| `c⊣` | U | P item, Q claim → claim (+6) | P restricts the possibility that Q † |
| `l⊣` | P | P item, Q item → claim (+6) | P is a limit on Q † |
| `n□` | P | P claim, Q claim → claim (+6) | P is required under Q † |

**2.4 Sameness, difference, comparison and order**

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

**2.5 Epistemic status, verification, probability and absence**

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

**2.6 Provenance and reference**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `s@` | E | P claim or item, Q claim or item → claim (+6) | P comes from Q |
| `s@*` | E | P claim or item, Q claim or item → claim (+6) | P descends from Q |
| `r@` | Ep | P claim or item, Q item; or P item, Q message name → claim; or the kind of P | P is found at Q ; P as it stands in the message Q |
| `⊛` | E | P claim → claim (+7) | from stored knowledge, P |
| `r:` | U | P item, Q item, R item → claim (+5) | P is related to Q by R |

**2.7 Time and sequence**

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

**2.8 Structure, description, classification and relation**

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

**2.9 Agents: holding, attitude and interaction states**

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

**3.1 Action constructors and role markers**

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

**3.2 Act verbs**

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

**3.3 Execution, completion, retry, decision and result**

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

**3.4 Directives and requirements**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `i!` | Ep | P act → directive (+7) | do P |
| `r<` | Ep | P agent, Q act → directive (+6) | ask P to Q |
| `r□` | Ep | P claim; or P conditional directive → requirement (+7) | it is required that P ; it is required: P |

**4.1 Question formers**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `?=` | E | P variable, Q claim → question | which P satisfies Q? |
| `?⊤` | E | P claim → question (+7) | is it so that P? |
| `?◷` | P | P claim → question (+7) | when is it so that P? |
| `?@` | P | P claim → question (+7) | where is it so that P? |
| `?⊙` | P | P variable, Q collection, R claim → question | which P of Q satisfies R? |
| `?∵` | P | P claim → question (+7) | why is it so that P? |
| `?` | U | no signature (E-UNSIG) | — |

**4.2 Answer forms**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `n⊘` | U | P mentioned question → claim (+7) | no, as to P |
| `y✓` | P | P mentioned question → claim (+7) | yes, as to P |
| `a>` | X | no signature (E-UNSIG) | — |

**5.1 Status force**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `g←` | E | P claim → line (+7) | supplied: P |
| `h◇` | E | P claim → line or claim (+7) | as a hypothesis: P ; it is hypothesized that P |
| `p◇` | E | P claim → line or claim (+7) | admissible: P ; it is admissible that P |
| `u?` | E | P claim → line or claim (+7) | not known: P ; it is not known that P |
| `u~` | E | P claim → line or claim (+7) | not established: P ; it is not established that P |

**5.2 Dialogue acts**

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

**6.1 Messages: identity, transmission and answer links**

| Root | Tier | Shape | Reading |
| --- | --- | --- | --- |
| `m▤` | use | P message name, Q agent; or P agent, Q agent, R item → declaration (the header); or claim | message P from Q ; the message R from P to Q |
| `r←` | P | P agent, Q agent, R item → claim (+5) | R is directed to Q by P † |
| `r>` | use | P message name, Q mentioned question, R line; or P item, Q item → line (the answer link); or claim | answer to Q of message P: R ; P answers Q |
