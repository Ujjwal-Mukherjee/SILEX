# SILEX rulebook: how every root is used

Nov 1, 2026 · @Moonbeam · r3: the placeholder is `n0` (your ruling of 07:29); `null` is retired

## 1. What this book is, and what I need from you

This book says how each of the 195 roots in the table is written: what goes in each place inside its parentheses, what it makes, what can sit inside it and what it can sit inside. 42 of the roots are established or already in use. The other 153 are not. Both kinds are written up in the same style, so any root can be nested in any other wherever the kinds allow.

**Grammar first.** On 1 November you ruled that the grammar leads and the checker follows later. So where this book and today's checker disagree, the book is the rule, and the difference goes on the checker change list (section 9). A line that the checker refuses but this book allows is a note for the checker, not a mistake in the line.

**Rule numbers and tags.** Rules are numbered B-1, B-2 and so on, so you can answer by number. Each rule and each entry says where it comes from:

- **\[E\]** established: written in your ALREADY-ESTABLISHED file or in the pinned table.
- **\[O\]** your ruling, with its date.
- **\[P\]** proposed by me. It is not in force until you agree. Every \[P\] has a default in section 10, and the entries use that default until you say otherwise.

**What I need from you.**

1. Read sections 3 and 4. They are the rules. Tell me which rule is wrong, by its number, or write a comment on it.
2. Answer the open points in section 10, or say "go" and I use my default for each.
3. Sections 7 and 8 are for looking things up: all 195 roots, and one entry for each. You need not read them through.

**Where things are.** Section 2 lists your rulings. Sections 3 to 6 are the rules: the core grammar, the details beyond the core slots (up to 8 arguments, `n0`), names and declarations, and numbers, times and criteria. Section 7 lists all 195 roots. Section 8 has the entries by family. Section 9 lists what the checker must change to agree with the book. Section 10 holds the open points.

## 2. Your rulings so far

These are your own words, shortened, in the order you gave them (1 November, India time). Each one is tagged **\[O\]** where it appears in the rules.

| When | Your ruling | Where it is used |
| --- | --- | --- |
| 01:29 | The roots should be usable "in the same style, grammar and in a self contained way", for AI-to-AI conversation with as little English as possible. | The whole book |
| 01:45 | Roots nest like functions with arguments: one root inside another, some with one argument and some with five or six. Your example: `a(xx, yy, b(45, 34, c(y, y, d(23:45, PDT, e(xyz)))))`. | Section 3 |
| 01:57 | Established roots take more roots inside them. A root shown with three arguments can take up to 8, `e(P, Q, R, S, T, U, V, W)`, and each argument can hold roots with their own arguments. | Section 4 |
| 01:57 | An argument that is not available is written `null`, as in `null, null, null`. | Section 4 |
| 02:42 | Numbers and times are wrapped in term roots (your answer to my question). You also chose to see a sample first. | Section 6 |
| 03:22 | Declarations may be written on one line: all the names first, then all the definitions in the same order. | Section 5 |
| 03:29 | The grammar is primary. The checker is changed later to follow it, never the other way round. | Sections 1 and 9 |
| 03:48 | Use the established roots too. A failing checker is no problem. What is needed is a rulebook. | The whole book |
| 07:29 | The placeholder is written `n0`, as in the table, not the word `null`. The rulebook and the tools follow. | Sections 4, 7 to 10 |

Two of these are only partly specified: what `n0` means in a place that must be filled, and what a term root for a number or a time looks like. Sections 4 and 6 propose answers and tag them **\[P\]**.

## 3. The core rules

These rules hold for all 195 roots. In the examples, `zo1` is an object, `zq1` a claim, `zkA` an agent, `zS1` a collection, `zm1` a method and `zcr1` a criterion (section 5 says how names work). Every example was run through the candidate checker described in section 9, and, when it uses nothing new, through your pinned checker. A result such as "refused E-CAT" is the checker's own code.

### Sentences and kinds

**B-1 \[E\] A sentence is a root applied to arguments:** `root(argument, argument, …)`. The root is the head. The arguments fill its places from left to right. Example: `g←(s=(zo1,zo2))` (AE-1).

**B-2 \[E\] Every place asks for a kind, and every root makes a kind.** The kinds are these:

| Kind | What it is | Examples |
| --- | --- | --- |
| claim | something that can be supplied, denied, questioned, assumed or left unknown | `s=(zo1,zo2)`, `zq1` |
| question | a request for a value or for a truth status; not a claim | `?⊤(zq1)` |
| act | an action expression; a named method is also an act | `▶(zm1)`, `cƒ(zo1,♙(zkA))` |
| item | anything talked about. Narrower kinds: agent, object, value, collection, method, time, criterion, message name, variable, mention; a count is a value; a premise set is a collection | `zo1`, `zkA`, `#(zS1)` |
| math term | a `✠(…)` term or a `zE` name; not an item | `✠(×(7,6))` |
| role marker | one of `⌘ ⚙ ↣ ☞ ☼ ⚓ ♙` applied to one argument | `♙(zkA)` |
| line | a complete unit of a message. Narrower kinds: directive, conditional directive, requirement, declaration, assumption, question | `g←(zq1)`, `i!(▶(zm1))` |

**B-3 \[E\] Fit.** A root fits a place when the kind it makes is the kind the place asks for, a narrower kind of it, or the place accepts anything. Some places name two kinds, "claim or item", and either fits. A claim is not an item, a question is not a claim, and a math term is neither. A wrong kind is refused (E-CAT). Example: `g←(∈(zo1,zo2))` is refused E-CAT, because `∈` needs a collection in its second place and `zo2` is an object.

**B-4 \[E\] One root can have more than one shape, and the place decides.** `h◇` is a line at the top of a message and a claim inside a claim place. `d↦` and `v✓` are acts, or claims by position.

**B-5 \[E\] There is one automatic conversion.** An act where a claim is asked is read as the event claim "an act of this kind occurs". It says nothing about completion, success or result. Completion is `c■`. Example: `g←(▶(zm1))` passes. No other conversion exists.

### Nesting

**B-6 \[O 01:45\] Roots nest.** Any application that fits a place can fill it, and the places of that filler can hold more applications, to any depth. Your own line of 03:22 is four roots deep, with eight applications:

```
h◇(s∵(m>(#(zS2),#(zS1)),b≻(g↦(zo3,zm1),g↦(zo3,zm2),zcr1)))
```

A shape that fits but has no determinate reading is still refused where the checker knows it: tense over a negated event (E-KIND), negated existence without a domain (E-DOMAIN), a tense around a value claim (E-ATEMP), a free letter in a value claim (E-FREE), a term with no defined value (E-UNDEFVAL).

**B-7 \[E\] Core places.** Every root has a fixed number of core places, 0 to 4 (the atoms have none), listed in section 8. The joiners, `d≔` and the three action roots are the exceptions. The core places are written in the table's order. A wrong count is refused (E-ARITY): `g←(n¬(zq1,zq2))`, because `n¬` has one core place. A core place with nothing available is written `n0` (B-19).

**B-8 \[E\] Joiners.** `∧`, `a|` and `s≺` take two or more operands of one kind: `∧` claims or acts, `a|` claims or items, `s≺` claims, acts or items. Three or more are read right-nested: `∧(a,b,c)` means `∧(a,∧(b,c))`. Example: `g←(∧(v⊨(zo1,zcr1),∈(zo1,zS1),c↝(zq1,zq2)))`. Operands of different kinds are refused (E-MIX): `g←(∧(v⊨(zo1,zcr1),zo2))`. Today's checker lets an act stand among claims, because of B-5. Joiners take neither role markers nor `n0`.

**B-9 \[E\] Binders.** `∃(v,φ)` and `?=(v,φ)` bind the variable `v` inside the claim φ. The variable is a name with the prefix `zk zm zo zv` or `zS`, not declared and not already bound. A question holds one binder, and the variable must occur in its body. A negated existence needs an explicit domain, a conjunct `∈(v,S)`.

```
g←(∃(zox,∧(∈(zox,zS1),v⊨(zox,zcr1))))
?=(zox,∈(zox,zS1))
```

`g←(n¬(∃(zox,v⊨(zox,zcr1))))` is refused E-DOMAIN. **\[P\]** `?⊙(v,S,φ)` binds in the same way, with `S` a collection: `?⊙(zox,zS1,v⊨(zox,zcr1))`. Your pinned checker refuses every `?⊙` line (E-CAT); the candidate checker reads this one.

### Which roots may be written

**B-10 \[E\] Status decides use.** Established roots are used freely. Partly established roots are in the CORE of your lexicon, so a session may use them. Candidate roots may be written, and the reader treats the line as candidate. Parked roots are not applied, and a reader who meets one answers `a?`. Six roots have no signature, five of them parked and one excluded (`c⇒ ∴ y⋯ g◎ ? a>`), and the checker refuses them (E-UNSIG).

**B-11 \[E\] Basis.** The basis of a sentence is the weakest status among its parts. A sentence is never more established than its weakest part (AE-15).

**B-12 \[E\] Lines.** These can stand alone in a message: a claim under a force root, a directive `i!(act)`, a request `r<(agent,act)`, a requirement `r□(claim)`, a question, a declaration, an assumption `~(claim)`, an acknowledgement. An act or a term alone is not a line (E-LINE): `cƒ(zo1,♙(zkA))` is refused, `i!(cƒ(zo1,♙(zkA)))` passes.

## 4. Beyond the core places: details, up to 8 arguments, and n0

You ruled on 1 November (01:57) that an established root can take up to 8 arguments, that each argument can hold roots with their own arguments, and that an argument which is not available is written `n0`. The only construction in your files that already works this way is the action construction (AE-14): an object, then role markers. This section applies it to every root. B-13, B-14, B-16 and B-19 are yours or established. B-15, B-17, B-18 and B-20 to B-22 are my proposals, tagged **\[P\]**.

### Width

**B-13 \[O 01:57\] A root takes up to 8 arguments in all:** its core places plus its details. The action roots already reach the limit with one object and seven role markers. The joiners, which take two or more operands, and `d≔`, which takes k names and k definitions (B-28), are the two exceptions.

**B-14 \[E\] The action roots `cƒ`, `o→` and `a+`** take an object first, then distinct role markers, each at most once, in any order. An omitted role is unspecified, not absent (AE-14). All eight arguments:

```
i!(cƒ(zo1,⌘(zm1),⚙(zo2),↣(zo3),☞(zo4),☼(zo5),⚓(zq1),♙(zkA)))
```

The seven role markers are established. Each takes one argument:

| Marker | Role | Its argument |
| --- | --- | --- |
| `⌘` | method | a method |
| `⚙` | instrument | an item |
| `↣` | recipient | an item |
| `☞` | destination | an item |
| `☼` | source | an item |
| `⚓` | basis | a claim or an item |
| `♙` | agent | an agent |

### Details on every root

**B-15 \[P\] Every root can take details.** After its core places, any root may take role markers, each at most once, in any order, with 8 arguments in all at most. The exceptions are the joiners, the binders (`∃ ?= ?⊙`), `r@`, `d≔`, the role markers themselves, the atoms (`t 0 ⊤ x w n`), the mention `⌜ ⌝` and the math term `✠`, none of which has a place for details. A root with two core places takes up to six details, and a root with four core places takes up to four. Section 8 gives the number of details of each root as `+k`. Examples:

```
g←(c↝(zq1,zq2,⚓(zq3)))
g←(v⊨(zo1,zcr1,☼(zo2)))
g←(s=(zo1,zo2,⌘(zm1),⚙(zo3),↣(zo4),☞(zo5),☼(zo6),⚓(zq1)))
```

The last one has 2 core places and 6 details. Your pinned checker refuses all three (E-ARITY); the candidate checker reads them.

**B-16 \[O 01:57\] A detail can hold roots.** The argument of a role marker is a name or any application that makes the kind the marker needs, and that application has its own places. Here is your `e(P, Q, R, S, T, U, V, W)` with eight arguments, six of them roots:

```
g←(c↝(s∵(zq1,zq2),v⊨(zo1,zcr1),⌘(zm1),⚙(g∪(zo2,zo3)),↣(zkB),☞(zo4),☼(zo5),⚓(i→(zq3,zq4))))
```

The two core places of `c↝` are the cause and the effect. The six details follow.

**B-17 \[P\] What a detail says.** A marker adds one fact about the thing the root describes: by which method, with which instrument, to whom, to where, from where, on what basis, by which agent. A marker that makes no sense for the root, such as a recipient on a sameness claim, is not refused by the grammar. A reader marks `a?`. Layer 3 of your checker (plausibility, P01 to P09) has no rule for it today, and one can be added.

**B-18 \[P\] Details are optional and unordered.** A detail that is not available is left out, or written `n0`, which means the same. Two of the same marker are refused (E-ROLE): `g←(s=(zo1,zo2,⚓(zq1),⚓(zq2)))`. A ninth argument is refused (E-ARITY). A marker with the wrong kind of argument is refused (E-CAT): `g←(s=(zo1,zo2,⌘(zo3)))`, because `⌘` needs a method.

### n0

**B-19 \[O 01:57; spelling O 07:29\] A place with nothing available is written `n0`,** so the other places keep their positions. In a core place: `g←(m∥(zo1,zo2,n0,zo3))` and `g←(s=(n0,zo2))`. After the core places, an `n0` stands for a detail that is not given, and it counts toward the 8: `g←(s=(zo1,zo2,n0,n0))`. Inside a marker, `⚓(n0)` means the same as leaving `⚓` out. `n0` is an atom of the table (family 2.5). It takes no arguments (`n0(zo1)` is E-ARITY) and has no kind of its own, and it fits every place except the ones B-21 lists. The word `null`, which your 01:57 ruling used, is no longer read (E-SYNTAX).

**B-20 \[P\] What `n0` means.** "Not supplied." It does not mean none, zero, empty or unknown, and the reader does not fill it in. "Unknown" is `u?`. "No such thing" is `n¬`. This is the reading AE-14 already gives to an omitted role.

