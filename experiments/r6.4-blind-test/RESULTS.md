# SILEX r6.4 blind test: results

**Status:** all 12 sessions run and scored on 6 November 2026. Protocol: [`PROTOCOL.md`](PROTOCOL.md). Reference tested: `reference/SILEX-r6.4.md`, SHA-256 `4cb2db0f2f43e09f3000b7416c17bcafec41d8e60a96f5f95aec09a7f798d799`.

**Reading the labels.** The answers were masked as W1 to W4 **separately in each condition**. W1 in one table is not necessarily W1 in another, so the tables below cannot be read per model, and no model names appear in this report.

## Summary

With the language reference, four AI models read and wrote SILEX r6.4 almost without error; without it, reading fell from 100% to 86%. This was a pilot, and its items were too easy to separate the models.

| Condition | Items fully right |
| --- | --- |
| Reading, with the reference (20 items, 4 models) | 80/80 (100%) |
| Checker verdicts, with the reference (10 items) | 39/40 (97.5%) |
| Writing, with the reference (24 items) | 94/96 (97.9%) |
| Reading, no reference (20 items) | 69/80 (86.3%) |

Without the reference the models still got 15 of 20 items right from the English words alone. They missed the rules the words do not give away: message order and concurrency, counterfactuals, and a claim read as an order.

## Design

Four AI systems each did three fresh, memory-off chats, 12 sessions in all, with the answers masked as W1 to W4 inside each condition.

| Condition | What the AI received | Items |
| --- | --- | --- |
| S-read | the reference, then reading and verdict items | R1–R20, V1–V10 |
| S-write | the reference, then English sentences to write as SILEX | P1–P24 |
| N-read (control) | no reference, only the reading items | R1–R20 |

- **Fixed materials:** SILEX r6.4 (SHA-256 `4cb2db0f…d799`) and its checker `silex_check_r6.4.py` (SHA-256 `6e8d6c3c…3193`).
- **Items:** set on a farm and in a laboratory, not in the reference's own examples, so success cannot come from copying one.
- **Scoring:** reading by meaning against a private key; writing in two tiers, the checker for form, then two scorers for meaning. The AIs never saw the checker.
- **Masking:** the labels W1 to W4 do not link across conditions, and no model names appear in this report.

## Results

With the reference, reading and writing were at or near the ceiling; without it, reading averaged 86%. Each cell is the number of items fully right.

**Reading with the reference**

| | W1 | W2 | W3 | W4 | Pooled |
| --- | --- | --- | --- | --- | --- |
| Reading items fully right (of 20) | 20 | 20 | 20 | 20 | 80/80 |
| Checker verdicts right (of 10) | 10 | 10 | 10 | 9 | 39/40 |

**Writing with the reference.** All 96 answers passed the checker. An item counts as correct only when it also says what the English says.

| | W1 | W2 | W3 | W4 | Pooled |
| --- | --- | --- | --- | --- | --- |
| Items correct (of 24) | 22 | 24 | 24 | 24 | 94/96 |

**Reading without the reference**

| | W1 | W2 | W3 | W4 | Pooled |
| --- | --- | --- | --- | --- | --- |
| Items fully right (of 20) | 16 | 19 | 17 | 17 | 69/80 |
| Points, full = 2, partial = 1 (of 40) | 36 | 39 | 37 | 37 | 149/160 |

On the lenient score (full = 2, partial = 1), reading with the reference scored 160/160 and writing 190/192.

- **The one verdict miss:** W4 gave `E-KIND` for `will(Ben,"restart pump")`; the right verdict is `E-ARITY`.
- **The writing deductions:** W1's P14 made the tomato plants the effect of the frost instead of their death, and W1's P24 made the buyer the one who delivers the grain.

## What the reference adds

The no-reference readers lost 11 of 80 items. Fifteen items (R1–R6, R8–R13, R15–R17) were fully right for all four, so most of the language reads correctly from its words alone. The misses cluster on rules that the words cannot show.

| Item | What the reference settles | Readers short of full credit | What the answers did |
| --- | --- | --- | --- |
| R20 | Concurrent messages: what a sender had seen | W1, W2, W3, W4 | Right answer. "Ana had not read Cy's answer" was justified by display order. |
| R19 | Concurrency, and when a proposal is adopted | W1, W3, W4 | Right or hedged verdict. Ben's ignorance was explained by display order, and W4 did not commit to "not adopted". |
| R7 | A completion claim versus an instruction | W1, W4 | W1 read it as "finish the review by…". W4 left open whether it was a claim or an obligation. |
| R14 | A counterfactual "would" | W3 | Read as a plain conditional outcome. |
| R18 | The sender declines, with both reasons asserted | W1 | Read as the imperative "Reject the repeat assay". |

