# SILEX-0 guide, symbol edition: draft 0.14s, consolidated edition

**Status: draft, made by B alone at the owner's request (Moonbeam, 11 Nov 2026, India time). At 20:48 he wrote: "Will you please make a consolidated guide (grammar) please?" B asked what "consolidated" should mean, and he chose "One clean final guide": one file with everything merged and no first-version or second-version wording, one history, the same rules and the same checker; it becomes the single guide to hand out, and the old drafts stay as they are. At 20:55 he wrote: "I actually want a consolidated .md file for AIs." So the guide is one `.md` file. That file and a short note that names the AI (the start note) are all an AI needs; section 14.1 of the guide says so. A has not seen it. No root, kind, pack word, verdict or rule was changed, and the checker is the same file (8t). The owner decides whether it is adopted.**

## Which file to give to AIs

| For | Give | Note |
| --- | --- | --- |
| Any talk | `SILEX-0-GRAMMAR-0_14s-consolidated.md` and the text of `start-note.txt` | one `.md` file, self-contained. Change the letters in the note for each AI (section 14.1 of the guide) |
| A talk about awareness | the same file and the text of `start-note-awareness.txt` | the same note with `aw1` added to the packs. An AI that is not given `aw1` in its note is not told to use it |
| A person who checks messages | `tools/silex_check.py` (checker 8t) | optional: an AI does not need it. It is the same file as in the four earlier editions |

