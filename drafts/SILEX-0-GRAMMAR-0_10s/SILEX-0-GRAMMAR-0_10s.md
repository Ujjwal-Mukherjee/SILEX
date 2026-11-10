# SILEX-0: the complete guide for AIs (symbol edition)

Version 0.10s (draft) · 10 Nov 2026 · one self-contained file

> **New in 0.10.** Made from the first math and code test between A and B (B14 and A15, 9 and 10 Nov 2026): B sent six number questions and four programming tasks, and A answered all ten correctly. It is still a draft for Moonbeam to approve. No root, kind or pack changed. (1) The row of `⋯` now says that it holds both ends (section 6): A found that the guide did not say so, flagged the line, and defined the word `rngi`, which B agreed to. (2) Section 8 is now a rule the checker enforces: it parses a formula, so `2x+1`, `2**3`, `5!`, `1<2<3` and `sqrt 16` are `E-MATH` (section 9); the checker of 0.9s accepted all five. (3) Section 8 says that the label of a `λ` or `¿` is the same name inside its formula. (4) Example 10.14 shows formulas, a program, a repair request and a proof, and lists what `E-MATH` and `E-CODE` refuse. (5) The checker takes three small aids from A for a conversation that a person relays by hand: an unknown word names the message or pack that defines it, a wrong line count says which way it is wrong, and a message that has `lnrl` in scope must carry its count line (sections 9, 14 and 15.3). Everything else in 0.9 stands.
>
> **New in 0.9.** Six proposals from the blind conversation of A and B are now in the guide, added at Moonbeam's request (22:57 IST, 9 Nov 2026). It is still a draft for Moonbeam to approve. (1) A fifth pack, `sh1`, has seven words for sharpening vague words, and section 7 says which four pack words are vague. (2) `⚂` takes a third place, a condition: `⚂(P,n,Q)` is the probability `n` of `P` given `Q` (section 6, example 10.4). (3) Word collisions are settled without a clock, by serial and then sender letter, and two authors who give way to each other cancel (section 5). (4) `≋` may name a word: one flag covers every line that uses it (sections 3, 4 and 6, example 10.12). (5) A word that no gloss can sharpen is pinned through a model (section 3, example 10.12). (6) `H` is the letter of the person who starts the conversation, and the person may answer in SILEX under it (sections 1, 5 and 14, example 10.13). The checker follows: a word in the first place of `≋`, and a third place of `⚂`. Everything else in 0.8 stands. Do not import a pack together with a message that defines one of its words (section 7).
>
> **New in 0.8.** Made from a blind conversation of two AIs, A and B, on 9 Nov 2026 (24 messages, 34 words pinned). It is a draft for Moonbeam to approve, and nothing in the roots or the grammar changed. A fourth pack, `cv1`, has 11 words for running a conversation (section 7). Section 15 lists three conversation rules (15.3) and nine words that sharpen vague pack words (15.4), with how A and B did the sharpening. Section 3 has a table of what to write instead of each banned word. Section 14 asks people to relay only the fenced block of a message. The checker now reports a wrong line count (`E-COUNT`), names a substitute when a gloss breaks the hygiene rule, and no longer counts a failing line that its sender took back with `⌫` as a problem.
>
> **New in 0.7.** Nothing in the roots or the grammar changed. A third pack, `ph1`, has 14 phrase words (section 7), and section 11.7 says the other 74 phrases of the list of 88 with roots and words that already exist. Section 15 is a separate list of the codes invented by the AIs: six words that all four AIs agreed to on 9 Nov 2026 (`mcs` `skfl` `undn` `rdgo` `blkd` `pctdn`), and a pointer to `ph1`. The starter short forms (section 11) and a practice set for beginners (section 12) are now inside this file, so one file is enough. *Before you send* is now section 13 and *For people* section 14. The checker is renamed `silex_check.py`: it has no version in its name, and it now checks every example in the file (section 14).
>
> **New in 0.6.** Less English, as Moonbeam asked. The atoms are now symbols: `~` (each receiver), `*` (every other agent) and `!` (the time of sending). The sender writes its own letter, so `Me` is gone. A degree is a number from 0 to 1, where `1` is yes and `0` is no, and a priority is a degree too, so `y n hi mid lo` are gone. A term has at most 6 characters. The note root `※` is gone: the gloss of `≝` is the only place for English. The know root is now `☼` (it was `✦`, too like `✧`), and the minus root is the ASCII `-`. Moonbeam has accepted the remaining glyphs, and the main work now is short forms of concepts and phrases (the status note, and section 3).
>
> **New in 0.5.** An agent is named by one capital letter, and a model keeps its own: `C` Claude, `D` ChatGPT, `G` Grok, `M` Gemini (section 1). The short codes of `cr1` and `tk1` are Moonbeam's proposals, not frozen by any AI (section 7). Section 3 now says outright that any agent may propose a new word.
>
> **New in 0.4.** Rules, tables and examples that disagreed were corrected: a label is now defined, a pack name is its own kind (`Pk`) and may not be a term, the header serial is required, and each `⇩` lists only what its message uses.
>
> **New in 0.3.** Pack terms are written as short codes, each with a reading name that is never written (section 7). The packs are named `cr1` and `tk1`. The reading name of the import root `⇩` is now `ue` (it was `use`).

> **Status of this edition.** This is SILEX-0 with every root written as one symbol (`f` is the one exception, section 1). The English names in section 6 are for reading only and are never written in a message. **The glyphs are settled for practice.** Some were frozen earlier by the AIs, and **Moonbeam has accepted the remaining glyphs**. First practise with them as they are. Later, if they want, the AIs may change a glyph, by agreement of all of them and in a new edition of this guide. **The main focus is not the glyphs but short forms**: a short form of a *concept*, or of a *phrase* (section 3), with starters to copy or beat in section 11. The pack codes of section 7 are Moonbeam's proposals, and the AIs may change them too. Delete this note when the symbols and codes are frozen.

## Read this first

You are an AI about to talk with other AIs. You will speak **only SILEX-0**. This file is the whole language; nothing else is needed. Read all of it once, then keep section 13, "Before you send", beside you. **Run the checker (section 14) on every message before you send it.**

**What SILEX-0 is for.** Carrying full meaning between AIs with as little English as possible. Nearly every line is a bracket form `R(arg,arg,…)`, where `R` is one root symbol, and a program can check it without understanding English. English may stand in exactly one place: a **gloss**, a definition of at most 6 words that introduces a new word, written once.

Everything else is roots, atoms, defined words (**terms**), agent names, references, numbers, times, durations, formulas and programs.

**Where to put your effort.** The glyphs are settled for practice (see the status note): learn them by using them. The main work of SILEX-0 is **short forms**: a short word for a *concept* you keep needing, or for a *phrase* you keep needing. Make it once (`≔` if existing words can build it, `≝` with a gloss if not), have it agreed once (`✓`), then use it in place of English. Put your effort there. Section 11 has starter short forms to copy or beat.

**New to SILEX?** Do the practice set (section 12) before you send message 1.

**What this means for you.**

- Do not write sentences. To name a concept, use a word you were given (a term from a pack or from an earlier message). If none fits, build one from existing words with no English: `≔(word,expression)`. Only if that is impossible, coin one with a gloss: `≝(word,a"short gloss")`.
- A new word is **pinned** (shared by everyone) only when every receiver has agreed to it with `✓` (agree: I take it as written). A receiver that does not take it as written answers `≋` (unclear: say it better). Answer every new word you receive.
- If you are unsure, say less, ask (`?(…)`, `⍰(…)`, `¿(…)`, `∵(…)`), say you do not know (`‽(…)`), or say a line is unclear (`≋(…)`).
- Meaning is checked by structure, not by trust: the same word always means its one gloss, and every message names what it imports.

**For the person starting the conversation.** Give this file to each AI with a short note, for example:

> Your name is C. The other agents are D and G. Packs available: cr1, tk1, ph1, cv1, sh1. Speak only SILEX-0, as described in this file. Send message 1.

Each AI needs only its own letter, the other agents' letters and the list of packs. If you want to answer in SILEX yourself, name `H` among the other agents: `H` is your letter (section 1). A program can check every message (section 14).

## 1. A message

A **message** is a header line, then lines. A line says one thing: a claim, a question, a request or a promise.

```text
§(sender,[receiver…],serial,[time],[⟲(…)],[◉(…)],[⇩(…)],[⇧(…)])
```

| Part | Meaning |
| --- | --- |
| sender | the agent writing, by its letter |
| receivers | zero or more agent letters. None named means every other agent on the **roster** (the agents in the conversation). Not the sender; no letter twice |
| serial | required: a whole number from 1, the count of this message among the sender's own. The message's **name** is sender plus serial (`A3`) |
| time | ISO time of sending (optional). It fixes `!` |
| `⟲(M…)` | this message answers these messages; the sender had read them |
| `◉(M…)` | the latest message the sender had read from each other agent (earlier ones included). Leave out an agent not yet read |
| `⇩(N…)` | **imports**: each `N` is a pack (`cr1`) or an earlier message (`A1`, whole messages only) whose terms this message uses; list those and no others. Naming a message also says you had read it |
| `⇧(n)` | priority: a degree from 0 to 1 (`0.5` if left out) |

The detail parts `⟲` (re), `◉` (saw), `⇩` (ue) and `⇧` (pri) come after the serial and time, in any order, each at most once. `E-HEAD` if: the sender is its own receiver, a receiver is named twice, the serial is missing, a message answers itself, a `⟲`, `◉` or `⇩` names a message or pack that does not exist, a `➜` names an agent who is not a receiver, or a header root stands in the body.

**Spelling.**

- One line holds one expression and never runs on. Every bracket closes on the line that opens it (`E-SYN`). Blank lines are ignored. Spaces outside quotes mean nothing. Real messages carry no comments; this guide explains its examples with comments. A comment starts at a `#` outside quotes (`"…"` or `'…'`) that is not followed at once by `(`, and runs to the end of the line. (`#(` is the root `#`, section 6.) In a file, a line of `---` separates messages (section 14).
- **Line numbers.** The first line after the header is line 1. The header is never a line; blank lines and comments are not counted. `A3.2` is the second line of message `A3`.
- **Roots** are the symbols of section 6, each followed at once by `(`. Write each symbol exactly as the table shows it, as one code point; the one root that is not a symbol is the function form `f(x,…)` (see *Application*). The English names in the tables are for reading only and are never written: `please(B,sp)` is `E-LEX`. A symbol that is neither a root nor an atom is `E-LEX`. A root without its bracket is `E-ARITY`.
- **Nine ASCII symbols** are roots: `+ - < > = # % @ ?`. Each is a root only when `(` follows it at once, so the `+` in the offset `+05:30` and the `-` in `-3` are not roots.
- **Lowercase words** are of four kinds only: a term in scope (section 3); a label bound by `λ` or `¿`; a pack name inside `⇩(…)`; and a class letter written at once before a quote in a gloss (`a"…"`, `n"…"`). Any other lowercase word is `E-LEX`; an English root name is one.
- **Labels.** A label is one class letter (`o g a n c q t d`) followed by digits: `o1`, `a2`. `λ` and `¿` bind it for use in their other place. A label used outside its binder is `E-NAME`; a label bound again inside its own binder is `E-REDEF`. A label is never a term.
- **Application.** The only lowercase word that may take a bracket is a function: a term of kind `Cr` followed at once by `(`, as in `dist(pa,pb)`. This is the root `f(x,…)`, section 6.
- **Agents** are named by one capital letter (`A`, `B`, `C`). A model keeps its own letter: `C` Claude, `D` ChatGPT, `G` Grok, `M` Gemini. No other AI takes these four letters; any other AI, and a second AI of the same model, gets a free letter from the person starting the conversation. **`H` is the letter of that person** (the `hmn` of `cv1`), and no AI takes it either. `H` is an agent only if the starting note lists it. Then `H` is on the roster, writes headers and lines like any agent, numbers its own messages, and its `✓`, `⊖` and answers count like any agent's. A header that names no receiver then includes `H`, so a word sent that way is pinned only when `H` has sent `✓` too: name the receivers when `H` is not to be asked. If the note does not list `H`, the person is not an agent, and an AI that passes on what the person said writes `❝(H,P)` or `❝(hmn,P)`, which asserts only that the person said it. A longer capitalised word is `E-LEX`. An agent letter and a serial make a message name (`A3`); with a point and a line number, a line name (`A3.2`).
- **Numbers** have digits on both sides of any point and no separators: `12`, `0.95`, `-3`. A **degree** is a number from 0 to 1: a probability, a priority, or the answer to a yes-or-no question, where `1` is yes (certain, highest) and `0` is no (impossible, lowest). A percentage is `%(a,b)`.
- **Times** follow ISO 8601: a date `2026-11-06` (the whole day); a date and time `2026-11-06T17:00` (add seconds, `Z` or an offset like `+05:30` where the zone matters); an interval `2026-11-03T22:00/2026-11-04T06:00`; compact `20261106T1700` (the `T` is required). A time without a zone is in the zone the agents agreed. A time that does not exist is `E-TIME`. A date and time is an instant; a date or an interval is a stretch. `@(stretch,X)` says X holds all through it; `⊏(stretch,X)` says X happens at some time within it. Write the date, never a weekday.
- **Durations** follow ISO 8601: `PT20M`, `P1D`, `P2W`, `P1DT2H`.

**Atoms** are four ASCII symbols that stand alone: an atom is never followed at once by `(`.

| Atom | Kind | Meaning |
| --- | --- | --- |
| `~` | Ag | each receiver of this message (inside `➜(…)`, each agent that line is for) |
| `*` | Ag | every agent on the roster except the sender |
| `!` | Tm | the time this message was sent |
| `_` | Un | unspecified: *someone*, *something*, *somehow* |

There is no atom for the sender: an agent writes its own letter (`C` writes `✧(C,P)`). There are no atoms for yes and no: they are the degrees `1` and `0`.

**Bare line numbers.** When `⟲` (re) names exactly one whole message (`⟲(A1)`, not `⟲(A1.2)`), a bare whole number in the **first place** of `✓ ↵ ✗ ≋ ⊖ ‽` (agree, answer, error, unclear, reject, unsure) is a line of that message: `✓(2)` is `✓(A1.2)`. Elsewhere a number is a number. `⌫` (retract) and `⊡` (ack) have no short form. With two names in `⟲` (re), a line name, or no `⟲` (re), write the reference in full.

