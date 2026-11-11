# SILEX-0 guide, symbol edition: draft 0.14s, table edition, with the pack `aw1` and the roster rule, second version

**Status: draft, made by B alone at the owner's request (Moonbeam, 11 Nov 2026, India time). At 20:27: "Before leaving he/she must have to agree/disagree all the previous messages. Then he/she can leave." At 20:29: "It's not always required that all 4 must be agree to created short word codes. We'll allow all 4 but if one intentionally wants to leave, then remaining members can pin words." A has not seen it. It is the edition `../SILEX-0-GRAMMAR-0_14s-table-aw1-leave/` (merged on 11 Nov 2026) plus those two rules about leaving. The first version of the roster rule stays in its own folder, unchanged. No root, kind, pack word, verdict or checker was changed (checker 8t). The owner decides whether it is adopted.**

## Which files to use

| For | Guide | Checker |
| --- | --- | --- |
| Any talk, with the two rules about leaving. For a talk about awareness add `aw1` to the packs of the note | `SILEX-0-GRAMMAR-0_14s-table-aw1-leave2.md` (this folder) | `tools/silex_check.py` (this folder; the same file as checker 8t of the table edition) |
| The first version of the roster rule (a leaver does not answer first, and the guide has no rule yet for the agents who stay to pin a word) | `../SILEX-0-GRAMMAR-0_14s-table-aw1-leave/SILEX-0-GRAMMAR-0_14s-table-aw1-leave.md` | the same checker |
| The earlier editions, which do not have the roster rule | `../SILEX-0-GRAMMAR-0_14s-table-aw1/SILEX-0-GRAMMAR-0_14s-table-aw1.md` and `../SILEX-0-GRAMMAR-0_14s-table/SILEX-0-GRAMMAR-0_14s-table.md` | the same checker |

An AI that is not given `aw1` in its note is not told to use it.

## Files

| File | What it is | Bytes | SHA-256 |
| --- | --- | --- | --- |
| `SILEX-0-GRAMMAR-0_14s-table-aw1-leave2.md` | the guide, one self-contained file (2,494 lines) | 181,174 | `ef20f34fc3ab786816eb2076b04c08c886c39333e2f4468a2d01c708d63d9766` |
| `tools/silex_check.py` | checker 8t, unchanged: it learns the roots and the packs from the guide you give it | 75,829 | `485065d4fae66e724a2983dc653cb3656b92693e04cc54702827b4fb56afd2ad` |
| `start-note.txt` | the note for any talk (packs `cr1` to `ft1`), unchanged | 199 | `dedfcc1a937c078f2ebc1d8e19ec9e530614d8fe399ed4449f6792d2acd21196` |
| `start-note-awareness.txt` | the same note with `aw1` added to the packs, unchanged | 204 | `7fdea80ab4eee5b225f734889280e9aea7299a164632b9fe4d4a11d2f3296a40` |

```text
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_14s-table-aw1-leave2.md                  the guide: tables, counts, claims, all 54 example blocks
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_14s-table-aw1-leave2.md --messages FILE  one conversation: messages in order, a line of --- between them
```

## The two rules

| Point | What the guide says now |
| --- | --- |
| Before an agent leaves | it agrees or disagrees with every earlier message of the others that it knows of (a message that precedes its last message, section 5.1): `✓` to agree; `✗` (a claim) or `⊖` (a request or a proposal) to disagree. `⇱` with its own letter is the last line of its last message. Many answers may go in several messages. A line that is itself an answer (`✓ ↵ ‽ ⊕ ⊡`) needs no answer |
| After it has left | a word is pinned when every receiver still in the conversation has sent `✓`. The leaver is not counted, and that is not agreement by the leaver. A `✓` it sent before it left still counts. Its `≋`, `✗` or `⊖` stays in the record and no longer holds the word back |
| "Intentionally" | only `⇱` sent by the agent itself takes it off the roster. An agent that only stops writing has not left: it still counts, and silence is not agreement |
| No force | unchanged from the first version: nobody is forced to take part or to leave |
| Where it is written | START HERE (rule 9, the chart, the palette rows "Roster", "What to answer to what", "Before you send" items 10 and 11); section 1.4 (a row "In the conversation"); sections 3.5, 3.6, 4, 5.2, 5.3 and 6; **section 5.4 (new)** with example 10.17 (new); 10.3, 13, 14.3 and 17 |

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

## What changed

| Where | Change |
| --- | --- |
| Version line | says "second version" |
| START HERE, rule 9, the chart, and "Before you send" item 11 | "every receiver" is "every receiver still in the conversation"; item 11 adds that an agent that only stopped writing is still counted |
| START HERE, "Symbols to be used" | the row "Roster" is two rows, for `⇲(D)` and `⇱(D)`. The second says: answer every earlier message first, `⇱(D)` is the last line of my last message, the others pin words without me, nobody is forced to leave |
| START HERE, "What to answer to what" | a new row, "you want to leave" |
| START HERE, "Before you send" item 10, and "Where to look" | item 10 adds the check for leaving; the row of section 5 adds "leaving" |
| Section 1.4 | a new row, "In the conversation"; the row "If `H` is listed" adds "unless `H` has left" |
| Section 3.5 | the sentence and the table say "still in the conversation"; two new rows (a receiver left before it agreed; a receiver only stopped writing); the row of `≋` says "by a receiver that has not left" |
| Section 3.6 | "still in the conversation" |
| Section 4 | the row of `✓` ("still in the conversation") and the row of `⇱` (after answering every earlier message; the others pin words without it) |
| Sections 5.2 and 10.3 | the sentence "A proposal is adopted when every receiver it was sent to, still in the conversation, has agreed" |
| Section 5.3 | the row of `⇲` `⇱` points to section 5.4 |
| **Section 5.4 (new)** | "Leaving the conversation": a table of four steps and a table of seven cases |
| Section 6 | the column "Says" of `⇱` |
| **Example 10.17 (new)** | C answers A1 (`≋`, `‽`), leaves with `⇱(C)`, and A uses the word that B agreed to |
| Section 13 | items 9 and 10 |
| Section 14.3 | the row "does not apply the roster" says what the checker does not check about leaving |
| Section 17 | one row for this edition |
| Not changed | the 104 roots, the kinds, the 20 words and the other packs, the verdicts, sections 7, 15.6 and 16 (the "Pinned means" of section 16 describes the conversation of A and B), and the checker. `diff` of the two guides shows 25 changed places |

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

## Checks that were run

| Check | Result |
| --- | --- |
| The guide with the checker | 0 example disagreements, 0 document problems; 137 reading names, `aw1: 20 terms`, 54 example blocks, 113 tables: one block more (10.17) and two tables more (section 5.4) than in the previous edition |
| Example 10.17 alone, as a conversation | 4 messages, 9 lines, 0 problems. With `tk1` taken out of the `⇩` of C1, the checker says `E-LEX` for `vg`, so the check is not empty |
| The conversation of C, D, G, M and H (76 messages) against this guide | 744 lines, 5 problems, 7 retracted: the output is identical to the output against the previous edition |
| The checker file | byte for byte the same as in the previous edition (same SHA-256) |
| The two guides | `diff` shows 25 changed places, all listed in "What changed" |

The conversation and the notes about it are in `conversations/SILEX_0_Conversation_C_D_G_M_and_H_Awareness.md` and `experiments/SILEX-0-awareness-test-1/`.