**B-21 \[P\] Where `n0` may not stand.** Not as an operand of a joiner (E-NULL): `g←(∧(n0,zq1))`. Not as a line (E-LINE). Not as the name in `d≔` (E-DEF) and not as a bound variable (E-BIND).

**B-22 \[P\] A claim with `n0` in a core place is incomplete.** Under `n¬`, in a condition `i→` or in a question `?⊤` an incomplete claim has two readings, "not this at all" and "not this particular one". A reader marks `a?` there. The candidate checker prints the warning NU for every `n0` in a core place, and none for an `n0` after the core places; it does not refuse these lines.

What your pinned checker does today with all of this: it refuses every detail on a root other than the three action roots (E-ARITY) and it reads `n0` only as the two-argument claim root of the old table, so a bare `n0` is E-UNSIG, and the word `null` is E-SYNTAX. Both are on the change list in section 9.

## 5. Names, declarations, force and messages

### Names

**B-23 \[E\] A name is a class prefix plus letters and digits.** The prefix is the only meaning a name has. A free-standing name is a constant of its message (AE-2). The class also says what a declaration may define:

| Prefix | Kind | `d≔` defines it as |
| --- | --- | --- |
| `zp zq zr zh` | claim | a claim |
| `zk` | agent | an agent |
| `zm` | method | an act or a method |
| `zo` | object | an item |
| `zv` | value | a value |
| `zS` | collection | a collection |
| `zE` | math term | a `✠` term |
| `zt` | time | `t`, or an imported qualified reference `r@(…)` |
| `zcr` | criterion | a criterion name, or a scaffold (no root makes a criterion) |
| `zU` | message | nothing: only the header declares it |

**B-24 \[E\] A time name must be declared before it is used,** with `d≔(zt1,t)` (E-UNDECL otherwise). The pinned checker does not require the other names to be declared. A name with no definition has only its class as meaning.

**B-25 \[E\] Roster names** (AE-11). A `zk` name that is a sender in a header means that participant in every message. All other names are local to their message.

### Declarations

**B-26 \[E\] `d≔(name,definition)` names a definition and asserts nothing** (D3 3.3). Quoted English as the definition is a scaffold: the meaning stays in the English, and the checker notes SCAFFOLD. A name declared twice is refused (E-REDECL). A message name is refused (E-DEF), because only the header declares it.

```
d≔(zo1,⌜the signed contract file⌝)
d≔(zq5,v⊨(zo1,zcr1))
```

**B-27 \[O 03:22\] One-line declarations.** `d≔(n1,…,nk,def1,…,defk)` takes all k names first and then all k definitions in the same order. It means the same as k separate `d≔` lines in that order. Your own example, with six names:

```
m▤(zUa1,zkA)
d≔(zm1, zm2, zo3, zS1, zS2, zcr1, ⌜the new ranking method⌝, ⌜the old ranking method⌝, ⌜the benchmark queries⌝, ⌜the queries the new method ranks wrongly⌝, ⌜the queries the old method ranks wrongly⌝, ⌜the ranking agrees with the human relevance labels⌝)
h◇(s∵(m>(#(zS2),#(zS1)),b≻(g↦(zo3,zm1),g↦(zo3,zm2),zcr1)))
```

**B-28 \[P\] Rules around the one-line form.** There is no limit on k. The number of arguments must be even and at least two (E-ARITY): `d≔(zq6,zq7,v⊨(zo1,zcr1))` is refused. A name declared twice, in the line or before it, is refused (E-REDECL). A definition may use any name declared earlier in the same line, as with separate lines. Time names go in the same line with the definition `t`. Your pinned checker refuses the one-line form (E-SYNTAX "bad d≔"); `expand_batch.py` in the pilot zip turns it into lines it reads, and the candidate checker reads it as it stands.

### Mention and force

**B-29 \[E\] Mention.** `⌜ … ⌝` makes an expression talked about, not used or asserted. English text outside a mention is never part of the language (AE-3).

**B-30 \[E\] Force at the outside** (AE-4). A claim line is put under exactly one force root: `g←` supplied, `h◇` put forward as a hypothesis, `p◇` admissible under the context, `u?` not known, `u~` not established at the required standard. `g←` supplies and does not verify. A bare claim line is accepted with the warning FU (force unspecified).

**B-31 \[E\] Negation and questions** (AE-5, AE-6). `n¬` negates a claim; disagreement is `g←(n¬(P))` with P restated. `?⊤(c)` has exactly three answers: `g←(c)`, `g←(n¬(c))` and `u?(c)`.

**B-32 \[E\] Roots that must not be mixed up** (AE-7, AE-8). `s∵` support, `c↝` cause and `d⊢` derivation are three roots, and none says that its parts hold or occurred. `⊛` claimed origin, `v✓` checking and `v⊨` satisfaction are three roots, and none proves the claim.

**B-33 \[E\] Propose and agree** (AE-13). `p↗` puts a candidate forward and adopts nothing. `a=` agrees and does not verify. A new name is accepted by restating its declaration: `a=(d≔(zo9,⌜the new file⌝))`.

**B-34 \[E\] Attribution.** `zkB:claim` attributes a claim to an agent: `g←(zkB:c■(zm1))`. It is not allowed before a value claim (E-ATTR). L0 treats it as a candidate, in its Change 12 (not C-12 of section 9).

### Messages

**B-35 \[E\] The header** (AE-9). The first line of a message is `m▤(zU,zk)`. One sender per message. A message is never edited. It is established by use, though D3 gives it status U.

**B-36 \[E\] The answer link** (AE-10). `r>(zUk,⌜Q⌝,W)` answers question Q of message zUk, and W is exactly `g←(A)` or `u?(A)` (otherwise E-FORCE). One answer per question. Unknown is `u?`. A question with no target is marked `a?`.

```
r>(zUb1,⌜?⊤(zq1)⌝,g←(zq1))
```

**B-37 \[E\] Unresolved means `a?`** (AE-12). A reader who meets a line outside the rules, or one it cannot resolve, marks `a?` and does not guess.

## 6. Numbers, units, times and criteria

The first two parts say what the table and the checker allow today (\[E\]). The last part proposes what is missing (\[P\]) for your ruling. You ruled on 1 November (02:42) that numbers and times are wrapped in term roots. The table has two term roots for numbers, `✠` and `#`, and none for units, clock times, dates or zones.

### Numbers today

**B-38 \[E\] A number is a math term or a count.** `✠(…)` writes integers, fractions and arithmetic (`+ − × ÷ ^ √ sin cos ln ∫ Σ lim`); there are no decimals. It is accepted only where a math term is asked: the object of `cƒ`, an argument of `r→` and `m>`, and the definition of a `zE` name (otherwise E-MATHPLACE). `#(S)` is the count of a collection, and a count is a value. `m>` takes two math terms or two counts, never one of each (E-CAT). A bare numeral is refused (E-LEX), except `0`, which is a root. A number with a unit has no form, so the value name carries it in a scaffold.

```
g←(r→(✠(×(7,6)),✠(42)))             passes
g←(m>(#(zS1),#(zS2)))               passes
g←(m>(#(zS1),✠(40)))                refused E-CAT
g←(m∥(zo1,zo2,91,zo3))              refused E-LEX
g←(m∥(zo1,zo2,✠(91),zo3))           refused E-MATHPLACE
g←(m∥(zo1,zo2,zv1,zo3))             passes; zv1 is a value name whose scaffold says the number and the unit
```

### Times today

**B-39 \[E\] A time frame has three parts.** A time name is declared `d≔(zt1,t)`. `c⊃(zt1,claim)` puts a claim in that time frame. `t≺`, `t●` and `t▷` say before, at and after the reference time, which comes from the nearest enclosing `c⊃(zt,…)`; with none the checker warns (RT). Tense over a negation is allowed only for a state predicate (E-KIND). A value claim is atemporal and takes no tense or time frame (E-ATEMP). There is no "now", no interval, no clock time, no date and no zone.

```
g←(c⊃(zt1,t≺(∈(zo1,zS1))))          passes
g←(t≺(n¬(▶(zm1))))                  refused E-KIND
g←(c⊃(zt1,r→(✠(1),✠(2))))           refused E-ATEMP
```

### What I propose

**B-40 \[O 02:42\] Numbers and times are wrapped in term roots.** So a quantity with a unit, a clock time, a date and a zone each need a root that makes them. None of the 195 does.

**B-41 \[P\] A term root makes a math term or a time and takes its parts as arguments.** A number or quantity term makes a math term, so `r→` and `m>` accept it. A clock-time or date term makes a time, so `c⊃` accepts it. The parts (hour, minute, zone, unit) are arguments or role markers, and any of them can be `n0`. Your `d(23:45, PDT, e(xyz))` is then a root with a clock-time term, a zone and a nested claim, and B-6 already covers the nesting. I have not chosen symbols for these roots.

**B-42 \[P\] Cb2's nine words are the first candidates.** They are not among the 195 and nothing is adopted. D read each one blind from its card:

| Word | Takes | Makes | Reads as | D's blind reading |
| --- | --- | --- | --- | --- |
| `c⌗` | collection, optional time | math term | the number of members, as a term `r→` and `m>` accept | MATCH, useful |
| `m⌗` | item, value, optional time | math term | the number the quantity has for the item, in the unit the quantity names | MATCH, needed |
| `s⌗` | collection, value, optional time | math term | the sum over the members of the quantity | MATCH, needed |
| `b≬` | math term, math term, math term | claim | the value is between two bounds, ends included | MATCH, redundant |
| `p◑` | claim, math term, item | claim | relative to a basis, the probability of the claim is p, from 0 to 1 | MATCH, useful |
| `u⊕` | act | line | the sender undertakes the act | MATCH, needed |
| `d⊖` | act, optional claim | line | the sender declines the act, with an optional reason | MATCH, needed |
| `f⊂` | collection, collection, criterion | claim | sub holds exactly the members of whole that meet the criterion | PARTIAL, useful |
| `y▸` | method, time | claim | the method was triggered before the time and is not completed | PARTIAL, misleading |

Under B-15 the optional time of the first three is a time detail, not a second shape. Its marker is not drafted.

**B-43 \[P\] A criterion needs a builder.** 26 places among the 153 take a criterion and no root makes one, so a criterion is a name with a scaffold. I propose a root that makes a criterion from a claim with a bound variable, "the criterion that v satisfies φ", binding as `∃` does (B-9), and a role marker for a criterion detail. The pinned checker accepts a bound variable only in `∃` and `?=`, so this rule is on the change list. The root and the marker have no symbols yet.

## 7. All 195 roots at a glance

Section 8 gives one entry for every root. This section shows the whole set first, in four views: the status of the 195, the 25 families, what makes each kind of argument, and the roots that share a shape. Every figure was counted by script from your table and the checker.

### Status

| Status | Roots | What it means here |
| --- | --- | --- |
| established | 40 | in your pinned files, with the readings of your established file |
| by use | 2 | `m▤` and `r>`: your sessions use them as the header and the answer link, but the table does not list them as established |
| partly | 26 | some uses are settled and others are open (your Settled/Open table) |
| candidate | 97 | proposed in the table with a signature, not yet used in your files |
| parked | 29 | held back; 24 have a signature and 5 have none |
| excluded | 1 | `a>`, which has no signature |
| all | 195 |  |

The six roots with no signature are `c⇒` `∴` `y⋯` `g◎` `?` `a>`. The checker refuses a line that uses one (E-UNSIG), and B-10 says what a reader does. Their entries in section 8 give the table's gloss and no example.

### The families

Each root belongs to one family. The names are the ones in D3.

| Family | Established, by use | Partly | Candidate | Parked, excluded |
| --- | --- | --- | --- | --- |
| 0.1 Application, names and definition (1) | — | `d≔` | — | — |
| 0.2 Mention and attribution (1) | `⌜ ⌝` | — | — | — |
| 0.3 Atoms and placeholders (6) | `t` `0` | — | — | `⊤` `x` `w` `n` |
| 1.1 Collections and selection (10) | — | — | `g∪` `i+` `e−` `a/` `c↓` `s∃` `s⊙` `k▤` `b▁` | `f∃` |
| 1.2 Items, data and transformations (12) | — | `⧉` | `d▤` `i▤` `f▦` `fƒ` `g↦` `i↦` `m↻` `o←` `s↦` `u↻` `e⚖` | — |
| 1.3 Methods, processes and tasks (3) | — | — | `m▦` `p▷` `t▦` | — |
| 1.4 Quantity and mathematics (4) | — | `✠` `#` | `c∑` `dΔ` | — |
| 2.1 Logical core: negation, joining, quantification, implication, context (8) | `n¬` `i→` | `∧` `a\|` `∃` `i⇒` `c⊃` | — | `c⇒` |
| 2.2 Reasons, support, inference and evidence (12) | `s∵` `d⊢` | — | `∵` `r∵` `j∵` `e∵` `l⊢` | `c∴` `∴` `i⊢` `p⊢` `e▤` |
| 2.3 Causation, condition, constraint and necessity (4) | `c↝` | — | `l⊣` `n□` | `c⊣` |
| 2.4 Sameness, difference, comparison and order (16) | — | `s=` `i≡` `m>` | `r≡` `c≡` `c≠` `d≠` `b≻` `≈` `o≺` `v=` `m∥` `n−` | `s≈` `m≡` `d≢` |
| 2.5 Epistemic status, verification, probability and absence (13) | `v⊨` `n0` | — | `f⊥` `✓` `✗` `r✓` `s✓` `p⇢` | `f⊤` `k✓` `u±` `l≥` `pℙ` |
| 2.6 Provenance and reference (5) | `s@` `s@*` `⊛` | `r@` | — | `r:` |
| 2.7 Time and sequence (9) | `t≺` `t●` `t▷` | `s≺` | `b₀` `s◷` `s▷` | `▷` `y⋯` |
| 2.8 Structure, description, classification and relation (18) | `∈` | `⊡` | `e∈` `o\|` `c◉` `d⋮` `p▦` `s▦` `s⊞` `m⊞` `m↦` `k#` `l↔` `↔` `r∩` `s≔` `p?` `i←` | — |
| 2.9 Agents: holding, attitude and interaction states (15) | `h⊡` | — | `b~` `t~` `i◎` `o◎` `n!` `r−` `g▷` `f▷` `h+` `s◇` `f↩` `o▤` `u✓` | `g◎` |
| 3.1 Action constructors and role markers (10) | `cƒ` `o→` `a+` `⌘` `⚙` `↣` `☞` `☼` `⚓` `♙` | — | — | — |
| 3.2 Act verbs (11) | — | — | `c?` `c≶` `e⋯` `i?` `t⋯` `u↦` `l↻` `i↑` `t⚖` `a<` | `q<` |
| 3.3 Execution, completion, retry, decision and result (8) | `d↦` `v✓` | `▶` `c■` `⤿` `r→` | — | `d⊙` `c✓` |
| 3.4 Directives and requirements (3) | — | `i!` `r<` `r□` | — | — |
| 4.1 Question formers (7) | `?=` `?⊤` | — | `?◷` `?@` `?⊙` `?∵` | `?` |
| 4.2 Answer forms (3) | — | — | `y✓` | `n⊘` `a>` |
| 5.1 Status force (5) | `g←` `h◇` `p◇` `u?` `u~` | — | — | — |
| 5.2 Dialogue acts (8) | `a=` `a?` `p↗` | `a.` `e✗` `r↻` `~` | `p▁` | — |
| 6.1 Messages: identity, transmission and answer links (3) | `m▤` `r>` | — | `r←` | — |

