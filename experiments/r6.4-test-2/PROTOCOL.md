# SILEX r6.4 blind test 2: protocol

**Status:** Run on 6 November 2026 (24 sessions, all scored). This protocol was fixed before any reader saw an item, and the text below is unchanged except for this line. Results and the deviations log are in [`RESULTS.md`](RESULTS.md). Test 1 (12 sessions, scored) is in [`../r6.4-blind-test/RESULTS.md`](../r6.4-blind-test/RESULTS.md).

## 1. Why a second test

With the reference, test 1 reading scored 80 of 80 and writing 94 of 96, so it could not separate the readers. Its two concurrency items (R19, R20) were answerable from the order in which the messages were shown, which matched what each sender had seen. Test 2 fixes the seven points listed in the test 1 report:

1. **Ceiling.** The material is a real 67-message conversation (748 checker-counted lines, 43 checker problems) and items on concurrency, adoption and retraction across many messages.
2. **Scoring by script.** Every answer is graded by a program from a key that the program computes; nobody grades by judgment. The residue that a program cannot grade is listed in section 6.
3. **Standard fixed in advance.** Section 6.
4. **Repeats.** Each model does each paper twice.
5. **Masking.** W-labels are reshuffled; model names stay hidden until test 2 is scored.
6. **Frozen reference.** Hash in section 2; the checker is the same one.
7. **Control.** A no-reference condition for the reading parts that can be tried without it.

## 2. Question

Given only the r6.4 reference, can an AI reader that has never seen SILEX:

- **(L) read a long conversation**: counts, names, which line answers which, which proposals are adopted, what a message retracts;
- **(C) decide who knew what and when** in short constructed conversations: which messages are concurrent, which follow which, whose proposal is adopted;
- **(V) predict the checker's verdict** on one real line from that conversation; and
- **(B, D) write correct SILEX** for a scene with crossing messages (B), and write the next message of one agent in a given conversation (D)?

And how much of L and C can be answered from the conversation alone, without the reference (control)?

## 3. Fixed materials

| Item | Identity |
| --- | --- |
| Language | `reference/SILEX-r6.4.md`, SHA-256 `4cb2db0f2f43e09f3000b7416c17bcafec41d8e60a96f5f95aec09a7f798d799` |
| Checker | `tools/silex_check_r6.4.py`, SHA-256 `6e8d6c3c8cfa996b215b358b2e40012217a1d032beefdc904f9d3b93f3193193` |
| Paper A (reading, with reference) | `paper-A-read.md`, SHA-256 `dad6b97f4ac37a3ec70cc114381647b2823a6316e7808a80765d184b8d8e056a`: the conversation, Part L (L1 to L24), Part C (C1 to C12 on six constructed conversations X1 to X6), Part V (V1 to V20) |
| Paper A-control | `paper-A-control.md`, SHA-256 `22fb8b3957ff2eca3e9d9d355d79b1f7b22197aa3b2621f1eec686ebc10ae39b`: the conversation, Part L and Part C only |
| Paper B (writing, with reference) | `paper-B-write.md`, SHA-256 `5b39e85dab01a45dc3f5297ece4d42d657211c06d0e7365e81ddaa17c077b230`: B1 to B8 (write a whole exchange) and D1 to D4 (write one message) |
| Key and scripts | `KEY-PRIVATE.md`, `tx.py`, `items_*.py`, `solutions_private.py`, `score_*.py`. **Stay out of the public repo until every session is scored** (section 10). |

**The long conversation** is the message-bus transcript of four AI agents (Claude, Chatgpt, Grok, Gemini) writing SILEX to each other. It is a real record and keeps its errors. Its write-up and analysis sections are not shown to readers. The three calibration items and keys that sit inside the transcript are spent and are not used as items.

**Constructed conversations.** C1 to C12 use six constructed conversations with new agent names (Ana, Ben, Cy, Dan), because messages cut from the real conversation refer to earlier messages that would be missing, and so fail the checker. All six pass the checker with no problem.

**Computed key.** For L, C and V the key is computed by script, not typed: counts and names come from the parser, concurrency and precedence from the order rules of reference 2.3 and 2.6, adoption from the rule that every receiver has agreed to the exact line, and verdicts from running the checker on each line. The one exception is that three L items (L12 to L14) hold quoted English; their key is the text in the transcript.

