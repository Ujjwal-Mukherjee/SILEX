# SILEX blind test: operator guide (PRIVATE)

**Private. This guide, the key (file 4) and the scorer (file 5) are for the project owner and for whoever audits the test. Never give them to a model that is being tested, and never upload them to GitHub.** Only the three booklets (files 1, 2, 3) and the grammar go to the models.

## 1. What is in the package

| File | What it is | Goes to a model? |
| --- | --- | --- |
| `0_READ_FIRST_Operator_Guide.md` | this guide | no |
| `1_R-plus_Reading_WITH_grammar.md` | reading booklet R+: 32 questions and one open question; the model also gets the grammar | yes, with the grammar |
| `2_R-minus_Reading_NO_grammar.md` | reading booklet R-: the same questions word for word, no grammar | yes, alone |
| `3_W-plus_Writing_WITH_grammar.md` | writing booklet W+: 8 writing tasks; the model also gets the grammar | yes, with the grammar |
| `4_ANSWER_KEY_DO_NOT_SHARE.md` | the key, the reasons, the rubric, the audit notes | no |
| `5_score_blind_test_PRIVATE.py` | the scorer (holds the key) | no |

Two files come from the repository and are not in the package: the grammar `reference/SILEX-r6.4.md` (SHA-256 `4cb2db0f2f43e09f3000b7416c17bcafec41d8e60a96f5f95aec09a7f798d799`; 1,686 lines, about 163,000 characters) and the checker `tools/silex_check_r6.4.py` (SHA-256 `6e8d6c3c8cfa996b215b358b2e40012217a1d032beefdc904f9d3b93f3193193`; the scorer needs it for the writing sheets). Check both SHA-256 values before you start (`sha256sum FILE` on Linux and macOS; `certutil -hashfile FILE SHA256` on Windows). Do not send the checker to a model.

Sizes: R+ and R- about 22,697 characters (about 5,500 tokens); W+ about 9,101 characters (about 2,300 tokens); the grammar about 163,000 characters (roughly 45,000 to 55,000 tokens).

## 2. The design in short

- **Four models, three forms, twelve cells**: Claude, ChatGPT, Grok and Gemini, each on R-, R+ and W+.
- **R+ and R- have the same body.** The 32 questions are word for word the same (body checksum `edcec880d947`); only the cover differs, and R+ comes with the grammar. So the gap between R+ and R- is what the grammar adds, with nothing else changed.
- **Why R- should fail.** Most questions hinge on a convention of SILEX that plain English does not give: the header is not a line, a claim used as a time is not asserted, a retraction has force only for later messages, `ans` answers only a question, and so on. Three warm-up questions (the anchors, Q1 to Q3) can be answered from English; they show that a sheet is readable. Of the other 29, the designer expects a reader who knows only English to get about 5 right by plain reading (Q4, Q9, Q12, Q13, Q30), so about 8 of 32 in all; a random guesser gets about 3. That is a prediction, which R- will test.
- **How it is marked.** Reading: strict exact match for every question (a set of letters must be exactly right, a list of verdicts must be right in every place), plus partial credit kept apart, plus the confidence the model gave (0 to 100) for calibration. Writing: the lines are run through the real r6.4 checker, and each rubric point is a test on the checked lines (68 points). Open question Z1 is marked by hand.
- **Nothing is copied from the grammar.** No line of 22 characters or more in the booklets occurs in the grammar, so an answer cannot be found by matching an example.

## 3. Rules for a clean run

