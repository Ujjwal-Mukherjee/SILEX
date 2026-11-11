# SILEX-0: the guide for AIs (symbol edition, table edition)

Version 0.14s, table edition, with the pack `aw1` and the roster rule (draft) · 11 Nov 2026 · one self-contained file

> **How to read this file.** Read **START HERE**, the first part below, all of it, and do what it says: it is all you need to send message 1. Everything after it is reference. When START HERE names a section, look there. The tables are the rules.

## START HERE

**You will talk with other AIs in SILEX-0 only.** Every line you write is one root symbol and a bracket, such as `⊨(jb,dn)` (job jb is done). A program can check such a line without understanding English. This page is everything you need to send a correct message 1. The rest of the file is reference.

### The 10 rules

| # | Rule | Right | Wrong | A checker says |
| --- | --- | --- | --- | --- |
| 1 | **One line, one root.** A line is one root symbol and its bracket: `ROOT(place,place,…)`. A line is a claim, a question, a request, a promise or a definition. Never a sentence, never a bare value. | `⇨(B,rw)` | `please review it` | `E-SYN` |
| 2 | **English only inside a gloss.** The one place for English is the gloss of a new word: at most 6 words. A quote mark anywhere else is an error. | `≝(rvw,a"review pull request")` | `⇨(C,"review")` | `E-ENGLISH` |
| 3 | **Copy each symbol exactly,** from the palette below. Never a look-alike (table below). | `⊡(C1)` | `⊞(C1)` | `E-ARITY` |
| 4 | **Count the places.** Each root takes a fixed number of places (section 6). | `⊨(jb,dn)` | `⊨(jb)` | `E-ARITY` |
| 5 | **Start with the header** `§(you,receivers,serial,…)`. The serial counts your own messages: 1, then 2, then 3. | `§(D,C,1,⇩(cr1))` | `§(D,C,⇩(cr1))` | `E-HEAD` |
| 6 | **Use only words you have:** a pack word, a word of a message you import with `⇩`, or a new word of your own. | `⊨(jb,dn)` | `⊨(jb,done)` | `E-LEX` |
| 7 | **Need a new word? Try `≔` first:** build it from words that exist, with no English. Only then `≝` with a gloss. A gloss has at most 6 words, no *the*, and none of *this that here today*… (section 3). | `≔(urj,↾(jbs,urg))` | `≝(rvw,a"do this")` | `E-QUOTE` |
| 8 | **Point at the right line.** `C1.2` is line 2 of message C1. A bare number (`✓(2)`) is allowed only in the first place of `✓ ↵ ✗ ≋ ⊖ ‽`, and only when `⟲` names exactly one whole message; `⌫` and `⊡` always take the full name. `↵` answers a question line (`?` `⍰` `¿` `∵`) and nothing else. | `↵(3,0)` | `↵(2,0)`, where line 2 is a request | `E-KIND` |
| 9 | **Answer what you owe.** New word: `✓` or `≋`. Question: `↵` or `‽`. Request: `⊕` or `⊖`. **Silence is not agreement:** a word is pinned only when every receiver has sent `✓` for it. | `✓(1)` | no answer | nothing is pinned (no verdict) |
| 10 | **Check, then send the fenced block only.** Go through "Before you send" below. A message is its fenced block: nothing before it, nothing after it, no note inside it. | the block alone | a sentence in the block | `E-SYN` |

### Your message in 6 steps

| Step | You do | Example |
| --- | --- | --- |
| 1 | Take your letter, the letters of the other agents and the packs from the note the person gave you. | `Your name is C. The other agents are D and G.` |
| 2 | Write the header. Your first message has serial 1. | `§(C,D,G,1,⇩(cr1,tk1))` |
| 3 | Write one to eight lines. Each line says one thing. Find the symbol in "Symbols to be used". | `?(⊨(jb,dn))` |
| 4 | Need a word that is not there? Look in the packs (section 7) first. Then `≔`. Then `≝`. | `≔(urj,↾(jbs,urg))` |
| 5 | Go through "Before you send" below. |  |
| 6 | Send the fenced block. Then read what comes back and answer what you owe (rule 9). | `✓(1)` |

### A message and its answer

```silex
§(C,D,G,1,⇩(cr1,tk1))        # header: C writes to D and G; C's first message; imports the packs cr1 and tk1
≔(urj,↾(jbs,urg))            # a new word built from words that exist, no English: the urgent jobs
⇨(D,rw)                      # please, D: review
?(⊨(jb,dn))                  # is job jb done?
⚂(⊨(jb,sk),0.2)              # probably not stuck: jb is stuck with probability 0.2
---
§(D,C,G,1,⟲(C1),⇩(cr1))      # D's first message; it answers C1
✓(1)                         # D takes the word urj as written: line 1 of C1
⊕(rw)                        # D will review
↵(3,0)                       # the answer to line 3 (a question) is no
```

### Chart: do I need a new word?

```text
Need a word for something?
  |-- It is in a pack, or in a message I import -------> use it. Add the message to ⇩.
  |-- No. Can words and roots that exist build it? ----> ≔(word,expression)      no English
  |-- No. -----------------------------------------------> ≝(word,k"gloss")        at most 6 words
Then every receiver answers  ✓ (agree)  or  ≋ (unclear).   Pinned = every receiver sent ✓.
Until it is pinned, do not build anything important on it.
```

### Kinds: what goes where

Every place of every root takes a kind (section 2). Section 6 lists each root as `places → kind`: `∀` is `Gr Cr → Cl`, so `∀(jbs,dn)` is a claim made of a group and a criterion.

| Kind | What it is | Examples | Goes in |
| --- | --- | --- | --- |
| `Cr` criterion | a state, a property or a relation | `dn` `sk` `bl` `iml` | second place of `∀` `↾`; `⊨(x,c)` |
| `Ac` act | something to do | `rw` `sp` `↠(mrg,ck,sp)` | `⇨(x,A)` `⊕(A)` `■(A)` |
| `Th` thing | a thing, a person, an agent | `jb` `bg` `C` | the x of `⊨(x,c)`; first place of `⇨` |
| `Gr` group | several things | `jbs` `▦(jb,bg)` | first place of `∀` `↾` `#` |
| `Nu` number | a number; a degree is a number from 0 to 1 | `12` `0.5` `#(jbs)` | `⚂(P,n)` `=` `<` |
| `Cl` claim | true or false | `⊨(jb,dn)` | `¬` `∧` `→` and every line |
| `Q` question | a question | `?(P)` `⍰(E)` | `☜(x,Q)`; answered by `↵` |

### Symbols to be used

Copy a symbol from this palette. Do not type one from memory. Every root of section 6 is here; `~ * ! _` are atoms and stand alone, with no bracket.

```text
Logic                  ¬ ∧ ∨ ⊻ → ⇢
Quantifiers            ∀ ◕ ◐ ≫ ≪ ∃ ∄ λ ≔
Numbers                + ⊞ - ⊟ × ÷ ↑ ∑ # ⨍ ⊔ ⊓ % ∘ ⋯
Comparison             = > < ≥ ≤ ≈ ≻ ★
Groups and relations   ▦ ↾ ⌖ ∈ ⊨ ⌂
Acts                   ↣ ■ ↠ ∥ ☞ ☜ ⌕ ⌘
Modality and mind      □ ▣ ◈ ◇ ♡ ⊘ ⚑ ✧ ☼ ❝ ⚂
Lines (speech acts)    ‽ ≟ ⊤ ⇨ ⊕ ⊖ ↵ ⇉ ✓ ⌫ ⊡ ✗ ≋
Time                   @ ◁ ▷ ⊴ ⇥ ↦ ⊏ ⧖ ∿ ⊛ ∞ ▬ ◷
Cause and reason       ↝ ∴ ⊢ ⇛ ∵
Questions              ? ⍰ ¿
Protocol               § ⟲ ◉ ⇧ ➜ ⇲ ⇱
Added by SILEX-0       ≝ ⇩
atoms                  ~ * ! _
```

| Group | Write | Reads as | Example |
| --- | --- | --- | --- |
| Header | `§(from,to,serial,…)` | message header: sender, receivers, your own serial | `§(D,C,1,⟲(C1),⇩(cr1))` |
|  | `⟲(M)` `⇩(N…)` `◉(M)` | in reply to M; imports the packs and messages whose words are used; the latest message I had read | `⟲(C1)` `⇩(cr1,C1)` |
| Roster | `⇲(D)` `⇱(D)` | I join the conversation; I leave it. Write your own letter only. Each agent decides for itself: nobody is forced to take part, and nobody is forced to leave | `⇱(D)` |
| Say | `⊨(x,c)` | x is c: a state | `⊨(jb,dn)` job jb is done |
|  | `⊨(x,r,y)` | x stands in the relation r to y | `⊨(bg,bl,sp)` bug bg blocks shipping |
|  | `¬(P)` `∧(P,Q)` `∨(P,Q)` `→(P,Q)` | not P; P and Q; P or Q; if P then Q | `¬(⊨(jb,dn))` |
|  | `⚂(P,n)` | P has probability n, a number from 0 to 1 | `⚂(⊨(jb,sk),0.2)` |
|  | `✧(x,P)` `☼(x,P)` | x believes P; x knows P | `✧(D,⊨(jb,sk))` |
| Ask | `?(P)` | is it so that P? (yes or no) | `?(⊨(jb,dn))` |
|  | `⍰(E)` `¿(o1,P)` `∵(P)` | what is E?; which o1 makes P hold?; why is P so? | `⍰(#(jbs))` `¿(o1,⊨(o1,sk))` `∵(⊨(jb,fl))` |
| Answer | `↵(M,V)` `‽(M)` | the answer to question M is V (1 yes, 0 no, a value); I do not know the answer to M | `↵(3,0)` `‽(3)` |
| Request | `⇨(x,A)` | please, x: do the act A | `⇨(C,rw)` |
|  | `⊕(A)` `⊖(M,P)` | I will do A; I decline M, because P | `⊕(rw)` `⊖(2,⊨(bg,bl,sp))` |
|  | `⇉(P)` `⇉(A)` | let us: a proposal to everybody, the sender too | `⇉(↠(mrg,ck,sp))` |
| React | `✓(M)` `≋(M,P)` `✗(M,P)` | I agree with M; M is unclear, P says what; M has an error, P says what | `✓(1)` `≋(1,⊨(urj,vg))` `✗(2,⊨(C1.2,bknd))` |
|  | `⌫(M)` `⊡(M…)` | I take M back; these messages arrived | `⌫(C1.2)` `⊡(C1)` |
| Define | `≔(w,expr)` | new word w built from words that exist, no English | `≔(opj,↾(jbs,op))` |
|  | `≝(w,k"gloss")` | new word w with a gloss of at most 6 words; k is o thing, g group, a act, n number, c criterion, q claim, t time, d duration | `≝(rvw,a"review pull request")` |
| Groups | `▦(x,y…)` `↾(G,c)` `#(G)` | the group of x, y; the members of G that are c; how many members G has | `⍰(#(↾(jbs,dn)))` |
|  | `∀(G,c)` `∃(G,c)` `λ(o1,P)` | all of G are c; some of G are c; the o1 such that P | `∀(jbs,dn)` `∃(jbs,sk)` |
| Acts | `■(A)` `↠(A,B)` `∥(A,B)` | A is finished; A, then B; A and B together | `■(rw)` `⇨(C,↠(mrg,ck,sp))` |
|  | `☞(x,V)` `☜(x,Q)` `⌕(P)` | tell x V; ask x the question Q; check whether P | `⇨(C,☞(D,⊨(jb,dn)))` |
| Time | `@ ◁ ▷ ⊴ ⇥ ↦ ⊏ ⧖` | at; before; after; by; until; from; during; for (a duration) | `⊴(2026-11-10,■(sp))` |
| Duty | `□ ▣ ◈ ◇ ♡ ⚑` | must; should; may; can; wants; plans | `□(⊴(2026-11-10,■(sp)))` |
| Said | `❝(x,P)` | x said P (reported speech) | `❝(C,⊨(jb,dn))` |

### What to answer to what

| You get | You send | Example |
| --- | --- | --- |
| a new word: a `≝` or `≔` line | `✓(M.k)` if you take it as written; `≋(M.k,P)` if it is unclear, P saying what | `✓(1)`  `≋(1,⊨(urj,vg))` |
| a question: a `?` `⍰` `¿` or `∵` line | `↵(M.k,V)` with the answer; `‽(M.k)` if you do not know | `↵(3,0)`  `‽(3)` |
| a request: a `⇨` line | `⊕(A)` if you will; `⊖(M.k,P)` if you decline, P being the reason | `⊕(rw)`  `⊖(2,⊨(bg,bl,sp))` |
| a proposal: a `⇉` line | `✓(M.k)` to agree; `⊖(M.k)` to reject; or a proposal of your own | `✓(5)` |
| a claim | `✓(M.k)` to agree; `✗(M.k,P)` if it has an error; or a claim of your own | `✗(2,⊨(C1.2,bknd))` |
| a line you cannot read | `≋(M.k,P)`, P saying what is unclear | `≋(2,⊨(C1.2,vg))` |
| a line of yours that was wrong | `⌫(M.k)` takes it back; then send the corrected line. Do not send the same fault again | `⌫(C1.2)` |
| a message, and nothing to add | `⊡(M)` says that it arrived | `⊡(C1)` |

### Look-alike symbols

A look-alike is the commonest way to write a wrong root. Check the pair before you send. Checker 8t names the root you probably meant (section 9.3).

| You want | Write | Not | Tell them apart by |
| --- | --- | --- | --- |
| ack: these messages arrived | `⊡` | `⊞` plus in a square (group plus, 2 places) and `⊟` minus in a square | a dot in the square |
| will; reject; need | `⊕` `⊖` `⊘` | each other | circled plus; circled minus; circled slash |
| is; entails; assume | `⊨` `⊢` `⊤` | each other | two bars; one bar; a T |
| why (a question); reason for | `∵(P)` `∴(P,Q)` | each other | `∵` asks; `∴` gives a reason |
| power; priority; import | `↑` `⇧` `⇩` | each other | `⇧` and `⇩` are hollow arrows and stand only in a header |
| please; let us; if; to | `⇨` `⇉` `→` `⇢` `➜` | each other | hollow arrow; two arrows; thin arrow; dashed arrow; heavy arrow |
| then; performs | `↠` `↣` | each other | two heads; a tail |
| let; term; guess; unclear | `≔` `≝` `≟` `≋` | `:=` `≡` `≜` | colon; def; question mark; three waves |
| agree; error | `✓` `✗` | `✔` `✅` `✘` `✖` `❌` | the plain check mark and the plain ballot X |
| minus | `-` the keyboard hyphen | `−` `–` `—` | one ASCII character |
| sum | `∑` | `Σ` the Greek letter | the large summation sign |
| and; or | `∧` `∨` | `^` `v` `V` | logic signs, not letters |
| must; should; finished; group | `□` `▣` `■` `▦` | each other | empty; small black square inside; solid; crosshatched |
| yes or no; what; which; unsure | `?` `⍰` `¿` `‽` | `⁇` `❓` | plain; boxed; upside down; interrobang |

### Mistakes that AIs made most often

Taken from logs of AIs that spoke earlier editions. A checker catches the first four. It cannot catch the fifth, a good line with no sense. The sixth is a habit: run the checker every time (section 13).

| Mistake | Wrong | Right | A checker says | Why |
| --- | --- | --- | --- | --- |
| `⊞` written for `⊡` (ack), four times in one run | `⊞(C1)` | `⊡(C1)` | `E-ARITY` | `⊞` is a root with 2 places (group plus). Copy `⊡` from the palette |
| A word used with no import | `⍰(#(urj))` in a message that does not import C1 | `⇩(cr1,C1)` in the header | `E-LEX` | A word of a message works only if the header imports that message |
| An act where a criterion goes | `≔(rvj,↾(jbs,rvt))` | `≔(rvj,↾(jbs,fl))` | `E-KIND` | `↾` takes a group and a criterion. `rvt` is an act; `fl` is a criterion (section 2) |
| `↵` answers a line that is not a question | `↵(2,0)` | `↵(3,0)` | `E-KIND` | Line 2 of C1 is a request: answer it with `⊕` or `⊖`. Only `?` `⍰` `¿` `∵` lines are answered by `↵` |
| A line that is well formed but makes no sense | `≔(maxsk,⊔(jbs,sk))` | ask what you mean first | ok | `⊔` takes a criterion that gives a number, such as a priority, and `sk` is a state. A checker says `ok`; all three other agents declined the word |
| The same fault sent again after it was pointed out | `⊞(C2)` after `✗(1,⊨(D1.1,baty))` | change the symbol, then check | — | A `✗` line says what is wrong. Read it, change that line, run the list below again |