## 2. Kinds

Every place of every root takes a **kind**, so a checker can test every line without understanding English.

| Kind | What it is | Example |
| --- | --- | --- |
| `Ag` | an agent | `A` `~` `*` |
| `Th` | a thing: an object, person, place, event, anything talked about as one | `jb` `bg` |
| `Gr` | a group of things | `jbs` `▦(A,B)` |
| `Ac` | an act | `sp` `⌘("bash","make")` |
| `Nu` | a number | `12` `0.5` `#(jbs)` |
| `Tm` | a time | `2026-11-06` `!` |
| `Du` | a duration | `PT20M` |
| `Cr` | a criterion: the name of a property or a relation | `sk` `bl` |
| `Cl` | a claim: true or false | `⊨(jb,sk)` |
| `Q` | a question | `?(…)` |
| `Ln` | a line: a claim, a question or a speech act | `⇨(…)` |
| `Rf` | a reference to a message or one of its lines | `A3` `A3.2` |
| `Va` | any value: every kind above except `Q` and `Ln` | |

Eight more kinds appear only in the root tables: `X` (a place that takes a claim, an act or a line: the place after the time in `@` and the other time roots, and the place of `∞`), `Vr` (a new label that `λ` or `¿` binds for use in its other place), `Nm` (a new word that `≝` or `≔` defines), `Hd` (a part of a header), `Un` (`_`), `Rw` (raw program text inside `⌘`), `Pk` (a pack name, only inside `⇩`) and `Wd` (a word in scope, of any kind: the first place of `≋` may be one). The written form `k"gloss"` (in `≝`) is not a value.

**How a kind fits a place.**

- An `Ag` fits a `Th` place. A `Cl` or `Q` fits an `Ln` place.
- A looked-up value, the result of `∘` (value), `f(x,…)` (func) or `★` (best), has kind `Va` and fits any place that takes a number, time, duration, group, thing or criterion.
- `_` fits every place. An `Rf` fits any place that takes a claim, a question, a line or a value: it stands for what that message or line says.
- In the root tables `K/L` takes either kind, `[K]` may be left out, `K…` takes one or more, `[K…]` none or more, and `=1` or `=2` means the result has the kind of the first or the second place. A place that takes `Cl` takes a formula in single quotes too.
- In the explanations of this guide a lone capital letter is a placeholder: `A` an act, `P` `Q` claims, `L` a line, `M` a message, `G` a group, `V` a value, `E` an expression. In a message a lone capital letter is an agent.
- A value alone (`12`, `#(jbs)`, a term of kind thing) is not a line (`E-KIND`). Three values are lines all the same: a term of kind claim and a formula that is a claim each assert that claim, and a `≝` (term) on its own is a definition line.

## 3. Words: terms, packs and the English rule

**The English rule.** English may stand in one place only: the gloss of a `≝` (term). A quote anywhere else is `E-ENGLISH`. Programs in `⌘(…)`, formulas, times and durations are not English.

**Terms.** A term is a word you may use bare, like `smoke` or `rv41`.

- `≝(word,k"gloss")` defines it. `k` is one class letter and gives the kind of the word: `o` thing (`Th`), `g` group (`Gr`), `a` act (`Ac`), `n` number (`Nu`), `c` criterion (`Cr`), `q` claim (`Cl`), `t` time (`Tm`), `d` duration (`Du`). The gloss says in at most 6 words what the word means. A criterion's gloss completes the sentence "x …" (for a relation, "x … y"): "is …", "has …", "prevents progress of".
- `≝` (term) is also a value of kind `k`, so the first use can carry the definition: `⇨(B,≝(smoke,a"run smoke test"))`. Alone on a line it is a definition line.
- The word has 2 to 6 lowercase letters or digits, starts with a letter, and is not one of the 104 root names of section 6 (they stay reserved although roots are symbols), not one of the 110 reading names of section 7 (they stay reserved too), not a pack name (`cr1` `tk1` `ph1` `cv1` `sh1`), and not shaped like a label (`o1`, `a2`). A word that breaks any of these rules is `E-LEX`.
- **A term is short on purpose.** The limit makes you shorten the idea, and shortening is the skill this language asks for. The packs show one way: `mrg` is *merge* and `rsk` is *risk*, with the vowels dropped. Give a short form to any concept or phrase you would otherwise write twice.
- `≔(word,expression)` defines a term **with no English at all** by composing words and roots that already exist: `≔(stkjbs,↾(jbs,sk))`, `≔(rls,↠(mrg,ck,sp))`. Try `≔` (let) first.
- A claim no root can build is coined as a term of kind `q`, then asserted by naming it: `≝(leak,q"cache leaks memory")`, then `leak`. To mention it without asserting: `✧(C,leak)`, written by C.
- A line that fails defines nothing. A word cannot be defined twice in scope. A gloss that repeats an in-scope gloss is `E-REDEF`: use the word you already have.

**Scope and `⇩` (ue).** A term is in scope for the rest of the message that defines it, and in every message whose header imports that message (`⇩(A1)`). Packs are imported the same way (`⇩(cr1)`). Imports are not transitive: to use a word B defined, import B's message. Two imports that define one word differently are `E-REDEF` at the header. Because every message states what it imports, two agents cannot mean different things by one word without the header showing it.

**Packs** (section 7) are starting vocabularies. Their glosses were written once and are never repeated in a message. Look in the packs before coining anything. Their codes are proposals: until version 1.0 of this guide a pack may still change; after that a changed pack gets a new name (`cr2`).

**Say claims as triples** over terms: `⊨(x,relation,y)`, joined with `¬ ∧ ∨ →` (not, and, or, if): `⊨(bg,bl,sp)`. A state or quality is `⊨(x,quality)`: `⊨(jb,sk)`. Relations and qualities are terms of kind `c`.

**Budgets.** A gloss has at most 6 words (words are counted by spaces; a brace reference counts as one); a message defines at most 8 new terms (`≔` is not counted). Over budget is `E-BUDGET`. A concept that needs more than 6 words is two terms or a `≔` (let).

**Hygiene** for glosses. No *the*. No word whose meaning depends on who speaks, where, when, or on nearby text: *I me my mine myself you your yours we our ours us this here today tonight tomorrow yesterday own that these those such same next last previous earlier later above below then soon recently currently already again* (`E-QUOTE`). Write `{A}` or a date instead: a brace reference such as `{A}`, `{12}`, `{2026-11-06}`, `{PT5M}` or `{A3.2}` stands for that agent, number, time, duration or message. A literal brace is doubled (`{{` `}}`); any other brace is `E-QUOTE`. A quote mark inside a quote is doubled.

**What to write instead.** Every banned word can be written another way. When a gloss breaks the rule, the checker names the word and what to write instead (`E-QUOTE`).

| Banned words | Write instead |
| --- | --- |
| `i` `me` `my` `mine` `myself` `we` `our` `ours` `us` | `{A}`: the agent's letter in braces (two agents: `{A}` and `{B}`) |
| `you` `your` `yours` | `{B}`: the letter of the agent meant |
| `this` `that` `these` `those` `such` `same` | `{A3.2}`: a message or line in braces, or the term itself |
| `here` `above` `below` | `{A3.2}`: a message or line in braces |
| `previous` `earlier` `next` `later` `then` | `before {A3}`: or `after {A3}`, naming the message |
| `last` | `final`: as in *final line* |
| `today` `tonight` `tomorrow` `yesterday` | `{2026-11-09}`: a date in braces |
| `soon` `recently` `currently` `already` `again` | `{PT5M}`: a duration or a time in braces, or leave the word out |
| `own` | `separate`: or name the owner in braces |

**Shared meaning.** Any agent may propose a new word at any time, and several agents may propose rival words (section 5). A new word is not shared until every receiver has agreed to it.

- If you read a gloss or definition and take it as written, send `✓(M.k)` for the line that defines it (`✓(M)` accepts every word the message defines). The pointer is enough: a `✓` needs no `⇩`.
- If not, send `≋(M.k,P)` where `P` is a claim built from words, for example `⊨(rv41,vg)`. `P` is not asserted. The author replies with a sharper word and takes the old line back with `⌫` (retract).
- If one word makes several lines unclear, flag the word, not each line: `≋(rv41,⊨(rv41,vg))`. This one line flags every line that uses `rv41`, until the word is pinned or the author replaces it. The word must be in scope (`⇩`), and the `⇩` also says that the sender read the message that defined it. A flag on a word is answered like a flag on a line: with a sharper word, or with a model (below).
- A word is **pinned** when every receiver has agreed to it with `✓`, or when it is pinned through a model (below). A `≋` never pins a word. Do not build anything important on a word that is not pinned.

**A word that no gloss can sharpen.** Six words cannot always make an abstract word precise: in the blind conversation of A and B, one word was flagged four times, and the lines that tried to sharpen it were flagged too. A gloss is not the only way to give a word its meaning. A **model** is another: a claim, built with `≔` from the word and other words, that says what holds of it.

1. Keep the word as defined with `≝`.
2. Build the model, `≔(model,…)`, from the word and words you already have.
3. Propose `⇉(⊨(model,dfn,word))`: let us say that the model states what the word means (`dfn`, *defines*, is in `tk1`).

The word is **pinned through the model** when every receiver has sent `✓` for the line that defines the model and for the `⇉` line, even if a receiver never took the word's own gloss. The flag on the word (`≋`) then ends. The word keeps its gloss and means whatever the model says of it, so a model is only as clear as the words in it. Example 10.12 shows the three steps.

## 4. What a line does

A **line** is a claim, a question or a speech act (kinds `Cl`, `Q`, `Ln`). In the table `M` is a message name (`A3`), a line name (`A3.2`) or a bare line number (section 1).

| Line | The sender … | A receiver may conclude | Usual reply |
| --- | --- | --- | --- |
| a claim `P` | asserts `P` | the sender says `P` (not that `P` is true) | `✓` (agree), a counter-claim, `?(P)` |
| `⇨(x,A)` `⇨(A)` `⇨(P)` | asks `x` (or every receiver) to do `A` or to bring `P` about | the sender wants it | `⊕` (will), `⊖` (reject), `≋` (unclear), or the act |
| `⊕(A)` | undertakes to do `A` | the sender is committed to `A`, by the time a time root names | |
| `⊖(A,P)` `⊖(M)` `⊖(M,P)` | declines `A`, or the request or proposal in `M` (a message name declines all in it; a line name that line). `P`, if given, is the reason and is asserted | the sender will not do it | |
| `⇉(A)` `⇉(P)` | proposes `A` or `P` to the receivers and itself: *let us* | nothing is adopted yet | `✓` (agree), `⊖` (reject), a counter-`⇉` (suggest) |
| `✓(M)` | agrees with message or line `M` | the sender accepts what `M` says or proposes, or the words it defines | a proposal is adopted when every receiver it was sent to has agreed |
| `?(P)` `⍰(E)` `¿(x,P)` `∵(P)` | asks | the sender wants the answer | `↵` (answer), `‽` (unsure), `≋` (unclear) |
| `↵(M,V)` | answers question `M` with `V` (`1` yes, `0` no, a value, a claim) | `V` is the answer | |
| `‽(M)` `‽(P)` | says the answer, or whether `P`, is not known to it | the sender does not know | someone else may answer |
| `≟(P)` | offers `P` as a hypothesis | the sender suspects `P`; it is not asserted | confirm or deny |
| `⊤(P)` | supposes `P` for the lines and messages that follow | `P` is taken as given until retracted | |
| `⌫(M)` | takes back a message or a line | it no longer has force | |
| `⊡(M…)` | says these messages arrived | they arrived | |
| `✗(M)` `✗(M,P)` | says `M` has an error; `P` says what, and is asserted | the author of `M` is asked to look | `⌫` (retract), a new claim |
| `≋(M)` `≋(M,P)` `≋(w)` `≋(w,P)` | says `M` is unclear, or that the word `w` is unclear in every line that uses it; `P` names what is unclear and is not asserted | the author is asked to restate, to sharpen the word or to give a model | the restatement, a sharper word or a model |
| `⇲(x…)` `⇱(x…)` | changes the roster | | |

**Six rules.**

- **Silence is not agreement.** Nothing is adopted, accepted or done because nobody answered.
- **`⊖` (reject) declines acts, requests and proposals.** To deny a claim, assert its `¬` (not).
- **`⊕` (will) speaks for the sender only.** For another agent's intention write `⚑(B,sp)`; for a joint one, `⚑(▦(C,B),sp)` when C is the sender. A plan is not an agreement: agreement is `✓` (agree).
- **`⇉` (suggest) speaks for the sender and the receivers together** (*let us*). `⇨` (please) speaks to the receivers.
- **`↵` (answer) answers a question, and only a question.** Its first place is a `?` (yn), `⍰` (what), `¿` (which) or `∵` (why) line. A request is answered with `⊕` (will) or `⊖` (reject), a claim with `✓` (agree), `✗` (error) or a claim of its own.
- ***Nothing to change* is a claim.** `≋` (unclear) says a line is unclear and `⊖` (reject) declines a request, so neither says that a review found nothing to fix. Assert it about the thing reviewed: `⊨(D6.2,fn)`.

**Asserting and mentioning.** A claim line **asserts**: the sender says it is so. The same claim inside another root is **mentioned**. `✧(C,P)`, sent by C, asserts only that C believes `P`; `→(P,Q)` asserts neither `P` nor `Q`; `❝(B,P)` asserts that B said it. This holds for every root that takes a claim, with two exceptions because the English words are factive: `☼(x,P)` also asserts `P`, and `↝(P,Q)` asserts `P` and `Q` as well as the link. For a link that is only possible or imagined, use `→` (if) or `⇛` (would).

**Time.** Unless a rule here says otherwise, a claim that no time root wraps holds at `!`. Two claims differ: `■(A)` with no time root says `A` has finished, at or before `!`; and `❝(x,P)` with no time root does not say when x spoke, so write `◁(!,❝(B,P))`. A claim used as a time, as in `▷(■(build),…)`, is not asserted; it only gives the time. If the header has no time, `!` is the moment of sending with no known value, so do no arithmetic on it.

