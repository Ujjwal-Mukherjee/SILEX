# SILEX r6.4 blind test: protocol

**Status:** Run on 6 November 2026 (12 sessions, all scored). This protocol was fixed before any reader saw an item, and the text below is unchanged except for this line. Results and the deviations log are in [`RESULTS.md`](RESULTS.md).

## 1. Question

Given only the r6.4 reference, can an AI reader that has never seen SILEX:

- **(R) recover the meaning** of SILEX lines and short conversations,
- **(V) predict the checker's verdict** on a line, and
- **(P) write correct SILEX** from English sentences?

And how much of (R) is guessable from the English words in the roots, without the reference? That is the **no-spec control (N)**.

## 2. Fixed materials

| Item | Identity |
| --- | --- |
| Language | `reference/SILEX-r6.4.md`, SHA-256 `4cb2db0f2f43e09f3000b7416c17bcafec41d8e60a96f5f95aec09a7f798d799` |
| Checker | `tools/silex_check_r6.4.py`, SHA-256 `6e8d6c3c8cfa996b215b358b2e40012217a1d032beefdc904f9d3b93f3193193` |
| Reader paper 1 | `paper-1-read.md`: 20 recovery items (R1 to R20), 10 verdict items (V1 to V10) |
| Writer paper 2 | `paper-2-write.md`: 24 production items (P1 to P24), graded in four levels of six |
| Key | `KEY-PRIVATE.md`: meanings, rubrics, reference lines. **Stays out of the public repo until every run is scored.** |

The items use a farm and a laboratory, not the servers and builds of the reference's own examples, so a reader cannot succeed by copying an example. Every reference line in the key was run through the checker (all `ok`; every faulty line in V gives its stated code).

## 3. Participants and sessions

Four AI systems: Claude, ChatGPT, Gemini, Grok. Each run is a **fresh chat with memory off**. Nothing is given except what the condition lists. The owner records the model name and version and the settings as the app shows them, the date and time, and pastes the raw answer unchanged.

| Condition | Reader receives | Items | Sessions |
| --- | --- | --- | --- |
| **S-read** | the reference file, then paper 1 | R1 to R20, V1 to V10 | 4 |
| **S-write** | the reference file, then paper 2 | P1 to P24 | 4 |
| **N-read** (control) | paper 1 only, **no reference** | R1 to R20 | 4 |

That is 12 sessions. A model's three sessions are separate chats. The prompt text is at the top of each paper and is pasted as it stands.

## 4. Independence, stated up front

The drafter of the reference, the items and the key is Claude (Dexter). A Claude reader in a fresh chat is blind but **not independent**; the other three are blind and independent of the drafting. Results are reported per model so a reader can see this. The scorers (ChatGPT and Claude) also took part in developing the language, and this is reported as a limit.

## 5. Scoring

Answers are masked as W1 to W4 (model names hidden) before scoring. Two scorers score every answer independently against the key; disagreements go to the owner.

- **R (recovery):** 2 = every feature in the key's "full" line is right; 1 = the main reading is right and one named feature is missing or wrong; 0 = anything else. The reading must be exact on what is **asserted and what is only mentioned**, on who acts, on negation scope, on quantity and on time. A vague gloss that fits the line and also fits a different line scores at most 1.
- **V (verdict):** 1 = the right verdict (`ok` or the right error code); 0 = otherwise. The reason is recorded and not scored.
- **P (production):** two tiers. **Tier 1** is objective: every line the writer gave is run through the r6.4 checker; the item passes only if all its lines are `ok`. **Tier 2** is meaning: 2, 1 or 0 against the key's required features, by the two scorers. An item is **correct** only if tier 1 passes and tier 2 is 2. Both tiers are also reported alone.

## 6. Measures and the pre-stated bar

- **Primary:** strict rate = items scored 2 (for P: correct) divided by items, for S-read R, S-write P, and N-read R, each pooled over the four models and per model, with the item table and a 95% Wilson interval.
- **The owner's bar** is more than 92% of meaning recovered, and about 60% counts as "No". It is applied to the **strict rate of S-read R and of S-write P**. It is not applied to V or to N-read.
- **Secondary:** lenient score ((2s + 1s) over maximum), per level, per model, the kinds of errors, the V rate, the tier-1 pass rate of P, and the **gap between N-read and S-read** (the part of recovery that the reference itself adds).

## 7. Recording

One row per model, condition and item: model, version, settings, date and time, memory state, session id, condition, item, the raw answer, scorer 1, scorer 2, final score, note. Raw answers are kept verbatim. Hashes of the files given to the reader are kept with the run.

## 8. Known limits to report

Four models and one run each; 20 + 10 + 24 items; items written by the drafter; two scorers who helped develop the language; AI readers only; the checker judges form and not meaning, and one checker written by the drafter ran all the key lines (reference section 6.5); the token counts of the reference are not used here.

## 9. Changes and faulty items

No item, key or rubric changes after the first session. If a key turns out faulty, the item is scored both ways, the original and the corrected, and both are reported; it is not dropped silently. Any other departure (a session rerun, a missing field, an answer given in the wrong condition) is written in a deviations log with the reason.

## 10. Publication

The papers go to the repository after the last session is done. The key goes after scoring is finished. The repository is public, so neither is committed before then.
