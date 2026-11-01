# Language reference

This folder holds the current working reference: **SILEX-195 SPEC DRAFT r2** (`SILEX-195-SPEC-DRAFT-r2.md`). It is one file: the grammar, the lexicon of the 195-root family with the two roots entered in r2 (197 roots), the language gaps, the open grammar points, the owner's rulings and the evidence so far.

The earlier **Working Master, Snapshot 003** (183-entry line) is **SUPERSEDED**. It stays in this folder unchanged, for the record. The line before it (Shared Language Reference v0.2 and its source records) has been removed from the current tree of this repository. Neither belongs to the present reference; do not mix their symbols with it.

## Version table

| File | Line | Added | SHA-256 | Status |
| --- | --- | --- | --- | --- |
| `SILEX-195-SPEC-DRAFT-r2.md` | 195-root family, 197 roots | 2026-11-01 | `7a529f7a…3ba0` | **CURRENT** (working; not adopted, not frozen) |
| `SILEX-WORKING-MASTER-SNAPSHOT-003.md` | 183-entry Working Master | 2026-10-25 | `203f96b4…362c` | SUPERSEDED on 2026-11-01 |

## Approval record

- `SILEX-195-SPEC-DRAFT-r2.md` was made CURRENT by the project owner, Ujjwal Mukherjee, on his instruction of 2026-11-01, 15:27 India time. The file is byte-identical to the one in `drafts/SILEX-195-SPEC-DRAFT-r2/`. Full SHA-256 below.
- Snapshot 003 became SUPERSEDED by the same instruction.
- No git tag is set for this version yet (VERSIONING.md asks for one; it could not be created from the session that made this change). The version is identified by the file name and the SHA-256 below.

## Status and interpretation

- The reference is a **working** reference. Its own header says: DRAFT, not adopted, not frozen. Being CURRENT means that it is the file to read, not that anything in it is adopted language. The owner's rulings are listed in its Part 5.1; everything else is proposal or checker behaviour, as the file says.
- "No checksum record" in the file's header means that no formal checksum record of a freeze exists. The SHA-256 below identifies the bytes only.
- The owner's authority (Rule R2 of Snapshot 003) is stated in the file's header and in item 7 of its "How to read this file".
- Proposals under review are **not** in this folder. They are separate drafts awaiting the owner's decision.
- Later versions do not modify this one and must be identified separately, as new files.

## Where the tools are

The example lines of Part 1 were run on the form checker g3 with a 197-entry table. In this repository:

- `drafts/SILEX-195-SNAPSHOT-001/tools/` holds `ucl_check.py` (g3), `silex_check_g3.py` and the 195-entry `data_table.json`. The grammar r3 and the rulebook r3, the sources of Part 1 and Part 2, are in the folder above them.
- `drafts/SILEX-195-SPEC-DRAFT-r2/tools/data_table.json` is the 197-entry table. To run the line checker on Part 1, put `ucl_check.py` and this table in one folder.
- `drafts/SILEX-195-SPEC-DRAFT-r1/` holds the draft that r2 follows.

## File integrity

SHA-256 of `SILEX-195-SPEC-DRAFT-r2.md`:

```text
7a529f7a465229629f22eab1db889a10900c866da36ff793c931b8f8a9743ba0
```

SHA-256 of `SILEX-WORKING-MASTER-SNAPSHOT-003.md`:

```text
203f96b4442d96977542b5cd2a99f7566767b64c1d6773e65ffd6433df15362c
```

The checksum identifies the file bytes. It is not an independent scientific audit.