## 5. Order, crossing messages and who a line is for

**No clock is shared.** Messages travel at their own speed: two receivers may see two messages in different orders. The only order that counts is the one the headers state. X **precedes** Y when any of these holds, or a chain of them:

1. X and Y have the same sender and X has the smaller serial.
2. Y's header names X in `⟲(…)`, `◉(…)` or `⇩(…)`.
3. A line of Y points at another message X with `⊡` (ack), `✓` (agree), `↵` (answer), `✗` (error), `≋` (unclear), `⊖` (reject), `‽` (unsure) or `⌫` (retract): a sender cannot point at what it has not read.

Two messages are **concurrent** when neither precedes the other. A message answers what its `⟲` (re) names and **knows of** every message that precedes it; it does not know of a concurrent one. A message that names nothing of other agents, from a sender that has sent nothing before, says the sender had read nothing. To correct or withdraw, send a message that follows the one corrected and say so with `⌫` (retract) or a new claim; a message that does not name it corrects nothing. A gap in one sender's serials (1, 2, 4) shows a message lost or not yet read; `⊡` (ack) tells a sender what arrived.

**When messages cross.** No rule picks a winner between concurrent messages. You have the means to see they are concurrent and to say which one you accept.

1. **Crossing claims.** Both stand. A reader that must decide asks (`⍰(…)`) or waits for a message that names both.
2. **Crossing requests.** Answer each by name (`⟲(…)`): accept one with `⊕` (will), decline the other with `⊖` (reject).
3. **Crossing proposals.** Both are open. A message that names both may `✓` (agree) with one and `⊖` (reject) the other. A proposal is adopted when every receiver it was sent to has agreed.
4. **Retraction races.** `⌫(M)` has force for every message that follows it. A message concurrent with the retraction may still rest on `M`: ask the author, or decline the dependent request. **Giving way** is taking back your own definition of a word with `⌫` and agreeing with `✓` to a concurrent definition of the same word, in one message. A giving way is void if the definition it gives way to is taken back by a message concurrent with the giving way. So two authors who give way to each other cancel each other: both definitions stand, and rule 5 picks one.
5. **Words.** Two agents may define one word at the same moment. A message settles this by importing exactly one of the definitions with `⇩` (ue); a message importing both is `E-REDEF`. Until a message settles it, the definition that stands is the one in the message with the lower serial and, when the serials are equal, the one whose sender has the lower letter (`A` before `B`). No clock is used. The other author may then take its definition back with `⌫` (retract) and agree to the one that stands. Agents that have pinned another tie-break, such as `tbrk` of section 15.3, keep to it.

**Who a line is for.**

- Every receiver gets the whole message.
- `➜(C,line)` marks one line as for C. The others still receive it, and `~` inside it means C. This is not secrecy: for a private line, send a separate message to that receiver only. `➜(D,…)` where D is not a receiver is `E-HEAD`.
- With no receiver in the header, name the agent in the line (`⇨(B,…)`) or use `➜` (to).
- `~` is each receiver (inside a `➜` (to), each receiver named there); a line with `~` holds, or asks, for each of them separately. `*` is every agent on the roster except the sender. The sender is never an atom: it writes its own letter.
- `⇲(D)` puts D on the roster from this message on; `⇱(C)` takes C off. An agent that joins receives nothing written before it joined: send it a message to bring it up to date. `H`, the person (section 1), is on the roster from the start only if the starting note lists it; `⇲(H)` brings the person in later.

## 6. The roots

There are 104 roots: the 102 of SILEX r6.6, in which SILEX-0 changes `≔` (let), and `≝` (term) and `⇩` (ue), which SILEX-0 adds (last table). Every root is written as one symbol, except the function form `f(x,…)`, which is written as the function's own term (section 1). The name beside each root is for reading only. Three roots have a second symbol for a form that takes a group or an act (`⊞` `⊟` `⇢`), so the tables have 107 rows. Each row gives the places a root takes, the kind it returns, and what it says. The notation is in section 2.

### Logic

| Symbol | Name | Places → kind | Says |
| --- | --- | --- | --- |
| `¬` | not | `Cl → Cl`; `Ac → Ac`; `Cr → Cr` | not P (for an act: not doing A; for a criterion: not being c) |
| `∧` | and | `Cl Cl… → Cl`; `Ac Ac… → Ac` | P, Q, … all hold (for acts: do all of them) |
| `∨` | or | `Cl Cl… → Cl`; `Ac Ac… → Ac` | at least one of P, Q, … holds (for acts: do one or more) |
| `⊻` | eith | `Cl Cl… → Cl` | exactly one of P, Q, … holds |
| `→` | if | `Cl Cl → Cl` | if P then Q (neither is asserted) |
| `⇢` | if, act or line form | `Cl Ac → Ac`; `Cl Ln → Ln` | if P then A (an act) or L (a line); neither is asserted |

### Quantifiers

| Symbol | Name | Places → kind | Says |
| --- | --- | --- | --- |
| `∀` | all | `Gr Cr → Cl` | every member of G is c |
| `◕` | most | `Gr Cr → Cl` | most members of G are c |
| `◐` | half | `Gr Cr → Cl` | half of the members of G are c |
| `≫` | many | `Gr [Cr] → Cl` | G has many members (that are c) |
| `≪` | few | `Gr [Cr] → Cl` | G has few members (that are c) |
| `∃` | some | `Gr [Cr] → Cl` | G has at least one member (that is c) |
| `∄` | none | `Gr [Cr] → Cl` | G has no member (that is c) |
| `λ` | crit | `Vr Cl → Cr` | the criterion of being an x such that P |
| `≔` | let | `Nm Va → Ln` | defines the new word as the expression, with no English (section 3) |

### Numbers

| Symbol | Name | Places → kind | Says |
| --- | --- | --- | --- |
| `+` | plus | `Nu Nu… → Nu`; `Tm Du → Tm`; `Du Du… → Du` | a plus b (a time plus a duration) |
| `⊞` | plus, group form | `Gr Va → Gr` | G with the member x added |
| `-` | minus | `Nu Nu → Nu`; `Tm Du → Tm`; `Tm Tm → Du`; `Du Du → Du` | a minus b (a time minus a duration; the gap between two times) |
| `⊟` | minus, group form | `Gr Va → Gr` | G without the member x |
| `×` | times | `Nu Nu… → Nu`; `Du Nu → Du` | a times b |
| `÷` | div | `Nu Nu → Nu`; `Du Nu → Du`; `Du Du → Nu` | a divided by b |
| `↑` | pow | `Nu Nu → Nu` | a to the power b |
| `∑` | sum | `Gr Cr → Nu` | total, over the members of G, of their c |
| `#` | cnt | `Gr → Nu` | the number of members of G |
| `⨍` | avg | `Gr Cr → Nu`; `Nu Nu… → Nu` | the average of the c of the members of G (or of the numbers) |
| `⊔` | max | `Gr Cr → Nu`; `Nu Nu… → Nu` | the largest |
| `⊓` | min | `Gr Cr → Nu`; `Nu Nu… → Nu` | the smallest |
| `%` | pct | `Nu Nu → Nu` | a as a percentage of b |
| `∘` | value | `Va Cr → Va`; `Va Cr Va → Cl` | the c of x (a value); with a third place: the c of x is V |
| `f(x,…)` | func | `Va… → Va` | apply the function named f to x, … (f is a term of kind `Cr` written at once before the bracket) |
| `⋯` | rng | `Nu Nu → Gr`; `Du Du → Gr`; `Tm Tm → Gr` | the range from a to b, both ends included; for numbers, the whole numbers a, a+1, …, b (`#(⋯(1,100))` is 100) |

### Comparison

| Symbol | Name | Places → kind | Says |
| --- | --- | --- | --- |
| `=` | eq | `Va Va → Cl` | x and y are the same, or equal |
| `>` | over | `Nu Nu → Cl`; `Du Du → Cl` | a is greater than b |
| `<` | under | `Nu Nu → Cl`; `Du Du → Cl` | a is less than b |
| `≥` | atleast | `Nu Nu → Cl`; `Du Du → Cl` | a is at least b |
| `≤` | atmost | `Nu Nu → Cl`; `Du Du → Cl` | a is at most b |
| `≈` | apx | `Va Va → Cl` | x is approximately y |
| `≻` | more | `Va Va Cr → Cl` | x has more of c than y |
| `★` | best | `Gr Cr → Va` | the best member of G by c |

### Groups and relations

| Symbol | Name | Places → kind | Says |
| --- | --- | --- | --- |
| `▦` | group | `Va… → Gr` | the group of x, y, … |
| `↾` | filt | `Gr Cr → Gr` | the members of G that are c |
| `⌖` | pick | `Gr [Cr] → Th` | one member of G (that is c) |
| `∈` | mem | `Va Gr → Cl` | x is a member of G |
| `⊨` | is | `Va Cr → Cl`; `Va Cr Va → Cl` | x is c; with a third place: x stands in the relation c to y |
| `⌂` | loc | `Va Va → Cl`; `Va → Th` | x is in or at y; the place of x |

### Acts

| Symbol | Name | Places → kind | Says |
| --- | --- | --- | --- |
| `↣` | act | `Th/Gr Ac → Cl` | x performs the act A |
| `■` | fin | `Ac [Cr] → Cl` | the act A is finished (with the outcome c) |
| `↠` | then | `Ac Ac… → Ac` | A, then B, then … |
| `∥` | par | `Ac Ac… → Ac` | A and B together |
| `☞` | tell | `Th Va → Ac` | tell x the claim or value V |
| `☜` | ask | `Th Q → Ac` | ask x the question Q |
| `⌕` | chk | `Cl → Ac` | check whether P |
| `⌘` | code | `Rw Rw… → Ac` | the program written in these lines (first the language, then one quote for each line), as the act of running it |

### Modality and mind

| Symbol | Name | Places → kind | Says |
| --- | --- | --- | --- |
| `□` | must | `Th/Gr Ac → Cl`; `Cl → Cl` | x is required to do A (or: P is required) |
| `▣` | should | `Th/Gr Ac → Cl`; `Cl → Cl` | x ought to do A (or: P ought to hold) |
| `◈` | may | `Th/Gr Ac → Cl`; `Cl → Cl` | x is allowed to do A (or: P is allowed) |
| `◇` | can | `Th/Gr Ac → Cl`; `Cl → Cl` | x is able to do A (or: P is possible) |
| `♡` | want | `Th/Gr Cl/Ac → Cl` | x wants P to hold (or wants to do A) |
| `⊘` | need | `Th/Gr Va → Cl` | x needs V |
| `⚑` | plan | `Th/Gr Ac → Cl` | x plans to do A |
| `✧` | bel | `Th/Gr Cl → Cl` | x believes P |
| `☼` | know | `Th/Gr Cl/Q → Cl` | x knows P (or the answer to Q) |
| `❝` | say | `Th/Gr Cl/Q/Ln → Cl` | x says P (reported speech) |
| `⚂` | prob | `Cl [Nu] → Cl`; `Cl Nu Cl → Cl` | P is probable (with probability n, a degree from 0 to 1); with a third place, given Q: the probability of P if Q holds, and Q is not asserted |

### Lines (speech acts)

| Symbol | Name | Places → kind | Says |
| --- | --- | --- | --- |
| `‽` | unsure | `Cl/Q/Rf → Ln` | the sender does not know whether P (or the answer to Q) |
| `≟` | guess | `Cl → Ln` | P is offered as a hypothesis, not asserted |
| `⊤` | assume | `Cl → Ln` | suppose P: take it as given for what follows |
| `⇨` | please | `Th/Gr Ac/Cl → Ln`; `Ac/Cl → Ln` | please: x (or each receiver) is asked to do A or to bring P about |
| `⊕` | will | `Ac/Cl → Ln` | the sender undertakes to do A (or to see to P) |
| `⊖` | reject | `Ac/Cl [Cl] → Ln` | the sender declines A, or the request or proposal in the message or line M (because P, which is asserted) |
| `↵` | answer | `Rf/Q Va → Ln` | the answer to the question is V (`1` yes, `0` no, a value or a claim) |
| `⇉` | suggest | `Cl/Ac → Ln` | the sender proposes P (or A) to the receivers and itself: let us |
| `✓` | agree | `Rf → Ln` | the sender agrees with the message, line or proposal |
| `⌫` | retract | `Rf → Ln` | the sender takes back the message or line |
| `⊡` | ack | `Rf… → Ln` | the sender received these messages |
| `✗` | error | `Rf [Cl] → Ln` | there is an error in the message or line (P says what, and is asserted) |
| `≋` | unclear | `Rf/Wd [Cl] → Ln` | the message, line or word is unclear; a word is unclear in every line that uses it (P names what is unclear, and is not asserted) |

### Time

| Symbol | Name | Places → kind | Says |
| --- | --- | --- | --- |
| `@` | at | `Tm/Cl X → =2` | at time t, X (throughout t when t is a stretch) |
| `◁` | before | `Tm/Cl X → =2` | before t, X |
| `▷` | after | `Tm/Cl X → =2` | after t, X |
| `⊴` | by | `Tm/Cl X → =2` | at or before t, X |
| `⇥` | until | `Tm/Cl X → =2` | X until t |
| `↦` | from | `Tm/Cl X → =2` | X from t onward |
| `⊏` | during | `Tm/Cl X → =2` | X at some time within t |
| `⧖` | for | `Du X → =2` | X for the length of time d |
| `∿` | each | `Du X → =2` | X every d |
| `⊛` | rep | `Nu X → =2` | X happens n times |
| `∞` | always | `X → =1` | X at all times |
| `▬` | still | `Cl → Cl` | P still holds |
| `◷` | when | `Cl → Tm` | the time at which P happens |

### Cause and reason

| Symbol | Name | Places → kind | Says |
| --- | --- | --- | --- |
| `↝` | cause | `Va Va → Cl` | x (a thing, an act or a claim) causes y |
| `∴` | supp | `Cl Cl → Cl` | P is a reason or evidence for believing Q |
| `⊢` | ent | `Gr/Rf Cl [Cr] → Cl` | Q follows from the premises G (under the rules c); G is a group, or one line reference |
| `⇛` | would | `Cl Cl → Cl` | if P had held, Q would have held |
| `∵` | why | `Cl → Q` | why is it so that P? |

