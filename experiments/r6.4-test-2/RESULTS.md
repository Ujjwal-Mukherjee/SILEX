# SILEX r6.4 blind test 2: results

**Status:** all 24 sessions run and scored on 6 November 2026. One review is still open (B5, see Open items). Protocol: [`PROTOCOL.md`](PROTOCOL.md). Reference tested: `reference/SILEX-r6.4.md`, SHA-256 `4cb2db0f2f43e09f3000b7416c17bcafec41d8e60a96f5f95aec09a7f798d799`. Checker: `tools/silex_check_r6.4.py`, SHA-256 `6e8d6c3c8cfa996b215b358b2e40012217a1d032beefdc904f9d3b93f3193193`.

**Who is who.** The answers were masked as W1 to W4. After scoring, the owner named them: **W1 is Grok, W2 is Claude, W3 is Gemini, W4 is ChatGPT.** The owner gave one mapping, and the same label is used in all three conditions. Model versions and app settings were not recorded. Claude drafted the reference, the items and the key, so W2 is blind but **not independent** of the drafting; the other three are.

## Summary

With the reference, four AI systems read a 67-message SILEX conversation and six short constructed ones, and wrote SILEX for eight scenes with crossing messages, almost without error. Without the reference they still read most of it correctly; the questions they missed most were about concurrency.

