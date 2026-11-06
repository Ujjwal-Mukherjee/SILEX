# SILEX r6.4 blind test 3

How well do four AI models read and write SILEX r6.4, with and without its grammar in front of them? The test ran on 6 Nov 2026, after [test 1](../r6.4-blind-test/) and [test 2](../r6.4-test-2/), which have other items, their own scoring and their own labels. The project owner, Ujjwal Mukherjee, ran each model himself and pasted the replies. Dexter (Claude), the project's Auditor and Researcher, designed the items, wrote the answer key and the scorer, and scored the replies by label. The models were hidden behind the labels W1 to W4 until all scoring was done; the owner gave the names afterwards.

| Label | Model |
| --- | --- |
| W1 | Claude |
| W2 | Grok |
| W3 | ChatGPT |
| W4 | Gemini |

**These labels belong to this test only.** Each test masked its models separately: in test 2, for example, W1 is Grok, W2 Claude, W3 Gemini and W4 ChatGPT. Do not combine tables from different tests by label.

In [REPORT.md](REPORT.md), "the Owner" is Ujjwal Mukherjee and "Dex" is Dexter (see [CONTRIBUTORS.md](../../CONTRIBUTORS.md)).

## The three forms

| Form | What the model does | What it is given |
| --- | --- | --- |
| R+ | reads: 32 multiple-choice questions on SILEX lines and short conversations, plus one open question (Z1) | the reading booklet and the r6.4 grammar |
| R− | the same questions, word for word | the reading booklet only |
| W+ | writes: 8 tasks, 68 rubric points, each reply run through the r6.4 checker | the writing booklet and the r6.4 grammar |

Four models and three forms make 12 cells, one run per cell. R+ against R− shows what the grammar adds. Q1–Q3 are anchors that plain English settles, so "core" counts the other 29 questions.

## Result in brief

Strict scores (exact match). Reading is out of 32, writing out of 68.

| | R− | R+ | W+ |
| --- | --- | --- | --- |
| W1 Claude | 20 | 32 | 68 |
| W2 Grok | 17 | 28 | 59 |
| W3 ChatGPT | 20 | 30 | 66 |
| W4 Gemini | 22 | 29 | 62 (fences put back, see the notes below) |
| Mean | 19.75 | 29.75 | — |

Without the grammar the models scored 17–22 of 32, well above the 8 that the designer had predicted for a reader who knows only English. With it they scored 28–32. The grammar added 7 to 12 items for every model, most of it in the questions on the checker's verdicts (Part E, pooled over the four models: 3 of 24 right without the grammar, 20 of 24 with it). In writing with the grammar the scores ran from 59 to 68 of 68. The test shows a clear gap from having the grammar; it does not show that the language cannot be read unaided.

[REPORT.md](REPORT.md) has the analysis: the parts and items one by one, confidence, the writing errors, and what they imply for a second round.

## Limits

- One run per cell. Run-to-run variation was not measured, so a gap of one to three items between two labels is within what a re-run could change.
- Claude (W1) is of the same family as the author of the items, the key and the rubric, and the key has not been checked by an independent reader. REPORT.md names the items to check first.
- Model versions and modes are not recorded, and whether web search, other tools or a thinking mode were off in each cell is not confirmed (REPORT.md, "Data issues").
- Z1, the open question, was marked by one marker (Dexter), who had seen the accounts with their labels. It is not yet a result.
- The items were meant to be hard without the grammar and were not: 62% strict without it, against a predicted 25% (REPORT.md, "What this means for the design").

## Published after the test

The operator guide, the answer key and the scorer carry the marks PRIVATE and DO NOT SHARE, and the guide says never to upload them to GitHub. That was the rule while the test ran. The test is finished, the guide itself allows publication afterwards (its section 11), and the project owner asked for everything to be put here. The files are published exactly as they were used, which is why the marks are still in them; [SHA256SUMS](SHA256SUMS) lets you check that.