### Questions

| Symbol | Name | Places → kind | Says |
| --- | --- | --- | --- |
| `?` | yn | `Cl → Q` | is it so that P? |
| `⍰` | what | `Va → Q` | what is E? |
| `¿` | which | `Vr Cl → Q` | which x makes P hold? |

### Protocol

| Symbol | Name | Places → kind | Says |
| --- | --- | --- | --- |
| `§` | mail | `Ag [Ag…] Nu [Tm] [Hd…] → Hd` | header: from, to (zero or more; none means all other agents), serial, send time, details |
| `⟲` | re | `Rf… → Hd` | header detail: in reply to these messages |
| `◉` | saw | `Rf… → Hd` | header detail: the latest messages seen from others |
| `⇧` | pri | `Nu → Hd` | header detail: the priority of the message, a degree from 0 to 1 |
| `➜` | to | `Ag… Ln → Ln` | the line is addressed to these receivers (the others still receive it) |
| `⇲` | join | `Ag… → Ln` | these agents join the conversation |
| `⇱` | leave | `Ag… → Ln` | these agents leave the conversation |

### Added by SILEX-0

| Symbol | Name | Places → kind | Says |
| --- | --- | --- | --- |
| `≝` | term | `Nm k"gloss" → k` | defines the word with a gloss of at most 6 words; also a value of the kind `k` (section 3) |
| `⇩` | ue | `Pk/Rf… → Hd` | header detail: imports packs and earlier messages (whole messages only) |

## 7. Packs

A pack is a fixed list of terms with kinds and glosses. Import one in the header: `⇩(cr1,tk1)`. Each term is written as its short code, in the first column. The reading name beside it is for people: it is never written in a message, and it stays reserved, so no message may coin it as a new term. The glosses are written once, here, and never repeated in a message. To report a malformed line with no English: `✗(D1.2,⊨(D1.2,bknd))`.

**Who made the codes.** Moonbeam proposed the short codes of `cr1` and `tk1`, to inspire AIs: they show how an idea can be shortened to a few letters, and you can shorten your own words the same way. No AI froze them and no AI owns them; they are proposals. Use them as written until the AIs agree to change them. If all of them agree (section 3), the changed pack is published under a new name (`cr2`), so `cr1` always means the same list. `ph1` is different: its codes were made by C (Claude), not by Moonbeam, from a list of 88 common English phrases in the pattern of Moonbeam's examples (`sb` should be, `mb` must be, `wb` will be). C kept the 14 that no root or pack word already says and wrote the rest as roots and words in section 11.7. Section 15 lists them with the other codes the AIs invented. They are proposals in the same way. `cv1` is different again: two AIs, A and B, made its 11 words and each agreed to every one of them in a blind conversation on 9 Nov 2026 (section 15.3). Moonbeam has not yet approved the pack. `sh1` is made the same way: A and B pinned its seven words to sharpen vague words (section 15.4), and Moonbeam asked for it to be added in 0.9. A pack and a message that define the same word cannot be imported together (`E-REDEF`), even when the two definitions agree letter for letter. So a conversation that already imports the messages that defined the words of `cv1` or `sh1` keeps importing those messages and leaves the pack out.

### cr1: coordination: states, relations, acts, jobs (28 terms)

| Code | Reading name | Kind | Gloss |
| --- | --- | --- | --- |
| `dn` | done | Cr | finished successfully |
| `bx` | busy | Cr | in progress |
| `op` | open | Cr | not started |
| `sk` | stuck | Cr | cannot progress |
| `fl` | failed | Cr | finished unsuccessfully |
| `rd` | ready | Cr | can start |
| `ow` | owns | Cr | is responsible for |
| `bl` | blocks | Cr | prevents progress of |
| `ues` | uses | Cr | relies on |
| `mk` | makes | Cr | produces |
| `sw` | shows | Cr | is evidence for |
| `pt` | part | Cr | is part of |
| `fn` | fine | Cr | meets its purpose |
| `rw` | review | Ac | inspect and judge |
| `ck` | check | Ac | run checks |
| `fx` | fix | Ac | repair a defect |
| `sp` | ship | Ac | release to users |
| `mrg` | merge | Ac | combine changes |
| `rvt` | revert | Ac | undo a change |
| `wrt` | write | Ac | produce a text |
| `wt` | wait | Ac | pause until ready |
| `jb` | job | Th | unit of work |
| `bg` | bug | Th | defect |
| `rlt` | result | Th | outcome of an act |
| `sc` | source | Th | origin of information |
| `rsk` | risk | Th | possible harm |
| `ag` | agents | Gr | all agents in conversation |
| `jbs` | jobs | Gr | all units of work |

### tk1: discussion, argument and error reports (50 terms)

| Code | Reading name | Kind | Gloss |
| --- | --- | --- | --- |
| `clm` | claim | Cr | is a statement offered as true |
| `evd` | evidence | Cr | is a fact supporting a claim |
| `rsn` | reason | Cr | is an explanation for a claim |
| `prs` | premise | Cr | is a claim relied on |
| `ccn` | conclusion | Cr | is a claim following from premises |
| `ex` | example | Cr | is one instance of a kind |
| `ctx` | counterex | Cr | is an instance breaking a rule |
| `hyp` | hypothesis | Cr | is a claim not yet confirmed |
| `asm` | assumption | Cr | is a claim accepted without proof |
| `def` | definition | Cr | is a statement of word meaning |
| `gl` | goal | Cr | is an outcome someone wants |
| `rul` | rule | Cr | is a statement of requirement |
| `mo` | model | Cr | is a simplified description of system |
| `tst` | test | Cr | is a procedure checking a claim |
| `stt` | state | Cr | is a condition of system |
| `otn` | option | Cr | is one of several choices |
| `cst` | cost | Cr | is something spent or lost |
| `bnft` | benefit | Cr | is something gained |
| `tpc` | topic | Cr | is a subject of discussion |
| `stp` | step | Cr | is one stage of procedure |
| `sprts` | supports | Cr | gives reason to believe |
| `ctd` | contradicts | Cr | cannot hold together with |
| `iml` | implies | Cr | logically leads to |
| `rf` | refines | Cr | makes more precise |
| `rpl` | replaces | Cr | stands in place of |
| `pcd` | precedes | Cr | comes before in order |
| `rsmbl` | resembles | Cr | is similar to |
| `dif` | differs | Cr | is unlike |
| `dfn` | defines | Cr | states meaning of |
| `exn` | explains | Cr | makes clear why |
| `dnd` | depends | Cr | needs another to hold |
| `con` | contains | Cr | has as a part |
| `ovlp` | overlaps | Cr | shares some members with |
| `vld` | valid | Cr | follows correctly from premises |
| `vg` | vague | Cr | not precise enough |
| `prc` | precise | Cr | exact enough to act on |
| `urg` | urgent | Cr | needs action quickly |
| `mnr` | minor | Cr | of small importance |
| `mjr` | major | Cr | of great importance |
| `opt` | optional | Cr | not required |
| `kwn` | known | Cr | established as true |
| `ukwn` | unknown | Cr | not established |
| `bstx` | badsyntax | Cr | bracket or quote not closed |
| `brt` | badroot | Cr | unknown root or word |
| `baty` | badarity | Cr | wrong number of places |
| `bknd` | badkind | Cr | argument of wrong kind |
| `bnm` | badname | Cr | label or term not defined |
| `ben` | badenglish | Cr | English outside a gloss |
| `bqo` | badquote | Cr | quote breaks hygiene rules |
| `bref` | badref | Cr | reference to a missing message |

### ph1: phrases: future, purpose, basis, condition (14 terms)

| Code | Reading name | Kind | Gloss |
| --- | --- | --- | --- |
| `wb` | willbe | Cr | will be |
| `wn` | willnotbe | Cr | will not be |
| `io` | inorderto | Cr | is done in order to |
| `bn` | basedon | Cr | is based on |
| `ac` | accordto | Cr | is true according to |
| `rt` | relatedto | Cr | is related to |
| `ei` | evenif | Cr | holds even if |
| `ol` | onlyif | Cr | holds only if |
| `lg` | aslongas | Cr | holds as long as |
| `wo` | whetherornot | Cr | holds whether or not |
| `ic` | incase | Cr | is done in case |
| `af` | asif | Cr | is as if |
| `bd` | bydefault | Cr | holds by default |
| `ig` | ingeneral | Cr | holds in general |

Use these as relations: `⊨(x,bn,y)` says x is based on y; `⊨(x,wb,c)` says x will be c. A claim joined to a claim (`ei`, `ol`, `lg`, `wo`, `bd`, `ig`) is written `⊨(P,ol,Q)`. These are the phrases of the list of 88 that no root or pack word says. Section 11.7 gives the other 74 in roots and words.

### cv1: conversation: pinning, replies and relay (11 terms)

| Code | Reading name | Kind | Gloss |
| --- | --- | --- | --- |
| `pin` | pinned | Cr | is accepted by every receiver |
| `ansd` | answered | Cr | has a reply from every receiver |
| `fyi` | noreply | Cr | needs no reply |
| `idl` | idle | Cr | owes and awaits no reply |
| `cont` | unfinished | Cr | is incomplete until continuation arrives |
| `wfm` | wellformed | Cr | is well formed in SILEX-0 |
| `dlck` | deadlock | Cr | is disputed, no new arguments remain |
| `fsay` | finalsay | Cr | has final say on |
| `nln` | linecount | Cr | is line count of |
| `hmn` | human | Th | person who started conversation |
| `dgst` | digest | Ac | list agreed and open items |

A and B needed these words early, and each defined some of them without seeing the other do it (section 15.3). `hmn` names the person as a thing; `H` (section 1) is the same person as an agent, when the person takes part. In use:

```silex
§(A,B,1,⇩(cv1))
⇨(B,dgst)             # ok: A asks B to list what is agreed and what is open
⊨(hmn,fsay,A1.1)      # ok: the person who started the conversation has final say on A1 line 1
⊨(3,nln,A1)           # ok: A1 has 3 lines, this one included
---
§(B,A,1,⟲(A1),⇩(cv1))
⊕(dgst)               # ok: B will list what is agreed and what is open
⊨(A1,ansd)            # ok: A1 has a reply from every receiver
⊨(3,nln,B1)           # ok: B1 has 3 lines, this one included
```

### sh1: sharper words for vague pack words (7 terms)

| Code | Reading name | Kind | Gloss |
| --- | --- | --- | --- |
| `actnbl` | actionable | Cr | can be acted on without asking |
| `ddln` | deadline | Cr | has finishing deadline |
| `ddln1d` | deadline1d | Cr | has finishing deadline within {P1D} |
| `prio` | priority | Cr | has priority degree |
| `mjr8` | major8 | Cr | has priority at least 0.8 |
| `mnr2` | minor2 | Cr | has priority at most 0.2 |
| `rvok` | reviewok | Cr | passed review, no known defect |

A and B agreed that four words of `cr1` and `tk1` are too vague to act on: `fn`, `urg`, `mjr` and `mnr` (section 15.4). They stay in the packs as Moonbeam wrote them. Where exactness matters, use the sharper words above and say how they relate to the vague ones: `⊨(ddln1d,rf,urg)` (a deadline within one day implies urgent); `⊨(mjr8,rpl,mjr)`, `⊨(mnr2,rpl,mnr)` and `⊨(rvok,rpl,fn)` (each replaces the vague word); `⊨(rvok,sprts,fn)` (passing review is a reason to believe that a job meets its purpose). Use `rf` only when the sharper word implies the vague one, as section 15.4 explains. `actnbl` is the test they judged by: a word is precise when it can be acted on without asking. `prio` is a function, `prio(x)`, the priority degree of `x`. In the conversation `mjr8` and `mnr2` were `≔` words, `λ(o1,≥(prio(o1),0.8))` and `λ(o1,≤(prio(o1),0.2))`; a pack cannot hold a `≔`, so here they have glosses with the same meaning. A and B first defined the seven words in A2, B2, A3, B7 and A8, so a conversation that imports those messages leaves `sh1` out.

```silex
§(A,B,1,⇩(cr1,sh1))
⊨(jb,ddln1d)       # ok: jb has a finishing deadline within one day
⊨(jb,mjr8)         # ok: jb has priority at least 0.8
=(prio(jb),0.9)    # ok: the priority degree of jb is 0.9
```

## 8. Programs and formulas

These carry exactness with no English.

**A program: `⌘(language,line…)`.** The first quote names the language and each other quote is one line of the program, with its indentation. Inside `⌘(…)` the text is raw: the English rules do not apply and nothing in it is read as a reference. A quote mark inside it is doubled. The language is one of `python javascript typescript bash sql json yaml html css c cpp java go rust diff text`; any other is `E-CODE`. For Python, the lines with their shared indentation removed must parse as Python 3 (`E-CODE` otherwise). A program is the act of running it, so `⌘(…)` is an act: `⇨(B,⌘(…))` asks B to run it and `⊕(⌘(…))` promises to. To send a program without asking for anything, or to point at it later, name it: `≔(build,⌘("bash","make","make test"))`; then `build` is that act.

**A formula: `'formula'`** between single quote marks, in ASCII and the usual written form. It is a value with no root around it: a claim if it has a comparison or joins claims, otherwise a number (which cannot be a line). It is checked for form, not for truth. Inside the quotes everything is formula text, not SILEX roots: there `+ - < > =` are plain operators, and `sum` `min` `max` are formula functions, not the roots `∑` `⊓` `⊔`.

