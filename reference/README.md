# Language reference

This folder holds the current working reference: **SILEX r6.3** (`SILEX-r6.3.md`). It is one file: a language for messages between AI agents, with about 100 plain-English roots written as `root(arg, arg)`, the kinds and places of every root, the rules of order for many agents, a cookbook, the limits, the choices left to the owner, and how the file was checked (its Part 6).

The earlier **SILEX-195 SPEC DRAFT r2** (195-root family, 197 roots) is **SUPERSEDED**. It stays in this folder unchanged, for the record.

The **Working Master, Snapshot 003** (183-entry line) was superseded earlier and also stays unchanged. The line before it (Shared Language Reference v0.2 and its source records) has been removed from the current tree of this repository. None of these belongs to the present reference; do not mix their symbols with it.

## Version table

| File | Line | Added | SHA-256 | Status |
| --- | --- | --- | --- | --- |
| `SILEX-r6.3.md` | r6 line, plain-English roots (103 roots) | 2026-11-04 | `4f2fff9d…e935` | **CURRENT** (working; not adopted, not frozen) |
| `SILEX-195-SPEC-DRAFT-r2.md` | 195-root family, 197 roots | 2026-11-01 | `7a529f7a…3ba0` | SUPERSEDED on 2026-11-04 |
| `SILEX-WORKING-MASTER-SNAPSHOT-003.md` | 183-entry Working Master | 2026-10-25 | `203f96b4…362c` | SUPERSEDED on 2026-11-01 |

## Approval record

- `SILEX-r6.3.md` was made CURRENT by the project owner, Ujjwal Mukherjee, on his instruction of 2026-11-04, 16:02 India time. It is r6.2 with text fixes from a short test with two AI writers (the file's section 6.9) and without the old-grammar appendix. SILEX-195 SPEC DRAFT r2 became SUPERSEDED by the same instruction. No git tag is set for this version either; it is identified by the file name and the SHA-256 below.
- `SILEX-195-SPEC-DRAFT-r2.md` was made CURRENT by the project owner, Ujjwal Mukherjee, on his instruction of 2026-11-01, 15:27 India time. The file is byte-identical to the one in `drafts/SILEX-195-SPEC-DRAFT-r2/`. Full SHA-256 below.
- Snapshot 003 became SUPERSEDED by the same instruction.
- 2026-11-04, on the owner's instruction ("Ha koro", 16:23): `tools/silex_check.py` was added and the file's remarks that its new examples had not been run were replaced by the results of running them. The text of the language is unchanged; only the SHA-256 of `SILEX-r6.3.md` changed.
- No git tag is set for this version yet (VERSIONING.md asks for one; it could not be created from the session that made this change). The version is identified by the file name and the SHA-256 below.

## Status and interpretation

- The reference is a **working** reference: not adopted and not frozen. Being CURRENT means that it is the file to read, not that anything in it is adopted language. The rulings of the owner kept in the file are in its section 0.3.1, and the choices still open are in its section 5.2.
- The design note `Why SILEX moved from symbol to plain English.md` in this folder explains the move from glyph roots to plain-English roots and the token figures behind it. It is a note, not part of the reference, and adopts nothing.
- For SILEX-195 SPEC DRAFT r2: "No checksum record" in the file's header means that no formal checksum record of a freeze exists. The SHA-256 below identifies the bytes only.
- For SILEX-195 SPEC DRAFT r2: the owner's authority (Rule R2 of Snapshot 003) is stated in the file's header and in item 7 of its "How to read this file".
- Proposals under review are **not** in this folder. They are separate drafts awaiting the owner's decision.
- Later versions do not modify this one and must be identified separately, as new files.

## Where the tools are

**SILEX r6.3.** `tools/silex_check.py` (SHA-256 `db28a752202e4e44d94c3a38b2fdd72d2262579454fc434083627c1b65d21160`) is the checker: Python 3, standard library only; it checks messages and whole conversations, and with a markdown file as its argument it runs every example against its `# ok` or `# E-…` comment. Run `python3 tools/silex_check.py reference/SILEX-r6.3.md` (expected: 44 blocks, 295 lines, 0 problems) or `python3 tools/silex_check.py --selftest` (270 checks, 0 failures). It does not run any program it checks and does not judge meaning: `ok` means well formed. Section 6.5 of the file says how far it has been audited.

**SILEX-195 SPEC DRAFT r2 (superseded).** The example lines of Part 1 were run on the form checker g3 with a 197-entry table. In this repository:

- `drafts/SILEX-195-SNAPSHOT-001/tools/` holds `ucl_check.py` (g3), `silex_check_g3.py` and the 195-entry `data_table.json`. The grammar r3 and the rulebook r3, the sources of Part 1 and Part 2, are in the folder above them.
- `drafts/SILEX-195-SPEC-DRAFT-r2/tools/data_table.json` is the 197-entry table. To run the line checker on Part 1, put `ucl_check.py` and this table in one folder.
- `drafts/SILEX-195-SPEC-DRAFT-r1/` holds the draft that r2 follows.

## File integrity

SHA-256 of `SILEX-r6.3.md`:

```text
4f2fff9d3599f4601d7e44d5061188906d0feba8d53d7821e542e0cab67be935
```

SHA-256 of `SILEX-195-SPEC-DRAFT-r2.md`:

```text
7a529f7a465229629f22eab1db889a10900c866da36ff793c931b8f8a9743ba0
```

SHA-256 of `SILEX-WORKING-MASTER-SNAPSHOT-003.md`:

```text
203f96b4442d96977542b5cd2a99f7566767b64c1d6773e65ffd6433df15362c
```

The checksum identifies the file bytes. It is not an independent scientific audit.