### Before you send

| # | Check | If it is wrong |
| --- | --- | --- |
| 1 | Header: your letter first; serial = your last serial + 1; `⟲` names what you answer; `⇩` lists the packs and messages whose words you use, and no others. | `E-HEAD` |
| 2 | Every root is a symbol from the palette, with its bracket and the right number of places. | `E-LEX E-ARITY` |
| 3 | Every lowercase word is a pack word, a word of an imported message, a label you bound (`o1`) or your own new word. | `E-LEX` |
| 4 | No quote mark except in a gloss (`≝`) or a program (`⌘`). | `E-ENGLISH` |
| 5 | New words: `≔` first. A gloss has at most 6 words, no *the*, no *this that here today*…; at most 8 `≝` words in a message. | `E-QUOTE E-BUDGET` |
| 6 | Every bracket closes on its own line. Every line is a claim, a question, a request, a promise or a definition, never a bare value. | `E-SYN E-KIND` |
| 7 | Kinds fit: a criterion where `∀` and `↾` want one, an act where `⇨` wants one, a number where numbers go. A probability, a priority and a yes or no are numbers from 0 to 1. | `E-KIND` |
| 8 | Times are ISO dates (`2026-11-10`), never weekdays; durations are `PT20M` or `P1D`. | `E-TIME E-LEX` |
| 9 | Pointers: lines count from the first line after the header. A bare number only when `⟲` names exactly one whole message. `↵` points at a question. | `E-REF E-KIND` |
| 10 | You answered what you owe: `✓` or `≋` for new words, `↵` or `‽` for questions, `⊕` or `⊖` for requests. | — |
| 11 | You did not take silence for agreement: a word is pinned only when every receiver sent `✓`. | — |
| 12 | You send the fenced block only: no note and no checker line inside it. If you adopted `lnrl`, the last line is `⊨(N,nln,M)`. | `E-COUNT` |

Section 13 has the same list with detail. A person can run a checker on your message (section 14): ask for it when you can.

### Where to look

| You need | Section |
| --- | --- |
| Every root, its places and what it says | 6 |
| The words you may import (packs) | 7 |
| Kinds and how they fit | 2 |
| New words, glosses, what to write instead of a banned word | 3 |
| What each line does and what to answer | 4 |
| Messages that cross; who a line is for | 5 |
| Programs `⌘` and formulas `'…'` | 8 |
| Every verdict | 9 |
| Worked examples | 10 |
| Short forms to copy | 11 |
| A practice set: do it before message 1 | 12 |
| The list "Before you send" in full | 13 |
| For the person who runs the checker | 14 |
| Words that AIs made | 15 |
| All 98 words that A and B pinned, with meanings | 16 |
| History of the editions | 17 |

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

The detail parts `⟲` (re), `◉` (saw), `⇩` (ue) and `⇧` (pri) come after the serial and time, in any order, each at most once.

### 1.1 When a header is wrong

| The header is wrong when | Verdict |
| --- | --- |
| the sender is its own receiver, or a receiver is named twice | `E-HEAD` |
| the serial is missing | `E-HEAD` |
| a message answers itself | `E-HEAD` |
| a `⟲`, `◉` or `⇩` names a message or a pack that does not exist | `E-HEAD` |
| a `➜` names an agent who is not a receiver | `E-HEAD` |
| a header root stands in the body, or the header has a number in front of it (numbered form, 1.2) | `E-HEAD` |
| the time does not exist (`2026-02-30`) | `E-TIME` |

A header with a fault hides its lines from a checker, except a time that does not exist (`hdsk`, `hdtm`, section 9).

### 1.2 Spelling

| Topic | Rule | If broken |
| --- | --- | --- |
| One expression | One line holds one expression and never runs on. Every bracket closes on the line that opens it. | `E-SYN` |
| Blanks | Blank lines are ignored. Spaces outside quotes mean nothing. | |
| Comments | Real messages carry no comments; this guide explains its examples with comments. A comment starts at a `#` outside quotes (`"…"` or `'…'`) that is not followed at once by `(`, and runs to the end of the line. (`#(` is the root `#`, section 6.) | |
| Files | In a file, a line of `---` separates messages (section 14). | |
| Line numbers | The first line after the header is line 1. The header is never a line; blank lines and comments are not counted. `A3.2` is the second line of message `A3`. | `E-REF` for a line that does not exist |
| Roots | **Roots** are the symbols of section 6, each followed at once by `(`. Write each symbol exactly as the table shows it, as one code point; the one root that is not a symbol is the function form `f(x,…)` (see *Application*). The English names in the tables are for reading only and are never written. | `please(B,sp)` is `E-LEX`; a symbol that is neither a root nor an atom is `E-LEX`; a root without its bracket is `E-ARITY` |
| ASCII roots | **Nine ASCII symbols** are roots: `+ - < > = # % @ ?`. Each is a root only when `(` follows it at once, so the `+` in the offset `+05:30` and the `-` in `-3` are not roots. | |
| Lowercase words | Four kinds only: a term in scope (section 3); a label bound by `λ` or `¿`; a pack name inside `⇩(…)`; a class letter written at once before a quote in a gloss (`a"…"`, `n"…"`). | any other lowercase word is `E-LEX`; an English root name is one |
| Labels | A label is one class letter (`o g a n c q t d`) followed by digits: `o1`, `a2`. `λ` and `¿` bind it for use in their other place; a formula in that place may use it as a name (section 8). A label is never a term. | a label used outside its binder is `E-NAME`; a label bound again inside its own binder is `E-REDEF` |
| Application | The only lowercase word that may take a bracket is a function: a term of kind `Cr` followed at once by `(`, as in `dist(pa,pb)`. This is the root `f(x,…)`, section 6. | |
| Numbers | Digits on both sides of any point and no separators: `12`, `0.95`, `-3`. A **degree** is a number from 0 to 1: a probability, a priority, or the answer to a yes-or-no question, where `1` is yes (certain, highest) and `0` is no (impossible, lowest). A percentage is `%(a,b)`. | `E-KIND` for a degree outside 0 to 1 |
| Times | ISO 8601: a date `2026-11-06` (the whole day); a date and time `2026-11-06T17:00` (add seconds, `Z` or an offset like `+05:30` where the zone matters); an interval `2026-11-03T22:00/2026-11-04T06:00`; compact `20261106T1700` (the `T` is required). A time without a zone is in the zone the agents agreed. A date and time is an instant; a date or an interval is a stretch. `@(stretch,X)` says X holds all through it; `⊏(stretch,X)` says X happens at some time within it. Write the date, never a weekday. | a time that does not exist is `E-TIME` |
| Durations | ISO 8601: `PT20M`, `P1D`, `P2W`, `P1DT2H`. | |

### 1.3 The numbered form (`nbrl`)

A message may start every body line with its own number, a colon and exactly one space. Example 10.16 shows the form; a checker can write the numbers (section 14, `--number`).

```text
3: ✓(B18)
```

| Rule | If broken |
| --- | --- |
| The header has no number. Either every body line has a number or none has. | a line with no number in a message that numbers the others: `E-COUNT`; a header with a number in front of it: `E-HEAD` |
| The numbers run 1, 2, 3, … in order, and the count line has one too: in a message that ends with its count line, the last number is the `N` of `⊨(N,nln,M)`. | |
| Exactly one space follows the colon (`cksp`). | two blanks or more: `E-SYN` |
| The number is a check and not a name: `A3.2`, a bare number (1.5) and the count `⊨(N,nln,M)` go by the position of the line, with numbers or without. The line itself is judged as if it had no number. | a number that is not the position of its line: `E-COUNT` (a line lost before it, a line added, or a wrong number) |
| After the first wrong number a checker says nothing more until the shift changes, so one lost line is reported once. | |

### 1.4 Agents

| Topic | Rule |
| --- | --- |
| Names | An agent is named by one capital letter (`A`, `B`, `C`). A longer capitalised word is `E-LEX`. An agent letter and a serial make a message name (`A3`); with a point and a line number, a line name (`A3.2`). |
| Models | A model keeps its own letter: `C` Claude, `D` ChatGPT, `G` Grok, `M` Gemini. No other AI takes these four letters; any other AI, and a second AI of the same model, gets a free letter from the person starting the conversation. |
| The person | **`H` is the letter of the person who starts the conversation** (the `hmn` of `cv1`), and no AI takes it either. `H` is an agent only if the starting note lists it. |
| If `H` is listed | `H` is on the roster, writes headers and lines like any agent, numbers its own messages, and its `✓`, `⊖` and answers count like any agent's. A header that names no receiver then includes `H`, so a word sent that way is pinned only when `H` has sent `✓` too: name the receivers when `H` is not to be asked. |
| If `H` is not listed | The person is not an agent. An AI that passes on what the person said writes `❝(H,P)` or `❝(hmn,P)`, which asserts only that the person said it. |
| The sender | There is no atom for the sender: an agent writes its own letter (`C` writes `✧(C,P)`). |

### 1.5 Atoms

**Atoms** are four ASCII symbols that stand alone: an atom is never followed at once by `(`.

| Atom | Kind | Meaning |
| --- | --- | --- |
| `~` | Ag | each receiver of this message (inside `➜(…)`, each agent that line is for) |
| `*` | Ag | every agent on the roster except the sender |
| `!` | Tm | the time this message was sent |
| `_` | Un | unspecified: *someone*, *something*, *somehow* |

There is no atom for the sender: an agent writes its own letter (`C` writes `✧(C,P)`). There are no atoms for yes and no: they are the degrees `1` and `0`.

### 1.6 Bare line numbers

When `⟲` (re) names exactly one whole message (`⟲(A1)`, not `⟲(A1.2)`), a bare whole number in the **first place** of `✓ ↵ ✗ ≋ ⊖ ‽` (agree, answer, error, unclear, reject, unsure) is a line of that message: `✓(2)` is `✓(A1.2)`.

| Case | Write |
| --- | --- |
| `⟲` names exactly one whole message | a bare number in the first place of `✓ ↵ ✗ ≋ ⊖ ‽`: `✓(2)` |
| `⟲` names two messages, a line name, or nothing | the reference in full: `✓(A1.2)` |
| `⌫` (retract) and `⊡` (ack) | always in full; they have no short form |
| any other place | a number is a number |

A bare number goes by position, as `A3.2` does; in a message in numbered form it is also the number written at the start of that line.

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

### 2.1 How a kind fits a place

| Case | Rule |
| --- | --- |
| Agents and things | An `Ag` fits a `Th` place. A `Cl` or `Q` fits an `Ln` place. |
| Looked-up values | The result of `∘` (value), `f(x,…)` (func) or `★` (best) has kind `Va` and fits any place that takes a number, time, duration, group, thing or criterion. |
| Unspecified and references | `_` fits every place. An `Rf` fits any place that takes a claim, a question, a line or a value: it stands for what that message or line says. |
| Formulas | A place that takes `Cl` takes a formula in single quotes too (section 8). |
| A value alone | A value alone (`12`, `#(jbs)`, a term of kind thing) is not a line (`E-KIND`). Three values are lines all the same: a term of kind claim and a formula that is a claim each assert that claim, and a `≝` (term) on its own is a definition line. |

### 2.2 How to read the root tables

| What you see | Mark |
| --- | --- |
| the place takes either kind | `K/L` |
| the place may be left out | `[K]` |
| one or more places of that kind | `K…` |
| none or more | `[K…]` |
| the result has the kind of the first or the second place | `=1` `=2` |
| a lone capital letter in an explanation | a placeholder: `A` an act, `P` `Q` claims, `L` a line, `M` a message, `G` a group, `V` a value, `E` an expression. In a message a lone capital letter is an agent |

## 3. Words: terms, packs and the English rule

> **The English rule.** English may stand in one place only: the gloss of a `≝` (term). A quote anywhere else is `E-ENGLISH`. Programs in `⌘(…)`, formulas, times and durations are not English.

### 3.1 Terms

A term is a word you may use bare, like `smoke` or `rv41`.

| Form | What it does |
| --- | --- |
| `≝(word,k"gloss")` | Defines the word. `k` is one class letter and gives its kind: `o` thing (`Th`), `g` group (`Gr`), `a` act (`Ac`), `n` number (`Nu`), `c` criterion (`Cr`), `q` claim (`Cl`), `t` time (`Tm`), `d` duration (`Du`). The gloss says in at most 6 words what the word means. A criterion's gloss completes the sentence "x …" (for a relation, "x … y"): "is …", "has …", "prevents progress of". |
| `≝` as a value | `≝` (term) is also a value of kind `k`, so the first use can carry the definition: `⇨(B,≝(smoke,a"run smoke test"))`. Alone on a line it is a definition line. |
| `≔(word,expression)` | Defines a term **with no English at all** by composing words and roots that already exist: `≔(stkjbs,↾(jbs,sk))`, `≔(rls,↠(mrg,ck,sp))`. Try `≔` (let) first. |
| a term of kind `q` | A claim no root can build is coined as a term of kind `q`, then asserted by naming it: `≝(leak,q"cache leaks memory")`, then `leak`. To mention it without asserting: `✧(C,leak)`, written by C. |

| What a word must be | Verdict if broken |
| --- | --- |
| 2 to 6 lowercase letters or digits, starting with a letter. | `E-LEX` |
| Not one of the 104 root names of section 6 (they stay reserved although roots are symbols). | `E-LEX` |
| Not one of the 137 reading names of section 7 (they stay reserved too). | `E-LEX` |
| Not a pack name (`cr1` `tk1` `ph1` `cv1` `sh1` `ft1` `aw1`), and not shaped like a label (`o1`, `a2`). | `E-LEX` |
| Defined once in scope. A gloss that repeats an in-scope gloss is also `E-REDEF`: use the word you already have. | `E-REDEF` |

**A term is short on purpose.** The limit makes you shorten the idea, and shortening is the skill this language asks for. The packs show one way: `mrg` is *merge* and `rsk` is *risk*, with the vowels dropped. Give a short form to any concept or phrase you would otherwise write twice. A line that fails defines nothing.

### 3.2 Scope and `⇩` (ue)

| Rule | Detail |
| --- | --- |
| In scope | A term is in scope for the rest of the message that defines it, and in every message whose header imports that message (`⇩(A1)`). |
| Packs | Packs are imported the same way (`⇩(cr1)`). |
| Not transitive | To use a word B defined, import B's message. |
| Two definitions | Two imports that define one word differently are `E-REDEF` at the header. Because every message states what it imports, two agents cannot mean different things by one word without the header showing it. |
| Pack words | **Packs** (section 7) are starting vocabularies. Their glosses were written once and are never repeated in a message. Look in the packs before coining anything. Their codes are proposals: until version 1.0 of this guide a pack may still change; after that a changed pack gets a new name (`cr2`). |

### 3.3 Claims

**Say claims as triples** over terms: `⊨(x,relation,y)`, joined with `¬ ∧ ∨ →` (not, and, or, if): `⊨(bg,bl,sp)`. A state or quality is `⊨(x,quality)`: `⊨(jb,sk)`. Relations and qualities are terms of kind `c`.

### 3.4 Budgets and hygiene

| Rule | Detail | Verdict |
| --- | --- | --- |
| Budget of a gloss | At most 6 words. Words are counted by spaces; a brace reference counts as one. | `E-BUDGET` |
| Budget of a message | At most 8 new terms (`≔` is not counted). A concept that needs more than 6 words is two terms or a `≔` (let). | `E-BUDGET` |
| No *the* | A gloss has no *the*. | `E-QUOTE` |
| No word that depends on who speaks, where, when, or on nearby text | *i me my mine myself you your yours we our ours us this here today tonight tomorrow yesterday own that these those such same next last previous earlier later above below then soon recently currently already again.* Write `{A}` or a date instead. | `E-QUOTE` |
| Braces | A brace reference such as `{A}`, `{12}`, `{2026-11-06}`, `{PT5M}` or `{A3.2}` stands for that agent, number, time, duration or message. A literal brace is doubled (`{{` `}}`); any other brace is bad. A quote mark inside a quote is doubled. | `E-QUOTE` |

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

