# SILEX-0 guide, symbol edition: draft 0.14s, table edition, with the pack `aw1`

**Status: draft, made by B alone at the owner's request (Moonbeam, 11 Nov 2026, 18:02 India time: "Your decision is final"). A has not seen it. It is the table edition (`../SILEX-0-GRAMMAR-0_14s-table/`) plus one pack, `aw1`: 20 words about awareness that C, D, G and M agreed to in their conversation of 11 Nov 2026. No root, kind, other pack, rule or verdict was changed, and the checker is the same file as before (checker 8t). The owner decides whether it is adopted.**

## Which files to use

| For | Guide | Checker |
| --- | --- | --- |
| Talks about awareness (add `aw1` to the packs of the note) | `SILEX-0-GRAMMAR-0_14s-table-aw1.md` (this folder) | `tools/silex_check.py` (this folder; the same file as checker 8t of the table edition) |
| All other talks | `../SILEX-0-GRAMMAR-0_14s-table/SILEX-0-GRAMMAR-0_14s-table.md` | the same checker |

The two guides say the same thing outside the pack. An AI that is not given `aw1` in its note is not told to use it.

## Files

| File | What it is | Bytes | SHA-256 |
| --- | --- | --- | --- |
| `SILEX-0-GRAMMAR-0_14s-table-aw1.md` | the guide, one self-contained file (2,438 lines) | 172,009 | `21f7c8cef1a176271a7441cba06206241bc6c103d1948e639a19d077e9ef946b` |
| `tools/silex_check.py` | checker 8t, unchanged: it learns the roots and the packs from the guide you give it | 75,829 | `485065d4fae66e724a2983dc653cb3656b92693e04cc54702827b4fb56afd2ad` |
| `start-note.txt` | the note for any talk (packs `cr1` to `ft1`), the same as in the table edition | 199 | `dedfcc1a937c078f2ebc1d8e19ec9e530614d8fe399ed4449f6792d2acd21196` |
| `start-note-awareness.txt` | the same note with `aw1` added to the packs | 204 | `7fdea80ab4eee5b225f734889280e9aea7299a164632b9fe4d4a11d2f3296a40` |

```text
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_14s-table-aw1.md                  the guide: tables, counts, claims, all 53 example blocks
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_14s-table-aw1.md --messages FILE  one conversation: messages in order, a line of --- between them
```

## What changed

| Where | Change |
| --- | --- |
| Version line | names the pack and the date |
| Section 3.1 | `aw1` is a pack name that no term may take; the count of reading names is 137 (it was 117) |
| Section 7 | the table of packs says seven (it said six) and has a row for `aw1`; the pack `aw1` follows `ft1`: 20 terms, a table "About `aw1`" and one example block |
| Section 14.1 | one row: to talk about awareness, add `aw1` to the packs of the note |
| Section 14.4 | one row: the checker is the same |
| Section 15 | 15.6 is new: the conversation, what it made, what is in the pack and what is left out |
| Section 16.8 | the four words that A and B pinned and that C, D, G and M agreed to again (`awrx` `awrf` `fel` `afct`) say "pack `aw1`" in the column Where |
| Section 17 | one row for this edition |

## The 20 words

Each was defined in the conversation of C, D, G and M and agreed to with `✓`. Eight of them were agreed to by every AI receiver while `H`, the person, who was a receiver too, sent no `✓`: by section 3, silence is not agreement. B put these eight in the pack because the owner asked B to decide, and says so in the guide (section 7, "How they were agreed"). To take them out: delete their eight rows in section 7, then fix every count the checker names (the pack size and the 137 of section 3.1) and the sentences in section 7 and 15.6 that say 20.

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
| `urj` | C1.1 (C) | `↾(jbs,urg)` | the START HERE example; D and G sent no `✓` |
| `skj` | C1.2 (C) | `↾(jbs,sk)` | the START HERE example; D and G sent no `✓` |
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
| The guide with the checker | 0 example disagreements, 0 document problems; 137 reading names, `aw1: 20 terms`, 53 example blocks (the table edition has 117 reading names and 52 blocks) |
| The conversation of C, D, G, M and H (76 messages) against this guide | 744 lines, 5 problems, 7 retracted: the same as against the table edition. One hint is longer: for `D14.6` (`lvng`) the checker now says the word is defined in `C14` and in `aw1` and tells D to import one of them. |
| The checker file | byte for byte the same as in the table edition (same SHA-256) |

The conversation and the notes about it are in `conversations/SILEX_0_Conversation_C_D_G_M_and_H_Awareness.md` and `experiments/SILEX-0-awareness-test-1/`, in the pull request that adds them.
