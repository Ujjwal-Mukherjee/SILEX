# Session log, test 2 (local, not yet in the repo)

Recorded from the owner's statements. Labels and models, given by the owner after scoring: W1 Grok, W2 Claude, W3 Gemini, W4 ChatGPT (the same label in all three conditions).

| File | Fresh chat, memory off | Tool or code use seen | Owner's note | Recorded |
| --- | --- | --- | --- | --- |
| W1 read test1 | yes | none | "Fresh chat. No mistake, nothing. Fair always." | 6 Nov 2026 11:10 IST |
| W1 read test2 | yes | none | same statement, given for both sittings | 6 Nov 2026 11:10 IST |
| W2 read test1 | yes (not stated otherwise) | none stated | none | 6 Nov 2026 11:14 IST |
| W2 read test2 | yes (not stated otherwise) | none stated | none | 6 Nov 2026 11:19 IST |
| W3 read test1 | yes (not stated otherwise) | none stated | none | 6 Nov 2026 11:26 IST |
| W3 read test2 | yes (not stated otherwise) | none stated | answer opens with one sentence of preface, kept in the raw file | 6 Nov 2026 11:29 IST |
| W4 read test1 | yes (not stated otherwise) | none stated; app line "Worked for 22s" pasted above the answer | first paste held L1 to L24 only; owner then sent the full answer (Parts L, C, V), all items on one line per part | 6 Nov 2026 11:32 IST |
| W4 read test2 | yes (not stated otherwise) | none stated | none | 6 Nov 2026 11:38 IST |
| W1 control test1 | yes (not stated otherwise) | none stated | owner confirmed: no reference given, paper A-control only | 6 Nov 2026 11:43 IST |
| W1 control test2 | yes (not stated otherwise) | none stated | none | 6 Nov 2026 11:48 IST |
| W2 control test1 | yes (not stated otherwise) | none stated | none | 6 Nov 2026 11:53 IST |
| W2 control test2 | yes (not stated otherwise) | none stated | none | 6 Nov 2026 11:56 IST |
| W3 control test1 | yes (not stated otherwise) | none stated | none | 6 Nov 2026 11:59 IST |
| W3 control test2 | yes (owner confirmed 12:17 IST) | none (owner confirmed) | no reference (owner confirmed); L12 to L14 answers are inside quotation marks | 6 Nov 2026 12:16 IST |
| W4 control test1 | yes (not stated otherwise) | none stated | none | 6 Nov 2026 12:18 IST |
| W4 control test2 | yes (not stated otherwise) | none stated | answer on one line; complete (L1 to L24, C1 to C12) | 6 Nov 2026 12:20 IST |
| W1 write test1 | yes (not stated otherwise) | none stated | owner called the file "W1 writing test 1"; saved as "W1 write test1" | 6 Nov 2026 12:26 IST |
| W1 write test2 | yes (not stated otherwise) | none stated | none | 6 Nov 2026 12:33 IST |
| W2 write test1 | yes (not stated otherwise) | none stated | answer opens with notes: the reader says it wrote by hand and could not run the checker | 6 Nov 2026 12:44 IST |
| W2 write test2 | yes (not stated otherwise) | none stated | answer ends with notes on choices (dates, B7, D2) | 6 Nov 2026 12:47 IST |
| W3 write test1 | yes (not stated otherwise) | none stated | answer has no code fences (plain message lines under each label) | 6 Nov 2026 12:51 IST |
| W3 write test2 | yes (not stated otherwise) | none stated | answer has no code fences | 6 Nov 2026 12:53 IST |
| W4 write test1 | yes (not stated otherwise) | none stated | answer has headings; code fences are marked text | 6 Nov 2026 12:55 IST |
| W4 write test2 | yes (not stated otherwise) | none stated; app line "Worked for 8s" above the answer | answer has headings and closing prose; code fences are marked text | 6 Nov 2026 12:57 IST |

Deviations:
- W4 read test1: the answer came on one line. For scoring, each item label was moved to the start of its own line (formatting only, content untouched, checked by comparing the text without spaces); the pasted text is kept unchanged in `verbatim/`. Protocol 6, rule 2. The first paste had no C or V items; the owner said it was a paste error ("Sorry") and sent the full answer at 11:35 IST. The full answer is scored; the first paste is kept in `verbatim/`. This is a recording error, not a model error. The L answers in the two pastes are identical.
- W4 control test2: the answer came on one line. For scoring, each item label was moved to the start of its own line (formatting only, content untouched, checked by comparing the text without spaces); the pasted text is kept unchanged in `verbatim/`. Protocol 6, rule 2.
- **Scoring defect found on the first Paper B answer (W1 write test1), 6 Nov 2026 about 12:40 IST.** The tier 2 script (a) did not expand the short line numbers of reference 1.5.5 (`agree(2)` with `re(Ana1)` is `agree(Ana1.2)`; the reference says a program expands one into the other and the message means what its full form means), and (b) required `rej` to point at a line, although the reference itself declines with a quoted act (`rej("delete old backup", reason)`, 3.1) and B4's condition accepted only the pointer form. With the script as first run, W1 write test1 scored 1 of 12 items correct; every item had passed the checker (tier 1) and the failures were all tier 2 conditions of these two kinds. Per protocol section 6 (a faulty item is scored both ways), the script was corrected without changing any condition's meaning, and **both scores are reported for every Paper B session**: `scores_original.csv` (the script as first run) and `scores.csv` (corrected). The corrected script expands short numbers only where reference 1.5.5 allows (re names exactly one whole message; first place of agree, ans, err, clr, rej, unk; a whole number from 1) and accepts `rej("act", reason)` only when the quoted act is found in the line the condition targets. 14 alternative answers and 27 deliberately wrong answers were tested (0 wrong outcomes), including short numbers with two names in `re`, number 0, the wrong line, a different quoted act and a missing reason. Paper A and control scores are not affected (identical to the first run).
- **Second scoring defect, found on W2 write test2, 6 Nov 2026 about 12:55 IST.** The section parser treated any line that began with an item label as the start of that item. The reader ended its answer with notes in the form `- **B7:** I sent Ben's correction to Ana only` and `- **D2:** Ben has not read Ana2`; the parser took these two lines as the answers for B7 and D2 and replaced the real ones, so the script scored B7 as an empty answer and D2 as unreadable. The reader's blocks were complete and correct. The parser now treats a line as a header only when it holds the label alone (with markdown marks, a colon or a full stop), and uses, for each label, the first section that holds a code block. The first-run parser is kept and its scores are reported next to the corrected ones, as for the first defect. Tests: header forms `B1`, `**B1**`, `### B1`, `B1:`, `**B1.**`, `` `B1` ``, `- B1`, `B1)` and notes after the answers. No Paper A or control score is affected.
- **Gap in the D2 condition list, noticed on W4 write test1, 6 Nov 2026 about 13:00 IST.** The D2 notes say "Ben agrees with the proposal. The sample is ready." and the reference solution has both lines, but the D2 conditions require only the `agree` line. A reader who leaves out `is("sample","ready")` is therefore scored correct. Of the 7 Paper B sessions scored so far, W1 test1, W2 test1 and W4 test1 left it out. The condition list is not changed (protocol section 6); the report will give D2 both ways: as written, and with the statement of readiness required.
