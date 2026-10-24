# Versioning and reading guide

This file explains how the SILEX repository is organised, so that any participant, human or AI, can find the right file and read its status correctly. It adds no language rule.

## For a participant reading this repository for the first time

1. Read `README.md`, then `reference/README.md`.
2. In `reference/README.md`, find the row marked **CURRENT** in the version table. That is the working reference. There is only one.
3. Read that file completely, starting with its own "read this first" section. It is your source on SILEX. Do not rely on anything you remember from before.
4. Treat every entry by the status label it carries in that file: WORKING, PROVISIONAL, CANDIDATE, OPEN, TEST-ONLY, HISTORY, or ADOPTED. **Being stored in this repository does not make anything adopted.**
5. Anything undeclared or outside the reference: say so and mark it as unknown. Do not guess a meaning.
6. Do not use material from branches other than `main`, or from files marked SUPERSEDED, as current language.

## How the repository changes

- **Owner authority.** Only the project owner decides what enters `main` as the current reference and what is adopted (Rule R2 in the reference). AI participants propose; they do not decide.
- **Drafts go on branches.** A proposal or a draft snapshot is prepared on its own branch and shown through a pull request. It reaches `main` only after the owner approves it.
- **New file, never an overwrite.** A new snapshot is added as a new file, for example `reference/SILEX-WORKING-MASTER-SNAPSHOT-004.md`. Earlier snapshots stay unchanged.
- **Version table.** `reference/README.md` lists every snapshot with its file name, date, SHA-256 and status (CURRENT or SUPERSEDED). When a new snapshot is accepted, the previous CURRENT row becomes SUPERSEDED.
- **Tags.** An accepted snapshot is tagged in git (for example `snapshot-004`), so a reader can be pointed to an exact version.
- **Approval record.** For each accepted snapshot, the version table or `docs/` records who approved it, on what date, and the SHA-256 of the approved file.
- **Integrity.** A SHA-256 checksum identifies the bytes of a file. It does not make the file authoritative or independently audited.

## What does not belong in this repository

- Proposals still under review, unless they are on a branch and marked as drafts.
- Test items and their answer keys. If readers can see them in advance, later blind tests become invalid. They are kept outside the public reference and given to readers only under the owner's control.
- Conversation transcripts with other participants, unless the owner decides to publish them with an explicit scope note.

## Separation of old and new material

The earlier SILEX line (Shared Language Reference v0.2 and its drafts) is not part of the current reference. Its files are not in the current tree. Do not mix its symbols or conventions with the current reference.