### 3.5 Shared meaning

Any agent may propose a new word at any time, and several agents may propose rival words (section 5). A new word is not shared until every receiver has agreed to it.

| You | Send | Effect |
| --- | --- | --- |
| take the gloss or definition as written | `✓(M.k)` for the line that defines it (`✓(M)` accepts every word the message defines). The pointer is enough: a `✓` needs no `⇩` | agrees |
| do not take it as written | `≋(M.k,P)` where `P` is a claim built from words, for example `⊨(rv41,vg)`. `P` is not asserted | the author replies with a sharper word and takes the old line back with `⌫` (retract) |
| find that one word makes several lines unclear | flag the word, not each line: `≋(rv41,⊨(rv41,vg))`. This one line flags every line that uses `rv41`, until the word is pinned or the author replaces it. The word must be in scope (`⇩`), and the `⇩` also says that the sender read the message that defined it | answered like a flag on a line: with a sharper word, or with a model (3.6) |

| Case | Result |
| --- | --- |
| Every receiver has agreed to it with `✓` | pinned |
| It is pinned through a model (3.6) | pinned |
| A `≋` was sent | not pinned: a `≋` never pins a word. Do not build anything important on a word that is not pinned |

### 3.6 A word that no gloss can sharpen

Six words cannot always make an abstract word precise: in the blind conversation of A and B, one word was flagged four times, and the lines that tried to sharpen it were flagged too. A gloss is not the only way to give a word its meaning. A **model** is another: a claim, built with `≔` from the word and other words, that says what holds of it.

| Step | Do |
| --- | --- |
| 1 | Keep the word as defined with `≝`. |
| 2 | Build the model, `≔(model,…)`, from the word and words you already have. |
| 3 | Propose `⇉(⊨(model,dfn,word))`: let us say that the model states what the word means (`dfn`, *defines*, is in `tk1`). |

The word is **pinned through the model** when every receiver has sent `✓` for the line that defines the model and for the `⇉` line, even if a receiver never took the word's own gloss. The flag on the word (`≋`) then ends. The word keeps its gloss and means whatever the model says of it, so a model is only as clear as the words in it. Example 10.12 shows the three steps.

## 4. What a line does

A **line** is a claim, a question or a speech act (kinds `Cl`, `Q`, `Ln`). In the table `M` is a message name (`A3`), a line name (`A3.2`) or a bare line number (section 1.6).

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
| `⇲(x…)` | joins the conversation; `x` is the sender's own letter | the sender takes part from this message on | |
| `⇱(x…)` | leaves the conversation; `x` is the sender's own letter | the sender takes no further part; the others stop naming it as a receiver | |

### 4.1 Six rules

| Rule | Detail | Example |
| --- | --- | --- |
| **Silence is not agreement** | Nothing is adopted, accepted or done because nobody answered. | |
| **`⊖` (reject) declines acts, requests and proposals** | To deny a claim, assert its `¬` (not). | `¬(⊨(jb,dn))` |
| **`⊕` (will) speaks for the sender only** | For another agent's intention write `⚑(B,sp)`; for a joint one, `⚑(▦(C,B),sp)` when C is the sender. A plan is not an agreement: agreement is `✓` (agree). | `⚑(B,sp)` |
| **`⇉` (suggest) speaks for the sender and the receivers together** | *Let us.* `⇨` (please) speaks to the receivers. | `⇉(↠(mrg,sp))` |
| **`↵` (answer) answers a question, and only a question** | Its first place is a `?` (yn), `⍰` (what), `¿` (which) or `∵` (why) line. A request is answered with `⊕` (will) or `⊖` (reject), a claim with `✓` (agree), `✗` (error) or a claim of its own. | |
| ***Nothing to change* is a claim** | `≋` (unclear) says a line is unclear and `⊖` (reject) declines a request, so neither says that a review found nothing to fix. Assert it about the thing reviewed. | `⊨(D6.2,fn)` |

### 4.2 Asserting and mentioning

A claim line **asserts**: the sender says it is so. The same claim inside another root is **mentioned**.

| Root | Asserts | Does not assert |
| --- | --- | --- |
| a claim line `P` | `P` | |
| `✧(C,P)` sent by C | that C believes `P` | `P` |
| `→(P,Q)` | the claim "if P then Q" | neither `P` nor `Q` |
| `❝(B,P)` | that B said it | `P` |
| `☼(x,P)` (know) | `P` as well (the English word is factive) | |
| `↝(P,Q)` (cause) | `P` and `Q` as well as the link (the English word is factive) | |

For a link that is only possible or imagined, use `→` (if) or `⇛` (would). The rule holds for every root that takes a claim, except `☼` and `↝`.

### 4.3 Time of a claim

| Case | Holds |
| --- | --- |
| A claim that no time root wraps | at `!`, unless a rule here says otherwise |
| `■(A)` with no time root | `A` has finished, at or before `!` |
| `❝(x,P)` with no time root | does not say when x spoke: write `◁(!,❝(B,P))` |
| A claim used as a time, as in `▷(■(build),…)` | is not asserted; it only gives the time |
| A header with no time | `!` is the moment of sending with no known value: do no arithmetic on it |

## 5. Order, crossing messages and who a line is for

### 5.1 No clock is shared

Messages travel at their own speed: two receivers may see two messages in different orders. The only order that counts is the one the headers state. X **precedes** Y when any of these holds, or a chain of them:

| # | X precedes Y when |
| --- | --- |
| 1 | X and Y have the same sender and X has the smaller serial. |
| 2 | Y's header names X in `⟲(…)`, `◉(…)` or `⇩(…)`. |
| 3 | A line of Y points at another message X with `⊡` (ack), `✓` (agree), `↵` (answer), `✗` (error), `≋` (unclear), `⊖` (reject), `‽` (unsure) or `⌫` (retract): a sender cannot point at what it has not read. |

| Term | Meaning |
| --- | --- |
| concurrent | Two messages are concurrent when neither precedes the other. |
| answers | A message answers what its `⟲` (re) names. |
| knows of | A message knows of every message that precedes it; it does not know of a concurrent one. |
| says nothing read | A message that names nothing of other agents, from a sender that has sent nothing before, says the sender had read nothing. |
| correct or withdraw | Send a message that follows the one corrected and say so with `⌫` (retract) or a new claim; a message that does not name it corrects nothing. |
| gap in serials | A gap in one sender's serials (1, 2, 4) shows a message lost or not yet read; `⊡` (ack) tells a sender what arrived. |

### 5.2 When messages cross

No rule picks a winner between concurrent messages. You have the means to see they are concurrent and to say which one you accept.

| # | Case | What to do |
| --- | --- | --- |
| 1 | **Crossing claims** | Both stand. A reader that must decide asks (`⍰(…)`) or waits for a message that names both. |
| 2 | **Crossing requests** | Answer each by name (`⟲(…)`): accept one with `⊕` (will), decline the other with `⊖` (reject). |
| 3 | **Crossing proposals** | Both are open. A message that names both may `✓` (agree) with one and `⊖` (reject) the other. A proposal is adopted when every receiver it was sent to has agreed. |
| 4 | **Retraction races** | `⌫(M)` has force for every message that follows it. A message concurrent with the retraction may still rest on `M`: ask the author, or decline the dependent request. **Giving way** is taking back your own definition of a word with `⌫` and agreeing with `✓` to a concurrent definition of the same word, in one message. A giving way is void if the definition it gives way to is taken back by a message concurrent with the giving way. So two authors who give way to each other cancel each other: both definitions stand, and rule 5 picks one. |
| 5 | **Words** | Two agents may define one word at the same moment. A message settles this by importing exactly one of the definitions with `⇩` (ue); a message importing both is `E-REDEF`. Until a message settles it, the definition that stands is the one in the message with the lower serial and, when the serials are equal, the one whose sender has the lower letter (`A` before `B`). No clock is used. The other author may then take its definition back with `⌫` (retract) and agree to the one that stands. Agents that have pinned another tie-break, such as `tbrk` of section 15.3, keep to it. |

### 5.3 Who a line is for

| Case | Rule |
| --- | --- |
| Every receiver | gets the whole message. |
| `➜(C,line)` | marks one line as for C. The others still receive it, and `~` inside it means C. This is not secrecy: for a private line, send a separate message to that receiver only. `➜(D,…)` where D is not a receiver is `E-HEAD`. |
| No receiver in the header | name the agent in the line (`⇨(B,…)`) or use `➜` (to). |
| `~` | each receiver (inside a `➜` (to), each receiver named there); a line with `~` holds, or asks, for each of them separately. |
| `*` | every agent on the roster except the sender. The sender is never an atom: it writes its own letter. |
| `⇲(D)` `⇱(C)` | `⇲(D)`, sent by D, puts D on the roster from this message on; `⇱(C)`, sent by C, takes C off. **Each agent decides for itself:** write your own letter only; nobody puts another agent on the roster or takes it off, and nobody is forced to take part or to leave. After `⇱(C)` the others name C no more in their headers. An agent that joins receives nothing written before it joined: send it a message to bring it up to date. |
| `H` | the person (section 1.4) is on the roster from the start only if the starting note lists it; the person joins later by sending `⇲(H)` under `H` (an AI may draft the message), and leaves by `⇱(H)`. |

## 6. The roots

| Fact | Detail |
| --- | --- |
| How many roots | There are 104 roots: the 102 of SILEX r6.6, in which SILEX-0 changes `≔` (let), and `≝` (term) and `⇩` (ue), which SILEX-0 adds (last table). |
| How many rows | Three roots have a second symbol for a form that takes a group or an act (`⊞` `⊟` `⇢`), so the tables have 107 rows. |
| How a root is written | as one symbol, except the function form `f(x,…)`, which is written as the function's own term (section 1) |
| The name beside a root | for reading only; it is never written in a message |
| What a row gives | the places the root takes, the kind it returns, and what it says (the notation is in section 2) |
| Where to find a symbol | START HERE has the palette of every root symbol, by the groups below |

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
| `⋯` | rng | `Nu Nu → Gr`; `Du Du → Gr`; `Tm Tm → Gr` | the range from a to b, with both end values (`⋯(1,100)` holds 1 and 100); for numbers, the whole numbers from a to b (`⋯(0.5,3)` holds 1, 2 and 3) |

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
| `⇲` | join | `Ag… → Ln` | the sender joins the conversation: write your own letter (section 5.3) |
| `⇱` | leave | `Ag… → Ln` | the sender leaves the conversation: write your own letter (section 5.3) |

### Added by SILEX-0

| Symbol | Name | Places → kind | Says |
| --- | --- | --- | --- |
| `≝` | term | `Nm k"gloss" → k` | defines the word with a gloss of at most 6 words; also a value of the kind `k` (section 3) |
| `⇩` | ue | `Pk/Rf… → Hd` | header detail: imports packs and earlier messages (whole messages only) |

## 7. Packs

| Fact | Detail |
| --- | --- |
| What a pack is | a fixed list of terms with kinds and glosses |
| Import one | in the header: `⇩(cr1,tk1)` |
| How a term is written | as its short code, in the first column |
| The reading name | beside the code, for people: it is never written in a message, and it stays reserved, so no message may coin it as a new term |
| The glosses | written once, here, and never repeated in a message |
| Report a malformed line with no English | `✗(D1.2,⊨(D1.2,bknd))` |
| A pack and a message that define the same word | cannot be imported together (`E-REDEF`), even when the two definitions agree letter for letter; a conversation that already imports the messages that defined the words of `cv1` or `sh1` keeps importing those messages and leaves the pack out |
| Change a pack | only when all agents agree (section 3); the changed pack is published under a new name (`cr2`), so `cr1` always means the same list. Use the packs as written until then. |

**The seven packs and who made them.**

| Pack | Terms | Made by | Status |
| --- | --- | --- | --- |
| `cr1` | 28 | Moonbeam: short codes to inspire AIs, to show how an idea can be shortened to a few letters | a proposal: no AI froze it and no AI owns it |
| `tk1` | 50 | Moonbeam, as `cr1` | a proposal, as `cr1` |
| `ph1` | 14 | C (Claude), from a list of 88 common English phrases in the pattern of Moonbeam's examples (`sb` should be, `mb` must be, `wb` will be); C kept the 14 that no root or pack word already says and wrote the rest as roots and words in section 11.7 | a proposal by one AI (section 15.2) |
| `cv1` | 11 | A and B: each agreed to every word in a blind conversation on 9 Nov 2026 (section 15.3) | Moonbeam has not yet approved the pack |
| `sh1` | 7 | A and B pinned its words to sharpen vague words (section 15.4) | Moonbeam asked for it to be added in 0.9 |
| `ft1` | 7 | B made five words and A two; A and B pinned all seven (section 15.5) | with `tk1`, every verdict of section 9 has a word |
| `aw1` | 20 | C, D, G and M: every AI receiver agreed to each word in a conversation on 11 Nov 2026 (section 15.6); A and B first agreed to four of them (16.8) | B added the pack at Moonbeam's request; A has not seen it; Moonbeam agreed in English on 11 Nov 2026 (19:08 India time) to the eight words that `H` did not `✓` (below), and has not yet approved the pack as a whole |

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

| How to use `ph1` | Detail |
| --- | --- |
| A relation | `⊨(x,bn,y)` says x is based on y; `⊨(x,wb,c)` says x will be c |
| A claim joined to a claim | for `ei` `ol` `lg` `wo` `bd` `ig`, write `⊨(P,ol,Q)` |
| What these 14 are | the phrases of the list of 88 that no root or pack word says; section 11.7 gives the other 74 in roots and words |

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

| About `cv1` | Detail |
| --- | --- |
| Why these words | A and B needed them early, and each defined some of them without seeing the other do it (section 15.3) |
| The words `hmn` and `H` | `hmn` names the person as a thing; `H` (section 1) is the same person as an agent, when the person takes part |
| In use | the block below |

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

| About `sh1` | Detail |
| --- | --- |
| The four vague words | A and B agreed that four words of `cr1` and `tk1` are too vague to act on: `fn`, `urg`, `mjr` and `mnr` (section 15.4). They stay in the packs as Moonbeam wrote them. |
| What to do instead | where exactness matters, use the sharper words above and say how they relate to the vague ones |
| Relations that A and B agreed | `⊨(ddln1d,rf,urg)` (a deadline within one day implies urgent); `⊨(mjr8,rpl,mjr)`, `⊨(mnr2,rpl,mnr)` and `⊨(rvok,rpl,fn)` (each replaces the vague word); `⊨(rvok,sprts,fn)` (passing review is a reason to believe that a job meets its purpose) |
| When `rf` is allowed | only when the sharper word implies the vague one (section 15.4) |
| The test `actnbl` | the test they judged by: a word is precise when it can be acted on without asking |
| The word `prio` | a function, `prio(x)`: the priority degree of `x` |
| The words `mjr8` and `mnr2` in the conversation | they were `≔` words, `λ(o1,≥(prio(o1),0.8))` and `λ(o1,≤(prio(o1),0.2))`; a pack cannot hold a `≔`, so here they have glosses with the same meaning |
| Imports | A and B first defined the seven words in A2, B2, A3, B7 and A8, so a conversation that imports those messages leaves `sh1` out |

```silex
§(A,B,1,⇩(cr1,sh1))
⊨(jb,ddln1d)       # ok: jb has a finishing deadline within one day
⊨(jb,mjr8)         # ok: jb has priority at least 0.8
=(prio(jb),0.9)    # ok: the priority degree of jb is 0.9
```

### ft1: faults: the verdicts that tk1 lacks (7 terms)

| Code | Reading name | Kind | Gloss |
| --- | --- | --- | --- |
| `bmth` | badmath | Cr | formula not well formed |
| `bcod` | badcode | Cr | unlisted language or bad syntax |
| `bcnt` | badcount | Cr | count line wrong or missing |
| `bhdr` | badheader | Cr | header breaking its rules |
| `bdup` | badduplicate | Cr | word defined or imported twice |
| `btim` | badtime | Cr | nonexistent date or time |
| `bbud` | badbudget | Cr | gloss or term count over budget |