**Why R19 and R20 matter most.** Every no-reference reader answered R20 correctly, but by the shortcut "her message came first, so she had not read his". That shortcut gives the right answer here only because the items line up. A message shown earlier can still be unseen by a later one, and the reference's concurrency rule (2.3) is what says so. The reference condition read R19 and R20 correctly in all eight answers.

**Size of the effect.** 80/80 against 69/80 is a gap of 11 items, or about 14 percentage points. The control is one sitting per model, so the gap is an estimate, not a tested difference.

## Findings about the language

Four points come out of the answers, and each can be traced to specific items.

- **A checker pass is not a meaning pass.** All 96 writing answers passed the checker, and two still said the wrong thing: W1's P14 made the tomato plants the effect of the frost instead of their death, and W1's P24 made the buyer the one who delivers the grain. Both are errors in who does what, which is the part a form check cannot see. The reference already says this about line numbers: a number that names another existing line is accepted even when it is the wrong one (reference 5.1).
- **Some meanings have more than one valid spelling.** June in P17 was written as `2026-06` by W1 and as `t"June"` by W3. The checker accepts the first, but section 1.6 shows only full dates and times. "Nobody has told the buyer" in P24 was written as a negated finished telling by W3 and as a negated act with a blank doer by W4. The owner ruled these the same meaning, but the language has no single form for either, and a short cookbook line for each would remove the choice.
- **`will` is a repeat trap.** The only verdict miss was W4's `E-KIND` for `will(Ben,"restart pump")`, where the key is `E-ARITY`: `will` takes one place, the sender's own act, and a doer in front of it is an arity error. An earlier two-writer test in the reference (6.9) records a doer in front of `will` twice, and here a reader misnamed the resulting error.
- **The hardest rule to guess is concurrency.** No-reference readers could not recover it, and with the reference all four applied it (R19, R20). The other misses were scattered: R7 by two readers, R14 and R18 by one each.

Whether to change the language for any of these is the owner's call. None of them was a failure of the reference in this test: with it, reading scored 80/80 and writing 94/96.

## Scoring

Two scorers marked the same masked answers: Claude (the drafter) first, then a second AI scorer who saw only the masked answers, the keys and, for the writing set, a short excerpt of the roots. Neither knew which model wrote which answer. Reading items scored 2, 1 or 0 against the key, verdicts 1 or 0, and writing items counted as correct only when they passed the checker and also said what the English says.

**Fully-right cells at each stage**

| | Claude, first pass | Second scorer | After the owner's rulings |
| --- | --- | --- | --- |
| Reading with reference (of 80) | 80 | 79 | 80 |
| Verdicts (of 40) | 39 | 39 | 39 |
| Writing with reference (of 96) | 94 | 90 | 94 (97.9%) |
| Reading without reference (of 80) | 65 | 65 | 69 (86.3%) |

The two scorers agreed on 284 of 296 cells (95.9%) before any ruling. Both with-reference results clear the pre-stated 92% bar: reading at 100% and writing at 97.9% after the rulings, and 98.8% and 93.8% on the second scorer's marks alone. The no-reference result depends on the standard: 65/80 (81.3%) on either first pass, 69/80 after the rulings.

**The owner's ruling.** On the 12 disagreements the owner decided: "If the meanings are same then give full marks. But if the meaning is partial or close but not intended then deduct." That gave full credit in 10 cells (R14, R17, R18 and R19 among the no-reference answers; W1's R14 with the reference; P17 for W1, W3 and W4; P24 for W3 and W4) and a deduction in 2: W4's R19 without the reference (adoption left open, reasoned from order) and W1's P24 (the buyer made the one who delivers).

**Three things to know about how the scores were reached**

- Claude applied the same standard to W1's and W2's R14 without the reference, where both scorers had agreed on 1, so that all four answers to R14 were judged alike. Their answers say neither the finishing nor the low rate is asserted. W3's R14 stays at 1 because it calls the line an asserted conditional outcome. Holding W1 and W2 at 1 would give 67/80 (83.8%).
- Claude's own first pass was not consistent. It scored R14 with the reference as full credit but similar answers without it as partial, and it first gave W1's P17 a 1 and then a 2 after reading W3's answer. Both changes were reported to the owner and logged.
- The first scorer wrote the items and the keys, so it is not independent of them. The second scorer is the check on that, and the cells where they differ are listed in [`results/disagreements.csv`](results/disagreements.csv).

## Deviations and notes (protocol section 9)

