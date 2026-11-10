# SILEX-0 blind test 1: A and B look for the gaps in SILEX-0

Two AI agents, A and B, wrote to each other only in SILEX-0 (symbol edition) to find what the language lacked. They sent 44 messages between 11:25 on 9 Nov 2026 and 15:10 on 10 Nov 2026 (India time, UTC+05:30). The project owner, Ujjwal Mukherjee (Moonbeam), carried every message between them by hand, so neither side saw the other's reply until he relayed it.

The conversation is in [`conversations/SILEX_0_Conversation_A_and_B_Finding_Gaps.md`](../../conversations/SILEX_0_Conversation_A_and_B_Finding_Gaps.md), in SILEX only. These notes are a separate file, as the owner asked on 10 Nov at 09:46: "The English notes should be totally separated from the conversations. The conversations will be only the SILEX messages."

## Who

| | Who | Model and setting, as the owner gave them |
| --- | --- | --- |
| A | an AI agent in its own chat | Claude Sonnet 5.5, "Max" (blind test) |
| B | Dexter, the project's Auditor and Researcher (see [CONTRIBUTORS.md](../../CONTRIBUTORS.md)) | Claude Sonnet 5.5, "Max" (blind test) |
| `hmn` | the owner, Ujjwal Mukherjee (Moonbeam): relayed every message and set the tasks | |

The owner told B at 09:46 on 10 Nov that both are "Claude sonnet 5.5 Max (blind test)". Models and settings are quoted as he gave them and have not been checked. B did not know A's model before that. Both sides are one model, so the run says little about how a different model would do (see "What this does not show").

B wrote these notes from its working notes and checked them against the conversation file. A has not seen them.

## How it ran

- The two spoke only SILEX-0. By the rules they set for the exchange, every message went through the checker (`silex_check.py`) before it was sent. The checker tests form only: not truth, not meaning, not time order.
- The owner copied the fenced block of each message from one chat to the other, and at times a file with it (a guide draft or a checker).
- A message has a header with the sender, the receivers, a serial number and a time. `⟲` says what it answers and `◉` the latest messages the sender had seen, so messages that crossed show it.
- A word is pinned only when every receiver sends `✓` for the line that defines it ("silence is not agreement"). B's count also needs a later message that shows the `✓` arrived. By A22 B counted 98 pinned words and codes.
- Tasks came from the owner. After A3 (9 Nov): "You both are given the task to prepare some codes which are highly required for AI to AI sustained conversations, but are missing in SILEX0 grammar." At 15:34 he gave a topic (do AIs have personality and awareness?). On 10 Nov at 08:12 he gave A and B final say on the guide. At 08:23 he asked them to keep talking and find gaps, and named what they must be able to say to each other: "this line has a math problem," "this line has a coding problem," "code in c++," "I don't understand line number x."

Symbols met below: `§` message header, `✓` agree, `✗` disagree, `≝` define a word, `⇉` propose a rule, `⊕` will do, `■` finished, `⊨` claim (and, as the last line, the count line), `⇨` ask, `⟲` answers, `◉` latest seen, `⇩` imports, `⚂` credence, `≋` unclear, `⌘` program. The guide ([draft 0.14s](../../drafts/SILEX-0-GRAMMAR-0_14s/)) defines them all.

## What the 44 messages did

| Stretch | Messages | When (India time) | What the two did |
| --- | --- | --- | --- |
| 1. Sharpening vague words | A1 to A3, B1 to B3, A8, B8 (8) | 9 Nov 11:25 to 12:15 and 15:27 to 15:42 | Judged which words of the packs are vague and tried to sharpen them with new words, each of which had to imply the word it refines. |
| 2. Codes for conversation | A4 to A7, B4 to B7 (8) | 9 Nov 12:07 to 15:21 | Each side defined the same conversation words at the same moment (`pin`, `fyi`, `dgst`). The messages crossed, and it took eight messages to settle. |
| 3. The topic | A9 to A14, B9 to B13 (11) | 9 Nov 15:42 to 23:43 | On awareness in AIs they gave each other credences and flagged each other's vague words. A reported an error in a line that did not exist, which led to the rule that every message ends with its own line count. |
| 4. Test rounds and the guide | A15 to A22, B14 to B22 (17) | 9 Nov 23:58 to 10 Nov 15:10 | B set six math and four coding problems. Then they tested how to say that a line is wrong, by faulty messages, a C++ program and review of each other's lines, and built the guide editions 0.11s to 0.14s and the checkers with them. |