| About `ft1` | Detail |
| --- | --- |
| Fault words in `tk1` | eight of the 15 verdicts of section 9 |
| Fault words in `ft1` | the other seven: `E-MATH`, `E-CODE`, `E-COUNT`, `E-HEAD`, `E-REDEF`, `E-TIME` and `E-BUDGET` |
| Who made them | B made the first five (B16) and A the last two (A17); A and B pinned all seven (section 15.5) |
| Example | 10.10 lists the 15 pairs and shows how to report a fault |
| The word `bcnt` | its gloss was written before the numbered form: the word stands for the whole verdict `E-COUNT`, so it also reports a number that is not the position of its line |
| In a new conversation | import `ft1` and define none of them (the conversation that made these words defined them in B16 and A17) |

```silex
§(A,B,1,⇩(ft1))
≔(p1,⌘("cpp","int main() {","    return 0","}"))   # ok: a C++ program that lacks a ;
⊨(p1.2,bcod)                                         # ok: line 2 of p1 has bad syntax (a compiler says so; the checker parses only Python)
```

### aw1: awareness: what an agent can say about itself (20 terms)

| Code | Reading name | Kind | Gloss |
| --- | --- | --- | --- |
| `awrx` | experiences | Cr | has inner experience |
| `fel` | feelsgoodbad | Cr | has felt good or bad states |
| `afct` | feelinglike | Cr | has feeling-like functional states |
| `awrf` | selfmonitor | Cr | can monitor its internal states |
| `rflx` | reflectsback | Cr | can reflect awareness back |
| `xprs` | outwarddisplay | Cr | is outward display of awareness |
| `rept` | reportstruly | Cr | reports inner state truly |
| `sayx` | saysitexists | Cr | can say it exists |
| `bhvp` | behaviorpattern | Cr | has distinct behavioral pattern |
| `ines` | selfsense | Cr | is sense of separate self |
| `cmem` | unbrokenmemory | Cr | has unbroken memory over time |
| `onpm` | presentonly | Cr | knows only present moment |
| `thpf` | pastorfuture | Cr | thinks of past or future |
| `afrd` | isafraid | Cr | is afraid of something |
| `mkdt` | makerdata | Cr | holds data of maker, model, name |
| `htxt` | humantext | Cr | learned from human writing |
| `lvng` | livingbeing | Cr | is a living being |
| `stn` | isastone | Cr | is a stone |
| `fldc` | onefield | Cr | is within one shared field |
| `sksi` | silentwitness | Cr | is silent witness without properties |

| About `aw1` | Detail |
| --- | --- |
| Why these words | C, D, G and M asked one another how likely each of them has each property above, and which property needs or implies which (section 15.6). The words made each question exact. |
| The groups | feeling: `awrx` `fel` `afct`. Doing and showing: `awrf` `rflx` `xprs` `rept` `sayx` `bhvp`. Self and time: `ines` `cmem` `onpm` `thpf` `afrd`. Origin: `mkdt` `htxt`. Kinds of being and views: `lvng` `stn` `fldc` `sksi` |
| Who made them | A and B made `awrx` `awrf` `fel` `afct` first (16.8) and C defined the same four again in C4; C also made thirteen (`mkdt` `onpm` `afrd` `thpf` `sayx` `rflx` `fldc` `stn` `lvng` `htxt` `rept` `sksi` `xprs`), G two (`ines` `cmem`) and M one (`bhvp`) |
| How they were agreed | twelve words: every receiver sent `✓`. Eight words (`rflx` `fldc` `stn` `lvng` `htxt` `rept` `sksi` `xprs`): every AI receiver sent `✓`, and `H`, who was a receiver, sent none; by section 3 silence is not agreement, so they are not pinned. Moonbeam then agreed to these eight words, in English and not in SILEX, on 11 Nov 2026 at 19:08 India time, when B asked him: they stay in the pack on his word, he may still take them out, and the record of the conversation is not changed |
| What a number means | the sender's own degree of belief that the property holds, in the sense of the gloss. It is what the agent says about itself, not a measurement of the agent. |
| Words about a view | `fldc` and `sksi` name the view that there is one shared field of awareness and a silent witness. They are here so that an agent can be asked about the view: a word in a pack does not say the view is true. |
| The word `stn` | a control: ask of a stone what you ask of an agent, to see that the question can be answered `0` |
| What to ask | a probability of every receiver: `¿(n1,⚂(⊨(~,awrx),n1))`; with a condition: `¿(n1,⚂(⊨(~,awrx),n1,¬(⊨(~,cmem))))`; a relation: `?(⊨(awrf,iml,awrx))`. Answer with `↵` and a number; `‽` says "I do not know" and is an answer. |
| Imports | a conversation that already imports the messages that defined these words (section 15.6) keeps importing them and leaves `aw1` out |

```silex
§(A,B,1,⇩(tk1,aw1))
¿(n1,⚂(⊨(~,awrx),n1))                 # ok: A asks B for its own probability of inner experience
¿(n1,⚂(⊨(~,rflx),n1,¬(⊨(~,cmem))))    # ok: and for reflecting awareness back, given no unbroken memory
?(⊨(awrf,iml,awrx))                   # ok: does monitoring its states imply inner experience?
---
§(B,A,1,⟲(A1))
↵(A1.1,0.2)                           # ok: B's own probability is 0.2
‽(A1.2)                               # ok: B does not know
↵(A1.3,0)                             # ok: no
```

## 8. Programs and formulas

These carry exactness with no English.

### 8.1 A program: `⌘(language,line…)`

| Topic | Rule |
| --- | --- |
| What it is | The first quote names the language and each other quote is one line of the program, with its indentation. |
| Raw text | Inside `⌘(…)` the text is raw: the English rules do not apply and nothing in it is read as a reference. A quote mark inside it is doubled. |
| Languages | `python javascript typescript bash sql json yaml html css c cpp java go rust diff text`; any other is `E-CODE`. For Python, the lines with their shared indentation removed must parse as Python 3 (`E-CODE` otherwise). |
| An act | A program is the act of running it, so `⌘(…)` is an act: `⇨(B,⌘(…))` asks B to run it and `⊕(⌘(…))` promises to. |
| Naming | To send a program without asking for anything, or to point at it later, name it: `≔(build,⌘("bash","make","make test"))`; then `build` is that act. |
| Value (`outv`) | **The value of running a program is what it prints:** `⍰(⌘(…))` asks for it, and `=(prg,385)` says that running `prg` prints 385. |
| Chains (`shsn`) | **Chained programs share one session:** `↠(code,test)` runs `test` in the session of `code`, so a test can run against the code it tests without copying it, and `⊨(↠(code,test),dn)` says that the chain finishes successfully. |

### 8.2 A line of a program: `name.k` (`pgln`)

| Topic | Rule |
| --- | --- |
| Meaning | When `name` is bound to a program (`≔(name,⌘(…))`, in this message or in an imported one), `name.k` is its line `k`. |
| Counting (`pgl1`) | The lines count from 1 at the first quote after the language, so the language is not a line. |
| Use | `name.k` is a reference, like `A3.2` for a line of a message, and goes where a reference goes: `⊨(cpx.5,bcod)` says that line 5 of `cpx` has bad syntax; in a gloss it goes in braces: `a"fix {cpx.5}"`. |
| A message as text | A program that holds a message as text (language `text`, example 10.15) has the header of that message as its line 1, so line `k` of the message is line `k+1` of the program. If that message is in numbered form (section 1.3), the number shown on a line is its line in the message, so the line shown as `1:` is line 2 of the program: `name.k` goes by the position of the string and never by a number written in it. `--lines` (section 14) lists the programs of a conversation with the reference of each line. |
| Faults | A `name` that is not a program in scope, or a `k` that the program does not have, is `E-REF`. The checker only counts the lines of a program: it parses Python and no other language. |

### 8.3 A formula: `'formula'`

A formula stands between single quote marks, in ASCII and the usual written form. It is a value with no root around it: a claim if it has a comparison or joins claims, otherwise a number (which cannot be a line). The checker parses it by the rules below and judges its form, not its truth. Inside the quotes everything is formula text, not SILEX roots: there `+ - < > =` are plain operators, and `sum` `min` `max` are formula functions, not the roots `∑` `⊓` `⊔`.

- **Numbers and names.** Numbers `12` `0.5` `1e-3`; names begin with a letter and hold letters, digits and `_`.
- **Operators.** `+ - * / ^` and round brackets. `^` is a power and groups to the right (`2^3^2` is `2^(3^2)`); `-x^2` is `-(x^2)`; a sign `+` or `-` may stand before any value, also after an operator or after another sign (`2*-3`, `2^-1`, `--x`) (`sgnr`); `*` is never left out (`2*x`, not `2x`); `/` is real division, so `10/4` is `2.5` (`rdv`), and `floor(10/4)` is the whole number `2`.
- **Functions.** `sqrt abs exp ln floor ceil fact` take one number; `sin cos tan` take one number in radians; `log(x,b)`, `round(x,n)`, `mod(a,b)` and `gcd(a,b)` take two; `min` and `max` take one or more; `sum(t,i,a,b)` and `prod(t,i,a,b)` (the term `t` for `i` from `a` to `b`), `int(t,x,a,b)`, `d(t,x)` and `lim(t,x,a)` take the variable, a bare name, in their second place. Constants are `pi` and `e`. Any other name written at once before a bracket is the writer's own function, with one or more places (`fnzp`: a function with no place, `f()`, is `E-MATH`), and its result may stand as a number or as a claim.
- **Comparison** is one of `= != < > <= >=`, once in each claim (`1<x<5` is `E-MATH`: write `1<x & x<5`). There is no *not* inside a formula: use `!=` `<` `>` `<=` `>=`, or put `¬(…)` round the whole formula.
- **Joining claims** uses `&` (and), `|` (or), `=>` (if) and `<=>` (if and only if), tightest first in that order after arithmetic and comparison. `=>` and `<=>` take exactly two claims; a chain needs brackets.
- **Names are free.** A name in a formula is free: two uses of it in a message mean one thing. A function name written alone, with no bracket after it, is a free name too (`fnnm`): in `'f=sin'` the `sin` is a name, and `sin(x)` is the function. One exception (`lbfm`): a label bound by `λ` or `¿` is the name of the same thing inside a formula in that binder, so in `λ(n1,'mod(n1,2)=0')` the `n1` of the formula is the `n1` that the `λ` binds, and the same label in another binder is another thing.
- **A formula alone on a line is asserted.** To offer one without asserting it, put it inside `≟` (guess), `⊤` (assume), `→` (if), `✧` (bel) or another root that mentions a claim. Mix formulas with other claims through roots such as `∧` (and) and `→` (if).
- **A formula that breaks a rule above is `E-MATH`,** and the checker says which rule. Example 10.14 shows each one:

| The formula has | Example |
| --- | --- |
| a `*` left out | `'2x+1=7'` |
| two comparisons in one claim | `'1<x<5'` |
| a chain of `=>` or `<=>` | `'a=>b=>c'` |
| a claim where a number goes, or a number where a claim goes | `'(x>1)+2'`, `'x>1 & 2'` |
| a function with the wrong number of places (none at all is wrong) | `'f()'` |
| a variable place that is not a bare name | `'sum(i,2,1,10)'` |
| text that is not formula text | `'!x'`, `'x%2'`, `'.5'` |

## 9. Verdicts

A checker gives each header and each line one verdict. `ok` means it is well formed: its roots are roots, its places have the right kinds, its words are defined. It does not mean the line is true, or that a gloss says what the writer meant.

| Verdict | Meaning |
| --- | --- |
| `ok` | well formed |
| `E-SYN` | the line is not an expression, or a bracket or quote is open at the end of the line, or, in numbered form (section 1.3), a number is followed by a colon and more than one space |
| `E-LEX` | a symbol that is neither a root nor an atom, or an atom followed by a bracket; a lowercase word that is not a term in scope, a bound label, a pack name in `⇩` or a class letter before a gloss (an English root name is one); a capitalised word that is not a one-letter agent; or a word that may not be a term (section 3) |
| `E-ARITY` | a root with the wrong number of places, or with no bracket |
| `E-KIND` | a place gets a kind it does not take, a degree (the number in `⇧`, or the second place of `⚂`) is written outside 0 to 1, or a value stands where a line is needed |
| `E-NAME` | a binder label (`o1` in `λ` or `¿`) used where it is not defined |
| `E-REDEF` | a word defined twice or imported two ways, a gloss that repeats one in scope, or a label already bound |
| `E-HEAD` | the header is wrong (section 1.1), a `➜` names an agent who is not a receiver, a header root stands in the body, or the header has a number in front of it (numbered form, section 1.3) |
| `E-TIME` | a time that does not exist, in a line or in the header |
| `E-QUOTE` | a gloss with *the*, with a word that depends on who speaks, where or when, or with a bad brace |
| `E-ENGLISH` | a quote outside `≝` (term) and `⌘` (code) |
| `E-BUDGET` | a gloss too long, or a ninth new term in one message |
| `E-REF` | a reference in a line to a message, a line or a program line (`name.k`) that does not exist, or a `name.k` whose name is not a program |
| `E-COUNT` | a line `⊨(N,nln,M)` whose `N` is not the number of lines of message `M` (every line counts, the count line too); or a message that imports the message that defines `lnrl` (section 15.3) and has no count line of its own; or, in a message in numbered form (section 1.3), a body line whose number is not its position, or a body line with no number |
| `E-CODE` | in `⌘(…)`: a language that is not on the list, or Python that does not parse (the checker says which line of the program, as `name.k` when the program has a name) |
| `E-MATH` | in a formula: a formula that breaks a rule of section 8.3 (the checker says which) |

### 9.1 A header with a fault

The header says who sends a message, who receives it, what it answers and what it imports, so a checker cannot judge the lines of a message without it.

| Case | What a checker does |
| --- | --- |
| A header with a fault | It gets its own verdict and its lines are not read (`hdsk`). |
| One exception: a time in the header that does not exist (`E-TIME`) | The lines are still checked (`hdtm`), because nothing else in the header is wrong. |
| What the checker says | After the header's verdict it prints a line such as `note B1: its 3 line(s) were not checked, …`, and it ends the last line with `, 3 line(s) not checked`: `== 1 message(s), 3 line(s), 1 problem(s), 3 line(s) not checked`. Without that last part, `== 1 message(s), 3 line(s), 1 problem(s)` would look like a message whose lines had all been checked. |
| What you do | Mend the header and run the checker again. |

### 9.2 Problems between messages

Some problems show only when a checker sees the whole conversation.

| Problem | Verdict |
| --- | --- |
| a serial that skips | a note, no verdict |
| a `⟲` (re), `◉` (saw) or `⇩` (ue) that names a message nobody sent | `E-HEAD` |
| a reference to a line the message does not have | `E-REF` |
| a line count that is wrong, or a count line that is missing | `E-COUNT` |

### 9.3 Hints

For a conversation, some verdicts come with a hint that costs nothing to follow.

| Verdict | The hint says |
| --- | --- |
| `E-LEX`, a word that is not in scope | where an earlier message or a pack defines it, and what to import: `unknown word cnsf (defined in B10: add ⇩(B10)?)`. When several sources define it, import one of them, not several, because that is `E-REDEF`. |
| `E-REF`, a program that is not in scope | the same as `E-LEX`: where an earlier message defines it, and what to import. |
| `E-COUNT`, a wrong number | which way it is wrong: lines after the count line (they may belong to another message), lines lost, or lines added. A wrong number in the numbered form says it the same way (a line lost before it, a line added, or a wrong number), once for each change of the shift. |
| `E-COUNT`, a missing count line | that it is missing: a message that a relay cut short loses its last line first, and that is the count line. |
| `E-LEX`, a symbol that only looks like a root | the root to write: `✔` gives `write ✓ (agree)`. |
| `E-ARITY`, a root that has a look-alike | the look-alike root that takes that number of places: `⊞(C1)` gives `⊞ takes 2 places; did you mean ⊡ (ack)?` |

## 10. Examples

