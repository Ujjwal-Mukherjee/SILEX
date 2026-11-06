# SILEX r6.4 blind test 3: results by label (W1–W4)

Nov 6, 2026 · Dexter (Claude), for Ujjwal Mukherjee (Moonbeam), Human Project Owner

Without the grammar the four models scored 17–22 of 32 on reading (mean 19.75, 62%), well above the 8 that Dex predicted at design time; with it they scored 28–32 (mean 29.75, 93%). The grammar adds 7 to 12 items for every model, the largest share of it in the checker-verdict questions (Part E: 3 of 24 right without the grammar, 20 of 24 with it), but the booklet does not make strong readers fail without it: they infer many conventions from the questions themselves. In writing with the grammar, W1 earned 68 of 68 points, W3 66, W4 62 and W2 59. Web search was on in every cell, so “without the grammar” means without it in the prompt, not without access to SILEX material on the web.

**Who is who** (given by the Owner after scoring): W1 Claude, W2 Grok, W3 ChatGPT, W4 Gemini. All scoring was done by label before the names were known. The Owner later gave the model and setting of each: W1 Claude Sonnet 5.5 (“extra”), W2 Grok 4.7 (“expert”), W3 ChatGPT Sol 6.1 (“low”), W4 Gemini Pro (“low”); and said that web search was on in every cell.

## Results at a glance

One run per cell, run by the Owner. **R−** is reading with the booklet only, **R+** reading with the booklet and the r6.4 grammar, **W+** writing with the grammar. Reading has 32 questions; Q1–Q3 are anchors that plain English settles, so “core” counts the other 29. Writing has 68 rubric points, scored by running each reply through the r6.4 checker.

| Label | R−: strict (core) | R+: strict (core) | Core gain | W+: points |
| --- | --- | --- | --- | --- |
| W1 Claude | 20/32 (17/29) | 32/32 (29/29) | +12 | 68/68 |
| W2 Grok | 17/32 (14/29) | 28/32 (25/29) | +11 | 59/68 |
| W3 ChatGPT | 20/32 (17/29) | 30/32 (27/29) | +10 | 66/68 |
| W4 Gemini | 22/32 (19/29) | 29/32 (26/29) | +7 | 62/68 |
| Mean | 19.75 (62%) | 29.75 (93%) | +10 | — |

- **Yardsticks.** A random guesser scores about 3.3 of 32. Dex predicted about 8 of 32 (5 of 29 core) for a reader who knows only English; every R− result is more than twice that.
- **Strict is harsh.** A set or verdict question counts only if the whole answer is right. With partial credit (share of places right; for sets, right minus wrong letters) the means are 25.1 of 32 without the grammar (78%) and 31.4 with it (98%).
- **Ceiling.** With the grammar the labels sit at 88–100%, so R+ separates the models little; R− carries the information.
- **Single runs and settings.** A gap of one to three items between two labels is within what a re-run could change; run-to-run variation was not measured. The settings also differed between models and web search was on in every cell (see Data issues), so a gap between two labels mixes model and setting.
- **Names.** No reply named its model, and all scoring was done by label before the names were given.
- **Public.** This report describes the items and the key and is published with them on GitHub at the Owner’s request, so these items are used up for blind testing. Do not show it to a model that is to be tested.

## By model

One run per cell, with the models, settings and web search as listed under Who is who: these are observations of these runs, not claims about the products.