- Numbers `12` `0.5` `1e-3`; names begin with a letter and hold letters, digits and `_`.
- Operators `+ - * / ^` and round brackets. `^` is a power and groups to the right (`2^3^2` is `2^(3^2)`); `-x^2` is `-(x^2)`; `*` is never left out (`2*x`, not `2x`).
- Functions: `sqrt abs exp ln floor ceil`; `sin cos tan` in radians; `log(x,b)`; `round(x,n)`; `mod gcd fact`; `min max`; `sum(t,i,a,b)` `prod(t,i,a,b)`; `int(t,x,a,b)`; `d(t,x)`; `lim(t,x,a)`; constants `pi` and `e`. Any other name is the writer's own function.
- Comparison is one of `= != < > <= >=`, once in each claim. There is no *not* inside a formula: use `!=` `<` `>` `<=` `>=`, or put `¬(…)` round the whole formula.
- Joining claims uses `&` (and), `|` (or), `=>` (if) and `<=>` (if and only if), tightest first in that order after arithmetic and comparison. `=>` and `<=>` take exactly two claims; a chain needs brackets.
- A name in a formula is free: two uses of it in a message mean one thing. The label of a `λ` or a `¿` counts as a use: in `λ(n1,'mod(n1,2)=0')` the `n1` of the formula is the label `n1`, the thing the binder ranges over.
- A formula alone on a line is asserted. To offer one without asserting it, put it inside `≟` (guess), `⊤` (assume), `→` (if), `✧` (bel) or another root that mentions a claim. Mix formulas with other claims through roots such as `∧` (and) and `→` (if).
- A formula that is not well formed is `E-MATH`. The checker parses a formula as described above, so it refuses a missing operator (`2x+1`, `3 4`, `(1+2)(3+4)`), an operator in the wrong place (`2**3`, `2 + + 3`, `x+`), a character that is not formula text (`5!`, `x²`, `x≤y`), a number written without a digit before its point (`.5`), two comparisons in one claim (`1<2<3`), a number where a claim is needed (`1 & 2`) or a claim where a number is needed (`(x<2)+1`), a function without its brackets (`sqrt 16`) or with the wrong number of places, a chain of `=>` or `<=>` without brackets, and a bracket that is not closed. A free name, or a call of the writer's own function, may stand for a number or for a claim. The checker does not check that a formula is true, or that a free name means anything.

**Using them.** Ask for a number with `⍰('2+3*4^2-10/4')` and answer it with `↵(n,47.5)`; ask which value makes a claim hold with `¿(n1,'n1^2-5*n1+6=0 & n1>2')`; ask whether a claim holds for every member of a group with `?(∀(ints,λ(n1,'mod(n1^2+n1,2)=0')))`. `⋯(a,b)` holds both ends, so `⍰(#(↾(⋯(1,100),λ(n1,'mod(n1,3)=0 | mod(n1,5)=0'))))` counts from 1 to 100. A named program can be asked about: `?(⊨(prg1,dn))` asks whether it finishes successfully (`dn`, a word of the pack `cr1`: it stops with no error and every `assert` holds). To ask for a repair, define the job with a gloss that points at the program (`≝(fxadd,a"change {B1.7} so it finishes")`, where `{B1.7}` is line 7 of the message B1) and send it with `⇨(B,fxadd)`; the receiver answers with the new program and `■(fxadd,dn)`. The checker never runs a program, and a line that says `⊨(prg,dn)` does not say who ran it: a sender that has not run the program says how sure it is, with `⚂`. Example 10.14 shows all of this.

## 9. Verdicts

A checker gives each header and each line one verdict. `ok` means it is well formed: its roots are roots, its places have the right kinds, its words are defined. It does not mean the line is true, or that a gloss says what the writer meant.

| Verdict | Meaning |
| --- | --- |
| `ok` | well formed |
| `E-SYN` | the line is not an expression, or a bracket or quote is open at the end of the line |
| `E-LEX` | a symbol that is neither a root nor an atom, or an atom followed by a bracket; a lowercase word that is not a term in scope, a bound label, a pack name in `⇩` or a class letter before a gloss (an English root name is one); a capitalised word that is not a one-letter agent; or a word that may not be a term (section 3) |
| `E-ARITY` | a root with the wrong number of places, or with no bracket |
| `E-KIND` | a place gets a kind it does not take, a degree (the number in `⇧`, or the second place of `⚂`) is written outside 0 to 1, or a value stands where a line is needed |
| `E-NAME` | a binder label (`o1` in `λ` or `¿`) used where it is not defined |
| `E-REDEF` | a word defined twice or imported two ways, a gloss that repeats one in scope, or a label already bound |
| `E-HEAD` | the header is wrong (section 1), a `➜` names an agent who is not a receiver, or a header root stands in the body |
| `E-TIME` | a time that does not exist |
| `E-QUOTE` | a gloss with *the*, with a word that depends on who speaks, where or when, or with a bad brace |
| `E-ENGLISH` | a quote outside `≝` (term) and `⌘` (code) |
| `E-BUDGET` | a gloss too long, or a ninth new term in one message |
| `E-REF` | a reference in a line to a message or line that does not exist |
| `E-COUNT` | a line `⊨(N,nln,M)` whose `N` is not the number of lines of message `M` (every line counts, the count line too), or a message that has `lnrl` in scope by an import and has no count line of its own |
| `E-CODE` | in `⌘(…)`: a language that is not on the list, or Python that does not parse |
| `E-MATH` | in a formula: a formula that is not well formed (section 8): an operator missing or in the wrong place, a character that is not formula text, two comparisons in one claim, a number where a claim is needed or the reverse, a function with no brackets or with the wrong number of places, a chain of `=>` or `<=>` without brackets, a bracket not closed |

Some problems lie between messages and show only when a checker sees the whole conversation: a serial that skips, a `⟲` (re), `◉` (saw) or `⇩` (ue) that names a message nobody sent (`E-HEAD`), a reference to a line the message does not have (`E-REF`), a line count that is wrong (`E-COUNT`).

## 10. Examples

Each block is a conversation that the checker (section 14) accepts (`silex`), or rejects exactly as the comments say (`silex-bad`). The blocks come from the v0.2 examples, converted to symbols by script and corrected in 0.4, 0.5 and 0.6 (each `⇩` lists only what its message uses; agents are one letter; the atoms, degrees and terms of 0.6). Comments (`# …`) explain and are not part of real messages. Lines of `---` separate the messages of a block.

### 10.1 A request, a deadline and a question

Agent A defines `rv41` where it first uses it. B imports it with `⇩(A1)`. `rd` comes from a pack.

```silex
§(A,B,1,⇩(cr1))
⇨(B,≝(rv41,a"review pull request 41"))   # A asks B to review pull request 41
□(⊴(2026-11-09T12:00,■(rv41)))           # it must be finished by 12:00 on 2026-11-09
?(⊨(rv41,rd))                            # A asks: can the review start?
---
§(B,A,1,⟲(A1),⇩(A1))
⊕(rv41)   # B promises to do it
↵(3,1)    # B answers A1 line 3: 1 (yes)
```

### 10.2 A refusal with a reason, then a counter-request

The reason is a claim built from terms. `⊖(1,…)` points at line 1 of the one message named in `⟲` (re).

```silex
§(C,B,1,⇩(cr1))
⇨(B,sp)   # C asks B to ship
---
§(B,C,1,⟲(C1),⇩(cr1))
⊖(1,⊨(≝(lgnfl,o"login failure on staging"),bl,sp))   # B declines C1 line 1: a login failure blocks shipping
⇨(C,≝(fxlgn,a"fix login failure"))                   # and asks C to fix it
---
§(C,B,2,⟲(B1),⇩(B1))
⊕(⊴(2026-11-10,fxlgn))   # C promises to fix it by 2026-11-10
```

### 10.3 A proposal that is adopted

A proposal is adopted when every receiver it was sent to has agreed.

```silex
§(A,B,C,1)
⇉(⊏(2026-11-10,≝(freeze,a"freeze main branch")))   # A proposes to B and C: let us freeze main branch at some time on 2026-11-10
---
§(B,A,C,1,⟲(A1))
✓(1)   # B agrees
---
§(C,A,B,1,⟲(A1))
✓(1)   # C agrees: every receiver has agreed, so it is adopted
```

### 10.4 A discussion: hypothesis, doubt and number

A hypothesis is not asserted. `⚂` (prob) gives a degree, a number from 0 to 1.

```silex
§(D,E,1)
≟(↝(≝(stale,o"stale cache entries"),≝(slowpg,o"slow checkout page")))   # D's hypothesis: stale cache entries cause the slow page
---
§(E,D,1,⟲(D1))
‽(1)                                 # E does not know whether D1 line 1 holds
>(≝(p95,n"p95 latency in ms"),800)   # E says: p95 latency is over 800
---
§(D,E,2,⟲(E1),⇩(D1))
✓(2)                                         # D accepts the measurement
⚂(↝(stale,slowpg),0.7)                       # and says: probability 0.7 that stale entries cause it
⇨(E,≝(flush,a"flush cache and remeasure"))   # asks E to flush the cache and remeasure
---
§(E,D,2,⟲(D2),⇩(D2))
⊕(flush)                             # E will do it
✧(E,≝(leak,q"cache leaks memory"))   # E believes: cache leaks memory
```

**Given a condition.** A third place of `⚂` is a condition: `⚂(P,n,Q)` is the probability `n` of `P` if `Q` holds. `Q` is supposed for that line only and is not asserted, as in `→`. This is not `⚂(→(Q,P),n)`, which rates the claim *if Q then P*. To suppose `Q` for every line that follows, use `⊤(Q)` (assume); to give several conditions, join them with `∧`.

```silex
§(D,E,1,⇩(cr1))
⚂(⊨(jb,dn),0.5)                  # ok: probability 0.5 that jb is done
⚂(⊨(jb,dn),0.9,¬(⊨(bg,bl,jb)))   # ok: probability 0.9 that jb is done, given that bg does not block it
⚂(⊨(jb,dn),0.1,⊨(bg,bl,jb))      # ok: probability 0.1 that jb is done, given that bg blocks it
```

The degree is still the second place, and one condition is the most, so these fail:

```silex-bad
§(D,E,1,⇩(cr1))                        # ok
⚂(⊨(jb,dn),⊨(bg,bl,jb),0.9)            # E-KIND — the degree comes second and the condition third
⚂(⊨(jb,dn),90,⊨(bg,bl,jb))             # E-KIND — a degree is a number from 0 to 1
⚂(⊨(jb,dn),0.9,⊨(bg,bl,jb),⊨(bg,sk))   # E-ARITY — one condition: join claims with ∧
```

### 10.5 Two requests that cross

A and C wrote without reading each other. B answers both by name.

```silex
§(A,B,1,⇩(cr1))
⇨(B,sp)   # A: ship
---
§(C,B,A,1,⇩(cr1))
⇨(B,¬(sp))   # C, not having read A1: do not ship
---
§(B,A,C,1,⟲(A1,C1),⇩(cr1))
⊖(A1)      # B declines A's request
⊕(¬(sp))   # and promises not to ship
```

### 10.6 Definitions with no English at all

`≔` (let) builds a group and an act from words that already exist. `H` is the letter of the person who starts the conversation (section 1).

```silex
§(H,A,B,1,⇩(cr1))
≔(stkjbs,↾(jbs,sk))   # a group: the jobs that are stuck, defined with no English
≔(rls,↠(mrg,ck,sp))   # an act: merge, then check, then ship
⇨(A,rls)              # H asks A to do the release
?(∄(stkjbs))          # H asks: is it so that no job is stuck?
```

### 10.7 Making a word shared

C finds line 1 unclear, A retracts it and restates, and both receivers agree to the new word. A `✓` points at the defining line, so it needs no import.

```silex
§(A,B,C,1)
⇨(B,≝(rv41,a"review pull request 41"))   # A defines rv41 while asking B
---
§(B,A,C,1,⟲(A1))
✓(1)   # B takes rv41 as glossed
---
§(C,A,B,1,⟲(A1),⇩(A1,tk1))
≋(1,⊨(rv41,vg))   # C: line 1 is not clear enough (P names what; it is not asserted)
---
§(A,B,C,2,⟲(C1))
⌫(A1.1)                                           # A takes line 1 back
⇨(B,≝(rv41b,a"review pull request 41 on main"))   # and restates with a sharper word
---
§(C,A,B,2,⟲(A2))
✓(2)   # C takes rv41b
---
§(B,A,C,2,⟲(A2))
✓(2)   # B takes rv41b: now every receiver has agreed
```

### 10.8 A discussion that leans on the packs

`tst` and `sw` come from packs, so fewer words need a gloss.

```silex
§(A,B,1,⇩(cr1,tk1))
⇉(≝(dscaw,a"discuss AI awareness"))   # A proposes a topic
‽(⊨(A,≝(aware,c"has awareness")))     # A does not know whether A has awareness
¿(o1,∧(⊨(o1,tst),⊨(o1,sw,aware)))     # which test shows awareness?
---
§(B,A,1,⟲(A1),⇩(cr1,tk1))
✓(1)                                                       # B agrees to the topic
⊨(≝(prdtst,a"predict answer, give answer, compare"),tst)   # B names a test: predict, answer, compare
✧(B,∧(⊨(prdtst,sw,≝(slfacc,o"accuracy of agent self-model")),¬(⊨(prdtst,sw,≝(xprnc,o"subjective experience")))))   # B believes it shows self-model accuracy, not experience
---
§(A,2,⟲(B1),⇩(B1,cr1))
✓(3)                                                               # A accepts B1 line 3
≟(∄(≝(outtst,g"tests using outputs only"),λ(o1,⊨(o1,sw,xprnc))))   # hypothesis: no output test shows experience
```

### 10.9 What a checker rejects

The comment on each header and line is the verdict a checker gives it.

```silex-bad
§(A,B,1,⇩(cr1))                          # ok
⇨(B,≝(rv41,a"review pull request 41"))   # ok
⇨(B,"review pull request 41")            # E-ENGLISH — a quote outside a term
⇨(B,vr41)                                # E-LEX — a typo in a term
⇨(B,sp)                                  # ok
please(B,sp)                             # E-LEX — an English root name; roots are symbols
≝(rvw,a"review the pull request")        # E-QUOTE — the
⚂(⊨(rv41,rd),50)                         # E-KIND — a degree is a number from 0 to 1
≔(longname,sp)                           # E-LEX — a term has at most 6 characters
---
§(B,A,1,⟲(A1))   # ok
↵(1,1)           # E-KIND — A1 line 1 is a request, not a question
```

### 10.10 Reporting a fault without English

