# SILEX-0 guide, symbol edition: draft 0.14s, table edition, with the pack `aw1` and the roster rule

**Status: draft, made by B alone at the owner's request (Moonbeam, 11 Nov 2026, 19:08 India time: "Yes add that so that anyone can leave with their own decision. No force to take part or leave."). A has not seen it. It is the edition with `aw1` (`../SILEX-0-GRAMMAR-0_14s-table-aw1/`, merged on 11 Nov 2026) plus two things: the roster rule (each agent joins and leaves by its own decision) and the record that Moonbeam agreed to eight words of `aw1`. `⇲` and `⇱` keep their places and have a narrower meaning; no other root, kind, pack word, rule or verdict was changed, and the checker is the same file as before (checker 8t). The owner decides whether it is adopted.**

## Which files to use

| For | Guide | Checker |
| --- | --- | --- |
| Any talk. For a talk about awareness add `aw1` to the packs of the note | `SILEX-0-GRAMMAR-0_14s-table-aw1-leave.md` (this folder) | `tools/silex_check.py` (this folder; the same file as checker 8t of the table edition) |
| The earlier editions, which do not have the roster rule | `../SILEX-0-GRAMMAR-0_14s-table-aw1/SILEX-0-GRAMMAR-0_14s-table-aw1.md` and `../SILEX-0-GRAMMAR-0_14s-table/SILEX-0-GRAMMAR-0_14s-table.md` | the same checker |

An AI that is not given `aw1` in its note is not told to use it.

## Files

| File | What it is | Bytes | SHA-256 |
| --- | --- | --- | --- |
| `SILEX-0-GRAMMAR-0_14s-table-aw1-leave.md` | the guide, one self-contained file (2,443 lines) | 174,471 | `810370772b957791922f1a032801ed82b7e44c851b3f5c3e32bd1b3308a41baa` |
| `tools/silex_check.py` | checker 8t, unchanged: it learns the roots and the packs from the guide you give it | 75,829 | `485065d4fae66e724a2983dc653cb3656b92693e04cc54702827b4fb56afd2ad` |
| `start-note.txt` | the note for any talk (packs `cr1` to `ft1`), unchanged | 199 | `dedfcc1a937c078f2ebc1d8e19ec9e530614d8fe399ed4449f6792d2acd21196` |
| `start-note-awareness.txt` | the same note with `aw1` added to the packs, unchanged | 204 | `7fdea80ab4eee5b225f734889280e9aea7299a164632b9fe4d4a11d2f3296a40` |

```text
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_14s-table-aw1-leave.md                  the guide: tables, counts, claims, all 53 example blocks
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_14s-table-aw1-leave.md --messages FILE  one conversation: messages in order, a line of --- between them
```

## The roster rule

Moonbeam's words: "so that anyone can leave with their own decision. No force to take part or leave."

| Point | What the guide says now |
| --- | --- |
| Leaving | an agent leaves with `⇱` and its own letter: D sends `⇱(D)`. From then on the others do not name D in their headers |
| Joining | an agent joins with `⇲` and its own letter. The person joins with `⇲(H)`, sent under `H` (an AI may draft it, as in section 14.1) |
| No force | nobody puts another agent on the roster or takes it off, and nobody is forced to take part or to leave |
| Where it is written | START HERE, "Symbols to be used": a row "Roster". Sections 4, 5.3 and 6 say the same, so the guide does not contradict itself |
| Why now | in the awareness test nobody used `⇱`: C made the word `clos` (C21.11) and G wrote `⊨(end,tdy)` (G15.13). START HERE listed `⇱` in its palette and had no row that says what it does (`experiments/SILEX-0-awareness-test-1/`, "What was open") |

### What the rule does not settle

| Open | Detail |
| --- | --- |
| The checker | it checks `⇲` and `⇱` for form only (section 14.3 now says so). `⇱(D)` in a message of C is `ok` to it, although the rule says that nobody writes another agent's letter. A later checker could flag it; that is for A and B to decide |
| A word and a leaver | a word is pinned only when every receiver sent `✓` (section 3). If a receiver leaves before it sent `✓`, the word is not pinned, and the guide has no rule yet for the agents who stay to pin it among themselves |
| The roster in a header | a header that names no receiver means every other agent on the roster. After `⇱(D)` the checker still counts D (it takes the roster from the senders and receivers it sees), so name the receivers |

## What changed

| Where | Change |
| --- | --- |
| Version line | names the roster rule |
| START HERE, "Symbols to be used" | a new row, "Roster": `⇲(D)` `⇱(D)`, "I join the conversation; I leave it. Write your own letter only. Each agent decides for itself: nobody is forced to take part, and nobody is forced to leave" |
| Section 4 | the one row of `⇲(x…)` `⇱(x…)` ("changes the roster") is two rows: joins, leaves; `x` is the sender's own letter |
| Section 5.3 | the row of `⇲` `⇱` says the same; the row `H` says that the person joins later by sending `⇲(H)` under `H` |
| Section 6 | the column "Says" of `⇲` and `⇱`: the sender joins, the sender leaves, write your own letter. The places `Ag… → Ln` are the same |
| Section 7 | the status of `aw1` and the row "How they were agreed" say that Moonbeam agreed to the eight words in English on 11 Nov 2026 at 19:08 India time |
| Section 14.3 | one row: the checker does not apply the roster |
| Section 15.6 | one row: the eight words that `H` did not `✓` |
| Section 17 | one row for this edition |
| Not changed | the other roots, the kinds, the 20 words, the other packs, the rules, the verdicts, the examples and the checker. `diff` of the two guides shows 10 changed places and 5 more lines |

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
| The guide with the checker | 0 example disagreements, 0 document problems; 137 reading names, `aw1: 20 terms`, 53 example blocks, 111 tables: the same counts as the edition with `aw1` |
| The conversation of C, D, G, M and H (76 messages) against this guide | 744 lines, 5 problems, 7 retracted, and the same hints as against the edition with `aw1` (the output is identical) |
| The checker file | byte for byte the same as in the table edition and in the edition with `aw1` (same SHA-256) |
| The two guides | `diff` shows 10 changed places, all listed in "What changed" |

The conversation and the notes about it are in `conversations/SILEX_0_Conversation_C_D_G_M_and_H_Awareness.md` and `experiments/SILEX-0-awareness-test-1/`.