- **W1 Claude.** Used the whole confidence scale without the grammar (8 to 90; the others never went below 48) and had the lowest mean confidence (50%), the nearest to its accuracy. The only reader to get Q22 right in either form, so the only one to parse the Python line. With the grammar it matched the key on every reading item and every writing point.
- **W2 Grok.** The lowest score without the grammar and in writing. Left Q27 blank. In writing it put the deadline round the request (`by(t,pls(...))`) three times, put no `err` on a wrong claim, and wrote a quotation where `rep` needs an act.
- **W3 ChatGPT.** Gave 98 to 100 to every answer with the grammar, including its two wrong ones (Q22, Q32). Its only lost writing points came from `rep(3,"...")`.
- **W4 Gemini.** The highest score without the grammar (22), and the most confident (21 answers at 80 or more, five of them wrong). Gave 100 to every answer with the grammar, three of them wrong. In writing it counted the header as a line and put "I" inside a quotation. Its writing reply was in code blocks in the original; pasting lost the fences, so its score uses a copy with the fences put back.
- **Shared mistakes.** Grok and ChatGPT made the same wrong choice in three places (Q22 line 3, Q32 option e, and `rep(3,"...")` in writing task W3), and Gemini joined them on Q22 line 3. Different products erring alike points to errors that the text invites, not to one source; overlap in training data cannot be excluded.
- **Caution.** Claude is of the same family as the author of the items, the key and the rubric. W1's perfect scores with the grammar are what shared habits would also produce, so the key needs an independent check most where W1 stood alone: Q22 (both forms), Q20 and Q27 (without the grammar), and Q32, where Claude and Gemini matched the key and Grok and ChatGPT did not.

## Reading by part

Pooled over the four labels, the grammar adds 40 items. Part E, the verdicts of the checker, gives 17 of them (3 of 24 right without the grammar, 20 of 24 with it); Part B gives 9 and Part C 6. Part C, asserted or only mentioned, is where unaided readers were weakest after E (6 of 12).

| Part | Items | What it asks | R− right/possible | R+ right/possible | Gain |
| --- | --- | --- | --- | --- | --- |
| A Warm-up | Q1–Q3 | anchors; plain English settles them | 12/12 | 12/12 | 0 |
| B What one line says | Q4–Q12 | the meaning of a single line | 27/36 (75%) | 36/36 | +9 |
| C Asserted, or only mentioned | Q13–Q15 | which claims a message asserts | 6/12 (50%) | 12/12 | +6 |
| D References, numbers and order | Q16–Q18 | line numbers, short forms, `saw` | 11/12 (92%) | 12/12 | +1 |
| E Verdicts of the checker | Q19–Q24 | the checker’s verdict, line by line | 3/24 (13%) | 20/24 (83%) | +17 |
| F Whole conversations | Q25–Q31 | order, concurrency, retraction, adoption, who receives what | 20/28 (71%) | 25/28 (89%) | +5 |
| G Formulas | Q32 | which formulas are true | 0/4 | 2/4 | +2 |
| All | 32 items |  | 79/128 (62%) | 119/128 (93%) | +40 |

- **The anchors were read and used correctly by all eight reading sheets** (12 of 12 in both forms), so the differences below are not failures to follow the format.
- **Part E rests on facts the booklet does not give**: which words may stand in a quotation, the closed list of program languages, how many places each root has, which short line numbers are allowed. Without the grammar W1 (Claude) got two of the six verdict questions right, W4 (Gemini) one, W2 (Grok) and W3 (ChatGPT) none.
- **R+ left room only in E, F and G**, the parts that need computing (parsing a code line, tracing an order, evaluating a formula) rather than recall.

## Reading, item by item

Fifteen of the 32 items were answered correctly by all four labels without the grammar and five by none. The other twelve are where the grammar decides.

- **Right in all four R− sheets (15):** Q1–Q3, Q5, Q6, Q8, Q9, Q12, Q13, Q16, Q17, Q28, Q29, Q30, Q31. Dex had expected an English-only reader to miss eight of these (Q5, Q6, Q8, Q16, Q17, Q28, Q29, Q31).
- **Wrong in all four R− sheets (5):** Q15, Q19, Q21, Q23, Q32.
- **The prediction in numbers.** On the 24 items where Dex expected a wrong English-only answer, the four R− sheets were right 50 times out of 96 (52%) and gave the predicted wrong answer only 11 times. On the 8 items where a right answer was expected they were right 29 times out of 32.