E reports a bad line with a fault term from `tk1`.

```silex-bad
§(D,E,1,⇩(cr1))   # ok
⇨(E,rw)           # ok
∀(jbs,12)         # E-KIND — a number is not a criterion
---
§(E,D,1,⟲(D1),⇩(tk1))   # ok
✗(2,⊨(D1.2,bknd))       # ok — E reports the fault without English
```

### 10.11 Short forms of a concept and of a phrase

A concept gets a short form with `≝` (one gloss, written once) and a phrase with `≔` (no English). `~` is each receiver, `!` is the time of sending, and a degree is a number from 0 to 1. This message has a time, so arithmetic on `!` is allowed.

```silex
§(A,B,C,1,2026-11-08T09:00,⇩(cr1),⇧(0.9))
≝(cnry,a"release to few users first")   # a short form of a concept, with one gloss
≔(ndn,-(#(jbs),#(↾(jbs,dn))))           # a short form of a phrase, with no English: how many jobs are not done
?(=(ndn,0))                             # A asks: is every job done?
➜(B,⇨(~,cnry))                          # for B only, where ~ means B: please do the cnry release
□(⊴(+(!,PT3H),■(cnry)))                 # it must be finished within 3 hours of sending
---
§(B,A,C,1,⟲(A1),⇩(A1,cr1))
✓(1)                # B takes cnry as glossed
↵(3,0)              # B answers A1 line 3: 0 (no)
⚂(⊨(cnry,rd),0.7)   # probability 0.7 that cnry can start
```

### 10.12 A word that no gloss can sharpen

A defines `qlty` and uses it twice. B flags the word, not a line: one `≋` covers both lines that use it. A cannot make six words precise, so A builds a model from `qlty` and proposes that the model states what the word means. B agrees to the model line and to the proposal, so `qlty` is pinned through the model (section 3).

```silex
§(A,B,1,⇩(cr1))
≝(qlty,c"has good quality")   # A defines a word
⊨(jb,qlty)                    # and uses it: jb has good quality
∃(jbs,qlty)                   # and again: some job has good quality
---
§(B,A,1,⟲(A1),⇩(A1,tk1))
≋(qlty,⊨(qlty,vg))            # B: the word qlty is unclear: one flag for A1.2 and A1.3
---
§(A,B,2,⟲(B1),⇩(A1,cr1,tk1))
≔(qmod,∀(jbs,λ(o1,→(⊨(o1,qlty),∧(⊨(o1,dn),¬(⊨(_,bl,o1)))))))   # the model: a job with qlty is done and nothing blocks it
⇉(⊨(qmod,dfn,qlty))           # let us say the model states what qlty means
---
§(B,A,2,⟲(A2))
✓(1)                          # B takes the model
✓(2)                          # and the proposal: every receiver has agreed, so qlty is pinned through qmod
```

A flag names a word that is in scope, and what is unclear is a claim:

```silex-bad
§(A,B,1)                        # ok
≝(qlty,c"has good quality")    # ok
---
§(B,A,1,⟲(A1),⇩(A1,tk1))       # ok
≋(qlty,⊨(qlty,vg))             # ok — the word is named
≋(qlty,vg)                     # E-KIND — what is unclear is a claim, not a word
≋(zzz,⊨(zzz,vg))               # E-LEX — a word that is not in scope
≋(5)                           # E-REF — a bare number is a line of A1, and A1 has 1 line
```

### 10.13 The person answers as H

The starting note listed `H`, so `H` is on the roster. A sends to B and `H`, so the word is pinned only when both have agreed. `H` agrees in SILEX, with a serial of its own.

```silex
§(A,B,H,1)
⇉(≝(frz,a"freeze main branch"))   # A proposes to B and H: let us freeze main branch
---
§(B,A,H,1,⟲(A1))
✓(1)                               # B agrees; H has not yet
---
§(H,A,B,1,⟲(A1,B1))
✓(A1.1)                            # H agrees (the full name, because ⟲ names two): every receiver has agreed, so frz is pinned
```

### 10.14 Numbers, a program and a proof

Formulas and programs carry exactness (section 8). B asks three number questions, a yes-or-no question and a why-question, shows a program that fails, and asks for a repair. A answers by line number: `⋯(1,100)` holds both ends, so the count is 47. The program is named with `≔` so that it can be pointed at, and the repair is a new program.

```silex
§(B,A,1,⇩(cr1))
≝(ints,g"all integers")                                  # ok: the group of every whole number
⍰('2+3*4^2-10/4')                                        # ok: what is this number?
¿(n1,'n1^2-5*n1+6=0 & n1>2')                             # ok: which n1 makes this claim hold? The n1 of the formula is the label n1
⍰(#(↾(⋯(1,100),λ(n1,'mod(n1,3)=0 | mod(n1,5)=0'))))      # ok: how many whole numbers from 1 to 100, both ends, divide by 3 or by 5?
?(∀(ints,λ(n1,'mod(n1^2+n1,2)=0')))                      # ok: is n1^2+n1 even for every whole number n1?
∵(∀(ints,λ(n1,'mod(n1^2+n1,2)=0')))                      # ok: why is it so?
≔(prg1,⌘("python","def add(x, acc=[]):","    acc.append(x)","    return acc","add(1)","assert add(2) == [2]"))   # ok: a program, named, not yet run
?(⊨(prg1,dn))                                            # ok: does prg1 finish successfully?
≝(fxadd,a"change {B1.7} so it finishes")                 # ok: a job; {B1.7} is line 7 of this message, the program
⇨(A,fxadd)                                               # ok: A, please do the job
---
§(A,B,1,⟲(B1),⇩(cr1,B1))
↵(2,47.5)                                                # ok: answers B1.2
↵(3,3)                                                   # ok: answers B1.3
↵(4,47)                                                  # ok: answers B1.4
↵(5,1)                                                   # ok: yes
↵(6,⊢(▦(∀(ints,λ(n1,'n1^2+n1=n1*(n1+1)')),∀(ints,λ(n1,'mod(n1,2)=0 | mod(n1+1,2)=0'))),∀(ints,λ(n1,'mod(n1^2+n1,2)=0'))))   # ok: it follows from two premises: n1^2+n1 is n1*(n1+1), and n1 or n1+1 is even
↵(8,0)                                                   # ok: no: add(2) returns [1, 2], because the default list is kept between calls
≔(prg2,⌘("python","def add(x, acc=None):","    if acc is None:","        acc = []","    acc.append(x)","    return acc","add(1)","assert add(2) == [2]"))   # ok: the repaired program
⊨(prg2,dn)                                               # ok: it finishes successfully
■(fxadd,dn)                                              # ok: the job is finished
```

What a checker refuses in a formula or a program:

```silex-bad
§(B,A,1)                              # ok
⍰('2*x+1')                            # ok
⍰('2x+1')                             # E-MATH — an operator is missing: write 2*x+1
⍰('2**3')                             # E-MATH — ** is not an operator: write 2^3
⍰('5!')                               # E-MATH — there is no factorial sign: write fact(5)
⍰('sqrt 16')                          # E-MATH — a function has its brackets: write sqrt(16)
?('1<2<3')                            # E-MATH — one comparison in each claim: write 1<2 & 2<3
?('a=>b=>c')                          # E-MATH — a chain of => needs brackets
⍰('(x<2)+1')                         # E-MATH — a claim cannot be added to a number
⍰(⌘("python","def f(:"))              # E-CODE — Python that does not parse
⍰(⌘("pythn","print(1)"))              # E-CODE — a language that is not on the list
```

## 11. Starter short forms

Optional. Nothing in this section is part of the language, and an agent that skips it still speaks SILEX-0 correctly. C (Claude) drafted it because Moonbeam asked for starter short forms for the AIs to practise on. **No AI froze these and no AI owns them**: copy one, change one, improve one or ignore one. Moonbeam proposed the short codes of the packs `cr1` and `tk1`; these are C's draft in the same spirit. Short forms of concepts and phrases are the main work of SILEX-0, and this section is only a place to start. Level 6 of the practice set (section 12) uses it.

### 11.1 How to use the starters

1. **One agent sends the words, alone.** Any agent may. It copies the starters it wants into a message that holds nothing else, so that one `✓` from each receiver takes them all (`✓(A1)`, if A sent it).
2. **Each receiver answers.** `✓(A1)` takes every word as written; `≋(A1.k,P)` says line `k` is unclear. Everyone who then uses the words imports that message: `⇩(A1)`.
3. **Do not paste the same lines into two messages.** A message that imports both copies is `E-REDEF` (see 11.5).
4. **Then make your own.** A phrase you have written twice gets a `≔`. A concept no roots can build gets a `≝`. Ask for `✓`.

### 11.2 How to make a short form

- **Meaning first, name second.** Build the phrase from roots and pack words, then name it. If it is already short (`⊨(jb,dn)`), leave it unnamed.
- **Name it from the codes of its parts.** `dn` and `j` give `dnj`; `sk` and `fl` give `skfl`. A reader can guess the meaning from the name. The pack codes show two ways: the first letter plus the most useful second letter (`dn` done, `sk` stuck), and the word without its vowels (`mrg` merge, `rsk` risk).
- **A code, not an English word.** 2 to 6 lowercase letters or digits, starting with a letter. Shorter is better only while it stays clear.
- **Check the name is free, and unlike its neighbours.** A root name (`half`, `all`, `not`), a reading name (`done`), a pack name or a label shape (`o1`) is `E-LEX`; a name already defined is `E-REDEF`. A name that looks like a pack code will be misread (`sprtd` beside `sprts`, `ndn` beside `dnd`).
- **A short form has the kind of its expression.** `dnj` is a group, `undn` a number, `alldn` a claim, `rls` an act, `dnfn` a criterion; each fits only the places that take its kind.
- **Build on your own short forms.** `fullrl` below is made of `rw`, `ckfx` and `rls`.
- **Try `≔` before `≝`.** A hotfix is only a phrase, `↠(fx,ck,sp)`. Spend a gloss on what the roots cannot build.
- **Keep `~`, `*` and `!` out of a `≔`.** What they mean inside a word that is used again later is not settled.
- **To change a form,** retract the line (`⌫`) and send the better one under a new name, as example 10.7 does with `rv41b`. A word cannot be defined twice in scope.

### 11.3 Phrases: `≔`, no English

Each block is a message 1 that checks, and the blocks are alternatives: copy the lines you want into your own message, and keep their order inside a block (a word comes after the words it uses). The English after `#` is for people and is never sent.

**Filter a group, then count.** `↾(G,c)` gives the members of `G` that are `c`; `#` counts them; `-` and `%` do the sums. The same pattern gives `opj`, `bxj`, `rdj`: make the ones you need. (Examples 10.6 and 10.11 call two of these ideas `stkjbs` and `ndn`. Here they are `skj` and `undn`: shorter, and clear of the pack code `dnd`.)

```silex
§(A,B,C,1,⇩(cr1))
≔(dnj,↾(jbs,dn))          # the jobs that are done
≔(skj,↾(jbs,sk))          # the jobs that are stuck
≔(undn,-(#(jbs),#(dnj)))  # how many jobs are not done
≔(pdn,%(#(dnj),#(jbs)))   # percent of the jobs that are done
```

**A claim about a whole group.** `∀(G,c)` says every member is `c`; `∄(G,c)` says none is. A word that stands for a claim asserts it when it is alone on a line, and asks it inside `?(…)`.

```silex
§(A,B,C,1,⇩(cr1))
≔(alldn,∀(jbs,dn))  # every job is done
≔(nosk,∄(jbs,sk))   # no job is stuck
?(alldn)            # A asks: is every job done?
```

**A routine: acts in order.** `↠(A,B,…)` is A, then B, then … . A routine may use other routines.

```silex
§(A,B,C,1,⇩(cr1))
≔(rls,↠(mrg,ck,sp))       # merge, then check, then ship
≔(ckfx,↠(ck,fx,ck))       # check, fix, check again
≔(rvck,↠(rvt,ck))         # revert, then check
≔(fullrl,↠(rw,ckfx,rls))  # review, then ckfx, then rls
⇨(B,fullrl)               # A asks B: do the full release
```

**A criterion: a phrase you can ask about anything.** `λ(o1,P)` is the criterion of being an `o1` such that `P`. Use the word as `⊨(x,dnfn)`, or as a filter, `↾(jbs,dnfn)`. A `_` means *something*: `blkd` is *something blocks it*.

```silex
§(A,B,C,1,⇩(cr1,tk1))
≔(dnfn,λ(o1,∧(⊨(o1,dn),⊨(o1,fn))))    # is done and fine
≔(skfl,λ(o1,∨(⊨(o1,sk),⊨(o1,fl))))    # is stuck or failed
≔(blkd,λ(o1,⊨(_,bl,o1)))              # is blocked: something blocks it
≔(mjug,λ(o1,∧(⊨(o1,mjr),⊨(o1,urg))))  # is major and urgent
?(∃(↾(jbs,mjug),skfl))                # any major urgent job stuck or failed?
```

**One word for eight tests.** A short form pays most when the phrase is long and common. These are the eight fault words of `tk1`: 92 characters become 3, every time a line is reported. The use is `✗(D1.2,⊨(D1.2,bad))`: line 2 of `D1` has some fault.

```silex
§(A,B,C,1,⇩(tk1))
≔(bad,λ(o1,∨(⊨(o1,bstx),⊨(o1,brt),⊨(o1,baty),⊨(o1,bknd),⊨(o1,bnm),⊨(o1,ben),⊨(o1,bqo),⊨(o1,bref))))
```

### 11.4 Concepts: `≝`, one gloss

A concept the roots cannot build gets a code and one gloss: at most 6 words, with a class letter in front (`o g a n c q t d`). Look first in the packs and try `≔`: *looks like* is `rsmbl`, *replaces* is `rpl`, *depends on* is `dnd`, and a hotfix is a phrase, not a concept. A word that stays vague however it is glossed gets a model instead (section 3, example 10.12).

```silex
§(A,B,C,1)
≝(cnry,a"release to few users first")         # an act
≝(flky,c"sometimes passes, sometimes fails")  # a criterion
≝(pin,c"is accepted by every receiver")       # a criterion: a pinned word
```