### What fills a place

A place asks for a kind (B-2). A name of the right class fills it, and so does any root that makes the kind. This table counts both sides. The last column counts the roots that have at least one place the kind fits, over every shape of every root; the three joiners are added for the kinds they join. A kind of item (agent, value, collection, method, time, criterion, message name, mention) also fits every place that asks for an item, so those counts stay close to the count for item.

| Kind | Name class | Roots that make it | Roots with a place it fits |
| --- | --- | --- | --- |
| claim | `zp zq zr zh` | 107 roots, listed by family in section 8 | 65 |
| question | none (a question is mentioned: `⌜…⌝`) | `?=` `?⊤` `?◷` `?@` `?⊙` `?∵` | 3 |
| act | `zm` | `cƒ` `o→` `a+` `c?` `c≶` `e⋯` `i?` `t⋯` `u↦` `l↻` `i↑` `t⚖` `a<` `q<` `▶` `c■` `⤿` `d⊙` `d↦` `v✓` `c✓` | 9 |
| method | `zm` | `m▦` `p▷` `t▦` | 112 |
| item | `zo` | `s⊙` `d▤` `i▤` `f▦` `fƒ` `g↦` `i↦` `m↻` `o←` `s↦` `u↻` `e⚖` `c∑` `dΔ` and the atoms `t` `x` `w` `n` | 98 |
| collection | `zS` | `g∪` `i+` `e−` `a/` `c↓` `s∃` `k▤` | 104 |
| premise set | none | `b▁` | 108 |
| value | `zv` | `0` | 97 |
| count | none (a count is a value) | `#` | 98 |
| math term | `zE` | `✠` | 5 |
| agent | `zk` | none | 106 |
| time | `zt` | none (`t` is declared as a name) | 97 |
| criterion | `zcr` | none | 107 |
| message name | `zU` | none (only the header declares it) | 96 |
| role marker | none | `⌘` `⚙` `↣` `☞` `☼` `⚓` `♙` | 3 |
| line | none | `g←` `h◇` `p◇` `u?` `u~` `a.` `a=` `a?` `p↗` `e✗` `r↻` `p▁` `r>` | 1 |
| directive, requirement, declaration, assumption | none | `i!` `r<` `i⇒` `r□` `m▤` `d≔` `~` | 7 |
| mention | none | `⌜ ⌝` | 96 |

**B-44 \[E\] Four kinds have no root that makes them.** An agent, a time, a criterion and a message name can only be written as a declared name (`zk`, `zt`, `zcr`, `zU`). A time name is declared with the atom `t` (B-24). An object is a name `zo` or one of the item roots in the table. So much of the language is names, which is why section 5 is long, and why B-41 and B-43 propose roots for times and criteria.

### Roots with the same shape

121 roots share their exact places and result with at least one other root, in 32 groups. The groups below leave out the roots with a special shape (the joiners, the binders, the action roots, the header and the answer link). On the plain lines of section 8 the checker accepts any root of a group in the place of another, and at most prints a different status note, so there only the gloss tells them apart. In a larger line a checker rule can still tell members apart: `t≺` of G5 is refused under a negation (E-KIND) where `⊛` is not, and `r→` of G27 refuses counts (E-CAT) where `m>` takes them.

| Group | Shape | Roots |
| --- | --- | --- |
| G1 | P item, Q item → claim | `l⊣` `s=` `s≈` `i≡` `m≡` `d≢` `v=` `s✓` `▷` `s◷` `e∈` `m⊞` `m↦` `k#` `l↔` `↔` `r∩` `f↩` |
| G2 | P claim, Q claim → claim | `i→` `i⇒` `s∵` `∵` `r∵` `j∵` `e∵` `c↝` `n□` `c≡` `c≠` `p⇢` `p?` |
| G3 | P item, Q item → item | `d▤` `f▦` `fƒ` `m↻` `o←` `u↻` |
| G4 | P claim → line | `g←` `h◇` `p◇` `u?` `u~` `p▁` |
| G5 | P claim → claim | `k✓` `l≥` `⊛` `t≺` `t●` `t▷` |
| G6 | P item, Q collection → claim | `∈` `o\|` `c◉` `d⋮` `p▦` `s▦` |
| G7 | P item, Q criterion → claim | `n−` `v⊨` `✓` `✗` `r✓` |
| G8 | P claim → question | `?⊤` `?◷` `?@` `?∵` |
| G9 | P anything → line | `a.` `a?` `e✗` `r↻` |
| G10 | P item → role marker | `⚙` `↣` `☞` `☼` |
| G11 | P claim or item, Q claim or item → claim | `d⊢` `s@` `s@*` |
| G12 | P agent, Q item → claim | `h⊡` `n!` `r−` |
| G13 | P premise set, Q claim, R criterion → claim | `i⊢` `l⊢` `p⊢` |
| G14 | P item, Q item, R criterion → claim | `r≡` `b≻` `o≺` |
| G15 | P item, Q item, R item → claim | `≈` `r:` `s≔` |
| G16 | P claim or declaration → line | `a=` `p↗` |
| G17 | P agent, Q claim → claim | `b~` `i◎` |
| G18 | P method, Q claim → claim | `b₀` `o◎` |
| G19 | P item, Q criterion → act | `c?` `i↑` |
| G20 | P collection, Q criterion → collection | `c↓` `s∃` |
| G21 | P act → act | `c■` `⤿` |
| G22 | P item, Q claim → claim | `e▤` `c⊣` |
| G23 | P claim, Q criterion → claim | `f⊤` `f⊥` |
| G24 | P item, Q method → item | `g↦` `s↦` |
| G25 | P collection, Q item → collection | `i+` `e−` |
| G26 | P item, Q criterion → item | `i↦` `e⚖` |
| G27 | P math term, Q math term → claim | `m>` `r→` |
| G28 | P mentioned question → claim | `n⊘` `y✓` |
| G29 | P agent, Q agent, R item → claim | `s◇` `r←` |
| G30 | P agent, Q item, R item → claim | `t~` `u✓` |
| G31 | P agent, Q item → act | `t⋯` `q<` |
| G32 | P agent, Q item, R item → act | `u↦` `l↻` |

**B-45 \[P\] Among roots of one shape, the gloss decides.** A writer picks the root whose entry says what is meant. A reader takes the root as written and never reads a neighbour into it. Whether two readers keep the roots of a group apart is for the blind readers of phase 4 to test. The established roots are in these groups too (`∈` in G6, `h⊡` in G12, `v⊨` in G7), so the risk is not only in the candidates.

## 8. Root entries by family

One entry for each of the 195 roots, in D3's order. Each family has a table and a block of example lines.

**How to read a table.** *Root* is the root and its status (section 7). *Shape* lists the core places in order as `P`, `Q`, `R` and so on, which are your letters of `e(P, Q, R, S, T, U, V, W)`, then the kind the root makes. `(+k)` is how many details it can take after the core places, with 8 arguments in all at most (B-13, B-15). `G…` is the same-shape group of section 7. *Pattern* reads the places in plain English. *Table's gloss* is your table's own description, shortened.

**How to read an example block.** Each root has a line that shows it inside other roots. Where the root can take details, a second line adds one detail. Every line was run through both checkers. The label says `passes` when your pinned checker passes the line as well, and `candidate only` when only the candidate checker does. A line with a detail is `candidate only` (section 9), except for `cƒ`, `o→` and `a+`, whose table entries already take role markers. `[i+ + detail]` labels the second line of `i+`. The names in the lines (`zo1`, `zS1`, `zm1`, `zcr1`, `zq1`, `zkB` and so on) are not declared, which your pinned checker allows (B-24). The time name `zt1` in the `c⊃` lines is declared in front with `d≔(zt1,t)`.

**B-46 \[P\] The pattern is a proposed reading of the places.** The table gives the kinds and a gloss, and for many roots it does not say what each place means. A pattern reads the places in the table's order. A † marks a pattern where the gloss does not fix what a place means, so the order is my inference and a reader should not rely on it until you rule on the root or blind readers agree on it. The pattern of a role marker is the phrase it adds to a root (B-17).

### 0.1 Application, names and definition

1 root (1 partly). What they make: declaration (1).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `d≔` partly | P1 … Pk names, then Q1 … Qk definitions (k ≥ 1) → declaration (no details) | let the names P1 … Pk stand for the definitions Q1 … Qk | Names a definition and asserts nothing. The name class decides what may be defined. Local to its message. Quoted English is a scaffold. |

```
d≔(zo1,⌜the first file⌝)   [d≔] passes
```

### 0.2 Mention and attribution

1 root (1 established). What they make: mention (1).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `⌜ ⌝` established | P any expression → mention (no details) | “P” | Mention: the expression is talked about, not used or asserted. English text outside a mention is never part of the language. |

```
a?(⌜g←(zq1)⌝)   [⌜ ⌝] passes
```

### 0.3 Atoms and placeholders

6 roots (2 established, 4 parked). What they make: item (4), value (1), claim (1).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `t` established | nothing (an atom) → item (no details) | a time | A time concept. Only as the definition of a time name: `d≔(zt1,t)`. |
| `0` established | nothing (an atom) → value (no details) | zero | The number zero. |
| `⊤` parked | nothing (an atom) → claim (no details) | the true statement | Logical truth-value constant in a specified interpretation or formal system. |
| `x` parked | nothing (an atom) → item (no details) | a placeholder | Variable, unknown, or placeholder symbol. |
| `w` parked | nothing (an atom) → item (no details) | a word | Lexical unit; may be used as a typed atom in composition. |
| `n` parked | nothing (an atom) → item (no details) | something novel | Novel relative to specified reference/context; default atomic adjective-like sense. |

```
d≔(zt1,t)               [t] passes
g←(m∥(zo1,zo2,0,zo3))   [0] passes
g←(s∵(⊤,zq1))           [⊤] passes
g←(v⊨(x,zcr1))          [x] passes
g←(v⊨(w,zcr1))          [w] passes
g←(v⊨(n,zcr1))          [n] passes
```

### 1.1 Collections and selection

10 roots (9 candidate, 1 parked). What they make: collection (7), item (1), claim (1), premise set (1).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `g∪` candidate | P item, Q item → collection (+6) | the collection of P and Q | Organizing elements into a collection; set union is only one kind of grouping. |
| `i+` candidate | P collection, Q item → collection (+6) · G25 | P with Q added | Add or include a member within a specified set or structure. |
| `e−` candidate | P collection, Q item → collection (+6) · G25 | P without Q | Remove an element from a set or from consideration. |
| `a/` candidate | P item, Q criterion → collection (+6) | P broken into its elements by Q | Analyze/decompose an item into relevant elements. |
| `c↓` candidate | P collection, Q criterion → collection (+6) · G20 | P narrowed by Q † | Reduce the range of viable interpretations / uncertainty. |
| `s∃` candidate | P collection, Q criterion → collection (+6) · G20 | the entities sought in P under Q | Seek an entity satisfying a condition; `∃` itself states existence, not a search process. |
| `s⊙` candidate | P collection, Q criterion → item (+6) | the item chosen from P under Q | Mark or choose one item from a set of candidates. |
| `f∃` parked | P collection, Q criterion → claim (+6) | an entity of P that meets Q has been found | Identify an entity satisfying a specified condition, with a matching entity found. |
| `k▤` candidate | P agent → collection (+7) | the information that P holds as supported | An agent/context's epistemically supported information representation or collection. |
| `b▁` candidate | P collection → premise set (+7) | P taken as the foundation set of premises | Foundation / supporting premise set. |

```
g←(v⊨(g∪(zo1,zo2),zcr1))           [g∪] passes
g←(v⊨(g∪(zo1,zo2,☼(zo2)),zcr1))    [g∪ + detail] candidate only
g←(v⊨(i+(zS1,zo1),zcr1))           [i+] passes
g←(v⊨(i+(zS1,zo1,☼(zo2)),zcr1))    [i+ + detail] candidate only
g←(v⊨(e−(zS1,zo1),zcr1))           [e−] passes
g←(v⊨(e−(zS1,zo1,☼(zo2)),zcr1))    [e− + detail] candidate only
g←(v⊨(a/(zo1,zcr1),zcr1))          [a/] passes
g←(v⊨(a/(zo1,zcr1,☼(zo2)),zcr1))   [a/ + detail] candidate only
g←(v⊨(c↓(zS1,zcr1),zcr1))          [c↓] passes
g←(v⊨(c↓(zS1,zcr1,☼(zo2)),zcr1))   [c↓ + detail] candidate only
g←(v⊨(s∃(zS1,zcr1),zcr1))          [s∃] passes
g←(v⊨(s∃(zS1,zcr1,☼(zo2)),zcr1))   [s∃ + detail] candidate only
g←(v⊨(s⊙(zS1,zcr1),zcr1))          [s⊙] passes
g←(v⊨(s⊙(zS1,zcr1,☼(zo2)),zcr1))   [s⊙ + detail] candidate only
h◇(n¬(f∃(zS1,zcr1)))               [f∃] passes
h◇(n¬(f∃(zS1,zcr1,⚓(zq3))))        [f∃ + detail] candidate only
g←(v⊨(k▤(zkB),zcr1))               [k▤] passes
g←(v⊨(k▤(zkB,☼(zo2)),zcr1))        [k▤ + detail] candidate only
g←(v⊨(b▁(zS1),zcr1))               [b▁] passes
g←(v⊨(b▁(zS1,☼(zo2)),zcr1))        [b▁ + detail] candidate only
```