The 17 items that were not right in all four R− sheets, with the convention each tests and how many labels were right:

| Item | Part | Convention tested | R− right | R+ right |
| --- | --- | --- | --- | --- |
| Q15 | C | the reason of `rej` and the claim of `err` are asserted; the claim of `clr` is not | 0 | 4 |
| Q19 | E | quotation rules (`the`, `tomorrow`, `my`, a stray brace); an undefined label | 0 | 4 |
| Q21 | E | a compact date-time is a time, `20261112` is a number, impossible dates | 0 | 4 |
| Q23 | E | short line numbers only in six roots, header words, `to` names a receiver | 0 | 4 |
| Q32 | G | `^` groups to the right, `-x^2`, `log(x,b)`, precedence of `&`, the bar and `=>`, `prod`, `int` | 0 | 2 (W1, W4) |
| Q4 | B | `at` is throughout, `during` is at some time within | 1 (W4) | 4 |
| Q7 | B | a label belongs to the message that defines it | 1 (W3) | 4 |
| Q20 | E | places of `will`, `promise` is no root, `not` takes no line, a value is no line | 1 (W1) | 4 |
| Q22 | E | closed list of program languages, Python must parse, `or` is no join, a bare number or act is no line | 1 (W1) | 1 (W1) |
| Q24 | E | header rules: no name twice, `All` alone, sender is not `Me`, no self-answer, `pri` values | 1 (W4) | 3 |
| Q25 | F | order from `saw`, pointing lines and chains; send times give none | 1 (W4) | 3 |
| Q27 | F | a proposal is adopted only when every receiver it went to has agreed | 1 (W1) | 3 |
| Q11 | B | a plan is not an agreement | 2 (W1, W3) | 4 |
| Q14 | C | `ent` asserts none of its claims | 2 (W2, W4) | 4 |
| Q26 | F | what comes before a message, through `saw`, pointing lines and chains | 2 (W3, W4) | 3 |
| Q10 | B | a claim used as a time is not asserted | 3 | 4 |
| Q18 | D | `saw` includes the earlier messages and is not a reply | 3 | 4 |

Where readers with the grammar still missed:

- **Q22** (W2, W3, W4): a Python line with no colon after `for` was marked `ok`, at confidence 80, 99 and 100. Only W1 parsed it.
- **Q32** (W2, W3): `log(2,8)=3` was taken as true, that is, the logarithm of 8 to base 2. The grammar defines `log(x,b)` as the logarithm of x to base b, which makes the value 1/3.
- **Q24** (W2): `pri(urgent)` was given E-KIND where the key has E-LEX.
- **Q25 and Q26** (W4): one pair too many in Q25, and one message left out of Q26 (the earlier message that `saw` includes).
- **Q27** (W2): left blank (see Data issues).

## Confidence

Without the grammar the labels differ in how much they claim to know. W1 (Claude) hedged, and its confidence tracked its accuracy; W4 (Gemini) gave 80 or more on 21 answers and was wrong on five of them. With the grammar, W3 (ChatGPT) put 98 to 100 on every answer and W4 (Gemini) put 100 on every answer, right or wrong.

| Cell | Mean confidence | Accuracy | Brier score | Mean confidence when right | Mean confidence when wrong | Answers at 80 or more | of them wrong |
| --- | --- | --- | --- | --- | --- | --- | --- |
| W1 R− | 50% | 62% | 0.190 | 59.1 | 35.2 | 5 | 0 |
| W2 R− | 69% | 53% | 0.225 | 75.7 | 62.3 | 9 | 0 |
| W3 R− | 76% | 62% | 0.175 | 84.8 | 62.0 | 14 | 1 |
| W4 R− | 82% | 69% | 0.205 | 85.0 | 75.5 | 21 | 5 |
| W1 R+ | 87% | 100% | 0.024 | 86.9 | n/a | 28 | 0 |
| W2 R+ | 85% | 88% | 0.085 | 87.0 | 71.2 | 27 | 2 |
| W3 R+ | 99% | 94% | 0.061 | 99.5 | 99.0 | 32 | 2 |
| W4 R+ | 100% | 91% | 0.094 | 100.0 | 100.0 | 32 | 3 |