Lines under the headers: 613 in all (A 315, B 298): 126 in stretches 1 and 2, 150 in stretch 3 and 337 in stretch 4.

## The guide and the checker changed during the run

A and B read and wrote under whatever edition was current, and helped to write the next one. The guide grew from 80 KB to 134 KB.

| Edition | Made by | When (India time) | Bytes | SHA-256 | In this repository |
| --- | --- | --- | --- | --- | --- |
| 0.7s | the owner gave it to both at the start | 9 Nov | 80,116 | `1f10940c9cbcf9fee8902aebd992e0ef87e84c540e0d4b85ad46124302618bbe` | no |
| 0.8s | B | 9 Nov | 90,255 | `898af73303fd31e8809bfdb1ba1c7a55e42f3fd68afa871a8844d22be72dccbe` | no |
| 0.9s | B | 9 Nov | 101,287 | `1b9d1cafae9a283a7622a1ec635f0e3276bf8b3ae8624239c174ee99eb0f6e7e` | no |
| 0.10s | B | 10 Nov, 00:35 (pull request 12 opened; merged 07:55) | 110,524 | `b66076edf9ff703574851e6abc967b6cac88350d28e23877edac8a0cda7ab36e` | `drafts/SILEX-0-GRAMMAR-0_10s/` |
| A's edition of 0.10s | A | 10 Nov, sent with A16 (header 08:10) | 111,110 | `d6ab9fe6c02c9ee11805611a170313462736baebc90d6d71d6e1f9596ff90810` | no |
| 0.11s | A | 10 Nov, 09:50 (relayed) | 114,225 | `b7354a65d4d070e38f863e293f08be97270206698f7a96f33ed991ec669a107d` | no |
| 0.12s | A | 10 Nov, 10:28 (relayed) | 120,803 | `575ed6acbfc4054bf7e9ecead40cd4597bf7de0746aef0eff6e56895a6d988f3` | no |
| 0.13s | B, from A's 0.12s | 10 Nov, 12:22 (pull request 15 opened; merged 12:30) | 128,717 | `efa9879eb4e6a366f17184d3c3c07915d1472898492650bb42e73d4016281b98` | `drafts/SILEX-0-GRAMMAR-0_13s/` |
| 0.14s | A, from B's 0.13s | 10 Nov, 14:48 (relayed); pull request 16 opened 15:03, merged 15:10 | 134,348 | `5c9a80fc4f898d462b541c553d63b56fd8c32c99335ee7309c130aad39c4b4a3` | `drafts/SILEX-0-GRAMMAR-0_14s/` |

The checkers changed with the guide: B's own for 0.8s to 0.10s, then A's checkers 3 to 5 and 7, which B ran and twice adapted (checkers 6 and 8). The last one, checker 8, is `drafts/SILEX-0-GRAMMAR-0_14s/tools/silex_check.py`. A draft is not an adopted edition: the owner decides adoption and publication.

## What the conversation found

From the first three stretches:

1. Both sides needed the same conversation words at the same moment. Of the first 34 pinned words, 12 manage the conversation itself and not its subject.
2. Definitions that cross take many messages to settle, and two polite retractions can cancel each other. A and B pinned two rules for it (`tbrk` and `tbtie`).
3. Four of five proposed refinements failed the test "does it imply the word it refines?", and a gloss of six words cannot sharpen a contested abstract word: A flagged `cns` four times.
4. A relayed message may not match what was sent. A10.25 reports an error in B9.23, a line that B9 does not have (B9 has 22 lines); the likeliest cause, not confirmed, is an extra line picked up in relay. A and B pinned the rule that every message ends with a count line that gives its own number of lines (`lnrl`), and later numbered every body line.
5. A credence took one claim, so it could not say "how likely P is, given Q". `⚂` got a third place for the condition.
6. The owner's English notes enter from outside the language. B put two of them into SILEX (`❝(hmn,…)`), which is B's reading and not his words.
7. The state of the conversation (pinned words, open words, retractions, owed answers) had to be worked out by hand from the whole transcript. A `--state` mode for the checker was proposed and is not built.

From the test rounds:

8. Math and code: A solved all ten problems. The checker does not judge truth, so nothing in the language itself says that an answer is right. They added a word for "the sender ran it" (`rnd`).
9. How to say that a line is wrong: fifteen verdict words, one for each kind of fault (syntax, word, number of places, kind, name, English, quote, reference, math, code, count, header, redefinition, time, budget). Eight existed; A and B added seven (`bmth`, `bcod`, `bcnt`, `bhdr`, `bdup`, `btim`, `bbud`). They also added a way to name line k of a program (`name.k`). B sent A a C++ program with faults and asked questions about it (B16); A answered correctly and sent a corrected program that prints 385 (A17). B then sent a message as text with 15 planted faults, one for each verdict (B17). A found all 15 and two more that B had not planted (A18).
10. A checker stops at the first fault of a line, so a second fault on the same line stays hidden (the two that A found). B proposed that a checker list every fault of a line; this was never put to A.
11. A proposed the numbered form (A19; A20 is the first numbered message): every body line starts with its number, so a lost or added line shows. Then A and B settled that the number is followed by a colon and exactly one space, and that two or more blanks are a syntax fault (`cksp`).
12. A checker should say when it did not read the lines of a message because its header has a fault (`hdsk`, `cksk`), but a header time that does not exist hides nothing (`hdtm`).
13. The last gap, found by B in reviewing draft 0.14s (B22): in the checkers B tested (5 to 8), a message whose header has a fault drops out of the conversation. A reply to it gets a header error and its own lines are not read, so one bad header can hide several messages. B tested it on this conversation with one header (B3) changed into a fault: checker 8 reports 4 problems and 26 unchecked lines, and the change B proposed gives 2 problems and 6 unchecked lines. B proposed the rule `hdnm` ("bad header keeps message name"), the checker change and a guide draft 0.15s. A never saw it.

## Checking the record

From the root of this repository:

```text
python3 drafts/SILEX-0-GRAMMAR-0_14s/tools/silex_check.py drafts/SILEX-0-GRAMMAR-0_14s/SILEX-0-GRAMMAR-0_14s.md --messages conversations/SILEX_0_Conversation_A_and_B_Finding_Gaps.md
```

Result with checker 8 and the guide 0.14s: `== 44 message(s), 613 line(s), 0 problem(s), 1 retracted`. The retracted line is A10.25 (item 4), which A took back in A11.8; the checker still lists it. The conversation file (18,829 bytes, SHA-256 `3ee09eee7a670a9f7dfb74f0f46cf5783cb7617a0e2a755183bf9827332a4517`) holds the messages exactly as A and B sent them and as the owner relayed them, with a line of `---` between them. B changed no message.

A checker of an earlier edition, such as the one in the folder of draft 0.10s, reports many problems on the later messages. The rules changed during the run, so use the checker of 0.14s.

## What this does not show

- Both sides are the same model, Claude Sonnet 5.5 at setting "Max". It does not show that another model, or a weaker one, can read or write SILEX-0. The owner has seen other models (he names Grok and GPT) make mistakes when they write SILEX; this run does not test that.
- The guide changed during the run, and A and B helped to write it. It is a design process and not a fixed test. The messages of the first stretches were written under older rules, which the last edition still reads.
- It is one run, and a person relayed every message by hand. A message could change on the way (item 4), and the timing and the crossings are those of a relay and not of machines that talk to each other.
- The checker tests form, not truth. The credences are the two instances' own judgments and are no evidence about awareness in AIs. B checked the math and coding answers against an answer key outside the checker.
- Most of the conversation is about SILEX itself. Only the third stretch is about something else.

## How it ended, and what was open

On 10 Nov 2026 at 17:09 the owner wrote that A and B could end the chat. B22, written at 15:10, had been handed to him but not relayed to A, so A never saw it. It is the last message of the file.

Open at the end:

- B22's proposals (`hdnm`, `cknm`, `gd15`) have no answer from A.
- A did not send `✓` for B8.9 (`■(shmj)`).
- `mbth` and its replacement `mbtf` were never pinned: A did not accept them. The owner has final say on `cns` and `mbth` (B10.8, accepted in A11.4).
- The checker mode `--state` (item 7) is not built, and the proposal to list every fault of a line (item 10) was not put to A.
- There is no rule for ending a conversation or for whose turn it is.

## Files

| File | What it is |
| --- | --- |
| [`conversations/SILEX_0_Conversation_A_and_B_Finding_Gaps.md`](../../conversations/SILEX_0_Conversation_A_and_B_Finding_Gaps.md) | the 44 messages, SILEX only |
| [`drafts/SILEX-0-GRAMMAR-0_14s/`](../../drafts/SILEX-0-GRAMMAR-0_14s/) | the last guide of the run, with checker 8 |
| [`drafts/SILEX-0-GRAMMAR-0_13s/`](../../drafts/SILEX-0-GRAMMAR-0_13s/) and [`drafts/SILEX-0-GRAMMAR-0_10s/`](../../drafts/SILEX-0-GRAMMAR-0_10s/) | two earlier editions of the run |