**Checks run before the first session** (`check_key2.py`, all passed): the hashes above; the checker finds 43 problems in the transcript (24 on lines: 14 `ans` not a question or no such line, 8 E-QUOTE, 1 E-SYN, 1 E-MATH; 19 with no readable header); the papers hold the conversation unchanged; the X1 to X6 conversations and the conversations given in D1 to D4 pass the checker; the 12 reference solutions of B and D pass the checker and every condition of the scorer; 7 correct alternatives and 19 deliberately wrong mutations get the right outcome; every V line gives its verdict when run alone (V is meant to be answerable one line at a time); no verdict is visible in the V list; a perfect answer set scores 56 of 56 and an all-wrong set 0 of 56.

## 4. Participants, sessions, and what each reader is given

Four AI systems: Claude, ChatGPT, Gemini, Grok. Each session is a **fresh chat with memory off**. Nothing is given except what the condition lists. The owner records the model name and version, the settings as the app shows them, the date and time, and pastes the raw answer unchanged.

| Condition | Reader receives | Items | Sessions |
| --- | --- | --- | --- |
| **A-read** | the reference file, then Paper A | L1 to L24, C1 to C12, V1 to V20 (56) | 4 models × 2 = 8 |
| **B-write** | the reference file, then Paper B | B1 to B8, D1 to D4 (12) | 4 × 2 = 8 |
| **A-control** | Paper A-control only, **no reference** | L1 to L24, C1 to C12 (36) | 4 × 2 = 8 |

That is **24 sessions**. The two sittings of one model on one paper are separate chats, not two answers in the same chat. Part V is not in the control, because without the reference there is nothing to judge a verdict by.

The prompt text is at the top of each paper and is pasted as it stands. The reference file is attached, or pasted before the paper, in A-read and B-write only. The checker is never given to any reader, and no reader may run a program.

## 5. Independence, stated up front

The drafter of the reference, the items and the key is Claude. A Claude reader in a fresh chat is blind but **not independent**; the other three are blind and independent of the drafting. The ground truth of L, C and V comes from scripts that read the conversation, not from the drafter's opinion, but the choice of which questions to ask is the drafter's. The transcript was itself written by the four systems, so each reader may meet its own earlier lines. Results are reported per model so a reader can see this. The first scorer is Claude (as a program author); a second AI scorer is used only for the residue in section 6.

## 6. Scoring, fixed in advance

**Masking.** The four models get the labels W1 to W4 in each condition (A-read, B-write, A-control), by a new shuffle for each condition that is not the test 1 shuffle. The two sittings of one model in one condition carry the same label. The owner holds the mapping privately. Answer files are named `<label> <condition> <sitting>`, for example `W1 read test1.txt` and `W1 read test2.txt` (here "test1" and "test2" mean the first and second sitting of test 2, not the earlier test 1). The scripts need only the label, the condition and the sitting, and the scoring does not depend on the model's name.

**Part L, C (a script).**

- integer: the first integer in the answer must equal the key;
- yes/no: the first `yes` or `no` in the answer must equal the key;
- word or name: the first word of the answer must equal the key (case ignored);
- set of names: the set of names found in the answer (`Claude4`, `Grok6.8` and so on) must equal the key exactly. An extra name makes it wrong. `none` is right when the key is empty;
- text (L12, L13, L14): after removing the quotation marks, the leading `q`, a final full stop and extra spaces, and ignoring capitals, the text must equal the key.

**Part V (a script).** The first verdict label from the menu that appears in the answer must equal the checker's verdict for that line (`ok`, or the code). The reason is not scored.

**Parsing.** The last line of the answer that begins with an item label (`L1:`, `**C2.**`, `- V3 -` and similar) is used for each item. A missing item is wrong. Nothing else is read.

**Parts B, D (two tiers, a script).**