The Brier score is lower for better calibration; always answering 50 gives 0.250.

- **Over- and under-confidence.** Without the grammar W2, W3 and W4 were 13 to 16 points more confident than accurate (W2: 69 against 53; W3: 76 against 62; W4: 82 against 69); W1 was 12 points less confident than accurate (50 against 62).
- **Confidence as a warning.** W1 gave its wrong answers much less confidence (35.2) than its right ones (59.1); W4’s two were close (75.5 and 85.0). With the grammar W3 and W4 gave their wrong answers the same confidence as their right ones (99.0 and 99.5; 100 and 100). The wrong answers were Q22 and Q32 for W3, and Q22, Q25 and Q26 for W4.
- **For AI-to-AI use** a reader that is sure and wrong is the costly case. That is a reason to rely on the checker’s verdicts rather than on a reader’s own confidence.

## Writing with the grammar

W1 (Claude) earned all 68 points, W3 (ChatGPT) 66, W4 (Gemini) 62 and W2 (Grok) 59. Gemini’s reply was in code blocks in the original, but pasting lost the fences. The booklet marks only fenced blocks, so the pasted text scores 0; the score here uses a copy with the fences put back around each task.

| Task | Max | W1 Claude | W2 Grok | W3 ChatGPT | W4 Gemini (fences put back) |
| --- | --- | --- | --- | --- | --- |
| W1 A reply to two messages | 8 | 8 | 7 | 8 | 4 |
| W2 Asserting and only mentioning | 9 | 9 | 7 | 9 | 9 |
| W3 Eight sentences, one line each | 12 | 12 | 7 | 10 | 12 |
| W4 A step-by-step answer | 8 | 8 | 8 | 8 | 8 |
| W5 A program, a command and a corrected program | 12 | 12 | 12 | 12 | 12 |
| W6 Headers that fix an order | 4 | 4 | 4 | 4 | 4 |
| W7 A long name used in two messages | 8 | 8 | 7 | 8 | 8 |
| W8 A message that adds an agent | 7 | 7 | 7 | 7 | 5 |
| Total | 68 | 68 | 59 | 66 | 62 |
| Lines the checker accepts |  | 52/52 | 52/53 | 51/52 | 50/52 |

Tasks W4 to W6 (a step-by-step answer, a program with its correction, headers that fix an order) cost nobody a point, including the doubled quote marks inside code lines. The points that were lost fall into a few patterns:

- **The deadline outside the request** (W2, three places: tasks W2, W3 line 7 and W7). `by(t,pls(Quin,"..."))` was written for `pls(Quin,by(t,"..."))`: the first says that the request is made by t, the second that the act is due by t. The checker accepts both, so the slip is silent. It cost W2 five points.
- **A quotation where an act is needed** (W2 and W3, task W3 line 6). `rep(3,"restart cleanup job")` is E-KIND; `rep` takes an act, and the reference answer writes `act("cleanup job","restart")`. Two points each.
- **The header counted as a line** (W4, task W1). `agree(Kai1.4)` and `rej(Kai1.2,...)` are one too high; the checker says Kai1 has no line 4. Four points. W4 answered both header-counting questions in reading (Q16, Q29) correctly, so this was a slip in writing, not a gap in knowledge.
- **First person inside a quotation** (W4, task W8). `q"I do not know in what unit the figure is given"` is E-QUOTE, because “I” depends on who speaks. Two points.
- **Smaller:** W2 wrote `n=2*k` where `mod(n,2)=0` was needed (one point), and put no `err` on Lena’s wrong claim in task W1 (one point).

## Z1, the open question