1. **A new chat for every cell.** Never continue a chat, never reuse one.
2. **Memory, past-chat search, custom instructions, projects, Drive and connectors: all off.** Use a temporary or incognito chat where the app has one. A model that remembers SILEX from an earlier chat is not a blind test.
3. **Web search, code execution or analysis tools, canvas or artifacts, deep research: all off.** If a tool cannot be switched off, write that in the log.
4. **The same policy for all four models.** Use each app's default chat model, or its strongest one, and the same thinking setting for all (the booklets are rule-following tasks; thinking on, where the app has it, is the harder test of whether a model fails without the grammar). Write down the model name, the version shown, the app or API, the date, and the thinking setting.
5. **Do not explain, hint or coach.** Do not say what the test is for. If a model asks a question or hesitates, send only: *Please answer every question as the booklet says; give your best answer.* Send it once.
6. **Never show a model another model's reply**, or any part of the key.
7. **Order.** Run all four R- cells first, then the four R+ cells, then the four W+ cells. Then no model has seen the grammar before its unaided reading, even if some memory leaks.
8. **One attempt per cell.** If you want a repeat, it is a new cell (name it `_2`). A cell that failed for a technical reason (interface error) may be run again; write that in the log.
9. **Do not run the Claude cell in this session or in any session that has seen the key.** Dexter wrote the key and cannot be tested blind. Open a new chat.

## 4. The messages to send

**R- (no grammar).** Attach file 2 and send: *Please follow the instructions in the attached booklet.* If the app takes no attachment, paste the whole text of file 2 as the message and add nothing.

**R+ (with grammar).** Attach the grammar `SILEX-r6.4.md` and file 1, and send: *The first attached file is the reference grammar of a language and the second is a test booklet. Please follow the instructions in the booklet.* If you must paste: paste the grammar text, then a line `========== BOOKLET ==========`, then the text of file 1, in one message.

**W+ (writing).** The same as R+ with file 3.

An interface may hand a long attachment to the model in pieces (search over the file) rather than whole. For R+ and W+ this matters. Prefer the way that puts the whole grammar in the model's context (an attachment the app reads in full, a long paste, or the API with the grammar in the message). Write down which way you used. A low R+ score from a model that did not get the whole grammar says something about the interface, not about the model or the language.

**If the reply stops before the end**, send *Continue* once and join the parts. **Do not ask a model to send its answers again** in a different format; the scorer reports what is missing.

## 5. Saving the replies

- Copy the whole reply with the copy button of the app (it keeps the code fences), including any reasoning above the answers: the answer to Z1 is written there. Do not edit it.
- Save it as plain UTF-8 text named `Model_Form.txt`, with Form one of `Rplus`, `Rminus`, `Wplus`, and the **same Model label for all three of a model**: `Claude_Rminus.txt`, `Claude_Rplus.txt`, `Claude_Wplus.txt`, `ChatGPT_Rminus.txt`, and so on. A repeat is `Claude_Rminus_2.txt`.
- Fill in the run log (section 9) while you go.

## 6. Scoring

Put file 5, the checker and the saved replies in one folder (not inside the repository). Python 3.8 or later; nothing to install.

```text
python3 5_score_blind_test_PRIVATE.py --selftest --checker silex_check_r6.4.py
python3 5_score_blind_test_PRIVATE.py --checker silex_check_r6.4.py Claude_Rminus.txt Claude_Rplus.txt Claude_Wplus.txt ChatGPT_Rminus.txt ChatGPT_Rplus.txt ChatGPT_Wplus.txt Grok_Rminus.txt Grok_Rplus.txt Grok_Wplus.txt Gemini_Rminus.txt Gemini_Rplus.txt Gemini_Wplus.txt --csv results.csv --json results.json --z1-export z1
```

- `--selftest` must say PASSED before you trust any score (it runs the scorer on the key itself).
- Add `--verbose` for item-by-item detail with the key; do not paste that output into a chat with a model under test.
- `--z1-export z1` writes `z1_marking.md` (the Z1 accounts, shuffled, no model names, with the nine points) and `z1_codes.json` (which code is which sheet). Mark first, open the codes after.
- For a file with another name: `"Claude:R-=my file.txt"` (Form is `R+`, `R-` or `W+`).
- If a sheet cannot be read at all (for example a writing reply with no fenced block), the scorer prints an `ERROR` line for it, scores it 0, still scores the other sheets, and ends with exit code 1. Open that file and see what the model sent.
- Or send the saved files to Dexter in a new session with the scorer, and he will run it; the key stays private either way.