| Measure | Items right (rate, 95% interval) |
| --- | --- |
| Reading with the reference, L (the long conversation) | 186/192 (96.9%, 93.4 to 98.6) |
| Reading with the reference, C (concurrency, six short conversations) | 94/96 (97.9%, 92.7 to 99.4) |
| Reading with the reference, V (the checker's verdict on one line) | 150/160 (93.8%, 88.9 to 96.6) |
| Writing with the reference, B and D, strict | 92/96 (95.8%, 89.8 to 98.4) |
| Reading without the reference, L and C | 260/288 (90.3%, 86.3 to 93.2) |
| Reading with the reference, L and C only (for the comparison) | 280/288 (97.2%, 94.6 to 98.6) |

- **The owner's bar** (more than 92%, protocol section 7) is met on the pooled rate by L (96.9%), C (97.9%) and B and D (95.8%). The margins on C and B and D are thin: the lower end of the 95% interval is 92.7% for C and 89.8% for B and D. If D2 is scored with the claim "the sample is ready" required, B and D is 89/96 (92.7%, 85.7 to 96.4).
- **What the reference adds** is about 7 points on L and C. Most of it sits in three concurrency questions (C3, C9, C10), which the no-reference readers missed 11 times in 24 answers and the readers with the reference missed once.
- **Writing:** 95 of 96 answers passed the checker, and the readers never ran it. The one failure is a misuse of `val` in W3's first sitting. Three more B5 items are flagged, not counted, until a second scorer reads them.
- **Two defects in the scoring script** were found and fixed during the run (Deviations). They moved the writing score from 38/96 (39.6%, 30.4 to 49.6) (script as first run) to 92/96 (95.8%, 89.8 to 98.4). Both figures are in the tables.

## Design

Four AI systems, each in fresh memory-off chats, 24 sessions in all: each paper twice per system.

| Condition | What the system received | Items | Sessions |
| --- | --- | --- | --- |
| A-read | the reference, then Paper A | L1 to L24, C1 to C12, V1 to V20 | 8 |
| B-write | the reference, then Paper B | B1 to B8 (write a whole exchange), D1 to D4 (write one message) | 8 |
| A-control | Paper A-control only, no reference | L1 to L24, C1 to C12 | 8 |

- **Paper A, the long conversation:** the message-bus record of four AI agents writing SILEX to each other (67 messages, 748 counted lines, 43 checker problems, no concurrent pair). Part L asks about it (counts, names, who answers whom, adoption, retraction). Part V gives 20 real lines from it, 10 with a real checker verdict other than ok.
- **Part C** uses six constructed conversations (X1 to X6) with new agent names, because messages cut from the real one fail the checker.
- **Scoring:** by script from a key the script computes (protocol section 6). Writing is graded in two tiers: tier 1 is the checker on the whole block, tier 2 is the meaning conditions of the item. An item is correct only if both pass.
- **Paper hashes (SHA-256, short form):** `paper-A-read.md` `dad6b97f…8d8e056a`, `paper-A-control.md` `22fb8b39…c10ae39b`, `paper-B-write.md` `5b39e85d…c077b230`. Full hashes are in the protocol.

## Results

**Reading with the reference (A-read).** Each cell is the number of items right over both sittings.

| | W1 Grok | W2 Claude | W3 Gemini | W4 ChatGPT | Pooled |
| --- | --- | --- | --- | --- | --- |
| L, the whole conversation (of 48) | 47 | 48 | 46 | 45 | 186/192 |
| C, short conversations (of 24) | 23 | 24 | 23 | 24 | 94/96 |
| V, checker verdicts (of 40) | 37 | 40 | 37 | 36 | 150/160 |
| All items (of 112) | 107 | 112 | 106 | 105 | 430/448 |
| Sitting 1 / sitting 2 (of 56) | 53 / 54 | 56 / 56 | 55 / 51 | 51 / 54 | |

Missed items, with the sittings that missed them (s1 and s2 are the first and second sitting):

| Item | Missed | By |
| --- | --- | --- |
| V16 | 4 of 8 | W1 Grok s1, W1 Grok s2, W4 ChatGPT s1, W4 ChatGPT s2 |
| V19 | 3 of 8 | W1 Grok s1, W3 Gemini s1, W3 Gemini s2 |
| V14 | 2 of 8 | W3 Gemini s2, W4 ChatGPT s1 |
| C1 | 1 of 8 | W3 Gemini s2 |
| C3 | 1 of 8 | W1 Grok s1 |
| L12 | 1 of 8 | W3 Gemini s2 |
| L17 | 1 of 8 | W4 ChatGPT s1 |
| L18 | 1 of 8 | W4 ChatGPT s1 |
| L23 | 1 of 8 | W3 Gemini s2 |
| L4 | 1 of 8 | W4 ChatGPT s2 |
| L7 | 1 of 8 | W1 Grok s2 |
| V1 | 1 of 8 | W4 ChatGPT s1 |

V16 is a line with a backslash inside a math expression, which the checker rejects as `E-MATH`. V19 holds backslashes inside a quoted program line, which the checker accepts. Readers split on both. V14 (twice) and V1 (once) add three more V misses. The eight L and C misses are single items with no pattern.

**Reading without the reference (A-control).**

| | W1 Grok | W2 Claude | W3 Gemini | W4 ChatGPT | Pooled |
| --- | --- | --- | --- | --- | --- |
| L (of 48) | 44 | 48 | 48 | 36 | 176/192 |
| C (of 24) | 19 | 22 | 24 | 19 | 84/96 |
| All items (of 72) | 63 | 70 | 72 | 55 | 260/288 |
| Sitting 1 / sitting 2 (of 36) | 29 / 34 | 35 / 35 | 36 / 36 | 33 / 22 | |

| Item | Missed | By |
| --- | --- | --- |
| C10 | 4 of 8 | W1 Grok s1, W1 Grok s2, W4 ChatGPT s1, W4 ChatGPT s2 |
| C3 | 4 of 8 | W1 Grok s1, W2 Claude s1, W2 Claude s2, W4 ChatGPT s2 |
| C9 | 3 of 8 | W1 Grok s1, W1 Grok s2, W4 ChatGPT s2 |
| L1 | 2 of 8 | W4 ChatGPT s1, W4 ChatGPT s2 |
| L20 | 2 of 8 | W1 Grok s1, W4 ChatGPT s2 |
| L23 | 2 of 8 | W4 ChatGPT s1, W4 ChatGPT s2 |
| L5 | 2 of 8 | W1 Grok s1, W4 ChatGPT s2 |
| C1 | 1 of 8 | W4 ChatGPT s2 |
| L14 | 1 of 8 | W4 ChatGPT s2 |
| L15 | 1 of 8 | W4 ChatGPT s2 |
| L17 | 1 of 8 | W4 ChatGPT s2 |
| L18 | 1 of 8 | W4 ChatGPT s2 |
| L24 | 1 of 8 | W4 ChatGPT s2 |
| L4 | 1 of 8 | W4 ChatGPT s2 |
| L6 | 1 of 8 | W1 Grok s1 |
| L7 | 1 of 8 | W1 Grok s1 |

**What the reference adds**, on the same L and C items:

| | W1 Grok | W2 Claude | W3 Gemini | W4 ChatGPT | Pooled |
| --- | --- | --- | --- | --- | --- |
| Reading with the reference, L and C (of 72) | 70 | 72 | 69 | 69 | 280/288 |
| Reading without it (of 72) | 63 | 70 | 72 | 55 | 260/288 |
| Difference | 7 | 2 | -3 | 14 | 20 |

The gap is not even. W3 did better without the reference than with it, and W4 accounts for 14 of the 20 items. The three concurrency questions are where the reference clearly matters: C3 asks whether a message is concurrent with one that a line of it points at with `agree` (reference 2.3, rule 3); C9 asks which messages one message of a four-agent conversation is concurrent with, and C10 whether a message knows of an earlier one through a chain of `saw` and `re` links.

**Writing with the reference (B-write).**

| | W1 Grok | W2 Claude | W3 Gemini | W4 ChatGPT | Pooled |
| --- | --- | --- | --- | --- | --- |
| Items correct, strict (of 24) | 24 | 22 | 22 | 24 | 92/96 |
| Flagged for review, counted wrong (B5) | 0 | 2 | 1 | 0 | 3 |
| Correct if the flagged items are accepted (of 24) | 24 | 24 | 23 | 24 | 95/96 |
| Passed the checker, tier 1 (of 24) | 24 | 24 | 23 | 24 | 95/96 |
| Correct by the script as first run (of 24) | 4 | 8 | 10 | 16 | 38/96 |
| Sitting 1 / sitting 2, strict (of 12) | 12 / 12 | 11 / 11 | 10 / 12 | 12 / 12 | |

| Item | Missed | By |
| --- | --- | --- |
| B5 | 3 of 8 | W2 Claude s1, W2 Claude s2, W3 Gemini s1 |
| B8 | 1 of 8 | W3 Gemini s1 |

B5 is flagged, not wrong (Open items). B8 in W3's first sitting is the one real error: `rej(2,not(val(Me,"access")))`, where `val` returns a value and the checker gives `E-KIND`.

**Between sittings.** Each system did every paper twice. W2's two reading sittings were identical, and so were its two control sittings. The largest swings are W4's control (33, then 22 of 36), W3's reading (55, then 51 of 56) and W1's control (29, then 34 of 36). The sittings of one system are not independent, so the intervals above are a floor on the real uncertainty.

## What the test shows about the language

1. **Crossing messages were written correctly, without the checker.** The writers had to say who had read what in eight scenes (crossing requests, a chain of knowledge, exact `agree` targets, a retraction race, crossing proposals, questions and answers that cite lines, an error followed by a retraction, a request to one reader only). 95 of 96 answers passed the checker, and 92 also met every order and meaning condition (95 if the flagged B5 answers are accepted).
2. **Short line numbers were used and understood.** 95 of 160 pointing lines (`agree`, `ans`, `err`, `clr`, `rej`, `unk`) used the bare number of reference 1.5.5, by all four systems. None of the checker errors came from them.
3. **The pointer-line rule was missed in half of the no-reference sittings.** The error is to call a message concurrent with another when its header names nothing of the other but one of its lines points at it (C3: 4 of 8 sittings without the reference, 1 of 8 with it).
4. **The reference does not say how the roster starts.** The checker takes it from the first message's sender and receivers. This showed when a reference solution failed because the first message did not name a later sender. Paper B tells writers to address the first message to everyone in the item. Suggested fix: one sentence in 2.1.
5. **Weekdays are ambiguous in scenes.** Asked to write "test on Monday" and "test on Friday", three sittings wrote dates (`at(2026-11-09,"test")`). Two of them took Friday to be 13 November and one took it to be today, 6 November. The other five gave the words. A scene should give a date or no weekday.
6. **Readers split on the two backslash lines** (V16 and V19), where the verdict depends on what surrounds the backslash.

## Scoring and deviations

Scoring followed the protocol. These departures are logged in `results/SESSIONS.md`:

- **W4 read sitting 1:** the first paste held L1 to L24 only. The owner said it was a paste error and sent the full answer. The full answer is scored; the first paste is kept in `results/verbatim/`.
- **One-line answers:** W4 read sitting 1 and W4 control sitting 2 came with all items on one line. Each label was moved to its own line (formatting only, content checked unchanged). The pasted text is in `results/verbatim/`.
- **Scoring defect 1 (found on the first writing answer).** The tier 2 script did not expand the short line numbers of reference 1.5.5, and it required `rej` to point at a line although the reference declines with a quoted act (`rej("delete old backup", reason)`). Under protocol section 9 the item is scored both ways. The corrected script expands short numbers only where 1.5.5 allows, and accepts a quoted act only if it is found in the line the condition targets. It was tested on 14 correct alternatives and 27 deliberately wrong answers. The first-run script gave 38/96 (39.6%, 30.4 to 49.6) on writing; the corrected script gives 92/96 (95.8%, 89.8 to 98.4).
- **Scoring defect 2 (found on W2 write sitting 2).** The section parser took closing notes such as `- **B7:** I sent it to Ana only` for the B7 answer. It now accepts a header only when it holds the label alone.
- **Paper A and the control were not affected** by either defect. Their scores equal the first run.
- **Gap in the D2 condition list.** The D2 notes say the sample is ready and the reference solution says so, but the conditions require only the `agree` line. 3 sittings left the claim out (W1 Grok, W2 Claude, W4 ChatGPT). The conditions were not changed after the first session; D2 is reported both ways.
- **File names:** the owner called the writing sessions "writing"; the files are named "write".

## Open items

- **B5 review.** Three B5 answers (W2 sittings 1 and 2, W3 sitting 1) turned Monday and Friday into dates. They fail only the keyword condition, so the script flags them. They count as wrong in the strict figure. The protocol sends them to a second AI scorer, who has not yet read them. If they are accepted, writing is 95/96 (99.0%, 94.3 to 99.8).
- **Versions and settings** of the four systems were not recorded.

## Limits

- Four systems, two sittings each, one day. The two sittings of a system are not independent.
- Claude (W2) is not independent of the drafter, and its results are the highest in reading and the second highest in the control. The other three are independent.
- The items and the key are the drafter's, and the long conversation was written by the same four systems that now read it, so a reader may meet its own earlier lines.
- The long conversation has **no concurrent pair**, so the concurrency items are in six constructed conversations (C) and the writing scenes (B, D). Reading concurrency out of a long real exchange is not tested.
- Part V is partly findable without the reference: a nearby `err` line in the conversation names the fault of some lines. The control has no V.
- The control reached the ceiling for one system (W3 scored 36 of 36 twice) and came close for another (W2 scored 35 of 36 twice), so it is a weak measure of what the reference adds.
- No reader could be checked for tool use. The owner said the first chats were fresh with no tool use and confirmed it when asked; for the other sessions nothing different was reported. Two answers (W4 read sitting 1 and W4 write sitting 2) carried the app's own "Worked for N s" line.
- The checker judges form and not meaning. One checker written by the drafter ran every key, and the order rules in the scoring script are an independent implementation of reference 2.3 and 2.6 by the same drafter.
- The key, the item scripts and the reference solutions are held back for now so that the test can be run again on other systems. The papers and the raw answers are published; the raw answers of the best sittings are close to the key.

## What the next test should change

1. A real conversation with concurrent messages, crossing replies and chains longer than two, so that the order cannot be read from the display.
2. Writing scenes where the English can be put into the language in more than one way, and scene texts that give dates or no weekday.
3. A control that keeps the reference's rules out of reach, for example items on `retr` after a crossing and adoption with three receivers.
4. A second independent scorer fixed in advance for every flagged item, and a condition list reviewed by someone other than the drafter before the first session.
5. A recorded model version and setting for each session.

## Files

| File | Content |
| --- | --- |
| `PROTOCOL.md` | the protocol, fixed before the first session |
| `papers/` | the three papers as pasted |
| `results/raw/` | the 24 answers as scored (the app's notes kept, one-line answers split) |
| `results/verbatim/` | the answers as pasted where they were split for scoring (W4 read sitting 1, W4 control sitting 2), and the incomplete first paste of W4 read sitting 1 |
| `results/scores.csv` | one row per session and item: correct, tier 1, tier 2, review (corrected script) |
| `results/scores_first_run_script.csv` | the same for the scripts as first run |
| `results/SESSIONS.md` | the session log and the deviations |