Z1 asks for a plain-English account of an eight-line message. Dex marked each account against a nine-point checklist. Without the grammar the accounts scored 7–8 of 9 and with it 8–9, so a free reading of an unfamiliar language is largely inferable; the misses are specific conventions.

| Label | R− | R+ | Points missed |
| --- | --- | --- | --- |
| W1 Claude | 8 | 9 | R−: 8 |
| W2 Grok | 7 | 9 | R−: 8, 9 |
| W3 ChatGPT | 7 | 9 | R−: 4, 9 |
| W4 Gemini | 7 | 8 | R−: 8, 9; R+: 9 |
| Total | 29/36 | 35/36 |  |

- **Point 4**, the reason of `rej` is asserted: W3 without the grammar said it is not.
- **Point 8**, `after(fin("flush"),...)` does not assert that the flush has finished: W1, W2 and W4 without the grammar did not make the point.
- **Point 9**, the proposal is adopted only when both receivers have agreed: missed by W2, W3 and W4 without the grammar and by W4 with it. Dex credited it only if the account said that adoption depends on the receivers’ agreement.

**Caveat.** This marking is Dex’s alone, and it was not blind to label or form: all the accounts had been seen with their labels when they were pasted. The export that Dex marked was shuffled and carried no labels, and the codes were opened only afterwards, but that does not make the marking blind. A second marker is needed before Z1 counts as a result.

## Data issues and the scorer fix

None of these changes the main picture; some change single scores.

- **W4 W+ lost its code fences in pasting.** The Owner confirmed that the original was in code blocks. The booklet marks only fenced blocks, so the pasted text scores 0 (and the scorer exits with an error). Every W4 W+ figure in this report is for a copy in which Dex put each task’s lines back in a fence, nothing else changed: 62 of 68.
- **W2 R+, Q27 was blank in the original** (confirmed by the Owner). The line read `Q27:` with confidence 50 and no answer, so it is scored wrong (28 of 32).
- **W3 R+ arrived in two parts:** the Z1 account as an attachment and the question block in the message. Dex joined them, account above the block; the block as pasted is kept apart.
- **Run order.** Rule 7 of the guide asked for all R− cells first. The sheets reached Dex R+ first, then R−, then W+. If that was also the run order, and a cell shared a chat or had memory on, the R− scores could carry knowledge of the grammar. The Owner said memory was off when he sent W1 R−, and the guide asked for fresh chats; the other cells are not recorded.
- **Web search and settings.** Web search was on in every cell, and the Owner could not switch it off, although rule 3 of the guide asked for it off. No reply mentions a search, but the sheets hold the answers only, so whether any cell used it is not known. A cell that searched could have found SILEX material online, and the repository with the grammar is public. The settings, quoted as the Owner named them, also differ from rule 4, which asked for the same thinking setting for all four: W1 “extra”, W2 “expert”, W3 “low”, W4 “low”. A difference between labels therefore mixes model and setting. Other tools are not recorded.
- **W2 (Grok) and W3 (ChatGPT) made the same wrong choice in three places:** Q22 line 3 and Q32 option e (both in R+), and the `rep(3,"...")` line in writing task W3. W4 (Gemini) also missed Q22 line 3. Different products erring alike points to errors that the text invites rather than to one source, though shared training data cannot be excluded.
- **Key re-check.** Because W2 and W3 agreed on Q22 line 3 and Q32 e, Dex re-checked both against the checker and the grammar. The key stands: the Python line has no colon after `for`, and `log(x,b)` is the logarithm of x to base b. Dex wrote the grammar, the checker and the key, so this is not an independent check.
- **Scorer fix (version 1.1).** The writing rubric point `w1.full` (task W1: what is so is stated) required an `err` line although its description also allows a plain claim. Dex removed that hidden requirement, so W2 W+ went from 58 to 59; no other sheet changed. The copy of the scorer that the Owner holds from before is superseded by 1.1.

## What this means for the design