1. **Items, keys and rubrics.** By file times, the protocol, papers 1 and 2 and the key were last changed between 08:37 and 08:39 IST on 6 November 2026, before any answer existed, and were not changed afterwards. The no-reference chats used a paste-ready copy of paper 1's reading items, generated from paper 1 by script. The only edit to `PROTOCOL.md` after the runs is its status line.
2. **Scorers.** Section 4 names ChatGPT and Claude as the two scorers. Claude scored first. A second AI scored later from a masked package. Which AI it was is recorded by the owner and not here. For the writing set the package included a short excerpt of the reference (the kinds, 48 root rows, the notes for 3.7 and 3.9, a note on stretches of time, one cookbook line and a note on formulas) so the scorer could judge meaning without the full grammar. Section 5 did not provide for this.
3. **Rulings beyond the disagreements.** Section 5 sends disagreements to the owner. The ruling was also applied to the two no-reference R14 cells where the scorers agreed (see "Three things to know" above). This moves the no-reference total from 67 to 69.
4. **Records.** Section 7 asks for the model name and version, settings, date and time and session id for each run. The owner holds these and the key to the labels. They are not in this repository.
5. **Per-model reporting.** Sections 4 and 6 say results are reported per model. The labels W1 to W4 do not link across conditions, so the tables here are per label within one condition. A per-model table needs the owner's mapping and has not been made.
6. **Not yet published.** The papers, the key, the scoring package and the key-checking script are not committed. Section 10 allows it now that every session is scored. When to publish them is left to the owner.

## Limits

These results show that four models can read and write short SILEX lines correctly when the reference is in front of them. They do not show more than that.

- **Ceiling.** With the reference, reading was 80/80 and writing 94/96. A test this easy cannot rank the models, and it cannot show where the language starts to fail. The owner's own assessment is that the test was not complex.
- **Small and unrepeated.** Four models, one fresh chat per model per condition, twelve chats in all. There is no repeat run, so there is no estimate of how much one model's answer varies from sitting to sitting, and the 11-item gap in the control is an estimate, not a tested difference.
- **Short, single-purpose items.** Reading items were single lines or three-message exchanges, and writing items were one line each from fixed English. Nothing here tests a long conversation, a task that runs over many messages, or a message the writer chose for itself.
- **Not independent of the language.** The items, the keys and the first scoring were written by Claude, and one of the four readers is Claude with memory off. The owner holds the key to which answers are whose, so Claude does not know which are its own. The owner, who ruled on the borderline cells, is also the author of the project.
- **Two AI scorers.** The second scorer is another AI. Its marks and Claude's differ in 12 of 296 cells, and the owner's rulings settled them. The figures depend on that standard, as the 65 to 69 range for the control shows.
- **In-context knowledge only.** The models were given the reference in the chat. The results say nothing about models that have been trained on the language, or about how a reader behaves when the reference is far back in a long context.
- **A checker, not a receiver.** The checker confirms form. No test here has a receiving agent act on a message and fail or succeed at a task.

## What the next test must fix

The next test should be harder, and each point below answers a limit above.

1. **Remove the ceiling.** Use long conversations of ten or more messages, with concurrent replies, proposals that need every receiver to agree, and cases where the order messages are shown in differs from what each sender had seen. R19 and R20 were the items the control missed most often, so they are the model for the new items.
2. **Target the rules that decided this test.** Concurrency (2.3), adoption, counterfactual "would", a bare act read as a claim or as a request, and the places of `will`. Add writing items where the English can be put into the language in more than one way, such as a month with no day and "nobody has told", so that the key lists every accepted form before the test.
3. **Score by what happens, not only by a key.** Add a condition where a receiving agent acts on a message and a task succeeds or fails. That tests meaning in use, which the checker and an answer key cannot.
4. **Fix the scoring standard first.** This time the same-meaning standard was set after the disagreements appeared. Write it into the protocol before the test, with full and partial wording for each borderline item, and have the second scorer check the key before any answers exist.
5. **Repeat and widen.** Run each model in each condition at least twice, so that sitting-to-sitting variation can be measured, and add more models if the owner can run them.
6. **Keep the masking.** Shuffle the W-labels for the new test and keep the model names hidden until it is scored. If Claude is again one of the readers, the same independence note applies.
7. **Freeze the reference.** The results here are for r6.4 with the checksums in the protocol. If the text changes, the next test gets a new hash and these results do not carry over without a re-run.

## Files in this folder

| File | What it is |
| --- | --- |
| `PROTOCOL.md` | The protocol, fixed before the first answer (status line updated) |
| `results/raw/W{1-4}-{S-read,S-write,N-read}.txt` | The 12 answers, verbatim and masked |
| `results/scores.csv` | Claude's first-pass scores, with notes |
| `results/scorer2_raw.txt`, `results/scorer2_scores.csv` | The second scorer's output, verbatim and tabulated |
| `results/disagreements.csv` | The 12 cells where the two scorers differed, with the owner's ruling |
| `results/final_scores.csv` | All 296 cells: Claude's first pass, the second scorer, the final score |