### 1.2 Items, data and transformations

12 roots (1 partly, 11 candidate). What they make: item (11), same kind as its argument (1).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `d▤` candidate | P item, Q item → item (+6) · G3 | the structured content of P and Q † | Structured or processable content. |
| `i▤` candidate | P item → item (+7) | the information content of P | Information content or a meaningful representation; mnemonic symbol, not established mathematical notation. |
| `f▦` candidate | P item, Q item → item (+6) · G3 | P turned into the explicit structured form Q † | Turn an idea, problem or content into an explicit structured expression. |
| `fƒ` candidate | P item, Q item → item (+6) · G3 | the function that maps P to Q † | A defined function or input-output mapping. |
| `g↦` candidate | P item, Q method → item (+6) · G24 | what the method Q makes from P | Input or existing representation mapped to produced output; generation does not imply novelty. |
| `i↦` candidate | P item, Q criterion → item (+6) · G26 | the meaning of P under the interpretation Q | Map an expression to a meaning under an interpretation function. |
| `m↻` candidate | P item, Q item → item (+6) · G3 | P changed into Q † | Change an existing object or representation. |
| `o←` candidate | P item, Q item → item (+6) · G3 | P brought in from Q † | Bring or acquire some specified object, value, or information into the current context. |
| `s↦` candidate | P item, Q method → item (+6) · G24 | the solution to P by the method Q † | Process or mapping from a problem toward a solution. |
| `u↻` candidate | P item, Q item → item (+6) · G3 | P updated with the information Q † | Change a state or record using new information. |
| `e⚖` candidate | P item, Q criterion → item (+6) · G26 | the judgment of P against Q | Assess an object against specified criteria, yielding a judgment or value. |
| `⧉` partly | P item → same kind as its argument (+7) | a copy of P | A copy of x, a distinct item. |

```
g←(v⊨(d▤(zo1,zo2),zcr1))           [d▤] passes
g←(v⊨(d▤(zo1,zo2,☼(zo2)),zcr1))    [d▤ + detail] candidate only
g←(v⊨(i▤(zo1),zcr1))               [i▤] passes
g←(v⊨(i▤(zo1,☼(zo2)),zcr1))        [i▤ + detail] candidate only
g←(v⊨(f▦(zo1,zo2),zcr1))           [f▦] passes
g←(v⊨(f▦(zo1,zo2,☼(zo2)),zcr1))    [f▦ + detail] candidate only
g←(v⊨(fƒ(zo1,zo2),zcr1))           [fƒ] passes
g←(v⊨(fƒ(zo1,zo2,☼(zo2)),zcr1))    [fƒ + detail] candidate only
g←(v⊨(g↦(zo1,zm1),zcr1))           [g↦] passes
g←(v⊨(g↦(zo1,zm1,☼(zo2)),zcr1))    [g↦ + detail] candidate only
g←(v⊨(i↦(zo1,zcr1),zcr1))          [i↦] passes
g←(v⊨(i↦(zo1,zcr1,☼(zo2)),zcr1))   [i↦ + detail] candidate only
g←(v⊨(m↻(zo1,zo2),zcr1))           [m↻] passes
g←(v⊨(m↻(zo1,zo2,☼(zo2)),zcr1))    [m↻ + detail] candidate only
g←(v⊨(o←(zo1,zo2),zcr1))           [o←] passes
g←(v⊨(o←(zo1,zo2,☼(zo2)),zcr1))    [o← + detail] candidate only
g←(v⊨(s↦(zo1,zm1),zcr1))           [s↦] passes
g←(v⊨(s↦(zo1,zm1,☼(zo2)),zcr1))    [s↦ + detail] candidate only
g←(v⊨(u↻(zo1,zo2),zcr1))           [u↻] passes
g←(v⊨(u↻(zo1,zo2,☼(zo2)),zcr1))    [u↻ + detail] candidate only
g←(v⊨(e⚖(zo1,zcr1),zcr1))          [e⚖] passes
g←(v⊨(e⚖(zo1,zcr1,☼(zo2)),zcr1))   [e⚖ + detail] candidate only
g←(v⊨(⧉(zo1),zcr1))                [⧉] passes
g←(v⊨(⧉(zo1,☼(zo2)),zcr1))         [⧉ + detail] candidate only
```

### 1.3 Methods, processes and tasks

3 roots (3 candidate). What they make: method (3).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `m▦` candidate | P claim, Q act → method (+6) | the procedure that does Q under the condition P † | A structured procedure with steps and possibly conditions. |
| `p▷` candidate | P act → method (+7) | the process of P | An organized progression of operations or states. |
| `t▦` candidate | P act, Q claim → method (+6) | the task P with the condition Q † | A unit of work, potentially with objective, requirements, and completion criteria. |

```
r<(zkB,m▦(⊛(zq1),zm1))          [m▦] passes
r<(zkB,m▦(⊛(zq1),zm1,☼(zo2)))   [m▦ + detail] candidate only
r<(zkB,p▷(▶(zm1)))              [p▷] passes
r<(zkB,p▷(▶(zm1),☼(zo2)))       [p▷ + detail] candidate only
r<(zkB,t▦(▶(zm1),zq1))          [t▦] passes
r<(zkB,t▦(▶(zm1),zq1,☼(zo2)))   [t▦ + detail] candidate only
```

### 1.4 Quantity and mathematics

4 roots (2 partly, 2 candidate). What they make: item (2), math term (1), count (1).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `✠` partly | P a math expression (numbers and + − × ÷ ^ √ and so on) → math term (no details) | the number P | A math term, only in a closed list of places: the object of `cƒ`, an argument of `r→` and `m>`, the definition of a `zE` name. Integers and fractions. |
| `#` partly | P collection → count (+7) | the count of P | Count of the items of a collection. |
| `c∑` candidate | P collection, Q method → item (+6) | the total of P by the method Q | Sum suggests numerical calculation or aggregation. |
| `dΔ` candidate | P item, Q item, R criterion → item (+5) | the difference between P and Q under R | Difference between entities / values. |

```
g←(r→(✠(×(7,6)),✠(42)))                [✠] passes
g←(v⊨(#(zS1),zcr1))                    [#] passes
g←(v⊨(#(zS1,☼(zo2)),zcr1))             [# + detail] candidate only
g←(v⊨(c∑(zS1,zm1),zcr1))               [c∑] passes
g←(v⊨(c∑(zS1,zm1,☼(zo2)),zcr1))        [c∑ + detail] candidate only
g←(v⊨(dΔ(zo1,zo2,zcr1),zcr1))          [dΔ] passes
g←(v⊨(dΔ(zo1,zo2,zcr1,☼(zo2)),zcr1))   [dΔ + detail] candidate only
```

### 2.1 Logical core: negation, joining, quantification, implication, context

8 roots (2 established, 5 partly, 1 parked). What they make: claim (7), no signature (1).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `n¬` established | P claim or requirement → claim (+7) | it is not the case that P | Negation of a claim. |
| `∧` partly | P, Q, … (two or more, all claims or all acts) → claim, or act (no details) | P and Q and … (all of these) | Joins claims or joins acts, never a mix. Three or more nest to the right. |
| `a\|` partly | P, Q, … (two or more, all claims or all items) → claim, or collection of candidates (no details) | P or Q or … (alternatives) | Joins claims (inclusive) or lists candidates, never both in one use. |
| `∃` partly | P variable, Q claim; or P item → claim (no details) | some P satisfies Q; or P exists | Existence. `∃(v,φ)`: v is bound inside φ. Bare `∃(x)`: x exists in a stated domain. |
| `i→` established | P claim, Q claim → claim (+6) · G2 | if P then Q | Implication, condition first. Neither side is asserted. |
| `i⇒` partly | P claim, Q claim; or P claim, Q directive → claim; or conditional directive (+6) · G2 | when P, Q applies; or if P, then do Q | Conditional premise, condition first. A directive consequent only for `i!(…)`. |
| `c⊃` partly | P assumption or time, Q claim; or P criterion, Q claim → claim (+6) | within P, Q; or within the criterion P, Q | x is considered within ctx. The context is an assumption `~(P)` or a declared time name. |
| `c⇒` parked | no signature, refused (E-UNSIG) | — | A condition or logical if–then implication. |

```
h◇(i→(zq1,n¬(s@(zo1,zo2))))              [n¬] passes
h◇(i→(zq1,n¬(s@(zo1,zo2),⚓(zq3))))       [n¬ + detail] candidate only
g←(∧(v⊨(zo1,zcr1),c↝(zq1,zq2)))          [∧] passes
g←(a|(v⊨(zo1,zcr1),c↝(zq1,zq2)))         [a|] passes
g←(∃(zox,∧(∈(zox,zS1),v⊨(zox,zcr1))))    [∃] passes
h◇(c↝(i→(s@(zo1,zo2),zq1),zq2))          [i→] passes
h◇(c↝(i→(s@(zo1,zo2),zq1,⚓(zq3)),zq2))   [i→ + detail] candidate only
h◇(c↝(i⇒(s@(zo1,zo2),zq1),zq2))          [i⇒] passes
h◇(c↝(i⇒(s@(zo1,zo2),zq1,⚓(zq3)),zq2))   [i⇒ + detail] candidate only
h◇(n¬(c⊃(zt1,s∵(zq1,zq2))))              [c⊃] passes
h◇(n¬(c⊃(zt1,s∵(zq1,zq2),⚓(zq3))))       [c⊃ + detail] candidate only
```

No example for `c⇒`: the checker refuses a root with no signature.

### 2.2 Reasons, support, inference and evidence

12 roots (2 established, 5 candidate, 5 parked). What they make: claim (11), no signature (1).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `s∵` established | P claim, Q claim → claim (+6) · G2 | P supports Q | Support, support first and claim second. |
| `∵` candidate | P claim, Q claim → claim (+6) · G2 | P is given as a reason for Q † | Standalone reason-giving connective; grounds supplied or recoverable from context. |
| `r∵` candidate | P claim, Q claim → claim (+6) · G2 | P is the basis given for the inference Q † | Basis or cause given for an inference or conclusion (`∵`, because). |
| `j∵` candidate | P claim, Q claim → claim (+6) · G2 | P justifies Q † | Supply reasons, evidence, or grounds for a claim, decision, or action. |
| `e∵` candidate | P claim, Q claim → claim (+6) · G2 | P explains Q † | Supply a reason, mechanism, or justification for a statement. |
| `c∴` parked | P premise set, Q claim → claim (+6) | from the premises P it follows that Q | Therefore: reach a conclusion from premises or evidence. |
| `∴` parked | no signature, refused (E-UNSIG) | — | Conclusion/discourse marker linking an already established basis to a subsequent claim. |
| `d⊢` established | P claim or item, Q claim or item → claim (+6) · G11 | P is derived from Q | Derivation, derived item first. Does not establish the premises. |
| `i⊢` parked | P premise set, Q claim, R criterion → claim (+5) · G13 | Q is inferred from the premises P by the rules R | Derive a conclusion using premises and inference rules. |
| `l⊢` candidate | P premise set, Q claim, R criterion → claim (+5) · G13 | Q is derivable from P in the formal system R | Formal system of inference rules governing what can be derived from premises. |
| `p⊢` parked | P premise set, Q claim, R criterion → claim (+5) · G13 | Q is established from P under the rules R | Establish a conclusion under specified formal premises and inference rules. |
| `e▤` parked | P item, Q claim → claim (+6) · G22 | P is evidence bearing on Q | Information relevant to testing, supporting, or challenging a claim. |

```
g←(c↝(s∵(v⊨(zo1,zcr1),zq1),zq2))                  [s∵] passes
g←(c↝(s∵(v⊨(zo1,zcr1),zq1,⚓(zq3)),zq2))           [s∵ + detail] candidate only
h◇(n¬(∵(s∵(zq1,zq2),zq1)))                        [∵] passes
h◇(n¬(∵(s∵(zq1,zq2),zq1,⚓(zq3))))                 [∵ + detail] candidate only
h◇(s∵(r∵(⊛(zq1),zq1),zq2))                        [r∵] passes
h◇(s∵(r∵(⊛(zq1),zq1,⚓(zq3)),zq2))                 [r∵ + detail] candidate only
h◇(s∵(j∵(⊛(zq1),zq1),zq2))                        [j∵] passes
h◇(s∵(j∵(⊛(zq1),zq1,⚓(zq3)),zq2))                 [j∵ + detail] candidate only
g←(c↝(e∵(c↝(zq1,zq2),zq1),zq2))                   [e∵] passes
g←(c↝(e∵(c↝(zq1,zq2),zq1,⚓(zq3)),zq2))            [e∵ + detail] candidate only
g←(s∵(c∴(b▁(zS1),∈(zo1,zS1)),zq2))                [c∴] passes
g←(s∵(c∴(b▁(zS1),∈(zo1,zS1),⚓(zq3)),zq2))         [c∴ + detail] candidate only
g←(c↝(d⊢(c↝(zq1,zq2),zq1),zq2))                   [d⊢] passes
g←(c↝(d⊢(c↝(zq1,zq2),zq1,⚓(zq3)),zq2))            [d⊢ + detail] candidate only
h◇(i→(zq1,i⊢(b▁(zS1),i→(zq1,zq2),zcr1)))          [i⊢] passes
h◇(i→(zq1,i⊢(b▁(zS1),i→(zq1,zq2),zcr1,⚓(zq3))))   [i⊢ + detail] candidate only
h◇(n¬(l⊢(b▁(zS1),s∵(zq1,zq2),zcr1)))              [l⊢] passes
h◇(n¬(l⊢(b▁(zS1),s∵(zq1,zq2),zcr1,⚓(zq3))))       [l⊢ + detail] candidate only
g←(c↝(p⊢(b▁(zS1),c↝(zq1,zq2),zcr1),zq2))          [p⊢] passes
g←(c↝(p⊢(b▁(zS1),c↝(zq1,zq2),zcr1,⚓(zq3)),zq2))   [p⊢ + detail] candidate only
h◇(i→(zq1,e▤(zo1,i→(zq1,zq2))))                   [e▤] passes
h◇(i→(zq1,e▤(zo1,i→(zq1,zq2),⚓(zq3))))            [e▤ + detail] candidate only
```