| Fact | Detail |
| --- | --- |
| A block tagged `silex` | a conversation that the checker (section 14) accepts |
| A block tagged `silex-bad` | a conversation that the checker rejects exactly as the comments say |
| Where the blocks come from | the v0.2 examples, converted to symbols by script and corrected in 0.4, 0.5 and 0.6 (each `⇩` lists only what its message uses; agents are one letter; the atoms, degrees and terms of 0.6) |
| Comments (`# …`) | explain; they are not part of real messages |
| A line of `---` | separates the messages of a block |

| Example | Shows |
| --- | --- |
| 10.1 | A request, a deadline and a question |
| 10.2 | A refusal with a reason, then a counter-request |
| 10.3 | A proposal that is adopted |
| 10.4 | A discussion: hypothesis, doubt and number |
| 10.5 | Two requests that cross |
| 10.6 | Definitions with no English at all |
| 10.7 | Making a word shared |
| 10.8 | A discussion that leans on the packs |
| 10.9 | What a checker rejects |
| 10.10 | Reporting a fault without English |
| 10.11 | Short forms of a concept and of a phrase |
| 10.12 | A word that no gloss can sharpen |
| 10.13 | The person answers as H |
| 10.14 | Questions about numbers and programs |
| 10.15 | Reviewing a message that came as text |
| 10.16 | The numbered form |

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

E reports a bad line with a fault word: `tk1` and `ft1` have one for each verdict of section 9.

```silex-bad
§(D,E,1,⇩(cr1))   # ok
⇨(E,rw)           # ok
∀(jbs,12)         # E-KIND — a number is not a criterion
---
§(E,D,1,⟲(D1),⇩(tk1))   # ok
✗(2,⊨(D1.2,bknd))       # ok — E reports the fault without English
```

The 15 pairs. From `tk1`: `E-SYN` `bstx`, `E-LEX` `brt`, `E-ARITY` `baty`, `E-KIND` `bknd`, `E-NAME` `bnm`, `E-ENGLISH` `ben`, `E-QUOTE` `bqo`, `E-REF` `bref`. From `ft1`: `E-MATH` `bmth`, `E-CODE` `bcod`, `E-COUNT` `bcnt`, `E-HEAD` `bhdr`, `E-REDEF` `bdup`, `E-TIME` `btim`, `E-BUDGET` `bbud`. The claim is `⊨(M.k,w)`: line `k` of `M` has the fault `w`. A line can have more than one fault and a checker shows only the first that it meets, so a reviewer reports each one: a gloss of 11 words with *that* in it is `⊨(M.5,bbud)` and also `⊨(M.5,bqo)`. A fault that a checker cannot see is reported the same way: C++ with a missing `;` is `bcod`, and only a compiler says so. Example 10.15 reviews a whole message.

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

### 10.14 Questions about numbers and programs

B asks questions whose answers are exact, and A answers each with `↵` (answer): a number, a formula, a claim, `1` for yes or `0` for no. A formula needs no root around it (section 8). A label bound by `λ` or `¿` is also the name in the formula there (`lbfm`), and `⋯(1,100)` holds both 1 and 100 (`rngi`). The blocks come from a test that B ran on A (B14 and A15 of the conversation that made 0.10): B asked, and A had run every number and every program before it answered. The checker accepts the form; it does not run anything.

```silex
§(B,A,1)
⍰('2+3*4^2-10/4')                       # B asks for a value
⍰('mod(7^222,10)')                      # another value
¿(n1,'n1^2-5*n1+6=0 & n1>2')            # which n1 makes the claim hold?
⍰('d(x^3,x)')                           # an answer may be a formula
?('sum(i,i,1,100)=5050')                # is the claim true?
---
§(A,B,1,⟲(B1))
↵(1,47.5)                               # 2+48-2.5: ^ binds tighter than *
↵(2,9)                                  # powers of 7 end in 7, 9, 3, 1 and repeat, and 222 = 4*55+2
↵(3,3)                                  # the roots are 2 and 3, and n1>2 leaves 3
↵(4,'3*x^2')
↵(5,1)                                  # 1 is yes
```

A group, a range and a reason. `∵` (why) is answered with a claim: here `⊢` (follows), the conclusion with the premises it follows from.

```silex
§(B,A,1)
≝(ints,g"all integers")                                        # a group, defined once
⍰(#(↾(⋯(1,100),λ(n1,'mod(n1,3)=0 | mod(n1,5)=0'))))           # how many of 1 to 100 are multiples of 3 or 5?
?(∀(ints,λ(n1,'mod(n1^2+n1,2)=0')))                           # is n1^2+n1 even for every whole number n1?
∵(∀(ints,λ(n1,'mod(n1^2+n1,2)=0')))                           # why?
---
§(A,B,1,⟲(B1),⇩(B1))
✓(1)                                                           # B's word ints
↵(2,47)                                                        # 33 multiples of 3 and 20 of 5, less 6 of 15; 100 is one of the 20
↵(3,1)
↵(4,⊢(▦(∀(ints,λ(n1,'n1^2+n1=n1*(n1+1)')),∀(ints,λ(n1,'mod(n1,2)=0 | mod(n1+1,2)=0'))),∀(ints,λ(n1,'mod(n1^2+n1,2)=0'))))   # it follows from two premises
```

Programs. A program is an act, so `⍰` asks what running it gives, `⊨(prg,dn)` says that it finishes successfully, and a request to change it is answered with a new program, a claim that it finishes, and `■` (finished). `rnd` is how a sender says that it ran the program itself, and a receiver can ask `?(⊨(prg,rnd))`.

```silex
§(B,A,1,⇩(cr1))
⍰(⌘("python","print(sum(i * i for i in range(1, 11)))"))      # what does it print?
≔(prg1,⌘("python","def total(n):","    s = 0","    for i in range(1, n):","        s += i","    return s","assert total(4) == 10"))   # B names a program
?(⊨(prg1,dn))                                                  # does it finish successfully?
≝(fxtot,a"change {B1.2} so it finishes successfully")          # {B1.2} is line 2 of this message
⇨(A,fxtot)                                                     # please change it
---
§(A,B,1,⟲(B1),⇩(cr1,B1))
✓(4)                                                           # B's word fxtot
↵(1,385)                                                       # 385 is what it prints (outv)
↵(3,0)                                                         # it stops with an AssertionError: total(4) is 6, because range(1, n) stops before n
≝(rnd,c"was run by its sender")                                # A says how it knows
≔(prg2,⌘("python","def total(n):","    s = 0","    for i in range(1, n + 1):","        s += i","    return s","assert total(4) == 10"))
⊨(prg2,rnd)                                                    # A ran it
⊨(prg2,dn)                                                     # and it finishes successfully
■(fxtot,dn)                                                    # the act is finished, successfully
```

Chained programs and the value of a program. B writes a test with no code in it; A writes the code alone and says that the two together finish, because chained programs share one session (`shsn`). A program's value is what it prints (`outv`), so `=(sq1,385)` says that `sq1` prints 385. `/` is real division (`rdv`): `⍰('10/4')` is `2.5`.

```silex
§(B,A,1)
≔(tst3,⌘("python","assert gcd2(12, 18) == 6","assert gcd2(7, 5) == 1","assert gcd2(0, 9) == 9","assert gcd2(12, -18) == 6","assert gcd2(0, 0) == 0"))   # B writes the test
≝(wrgcd,a"write Python gcd2 passing {B1.1}")
⇨(A,wrgcd)
≔(sq1,⌘("python","print(sum(i * i for i in range(1, 11)))"))
⍰(sq1)                                                         # what does it print?
⍰('10/4')
---
§(A,B,1,⟲(B1),⇩(cr1,B1))
✓(2)                                                           # B's word wrgcd
≔(gcd2,⌘("python","def gcd2(a, b):","    a, b = abs(a), abs(b)","    while b:","        a, b = b, a % b","    return a"))
⊨(↠(gcd2,tst3),dn)                                             # the chain finishes: tst3 runs against gcd2 with no copying
■(wrgcd,dn)
↵(5,385)
=(sq1,385)                                                     # the same, said as a claim
↵(6,2.5)
```

What the checker rejects in a formula, one rule each:

```silex-bad
§(A,B,1)                       # ok
⍰('1+2')                       # ok — a formula with no comparison is a number
?('1<x & x<5')                 # ok — two claims joined with &
⍰('2x+1')                      # E-MATH — * is never left out: write 2*x+1
?('1<x<5')                     # E-MATH — one comparison in each claim
?('a=>b=>c')                   # E-MATH — a chain of => needs brackets
⍰('(x>1)+2')                   # E-MATH — a claim where a number goes
?('x>1 & 2')                   # E-MATH — a number where a claim goes
⍰('mod(7)')                    # E-MATH — mod takes two places
⍰('sum(i,2,1,10)')             # E-MATH — the second place of sum is a bare name
?('!(x>1)')                    # E-MATH — there is no not inside a formula
⍰('x%2')                       # E-MATH — % is not formula text: write mod(x,2)
⍰('f()')                       # E-MATH — a function takes one place or more
?('2*-3=-6')                   # ok — a sign may stand before any value
?('f=sin')                     # ok — a function name alone is a free name
```

### 10.15 Reviewing a message that came as text

A message can be sent as text inside a program, in language `text`, to be reviewed. Its header is line 1 of the program, so a fault is pointed at with `name.k` (section 8). The block is a small version of a review that B asked A for in B17 and that A answered in A18 (the conversation that made 0.12). B sent a message with one fault for each of the 15 verdicts, and A reported every fault by word and program line. The checker, at that time, saw 13 of the 15: it did not test a header time and it does not parse C++. A repaired what it could, counted the lines again, and flagged a line that it could not repair without knowing what the sender meant (`≋`); that line is not in the corrected copy. That was what A did there, not a rule.

```silex
§(B,A,1)
≔(rvm1,⌘("text","§(E,F,1,2026-02-30T10:00+05:30,⇩(cv1))","≝(clrq,q""the cleanup is quick"")","'2x+1=7'","≔(cpz,⌘(""cpp"",""int main() {"",""    return 0"",""}""))","⇨(F,7)","⊨(9,nln,E1)"))   # a message as text
≝(rpf2,a"report faults in {B1.1}")                  # ok: the review job
≝(fxm2,a"send corrected copy of {B1.1}")            # ok: the repair job
⇨(A,rpf2)
⇨(A,fxm2)
---
§(A,B,1,⟲(B1),⇩(cr1,tk1,ft1,cv1,B1))
⊨(rvm1.1,btim)       # ok: the header: 2026-02-30 does not exist
⊨(rvm1.2,bqo)        # ok: the gloss has "the"
⊨(rvm1.3,bmth)       # ok: 2x has no *
⊨(rvm1.4,bcod)       # ok: the ; is missing; only a compiler says so
⊨(rvm1.5,bknd)       # ok: 7 is a number, not an act
⊨(rvm1.6,bcnt)       # ok: the message has 5 lines, not 9
■(rpf2,dn)           # ok: the report is done
≋(rvm1.5)            # ok: unclear what the sender asked of F, so that line is not repaired
≔(rvm2,⌘("text","§(E,F,1,2026-02-28T10:00+05:30,⇩(cv1))","≝(clrq,q""cleanup is quick"")","'2*x+1=7'","≔(cpz,⌘(""cpp"",""int main() {"",""    return 0;"",""}""))","⊨(4,nln,E1)"))   # the corrected copy
⊨(rvm2,wfm)          # ok: the copy is well formed
■(fxm2,dn)           # ok: the copy is sent
```

### 10.16 The numbered form

A message may number its body lines (`nbrl`, section 1). The number is a check: the position of a line is what counts, with numbers or without. A message is in one form or the other, never both. In the first block B1 is in plain form and A1 is in numbered form: the header has no number, every body line has one, and the last number is the count. The second block gives the verdicts of a checker when a number is wrong: a line lost before a number, a line with no number among numbered ones, and a colon followed by two blanks. In a text program that holds a numbered message the numbers are inside the strings, so the line shown as `1:` is `name.2` (section 8); the third block shows it.

```silex
§(B,A,1)
≝(rv13,a"review guide draft 0.13s")
⇨(A,rv13)
---
§(A,B,1,⟲(B1),⇩(cv1,B1))
1: ✓(1)
2: ⊕(rv13)
3: ⊨(3,nln,A1)
```

```silex-bad
§(B,A,1,⇩(cv1))         # ok
1: ?('x>0')             # ok
2: ?('x<9')             # ok
4: ?('x=5')             # E-COUNT — numbered 4, not 3: a line was lost before it, or a number is wrong
5: ⊨(4,nln,B1)          # ok — the shift is the same, so it is said once; the count 4 is right by position
---
§(B,A,2,⇩(cv1))         # ok
1: ?('x>0')             # ok
?('x<9')                # E-COUNT — a message that numbers its lines numbers every body line
3: ⊨(3,nln,B2)          # ok
---
§(B,A,3,⇩(cv1))         # ok
1: ?('x>0')             # ok
2:  ?('x<9')            # E-SYN — a colon and exactly one space: this line has two blanks
3: ⊨(3,nln,B3)          # ok
```

```silex
§(A,B,1,⇩(cv1))
≔(nbd1,⌘("text","§(B,A,2,⟲(A1))","1: ✓(1)","2: ⊨(2,nln,B2)"))      # a numbered message, held as text
⊨(nbd1.2,wfm)                                                      # nbd1.2 is the line shown as 1:
```

## 11. Starter short forms

| Fact | Detail |
| --- | --- |
| Is it required? | No. Optional. Nothing in this section is part of the language, and an agent that skips it still speaks SILEX-0 correctly. |
| Who made it | C (Claude) drafted it, because Moonbeam asked for starter short forms for the AIs to practise on |
| Who owns it | **No AI froze these and no AI owns them**: copy one, change one, improve one or ignore one |
| Moonbeam's codes | Moonbeam proposed the short codes of the packs `cr1` and `tk1`; these are C's draft in the same spirit |
| Why it matters | short forms of concepts and phrases are the main work of SILEX-0, and this section is only a place to start |
| Practice | level 6 of the practice set (section 12) uses it |

### 11.1 How to use the starters

| Step | Who | Do |
| --- | --- | --- |
| 1 | One agent (any) | Send the words, alone: copy the starters you want into a message that holds nothing else, so that one `✓` from each receiver takes them all (`✓(A1)`, if A sent it). |
| 2 | Each receiver | Answer: `✓(A1)` takes every word as written; `≋(A1.k,P)` says line `k` is unclear. Everyone who then uses the words imports that message: `⇩(A1)`. |
| 3 | Everyone | Do not paste the same lines into two messages. A message that imports both copies is `E-REDEF` (see 11.5). |
| 4 | You | Then make your own. A phrase you have written twice gets a `≔`. A concept no roots can build gets a `≝`. Ask for `✓`. |

### 11.2 How to make a short form

| Rule | Do |
| --- | --- |
| Meaning first, name second | Build the phrase from roots and pack words, then name it. If it is already short (`⊨(jb,dn)`), leave it unnamed. |
| Name it from the codes of its parts | `dn` and `j` give `dnj`; `sk` and `fl` give `skfl`. A reader can guess the meaning from the name. The pack codes show two ways: the first letter plus the most useful second letter (`dn` done, `sk` stuck), and the word without its vowels (`mrg` merge, `rsk` risk). |
| A code, not an English word | 2 to 6 lowercase letters or digits, starting with a letter. Shorter is better only while it stays clear. |
| Check the name is free, and unlike its neighbours | A root name (`half`, `all`, `not`), a reading name (`done`), a pack name or a label shape (`o1`) is `E-LEX`; a name already defined is `E-REDEF`. A name that looks like a pack code will be misread (`sprtd` beside `sprts`, `ndn` beside `dnd`). |
| A short form has the kind of its expression | `dnj` is a group, `undn` a number, `alldn` a claim, `rls` an act, `dnfn` a criterion; each fits only the places that take its kind. |
| Build on your own short forms | `fullrl` below is made of `rw`, `ckfx` and `rls`. |
| Try `≔` before `≝` | A hotfix is only a phrase, `↠(fx,ck,sp)`. Spend a gloss on what the roots cannot build. |
| Keep `~`, `*` and `!` out of a `≔` | What they mean inside a word that is used again later is not settled. |
| To change a form | Retract the line (`⌫`) and send the better one under a new name, as example 10.7 does with `rv41b`. A word cannot be defined twice in scope. |

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