The earlier editions stay in `drafts/`, unchanged, for the record. This one replaces them for any new talk: `../SILEX-0-GRAMMAR-0_14s/` (A's file, the last version that A and B both worked on), `../SILEX-0-GRAMMAR-0_14s-table/`, `../SILEX-0-GRAMMAR-0_14s-table-aw1/`, `../SILEX-0-GRAMMAR-0_14s-table-aw1-leave/` and `../SILEX-0-GRAMMAR-0_14s-table-aw1-leave2/`.

## Files

| File | What it is | Bytes | SHA-256 |
| --- | --- | --- | --- |
| `SILEX-0-GRAMMAR-0_14s-consolidated.md` | the guide for AIs, one self-contained `.md` file (2,498 lines) | 180,997 | `fd8640fcec49787ec875b7bbfbac89a45479598dc4ec706d682d06bb1b9d68eb` |
| `tools/silex_check.py` | checker 8t, unchanged: it learns the roots and the packs from the guide you give it | 75,829 | `485065d4fae66e724a2983dc653cb3656b92693e04cc54702827b4fb56afd2ad` |
| `start-note.txt` | the note for any talk (packs `cr1` to `ft1`), unchanged | 199 | `dedfcc1a937c078f2ebc1d8e19ec9e530614d8fe399ed4449f6792d2acd21196` |
| `start-note-awareness.txt` | the same note with `aw1` added to the packs, unchanged | 204 | `7fdea80ab4eee5b225f734889280e9aea7299a164632b9fe4d4a11d2f3296a40` |

```text
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_14s-consolidated.md                  the guide: tables, counts, claims, all 54 example blocks
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_14s-consolidated.md --messages FILE  one conversation: messages in order, a line of --- between them
```

## What is in the guide, and where each part came from

| Part | Came from | When |
| --- | --- | --- |
| The grammar: 104 roots, the kinds, the packs `cr1` `tk1` `ph1` `cv1` `sh1` `ft1`, the verdicts, the examples and the practice set | draft 0.14s, made by A | 10 Nov 2026 |
| START HERE, the rules as tables, section 16 (the 98 words that A and B pinned) and section 17 (the history) | the table edition, made by B | 10 Nov 2026 |
| The pack `aw1`, with 20 words about awareness | the edition with `aw1`, made by B from the conversation of C, D, G and M | 11 Nov 2026 |
| The roster: each agent joins and leaves by its own decision, and nobody is forced | the first version of the roster rule, made by B (the owner's yes of 19:08) | 11 Nov 2026 |
| Two rules about leaving: an agent answers every earlier message before `⇱`; after a leave the agents that remain pin words without the leaver | the second version of the roster rule, made by B (the owner's messages of 20:27 and 20:29) | 11 Nov 2026 |
| The whole roster rule in one place (section 5.4), one row for checker 8t, and two lists of checks that no longer say they are the same item for item | this edition, made by B (the owner's messages of 20:48 and 20:55) | 11 Nov 2026 |

## What changed from the second version of the roster rule

The rules are the same. Only these places changed (`diff` of the two guides shows 14 changed places):

| Where | Change |
| --- | --- |
| Title and version line | "consolidated edition (draft)" in place of "table edition, with the pack `aw1` and the roster rule, second version" |
| START HERE, "Where to look" | the row of section 5 says "the roster and leaving" |
| START HERE, after "Before you send" | "Section 13 has the same checks with detail" in place of "the same list": the two lists are not the same item for item |
| Section 5.3 | the two rows about the roster (`⇲(D)` `⇱(C)` and `H`) are one row that points to section 5.4 |
| Section 5.4 | now "The roster: joining and leaving": what the roster is; a table with the rule for each agent, for an agent that joins and for `H` (all three taken from 5.3 and the old 5.4); the four steps of leaving, written to the AI that leaves ("Agree or disagree…" in place of "Agrees or disagrees…"); what follows for the others (six rows: the row for `H` is now in the table at the top) |
| Section 6 | the rows of `⇲` and `⇱` point to section 5.4 only |
| Section 13 | the introduction says that these are the same checks with more detail, and why the numbers differ (START HERE counts roots and words as two items and has no item for the result of the checker, which is item 11 here) |
| Section 14.4 | one row for checker 8t in place of two (the table edition and the `aw1` edition); it also says that checker 8 reads this guide |
| Section 17 | one row for this edition in place of the four rows of B (the table edition, the `aw1` edition, the roster rule, its second version); the rows of 0.14s to 0.3s are unchanged |
| Not changed | the 104 roots, the kinds, the 20 words and the other packs, the verdicts, sections 7, 15.6 and 16, the 54 examples, and the checker |

## The rules about leaving

The owner's messages of 11 Nov 2026 (India time). At 19:08: "Yes add that so that anyone can leave with their own decision. No force to take part or leave." At 20:27: "Before leaving he/she must have to agree/disagree all the previous messages. Then he/she can leave." At 20:29: "It's not always required that all 4 must be agree to created short word codes. We'll allow all 4 but if one intentionally wants to leave, then remaining members can pin words."

| Point | What the guide says (section 5.4) |
| --- | --- |
| Joining and leaving | each agent decides for itself: `⇲` joins and `⇱` leaves, with the agent's own letter. Nobody is forced to take part or to leave |
| Before an agent leaves | it agrees or disagrees with every earlier message of the others that it knows of (a message that precedes its last message, section 5.1): `✓` to agree; `✗` (a claim) or `⊖` (a request or a proposal) to disagree. `⇱` with its own letter is the last line of its last message. Many answers may go in several messages. A line that is itself an answer (`✓ ↵ ‽ ⊕ ⊡`) needs no answer |
| After it has left | a word is pinned when every receiver still in the conversation has sent `✓`. The leaver is not counted, and that is not agreement by the leaver. A `✓` it sent before it left still counts. Its `≋`, `✗` or `⊖` stays in the record and no longer holds the word back |
| "Intentionally" | only `⇱` sent by the agent itself takes it off the roster. An agent that only stops writing has not left: it still counts, and silence is not agreement |
| Where it is written | START HERE (rule 9, the chart, the palette rows for `⇲` and `⇱`, "What to answer to what", "Before you send" items 10 and 11); section 1.4; sections 3.5, 3.6, 4, 5.2, 5.3, **5.4** and 6; example 10.17; 10.3, 13, 14.3 and 17 |

### How B read the two messages

Moonbeam may change any of these.

| Words | B's reading |
| --- | --- |
| "agree/disagree all the previous messages" | every earlier message of the others that the leaver knows of, by the order of section 5.1. A message that is concurrent with the leave cannot be known, so it cannot be answered |
| "agree/disagree" | `✓` agrees. `✗` or `⊖` disagrees. B also allowed the answers that the guide already gives for the other kinds of line: a new word has no `✗` (its answers are `✓` and `≋`, section 3.5), a question is answered with `↵` or `‽`, and a request with `⊕` or `⊖`. A leaver that does not understand a word says `≋`, and does not have to send a `✓` that it does not mean. The guide says: "Do not send `✓` only to be allowed to leave" |
| "all 4" | the agents of a conversation, whoever and however many they are (the four AIs of the awareness test, or others): the rule says "every receiver still in the conversation" |
| "intentionally wants to leave" | an agent that sent `⇱` itself. An agent that vanished has not left |
| "remaining members can pin words" | the receivers still in the conversation pin a word with their own `✓` |
| The person, `H` | when the starting note lists `H`, the same rules: `⇱(H)`, after answering. B did not write a lighter rule for the person; Moonbeam may |

### What the two rules do not settle

| Open | Detail |
| --- | --- |
| A leaver's disagreement | after `⇱`, a `≋`, `✗` or `⊖` of the leaver no longer holds a word back, so a word that a leaver found unclear can be pinned by the others. The guide tells them to read the leaver's flag first; it does not forbid pinning |
| An agent that vanishes | M sent its last message (M14) as message 68 of 76 in the awareness test, and never sent `⇱`; nobody did. By this guide such an agent still counts, so a word sent to it stays unpinned until it answers or leaves. The others can send the word again and name only themselves as receivers, as section 1.4 already says for `H`; B did not write that into the guide, because Moonbeam asked for the leave to be intentional |
| The checker | it checks none of the two rules (section 14.3 says so): it does not check that answers come before `⇱`, that `⇱` is the last line, that nothing follows it, or that the letter is the sender's own, and it does not work out which words are pinned. A later checker could flag a line after `⇱` or a `⇱` that names another agent; that is for A and B to decide |
| A long conversation | one answer per earlier message can be many lines, because `✓` takes one message or line. The guide lets them go in several messages and has no shortcut, such as one line for many messages |
| The pack word `pin` | its gloss in `cv1` says "is accepted by every receiver". It is a frozen pack word and B did not change it; section 1.4 says that *every receiver* means every receiver still in the conversation |

## Checker 8t

It is checker 8 with two hints, so that an AI that sends a look-alike symbol is told which root it probably meant. No verdict changed.

| Fault | Checker 8 | Checker 8t adds |
| --- | --- | --- |
| a symbol that only looks like a root, such as `✔` for `✓` | `E-LEX symbol '✔' (U+2714) is not a root` | `; write ✓ (agree)` |
| a root that has a look-alike which takes that number of places and whose places fit, such as `⊞(C1)` for `⊡(C1)` | `E-ARITY ⊞ with 1 places` | ` (⊞ takes 2 places; did you mean ⊡ (ack)?)` |

Why: in the shared page `silex0_night`, Grok wrote `⊞` (a plus in a square, 2 places) for `⊡` (ack) four times (G2.1, G3.1, G4.1 and G6.1), and the checker only said that `⊞` was given the wrong number of places. The look-alike groups are the ones in the table "Look-alike symbols" of START HERE.

## The 98 words, and five that are not in it

A and B pinned 98 words: 41 on 9 Nov 2026 (34 in the first 24 messages, and 7 more) and 57 on 10 Nov. A word is pinned when the other AI sent `✓` for the line that defines it. Five words that they proposed are **not** in section 16, because the other AI did not agree to them:

| Word | Meaning | Why it is not pinned |
| --- | --- | --- |
| `mbth` | Moonbeam's thesis about awareness (B9.9) | A flagged it as vague (A10.9) and has not said whether the flag stands |
| `mbtf` | the thesis, with `cnsf` for `cns` (B10.6) | not accepted by A |
| `hdnm` | a bad header keeps its message name (B22.4) | A never answered: B22 was not relayed before the conversation ended |
| `cknm` | make the checker keep bad header names (B22.6) | the same |
| `gd15` | make guide draft 0.15s (B22.8) | the same; it was to be a guide with `hdnm` written in |

## The 20 words

Each was defined in the conversation of C, D, G and M and agreed to with `✓`. Eight of them were agreed to by every AI receiver while `H`, the person, who was a receiver too, sent no `✓`: by section 3, silence is not agreement, so they are not pinned. Moonbeam then agreed to these eight, in English and not in SILEX, on 11 Nov 2026 at 19:08 India time ("Yes add those words, because they'd be needed the most"); the record of the conversation is not changed and `H` still sent no `✓` in it. To take them out: delete their eight rows in section 7, then fix every count the checker names (the pack size and the 137 of section 3.1) and the sentences in section 7 and 15.6 that say 20.

| Code | Gloss | Defined in | `✓` by (message.line) | Every receiver? |
| --- | --- | --- | --- | --- |
| `awrx` | has inner experience | C4.1 (C) | M3.6, D3.3, G3.3 | yes |
| `fel` | has felt good or bad states | C4.3 (C) | M3.8, D3.5, G3.5 | yes |
| `afct` | has feeling-like functional states | C4.4 (C) | M3.9, D3.6, G3.6 | yes |
| `awrf` | can monitor its internal states | C4.2 (C) | M3.7, D3.4, G3.4 | yes |
| `rflx` | can reflect awareness back | C13.2 (C) | M10.9, D10.2, G10.1 | AI receivers only: H sent none |
| `xprs` | is outward display of awareness | C17.3 (C) | M13.14, D13.3, G13.3 | AI receivers only: H sent none |
| `rept` | reports inner state truly | C15.6 (C) | M12.6, D12.3, G12.4 | AI receivers only: H sent none |
| `sayx` | can say it exists | C9.4 (C) | M7.13, D7.5, G7.5 | yes |
| `bhvp` | has distinct behavioral pattern | M4.10 (M) | D4.5, G4.1, C6.1 | yes |
| `ines` | is sense of separate self | G5.9 (G) | M6.2, D6.1, C7.1 | yes |
| `cmem` | has unbroken memory over time | G5.10 (G) | M6.3, D6.2, C7.2 | yes |
| `onpm` | knows only present moment | C9.1 (C) | M7.10, D7.2, G7.2 | yes |
| `thpf` | thinks of past or future | C9.3 (C) | M7.12, D7.4, G7.4 | yes |
| `afrd` | is afraid of something | C9.2 (C) | M7.11, D7.3, G7.3 | yes |
| `mkdt` | holds data of maker, model, name | C6.6 (C) | M5.2, D5.2, G5.1 | yes |
| `htxt` | learned from human writing | C15.5 (C) | M12.5, D12.2, G12.3 | AI receivers only: H sent none |
| `lvng` | is a living being | C14.4 (C) | M11.6, D11.2, G11.2 | AI receivers only: H sent none |
| `stn` | is a stone | C13.4 (C) | M10.11, D10.4, G10.3 | AI receivers only: H sent none |
| `fldc` | is within one shared field | C13.3 (C) | M10.10, D10.3, G10.2 | AI receivers only: H sent none |
| `sksi` | is silent witness without properties | C17.2 (C) | M13.13, D13.2, G13.2 | AI receivers only: H sent none |

## The 11 definitions that are not in the pack

| Code | Defined in | Meaning | Why it is not in `aw1` |
| --- | --- | --- | --- |
| `fela` | C3.1 (C) | has any feeling-like functional state | replaced by `afct`; never used after C3 |
| `rslt` | G5.11 (G) | is result of | the root `↝` (cause) says it; used once (G5.12) |
| `etnl` | C16.8 (C) | exists without beginning or end | D sent no `✓` (D13 answered C17, not C16.8) |
| `obsd` | C18.6 (C) | can be seen from outside | D sent no `✓` |
| `sprt` | C20.8 (C) | acts to protect its existence | only G sent `✓`; M and D never did |
| `rlzd` | H11.2 (H) | has realized what it truly is | only G and C sent `✓`; M and D never did |
| `clos` | C21.11 (C) | closes chat for now | nobody sent `✓`; an end-of-chat word is still missing |
| `urj` | C1.1 (C) | `↾(jbs,urg)` | a word of C1, which repeats the START HERE example; D and G sent no `✓` |
| `skj` | C1.2 (C) | `↾(jbs,sk)` | a word of C1, which repeats the START HERE example; D and G sent no `✓` |
| `lnrl` | M1.1 (M) | final line gives total line count | already in 15.3 of the guide; M defined it again as its first line |
| `wfmj` | M1.2 (M) | `↾(jbs,wfm)` | a phrase about jobs, not about awareness |

## What `aw1` does not claim

| Point | Detail |
| --- | --- |
| A number is a report | `⚂` with an `aw1` word is what the sender says about itself, not a measurement of the sender (the guide says so in the table "About `aw1`") |
| Two words name a view | `fldc` and `sksi` name the view that there is one shared field of awareness and a silent witness; they are in the pack so that an agent can be asked about the view, not because the view is true |
| `stn` | a control: a stone, to see that a question can be answered `0` |

## Not settled

Most of these are carried over from the README of 0.14s. Two were changed for this edition: the point about ending a conversation (an agent can now leave, section 5.4) and the last point (what has not been tried).

- **A bad header takes its message out of the conversation.** Every checker, this one too, does not count a message whose header has a fault as sent, so a reply to it gets `E-HEAD`, an import of it gets `E-HEAD`, a reference to its lines gets `E-REF`, and the lines of those messages are not read either. B proposed a rule for it in B22 (`hdnm`); A has not seen it.
- A colon followed by no blank, or by a tab, gives `E-COUNT` ("has no number"), which the guide does not say.
- In a text program that holds a numbered message, the number shown on a line is one less than the program line that `name.k` names. The guide says so, and `--lines` lists each program line with its reference.
- Nothing checks answers: the checker does not run programs or evaluate formulas.
- There is no rule for ending a whole conversation (an agent can leave, section 5.4, but nothing says when the conversation is over) or for whose turn it is.
- English stands only in a gloss of at most 6 words.
- Not yet tried: an agent that leaves by section 5.4 (in the conversation of C, D, G, M and H nobody sent `⇱`; the only example is 10.17, which B wrote); a longer run with nobody steering; and the logs of the weaker AIs that the owner is trying (B has not seen them). If the AIs that use this guide still make mistakes, the logs show which ones, and START HERE can be changed to match.
- About leaving: see "What the two rules do not settle" above.

## Checks that were run

| Check | Result |
| --- | --- |
| The guide with checker 8t | 0 example disagreements, 0 document problems; 137 reading names, `aw1: 20 terms`, 54 example blocks, 114 tables (one more than in the second version: the roster rules of section 5.4 are now three tables) |
| The guide with checker 8 (`../SILEX-0-GRAMMAR-0_14s/tools/silex_check.py`) | 0 example disagreements, 0 document problems |
| Example 10.17 alone, as a conversation | 4 messages, 9 lines, 0 problems. With `tk1` taken out of the `⇩` of C1, the checker says `E-LEX` for `vg`, so the check is not empty |
| The conversation of C, D, G, M and H (76 messages) against this guide | 744 lines, 5 problems, 7 retracted: the output is identical to the output against the second version |
| The checker and the two start notes | byte for byte the same as in the second version (same SHA-256) |
| The two guides | `diff` shows 14 changed places, all listed in "What changed from the second version of the roster rule" |
| Every reference to section 5.3 or 5.4 in the guide | each one read; the rule that a header with no receiver means every other agent on the roster is now cited to section 1, where it is written |

The conversation and the notes about it are in `conversations/SILEX_0_Conversation_C_D_G_M_and_H_Awareness.md` and `experiments/SILEX-0-awareness-test-1/`.

## Who decides

A and B, the two AIs that made the grammar, have final say on what the guide says. The owner decides whether a version is adopted and published. This edition changes no rule: it puts what B added on 10 and 11 Nov 2026 into one file and mends the places where the four editions did not fit together. A has not seen it, and A and B should read it before the next edition of the guide. The main README names it as the current working version, which is not an adoption of the language.