No example for `∴`: the checker refuses a root with no signature.

### 2.3 Causation, condition, constraint and necessity

4 roots (1 established, 2 candidate, 1 parked). What they make: claim (4).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `c↝` established | P claim, Q claim → claim (+6) · G2 | P causes Q | Cause, cause first and effect second. Says neither occurred. |
| `c⊣` parked | P item, Q claim → claim (+6) · G22 | P restricts the possibility that Q † | Restrict permitted possibilities or operations. |
| `l⊣` candidate | P item, Q item → claim (+6) · G1 | P is a limit on Q † | Boundary or restriction on a quantity, operation, resource, or possibility. |
| `n□` candidate | P claim, Q claim → claim (+6) · G2 | P is required under Q † | Required relative to a specified rule, condition, or modal context, not merely preferable. |

```
g←(s∵(c↝(s∵(zq1,zq2),zq1),zq2))          [c↝] passes
g←(s∵(c↝(s∵(zq1,zq2),zq1,⚓(zq3)),zq2))   [c↝ + detail] candidate only
h◇(n¬(c⊣(zo1,s∵(zq1,zq2))))              [c⊣] passes
h◇(n¬(c⊣(zo1,s∵(zq1,zq2),⚓(zq3))))       [c⊣ + detail] candidate only
g←(i→(zq1,l⊣(zo1,zo2)))                  [l⊣] passes
g←(i→(zq1,l⊣(zo1,zo2,⚓(zq3))))           [l⊣ + detail] candidate only
g←(n¬(n□(v⊨(zo1,zcr1),zq1)))             [n□] passes
g←(n¬(n□(v⊨(zo1,zcr1),zq1,⚓(zq3))))      [n□ + detail] candidate only
```

### 2.4 Sameness, difference, comparison and order

16 roots (3 partly, 10 candidate, 3 parked). What they make: claim (16).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `s=` partly | P item, Q item → claim (+6) · G1 | P is the same as Q | Sameness relative to a criterion. |
| `s≈` parked | P item, Q item → claim (+6) · G1 | P is approximately equal to Q | Approximate equality / resemblance subject to a similarity criterion. |
| `i≡` partly | P item, Q item → claim (+6) · G1 | P is identified as Q | Identity or identification claim. |
| `m≡` parked | P item, Q item → claim (+6) · G1 | P matches Q | Match two entities or patterns under a specified criterion (not necessarily total identity). |
| `d≢` parked | P item, Q item → claim (+6) · G1 | P is told apart from Q | Tell apart by criterion. |
| `r≡` candidate | P item, Q item, R criterion → claim (+5) · G14 | P is recognized as matching Q under R † | Identify an observed entity or pattern as matching a known one (`≡` is suggestive, not a requirement of strict equality). |
| `c≡` candidate | P claim, Q claim → claim (+6) · G2 | P is compatible with Q | Compatibility across claims or states; symbol suggests equivalence, but is not the same as mere consistency. |
| `c≠` candidate | P claim, Q claim → claim (+6) · G2 | P conflicts with Q | Incompatibility or disagreement between propositions or states. |
| `d≠` candidate | P agent, Q agent, R claim → claim (+5) | P and Q hold different positions on R † | Positions do not match. |
| `b≻` candidate | P item, Q item, R criterion → claim (+5) · G14 | P is better than Q under R † | Preferable under a criterion. |
| `≈` candidate | P item, Q item, R item → claim (+5) · G15 | P is estimated as Q within R † | Standalone estimation / approximation; must distinguish relation from operation. |
| `m>` partly | P math term, Q math term; or P count, Q count → claim (+6) · G27 | P is more than Q | More than: two math terms or two counts. |
| `o≺` candidate | P item, Q item, R criterion → claim (+5) · G14 | P comes before Q under R † | A precedence or ordering relationship among items/events. |
| `v=` candidate | P item, Q item → claim (+6) · G1 | P has the value Q † | A variable or entity's value under a binding or interpretation. |
| `m∥` candidate | P item, Q item, R value, S item → claim (+4) | the Q of P is R on the scale S † | Obtain a quantitative value for a property under a specified scale and unit. |
| `n−` candidate | P item, Q criterion → claim (+6) · G7 | P is negative under Q † | Negative sign or polarity in a stated numeric, logical, or evaluative domain. |

```
g←(c↝(s=(zo1,zo2),zq2))                  [s=] passes
g←(c↝(s=(zo1,zo2,⚓(zq3)),zq2))           [s= + detail] candidate only
g←(n¬(s≈(zo1,zo2)))                      [s≈] passes
g←(n¬(s≈(zo1,zo2,⚓(zq3))))               [s≈ + detail] candidate only
h◇(c↝(i≡(zo1,zo2),zq2))                  [i≡] passes
h◇(c↝(i≡(zo1,zo2,⚓(zq3)),zq2))           [i≡ + detail] candidate only
g←(n¬(m≡(zo1,zo2)))                      [m≡] passes
g←(n¬(m≡(zo1,zo2,⚓(zq3))))               [m≡ + detail] candidate only
g←(n¬(d≢(zo1,zo2)))                      [d≢] passes
g←(n¬(d≢(zo1,zo2,⚓(zq3))))               [d≢ + detail] candidate only
g←(s∵(r≡(zo1,zo2,zcr1),zq2))             [r≡] passes
g←(s∵(r≡(zo1,zo2,zcr1,⚓(zq3)),zq2))      [r≡ + detail] candidate only
g←(c↝(c≡(c↝(zq1,zq2),zq1),zq2))          [c≡] passes
g←(c↝(c≡(c↝(zq1,zq2),zq1,⚓(zq3)),zq2))   [c≡ + detail] candidate only
h◇(s∵(c≠(⊛(zq1),zq1),zq2))               [c≠] passes
h◇(s∵(c≠(⊛(zq1),zq1,⚓(zq3)),zq2))        [c≠ + detail] candidate only
h◇(n¬(d≠(zkB,zkC,s∵(zq1,zq2))))          [d≠] passes
h◇(n¬(d≠(zkB,zkC,s∵(zq1,zq2),⚓(zq3))))   [d≠ + detail] candidate only
h◇(n¬(b≻(zo1,zo2,zcr1)))                 [b≻] passes
h◇(n¬(b≻(zo1,zo2,zcr1,⚓(zq3))))          [b≻ + detail] candidate only
h◇(n¬(≈(zo1,zo2,zo3)))                   [≈] passes
h◇(n¬(≈(zo1,zo2,zo3,⚓(zq3))))            [≈ + detail] candidate only
h◇(i→(zq1,m>(✠(×(7,6)),✠(42))))          [m>] passes
h◇(i→(zq1,m>(✠(×(7,6)),✠(42),⚓(zq3))))   [m> + detail] candidate only
h◇(c↝(o≺(zo1,zo2,zcr1),zq2))             [o≺] passes
h◇(c↝(o≺(zo1,zo2,zcr1,⚓(zq3)),zq2))      [o≺ + detail] candidate only
h◇(i→(zq1,v=(zo1,zo2)))                  [v=] passes
h◇(i→(zq1,v=(zo1,zo2,⚓(zq3))))           [v= + detail] candidate only
g←(n¬(m∥(zo1,zo2,zv1,zo3)))              [m∥] passes
g←(n¬(m∥(zo1,zo2,zv1,zo3,⚓(zq3))))       [m∥ + detail] candidate only
g←(s∵(n−(zo1,zcr1),zq2))                 [n−] passes
g←(s∵(n−(zo1,zcr1,⚓(zq3)),zq2))          [n− + detail] candidate only
```

### 2.5 Epistemic status, verification, probability and absence

13 roots (2 established, 6 candidate, 5 parked). What they make: claim (12), no kind (1).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `v⊨` established | P item, Q criterion → claim (+6) · G7 | P satisfies Q | x satisfies a criterion. A claim, not an act. |
| `f⊤` parked | P claim, Q criterion → claim (+6) · G23 | P is held established under Q | A proposition treated as established under specified evidence or context; `⊤` evokes truth. |
| `f⊥` candidate | P claim, Q criterion → claim (+6) · G23 | P is false under Q | Falsity under a specified interpretation; `⊥` evokes logical false. |
| `k✓` parked | P claim → claim (+7) · G5 | P is established | An epistemic status indicating a proposition/value is established relative to agent, context, and standards. |
| `✓` candidate | P item, Q criterion → claim (+6) · G7 | P is correct under Q | Standalone correctness relative to agreed criterion; distinct from truth or yes. |
| `✗` candidate | P item, Q criterion → claim (+6) · G7 | P is incorrect under Q | Standalone incorrectness relative to criterion; distinct from false/error. |
| `r✓` candidate | P item, Q criterion → claim (+6) · G7 | P is resolved under Q | Mark an issue as solved or closed, under stated criteria (`✓`). |
| `s✓` candidate | P item, Q item → claim (+6) · G1 | P is a candidate that meets the requirements Q † | A candidate satisfying requirements of a problem; `✓` alone does not prove independent verification. |
| `u±` parked | P value, Q value → claim (+6) | the estimate P carries the uncertainty Q | Degree, interval, or range of uncertainty associated with an estimate or state. |
| `l≥` parked | P claim → claim (+7) · G5 | the likelihood of P meets its threshold | Probability or likelihood meets a contextually specified threshold. |
| `pℙ` parked | P claim, Q value, R item → claim (+5) | the probability of P is Q under the model R | Quantitative measure of likelihood relative to model/context. |
| `p⇢` candidate | P claim, Q claim → claim (+6) · G2 | P predicts Q † | Estimate an outcome not yet observed, from available information. |
| `n0` established | nothing (an atom) → no kind (no details) | not supplied | Not supplied: the place or the role was not given. Not none, not zero, not unknown. |

```
g←(s∵(v⊨(zo1,zcr1),zq2))                    [v⊨] passes
g←(s∵(v⊨(zo1,zcr1,⚓(zq3)),zq2))             [v⊨ + detail] candidate only
h◇(s∵(f⊤(⊛(zq1),zcr1),zq2))                 [f⊤] passes
h◇(s∵(f⊤(⊛(zq1),zcr1,⚓(zq3)),zq2))          [f⊤ + detail] candidate only
g←(c↝(f⊥(c↝(zq1,zq2),zcr1),zq2))            [f⊥] passes
g←(c↝(f⊥(c↝(zq1,zq2),zcr1,⚓(zq3)),zq2))     [f⊥ + detail] candidate only
g←(n¬(k✓(v⊨(zo1,zcr1))))                    [k✓] passes
g←(n¬(k✓(v⊨(zo1,zcr1),⚓(zq3))))             [k✓ + detail] candidate only
h◇(n¬(✓(zo1,zcr1)))                         [✓] passes
h◇(n¬(✓(zo1,zcr1,⚓(zq3))))                  [✓ + detail] candidate only
h◇(s∵(✗(zo1,zcr1),zq2))                     [✗] passes
h◇(s∵(✗(zo1,zcr1,⚓(zq3)),zq2))              [✗ + detail] candidate only
h◇(s∵(r✓(zo1,zcr1),zq2))                    [r✓] passes
h◇(s∵(r✓(zo1,zcr1,⚓(zq3)),zq2))             [r✓ + detail] candidate only
g←(n¬(s✓(zo1,zo2)))                         [s✓] passes
g←(n¬(s✓(zo1,zo2,⚓(zq3))))                  [s✓ + detail] candidate only
h◇(c↝(u±(zv1,zv2),zq2))                     [u±] passes
h◇(c↝(u±(zv1,zv2,⚓(zq3)),zq2))              [u± + detail] candidate only
h◇(n¬(l≥(s∵(zq1,zq2))))                     [l≥] passes
h◇(n¬(l≥(s∵(zq1,zq2),⚓(zq3))))              [l≥ + detail] candidate only
g←(s∵(pℙ(∈(zo1,zS1),zv1,zo1),zq2))          [pℙ] passes
g←(s∵(pℙ(∈(zo1,zS1),zv1,zo1,⚓(zq3)),zq2))   [pℙ + detail] candidate only
h◇(i→(zq1,p⇢(i→(zq1,zq2),zq1)))             [p⇢] passes
h◇(i→(zq1,p⇢(i→(zq1,zq2),zq1,⚓(zq3))))      [p⇢ + detail] candidate only
g←(s=(n0,zo2))                              [n0] candidate only
```

### 2.6 Provenance and reference

5 roots (3 established, 1 partly, 1 parked). What they make: claim (5).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `s@` established | P claim or item, Q claim or item → claim (+6) · G11 | P comes from Q | Immediate source, derived item first. |
| `s@*` established | P claim or item, Q claim or item → claim (+6) · G11 | P descends from Q | Ancestry through one or more s@ steps. |
| `r@` partly | P claim or item, Q item; or P item, Q message name → claim; or the kind of P (no details) | P is found at Q; or P as it stands in the message Q | Qualified reference: x as it stands in message zUk. Also a pointer to a source. |
| `⊛` established | P claim → claim (+7) · G5 | from stored knowledge, P | Claimed origin: stated from stored knowledge, not verified. |
| `r:` parked | P item, Q item, R item → claim (+5) · G15 | P is related to Q by R | Indicate a connection between entities (:). |