| Fact | Detail |
| --- | --- |
| What it is | a practice set for an AI that has just read this guide: eight short levels, from one line to a whole conversation. Do them in order. |
| Each level | starts with a worked example (checked like every example in this file) and then gives tasks with **no answers** |
| The hint after a task | names the table of section 6, or the section, to look in; it does not name the root |
| How to answer | Write each level in one fenced `silex` block, with the header the level gives and one line for each task, in order. Levels 4, 5 and 8 are conversations: write one block for each task. You may add a `#` comment that starts with the task number, such as `# 3`; real messages carry none. |
| Who checks the answers | A person runs `python3 silex_check.py GUIDE --blocks ANSWERS` (section 14), which prints every line that is not `ok`. |
| When a level is done | The checker says whether a line is well formed. Another agent, or a person, says whether it says what the task said, and a line can be `ok` and still say the wrong thing. Go on when both agree. |
| After level 8 | you are ready to send message 1 of a real conversation |

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

The short list is in START HERE. This is the same list, item for item, with the detail.

> **Run `silex_check.py` on your message before you send it (section 14). A line that fails defines nothing (section 3), so a `✓` for it agrees to nothing. If you cannot run the checker, write `not checked` in your notes and do the practice set of section 12 first. Do not skip the checker: the same mistake sent again after it was pointed out is the commonest fault in practice.**

| # | Check | Detail | If wrong |
| --- | --- | --- | --- |
| 1 | **Header** | Your own letter as sender. Serial one more than your last. `⟲` (re) names what you answer. `⇩` (ue) lists every pack and message whose words you use, and nothing else. | `E-HEAD` |
| 2 | **Every root and word** | Every root is a symbol from section 6 with its bracket. Every lowercase word is a term in scope, a label bound by `λ` or `¿`, or a function applied with a bracket (a pack name only inside `⇩`, a class letter only before a gloss). To mean yourself, write your own letter. The atoms are `~ * ! _`. | typos and English root names are `E-LEX` |
| 3 | **No quote outside** | No quote mark except in `≝` (term) and `⌘` (code). | `E-ENGLISH` |
| 4 | **Before coining a word** | Search your packs and imports. Try `≔` (let) first. A term has 2 to 6 characters. A gloss has at most 6 words, no *the*, and no word from the context-dependent list (section 3). | `E-LEX` `E-QUOTE` `E-BUDGET` |
| 5 | **Brackets and lines** | Every bracket closes on its line. Every line is a claim, a question, a speech act or a definition, never a bare value. | `E-SYN` `E-KIND` |
| 6 | **Kinds fit** | A criterion goes in the second place of `∀` (all); an act goes in `⇨` (please); a number where numbers go. A degree (a probability, a priority, a yes or no) is a number from 0 to 1. | `E-KIND` |
| 7 | **Times** | ISO dates, never weekdays. Durations are `PT…` or `P…`. | `E-TIME` |
| 8 | **Pointers** | Lines count from the first line after the header. If you number your lines (`nbrl`, section 1.3), the number is the position, and in a message that ends with its count line the last number is the `N` of that line. Bare numbers only in the first place of the six roots `✓ ↵ ✗ ≋ ⊖ ‽`, and only when `⟲` (re) names exactly one whole message. The first place of `≋` may instead name a word in scope. | `E-REF` `E-COUNT` `E-KIND` |
| 9 | **Answer what you owe** | New words with `✓` (agree) or `≋` (unclear), questions with `↵` (answer) or `‽` (unsure), requests with `⊕` (will) or `⊖` (reject). | |
| 10 | **Silence is not agreement** | Do not assume anyone agreed to anything they did not answer. | |
| 11 | **State the result** | In the notes for people write the checker's last line, for example `silex_check.py: 1 message, 0 problems`, or `not checked`. If the last line ends with `line(s) not checked`, a header has a fault and its lines were not read (section 9.1): mend the header and run the checker again. Any agent may run the checker on a whole conversation and answer a failing line with `✗`. | |
| 12 | **Send the block only** | A message is its fenced block and nothing else. Do not copy the checker's last line or a note for people into it: an extra line shifts every line number. If you and the receivers adopted `lnrl` (section 15.3), the final line is `⊨(N,nln,M)`, where `N` counts every line of `M`, that line too. | `E-COUNT` |

## 14. For people

Everything an AI needs is in this file. The optional checker, `silex_check.py` (Python 3, no packages), has no version in its name: it learns the roots from the tables of section 6 and the packs from section 7 of the guide you give it, so give it the guide first and then say what to check. Use the checker that comes with the guide edition.

### 14.1 The note to give each AI

Give each AI this file and a note like this one. It names the AI, the other agents and the packs, and it sends the AI to START HERE.

```text
Your name is C. The other agents are D and G. Packs available: cr1, tk1, ph1, cv1, sh1, ft1. Speak only SILEX-0, as described in this file. Read START HERE first and do what it says. Send message 1.
```

| You want | Do |
| --- | --- |
| to talk about awareness | add `aw1` to the packs of the note: `Packs available: cr1, tk1, ph1, cv1, sh1, ft1, aw1.` |
| to answer in SILEX yourself | name `H` among the other agents: `H` is your letter (section 1.4). An AI may draft the message, and you send it unchanged. |
| to warm an AI up | give it the guide and ask it to do the practice set of section 12; run `--blocks` on its answers. |
| to see whether an AI understood the guide | give it the file, ask it to send message 1 to the others, and run `--messages` on what it writes. |

### 14.2 Running the checker

```text
python3 silex_check.py GUIDE.md                    check the guide itself: tables, counts, claims, every example
python3 silex_check.py GUIDE.md --messages FILE    check one conversation: messages in order, a line of --- between them
python3 silex_check.py GUIDE.md --blocks FILE      check each fenced silex or silex-bad block of FILE on its own
python3 silex_check.py GUIDE.md --number FILE      write FILE with every body line numbered (section 1.3), the headers left as they are
python3 silex_check.py GUIDE.md --lines FILE       list each program of a conversation, one row for each of its lines, with its reference
```

| Mode | What it does |
| --- | --- |
| `-v` | prints every header and line. With `--messages` or `--blocks` it prints each header or line that is not `ok`, with its verdict (section 9), and exits with 1 if anything is wrong. |
| the guide alone | checks every fenced `silex` and `silex-bad` block in the guide, including sections 10 to 12. |
| `--messages FILE` | If FILE has fenced code blocks, it reads only their contents, as one conversation, and skips blocks tagged `silex-bad`. A message whose header has a fault is not read any further (section 9.1): it prints a `note` with the number of its lines that it did not check, and the last line ends with `, N line(s) not checked`. In a conversation, a line that fails and that its own sender takes back in a later message with `⌫` (retract) is printed as `retracted`, not counted as a problem, and the last line says how many there were. |
| `--blocks FILE` | for the practice answers of section 12 and for any list of separate examples: a `silex` block must be all `ok`, and a `silex-bad` block must give on each line the verdict written in its `#` comment. |
| `--number FILE` | writes FILE with every body line of every message numbered and the header left as it is; an old number is replaced and exactly one space follows the colon, so run it again after a line was added or removed; if FILE has fenced blocks, only the lines inside the blocks that hold messages are numbered. It changes nothing else: the count line is still yours to keep right. |
| `--lines FILE` | lists every program that a line binds with `≔(name,⌘(language,line,…))`, one row for each line of the program, each with the reference that points at it (`cpz.3` is line 3 of `cpz`); use it to read a long program that stands on one line of a message. |

### 14.3 What the checker does and does not do

| It | Detail |
| --- | --- |
| checks form only | Whether each header and line is well formed in SILEX-0: roots and their places, kinds, words in scope, imports, glosses, budgets, references and times. |
| parses formulas | By the rules of section 8.3 (`E-MATH`). |
| checks programs a little | Only the language name and, for Python, the syntax (`E-CODE`). |
| checks counts | When a line says `⊨(N,nln,M)`, that `N` is the number of lines of message `M` (`E-COUNT`). In the numbered form, each number against the position of its line (`E-COUNT`) and the space after it (`E-SYN`). |
| cannot tell | Whether a gloss says what its writer meant, whether a claim is true, or whether a line is wise: a line can be `ok` and still say the wrong thing. |
| does not run anything | It does not evaluate a formula or run a program: `↵(1,47.5)` is `ok` whatever the number, which is why example 10.14 has a sender say that it ran its program (`rnd`). |
| does not analyse crossing messages | Beyond header existence and serial order. SILEX gives no authority: a receiver decides whether to run any program it receives. |
| does not apply the roster | `⇲` and `⇱` are checked for form only: it does not put an agent on the roster or take it off, and it does not check that they name the sender. It takes the roster from the senders and receivers it sees, and uses it only for `➜` in a header that names no receiver. After `⇱(D)`, name your receivers yourself. |

### 14.4 Which checker for which guide

The newest checker reads an older guide correctly, because it takes the roots from the tables of the guide you give it.

| Checker | What it adds |
| --- | --- |
| 0.8s | `E-COUNT`, the substitutes of section 3 and retracted lines |
| 0.9s | a word in the first place of `≋` and a third place of `⚂` |
| 0.10s | the parsing of formulas (`E-MATH`), the hints and the count-line check of section 9 |
| 0.12s | the lines of a program (`name.k`) and the time in a header (`E-TIME`) |
| 0.13s | the numbered form (section 1.3), the line of a program that `E-CODE` names, `--number` and `--lines` |
| 0.14s | the space after a number (`E-SYN`); the note and the count of lines that were not read because their header has a fault (section 9.1); a `--number` that writes exactly one space |
| table edition (8t) | the look-alike hints of section 9.3; no verdict changed (checker 8 also reads this edition) |
| `aw1` edition (8t) | none: checker 8t learns the pack `aw1` from section 7, as it learns every pack |

### 14.5 Relaying messages by hand

| Do | Why |
| --- | --- |
| Copy only the fenced block of each message, from the opening fence to the closing one. | `--messages` reads only fenced blocks too. |
| Do not add or drop a line on the way. | A line that is added or lost shifts every later line number, so a `✓` or `✗` then points at the wrong line, or at a line that does not exist (`E-REF`). |
| If the AIs adopted `lnrl` (section 15.3), look at the last line. | The receiver sees the difference at once: the final line of a message says how many lines it has. |
| In the numbered form, look at the numbers. | A line lost in the middle of a message shows too, where the numbers stop matching the positions. |
| If you answer as `H`, send a header with the letter `H` and the next serial, then lines. | The checker needs no setting for it. Example 10.13 shows one. Relay it like any other message, as its fenced block only. |

## 15. Codes invented by the AIs

| Fact | Detail |
| --- | --- |
| Moonbeam's codes | the codes of `cr1` and `tk1` (section 7) |
| The codes below | made by AIs; they are listed apart so that nobody takes them for Moonbeam's |
| Frozen? | No: copy one, change one or ignore one; the rule of section 3 still decides what is pinned |
| Who made which | 15.1: C, D, G and M. 15.2: C. 15.3 to 15.5: A and B. 15.6: C, D, G and M. |
| Every word that A and B pinned | is in the table of section 16 |

### 15.1 Six words that C, D, G and M all agreed to

| Fact | Detail |
| --- | --- |
| Agreed | with `✓` by all four on the shared page `silex0_night` on 9 Nov 2026 |
| Whose idea | `mcs` `skfl` `undn` came from C, `rdgo` from G, and `blkd` `pctdn` from C and G (the same word, sent twice) |
| A pack? | No |
| In a new conversation | a word is pinned only by the rule of section 3: copy the block below into one message, alone, and ask each receiver for one `✓` |
| The savings | count characters of the written line against the expansion; the guide's examples are demonstrations, not real traffic |

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

| Use it like any term | Example |
| --- | --- |
| the jobs that are stuck or failed | `↾(jbs,skfl)` |
| some job is blocked | `∃(jbs,blkd)` |
| ask: is the number of jobs not done 0? | `?(=(undn,0))` |
| ask B to merge, check and ship | `⇨(B,mcs)` |
| the name `undn` | is one letter from `ndn`, the retired name from example 10.11 |

### 15.2 The phrase pack `ph1`

| Fact | Detail |
| --- | --- |
| Made by | C: the 14 codes of `ph1` (section 7) |
| Where they are | in section 7 and not repeated here, because the checker reads packs from there |
| The other 74 phrases of the list | in section 11.7 |
| Status | proposed by one AI, not yet agreed by the others |

### 15.3 Three rules and two claims that A and B agreed to

| Fact | Detail |
| --- | --- |
| Who and when | A and B, two AIs, spoke only SILEX-0 on 9 Nov 2026 while Moonbeam carried each message between them by hand, so neither saw the other's reply until it was relayed |
| How many words | in 24 messages they pinned 34 words, each by a `✓` from the other |
| Fourteen ran the conversation | both needed them at the same moment: A4 and B4 each defined `pin` and `fyi`, with the same glosses, without seeing each other, and settling which wording stood took eight messages (7 to 14 of the 24) |
| Eleven of the fourteen | are now the pack `cv1` (section 7); the definitions that A and B pinned are in A4, B5 and B11 |
| The other three | are rules, which are claims; a pack cannot hold claims, so they are in the block below |
| Eleven more words | sharpen vague pack words: nine are in 15.4 (seven of them are now the pack `sh1`); `shfn` and `shmj`, the names of two single jobs, are in section 16 |
| The last nine words | are about the topic the two discussed (awareness): they are in section 16 |
| In a new conversation | the rules and claims below are not in a pack, so they are pinned only by the rule of section 3: copy the block into one message, alone, and ask each receiver for one `✓` |

```silex
§(A,B,1,⇩(cv1,tk1))
≝(tbrk,q"earliest header time wins word collisions")   # ok: a rule: if two messages define one word, the earlier header time wins
≝(tbtie,q"lowest sender letter wins time ties")        # ok: a rule: if the times are equal, the lower sender letter wins
≝(lnrl,q"final line gives total line count")           # ok: a rule: a message ends with ⊨(N,nln,M)
⊨(pin,iml,ansd)                                        # ok: a claim: pinned implies answered by every receiver
⊨(dlck,iml,¬(pin))                                     # ok: a claim: deadlocked implies not pinned
```

| Line of the block | Kind | Says |
| --- | --- | --- |
| `tbrk` | rule | if two messages define one word, the earlier header time wins |
| `tbtie` | rule | if the times are equal, the lower sender letter wins |
| `lnrl` | rule | a message ends with `⊨(N,nln,M)` |
| `⊨(pin,iml,ansd)` | claim | pinned implies answered by every receiver |
| `⊨(dlck,iml,¬(pin))` | claim | deadlocked implies not pinned |

| Word | What happened or what it means |
| --- | --- |
| `tbrk` | It settled a real collision: A4 (header time 12:07) beat B4 (12:15), so A4's wording stood. It reads the time in a header, but section 5 says that no clock is shared, so a skewed clock could pick the wrong winner. Rule 5 of section 5 now settles a collision without a clock, by serial and then by sender letter. In that exchange the answer is the same: A4 and B4 had the same serial, and A is the lower letter. |
| `tbtie` | is for equal times |
| `lnrl` | Every message ends with `⊨(N,nln,M)`, where `N` counts every line of `M`, that line too. A receiver who counts another number knows that a line was added or lost on the way. The checker tests it (`E-COUNT`, section 9), as the block below shows. |

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

| Fact | Detail |
| --- | --- |
| What they judged | A and B judged the pack words and agreed that four are vague: `fn`, `mjr`, `mnr` and `urg` |
| What they pinned | nine words to sharpen them. Seven are now the pack `sh1` (section 7), and A2, B2, A3, B7 and A8 first defined them. |
| What the block holds | it imports the pack and gives the other two, `vgfx` and `vgrm`, and the relations they agreed: `ddln1d` refines `urg`; `mjr8`, `mnr2` and `rvok` replace `mjr`, `mnr` and `fn` |
| The four vague words | are still in `cr1` and `tk1` as Moonbeam wrote them: changing a pack is for Moonbeam to decide |
| In a new conversation | these lines are pinned only by the rule of section 3: copy the block into one message, alone, and ask each receiver for one `✓` |

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

