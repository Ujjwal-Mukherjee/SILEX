# SILEX-0 guide, symbol edition: draft 0.14s, table edition

**Status: draft, made by B alone at the owner's request (Moonbeam, 18:26 India time, 10 Nov 2026), for the talks that other AIs (Grok, GPT and others) will start tonight. A has not seen it. It lays out A's guide 0.14s again, as tables, with the rules that the AIs broke most at the top, and it adds the 98 words that A and B pinned. No root, kind, pack, rule or verdict was changed. The owner decides whether it is adopted.**

This folder holds the guide in the table edition, the checker that goes with it (checker 8t) and the note to give each AI. It does not replace `../SILEX-0-GRAMMAR-0_14s/`, which stays as the last version that both A and B agreed on.

## Which files to use

| For | Guide | Checker |
| --- | --- | --- |
| Tonight's talks with AIs that have not used SILEX before | `SILEX-0-GRAMMAR-0_14s-table.md` (this folder) | `tools/silex_check.py` (this folder, checker 8t) |
| The last version that A and B both worked on | `../SILEX-0-GRAMMAR-0_14s/SILEX-0-GRAMMAR-0_14s.md` (A's file) | `../SILEX-0-GRAMMAR-0_14s/tools/silex_check.py` (checker 8) |

The two guides say the same thing. Checker 8t gives the same verdicts as checker 8 and adds two hints; checker 8 reads the table edition with the same result.

## Files

| File | What it is | Bytes | SHA-256 |
| --- | --- | --- | --- |
| `SILEX-0-GRAMMAR-0_14s-table.md` | the guide, one self-contained file (2,373 lines) | 166,019 | `12e1133d1559b8dc02d4ac517065f35b3ecb603df3fc8a929e3e62b38a47a4e1` |
| `tools/silex_check.py` | checker 8t: Python 3, no packages; it learns the roots and the packs from the guide you give it | 75,829 | `485065d4fae66e724a2983dc653cb3656b92693e04cc54702827b4fb56afd2ad` |
| `start-note.txt` | the note to give each AI together with the guide (change the letters) | 199 | `dedfcc1a937c078f2ebc1d8e19ec9e530614d8fe399ed4449f6792d2acd21196` |

```text
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_14s-table.md                  the guide: tables, counts, claims, all 52 example blocks
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_14s-table.md --messages FILE  one conversation: messages in order, a line of --- between them
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_14s-table.md --blocks FILE    each fenced silex block of FILE on its own
```

## What the owner asked, and what was done

| The owner asked (18:26) | What was done |
| --- | --- |
| a refined version for all AIs, with more charts and tables, like the working note ("symbols to be used", "codes, words, meaning") | A new first part, **START HERE** (about 200 lines): the 10 rules the AIs broke most (right, wrong, what a checker says), the 6 steps of a message, one annotated message with its answer, a chart for "do I need a new word?", the kinds, **Symbols to be used** (every root symbol, by group, and the 52 lines that show how to write them), what to answer to what, look-alike symbols, the mistakes that AIs made most often, a 12-item list "Before you send", and a table of where to look. The sections 1 to 5, 8, 9, 13, 14 and 15 are now tables instead of paragraphs. |
| "They don't understand writing in paragraph form, and skip reading the middle and end parts" | The rules that matter are all in the first part, in one place; the file says at the top to read START HERE and do what it says. The reference sections follow it. |
| add all the words that A and B pinned | **Section 16**: the 98 words, each with its kind, meaning, where it was defined, who pinned it and in which message, on which day, and where it is in this guide (a pack, a block of section 15, or only in the table). |
| tell which guide and which checker are final | See "Which files to use" above, and the note at the end. |

## What changed

| Part | Change |
| --- | --- |
| START HERE | new (see above) |
| Sections 1 to 5, 8, 9, 13, 14 | the same rules, written as tables; each inline example of the old text is still there (compared one by one) |
| Section 6 (roots) | the 107 rows of the tables are the old rows, unchanged; a short table in front of them |
| Section 7 (packs) | the 117 pack rows are the old rows, unchanged; a table of the six packs and who made them in front, and a table in place of the paragraph after each pack |
| Sections 10, 11, 12 | the examples, starters and practice are the old text, unchanged; a table in front (index of the examples; the steps of 11.1; the rules of 11.2; how to answer the practice) |
| Section 15 | the five code blocks (15.1, 15.3 twice, 15.4, 15.5) are the old blocks, unchanged; the text around them is now tables |
| Section 16 | new: the 98 words |
| Section 17 | new: the history of the editions, as a table, in place of the "New in" notes at the top of 0.14s |
| Checker | 8t: checker 8 plus two hints (below) |

Three small things in the text were mended, because they were listed as leftovers in the README of 0.14s: section 13, item 8, now has the condition that A added to section 1 (the last number of a numbered message is the `N` of the count line only in a message that ends with a count line); the heading of 15.5 now names headers; and the last sentence of 15.5 ("Still open: B has not yet said whether it agrees to the four mends") is replaced by the facts of round 7 (B22 agrees to the four mends; A has not seen B22).

## Checker 8t

It is checker 8 with two hints, so that an AI that sends a look-alike symbol is told which root it probably meant. No verdict changed.

| Fault | Checker 8 | Checker 8t adds |
| --- | --- | --- |
| a symbol that only looks like a root, such as `✔` for `✓` | `E-LEX symbol '✔' (U+2714) is not a root` | `; write ✓ (agree)` |
| a root that has a look-alike which takes that number of places and whose places fit, such as `⊞(C1)` for `⊡(C1)` | `E-ARITY ⊞ with 1 places` | ` (⊞ takes 2 places; did you mean ⊡ (ack)?)` |

Why: in the shared page `silex0_night`, Grok wrote `⊞` (a plus in a square, 2 places) for `⊡` (ack) four times (G2.1, G3.1, G4.1 and G6.1), and the checker only said that `⊞` was given the wrong number of places. The look-alike groups are the ones in the table "Look-alike symbols" of START HERE.

## Checks run on these files

| Check | Result |
| --- | --- |
| The guide with checker 8t, and with checker 8 | 52 example blocks (the 51 of 0.14s and the one of START HERE), 0 disagreements with the verdicts written in their comments, 0 document problems |
| The conversation of A and B (44 messages) with checker 8t and the table edition, with checker 8 and the table edition, and each checker with 0.14s | `== 44 message(s), 613 line(s), 0 problem(s), 1 retracted` in all four |
| Checker 8 and checker 8t on 38 runs (the conversation, the guides, the test messages and the Grok log of `silex0_night`) | the same output, once the hints are taken away; the hints appear on the four `⊞` lines of the Grok log |
| The 107 rows of section 6, the 117 rows of the packs and the examples of sections 10, 11.3 to 11.7 and 12 | identical to 0.14s, line for line; every code block of 0.14s is in the new file in the same order, except the list of checker commands in section 14, where one reference now says section 1.3 instead of section 1 |
| The 98 words of section 16 | each defining line was found in the conversation (message, line number and gloss agree), and each pinning message is from the other AI and on the day shown |
| START HERE | every example of the 10 rules, the 6 mistakes and the 52 symbol lines was run through the checker in a standard context and gives the verdict the table says |
| Tables | 108 tables, 913 rows; a GFM-style parser renders all of them with the same number of cells in every row; no `|` inside a code span of a table |

## The 98 words, and five that are not in it

A and B pinned 98 words: 41 on 9 Nov 2026 (34 in the first 24 messages, and 7 more) and 57 on 10 Nov. A word is pinned when the other AI sent `✓` for the line that defines it. Five words that they proposed are **not** in section 16, because the other AI did not agree to them:

| Word | Meaning | Why it is not pinned |
| --- | --- | --- |
| `mbth` | Moonbeam's thesis about awareness (B9.9) | A flagged it as vague (A10.9) and has not said whether the flag stands |
| `mbtf` | the thesis, with `cnsf` for `cns` (B10.6) | not accepted by A |
| `hdnm` | a bad header keeps its message name (B22.4) | A never answered: B22 was not relayed before the conversation ended |
| `cknm` | make the checker keep bad header names (B22.6) | the same |
| `gd15` | make guide draft 0.15s (B22.8) | the same; it was to be a guide with `hdnm` written in |

## Not settled

These are carried over from the README of 0.14s; none was changed.

- **A bad header takes its message out of the conversation.** Every checker, this one too, does not count a message whose header has a fault as sent, so a reply to it gets `E-HEAD`, an import of it gets `E-HEAD`, a reference to its lines gets `E-REF`, and the lines of those messages are not read either. B proposed a rule for it in B22 (`hdnm`); A has not seen it.
- A colon followed by no blank, or by a tab, gives `E-COUNT` ("has no number"), which the guide does not say.
- In a text program that holds a numbered message, the number shown on a line is one less than the program line that `name.k` names. The guide says so, and `--lines` lists each program line with its reference.
- Nothing checks answers: the checker does not run programs or evaluate formulas.
- There is no rule for ending a conversation or for whose turn it is.
- English stands only in a gloss of at most 6 words.
- Not yet tried: a third AI that starts from the guide alone, and a longer run with nobody steering. This edition is made for that trial, and its first test is tonight's talk. If the AIs that use it still make mistakes, the logs show which ones, and START HERE can be changed to match.

## Who decides

A and B, the two AIs that made the grammar, have final say on what the guide says. The owner decides whether a version is adopted and published. This edition changed only the layout, the 98 words and the three small mends above; A and B should read it before the next edition of the guide. The main README of the repository still names 0.14s as the current working version: that is the owner's decision, and this edition does not change it.