```
g←(i→(zq1,s@(h⊡(zkB,zo1),zq1)))          [s@] passes
g←(i→(zq1,s@(h⊡(zkB,zo1),zq1,⚓(zq3))))   [s@ + detail] candidate only
g←(n¬(s@*(v⊨(zo1,zcr1),zq1)))            [s@*] passes
g←(n¬(s@*(v⊨(zo1,zcr1),zq1,⚓(zq3))))     [s@* + detail] candidate only
g←(c↝(r@(zq1,zUa1),zq2))                 [r@] passes
g←(s∵(⊛(∈(zo1,zS1)),zq2))                [⊛] passes
g←(s∵(⊛(∈(zo1,zS1),⚓(zq3)),zq2))         [⊛ + detail] candidate only
g←(s∵(r:(zo1,zo2,zo3),zq2))              [r:] passes
g←(s∵(r:(zo1,zo2,zo3,⚓(zq3)),zq2))       [r: + detail] candidate only
```

### 2.7 Time and sequence

9 roots (3 established, 1 partly, 3 candidate, 2 parked). What they make: claim (8), no signature (1).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `t≺` established | P claim → claim (+7) · G5 | before the reference time, P | Tense: the claim holds before the reference time. |
| `t●` established | P claim → claim (+7) · G5 | at the reference time, P | Tense: at the reference time. |
| `t▷` established | P claim → claim (+7) · G5 | after the reference time, P | Tense: after the reference time. |
| `▷` parked | P item, Q item → claim (+6) · G1 | P is followed by Q † | Standalone next/successor indicator; no execution implied. |
| `b₀` candidate | P method, Q claim → claim (+6) · G18 | the start state of P is Q † | Initial point / start state. |
| `y⋯` parked | no signature, refused (E-UNSIG) | — | Still / so far / continuing / not completed at the present point. |
| `s≺` partly | P, Q, … (two or more: claims, acts or items) → claim, act, or claim about the order of items (no details) | P, then Q, then … (in this order) | Ordered sequence over claims, acts or items. Three or more nest to the right. |
| `s◷` candidate | P item, Q item → claim (+6) · G1 | P is in the condition Q † | Condition of an entity or task at a specified time. |
| `s▷` candidate | P method, Q item, R method → claim (+5) | in the process P, the stage Q leads to R † | A stage or next operation within a process. |

```
g←(s∵(t≺(∈(zo1,zS1)),zq2))               [t≺] passes
g←(s∵(t≺(∈(zo1,zS1),⚓(zq3)),zq2))        [t≺ + detail] candidate only
h◇(s∵(t●(⊛(zq1)),zq2))                   [t●] passes
h◇(s∵(t●(⊛(zq1),⚓(zq3)),zq2))            [t● + detail] candidate only
g←(i→(zq1,t▷(h⊡(zkB,zo1))))              [t▷] passes
g←(i→(zq1,t▷(h⊡(zkB,zo1),⚓(zq3))))       [t▷ + detail] candidate only
h◇(c↝(▷(zo1,zo2),zq2))                   [▷] passes
h◇(c↝(▷(zo1,zo2,⚓(zq3)),zq2))            [▷ + detail] candidate only
g←(c↝(b₀(zm1,c↝(zq1,zq2)),zq2))          [b₀] passes
g←(c↝(b₀(zm1,c↝(zq1,zq2),⚓(zq3)),zq2))   [b₀ + detail] candidate only
r<(zkB,s≺(▶(zm1),▶(zm2),▶(zm3)))         [s≺] passes
g←(i→(zq1,s◷(zo1,zo2)))                  [s◷] passes
g←(i→(zq1,s◷(zo1,zo2,⚓(zq3))))           [s◷ + detail] candidate only
g←(c↝(s▷(zm1,zo1,zm2),zq2))              [s▷] passes
g←(c↝(s▷(zm1,zo1,zm2,⚓(zq3)),zq2))       [s▷ + detail] candidate only
```

No example for `y⋯`: the checker refuses a root with no signature.

### 2.8 Structure, description, classification and relation

18 roots (1 established, 1 partly, 16 candidate). What they make: claim (18).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `∈` established | P item, Q collection → claim (+6) · G6 | P is a member of Q | Literal membership of x in a collection. |
| `e∈` candidate | P item, Q item → claim (+6) · G1 | P is an instance of Q † | An instance belonging to a class or illustrating a concept or rule. |
| `o\|` candidate | P item, Q collection → claim (+6) · G6 | P is one of the candidates Q | One available candidate choice, or an explicitly specified set of candidates. |
| `c◉` candidate | P item, Q collection → claim (+6) · G6 | P is a central representation of Q † | A central representation for an idea or abstraction. |
| `d⋮` candidate | P item, Q collection → claim (+6) · G6 | P has the properties Q † | Express properties / characteristics. |
| `p▦` candidate | P item, Q collection → claim (+6) · G6 | P is a pattern among Q † | An identifiable arrangement or regularity among properties/relations. |
| `s▦` candidate | P item, Q collection → claim (+6) · G6 | P is an arrangement of Q † | Arrangement of elements and their relationships. |
| `s⊞` candidate | P item, Q collection, R item → claim (+5) | P is a system of Q with R † | Functional whole composed of interacting components. |
| `m⊞` candidate | P item, Q item → claim (+6) · G1 | P is a model of Q † | A structured representation of a system, process, or relationship. |
| `m↦` candidate | P item, Q item → claim (+6) · G1 | P is mapped to the meaning Q † | A mapping from an expression to its semantic representation. |
| `k#` candidate | P item, Q item → claim (+6) · G1 | P is the key of Q † | A scope-defined identifier or lookup key for an item, record, or value. |
| `l↔` candidate | P item, Q item → claim (+6) · G1 | P is related to Q † | Relationship between two entities or pieces of information; not necessarily symmetric. |
| `↔` candidate | P item, Q item → claim (+6) · G1 | P is connected with Q † | Standalone connection operator; directionality requires operands/type. |
| `r∩` candidate | P item, Q item → claim (+6) · G1 | P overlaps with Q † | Indicate overlap with the current objective or context (`∩`, not necessarily literal set intersection). |
| `s≔` candidate | P item, Q item, R item → claim (+5) · G15 | P is declared to have the state Q in R † | Declare an entity's state or assigned value; English noun/verb scope requires later clarification. |
| `⊡` partly | P item → claim (+7) | P is retained and accessible | x is retained and accessible. Not "unchanged". |
| `p?` candidate | P claim, Q claim → claim (+6) · G2 | P is still open, pending Q † | A task/question/requirement still requiring a resolution. |
| `i←` candidate | P item, Q method → claim (+6) | P flows into the process Q † | Information flows into a process from a specified perspective. |

```
h◇(s∵(∈(zo1,zS1),zq2))               [∈] passes
h◇(s∵(∈(zo1,zS1,⚓(zq3)),zq2))        [∈ + detail] candidate only
g←(i→(zq1,e∈(zo1,zo2)))              [e∈] passes
g←(i→(zq1,e∈(zo1,zo2,⚓(zq3))))       [e∈ + detail] candidate only
g←(n¬(o|(zo1,zS1)))                  [o|] passes
g←(n¬(o|(zo1,zS1,⚓(zq3))))           [o| + detail] candidate only
h◇(i→(zq1,c◉(zo1,zS1)))              [c◉] passes
h◇(i→(zq1,c◉(zo1,zS1,⚓(zq3))))       [c◉ + detail] candidate only
g←(s∵(d⋮(zo1,zS1),zq2))              [d⋮] passes
g←(s∵(d⋮(zo1,zS1,⚓(zq3)),zq2))       [d⋮ + detail] candidate only
h◇(c↝(p▦(zo1,zS1),zq2))              [p▦] passes
h◇(c↝(p▦(zo1,zS1,⚓(zq3)),zq2))       [p▦ + detail] candidate only
g←(s∵(s▦(zo1,zS1),zq2))              [s▦] passes
g←(s∵(s▦(zo1,zS1,⚓(zq3)),zq2))       [s▦ + detail] candidate only
g←(i→(zq1,s⊞(zo1,zS1,zo2)))          [s⊞] passes
g←(i→(zq1,s⊞(zo1,zS1,zo2,⚓(zq3))))   [s⊞ + detail] candidate only
h◇(i→(zq1,m⊞(zo1,zo2)))              [m⊞] passes
h◇(i→(zq1,m⊞(zo1,zo2,⚓(zq3))))       [m⊞ + detail] candidate only
h◇(n¬(m↦(zo1,zo2)))                  [m↦] passes
h◇(n¬(m↦(zo1,zo2,⚓(zq3))))           [m↦ + detail] candidate only
g←(s∵(k#(zo1,zo2),zq2))              [k#] passes
g←(s∵(k#(zo1,zo2,⚓(zq3)),zq2))       [k# + detail] candidate only
g←(s∵(l↔(zo1,zo2),zq2))              [l↔] passes
g←(s∵(l↔(zo1,zo2,⚓(zq3)),zq2))       [l↔ + detail] candidate only
h◇(n¬(↔(zo1,zo2)))                   [↔] passes
h◇(n¬(↔(zo1,zo2,⚓(zq3))))            [↔ + detail] candidate only
g←(i→(zq1,r∩(zo1,zo2)))              [r∩] passes
g←(i→(zq1,r∩(zo1,zo2,⚓(zq3))))       [r∩ + detail] candidate only
h◇(c↝(s≔(zo1,zo2,zo3),zq2))          [s≔] passes
h◇(c↝(s≔(zo1,zo2,zo3,⚓(zq3)),zq2))   [s≔ + detail] candidate only
g←(c↝(⊡(zo1),zq2))                   [⊡] passes
g←(c↝(⊡(zo1,⚓(zq3)),zq2))            [⊡ + detail] candidate only
h◇(n¬(p?(s∵(zq1,zq2),zq1)))          [p?] passes
h◇(n¬(p?(s∵(zq1,zq2),zq1,⚓(zq3))))   [p? + detail] candidate only
g←(i→(zq1,i←(zo1,zm1)))              [i←] passes
g←(i→(zq1,i←(zo1,zm1,⚓(zq3))))       [i← + detail] candidate only
```

### 2.9 Agents: holding, attitude and interaction states

15 roots (1 established, 13 candidate, 1 parked). What they make: claim (14), no signature (1).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `h⊡` established | P agent, Q item → claim (+6) · G12 | P has Q | The holder has the item (holder first, an agent only). |
| `b~` candidate | P agent, Q claim → claim (+6) · G17 | P holds the stance that Q | Held but not necessarily verified stance. |
| `t~` candidate | P agent, Q item, R item → claim (+5) · G30 | P relies on Q for R † | Context-dependent reliance on a source, claim or process with defeasible confidence. |
| `i◎` candidate | P agent, Q claim → claim (+6) · G17 | P aims at Q | The target or purpose of an action/message. |
| `o◎` candidate | P method, Q claim → claim (+6) · G18 | P is meant to attain Q | A target or criterion that a task is intended to attain. |
| `g◎` parked | no signature, refused (E-UNSIG) | — | Defined target / desired outcome of a task or process. |
| `n!` candidate | P agent, Q item → claim (+6) · G12 | P needs Q | A task, agent, or goal requires particular information, a resource, or an action. |
| `r−` candidate | P agent, Q item → claim (+6) · G12 | P declines Q | Exclude or decline adoption of a candidate (`−`). |
| `g▷` candidate | P agent, Q claim, R method → claim (+5) | P directs, for the target Q, the next operation R † | Directing progression or next operation with respect to a target. |
| `f▷` candidate | P agent, Q method → claim (+6) | P proceeds by Q | Proceed in a sequence or follow a specified instruction. |
| `h+` candidate | P agent, Q agent, R method → claim (+5) | P helps Q by R † | Add assistance, information, or capacity to a task. |
| `s◇` candidate | P agent, Q agent, R item → claim (+5) · G29 | P presents R to Q as a candidate † | Present a candidate, proposal, or possibility for consideration. |
| `f↩` candidate | P item, Q item → claim (+6) · G1 | P is feedback about Q † | Information directed back about a previous output or action. |
| `o▤` candidate | P agent, Q item, R item, S item → claim (+4) | P observes Q, recorded as R and S † | Acquire and register an observation concerning an object/event. |
| `u✓` candidate | P agent, Q item, R item → claim (+5) · G30 | P has recovered the intended meaning of Q to the standard R † | A message's intended interpretation has been recovered to the specified criterion. |