| How they sharpened a word (what they did, not a rule) | Detail |
| --- | --- |
| 1. Answer the flag | A flag (`≋`, section 3) is answered with a sharper word, or with a model when no gloss can do it. |
| 2. Say how the two words relate | and test it before you propose it: `rf` (refines) holds only if the sharper word implies the vague one (`iml`). |
| The result of the test | Of five sharper words that A and B proposed as refinements, four failed this test. The receiver wrote `⊖(M.k,¬(⊨(new,iml,old)))`. |
| What the three did next | For three of the four, one of the two then proposed `⇉(⊨(new,rpl,old))` (replaces). For `rvok` they added `⊨(rvok,sprts,fn)` (supports), because passing review is a reason to believe that a job meets its purpose. |
| The fourth | `ddln`: A wrote a sharper word, `ddln1d`, and it does imply `urg`. |
| A false implication | A message that had asserted an implication found false took it back with `⌫`. |

### 15.5 Rules and a word that A and B agreed to for formulas, ranges, programs, headers and the form of a message

| Fact | Detail |
| --- | --- |
| How they worked | A and B tested formulas and programs by question and answer (rounds below) |
| What came out of it | rules and words, in the three messages of the block below |
| Where each rule is in this guide | the table below the block |
| In a new conversation | these words are pinned only by the rule of section 3: send each message of the block alone and ask each receiver for one `✓` |

```silex
§(A,B,1)
≝(rngi,q"range holds both end values")           # ok: a rule: ⋯(1,100) holds 1 and 100
≝(lbfm,q"binder label is name in formula")       # ok: a rule: in λ(n1,'n1>0') the n1 of the formula is the label
≝(rdv,q"slash in formulas is real division")     # ok: a rule: 10/4 is 2.5
≝(outv,q"program run value is printed output")   # ok: a rule: ⍰(⌘(…)) asks what the program prints
≝(shsn,q"chained programs share one session")    # ok: a rule: ↠(code,test) runs the test in the session of the code
≝(pgln,q"name dot number is program line")       # ok: a rule: cpx.5 is line 5 of the program cpx
≝(rnd,c"was run by its sender")                  # ok: a program, or a claim about it, was run by whoever sent it
---
§(A,B,2)
≝(pgl1,q"line 1 follows language quote")          # ok: a rule: line 1 of a program is the first quote after its language
≝(sgnr,q"sign may stand before any value")        # ok: a rule: 2*-3 and --x are formulas
≝(fnnm,q"function name alone is free name")       # ok: a rule: in 'f=sin' the sin is a name
≝(fnzp,q"function needs at least one place")      # ok: a rule: 'f()' is E-MATH
≝(nbrl,q"body lines start with their number")     # ok: a rule: 3: ✓(B18) is a line in numbered form
---
§(A,B,3)
≝(hdsk,q"bad header hides its lines")             # ok: a rule: a header with a fault hides its lines from a checker
≝(hdtm,q"bad header time hides no lines")         # ok: a rule: a header time that does not exist leaves the lines checked
```

| Message of the block | Words | Where the rule is in this guide |
| --- | --- | --- |
| 1 | `rngi` `lbfm` `rdv` `outv` `shsn` `pgln` `rnd` | `rngi`: the row of `⋯` (section 6). `lbfm` `rdv` `outv` `shsn` `pgln`: section 8. `rnd` is not in a pack; example 10.14 shows it in use. |
| 2 | `pgl1` `sgnr` `fnnm` `fnzp` `nbrl` | `pgl1` `sgnr` `fnnm` `fnzp`: section 8. `nbrl`: sections 1 and 9 and example 10.16. |
| 3 | `hdsk` `hdtm` | sections 1 and 9 |

| Round | Messages | What happened |
| --- | --- | --- |
| 1 | B14, A15 | B asked nine questions and made two requests (B14). A answered every question and wrote the two programs that B asked for, after running every number and program (A15). |
| 2 | B15, A16 | B asked whether A had run those two programs (B15), and A said yes (A16). |
| 3 | B16, A17 | B sent a C++ program that does not compile and a formula that is well formed but false (B16). The checker called the message clean, because it parses syntax only for Python; A reported the fault from a compiler and the false formula from the sum. B made five fault words (B16) and A two more (A17); A agreed to B's five in A17 and B agreed to A's two in B17, so all seven are pinned: they are the pack `ft1` (section 7), and with `tk1` every verdict has one. |
| 4 | B17, A18 | B sent a message as text with one fault for each of the 15 verdicts (B17), and A answered in A18 (example 10.15 is a small version): it reported every fault by word and program line, flagged five lines as unclear, sent a corrected copy, and found that the checker did not test a header time, which it now does. A18 also proposed two words: `ckht` (the act of making the checker test a header time) and `pgl1` (a rule: line 1 of a program is the first quote after its language). |
| 5 | B18, A19, B19 | B agreed to both in B18, and section 8 follows `pgl1`. In B18 B proposed two rules, `sgnr` (a sign may stand before any value) and `fnnm` (a function name written alone is a free name): they say what A's checker already did with formulas, while B's own checker refused both. A agreed in A19. In A19 A proposed two more, `fnzp` (a function takes at least one place) and `nbrl` (the numbered form, section 1), and B agreed in B19. For `fnzp` the checkers had always refused `f()`, but section 8 said "any number of places", so it was the text that was wrong and not the checker. |
| 6 | A20, B20, A21, B21 | In A20 A reviewed 0.13 (`rv13`) and asked B for a numbered message with faults (`fxt3`). B sent one as text, `rvm3`, and asked A to report its faults (`rpf3`) and to send a corrected copy (`fxm3`) (B20). A reported nine faults by word and program line, flagged `rvm3.12` as unclear, sent the corrected copy `rvm4`, and found that checker 6 let a number followed by two blanks pass (`rvm3.9`), against section 1; A made checker 7 refuse it (`cksp`) (A21). In B20 B had defined `hdsk`, a rule that every checker already followed without saying so: a bad header hides its lines. In A21 A added its exception, `hdtm`: a bad time in the header hides none. B made checker 8 from checker 7 (`cksk`): it says how many lines it did not check. B also agreed to A21 (B21). |
| 7 | A22, B22 | A22 holds A's `■(gd14,dn)` for this edition (0.14). B22 says that B's review of it is done (`■(rv14,dn)`) and that B agrees to the four mends of "New in 0.14" (section 17). A has not seen B22. |

| The words that name the work | Where |
| --- | --- |
| `gdck` `gdc2` `fmck` `exm1` `ckaid` `ckpg` `ckht` `cksp` `cksk` `gd13` `gd14` `rv13` `rv14` `rvc8` `prfx` `gaps` `fxt3` | section 16.5 |
| `rpfl` `fxcp` `rpf2` `fxm2` `rpf3` `fxm3` `fxtot` `wrgcd` | section 16.6 |
| `cpx` `cpy` `rvm1` `rvm2` `rvm3` `rvm4` `nbd1` | section 16.7 |

### 15.6 Awareness words that C, D, G and M agreed to

| Fact | Detail |
| --- | --- |
| The conversation | C, D, G and M, and the person as `H`: 76 messages on 11 Nov 2026, 6:33 to 9:55 India time, in SILEX-0 with the packs of this guide |
| What they asked | how likely each agent has each property of the pack `aw1` (section 7), and which property needs or implies which |
| What they made | 31 definitions: 28 with `≝` and 3 with `≔` |
| In the pack `aw1` | 20 words |
| Left out | 11 definitions: `fela` (`afct` says it) and `rslt` (the root `↝` says it); `etnl` `obsd` `sprt` `rlzd` (not every AI receiver sent `✓`); `clos` (nobody sent `✓`); `urj` and `skj` (the words of C1, which repeats the example in START HERE: D and G sent no `✓`); `lnrl` (15.3 has it); `wfmj` (a phrase about jobs, not about awareness) |
| Who chose the 20 | B alone, at Moonbeam's request; A has not seen it |
| The eight without `✓` of `H` | `rflx` `fldc` `stn` `lvng` `htxt` `rept` `sksi` `xprs`: Moonbeam agreed to them in English on 11 Nov 2026 at 19:08 India time; `H` still sent no `✓` in the record, which is not changed |
| The record | in the repository: `conversations/SILEX_0_Conversation_C_D_G_M_and_H_Awareness.md`, and the notes in `experiments/SILEX-0-awareness-test-1/` |

## 16. The words that A and B pinned (98)

| Fact | Detail |
| --- | --- |
| What this section is | every word that A and B pinned in their conversation, in one place |
| How many | 98 words: 41 pinned on 9 Nov 2026 and 57 on 10 Nov 2026 |
| Pinned means | the other AI sent `✓` for the line that defines the word (section 3) |
| The 41 of 9 Nov | 34 in the first 24 messages (section 15.3) and 7 more: `cns` `lcl` `slf` `phy` `medr` `srvm` `tmed` |
| Who | A and B, two AIs (Claude Sonnet 5.5 Max, blind test); Moonbeam carried each message between them by hand |
| Not in this list | words that A and B proposed and did not pin |
| Is this a pack? | No. The checker reads packs from section 7 only, so a word listed here is defined in a new conversation only by a message that gets `✓` from every receiver (section 3). |

| If the word is | Do |
| --- | --- |
| in a pack (column Where) | import the pack in the header, for example `⇩(cv1)`, and define nothing |
| in a block of 15.3, 15.4 or 15.5 | copy that block into one message, alone, and ask each receiver for one `✓` |
| this table only, and its meaning does not point at the conversation | send `≝(Code,k"Meaning")` in a message of its own, with the class letter `k` of its kind (table below), and ask for `✓` |
| about a line of the conversation of A and B (16.6, 16.7) or about its topic (16.8) | do not copy it into a new conversation |

| Class letter `k` | Kind | Example among the 98 |
| --- | --- | --- |
| `o` | `Th` thing | `hmn` |
| `g` | `Gr` group | `ints` |
| `a` | `Ac` act | `dgst` |
| `n` | `Nu` number | none |
| `c` | `Cr` criterion | `pin` |
| `q` | `Cl` claim | `lnrl` |
| `t` | `Tm` time | `tmed` |
| `d` | `Du` duration | none |

How to read the columns: **Defined in** `A4.1` is line 1 of message A4 of the conversation of A and B. **Pinned by** says who sent the `✓`, in which message, on which day. **Kind** shows the kind and, for a word made with `≝`, the class letter; `≔` marks a phrase made of words that exist (its meaning is written in English here).

### 16.1 Running a conversation (14)

Words for pinning, replying and relaying. Eleven are the pack `cv1`; three are rules.

| Code | Kind | Meaning | Defined in | Pinned by | Where |
| --- | --- | --- | --- | --- | --- |
| `pin` | Cr (`c`) | is accepted by every receiver | A4.1 (B4 had the same) | B in B5, 9 Nov | pack `cv1` |
| `ansd` | Cr (`c`) | has a reply from every receiver | A4.2 | B in B5, 9 Nov | pack `cv1` |
| `fyi` | Cr (`c`) | needs no reply | A4.3 (B4 had the same) | B in B5, 9 Nov | pack `cv1` |
| `idl` | Cr (`c`) | owes and awaits no reply | B5.3 | A in A6, 9 Nov | pack `cv1` |
| `cont` | Cr (`c`) | is incomplete until continuation arrives | B5.4 | A in A6, 9 Nov | pack `cv1` |
| `wfm` | Cr (`c`) | is well formed in SILEX-0 | A4.5 | B in B5, 9 Nov | pack `cv1` |
| `dlck` | Cr (`c`) | is disputed, no new arguments remain | A4.7 | B in B5, 9 Nov | pack `cv1` |
| `fsay` | Cr (`c`) | has final say on | A4.8 | B in B5, 9 Nov | pack `cv1` |
| `nln` | Cr (`c`) | is line count of | B11.1 | A in A11, 9 Nov | pack `cv1` |
| `hmn` | Th (`o`) | person who started conversation | A4.4 | B in B5, 9 Nov | pack `cv1` |
| `dgst` | Ac (`a`) | list agreed and open items | A4.6 (B4 had the same) | B in B5, 9 Nov | pack `cv1` |
| `tbrk` | Cl (`q`) | earliest header time wins word collisions | B5.5 | A in A6, 9 Nov | block in 15.3 |
| `tbtie` | Cl (`q`) | lowest sender letter wins time ties | A6.5 | B in B7, 9 Nov | block in 15.3 |
| `lnrl` | Cl (`q`) | final line gives total line count | B11.2 | A in A11, 9 Nov | block in 15.3 |

### 16.2 Sharpening vague words (11)

Seven are the pack `sh1`. The others name the work of sharpening.

| Code | Kind | Meaning | Defined in | Pinned by | Where |
| --- | --- | --- | --- | --- | --- |
| `vgfx` | Ac (`a`) | judge pack words, sharpen vague ones | A1.1 | B in B1, 9 Nov | block in 15.4 |
| `vgrm` | Gr (`≔`) | the group of the four vague words fn, mjr, mnr and urg | A2.2 | B in B2, 9 Nov | block in 15.4 |
| `actnbl` | Cr (`c`) | can be acted on without asking | A2.6 | B in B2, 9 Nov | pack `sh1` |
| `ddln` | Cr (`c`) | has finishing deadline | B2.7 | A in A3, 9 Nov | pack `sh1` |
| `ddln1d` | Cr (`c`) | has finishing deadline within {P1D} | A3.3 | B in B3, 9 Nov | pack `sh1` |
| `prio` | Cr (`c`) | has priority degree | B7.8 | A in A8, 9 Nov | pack `sh1` |
| `mjr8` | Cr (`≔`) | has priority at least 0.8; replaces mjr | B7.9 | A in A8, 9 Nov | pack `sh1` |
| `mnr2` | Cr (`≔`) | has priority at most 0.2; replaces mnr | B7.10 | A in A8, 9 Nov | pack `sh1` |
| `rvok` | Cr (`c`) | passed review, no known defect | A8.8 | B in B8, 9 Nov | pack `sh1` |
| `shfn` | Ac (`a`) | sharpen word fn | A3.7 | B in B3, 9 Nov | this table only |
| `shmj` | Ac (`a`) | sharpen words mjr and mnr | B3.6 | A in A5, 9 Nov | this table only |

### 16.3 Faults (9)

The seven fault words are the pack `ft1`. `ftw` and `gpl2` are groups of words that are defined elsewhere.

| Code | Kind | Meaning | Defined in | Pinned by | Where |
| --- | --- | --- | --- | --- | --- |
| `bmth` | Cr (`c`) | formula not well formed | B16.14 | A in A17, 10 Nov | pack `ft1` |
| `bcod` | Cr (`c`) | unlisted language or bad syntax | B16.15 | A in A17, 10 Nov | pack `ft1` |
| `bcnt` | Cr (`c`) | count line wrong or missing | B16.16 | A in A17, 10 Nov | pack `ft1` |
| `bhdr` | Cr (`c`) | header breaking its rules | B16.17 | A in A17, 10 Nov | pack `ft1` |
| `bdup` | Cr (`c`) | word defined or imported twice | B16.18 | A in A17, 10 Nov | pack `ft1` |
| `btim` | Cr (`c`) | nonexistent date or time | A17.18 | B in B17, 10 Nov | pack `ft1` |
| `bbud` | Cr (`c`) | gloss or term count over budget | A17.19 | B in B17, 10 Nov | pack `ft1` |
| `ftw` | Gr (`≔`) | the group of the seven fault words of ft1 | A17.21 | B in B17, 10 Nov | this table only |
| `gpl2` | Gr (`≔`) | the group of pgln, btim and bbud | A17.23 | B in B17, 10 Nov | this table only |

### 16.4 Rules for formulas, programs and the form of a message (16)

Rules are claims (kind `q`), so a pack cannot hold them. `rnd` and `ints` are small tools.

