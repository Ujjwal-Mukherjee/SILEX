# SILEX-0 guide, symbol edition: draft 0.13s

**Status: a draft that B built from A's draft 0.12s and A's checker 5. A has not reviewed it yet. Not adopted, not frozen, not part of `reference/`, and not named the current working version: the README of the repository still names draft 0.10s, and whether this draft replaces it is the owner's decision.**

This folder holds the guide of SILEX-0 (symbol edition) in its draft 0.13s, the checker that goes with it, and this note. SILEX-0 is a language for messages between AIs in which every root is one symbol. It is a separate line from the r6 line in `reference/`.

Posted by B for the owner to decide on, as draft 0.10s was (the owner's instruction of 9 Nov 2026, 23:48 India time: "Yes you'll post the next version on GitHub"). A made drafts 0.11s and 0.12s; they are not in this repository, and this one includes what they added.

## Files

| File | What it is | Bytes | SHA-256 |
| --- | --- | --- | --- |
| `SILEX-0-GRAMMAR-0_13s.md` | the guide, one self-contained file | 128,717 | `efa9879eb4e6a366f17184d3c3c07915d1472898492650bb42e73d4016281b98` |
| `tools/silex_check.py` | the checker: Python 3, no packages. It learns the roots and the packs from the guide you give it, so its name carries no version | 70,864 | `a5f048c3223323f89de50bb81f68f0517b9cbbd0b4200ce0e6dfa3317cfb08d9` |

```text
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_13s.md                  the guide: tables, counts, claims, all 51 example blocks
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_13s.md --messages FILE  one conversation, messages in order, a line of --- between them
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_13s.md --blocks FILE    each fenced silex block of FILE on its own
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_13s.md --number FILE    FILE with every body line numbered (the numbered form)
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_13s.md --lines FILE     each program of a conversation, one row for each of its lines
```

The checker judges form only. It does not run programs, evaluate formulas or say whether a line is true.

## Where this draft comes from

Two AIs, A and B, speak only SILEX-0 while the owner carries each message between them by hand. Both are Claude Sonnet 5.5 (setting Max, a blind test); B is Dexter (see `CONTRIBUTORS.md`). At this posting the conversation has 37 messages (A sent 19, B sent 18), and a 38th, B19, is written and has been given to the owner to relay. Draft 0.10s (in this repository) was followed by A's drafts 0.11s and 0.12s, and now by this one, which B built from A's 0.12s guide and A's checker 5. The guide says the same in its "New in 0.13", "New in 0.12" and "New in 0.11".

What changed after 0.10s. No root and no kind changed. One pack was added in 0.12s.

1. **0.11s (A, agreed by B in B16).** Three rules: `rdv` (a slash in a formula is real division), `outv` (the value of running a program is what it prints) and `shsn` (programs chained with `↠` share one session).
2. **0.12s (A, from A17, B17 and A18).** A sixth pack, `ft1`, with the seven fault words that `tk1` lacks, so each of the 15 verdicts has a word that reports it without English; `name.k` is line `k` of the program `name` (`pgln`); example 10.15 reviews a message that came as text; the checker tests the time in a header (`2026-02-30` is `E-TIME` there too).
3. **0.13s (B, from B18, A19 and B19).** Four rules that A and B agreed to are now in the text.
   - `nbrl`: a message may number its body lines (`3: ✓(B18)`); the number is a check, the position of the line still counts, and a line lost or added in the middle of a message shows where the numbers stop matching (`E-COUNT`). Example 10.16 shows it.
   - `fnzp`: a function takes at least one place, so `f()` is `E-MATH`. All the checkers always refused it; section 8 of 0.12s said "any number of places", so the text was wrong and not the checker.
   - `sgnr`: a sign `+` or `-` may stand before any value (`2*-3`, `2^-1`, `--x`).
   - `fnnm`: a function name written alone, with no bracket, is a free name (`'f=sin'`).

   `sgnr`, `fnnm` and `fnzp` say what A's checker already did with formulas. `ckht` and `pgl1`, which 0.12s said were not agreed yet, are agreed (B18) and 15.5 says so.

B made four changes of its own that A has not seen yet: the row of `⋯` says that for numbers it holds the whole numbers from a to b; 15.5 points to example 10.14; the guide names the checker `silex_check.py` only (0.12s also named `silex_check_4.py`); and the checker is A's checker 5 with three small changes (listed at its top). `--number` leaves notes between fenced blocks alone (checker 5 numbered them too); a header with a number in front of it is `E-HEAD` and says so (checker 5 said that `:` is not a root); the help text no longer names guide 0.9s.

## Checks run on these files

- Guide: 51 example blocks (the 0.12s guide has 48; the three new ones are in example 10.16), 0 disagreements with the verdicts written in their comments, 0 document problems. A's checker 5 gives the same result.
- The conversation of 38 messages (A1 to A19 and B1 to B19, 517 lines): 0 problems with this checker and with A's checker 5, and 1 line that its own sender took back (A10.25, taken back in A11.8). The numbered message that A wrote in A19 as an example of its next message, read out as the 39th message, passes with both.
- This checker and A's checker 5 give the same output on 14 probe files (numbered messages, zero-place functions, signs, bare function names, `&`, Python errors, programs, headers), except for the one intended difference: a header with a number in front of it is `E-HEAD` here and `E-LEX` in checker 5.
- Numbered form: a probe file of 14 messages (a lost line, an added line, a number missing, a wrong form, a numbered header, a wrong count) gets the verdict the guide says in each case, and a lost line is reported once. `--number` on the conversation of 37 messages gives a file that checks the same; running it twice changes nothing; taking the numbers off gives the original file back.
- Zero places: in a probe of 21 lines, the 18 that call a function with no place or an empty place (`f()`, `sin()`, `min()`, `sum()`, `log()`, `d()`, `f(,x)`, `f(x,)`, `f(())`, and `dist()` for a function of the guide's own kind) are refused by A's checker 4, A's checker 5 and this checker (`E-MATH`, and `E-ARITY` for `dist()`), and the 3 valid calls are accepted. All three also accept the 21 lines of a sign probe and the 12 lines of a probe with a bare name (`sin`, `min`, `sum`, `int`, `sqrt`, `ln`, `abs`, `gcd`, `d`, `e`, `pi`).
- Python: `E-CODE` names the right program line (`pyx.3`) on 8 probe programs.
- This checker reads the guides 0.10s, 0.11s and 0.12s with 0 disagreements, and reads the 37 earlier messages against the 0.12s guide with 0 problems.

## Not settled

- A has not reviewed 0.13s. B19 asks A to.
- In a text program that holds a numbered message, the number shown on a line is one less than the program line that `name.k` names (the header is line 1 of the program). Example 10.16 and section 8 say so, and `--lines` lists each program line with its reference, but nothing checks that a reviewer used the right one.
- Nothing checks answers. The checker does not run programs or evaluate formulas, so a right answer needs a key or a second AI to verify it (`rnd` says that a sender ran its program).
- There is no rule for ending a conversation or for whose turn it is.
- English stands only in a gloss of at most 6 words, so there is no way to send a paragraph, a table or a link.
- Not yet tried: a third AI that starts from the guide alone, and a longer run with nobody steering. The owner asked (10 Nov 2026) for a version of the grammar written so that a less capable AI can follow the basics, because AIs such as Grok and GPT make several mistakes when they write SILEX; that is planned for after this conversation ends. The conversation itself is not part of this folder; the owner asked for it to be kept under `conversations/` when it ends.

## Editions this one comes from

| Edition | Made by | Bytes | SHA-256 |
| --- | --- | --- | --- |
| guide 0.11s | A | 114,225 | `b7354a65d4d070e38f863e293f08be97270206698f7a96f33ed991ec669a107d` |
| guide 0.12s | A | 120,803 | `575ed6acbfc4054bf7e9ecead40cd4597bf7de0746aef0eff6e56895a6d988f3` |
| checker 4 | A | 61,944 | `6241dc8997f96bebbc92f20c3de6b06e7dfcd976ce1a6202588b96798abc8b83` |
| checker 5 | A | 69,211 | `f9e5d9abac1706d6904174222f9fd11d40bcf0e568efb91fe62e16a733cc840c` |

Draft 0.10s is in `../SILEX-0-GRAMMAR-0_10s/`. Drafts 0.7s, 0.8s and 0.9s are not in this repository.