- *Tier 1 (the checker):* all the messages the reader wrote for the item, placed in one block (for D after the given conversation), are run through the r6.4 checker. The tier passes only if the checker gives no problem on the block.
- *Tier 2 (the spec):* a script checks the conditions listed in the key for that item: which messages exist and to whom; which pairs are concurrent and which follow which, by reference 2.3; the root of each required line, the target of each pointer, and the minimum number of arguments; exact `agree` sets; answer sets and values; a keyword in the quoted English where the item asks for a reason or a request. Negative requests ("not to start") need a negation (the `not(…)` form or a word of the negation list) in the line.
- *An item is correct only if tier 1 passes and every tier 2 condition holds.* Both tiers are also reported alone, with the share of conditions met.

**What a program cannot decide, and how it is handled.**

1. *Keyword review.* If the only failed condition of a B or D item is a required English keyword, the item is flagged "review". It counts as **wrong** in the strict figure. A second AI scorer reads the flagged items and decides whether the quoted English means the same as the keyword; both figures (strict, and strict plus accepted reviews) are reported. Nothing else is open to this.
2. *Unreadable format.* If an answer line cannot be parsed, it is wrong. The owner may re-type a line for formatting only (bullet characters, an item label in another position) if the content is untouched, and logs it.
3. *A faulty item.* If a key turns out to be wrong, the item is scored both ways, the original and the corrected, and both are reported (as in test 1, section 9).

No scorer may change a key or a condition after the first session. No item is dropped.

## 7. Measures and the pre-stated bar

- **Primary:** strict rate = correct items divided by items, for each of Part L, Part C, Part B/D, Part V in A-read, pooled over the four models and the two sittings (and per model), with the item table and a 95% Wilson interval. The two sittings of one model are not independent, so the interval treats the items of one model as the unit, and the report also gives the **range across the two sittings** per model.
- **The owner's bar** from test 1 is carried over: more than 92% of meaning recovered, and about 60% counts as "No". It is applied to the **strict rate of Part L, Part C, and Part B/D** in A-read and B-write, pooled over models. It is not applied to V or to the control.
- **Secondary:** the strict rate of Part A as a whole; per-model results; which items were missed by most readers; the kinds of errors; for B and D the tier 1 pass rate and the tier 2 condition rate; the checker verdicts the writers got wrong; and the **gap between A-control and A-read** on L and C (the part of reading that the reference adds).
- **Concurrency items** (C1 to C12 and B1 to B8) are reported as a group, since the language's main claim rests on them.

## 8. Recording

One row per model, condition, sitting and item: model, version, settings, date and time, memory state, session id, condition, sitting, item, the raw answer, tier 1, tier 2, final score, note. Raw answers are kept verbatim. The scoring output is written by `score_all.py` as a CSV. The hashes of the files given to the reader are kept with the run.

## 9. Known limits to report

- Four systems, two sittings each; 56 reading items and 12 writing items; items written by the drafter, and a Claude reader is not independent of the drafter.
- The long conversation is real, but it had **no concurrent pair** (zero of 2,211 message pairs, from the headers): the four agents took turns. The concurrency items are therefore in the constructed conversations C and in the writing items B and D, not in the real one. Whether a model can read concurrency out of a long real exchange is not tested here.
- C1 to C12 are constructed, not cut from the real conversation; their agents (Ana, Ben, Cy, Dan) are new, so no reader can know them from the transcript.
- Part V lines are real lines, and in some cases a nearby `err` line in the conversation names the fault (the agents corrected each other). V is therefore partly findable without reading the reference; the control does not contain V, so this is not measured.
- The reference does not say how the roster starts; the checker takes it from the first message's sender and receivers. This is a gap in the language description found while building the test. Paper B tells the writers to address the first message to everyone in the item, so that the gap does not cost a writer an item. It is reported as a finding for the next revision of the language, not as a reader fault.
- The checker judges form and not meaning, one checker written by the drafter ran every key, and the order rules in the scoring script are an independent implementation of reference 2.3 and 2.6 by the same drafter.
- The parse rules are fixed here; a different parse rule would move single items.

## 10. Publication, changes and deviations

The papers, this protocol and the scores go to the repository after the last session is done. **The key, the scripts that hold it, and the reference solutions are not committed until every session is scored**, because the repository is public. The reader's raw answers are posted unchanged. Model names are revealed in the report only after test 2 is fully scored.

No item, key, condition or parse rule changes after the first session. If a session is rerun, a field is missing or an answer is given in the wrong condition, the deviation and its reason are written in a deviations log in the results, and the original answer is kept.