This repository is public, so anyone can now read the items, the key, the scorer and all twelve replies (W1's replies with the grammar match the key on every reading item and every writing point). The items of this test are spent: a model that has seen them is not an unaided reader of this form, and a new round needs new items. Do not give anything from `materials/` or `data/` to a model that is to be tested.

## What is here

```text
r6.4-test-3/
├── README.md        this file
├── REPORT.md        results, analysis and open items (6 Nov 2026)
├── SHA256SUMS       SHA-256 of every file in materials/ and data/
├── materials/       what was used to run and score the test, unchanged
│   ├── 0_READ_FIRST_Operator_Guide.md      design, rules for a clean run, how to score, run-log template
│   ├── 1_R-plus_Reading_WITH_grammar.md    reading booklet R+ (given together with the grammar)
│   ├── 2_R-minus_Reading_NO_grammar.md     reading booklet R− (same questions, no grammar)
│   ├── 3_W-plus_Writing_WITH_grammar.md    writing booklet W+ (given together with the grammar)
│   ├── 4_ANSWER_KEY_DO_NOT_SHARE.md        key, reasons, rubric, audit notes
│   └── 5_score_blind_test_PRIVATE.py       scorer 1.1 (holds the key)
└── data/
    ├── W1_Rminus.txt … W4_Wplus.txt        the 12 replies as pasted, by label
    ├── W4_Wplus_fenced.txt                 W4 W+ with the code fences put back
    ├── orig/W3_Rplus_qblock_only.txt       the question block of W3 R+ as pasted
    ├── results_strict/                     scorer output with every sheet as pasted
    ├── results_lenient/                    scorer output with W4 W+ from the fenced copy
    └── final_results_with_names.csv        the lenient scores with the model names
```

## Versions and checksums

| What | Value |
| --- | --- |
| Reading body (R+ and R−, identical), as printed by the scorer | `edcec880d947` |
| Writing body (W+), as printed by the scorer | `31742d8d1766` |
| Scorer banner `RB-1 / WB-1` | the versions of the reading and the writing body, not the test number |
| Scorer | 1.1 |
| Grammar [`reference/SILEX-r6.4.md`](../../reference/SILEX-r6.4.md) | SHA-256 `4cb2db0f2f43e09f3000b7416c17bcafec41d8e60a96f5f95aec09a7f798d799` |
| Checker [`tools/silex_check_r6.4.py`](../../tools/silex_check_r6.4.py) | SHA-256 `6e8d6c3c8cfa996b215b358b2e40012217a1d032beefdc904f9d3b93f3193193` |

The grammar and the checker are not copied into this folder; the ones in this repository are the files that were used. To check every file in `materials/` and `data/`, run `sha256sum -c SHA256SUMS` in this folder (`shasum -a 256 -c SHA256SUMS` on macOS).

## Scoring it again

Python 3.8 or later; nothing to install. From the repository root:

```sh
cd experiments/r6.4-test-3/data
python3 ../materials/5_score_blind_test_PRIVATE.py --selftest --checker ../../../tools/silex_check_r6.4.py
python3 ../materials/5_score_blind_test_PRIVATE.py --checker ../../../tools/silex_check_r6.4.py \
  W1_Rminus.txt W1_Rplus.txt W1_Wplus.txt \
  W2_Rminus.txt W2_Rplus.txt W2_Wplus.txt \
  W3_Rminus.txt W3_Rplus.txt W3_Wplus.txt \
  W4_Rminus.txt W4_Rplus.txt "W4:W+=W4_Wplus_fenced.txt" \
  --csv rescored.csv --json rescored.json
```

`--selftest` must print `SELFTEST PASSED`. The second command prints the report and writes `rescored.csv` and `rescored.json`, with the numbers of `results_lenient/`. Those files were made from inside their own folder, so their file names start with `../`; run from inside `results_lenient/` (sheets as `../W1_Rminus.txt` and so on, `--csv results.csv --json results.json`, the report redirected to `report.txt` and errors to `err.txt`), the scorer reproduces the stored files byte for byte. Add `--verbose` for item-by-item detail with the key. With `W4_Wplus.txt` instead of the fenced copy the scorer reports an error for W4 W+ and scores it 0, which is what `results_strict/` records.

## Notes on the data

- **Sheets.** `W1_Rminus.txt` … `W4_Wplus.txt` are the replies as the owner pasted them, without the label line he put above each paste. The scorer takes the model and the form from the file name.
- **W4 W+ (Gemini).** The original reply was in code blocks. Pasting lost the fences, and the writing booklet marks only fenced blocks, so `W4_Wplus.txt` scores 0 (see `results_strict/err.txt`). `W4_Wplus_fenced.txt` has each task's lines put back in a fence and nothing else changed. The report uses it: 62 of 68.
- **W2 R+ (Grok).** Q27 was blank in the original reply (confirmed by the owner), so it is scored wrong: 28 of 32.
- **W3 R+ (ChatGPT).** The reply came in two parts, the Z1 account as an attachment and the question block in the message. `W3_Rplus.txt` joins them, account above block; `orig/W3_Rplus_qblock_only.txt` is the question block as pasted.
- **`results_strict/` and `results_lenient/`.** The first scores all 12 sheets as pasted; the second scores W4 W+ from the fenced copy and is the one the report uses. The names refer only to that one decision. The `strict` column inside both files is the exact-match reading score, and `partial` is the partial-credit score kept apart.
- **Z1.** `z1_marking.md` is the shuffled export of the eight Z1 accounts with the nine-point checklist and no model names; `z1_codes.json` says which code is which sheet; `z1_marks.json` holds Dexter's marks (1 or 0 per point).
- **Scorer 1.1.** Version 1.0 required an `err` line for one writing rubric point whose description also allows a plain claim. Version 1.1 removes that hidden requirement, so W2 W+ went from 58 to 59; no other sheet changed.