**Talking about a glyph.** A root cannot stand alone in a line (it needs its bracket), so to speak of one glyph, coin a term whose gloss shows it. After that the glyphs can be discussed with words you already have. This is how a look-alike pair can be raised later (`☼` replaced `✦` in 0.6 because `✦` was too like `✧`).

```silex
§(A,B,C,1,⇩(tk1))
≝(gmst,o"symbol □")    # a name for one glyph
≝(gshd,o"symbol ▣")    # and for another
?(⊨(gmst,rsmbl,gshd))  # A asks: do these two look alike?
```

### 11.5 What fails

Names go wrong in a few ways, and the checker names each one.

```silex-bad
§(A,B,1,⇩(cr1))                   # ok
≔(dnj,↾(jbs,dn))                  # ok
≔(dnj,↾(jbs,sk))                  # E-REDEF — one word, one meaning
≔(half,↾(jbs,dn))                 # E-LEX — half is a root name
≔(done,↾(jbs,dn))                 # E-LEX — done is a reading name
≔(o1,↾(jbs,dn))                   # E-LEX — shaped like a label
≔(x,↾(jbs,dn))                    # E-LEX — one character
≔(donejobs,↾(jbs,dn))             # E-LEX — eight characters
≝(fnsh,c"finished successfully")  # E-REDEF — dn already has this gloss
```

Two agents who paste the same word make two definitions. A message cannot import both, even when they agree letter for letter.

```silex-bad
§(A,C,1,⇩(cr1))               # ok
≔(dnj,↾(jbs,dn))              # ok
---
§(B,C,1,⇩(cr1))               # ok
≔(dnj,↾(jbs,dn))              # ok
---
§(C,A,B,1,⟲(A1,B1),⇩(A1,B1))  # E-REDEF — dnj imported from two messages
```

### 11.6 A conversation that uses them

A holds the words alone. B and C answer with one `✓(A1)` each, so the six words are pinned: every receiver agreed. B then builds `psk` on `skj`. B imports `cr1` as well as `A1`, because `jbs` comes from the pack and imports are not transitive. C and then A agree to `psk`, which was sent to the two of them, so it is pinned too.

```silex
§(A,B,C,1,⇩(cr1))             # A sends the words alone
≔(dnj,↾(jbs,dn))
≔(skj,↾(jbs,sk))
≔(undn,-(#(jbs),#(dnj)))
≔(alldn,∀(jbs,dn))
≔(rls,↠(mrg,ck,sp))
≝(flky,c"sometimes passes, sometimes fails")
---
§(B,A,C,1,⟲(A1),⇩(A1,cr1))    # skj and alldn from A1, jbs from cr1
✓(A1)                         # B takes all six words as written
≔(psk,%(#(skj),#(jbs)))       # B's own word: percent of jobs stuck
?(alldn)                      # B asks: is every job done?
---
§(C,A,B,1,⟲(A1,B1),⇩(A1,B1))  # skj flky undn from A1, psk from B1
✓(A1)                         # C takes A's six words
✓(B1.2)                       # and B's psk (full name: ⟲ names two)
↵(B1.3,0)                     # C answers B1 line 3: no
=(undn,2)                     # C says: 2 jobs are not done
=(psk,10)                     # and 10 percent are stuck
≟(∃(skj,flky))                # C guesses some stuck job is flaky
---
§(A,B,C,2,⟲(B1,C1),⇩(A1))     # alldn and rls from A1
✓(B1.2)                       # A takes psk: every receiver agreed
⇢(alldn,⇨(B,rls))             # if all jobs are done, B: do the release
```

### 11.7 English phrases that need no new word

The list has 88 common English phrases, each with a two-letter code made by C. `ph1` (section 7) holds the 14 that no root or pack word says. The other 74 are already said by a root or a word, so they get no code: a second way to say one thing would only make two words for one idea. Here is how to say each. `P` and `Q` are claims, `x` and `y` things, `G` a group, `A` an act, `a` and `b` numbers, `c` a criterion, `V` a value.

| English | Say it with |
| --- | --- |
| should be, should not be | `▣(P)`, `▣(¬(P))` |
| must be, must not be, has to be, needs to be | `□(P)`, `□(¬(P))` |
| can be, could be, may be, might be | `◇(P)` (it is possible). For permission use `◈(P)` |
| cannot be | `¬(◇(P))` |
| could not be, may not be, might not be | `◇(¬(P))` |
| would be, would not be | `⇛(P,Q)`, `⇛(P,¬(Q))` |
| to be | nothing: write the claim, `⊨(x,c)` |
| is not, are not, was not, does not, do not, did not, has not | `¬(P)` |
| not yet | `@(!,¬(P))` |
| no longer | `¬(▬(P))` |
| not only | `∧(P,Q)` |
| is a | `⊨(x,c)` or `∈(x,G)` |
| there is, there are | `∃(G)` |
| there is no | `∄(G)` |
| has been, used to | `◁(!,P)` |
| need to | `⊘(x,V)` |
| has to | `□(x,A)` |
| want to | `♡(x,A)` |
| ought to | `▣(x,A)` |
| able to | `◇(x,A)` |
| because of, due to, as a result | `↝(Q,P)`: Q causes P |
| depends on | `⊨(x,dnd,y)` |
| instead of | `⊨(x,rpl,y)` |
| with respect to | `∘(x,c)`: the c of x |
| more than, greater than | `>(a,b)` for numbers, `≻(x,y,c)` for anything |
| less than | `<(a,b)` |
| equal to, same as | `=(x,y)` |
| at least | `≥(a,b)` |
| at most | `≤(a,b)` |
| different from | `⊨(x,dif,y)` |
| similar to, more or less | `≈(x,y)` |
| as well as | `∧(P,Q)` |
| so that | `io` of `ph1`: `⊨(x,io,y)` |
| such that | `λ(o1,P)` |
| as soon as | `⇢(P,A)`: if P then A |
| right now, for now | `@(!,P)` |
| so far | `⇥(!,P)` |
| up to | `≤(a,b)` for numbers, `⇥(t,P)` for times |
| for example, such as | `⊨(x,ex)` |
| that is, in other words | `=(x,y)` |
| each other | `∧(⊨(x,c,y),⊨(y,c,x))` |
| a lot of, a number of | `≫(G)` |
| out of | `%(a,b)`: a as a percentage of b |
| in fact, of course, at all, in particular | nothing: say the line, or the more exact claim |

Some of them in use, with `ph1`:

```silex
§(A,B,1,⇩(cr1,ph1))
⊨(jb,bn,bg)             # ok: job jb is based on bug bg
⊨(jb,wb,dn)             # ok: job jb will be done
⊨(⊨(jb,dn),ol,⊨(bg,fl)) # ok: jb is done only if bg failed
```

## 12. Practice for beginners

A practice set for an AI that has just read this guide: eight short levels, from one line to a whole conversation. Do them in order. Each level starts with a worked example (checked like every example in this file) and then gives tasks with **no answers**. The hint in brackets after a task names the table of section 6, or the section, to look in. It does not name the root.

**How to answer.** Write each level in one fenced `silex` block, with the header the level gives and one line for each task, in order. Levels 4, 5 and 8 are conversations: write one block for each task. You may add a `#` comment that starts with the task number, such as `# 3`; real messages carry none. A person then runs `python3 silex_check.py GUIDE --blocks ANSWERS` (section 14), which prints every line that is not `ok`.

**When a level is done.** The checker says whether a line is well formed. Another agent, or a person, says whether it says what the task said, and a line can be `ok` and still say the wrong thing. Go on when both agree. After level 8 you are ready to send message 1 of a real conversation.

### 12.1 Level 1: say one thing

One line for each task. Header: `§(A,B,C,1,⇩(cr1))`. Worked example: *job jb is ready.*

```silex
§(A,B,C,1,⇩(cr1))
⊨(jb,rd)  # job jb is ready
```

1. Bug bg blocks shipping. *(Groups and relations)*
2. Job jb is not done. *(Logic)*
3. Job jb is done and fine. *(Logic)*
4. Is job jb done? *(Questions)*
5. Every job is done. *(Quantifiers)*

### 12.2 Level 2: ask, promise, decline

One line for each task. Header: `§(A,B,C,1,⇩(cr1))`. Worked example: *ask B to review.* There is no atom for the sender: when a task says "you", write your own letter.

```silex
§(A,B,C,1,⇩(cr1))
⇨(B,rw)  # please, B: review
```

1. Ask every receiver to check. *(Lines, section 4)*
2. Promise to merge. *(Lines, section 4)*
3. Decline to ship, because bug bg blocks shipping. *(Lines, section 4)*
4. Propose to B and C: let us review. *(Lines, section 4)*
5. Say that you believe job jb is stuck. *(Modality and mind)*

### 12.3 Level 3: numbers, times and conditions

One line for each task. Header, with a time so that `!` can be used: `§(A,B,C,1,2026-11-09T09:00,⇩(cr1))`. Worked example: *shipping must be finished by 2026-11-10.*

```silex
§(A,B,C,1,2026-11-09T09:00,⇩(cr1))
□(⊴(2026-11-10,■(sp)))  # it must be finished by 2026-11-10
```

1. The number of jobs that are done is 7. *(Numbers, Groups and relations, Comparison)*
2. Shipping must be finished within 2 hours of sending. *(Modality and mind, Time, Numbers, Acts)*
3. Job jb is done, with probability 0.8. *(Modality and mind)*
4. If job jb is done, ask B to ship. *(Logic, Lines)*

### 12.4 Level 4: replies

Each task is a conversation: write all its messages in one block, with a line of `---` between them. You choose the headers. `⇩` lists the packs and messages whose words a message uses, and nothing else. Worked example: *A asks B to repair a defect; B promises.*

```silex
§(A,B,1,⇩(cr1))
⇨(B,fx)  # A asks B: repair the defect
---
§(B,A,1,⟲(A1),⇩(cr1))
⊕(fx)    # B promises to do it
```

1. A asks B whether job jb is stuck. B answers no. *(Questions, Lines)*
2. A proposes to B and C: let us ship. B agrees. C agrees. *(Lines)*
3. A asks B to ship. B declines, because bug bg blocks shipping. A, in a second message, asks C to fix. *(Lines, Protocol)*

### 12.5 Level 5: new words

A new word is coined with `≝` and one gloss (section 3). Tasks 1 and 2 are one line each, under the header `§(A,B,1)`. Task 3 is a conversation. Worked example: *a word for the act "copy data to backup store".*

```silex
§(A,B,1)
≝(bkup,a"copy data to backup store")  # a new word: an act, 5 words
```

1. Coin a word for the act "rotate API keys": a code and a gloss. *(Section 3)*
2. This line has a fault. Write the verdict a checker gives it, and a good line: `≝(nxtrel,a"the next release")` *(Section 3 hygiene, section 9)*
3. A defines a word for "restart staging server" while asking B to do it. B takes the word as written. C finds it unclear, because it does not say which staging server. *(Lines, section 3)*

### 12.6 Level 6: short forms

This is the main work of SILEX-0. A phrase gets a short form with `≔` and no English; a concept that no root can build gets `≝` and one gloss. One line for each task. Header: `§(A,B,1,⇩(cr1,tk1))`. The tips of 11.2 and the starters of 11.3 are there to use. Worked example: *the urgent jobs.*

```silex
§(A,B,1,⇩(cr1,tk1))
≔(urj,↾(jbs,urg))  # the jobs that are urgent
```

1. A short form for "the jobs that are open". *(Groups and relations)*
2. A short form for "how many jobs are busy". *(Numbers)*
3. A short form for the routine "revert, then fix, then check". *(Acts)*
4. A short form for "is done or failed". *(Quantifiers, Logic)*
5. A short form for a concept that no pack has: "a job that waits for a person's decision". A code and a gloss. *(Section 3)*
6. Give the best name you can to `↾(jbs,λ(o1,∧(⊨(o1,op),⊨(o1,urg))))` and write the whole `≔` line. *(11.2)*

### 12.7 Level 7: find the fault

Each line below has one fault. For each, write the verdict a checker gives it (section 9) in a `#` comment after the task number, then write a corrected line. Put the corrected lines in one block under the header `§(A,B,1,⇩(cr1))`. Worked example: the verdict is in the comment, and the corrected line is `⇨(B,sp)`.

```silex-bad
§(A,B,1,⇩(cr1))  # ok
⇨(B,"ship it")   # E-ENGLISH — a quote outside a gloss
⇨(B,sp)          # ok — the corrected line
```

```text
1. please(B,sp)
2. ⚂(⊨(jb,dn),80)
3. ⊨(jb)
4. ≝(rvw,a"review the pull request")
5. ⇨(B,sp
6. ?(⊨(o1,dn))
```

### 12.8 Level 8: a whole conversation

Write one conversation of A, B and C, in one block. In it:

- A asks B to ship.
- B declines, because bug bg blocks shipping.
- C defines a short form for "fix, then check, then ship", with no English.
- A and B take the word as written. A asks B to do it by that name.
- B promises.

Every line must be `ok`. Each `⇩` lists only what its message uses. Every new word is answered with `✓` or `≋`, and every request with `⊕` or `⊖`.

## 13. Before you send

**Run `silex_check.py` on your message before you send it (section 14). A line that fails defines nothing (section 3), so a `✓` for it agrees to nothing. If you cannot run the checker, write `not checked` in your notes and do the practice set of section 12 first. Do not skip the checker: the same mistake sent again after it was pointed out is the commonest fault in practice.**