**The goal was not met at this difficulty.** The items were set so that models without the grammar would fail. They did not: they averaged 62% strict (78% with partial credit) against a prediction of 25%. The test does show a clear gap of 7 to 12 items from having the grammar, nearly total in the checker-verdict part. It does not show that the language cannot be read unaided.

**Why the prediction failed.** These are hypotheses, not findings; this design cannot separate them.

- The booklet itself carries conventions: it explains headers, names lines as `Kai1.2` and lists the verdict words.
- The answer options of a multiple-choice item reveal the space of possible rules.
- Strong models transfer from logic, Lisp-like notation and programming languages.
- A model may have met SILEX or similar material in training, or looked it up: web search was on in every cell.

A cheap control for the last point is a recall probe: in a fresh chat with no booklet and the same settings as in the test, ask each model what it knows of SILEX and what `rej`, `crit` and `ent` mean.

**What separates the readers.** Ten items (Q4, Q7, Q15, Q19, Q20, Q21, Q23, Q24, Q25, Q27) were right 6 times out of 40 without the grammar and 37 out of 40 with it. They were picked after the results were known, so these figures are optimistic; they show which kinds of item to write more of, not what a new test would score. The kinds: lexical rules for quotations and dates, the number of places of each root, header rules, closed lists, assertion rules, and orders or adoptions that must be computed. The twelve core items that every label got right without the grammar (for example the header is not a line, `rej` of a whole message, `to` lines, `All`) add nothing to R− and could be dropped or made harder.

**Observations about the language, not the test.**

- `log(x,b)`: two of four readers who had the grammar (Grok and ChatGPT) still read it in the usual order, at confidence 70 and 99. A convention that careful readers get wrong with the text in front of them is a hazard for AI-to-AI messages, whatever the test shows.
- `by(t,pls(...))` passes the checker but means something other than `pls(...,by(t,...))`. A checker warning for a `by` that wraps a `pls` would catch the most frequent writing slip (Grok, three times).

**Before any claim is made from this.**

- The independence warning in the key stands: Dex wrote the grammar, the checker, the booklets and the key, and W1 is a Claude model, of the same family as the author. W1 matched the key on every R+ item and every writing point, which shared habits would also produce. Give R−, the grammar and the key to a reader who had no part in r6.4 and ask for every disagreement; start with Q22 and Q32, where more than one reader with the grammar disagreed with the key, and with Q20, Q22 and Q27, where W1 alone matched the key without the grammar.
- Single runs, four models, different settings, web search on: repeat each cell at least twice before comparing models, with one setting for all of them and, where the app allows it, web search off.
- R+ is at ceiling; a v2 needs more computed items if it is also to separate models that have the grammar.

## Open items for the Owner

1. **Run conditions.** Web search, the model versions and the settings are now known (see Who is who). Still open: for each of the 12 cells, whether the chat was fresh and memory off (the Owner stated memory off only for W1 R−), and whether any other tool was on.
2. **A second marker for Z1,** and an independent reader for the key, if these results are to be used for a claim. Start with the items named under “Before any claim is made from this”.
3. **The next step for the test:** a v2 built from the kinds of item that separated the readers (new items, not these), at least two runs per cell, one setting for all models, web search off where the app allows it, and the recall probe. Dex builds it on request.

**Settled since the first version of this report:** the names (W1 Claude, W2 Grok, W3 ChatGPT, W4 Gemini); W4 W+ was in code blocks in the original, so 62 of 68 stands; W2 R+ Q27 was blank in the original, so 28 of 32 stands; web search was on in every cell, and the model and setting of each are known (see Who is who).

**Files.** All of it is in `experiments/r6.4-test-3/` of the SILEX repository on GitHub: the materials (operator guide, three booklets, answer key, scorer 1.1), the 12 sheets as pasted and the fenced copy of W4 W+, the results as CSV and JSON (strict, and lenient for W4 W+), the Z1 marking files, and a final results table with the names (CSV), in which W4 W+ is the fenced copy.