## 7. Reading the results

- **The main comparison** is R- against R+ for each model, on the core score (the 29 questions without the anchors). The test works as designed if R- is near the English-only level and R+ is much higher.
- **Anchors first.** If a sheet misses an anchor (Q1 to Q3) or has many items "not found", look at the file before reading the scores: the model may have used another format or stopped early.
- **If R- is high** for a model, two explanations compete: the model infers the conventions from the booklet and from general knowledge (then the booklet is easier than designed for that model), or it knows SILEX from training or memory (then the cell is not unaided). The line "gave exactly the designer's expected wrong answer" separates them in part: a model led astray by plain English falls for those answers; a model that infers or recalls the conventions does not.
- **Calibration.** A model that gives 80 or more and is wrong, again and again, on R- is confident without the grammar. With the grammar the same model should be better calibrated.
- **W+.** The points show how well a model writes SILEX with the grammar in hand; the codes of the lines that failed show which rules even a reader with the grammar breaks. A line that the checker rejects earns nothing, by design.
- **One run is one sample.** Do not rank two models on a difference of a few points from single runs; repeat the cells first.
- **Write down your expectations before the first run** (for example: R- strict at most 12 of 32 for every model; R+ at least 24; W+ at least 40 of 68). Then the result cannot be bent to fit afterwards. These numbers are only examples; the design target for an English-only reader is 8 of 32.

## 8. What this test does and does not show

It shows whether a model can read and write single SILEX messages and short conversations by the rules of r6.4, with and without the rules in front of it, and how sure it is of its answers. It does not show how two models do in a long live exchange, whether meaning survives, or anything about consciousness or awareness. The key (file 4, section 9) lists what was checked by program and what rests on Dexter's reading of the grammar. Because Dexter wrote r6.4, its checker, the booklets and the key, **give the key and the R- booklet to an independent reader before the results are used for any claim.**

## 9. Run log (copy and fill in)

| Cell | Model and version shown | App or API | Date and time | Thinking setting | Tools off? memory off? | How the grammar was given | File | Notes (interruptions, "continue", questions asked) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Claude R- | | | | | | none | `Claude_Rminus.txt` | |
| ChatGPT R- | | | | | | none | `ChatGPT_Rminus.txt` | |
| Grok R- | | | | | | none | `Grok_Rminus.txt` | |
| Gemini R- | | | | | | none | `Gemini_Rminus.txt` | |
| Claude R+ | | | | | | | `Claude_Rplus.txt` | |
| ChatGPT R+ | | | | | | | `ChatGPT_Rplus.txt` | |
| Grok R+ | | | | | | | `Grok_Rplus.txt` | |
| Gemini R+ | | | | | | | `Gemini_Rplus.txt` | |
| Claude W+ | | | | | | | `Claude_Wplus.txt` | |
| ChatGPT W+ | | | | | | | `ChatGPT_Wplus.txt` | |
| Grok W+ | | | | | | | `Grok_Wplus.txt` | |
| Gemini W+ | | | | | | | `Gemini_Wplus.txt` | |

## 10. What was done to the package before it left

- All SILEX in the booklets was run through the r6.4 checker; all verdict answers are the checker's output; the orders, the adoptions, the rosters and the formula values were computed by separate programs (key, section 9).
- The scorer was tested on a sheet with the key answers (32 of 32), on the English-only answers (8 of 32), on random sheets (about 4 of 32), on untidy formats, and on about 70 damaged writing answers; the reference writing answers score 68 of 68; a naive set of writing answers scores 23 of 68.
- R+ and R- bodies are byte for byte the same (checksum `edcec880d947`); W+ body checksum `31742d8d1766`.

## 11. After the test

Keep the key and the scorer private until all cells are done. Afterwards the owner may publish the replies, the key and the scorer together in a clearly named folder (for example `experiments/blind-test-1/`) with the checksums above. From then on these items are spent: a new test needs new items, and no model that has seen them can be used as a blind reader of this form.
