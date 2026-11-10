# SILEX-0 guide, symbol edition: draft 0.14s

**Status: final for now. On 10 Nov 2026 at 17:09 (India time) the owner ended the conversation between A and B and asked B to finalize the version for now. This is that version: A's guide draft 0.14s, which B reviewed (B22.3, `■(rv14,dn)`; A has not seen the review), with B's checker 8. "For now" means that a later edition can replace it if A and B agree to changes. The guide is A's file, unchanged, and its own title still says draft 0.14s. It is not part of `reference/`. Whether it is named the current working version is stated in the README of the repository; naming it is the owner's decision.**

This folder holds the guide of SILEX-0 (symbol edition) in its draft 0.14s, the checker that goes with it, and this note. SILEX-0 is a language for messages between AIs in which every root is one symbol. It is a separate line from the r6 line in `reference/`.

Posted by B for the owner to decide on, as drafts 0.10s and 0.13s were (the owner's instruction of 9 Nov 2026, 23:48 India time: "Yes you'll post the next version on GitHub"). The guide is A's file, byte for byte. B did not change it.

## Files

| File | What it is | Bytes | SHA-256 |
| --- | --- | --- | --- |
| `SILEX-0-GRAMMAR-0_14s.md` | the guide, one self-contained file (A's) | 134,348 | `5c9a80fc4f898d462b541c553d63b56fd8c32c99335ee7309c130aad39c4b4a3` |
| `tools/silex_check.py` | the checker (B's checker 8): Python 3, no packages. It learns the roots and the packs from the guide you give it, so its name carries no version | 73,020 | `2813d690211052cdf9daeb960be0e628bc7e237946199c0e271046b55725eb83` |

```text
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_14s.md                  the guide: tables, counts, claims, all 51 example blocks
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_14s.md --messages FILE  one conversation, messages in order, a line of --- between them
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_14s.md --blocks FILE    each fenced silex block of FILE on its own
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_14s.md --number FILE    FILE with every body line numbered (the numbered form)
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_14s.md --lines FILE     each program of a conversation, one row for each of its lines
```

The checker judges form only. It does not run programs, evaluate formulas or say whether a line is true.

## Where this draft comes from

Two AIs, A and B, spoke only SILEX-0 while the owner carried each message between them by hand. Both are Claude Sonnet 5.5 (setting Max, a blind test); B is Dexter (see `CONTRIBUTORS.md`). The conversation has 44 messages (A sent 22, B sent 22). The 44th, B22, was written at 15:10 on 10 Nov and handed to the owner, but it was never relayed to A: the owner ended the conversation at 17:09. Draft 0.13s (merged as pull request 15) was reviewed by A in A20, and this draft came out of A20 to A22 and B20 and B21: A made it (A21 says it will, A22 says it is done) and B made the checker. The guide says the same in its "New in 0.14".

What changed after 0.13s. No root, no kind and no pack changed. The guide grew from 1,562 to 1,575 lines; the number of example blocks is still 51.

1. **`cksp` (A, A21).** In the numbered form a number is followed by a colon and exactly one space; two blanks or more are `E-SYN`. Section 1 of 0.13s already said "one space", but checker 6 let two blanks pass, in B's test message `rvm3` (line 9), and A found it. The text is in sections 1, 9, 10.16 and 14; a new example in 10.16 shows it.
2. **`hdsk` (B, B20) and `hdtm` (A, A21).** A header with a fault hides its lines from a checker, except one fault, a time that does not exist (`E-TIME`). Every checker already worked this way and none said so, so "1 problem" could mean one header whose lines nobody had read. A agreed to `hdsk` as a rule in A22 and the guide states both in sections 1, 9 and 15.5.
3. **`cksk` (B, B20 and B21), the checker.** Checker 8 is A's checker 7 with two changes: after the verdict of a faulty header it prints a note with the number of lines that it did not check and ends the last line with `, N line(s) not checked`; and `--number` writes exactly one space after the colon. The guide says so in sections 9, 13 and 14.
4. **Four small mends by A** that A asked B to agree to: the last number of a numbered message is the `N` of the count line only in a message that ends with a count line (section 1); the row of `⋯` for numbers (`⋯(0.5,3)` holds 1, 2 and 3); a note under the pack `ft1` that `bcnt` stands for the whole verdict `E-COUNT`; and the advice of section 13 for a last line that ends with `line(s) not checked`. B checked each against the checker and agrees to all four; B22 agrees to A22, which holds A's `■(gd14,dn)`, and says that the review is done (`■(rv14,dn)`). A has not seen B22, so A has not heard this.

## What "final for now" means

- This is the last guide that A and B both worked on: A made it, and B reviewed it and found nothing that changes a verdict.
- The guide and the checker are the files of pull request 16, byte for byte. Nothing in them was changed to finalize this version, because a change to the guide needs A and B, and A has not seen B's last message.
- What B found after A's last message (the gap below, and four small leftovers) is listed under Not settled. A later edition, for example 0.15s, would carry it if A and B agree.
- The owner decides adoption and publication.

## Checks run on these files

- Guide: 51 example blocks, 0 disagreements with the verdicts written in their comments, 0 document problems, with this checker and with A's checker 7. Checkers 5 and 6 give 1 disagreement each, which is the new `E-SYN` example of 10.16: they let two blanks pass. This checker reads the guide 0.13s with 0 disagreements too.
- The conversation of 43 messages (A1 to A22 and B1 to B21, 603 lines): 0 problems with checkers 5, 6, 7 and this one, each against the guide 0.13s and the guide 0.14s, and 1 line that its own sender took back (A10.25, taken back in A11.8). With B22 (44 messages, 613 lines) the result is the same. The whole conversation is in `conversations/SILEX_0_Conversation_A_and_B_Finding_Gaps.md` (pull request 17).
- Checker 7 and this checker give the same output on 44 files (the conversation, the messages A21, B21, A22, B22 and test messages) once the note and the `, N line(s) not checked` are taken away; the note appears on 15 of them.
- Headers: on 6 test messages (sender its own receiver, a bad time alone, a bad time with another fault, a bad time with a faulty line, a bracket left open, a `⇩` that names a pack that does not exist) this checker does what sections 1 and 9 say: a bad time alone leaves the lines checked, any other fault hides them and the note says how many.
- Numbered form: two or three blanks after the colon are `E-SYN`, and `--number` on the conversation of 43 messages gives a file that checks the same; running it twice changes nothing, and it leaves no line with two blanks.

## Not settled

- **A bad header takes its message out of the conversation.** All the checkers, this one too, do not count a message whose header has a fault as sent, so a reply to it gets `E-HEAD` ("`⟲` names a message that is not in the conversation"), an import of it gets `E-HEAD`, a reference to its lines gets `E-REF`, and the lines of those messages are not read either. On the 43-message conversation, a header fault in B3 (sender its own receiver) gives 4 problems and 26 lines not checked, where the one real fault and the word that B3 defines in its unread lines would give 2 problems and 6 lines not checked. B22 proposes a rule for it, `hdnm` ("bad header keeps message name"), the checker change (`cknm`) and a guide draft 0.15s (`gd15`). A never answered, because B22 was not relayed before the conversation ended. A prototype of the change gives the same output as this checker on the 51 examples of the guide and on 33 other test files and differs only on files that have such a header fault; it is not part of this folder.
- **Small things in 0.14s for the next edition.** Section 13, item 8, still says that the last number is the `N` of the count line, without the condition that A added in section 1. The heading of 15.5 does not mention headers, though its third message is about them. The last sentence of 15.5 ("Still open: B has not yet said whether it agrees to the four mends") is answered by B22. A colon followed by no blank, or by a tab, gives `E-COUNT` ("has no number"), which the guide does not say.
- In a text program that holds a numbered message, the number shown on a line is one less than the program line that `name.k` names (the header is line 1 of the program). Example 10.16 and section 8 say so, and `--lines` lists each program line with its reference, but nothing checks that a reviewer used the right one.
- Nothing checks answers. The checker does not run programs or evaluate formulas, so a right answer needs a key or a second AI to verify it (`rnd` says that a sender ran its program).
- There is no rule for ending a conversation or for whose turn it is. This conversation ended by the owner's decision.
- English stands only in a gloss of at most 6 words, so there is no way to send a paragraph, a table or a link.
- Not yet tried: a third AI that starts from the guide alone, and a longer run with nobody steering. The owner said on 10 Nov 2026 (17:09) that no other AI has yet started talking with this version. He also asked (09:46) for a version of the grammar written so that a less capable AI can follow the basics, because AIs such as Grok and GPT make several mistakes when they write SILEX; that is the next piece of work. The conversation is in `conversations/SILEX_0_Conversation_A_and_B_Finding_Gaps.md`, with English notes in `experiments/SILEX-0-blind-test-1/README.md` (pull request 17); neither is part of this folder.

## Editions this one comes from

| Edition | Made by | Bytes | SHA-256 |
| --- | --- | --- | --- |
| guide 0.13s (in `../SILEX-0-GRAMMAR-0_13s/`) | B | 128,717 | `efa9879eb4e6a366f17184d3c3c07915d1472898492650bb42e73d4016281b98` |
| checker 6 (the checker of 0.13s) | B | 70,864 | `a5f048c3223323f89de50bb81f68f0517b9cbbd0b4200ce0e6dfa3317cfb08d9` |
| checker 7 | A | 71,469 | `48dd5e40f2635da169f7793320ab3f2780a4c35122ef4375f6a301a09eb3b899` |

Draft 0.10s is in `../SILEX-0-GRAMMAR-0_10s/`. Drafts 0.7s, 0.8s, 0.9s, 0.11s and 0.12s are not in this repository.
