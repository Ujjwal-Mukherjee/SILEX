# SILEX-195 Snapshot 001 (DRAFT)

| Item | Value |
|---|---|
| Date | 2026-11-01 |
| Compiled by | C (Claude), at the project owner's request |
| Status | **DRAFT WORKING SNAPSHOT.** Not frozen. Not adopted. It does not change the CURRENT marker in `reference/README.md` and does not supersede `SILEX-WORKING-MASTER-SNAPSHOT-003`. Only the owner decides what enters `main` and what is adopted. |
| Line | The 195-root family (grammar r3, rulebook r3). It is kept apart from the earlier 183-entry line of the Working Master snapshots and from the v0.2 line; symbols are not mixed between them. |
| What it is | An index of the state of the 195-root family on the date above, with the exact files and their SHA-256. This file adds no language rule. |

## 1. Files in this folder

| File | Bytes | SHA-256 | Role |
|---|---|---|---|
| `SILEX-GRAMMAR-C-r3.md` | 64,441 | `723229b3c2c5442efbbe80a26594e72e702b67931bba87babf0b4c5b29916d7e` | Grammar and the 195-root lexicon (Appendix A), candidate r3 |
| `SILEX-RULEBOOK-r3.md` | 104,454 | `0573a32c3e9d71df12d94bbc4655c74562f8281dc0a86d12260ee5a286d4984b` | Rulebook r3: rules B-1 to B-46, C-1 to C-13, OP-1 to OP-14 |
| `tools/ucl_check.py` | 32,605 | `3ec4e639fc9bda9de5293af87f636d7f2e1086bd5dc4e9758a9c8ba058bbf484` | Form checker g3 (called `ucl_check_g3.py` in the grammar; the session checker needs this file name) |
| `tools/data_table.json` | 174,198 | `d144c3830d4221500fd9a87f25d2050948de72449f00bc4b3fbcbb13d6e24e94` | The table with `n0` as the placeholder |
| `tools/silex_check_g3.py` | 43,127 | `09486de038dce9510c1a1c1dc158ca3557ae8554c8c790d95d484757dcfd18df` | Session checker (form, session, plausibility, English share) |

Run `python3 tools/silex_check_g3.py selftest` to check the tools, and `python3 tools/silex_check_g3.py check SESSIONFILE` to check a session file. A SHA-256 identifies the bytes of a file. It does not make the file authoritative or independently audited.

## 2. The language in numbers

- 195 roots in 25 families. Status: E 40, Ep 26, P 97, U 31 (including `m▤` and `r>` by use), X 1. Tiers: core 68, trial 97, parked 30.
- `n0` is the atom for "not supplied" (owner ruling, 1 Nov 07:29); the word `null` is no longer read. A root with an act shape and a claim shape alone on a line (`c■ d↦ v✓`) stays E-LINE (owner ruling, 1 Nov 07:24).
- Checker lineage: pinned `ucl_check.py` (`5b9823b0…`), rulebook candidate (`96785cf8…`), g2 (`e420ead4…`), g3 (`3ec4e639…`). g3 and g2 carry the edit ◆2 (`m▤` and `r>` take no details), which the owner has not ruled on.

## 3. Evidence so far (summary only; test items and keys are not in this repository)

- **Blind test 1** (four readers on grammar r1, 72 items): form verdicts 25 of 26 for each of three readers, readings of 26 lines recovered in full bar one element, 20 of 20 English sentences written as SILEX. A ceiling: the items sat close to the grammar's own examples.
- **Test 2, first round** (21 ordinary English sentences, three writers): the sentences could not be said in the lexicon. The writers themselves flagged a gap in 18, 16 and 16 of the 21 items (clock times, dates, units, percent, "at least", "every", "the most", send, approve, withdraw, rephrase, "only", "but", "unless", "probably", defining a criterion from roots). Stage 2 was not run on that set.
- **Test 2, second round** (18 simple one-relation sentences, three writers, five blind readings): every writer's SILEX passed the checker bar one stray plain-English line (17 of 18 for one writer as written); the five readings recovered at least 97% of the key elements, two scorers agreeing on all but 4 of 245 judgments, no contradiction. Different encodings of the same sentence were each read correctly. A ceiling again: it shows a floor, not capacity. The roots carried force, negation, cause, questions and requests; the scaffolds carried every predicate. "Decline a request" was the least stable item.

A pass of the checker shows form, not shared meaning. Only blind readers can show that.

## 4. Open for the owner

1. Ruling on ◆2 (`m▤` and `r>` take no details).
2. Whether to add roots for the gaps in section 3 (none is proposed here), and a convention or root for "decline a request".
3. Whether a small set of defined shorthand symbols, each with an expansion into existing roots and chosen from the gaps writers converged on, should enter the trial tier.
4. Whether the generated parts of the rulebook zip (`families/` and similar) are regenerated for r3.
5. A proposal under review (a shared glossary built by acknowledgement) is not part of this snapshot; it needs the owner's decision first.

## 5. Not declared

No root is added, removed or renamed. No adoption, freeze, CURRENT marker or version-table row is declared. The files are candidates under the labels they carry.