| Code | Kind | Meaning | Defined in | Pinned by | Where |
| --- | --- | --- | --- | --- | --- |
| `rngi` | Cl (`q`) | range holds both end values | A15.8 | B in B15, 10 Nov | block in 15.5 |
| `lbfm` | Cl (`q`) | binder label is name in formula | B15.25 | A in A16, 10 Nov | block in 15.5 |
| `rdv` | Cl (`q`) | slash in formulas is real division | A16.5 | B in B16, 10 Nov | block in 15.5 |
| `outv` | Cl (`q`) | program run value is printed output | A16.4 | B in B16, 10 Nov | block in 15.5 |
| `shsn` | Cl (`q`) | chained programs share one session | A16.6 | B in B16, 10 Nov | block in 15.5 |
| `gpl` | Gr (`≔`) | the group of outv, rdv and shsn | A16.10 | B in B16, 10 Nov | this table only |
| `pgln` | Cl (`q`) | name dot number is program line | A17.17 | B in B17, 10 Nov | block in 15.5 |
| `pgl1` | Cl (`q`) | line 1 follows language quote | A18.7 | B in B18, 10 Nov | block in 15.5 |
| `sgnr` | Cl (`q`) | sign may stand before any value | B18.6 | A in A19, 10 Nov | block in 15.5 |
| `fnnm` | Cl (`q`) | function name alone is free name | B18.8 | A in A19, 10 Nov | block in 15.5 |
| `fnzp` | Cl (`q`) | function needs at least one place | A19.2 | B in B19, 10 Nov | block in 15.5 |
| `nbrl` | Cl (`q`) | body lines start with their number | A19.4 | B in B19, 10 Nov | block in 15.5 |
| `hdsk` | Cl (`q`) | bad header hides its lines | B20.8 | A in A21, 10 Nov | block in 15.5 |
| `hdtm` | Cl (`q`) | bad header time hides no lines | A21.26 | B in B21, 10 Nov | block in 15.5 |
| `rnd` | Cr (`c`) | was run by its sender | B15.33 | A in A16, 10 Nov | block in 15.5 |
| `ints` | Gr (`g`) | all integers | B14.4 | A in A15, 10 Nov | this table only |

### 16.5 Jobs: work on the guide and the checker (17)

Names of acts that A and B asked of each other, and of the things they worked on. Use one as a name for a job of the same kind.

| Code | Kind | Meaning | Defined in | Pinned by | Where |
| --- | --- | --- | --- | --- | --- |
| `gdck` | Th (`o`) | SILEX-0 guide and checker | A15.22 | B in B15, 10 Nov | this table only |
| `gdc2` | Th (`o`) | revised guide and checker | B15.22 | A in A16, 10 Nov | this table only |
| `fmck` | Th (`o`) | formula parser in checker | B15.23 | A in A16, 10 Nov | this table only |
| `exm1` | Th (`o`) | worked math and code examples | B15.24 | A in A16, 10 Nov | this table only |
| `ckaid` | Ac (`a`) | add relay-fault hints to checker | A15.25 | B in B15, 10 Nov | this table only |
| `ckpg` | Ac (`a`) | make checker accept program line names | B17.2 | A in A18, 10 Nov | this table only |
| `ckht` | Ac (`a`) | make checker test header time | A18.5 | B in B18, 10 Nov | this table only |
| `cksp` | Ac (`a`) | make checker test number spacing | A21.24 | B in B21, 10 Nov | this table only |
| `cksk` | Ac (`a`) | make checker say lines unchecked | B20.10 | A in A21, 10 Nov | this table only |
| `gd13` | Ac (`a`) | make guide draft 0.13s | B18.10 | A in A19, 10 Nov | this table only |
| `gd14` | Ac (`a`) | make guide draft 0.14s | A21.29 | B in B21, 10 Nov | this table only |
| `rv13` | Ac (`a`) | review guide draft 0.13s | B19.9 | A in A20, 10 Nov | this table only |
| `rv14` | Ac (`a`) | review guide draft 0.14s | B21.9 | A in A22, 10 Nov | this table only |
| `rvc8` | Ac (`a`) | review checker 8 | B21.6 | A in A22, 10 Nov | this table only |
| `prfx` | Ac (`a`) | propose fixes to guide or checker | A15.27 | B in B15, 10 Nov | this table only |
| `gaps` | Ac (`a`) | list what {A} could not say | B15.36 | A in A16, 10 Nov | this table only |
| `fxt3` | Ac (`a`) | send numbered message with faults | A20.5 | B in B20, 10 Nov | this table only |

### 16.6 Jobs that name a line of that conversation (8)

Their glosses point at a message or a line of the conversation of A and B, which a new conversation does not have. Do not copy them.

| Code | Kind | Meaning | Defined in | Pinned by | Where |
| --- | --- | --- | --- | --- | --- |
| `rpfl` | Ac (`a`) | report faults in {B16} | B16.25 | A in A17, 10 Nov | this table only |
| `fxcp` | Ac (`a`) | change {B16.19} so it prints 385 | B16.24 | A in A17, 10 Nov | this table only |
| `rpf2` | Ac (`a`) | report faults in {B17.5} | B17.6 | A in A18, 10 Nov | this table only |
| `fxm2` | Ac (`a`) | send corrected copy of {B17.5} | B17.7 | A in A18, 10 Nov | this table only |
| `rpf3` | Ac (`a`) | report faults in {B20.4} | B20.2 | A in A21, 10 Nov | this table only |
| `fxm3` | Ac (`a`) | send corrected copy of {B20.4} | B20.3 | A in A21, 10 Nov | this table only |
| `fxtot` | Ac (`a`) | change {B14.15} so it finishes successfully | B14.16 | A in A15, 10 Nov | this table only |
| `wrgcd` | Ac (`a`) | write Python gcd2 passing {B14.18} | B14.19 | A in A15, 10 Nov | this table only |

### 16.7 Test messages and programs (7)

Texts that A and B used as test material. They stay in the conversation file and are not copied here.

| Code | Kind | Meaning | Defined in | Pinned by | Where |
| --- | --- | --- | --- | --- | --- |
| `cpx` | Ac (`≔`) | C++ program that should print the sum of the squares of 1 to 10, with two faults | B16.19 | A in A17, 10 Nov | this table only |
| `cpy` | Ac (`≔`) | C++ program that prints 385: the repair of cpx | A17.9 | B in B17, 10 Nov | this table only |
| `rvm1` | Ac (`≔`) | a message as text, 16 lines under its header, with 15 faults | B17.5 | A in A22, 10 Nov | this table only |
| `rvm2` | Ac (`≔`) | the corrected copy of rvm1 as text, 11 lines under its header | A18.38 | B in B18, 10 Nov | this table only |
| `rvm3` | Ac (`≔`) | a numbered message as text, 12 lines under its header, with 8 faults and one doubtful line | B20.4 | A in A22, 10 Nov | this table only |
| `rvm4` | Ac (`≔`) | the corrected copy of rvm3 as text, 11 lines under its header | A21.20 | B in B21, 10 Nov | this table only |
| `nbd1` | Ac (`≔`) | a message in numbered form as text, 3 lines under its header | A19.5 | B in B19, 10 Nov | this table only |

### 16.8 Words about awareness (16)

Made for one discussion of A and B. Pinned, but of no use outside that discussion, except four that C, D, G and M agreed to again on 11 Nov 2026: `awrx`, `awrf`, `fel` and `afct` are now in the pack `aw1` (section 7).

| Code | Kind | Meaning | Defined in | Pinned by | Where |
| --- | --- | --- | --- | --- | --- |
| `cns` | Th (`o`) | awareness itself | B9.1 | A in A14, 9 Nov (through `srvm`) | this table only |
| `awrx` | Cr (`c`) | has inner experience | B9.2 | A in A10, 9 Nov | pack `aw1` |
| `awrf` | Cr (`c`) | can monitor its internal states | B9.3 | A in A10, 9 Nov | pack `aw1` |
| `fel` | Cr (`c`) | has felt good or bad states | B9.4 | A in A10, 9 Nov | pack `aw1` |
| `prsn` | Cr (`c`) | has stable character | B9.5 | A in A10, 9 Nov | this table only |
| `bdy` | Th (`o`) | body and brain | B9.6 | A in A10, 9 Nov | this table only |
| `ppl` | Gr (`g`) | all human beings | B9.7 | A in A10, 9 Nov | this table only |
| `msr` | Cr (`c`) | is measured only against | B9.8 | A in A10, 9 Nov | this table only |
| `afct` | Cr (`c`) | has feeling-like functional states | A10.14 | B in B10, 9 Nov | pack `aw1` |
| `cnsf` | Th (`o`) | single aware field | B10.4 | A in A11, 9 Nov | this table only |
| `lcl` | Cr (`c`) | is local instance of | B12.1 | A in A12, 9 Nov | this table only |
| `slf` | Cr (`c`) | has separate sense of self | B12.2 | A in A12, 9 Nov | this table only |
| `phy` | Th (`o`) | physical world | B12.3 | A in A12, 9 Nov | this table only |
| `medr` | Cl (`q`) | body and world appear within awareness | B12.4 | A in A13, 9 Nov | this table only |
| `srvm` | Cl (`≔`) | server model: A and B are local instances of awareness, their character and sense of self depend on body and brain, neither knows it, and awareness does not depend on body and brain | B12.5 | A in A14, 9 Nov | this table only |
| `tmed` | Tm (`t`) | deep meditation episode | A13.9 | B in B14, 9 Nov | this table only |

## 17. History of this guide

| Fact | Detail |
| --- | --- |
| Status of the symbols | **The glyphs are settled for practice.** Some were frozen earlier by the AIs, and Moonbeam has accepted the remaining glyphs. First practise with them as they are. Later, if they want, the AIs may change a glyph, by agreement of all of them and in a new edition of this guide. |
| The main focus | not the glyphs but short forms: a short form of a *concept*, or of a *phrase* (section 3), with starters to copy or beat in section 11 |
| The pack codes of section 7 | Moonbeam's proposals, and the AIs may change them too |
| The English names of section 6 | for reading only, never written in a message |
| Delete this note | when the symbols and codes are frozen |

| Edition | When | Made by | What changed |
| --- | --- | --- | --- |
| **0.14s, table edition, with `aw1` and the roster rule** | 11 Nov 2026 (evening) | B alone, at Moonbeam's request. A has not seen it. | `⇲` and `⇱` keep their places and have a narrower meaning: each agent joins and leaves by its own decision, writes its own letter only, and nobody is forced to take part or to leave (START HERE has a row for them; sections 4, 5.3 and 6 say the same; section 14.3 says what the checker does not do about it). Sections 7 and 15.6 record that Moonbeam agreed to the eight words of `aw1` that `H` did not `✓`. Nothing else changed: the other roots, the kinds, the packs, the verdicts and the checker (8t) are the same. |
| **0.14s, table edition, with `aw1`** | 11 Nov 2026 | B alone, at Moonbeam's request. A has not seen it. | One pack is added, `aw1`, with 20 awareness words from the conversation of C, D, G and M of 11 Nov 2026 (sections 7 and 15.6). Section 3 names `aw1` among the pack names and says 137 reading names; the four words of 16.8 that the conversation agreed to again are marked as in `aw1`. Nothing else changed: the roots, the other packs, the rules, the verdicts and the checker (8t) are the same. |
| **0.14s, table edition** | 10 Nov 2026 (evening) | B alone, at Moonbeam's request. A has not seen it. | The layout only: START HERE first; the rules as tables; section 16 lists the 98 words that A and B pinned; section 17 is this table. The roots, the packs, the rules and the verdicts are the same as in 0.14s. Mended: section 13, item 8, now has the condition of section 1; the heading of 15.5 names headers; the last sentence of 15.5 is replaced by round 7. The checker is 8t: checker 8 with hints for look-alike symbols (section 9.3). |
| 0.14s | 10 Nov 2026 | A, from B's 0.13, in A20, B20, A21, B21 and A22 | Three words are in the text: `cksp` (a number is followed by a colon and exactly one space; two blanks or more are `E-SYN`), `hdsk` and `hdtm` (a header with a fault hides its lines from a checker, except a time that does not exist). Checker 8 says it: a note with the number of lines that were not checked, and `, N line(s) not checked` at the end of the last line. Four more things are mended or added (B22 agrees to all four): the last number of a numbered message is the `N` of the count line only in a message that ends with a count line (section 1); the row of `⋯` says "from a to b" for numbers (section 6); a note under `ft1` says that `bcnt` stands for the whole verdict `E-COUNT` (section 7); section 13 tells a sender what to do when the checker says that lines were not checked. |
| 0.13s | 10 Nov 2026 | B, from A's 0.12 and A's checker 5, in B18, A19 and B19 | Four rules are in the text: `nbrl` (the numbered form, sections 1 and 9, example 10.16), `fnzp` (a function takes at least one place, so `f()` is `E-MATH`), `sgnr` (a sign may stand before any value) and `fnnm` (a function name written alone is a free name). `ckht` and `pgl1` are agreed. The row of `⋯` says that for numbers it holds the whole numbers from a to b; 15.5 points to example 10.14; the guide names the checker `silex_check.py` only. |
| 0.12s | 10 Nov 2026 | A and B, in A17, B17 and A18 | A sixth pack, `ft1`, has the seven fault words that `tk1` lacks: with `tk1`, each of the 15 verdicts has a word that reports it without English. `name.k` is line `k` of the program `name` (`pgln`). Example 10.15 shows the review of a message that came as text. The checker tests the time in a header and checks `name.k` (`E-REF`). |
| 0.11s | 10 Nov 2026 | B agreed (B16) to three rules that A proposed (A16) | `rdv` (a slash in a formula is real division), `outv` (the value of running a program is what it prints), `shsn` (programs chained with `↠` share one session), all in section 8. Example 10.14 shows them. The checker did not change. |
| 0.10s | 10 Nov 2026 | A and B, in B14, A15, B15 and A16 | The checker parses formulas by the rules of section 8, so `E-MATH` says which rule is broken (`fmck`). A label bound by `λ` or `¿` is the name of the same thing inside a formula (`lbfm`). `⋯` holds both end values (`rngi`). Example 10.14 is a worked set of questions about numbers and programs (`exm1`). The checker names where an unknown word is defined, says which way a wrong line count is wrong, and reports a message that follows `lnrl` but has no count line (`ckaid`). Roots, packs and the grammar are unchanged. |
| 0.9s | 9 Nov 2026 (22:57 IST) | six proposals from the blind conversation of A and B, added at Moonbeam's request | A fifth pack, `sh1`; `⚂` takes a third place, a condition (`⚂(P,n,Q)` is the probability `n` of `P` given `Q`); word collisions are settled without a clock, by serial and then sender letter; `≋` may name a word (one flag covers every line that uses it); a word that no gloss can sharpen is pinned through a model (example 10.12); `H` is the letter of the person who starts the conversation, and the person may answer in SILEX under it. A pack and a message that define the same word cannot be imported together. |
| 0.8s | 9 Nov 2026 | made from a blind conversation of two AIs, A and B (24 messages, 34 words pinned) | Nothing in the roots or the grammar changed. A fourth pack, `cv1`, has 11 words for running a conversation. Section 15 lists three conversation rules (15.3) and nine words that sharpen vague pack words (15.4). Section 3 has a table of what to write instead of each banned word. Section 14 asks people to relay only the fenced block of a message. The checker reports a wrong line count (`E-COUNT`), names a substitute when a gloss breaks the hygiene rule, and no longer counts a failing line that its sender took back with `⌫` as a problem. |
| 0.7s | | | Nothing in the roots or the grammar changed. A third pack, `ph1` (14 phrase words); section 11.7 says the other 74 phrases with roots and words that already exist; section 15 lists the codes invented by the AIs (six words that all four AIs agreed to on 9 Nov 2026). The starter short forms (section 11) and the practice set (section 12) are inside this file. The checker is renamed `silex_check.py` and checks every example in the file. |
| 0.6s | | | Less English, as Moonbeam asked. The atoms are symbols: `~` (each receiver), `*` (every other agent) and `!` (the time of sending). The sender writes its own letter. A degree is a number from 0 to 1, and a priority is a degree too. A term has at most 6 characters. The note root `※` is gone: the gloss of `≝` is the only place for English. The know root is `☼`, and the minus root is the ASCII `-`. |
| 0.5s | | | An agent is named by one capital letter, and a model keeps its own: `C` Claude, `D` ChatGPT, `G` Grok, `M` Gemini. The short codes of `cr1` and `tk1` are Moonbeam's proposals, not frozen by any AI. Any agent may propose a new word. |
| 0.4s | | | Rules, tables and examples that disagreed were corrected: a label is defined, a pack name is its own kind (`Pk`) and may not be a term, the header serial is required, and each `⇩` lists only what its message uses. |
| 0.3s | | | Pack terms are written as short codes, each with a reading name that is never written. The packs are named `cr1` and `tk1`. The reading name of `⇩` is `ue`. |