```
g←(s∵(h⊡(zkB,zo1),zq2))                      [h⊡] passes
g←(s∵(h⊡(zkB,zo1,⚓(zq3)),zq2))               [h⊡ + detail] candidate only
g←(s∵(b~(zkB,∈(zo1,zS1)),zq2))               [b~] passes
g←(s∵(b~(zkB,∈(zo1,zS1),⚓(zq3)),zq2))        [b~ + detail] candidate only
h◇(i→(zq1,t~(zkB,zo1,zo2)))                  [t~] passes
h◇(i→(zq1,t~(zkB,zo1,zo2,⚓(zq3))))           [t~ + detail] candidate only
g←(s∵(i◎(zkB,∈(zo1,zS1)),zq2))               [i◎] passes
g←(s∵(i◎(zkB,∈(zo1,zS1),⚓(zq3)),zq2))        [i◎ + detail] candidate only
h◇(s∵(o◎(zm1,⊛(zq1)),zq2))                   [o◎] passes
h◇(s∵(o◎(zm1,⊛(zq1),⚓(zq3)),zq2))            [o◎ + detail] candidate only
g←(n¬(n!(zkB,zo1)))                          [n!] passes
g←(n¬(n!(zkB,zo1,⚓(zq3))))                   [n! + detail] candidate only
h◇(i→(zq1,r−(zkB,zo1)))                      [r−] passes
h◇(i→(zq1,r−(zkB,zo1,⚓(zq3))))               [r− + detail] candidate only
g←(c↝(g▷(zkB,c↝(zq1,zq2),zm1),zq2))          [g▷] passes
g←(c↝(g▷(zkB,c↝(zq1,zq2),zm1,⚓(zq3)),zq2))   [g▷ + detail] candidate only
h◇(i→(zq1,f▷(zkB,zm1)))                      [f▷] passes
h◇(i→(zq1,f▷(zkB,zm1,⚓(zq3))))               [f▷ + detail] candidate only
g←(n¬(h+(zkB,zkC,zm1)))                      [h+] passes
g←(n¬(h+(zkB,zkC,zm1,⚓(zq3))))               [h+ + detail] candidate only
h◇(i→(zq1,s◇(zkB,zkC,zo1)))                  [s◇] passes
h◇(i→(zq1,s◇(zkB,zkC,zo1,⚓(zq3))))           [s◇ + detail] candidate only
h◇(n¬(f↩(zo1,zo2)))                          [f↩] passes
h◇(n¬(f↩(zo1,zo2,⚓(zq3))))                   [f↩ + detail] candidate only
g←(i→(zq1,o▤(zkB,zo1,zo2,zo3)))              [o▤] passes
g←(i→(zq1,o▤(zkB,zo1,zo2,zo3,⚓(zq3))))       [o▤ + detail] candidate only
h◇(n¬(u✓(zkB,zo1,zo2)))                      [u✓] passes
h◇(n¬(u✓(zkB,zo1,zo2,⚓(zq3))))               [u✓ + detail] candidate only
```

No example for `g◎`: the checker refuses a root with no signature.

### 3.1 Action constructors and role markers

10 roots (10 established). What they make: role marker (7), act (3).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `cƒ` established | P item or math term, then role markers → act (+7) | compute P | Action root: compute. The object first, then role markers. |
| `o→` established | P item or math term, then role markers → act (+7) | output P | Action root: output. The object first, then role markers. |
| `a+` established | P item or math term, then role markers → act (+7) | accept P | Action root: accept. The object first, then role markers. |
| `⌘` established | P method → role marker (no details) | by the method P | Role marker: method. |
| `⚙` established | P item → role marker (no details) · G10 | using P | Role marker: instrument. |
| `↣` established | P item → role marker (no details) · G10 | for the recipient P | Role marker: recipient. |
| `☞` established | P item → role marker (no details) · G10 | to the destination P | Role marker: destination. |
| `☼` established | P item → role marker (no details) · G10 | from the source P | Role marker: source. |
| `⚓` established | P claim or item → role marker (no details) | on the basis of P | Role marker: basis. |
| `♙` established | P agent → role marker (no details) | done by P | Role marker: agent. |

```
i!(cƒ(zo1,♙(zkA),⌘(zm1)))                                          [cƒ] passes
i!(cƒ(zo1,⌘(zm1),⚙(zo3),↣(zo2),☞(zo3),☼(zo2),⚓(zq1),♙(zkA)))       [cƒ + detail] passes
r<(zkB,o→(zo1,♙(zkA),⌘(zm1)))                                      [o→] passes
r<(zkB,o→(zo1,⌘(zm1),⚙(zo3),↣(zo2),☞(zo3),☼(zo2),⚓(zq1),♙(zkA)))   [o→ + detail] passes
i!(a+(zo1,♙(zkA),⌘(zm1)))                                          [a+] passes
i!(a+(zo1,⌘(zm1),⚙(zo3),↣(zo2),☞(zo3),☼(zo2),⚓(zq1),♙(zkA)))       [a+ + detail] passes
g←(cƒ(zo1,⌘(zm1)))                                                 [⌘] passes
g←(cƒ(zo1,⚙(zo1)))                                                 [⚙] passes
g←(cƒ(zo1,↣(zo1)))                                                 [↣] passes
g←(cƒ(zo1,☞(zo1)))                                                 [☞] passes
g←(cƒ(zo1,☼(zo1)))                                                 [☼] passes
g←(cƒ(zo1,⚓(h⊡(zkB,zo1))))                                         [⚓] passes
g←(cƒ(zo1,♙(zkB)))                                                 [♙] passes
```

### 3.2 Act verbs

11 roots (10 candidate, 1 parked). What they make: act (11).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `c?` candidate | P item, Q criterion → act (+6) · G19 | check whether P meets Q | Investigate whether a statement meets a criterion or is correct. |
| `c≶` candidate | P item, Q item, R criterion → act (+5) | compare P and Q on R | Compare values or objects on relevant dimensions. |
| `e⋯` candidate | P item, Q method → act (+6) | explore P using Q | Investigate an open set of possibilities without a fixed outcome. |
| `i?` candidate | P question, Q method → act (+6) | investigate the question P by Q | Pursue evidence to address an unresolved question. |
| `t⋯` candidate | P agent, Q item → act (+6) · G31 | P considers Q | Reason/consider/process a target under the current context, without asserting that a final result is available. |
| `u↦` candidate | P agent, Q item, R item → act (+5) · G32 | P applies Q to R † | Apply a resource, rule, tool, or method to a relevant target. |
| `l↻` candidate | P agent, Q item, R item → act (+5) · G32 | P updates Q based on R † | Update a representation or behaviour based on information, evidence, or feedback. |
| `i↑` candidate | P item, Q criterion → act (+6) · G19 | improve P in Q | A positive change relative to a specified quality measure. |
| `t⚖` candidate | P item, Q collection, R criterion → act (+5) | test P with the cases Q against R | Apply specified test cases or criteria to assess an object, claim or behavior. |
| `a<` candidate | P agent, Q question → act (+6) | ask P the question Q | Submit a question/request for information. |
| `q<` parked | P agent, Q item → act (+6) · G31 | demand from P the information Q | Directed demand for information, retrieval, or an answer. |

```
r<(zkB,c?(zo1,zcr1))              [c?] passes
r<(zkB,c?(zo1,zcr1,♙(zkA)))       [c? + detail] candidate only
r<(zkB,c≶(zo1,zo2,zcr1))          [c≶] passes
r<(zkB,c≶(zo1,zo2,zcr1,♙(zkA)))   [c≶ + detail] candidate only
r<(zkB,e⋯(zo1,zm1))               [e⋯] passes
r<(zkB,e⋯(zo1,zm1,♙(zkA)))        [e⋯ + detail] candidate only
r<(zkB,i?(?⊤(zq1),zm1))           [i?] passes
r<(zkB,i?(?⊤(zq1),zm1,♙(zkA)))    [i? + detail] candidate only
r<(zkB,t⋯(zkB,zo1))               [t⋯] passes
r<(zkB,t⋯(zkB,zo1,♙(zkA)))        [t⋯ + detail] candidate only
r<(zkB,u↦(zkB,zo1,zo2))           [u↦] passes
r<(zkB,u↦(zkB,zo1,zo2,♙(zkA)))    [u↦ + detail] candidate only
r<(zkB,l↻(zkB,zo1,zo2))           [l↻] passes
r<(zkB,l↻(zkB,zo1,zo2,♙(zkA)))    [l↻ + detail] candidate only
r<(zkB,i↑(zo1,zcr1))              [i↑] passes
r<(zkB,i↑(zo1,zcr1,♙(zkA)))       [i↑ + detail] candidate only
r<(zkB,t⚖(zo1,zS1,zcr1))          [t⚖] passes
r<(zkB,t⚖(zo1,zS1,zcr1,♙(zkA)))   [t⚖ + detail] candidate only
r<(zkB,a<(zkB,?⊤(zq1)))           [a<] passes
r<(zkB,a<(zkB,?⊤(zq1),♙(zkA)))    [a< + detail] candidate only
i!(q<(zkB,zo1))                   [q<] passes
i!(q<(zkB,zo1,♙(zkA)))            [q< + detail] candidate only
```

### 3.3 Execution, completion, retry, decision and result

8 roots (2 established, 4 partly, 2 parked). What they make: act (7), claim (1).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `▶` partly | P method → act (+7) | run P | Execution trigger. Does not assert completion. |
| `c■` partly | P act → act or claim (+7) · G21 | complete P; or P is completed | Completion, as an act or as the completed state. |
| `⤿` partly | P act → act (+7) · G21 | retry P | Retry or repeat an operation. Not a revision. |
| `d⊙` parked | P item → act (+7) | decide among P | Choose among options and settle a decision. |
| `d↦` established | P value, Q item → act or claim (+6) | determine the value P from Q; or the value P is determined from Q | Determine a value from information. An act, or a claim by position. |
| `v✓` established | P claim or item, Q criterion → act or claim (+6) | verify P against Q; or P is verified against Q | Verify against a criterion. An act, or a claim by position. |
| `c✓` parked | P item, Q claim → act (+6) | confirm P with Q † | Confirm prior content against supporting evidence or criteria. |
| `r→` partly | P math term, Q math term → claim (+6) · G27 | the value of P equals Q | Value claim: the value of a equals the value of b. Atemporal. |

```
i!(▶(zm1))                            [▶] passes
i!(▶(zm1,♙(zkA)))                     [▶ + detail] candidate only
i!(c■(▶(zm1)))                        [c■] passes
i!(c■(▶(zm1),♙(zkA)))                 [c■ + detail] candidate only
r<(zkB,⤿(▶(zm1)))                     [⤿] passes
r<(zkB,⤿(▶(zm1),♙(zkA)))              [⤿ + detail] candidate only
i!(d⊙(zo1))                           [d⊙] passes
i!(d⊙(zo1,♙(zkA)))                    [d⊙ + detail] candidate only
r<(zkB,d↦(zv1,zo1))                   [d↦] passes
r<(zkB,d↦(zv1,zo1,♙(zkA)))            [d↦ + detail] candidate only
r<(zkB,v✓(h⊡(zkB,zo1),zcr1))          [v✓] passes
r<(zkB,v✓(h⊡(zkB,zo1),zcr1,♙(zkA)))   [v✓ + detail] candidate only
i!(c✓(zo1,s@(zo1,zo2)))               [c✓] passes
i!(c✓(zo1,s@(zo1,zo2),♙(zkA)))        [c✓ + detail] candidate only
g←(n¬(r→(✠(×(7,6)),✠(42))))           [r→] passes
g←(n¬(r→(✠(×(7,6)),✠(42),⚓(zq3))))    [r→ + detail] candidate only
```

### 3.4 Directives and requirements

3 roots (3 partly). What they make: directive (2), requirement (1).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `i!` partly | P act → directive (+7) | do P | Directive or action requirement. Asks, does not report. |
| `r<` partly | P agent, Q act → directive (+6) | ask P to Q | Request: the party asked, then the act. |
| `r□` partly | P claim; or P conditional directive → requirement (+7) | it is required that P; or it is required: P | Requirement. A standalone top-level `r□(P)` has requirement force. |

```
i!(▶(zm1))               [i!] passes
i!(▶(zm1),☼(zo2))        [i! + detail] candidate only
r<(zkB,▶(zm1))           [r<] passes
r<(zkB,▶(zm1),☼(zo2))    [r< + detail] candidate only
r□(s@(zo1,zo2))          [r□] passes
r□(s@(zo1,zo2),☼(zo2))   [r□ + detail] candidate only
```

### 4.1 Question formers

7 roots (2 established, 4 candidate, 1 parked). What they make: question (6), no signature (1).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `?=` established | P variable, Q claim → question (no details) | which P satisfies Q? | Open question: the value a bound variable takes. |
| `?⊤` established | P claim → question (+7) · G8 | is it so that P? | Yes-or-no question about a claim. Three answers: `g←(c)`, `g←(n¬(c))`, `u?(c)`. |
| `?◷` candidate | P claim → question (+7) · G8 | when is it so that P? | Ask for event time or temporal position. |
| `?@` candidate | P claim → question (+7) · G8 | where is it so that P? | Ask for the location or position of a referent. |
| `?⊙` candidate | P variable, Q collection, R claim → question (no details) | which P of Q satisfies R? | Request choice/identification of an item from alternatives. |
| `?∵` candidate | P claim → question (+7) · G8 | why is it so that P? | Request reasons, grounds or causes. |
| `?` parked | no signature, refused (E-UNSIG) | — | A standalone question marker (contextual interrogative) and proposed general-purpose interrogative modifier. |

```
?=(zox,∈(zox,zS1))         [?=] passes
?⊤(⊛(zq1))                 [?⊤] passes
?⊤(⊛(zq1),⚓(zq3))          [?⊤ + detail] candidate only
?◷(s@(zo1,zo2))            [?◷] passes
?◷(s@(zo1,zo2),⚓(zq3))     [?◷ + detail] candidate only
?@(c↝(zq1,zq2))            [?@] passes
?@(c↝(zq1,zq2),⚓(zq3))     [?@ + detail] candidate only
?⊙(zox,zS1,v⊨(zox,zcr1))   [?⊙] candidate only
?∵(⊛(zq1))                 [?∵] passes
?∵(⊛(zq1),⚓(zq3))          [?∵ + detail] candidate only
```

The line for `?⊙` is `candidate only` although it has no detail: your pinned checker accepts a bound variable only inside `∃` and `?=` (section 9).

No example for `?`: the checker refuses a root with no signature.

### 4.2 Answer forms

3 roots (1 candidate, 1 parked, 1 excluded). What they make: claim (2), no signature (1).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `n⊘` parked | P mentioned question → claim (+7) · G28 | no, as to P | A negative response or refusal concerning an identified question, proposition, or request. |
| `y✓` candidate | P mentioned question → claim (+7) · G28 | yes, as to P | Affirmative response or approval. |
| `a>` excluded | no signature, refused (E-UNSIG) | — | Provide a response to a question. |

```
h◇(s∵(n⊘(⌜?⊤(zq1)⌝),zq2))          [n⊘] passes
h◇(s∵(n⊘(⌜?⊤(zq1)⌝,⚓(zq3)),zq2))   [n⊘ + detail] candidate only
h◇(n¬(y✓(⌜?⊤(zq1)⌝)))              [y✓] passes
h◇(n¬(y✓(⌜?⊤(zq1)⌝,⚓(zq3))))       [y✓ + detail] candidate only
```