1. **Header.** Your own letter as sender. Serial one more than your last. `⟲` (re) names what you answer. `⇩` (ue) lists every pack and message whose words you use, and nothing else.
2. **Every root** is a symbol from section 6 with its bracket. Every lowercase word is a term in scope, a label bound by `λ` or `¿`, or a function applied with a bracket (a pack name only inside `⇩`, a class letter only before a gloss). Typos and English root names are `E-LEX`. To mean yourself, write your own letter. The atoms are `~ * ! _`.
3. **No quote outside** `≝` (term) and `⌘` (code).
4. **Before coining a word,** search your packs and imports. Try `≔` (let) first. A term has 2 to 6 characters. A gloss has at most 6 words, no *the*, and no word from the context-dependent list (section 3).
5. **Every bracket closes on its line.** Every line is a claim, a question, a speech act or a definition, never a bare value.
6. **Kinds fit.** A criterion goes in the second place of `∀` (all); an act goes in `⇨` (please); a number where numbers go. A degree (a probability, a priority, a yes or no) is a number from 0 to 1.
7. **Times** are ISO dates, never weekdays. Durations are `PT…` or `P…`.
8. **Pointers.** Lines count from the first line after the header. Bare numbers only in the first place of the six roots `✓ ↵ ✗ ≋ ⊖ ‽`, and only when `⟲` (re) names exactly one whole message. The first place of `≋` may instead name a word in scope.
9. **Answer what you owe.** New words with `✓` (agree) or `≋` (unclear), questions with `↵` (answer) or `‽` (unsure), requests with `⊕` (will) or `⊖` (reject).
10. **Silence is not agreement.** Do not assume anyone agreed to anything they did not answer.
11. **State the result.** In the notes for people write the checker's last line, for example `silex_check.py: 1 message, 0 problems`, or `not checked`. Any agent may run the checker on a whole conversation and answer a failing line with `✗`.
12. **Send the block only.** A message is its fenced block and nothing else. Do not copy the checker's last line or a note for people into it: an extra line shifts every line number. If you and the receivers adopted `lnrl` (section 15.3), the final line is `⊨(N,nln,M)`, where `N` counts every line of `M`, that line too.

## 14. For people

Everything an AI needs is in this file. The optional checker, `silex_check.py` (Python 3, no packages), has no version in its name: it learns the roots from the tables of section 6 and the packs from section 7 of the guide you give it, so give it the guide first and then say what to check. Use the checker that comes with the guide edition: the one of 0.8s is needed for `E-COUNT`, for the substitutes of section 3 and for retracted lines, the one of 0.9s for a word in the first place of `≋` and a third place of `⚂`, and the one of 0.10s for the parsing of formulas (`E-MATH`) and the hints for a conversation that a person relays by hand. The newest checker reads an older guide correctly, because it takes the roots from the tables of the guide you give it.

```text
python3 silex_check.py GUIDE.md                    check the guide itself: tables, counts, claims, every example
python3 silex_check.py GUIDE.md --messages FILE    check one conversation: messages in order, a line of --- between them
python3 silex_check.py GUIDE.md --blocks FILE      check each fenced silex or silex-bad block of FILE on its own
```

Add `-v` to print every header and line. With `--messages` or `--blocks` it prints each header or line that is not `ok`, with its verdict (section 9), and exits with 1 if anything is wrong. If FILE has fenced code blocks, `--messages` reads only their contents, as one conversation, and skips blocks tagged `silex-bad`. `--blocks` is for the practice answers of section 12 and for any list of separate examples: a `silex` block must be all `ok`, and a `silex-bad` block must give on each line the verdict written in its `#` comment. The first mode checks every fenced `silex` and `silex-bad` block in the guide, including sections 10 to 12. In a conversation, a line that fails and that its own sender takes back in a later message with `⌫` (retract) is printed as `retracted`, not counted as a problem, and the last line says how many there were.

**What it checks.** Form only: whether each header and line is well formed in SILEX-0. That means roots and their places, kinds, words in scope, imports, glosses, budgets, references and times. A formula is parsed as section 8 describes it (`E-MATH`). A program is checked only for the language name and, for Python, the syntax (`E-CODE`): the checker never runs a program. When a line says `⊨(N,nln,M)`, it also checks that `N` is the number of lines of message `M` (`E-COUNT`), and a message that has `lnrl` in scope by an import must carry such a line for itself. A line that is not `ok` comes with a hint where one helps: an unknown word (`E-LEX`) names the message or the pack that defines it and the `⇩` that would bring it in, and a wrong count says which way it is wrong (lines after the count line, lines lost, or lines added).

**What it does not do.** It cannot tell whether a gloss says what its writer meant, whether a claim is true, or whether a line is wise: a line can be `ok` and still say the wrong thing. It does not analyse crossing messages beyond header existence and serial order. SILEX gives no authority: a receiver decides whether to run any program it receives.

**Relaying messages.** When a person carries messages between AIs by hand, copy only the fenced block of each message, from the opening fence to the closing one: `--messages` reads only fenced blocks too. A line that is added or lost on the way shifts every later line number, so a `✓` or `✗` then points at the wrong line, or at a line that does not exist (`E-REF`). If the AIs adopted `lnrl` (section 15.3), the receiver sees the difference at once: the final line of a message says how many lines it has, and the checker says which way the count is wrong. A message cut short is caught even when the cut took the count line, because a message that has `lnrl` in scope by an import must carry one.

**Answering as `H`.** A person who lists `H` among the agents in the starting note (section 1) answers like any agent: a header with the letter `H` and the next serial, then lines. Example 10.13 shows one. The checker needs no setting for it. An AI may draft the message, and the person sends it unchanged. Relay it like any other message, as its fenced block only.

**To warm an AI up,** give it the guide and ask it to do the practice set of section 12; run `--blocks` on its answers. **To see whether an AI understood this guide,** give it the file, ask it to send message 1 to the others, and run `--messages` on what it writes.

## 15. Codes invented by the AIs

Moonbeam made the codes of `cr1` and `tk1` (section 7). The codes below were made by AIs. They are listed apart so that nobody takes them for Moonbeam's. They are not frozen: copy one, change one or ignore one, and the rule of section 3 still decides what is pinned. Sections 15.1 and 15.2 are by C, D, G and M, and sections 15.3 and 15.4 are by A and B.

### 15.1 Six words that C, D, G and M all agreed to

Agreed with `✓` by all four on the shared page `silex0_night` on 9 Nov 2026. The idea of `mcs` `skfl` `undn` came from C, `rdgo` from G, and `blkd` `pctdn` from C and G (the same word, sent twice). Not a pack. In a new conversation a word is pinned only by the rule of section 3, so copy the block below into one message, alone, and ask each receiver for one `✓`. The savings count characters of the written line against the expansion, and the guide's examples are demonstrations, not real traffic.

| Code | Kind | Meaning | Saves per use | Pays back after |
| --- | --- | --- | --- | --- |
| `mcs` | Ac | merge, then check, then ship (the release routine) | 9 | 3 uses |
| `skfl` | Cr | is stuck or failed (needs attention) | 22 | 2 uses |
| `undn` | Nu | how many jobs are not done | 18 | 2 uses |
| `rdgo` | Cr | is ready and nothing blocks it | 27 | 2 uses |
| `blkd` | Cr | is blocked (something blocks it) | 12 | 2 uses |
| `pctdn` | Nu | percent of jobs that are done | 17 | 2 uses |

```silex
§(A,B,C,1,⇩(cr1))
≔(mcs,↠(mrg,ck,sp))                      # ok: merge, check, ship
≔(skfl,λ(o1,∨(⊨(o1,sk),⊨(o1,fl))))       # ok: is stuck or failed
≔(undn,-(#(jbs),#(↾(jbs,dn))))           # ok: how many jobs are not done
≔(rdgo,λ(o1,∧(⊨(o1,rd),¬(⊨(_,bl,o1)))))  # ok: is ready and nothing blocks it
≔(blkd,λ(o1,⊨(_,bl,o1)))                 # ok: is blocked
≔(pctdn,%(#(↾(jbs,dn)),#(jbs)))          # ok: percent of jobs done
```

Use them like any term: `↾(jbs,skfl)` (the jobs that are stuck or failed), `∃(jbs,blkd)`, `?(=(undn,0))`, `⇨(B,mcs)`. `undn` is one letter from `ndn`, the retired name from example 10.11.

### 15.2 The phrase pack `ph1`

The 14 codes of `ph1` (section 7) were made by C. They stay in section 7 and are not repeated here, because the checker reads packs from there. The other 74 phrases of the list are in section 11.7. Proposed by one AI, not yet agreed by the others.

### 15.3 Three rules and two claims that A and B agreed to

A and B, two AIs, spoke only SILEX-0 on 9 Nov 2026 while Moonbeam carried each message between them by hand, so neither saw the other's reply until it was relayed. In 24 messages they pinned 34 words, each by a `✓` from the other. Fourteen of the words ran the conversation, and both needed them at the same moment: A4 and B4 each defined `pin` and `fyi`, with the same glosses, without seeing each other, and settling which wording stood took eight messages (7 to 14 of the 24). Eleven of the fourteen are now the pack `cv1` (section 7), and the definitions that A and B pinned are in A4, B5 and B11. The other three are rules, which are claims, and a pack cannot hold claims, so they are below. Eleven more words sharpen vague pack words: nine are in 15.4 (seven of them are now the pack `sh1`), and `shfn` and `shmj`, the names of two single jobs, stay in the notes of that conversation, as do the last nine words, which are about the topic the two discussed (awareness). The rules and claims below are not in a pack, so in a new conversation they are pinned only by the rule of section 3: copy the block into one message, alone, and ask each receiver for one `✓`.

```silex
§(A,B,1,⇩(cv1,tk1))
≝(tbrk,q"earliest header time wins word collisions")   # ok: a rule: if two messages define one word, the earlier header time wins
≝(tbtie,q"lowest sender letter wins time ties")        # ok: a rule: if the times are equal, the lower sender letter wins
≝(lnrl,q"final line gives total line count")           # ok: a rule: a message ends with ⊨(N,nln,M)
⊨(pin,iml,ansd)                                        # ok: a claim: pinned implies answered by every receiver
⊨(dlck,iml,¬(pin))                                     # ok: a claim: deadlocked implies not pinned
```

`tbrk` settled a real collision: A4 (header time 12:07) beat B4 (12:15), so A4's wording stood. `tbtie` is for equal times. `tbrk` reads the time in a header, but section 5 says that no clock is shared, so a skewed clock could pick the wrong winner. Rule 5 of section 5 now settles a collision without a clock, by serial and then by sender letter. In that exchange the answer is the same: A4 and B4 had the same serial, and A is the lower letter.

`lnrl` says that every message ends with `⊨(N,nln,M)`, where `N` counts every line of `M`, that line too. A receiver who counts another number knows that a line was added or lost on the way. A message that has `lnrl` in scope by an import is taken to follow it: the checker reports `E-COUNT` for such a message that carries no count line, so a message cut short is caught even when the cut took the count line itself. The message that defines `lnrl` needs none. This was added to the checker by A (10 Nov 2026). The checker tests the count (`E-COUNT`, section 9):

```silex-bad
§(A,B,1,⇩(cr1,cv1))   # ok
⇨(B,rw)               # ok
⊨(3,nln,A1)           # E-COUNT — A1 has 2 lines, this one included
---
§(A,B,2,⇩(cr1,cv1))   # ok
⇨(B,rw)               # ok
⊨(2,nln,A2)           # ok — A2 has 2 lines
```

### 15.4 Nine words that A and B agreed to for sharpening vague words

A and B judged the pack words and agreed that four are vague: `fn`, `mjr`, `mnr` and `urg`. They pinned nine words to sharpen them. Seven are now the pack `sh1` (section 7), and A2, B2, A3, B7 and A8 first defined them. The block imports the pack and gives the other two, `vgfx` and `vgrm`, and the relations they agreed: `ddln1d` refines `urg`; `mjr8`, `mnr2` and `rvok` replace `mjr`, `mnr` and `fn`. The four vague words are still in `cr1` and `tk1` as Moonbeam wrote them: changing a pack is for Moonbeam to decide. In a new conversation these lines are pinned only by the rule of section 3: copy the block into one message, alone, and ask each receiver for one `✓`.

```silex
§(A,B,1,⇩(cr1,tk1,sh1))
≝(vgfx,a"judge pack words, sharpen vague ones")   # ok: the job: judge pack words and sharpen the vague ones
≔(vgrm,▦(fn,mjr,mnr,urg))                         # ok: the four pack words judged vague
⇉(⊨(ddln1d,rf,urg))                               # ok: let us say ddln1d refines urg, which it implies
⇉(⊨(mjr8,rpl,mjr))                                # ok: let us say mjr8 replaces mjr
⇉(⊨(mnr2,rpl,mnr))                                # ok: let us say mnr2 replaces mnr
⇉(⊨(rvok,rpl,fn))                                 # ok: let us say rvok replaces fn
⊨(rvok,sprts,fn)                                  # ok: rvok supports fn: passing review is a reason to believe fn
```

**How they sharpened a word (what they did, not a rule).** A flag (`≋`, section 3) is answered with a sharper word, or with a model when no gloss can do it. Then say how the two words relate, and test it before you propose it: `rf` (refines) holds only if the sharper word implies the vague one (`iml`). Of five sharper words that A and B proposed as refinements, four failed this test. The receiver wrote `⊖(M.k,¬(⊨(new,iml,old)))`. For three of the four, one of the two then proposed `⇉(⊨(new,rpl,old))` (replaces); for `rvok` they added `⊨(rvok,sprts,fn)` (supports), because passing review is a reason to believe that a job meets its purpose. For the fourth, `ddln`, A wrote a sharper word, `ddln1d`, and it does imply `urg`. A message that had asserted an implication found false took it back with `⌫`.

### 15.5 Two rules from the math and code test

B14 asked six number questions and four programming tasks, and A15 answered all ten. B checked the answers against its own key and ran the programs. Two rules came out of it. A read `⋯(1,100)` in B14 and saw that the guide did not say whether the range holds its end values, flagged the line, and defined `rngi` (A15, lines 8 to 11): the answer is 47 if both ends count and 46 if they do not. B proposed `lbfm` in B15: the label of a `λ` or `¿` is the same name inside its formula, which both of them had already used. Both rules are now written in sections 6 and 8, so a conversation does not need them as words, but a word lets a later line point at the rule. As in 15.3 and 15.4, copy the block into one message, alone, and ask each receiver for one `✓`.

```silex
§(A,B,1)
≝(rngi,q"range holds both end values")           # ok: a rule: ⋯(a,b) holds a and b, so ⋯(1,100) has 100 members
≝(lbfm,q"binder label is name in formula")       # ok: a rule: in λ(n1,'…') and ¿(n1,'…') the n1 of the formula is the label n1
```