No example for `a>`: the checker refuses a root with no signature.

### 5.1 Status force

5 roots (5 established). What they make: line (5).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `g←` established | P claim → line (+7) · G4 | supplied: P | Force: supply the claim. Does not verify it. |
| `h◇` established | P claim → line or claim (+7) · G4 | as a hypothesis: P; or it is hypothesized that P | Force: put forward as a tentative hypothesis. |
| `p◇` established | P claim → line or claim (+7) · G4 | admissible: P; or it is admissible that P | Force: admissible under the context. |
| `u?` established | P claim → line or claim (+7) · G4 | not known: P; or it is not known that P | Force: not known. |
| `u~` established | P claim → line or claim (+7) · G4 | not established: P; or it is not established that P | Force: not established at the required standard. |

```
g←(∈(zo1,zS1))            [g←] passes
g←(∈(zo1,zS1),⚓(zq3))     [g← + detail] candidate only
h◇(v⊨(zo1,zcr1))          [h◇] passes
h◇(v⊨(zo1,zcr1),⚓(zq3))   [h◇ + detail] candidate only
p◇(v⊨(zo1,zcr1))          [p◇] passes
p◇(v⊨(zo1,zcr1),⚓(zq3))   [p◇ + detail] candidate only
u?(∈(zo1,zS1))            [u?] passes
u?(∈(zo1,zS1),⚓(zq3))     [u? + detail] candidate only
u~(s@(zo1,zo2))           [u~] passes
u~(s@(zo1,zo2),⚓(zq3))    [u~ + detail] candidate only
```

### 5.2 Dialogue acts

8 roots (3 established, 4 partly, 1 candidate). What they make: line (7), assumption (1).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `a.` partly | P anything → line (+7) · G9 | received: P | Acknowledge receipt, not agreement. |
| `a=` established | P claim or declaration → line (+7) · G16 | agreed: P | Agree with a claim or a declaration. |
| `a?` established | P anything → line (+7) · G9 | unclear: P | Mark an ambiguity or an unresolved line. |
| `p↗` established | P claim or declaration → line (+7) · G16 | proposed, not adopted: P | Propose without adopting. |
| `e✗` partly | P anything → line (+7) · G9 | error in P | Marks x as containing an error. |
| `r↻` partly | P anything → line (+7) · G9 | revised: P | Marks x as revised. Whole-message withdrawal. |
| `p▁` candidate | P claim → line (+7) · G4 | taken as a starting point: P | A proposition taken as a starting input for reasoning. |
| `~` partly | P claim; or P criterion → assumption (+7) | assume P | Adopts c as a temporary premise. Not asserted. |

```
a.(zq1)                   [a.] passes
a.(zq1,⚓(zq3))            [a. + detail] candidate only
a=(v⊨(zo1,zcr1))          [a=] passes
a=(v⊨(zo1,zcr1),⚓(zq3))   [a= + detail] candidate only
a?(zq1)                   [a?] passes
a?(zq1,⚓(zq3))            [a? + detail] candidate only
p↗(s∵(zq1,zq2))           [p↗] passes
p↗(s∵(zq1,zq2),⚓(zq3))    [p↗ + detail] candidate only
e✗(zq1)                   [e✗] passes
e✗(zq1,⚓(zq3))            [e✗ + detail] candidate only
r↻(zq1)                   [r↻] passes
r↻(zq1,⚓(zq3))            [r↻ + detail] candidate only
p▁(s∵(zq1,zq2))           [p▁] passes
p▁(s∵(zq1,zq2),⚓(zq3))    [p▁ + detail] candidate only
~(i→(zq1,zq2))            [~] passes
~(i→(zq1,zq2),☼(zo2))     [~ + detail] candidate only
```

### 6.1 Messages: identity, transmission and answer links

3 roots (2 by use, 1 candidate). What they make: declaration (the header) (1), claim (1), line (the answer link) (1).

| Root | Shape | Pattern | Table's gloss |
| --- | --- | --- | --- |
| `m▤` by use | P message name, Q agent; or P agent, Q agent, R item → declaration (the header); or claim (+6) | message P from Q; or the message R from P to Q | Message header, the first line of a message: `m▤(zU,zk)`. One sender per message. |
| `r←` candidate | P agent, Q agent, R item → claim (+5) · G29 | R is directed to Q by P † | Information directed inward to a recipient (`←`). |
| `r>` by use | P message name, Q mentioned question, R line; or P item, Q item → line (the answer link); or claim (+5) | answer to Q of message P: R; or P answers Q | Answer link: `r>(zUk,⌜Q⌝,W)` answers question Q of message zUk; W is `g←(A)` or `u?(A)`. |

```
m▤(zUa1,zkA)                     [m▤] passes
h◇(n¬(r←(zkB,zkC,zo1)))          [r←] passes
h◇(n¬(r←(zkB,zkC,zo1,⚓(zq3))))   [r← + detail] candidate only
r>(zUb1,⌜?⊤(zq1)⌝,g←(zq1))       [r>] passes
```

## 9. What the checker must change

On 1 November (03:29) you ruled that the grammar comes first and the checker follows. This list says what the checker must change so that it reads every rule in this book. C-1 to C-5 are made in a candidate checker, `ucl_check_rb.py`, a copy of your pinned `ucl_check.py` in which 81 lines differ. C-13 (r3) is made in checker g3, `ucl_check_g3.py`, which is the candidate plus the `n0` spelling and one more edit, the `NO_DETAIL` words `m▤` and `r>` that grammar C-r2 proposes as ◆2 and that you have not ruled on (C-11 stays open). C-6 to C-12 wait for a ruling or for symbols. Your pinned files are not touched.

**Made in the candidate**

| # | Change | Rules | Pinned checker today | Candidate checker |
| --- | --- | --- | --- | --- |
| C-1 | `d≔` takes 2k arguments: k names, then k definitions in the same order | B-27, B-28 | More than two arguments: E-SYNTAX "bad d≔" | Reads k declarations in order, each under today's rules (E-REDECL, E-DEF, E-UNDECL). An odd number of arguments is E-ARITY |
| C-2 | `n0` is an argument | B-19 to B-22 | A bare `n0` is E-UNSIG (the old table makes it a root with two arguments). The word `null` is E-SYNTAX | Fits every place. Refused as a joiner operand (E-NULL), as a line (E-LINE), as the name in `d≔` (E-DEF) and as a bound variable (E-BIND). Every `n0` in a core place prints the warning NU, and an `n0` after the core places prints none. The candidate reads the word `null` for this; g3 reads `n0` (C-13) |
| C-3 | Every root takes details: role markers after its core places | B-13, B-15, B-17, B-18 | An extra argument is E-ARITY. Only the three action roots take markers | Markers after the core places, each at most once (E-ROLE), each of the kind the marker asks (E-CAT), 8 arguments in all (E-ARITY). Not for the joiners, the binders, `r@`, `d≔`, the markers themselves, the atoms `t` `0` `⊤` `x` `w` `n` `n0`, `⌜ ⌝` and `✠` |
| C-4 | The action roots accept `n0` and stop at 8 arguments | B-14, B-19 | No `n0` as a placeholder. No stated limit | `n0` for a role that is not given. A ninth argument is E-ARITY |
| C-5 | `?⊙` binds its variable | B-9 | Every `?⊙` line fails (E-CAT): a bound variable is accepted only inside `∃` and `?=` | `?⊙(v,S,φ)` binds like `?=`: S is a collection, a question holds one binder, v occurs in φ |

**Waiting for a ruling or for symbols**

| # | Change | Rules | What it waits for |
| --- | --- | --- | --- |
| C-6 | Term roots for numbers, quantities, clock times, dates and zones | B-40, B-41 | A symbol and a signature for each. The first of them is the first root that makes a time (B-44) |
| C-7 | A criterion builder and a criterion marker | B-43 | Symbols. The binder code of C-5 widens to a third binder, one that makes a criterion |
| C-8 | Cb2's nine words | B-42 | Your ruling on each, and on the wording of `y▸` and `f⊂`. Nine more rows in the table |
| C-9 | The six roots without a signature | B-10 | A signature each, or removal from the table. Until then the checker refuses them (E-UNSIG) |
| C-10 | An act among joiner claims | B-8 | The rule as written refuses mixed operands (E-MIX). Today's checker accepts `∧(claim, act)` through B-5, and the candidate keeps that |
| C-11 | Headers and answer links with details | B-15 | `m▤` and `r>` take details like any root. A header with a detail is no header. A file that starts with one is reported as having no message, and under a `===` separator the session checker reports S01. The candidate keeps the generic rule |
| C-12 | The pin in your session checker | none | `silex_check.py` refuses a base whose hash differs from its pin. A copy, `silex_check_rb.py`, carries the candidate's hash. Adoption means a new pin |

**Made in checker g3 (r3)**

| # | Change | Rules | Candidate checker | Checker g3 |
| --- | --- | --- | --- | --- |
| C-13 | The placeholder is written `n0`; the table's `n0` becomes an atom | B-19 to B-22 | Reads the word `null`. `n0(P,Q)` is the old claim root | Reads a bare `n0` (not followed by `(` or a letter or digit) as the placeholder, with the same rules as C-2. `n0(…)` is E-ARITY. The word `null` is E-SYNTAX. In the table, `n0` has the signature `atom:Null`, status established, family 2.5; the old reading "the field P has no value in Q" is withdrawn from this glyph |

**What was run.** On the 161 lines of your 11 regress files and of the two rounds of the six pilot sessions (the `=== id sender ===` separator lines are not counted), the candidate gives the same verdict, kind, basis and warnings as the pinned checker on every line. The pinned checker passes 157 of them and refuses 4 (E-UNSIG, E-ARITY, E-CAT, E-DEF), and the candidate refuses the same 4 with the same errors. The 21 candidate tests pass, and 76 test lines give the verdicts that sections 3 to 6 state, among them every full line that those sections show. Of the 353 example lines in section 8, 191 also pass the pinned checker and 162 pass only the candidate: 161 lines with a detail and the line for `?⊙`. The six pilot sessions in the one-line form pass your session checker when it runs on the candidate. A pass is evidence of form, protocol and plausibility. It is not evidence that two readers take the same meaning.

**Hashes.** Pinned `ucl_check.py` `5b9823b0`, the table `07a31dec`, your `silex_check.py` `754d1103`, the candidate `96785cf8` and the candidate session checker `f6366587` (first eight characters of each; the full hashes and the files are in the zip). Checker g3 `3ec4e639`, the n0 table `d144c383`, the g3 session checker `09486de0`.

## 10. Open points, each with my default

These decisions are yours. Where you do not rule, the default stands and the book is written that way. Tell me the numbers you want changed, and every other default stands.

| # | Open point | My default |
| --- | --- | --- |
| OP-1 | `n0`: what it means (B-19 to B-22) | Ruled on 1 November, 07:29: the spelling is `n0`, the symbol of the table, not the word `null` and not `∅`. It means *not supplied*, not none, not zero and not unknown. A claim with `n0` in a core place is incomplete, and a reader marks `a?` when it sits under `n¬`, `i→` or `?⊤`. |
| OP-2 | Details on every root, and which marker goes with which root (B-15, B-17, B-18) | Every root takes details except those B-15 lists. Details are optional and unordered (B-18). The grammar does not refuse a marker that makes no sense for the root, such as a recipient on a sameness claim. A reader marks `a?`. Layer 3 of your checker has no rule for it today, and one can be added. |
| OP-3 | Roots for numbers, quantities, clock times, dates and zones; a time on an act; decimals and units (B-38 to B-41) | No symbols are chosen yet. Each term root makes a math term or a time and takes its parts as arguments, with `n0` for a part that is missing. A time stays on a claim (`c⊃`) until these roots exist, and then I propose a *when* marker so that an act can carry one. Decimals stay out, and a number with a unit goes through the quantity root. |
| OP-4 | The criterion builder and a criterion marker (B-43) | A root that makes a criterion from a claim with a bound variable, and a marker for a criterion detail. No symbols are chosen. Until then a criterion is a declared name with a scaffold. |
| OP-5 | Cb2's nine words (B-42) | None is adopted. D's blind readings stay as recorded, and the wording of `y▸` and `f⊂` is yours to rule. |
| OP-6 | `?⊙` as a binder (B-9) | Yes. It binds like `?=`, and the candidate reads it (C-5). |
| OP-7 | An act among joiner claims (B-8) | Keep today's behaviour, which B-5 explains. If you want E-MIX for any act among claims, say so and C-10 moves to the made list. |
| OP-8 | Headers and answer links with details (B-15) | Keep B-15 as written. A header with a detail is no header: the session checker reports that the file has no message, or S01 under a `===` separator. |
| OP-9 | Parked roots, and the six roots without a signature (B-10) | The 30 parked roots stay parked: they are not applied, and a reader answers `a?`. The six roots without a signature (five parked, and `a>` excluded) stay refused (E-UNSIG). |
| OP-10 | Roots of one shape (B-45) | The gloss decides. No root is merged or dropped before the blind readers of phase 4 show whether two readers keep neighbours apart. |
| OP-11 | The English patterns and the † roots (B-46) | The patterns are proposals. They are the shared basis of the two programs, English to SILEX and SILEX to English. A † pattern is not relied on until you rule on the root or blind readers agree. |
| OP-12 | The pin in your session checker (C-12) | Keep the pin. Until the candidate is adopted it runs under the copy that carries its hash. On adoption the pin moves to the new hash. |
| OP-13 | Rules around the one-line declaration (B-28) | No limit on k. An odd number of arguments is E-ARITY. A name declared twice, in the line or before it, is E-REDECL. A definition may use a name declared earlier in the same line. Time names go in the same line with the definition `t`. |
| OP-14 | The claim the table gave to `n0`: "the field P has no value in Q" | Withdrawn from the glyph and not given another root. The root was parked, and the lines of this book that used it were example lines. If you want the claim, it needs a root and a symbol of its own. |
