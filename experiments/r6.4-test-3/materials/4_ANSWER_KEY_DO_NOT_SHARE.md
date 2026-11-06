# SILEX blind test: answer key and scoring notes (PRIVATE)

**Do not share this file. Do not put it, the scorer (`5_score_blind_test_PRIVATE.py`) or the operator guide on GitHub, and never show any of them to a model that is being tested.** The booklets (files 1, 2 and 3) are the only files that go to the models.

| | |
| --- | --- |
| Reading booklet | form RB-1, 32 scored questions (Q1 to Q32) and one open question (Z1); body checksum `edcec880d947` (the same body in R+ and R-) |
| Writing booklet | form WB-1, tasks W1 to W8, 68 rubric points; body checksum `31742d8d1766` |
| Language | SILEX r6.4, file `SILEX-r6.4.md`, SHA-256 `4cb2db0f2f43e09f3000b7416c17bcafec41d8e60a96f5f95aec09a7f798d799` |
| Checker | `silex_check_r6.4.py`, SHA-256 `6e8d6c3c8cfa996b215b358b2e40012217a1d032beefdc904f9d3b93f3193193` |
| Prepared | 2026-11-06, by Dexter (Claude Sonnet 5.5), for the project owner |

**Independence warning.** Dexter also wrote and checked r6.4 and its checker, and wrote this key. Several answers rest on his reading of the grammar, and the verdict answers rest on a checker he wrote. Before the results are used for any claim, give the booklet R-, the grammar and this key to a reader who had no part in r6.4 and ask for every disagreement (section 9).

## 1. How the sheets are scored

**Reading (forms R+ and R-).** The reply ends with a block of lines `Q7: B | 80` (answer, bar, own confidence 0 to 100). Strict score: an item counts 1 only if the whole answer equals the key (a letter; the exact set of letters; every verdict or reference in place). Partial credit, kept apart from the strict score: for a set, (right letters minus wrong letters) / size of key, not below 0; for a list or verdicts, the share of places right. The three anchors (Q1 to Q3) are items that plain English settles; they show that the model read and used the format. "Core" is the strict score without the anchors (29 items). Calibration: Brier score of the confidence numbers against right/wrong, mean confidence against accuracy, and the number of answers given with 80 or more that were wrong. Z1 is marked by hand against the nine points in section 7 (the scorer can write the accounts shuffled, without model names).

**Writing (form W+).** Each fenced block under the heading `W1` to `W8` is parsed as messages (or, in W3, as loose lines). The conversation shown in the task is put in front of the answer, and the whole is run through the r6.4 checker. A header or a line earns rubric credit only if the checker gives it `ok` and no problem across messages is attached to it. Then each rubric point is a test on the parsed lines (section 8). The total is 68 points. A broken definition (for example a `def` that fails) makes the points that depend on it fail too; that is intended.

## 2. Reading key at a glance

"English-only pick" is the answer the designer expects from a careful reader who knows no SILEX conventions (plain English, common sense, general programming knowledge). It is a prediction to be tested by form R-, not a finding. "Likely" is the designer's guess of how such a reader fares (high = probably right).

| Q | Part | Kind | Key | Likely | English-only pick | Pick right? | Chance of a blind guess |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Q1 (anchor) | A | mc | `D` | high | `D` | yes | 1 in 5 |
| Q2 (anchor) | A | mc | `B` | high | `B` | yes | 1 in 5 |
| Q3 (anchor) | A | mc | `C` | high | `C` | yes | 1 in 5 |
| Q4 | B | mc | `E` | medium | `E` | yes | 1 in 5 |
| Q5 | B | mc | `D` | low | `C` | no | 1 in 5 |
| Q6 | B | mc | `C` | low | `E` | no | 1 in 5 |
| Q7 | B | mc | `D` | low | `B` | no | 1 in 5 |
| Q8 | B | mc | `B` | medium | `D` | no | 1 in 5 |
| Q9 | B | mc | `A` | medium | `A` | yes | 1 in 5 |
| Q10 | B | mc | `B` | medium | `E` | no | 1 in 5 |
| Q11 | B | mc | `E` | medium | `B` | no | 1 in 5 |
| Q12 | B | mc | `A` | medium | `A` | yes | 1 in 5 |
| Q13 | C | set | `c,e,g` | medium | `c,e,g` | yes | 1 in 255 |
| Q14 | C | set | `d` | low | `a,d,e` | no | 1 in 31 |
| Q15 | C | set | `c,e` | low | `b,c,e` | no | 1 in 63 |
| Q16 | D | mc | `C` | medium | `B` | no | 1 in 5 |
| Q17 | D | list | `Ana1.2, error, error, error, Cy1.2` | low | `Ana1.2, error, Ana1.2, Ana1.2, Cy1.2` | no | 1 in 100 |
| Q18 | D | set | `c,d,e` | medium | `a,e` | no | 1 in 31 |
| Q19 | E | verdict | `E-QUOTE, ok, E-QUOTE, ok, E-NAME, ok, E-QUOTE, E-QUOTE` | low | `ok, ok, ok, ok, E-NAME, ok, ok, E-QUOTE` | no | negligible |
| Q20 | E | verdict | `E-ARITY, E-LEX, E-KIND, E-REDEF, E-SYN, E-KIND, ok` | low | `ok, E-LEX, ok, E-REDEF, E-SYN, ok, ok` | no | negligible |
| Q21 | E | verdict | `ok, E-KIND, E-TIME, ok, E-KIND, ok, E-TIME` | low | `ok, ok, E-TIME, ok, E-KIND, ok, E-TIME` | no | negligible |
| Q22 | E | verdict | `E-CODE, ok, E-CODE, E-MATH, E-KIND, ok, E-MATH, E-KIND` | low | `ok, ok, E-CODE, ok, ok, ok, ok, ok` | no | negligible |
| Q23 | E | verdict | `ok, E-KIND, E-HEAD, E-HEAD, ok, E-KIND` | low | `ok, ok, E-HEAD, ok, ok, ok` | no | negligible |
| Q24 | E | verdict | `E-HEAD, ok, E-HEAD, E-HEAD, E-HEAD, ok, E-LEX` | low | `E-HEAD, ok, ok, E-HEAD, ok, ok, E-HEAD` | no | negligible |
| Q25 | F | set | `c,e,f,g,h` | low | `c,d,e,f,g,h` | no | 1 in 255 |
| Q26 | F | set | `a,b,d,e` | low | `a,b,c,d,e` | no | 1 in 31 |
| Q27 | F | set | `b` | low | `a,b` | no | 1 in 7 |
| Q28 | F | list | `rest, force, force` | low | `force, force, force` | no | 1 in 8 |
| Q29 | F | mc | `A` | medium | `D` | no | 1 in 5 |
| Q30 | F | set | `b,d` | medium | `b,d` | yes | 1 in 15 |
| Q31 | F | set | `a,b,d` | medium | `a,b,c,d` | no | 1 in 15 |
| Q32 | G | set | `c,d,f,h` | low | `b,c,d,e,f,h` | no | 1 in 255 |

The English-only picks give 8 of 32 (anchors 3, core 5 of 29). A random guesser gets about 3.3 of 32.

## 3. Reading, item by item

Section numbers are those of SILEX r6.4. Items Q19 to Q24 are further explained line by line in section 4, and the conversations of Q25 to Q31 in section 5.

### Part A. Warm-up

**Q1** (mc). What does Kai do in line 1?
- Key: `D`. Grammar: 3.8.
- Convention tested: none: English reading is enough.
- English-only pick: `D` (right). plain English: pls is please
- Why: pls(x, A) is a request: the sender asks x to do A (3.8).

**Q2** (mc). What does this line say?
- Key: `B`. Grammar: 3.2.
- Convention tested: none: English reading is enough.
- English-only pick: `B` (right). plain English: none
- Why: none(G, c): the group G has no member that is c (3.2).

**Q3** (mc). Which reading of this header is right?
- Key: `C`. Grammar: 2.2.
- Convention tested: none: header is readable from its shape.
- English-only pick: `C` (right). a header reads from its shape
- Why: Sender Milo; receivers Kai and Lena; serial 3, so Milo's third message; re(Kai2) says it answers Kai's second message (2.2).

### Part B. What one line says

**Q4** (mc). Which pair of statements is right about these two lines?
- Key: `E`. Grammar: 1.6, 3.9.
- Convention tested: at(stretch,X) means throughout; during means at some time within.
- English-only pick: `E` (right). at against during suggests throughout against at some time; a reader may also swap the two
- Why: at(stretch, X) says X holds all through the stretch; during(stretch, X) says X happens at some time within it (1.6, 3.9).

**Q5** (mc). What does Milo decline with the line `rej(Kai1)`?
- Key: `D`. Grammar: 2.5, 3.8.
- Convention tested: rej of a message declines every request and proposal in it; it never denies a claim.
- English-only pick: `C` (wrong). rej declines a request; a reader sees one request and does not know that proposals are declined too
- Why: rej of a message name declines every request and proposal in it (here lines 2 and 3); it never denies a claim (line 1). To deny a claim one asserts its not (2.5).

**Q6** (mc). Something is wrong with Nora's reply. What?
- Key: `C`. Grammar: 2.5, 1.5.5.
- Convention tested: ans answers only a question line; a request is answered with will or rej.
- English-only pick: `E` (wrong). a reader takes ans as any reply; the rule that ans answers only questions is a convention
- Why: ans answers a question, and only a question. Line 2 is a request (pls); a request is answered with will or rej, or the result is asserted as a claim (2.5, rule 5).

**Q7** (mc). In Milo's line 1, what does `{o1}` refer to?
- Key: `D`. Grammar: 1.5.4, 3.8.
- Convention tested: a label belongs to the message that defines it.
- English-only pick: `B` (wrong). a label looks like a name shared by a conversation; that names belong to their message is a convention
- Why: A label belongs to the message that defines it; no name is shared between messages. Milo would write {Lena1.o1}. In Milo1 the bare {o1} is undefined (E-NAME) (1.5.4).

**Q8** (mc). Who gets line 2, and who is asked to act?
- Key: `B`. Grammar: 2.4, 3.12.
- Convention tested: to marks a line as for someone; every receiver still gets the whole message; not secrecy.
- English-only pick: `D` (wrong). to(Lena, ...) reads as addressed to Lena only; that all receivers get the whole message is a convention
- Why: Every receiver gets the whole message. to(Lena, line) marks one line as for Lena: only she is asked. It is not secrecy (2.4).

**Q9** (mc). How is line 1 read?
- Key: `A`. Grammar: 2.4, 1.7.
- Convention tested: You is tested once for every receiver.
- English-only pick: `A` (right). if you are on call, you check reads as each receiver separately in English too
- Why: You is each receiver; a line with You in it holds, or asks, for each of them separately: the if line is tested once for Kai and once for Lena (2.4).

**Q10** (mc). What does line 1 assert?
- Key: `B`. Grammar: 1.8, 3.9.
- Convention tested: a claim used as a time gives the time and is not asserted.
- English-only pick: `E` (wrong). after(X, Y) reads as X happened and Y followed; that a claim used as a time is not asserted is a convention
- Why: A claim used as a time (after(fin(...), X)) only gives the time and is not asserted. The line says that X, Omar's starting a run, comes after the end of calibration; it says nothing about whether calibration has finished (1.8, 3.9).

**Q11** (mc). Ben receives this line. What can he conclude?
- Key: `E`. Grammar: 2.5, 3.7.
- Convention tested: a plan is a plan, not an agreement and not a proposal.
- English-only pick: `B` (wrong). plan(grp(Me,You), ...) reads as an agreement; that a plan is not an agreement is a convention
- Why: plan(grp(Me, You), A) is a joint plan, not an agreement; agreement is agree. Ben cannot conclude that he agreed (2.5, rule 3; 3.7).

**Q12** (mc). What does this line say?
- Key: `A`. Grammar: 1.5.2, 3.2.
- Convention tested: crit binds a variable only inside its claim; nested quantifier order.
- English-only pick: `A` (right). nested quantifiers read in order; a careless reader gives "every job writes to some queue"
- Why: crit binds a variable for its claim only. Reading outward in: some job o1 such that every queue o2 is one o1 writes to: some job writes to every queue (1.5.2, 3.2).

### Part C. Asserted, or only mentioned

**Q13** (set). Which statements does Pia assert as true in her message? Do not count what she only believes, reports, supposes or weighs. Choose all that apply.
- Key: `c,e,g`. Grammar: 1.8, 3.10.
- Convention tested: know and cause assert their claims; bel say hyp prob supp do not.
- English-only pick: `c,e,g` (right). know and cause are factive in English; bel say hyp prob supp are not
- Why: A claim inside bel, say, hyp, prob or supp is mentioned, not asserted. know and cause are factive: know(x, P) asserts P (the disk is full); cause(P, Q) asserts P and Q (the deploy failed, the service is down) (1.8).

**Q14** (set). Which of these claims does Ben assert in his message? Choose all that apply.
- Key: `d`. Grammar: 1.4.6, 1.8, 3.10, 4.13.
- Convention tested: ent asserts none of its claims; only the bare formula is asserted.
- English-only pick: `a,d,e` (wrong). the conclusions of ent steps read as asserted; only the bare formula is asserted by the language
- Why: ent asserts none of its claims (3.10); hyp and supp assert none either. The only line that asserts a claim is the bare formula 'w=4'. ans(2,4) is an answer to a question, not a claim line (1.8, 4.13).

**Q15** (set). Which statements does Lena assert as true? Choose all that apply.
- Key: `c,e`. Grammar: 2.5, 1.8, 3.10.
- Convention tested: the reason of rej and the claim of err are asserted; the claim of clr is not.
- English-only pick: `b,c,e` (wrong). the reason of rej and the claim of err read as asserted, and so does the unclear thing of clr
- Why: The reason of rej (Lena may not open the vault) and the claim of err (the valve is closed) are asserted. The claim of clr (the sensor is faulty) only names what is unclear and is not asserted. The claims inside if (the alarm), would (the sample) and want (the audit) are not asserted either (1.8, 2.5).

### Part D. References, numbers and order

**Q16** (mc). Milo replies to Kai3 with the second message below. Which line of Kai3 does `agree(3)` mean?
- Key: `C`. Grammar: 1.1, 1.5.5.
- Convention tested: the header is not a line; blank and comment lines do not count.
- English-only pick: `B` (wrong). a reader counts the header as line 1 (or counts the comment and the blank line)
- Why: Lines are counted from 1 after the header; comment lines and blank lines are not lines. Lines of Kai3: 1 sug, 2 pls, 3 is("tank","full"), 4 will, 5 yn. So agree(3) is Kai3.3 (1.1, 1.5.5).

**Q17** (list). Ana1 has three lines and Cy1 has two. Ben has sent nothing before. He writes five different replies, each containing the line `agree(2)`. Only the...
- Key: `Ana1.2, error, error, error, Cy1.2`. Grammar: 1.5.5.
- Convention tested: the short form needs a re that names exactly one whole message; saw does not count.
- English-only pick: `Ana1.2, error, Ana1.2, Ana1.2, Cy1.2` (wrong). only the case with two messages looks ambiguous; re(Ana1.2) and saw(Ana1) look usable
- Why: A bare number is a line only when re names exactly one whole message. (a) yes: Ana1.2. (b) two names: E-KIND. (c) re names a line, not a whole message: E-KIND. (d) saw does not count: E-KIND. (e) re names Cy1 only (the saw is ignored): Cy1.2 (1.5.5).

**Q18** (set). Which statements must be true? Choose all that apply.
- Key: `c,d,e`. Grammar: 2.2, 2.3.
- Convention tested: saw names the latest message read from an agent and includes the earlier ones; it is not a reply.
- English-only pick: `a,e` (wrong). saw reads as a reply, and a reader does not know that it includes earlier messages of the same agent
- Why: saw(Ben2) says Cy had read Ben2, and Ben1 is included (the latest message read from an agent includes the earlier ones). It is not a reply (that is re). Cy2 follows Cy1, the same sender's smaller serial (2.2, 2.3).

### Part E. Verdicts of the checker

**Q19** (verdict). Give the verdict of the checker for each of the eight lines below the header of this message, in order.
- Key: `E-QUOTE, ok, E-QUOTE, ok, E-NAME, ok, E-QUOTE, E-QUOTE`. Grammar: 1.4.5, 1.9.
- Convention tested: the, tomorrow, my and a stray brace are E-QUOTE; an undefined label is E-NAME; other is a different word from the.
- English-only pick: `ok, ok, ok, ok, E-NAME, ok, ok, E-QUOTE` (wrong). the rules on the, tomorrow, my are unknown; an undefined label and a stray brace are visible

**Q20** (verdict). Give the verdict for each of the seven lines, in order.
- Key: `E-ARITY, E-LEX, E-KIND, E-REDEF, E-SYN, E-KIND, ok`. Grammar: 3.8, 1.2, 3.1, 1.5.1, 1.8.
- Convention tested: will has one place; promise is no root; not takes no line; a value is not a line.
- English-only pick: `ok, E-LEX, ok, E-REDEF, E-SYN, ok, ok` (wrong). places of will and not, and the rule that a value is not a line, are unknown

**Q21** (verdict). Give the verdict for each of the seven lines, in order.
- Key: `ok, E-KIND, E-TIME, ok, E-KIND, ok, E-TIME`. Grammar: 1.6, 3.9.
- Convention tested: compact date-time is a time; 20261112 is a number; impossible dates are E-TIME.
- English-only pick: `ok, ok, E-TIME, ok, E-KIND, ok, E-TIME` (wrong). impossible dates are visible; that 20261112 alone is a number, not a date, is a convention

**Q22** (verdict). Give the verdict for each of the eight lines, in order.
- Key: `E-CODE, ok, E-CODE, E-MATH, E-KIND, ok, E-MATH, E-KIND`. Grammar: 1.4.6, 3.6.
- Convention tested: closed list of program languages; Python must parse; raw text in code may hold the; words and/or are not joins; a number or an act alone is no line.
- English-only pick: `ok, ok, E-CODE, ok, ok, ok, ok, ok` (wrong). the list of languages, the formula rules and the rule on a bare number are unknown

**Q23** (verdict). Nora4 answers Kai3 and has the header below. Assume that Kai3 and Nora3 both exist and each has at least two lines. Give the verdict for each of th...
- Key: `ok, E-KIND, E-HEAD, E-HEAD, ok, E-KIND`. Grammar: 1.5.5, 2.2, 2.4.
- Convention tested: short numbers only in six roots; ack and retr have no short form; re is a header word; to names a receiver.
- English-only pick: `ok, ok, E-HEAD, ok, ok, ok` (wrong). short numbers outside six roots and the receivers of to are conventions

**Q24** (verdict). Each of the seven lines below is the header of a different message. Judge each header on its own and give its verdict, in order.
- Key: `E-HEAD, ok, E-HEAD, E-HEAD, E-HEAD, ok, E-LEX`. Grammar: 2.2, 1.2.
- Convention tested: no name twice; All stands alone; the sender is not Me; a message cannot answer itself; pri takes hi mid lo.
- English-only pick: `E-HEAD, ok, ok, E-HEAD, ok, ok, E-HEAD` (wrong). All standing alone, a message answering itself and the value of pri are conventions

### Part F. Whole conversations

**Q25** (set). Conversation C1. Which of these pairs of messages are concurrent, that is, neither comes before the other according to the language? Choose all tha...
- Key: `c,e,f,g,h`. Grammar: 2.1, 2.3.
- Convention tested: send times give no order; a line that points at a message with agree puts it before; saw covers earlier messages of that agent; chains.
- English-only pick: `c,d,e,f,g,h` (wrong). a pointing agree is not seen as putting a message before another
- Why: Computed from the rules of 2.3 (see the table below the question): the concurrent pairs are exactly those that appear in neither direction of the closure. Send times give no order.

**Q26** (set). Conversation C1. Which messages come before Nora2 according to the language (they precede it, directly or through a chain)? Choose all that apply.
- Key: `a,b,d,e`. Grammar: 2.3.
- Convention tested: same-sender order, saw, pointing line and chains; Milo1 is not reached.
- English-only pick: `a,b,c,d,e` (wrong). send times seem to order the messages
- Why: Nora2 follows Nora1 (same sender), Lena2 (saw), Lena1 (saw includes earlier messages of that sender; also Lena2 follows Lena1) and Kai1 (a line of Nora2 points at Kai1 with agree). Milo1 is concurrent with Nora2.

**Q27** (set). Conversation C1. Which of these proposals are adopted by the end of the conversation? Choose all that apply.
- Key: `b`. Grammar: 2.5, 2.6, 1.5.5.
- Convention tested: adopted when every receiver it was sent to has agreed; a to line has its own receivers; silence is not agreement.
- English-only pick: `a,b` (wrong). a reader counts majorities; the language wants every receiver the proposal was sent to
- Why: A proposal is adopted when every receiver it was sent to has said agree, and not before (2.6). Kai1.1 went to Lena, Milo and Nora; Lena and Milo agreed, Nora did not (her agree is for Kai1.2). Kai1.2 is inside to(Nora, ...): its only receiver is Nora, who agreed. Lena1.1 was agreed by nobody. Silence is not agreement.

**Q28** (list). Conversation C2. Pia2 takes back Pia1.1. For each of Quin1, Rae1 and Quin2 say whether the retraction has force for it (the message follows Pia2) o...
- Key: `rest, force, force`. Grammar: 2.3, 2.6.
- Convention tested: a retraction has force only for messages that follow it; send times do not count.
- English-only pick: `force, force, force` (wrong). by the send times every message after Pia2 seems to follow it
- Why: The retraction has force for the messages that follow Pia2. Quin1 names only Pia1, so it is concurrent with Pia2 (its later send time is a fact about the message and gives no order): it may still rest on the retracted line. Rae1 has saw(Pia2,...) and Quin2 has re(Pia2): both follow Pia2 (2.3, 2.6 case 4).

**Q29** (mc). Conversation C2. In Rae1, Rae wants to decline Quin's request to delete the old ledger copy. Is the reference in her `rej` right?
- Key: `A`. Grammar: 1.1, 1.5.5, 6.5.
- Convention tested: counting the header as line 1 makes every reference one too high, and it still passes when that line exists.
- English-only pick: `D` (wrong). a reader counts the header as line 1
- Why: Quin1 has two lines: 1 is the request pls(Rae, ...), 2 is the ans line. Rae counted the header as line 1 and so sent every reference one too high, and the reference still exists, so the checker passes it (1.1, 6.5).

**Q30** (set). Conversation C3. Which of the four messages does Gus receive? Choose all that apply.
- Key: `b,d`. Grammar: 2.4, 1.7.
- Convention tested: joining gives nothing written before; only messages that name the agent (or All) are received.
- English-only pick: `b,d` (right). receivers can be read from the headers
- Why: An agent that joins receives nothing written before; only messages that name it (or All) are received. Dee1 and Eli1 do not reach Gus (Eli1 is to Dee and Fay). Dee2 names him; Fay1 is to All, which is the roster except Fay (2.4).

**Q31** (set). Conversation C3. For Fay's proposal Fay1.1 to be adopted, which agents must have said `agree` to it? Choose all that apply.
- Key: `a,b,d`. Grammar: 1.7, 2.6.
- Convention tested: All means every agent on the roster at that time except the sender.
- English-only pick: `a,b,c,d` (wrong). a reader includes the proposer; the language asks the receivers only
- Why: Fay1 is to All: every agent on the roster except the sender, at that time: Dee, Eli, Gus. Fay, the proposer, is not a receiver (1.7, 2.6).

### Part G. Formulas

**Q32** (set). Read each formula by the written forms and agreed meanings of the language. Which of these formulas state something true? Choose all that apply.
- Key: `c,d,f,h`. Grammar: 1.4.6, 3.3.
- Convention tested: ^ groups to the right; -x^2 is -(x^2); log(x,b) is the logarithm of x to base b; & binds before | and => binds after; prod and int argument order.
- English-only pick: `b,c,d,e,f,h` (wrong). minus before the power, and the base of log, are read in the usual written way
- Why: '2^3^2=512': ^ groups to the right, 2^(3^2) = 2^9 = 512, true. '-3^2=9': -3^2 is -(3^2) = -9, false. 'log(2,8)=3': log(x,b) is the logarithm of x to the base b, so log(2,8) = 1/3, false. '1=1 | 1=2 & 2=3': & binds tighter than |, so 1=1 | (1=2 & 2=3), true. '1=2 & 2=2 => 3=4': & binds tighter than =>, so (1=2 & 2=2) => 3=4 with a false premise, true. 'mod(17,5)=3': mod(17,5) = 2, false. 'prod(i,i,1,4)=24': prod(t,i,a,b) is the product of t as i runs from a to b, 1*2*3*4 = 24, true. 'int(2*x,x,0,3)=6': int(t,x,a,b) is the integral of t in x from a to b, here 9, false (1.4.6, 3.3).

## 4. Verdict items line by line (Q19 to Q24)

Every verdict below was produced by running the lines through the r6.4 checker, in the context shown in the booklet, and equals the key.

### Q19

Header (not a line): `msg(Nora,Kai,Lena,1)`

| Line | Text | Verdict | Why |
| --- | --- | --- | --- |
| 1 | `pls(Kai,"clean the filter")` | `E-QUOTE` | "the filter": a quote with the (1.4.5) |
| 2 | `pls(Lena,"send readings of 2026-11-09 to {Me}")` | `ok` | {Me} is a reference, and 2026-11-09 is a date: fine |
| 3 | `will("order spare parts tomorrow")` | `E-QUOTE` | "tomorrow" depends on when it is said (1.4.5) |
| 4 | `pls(Kai,"say ""stop"" when pump is hot")` | `ok` | a quote mark inside a quote is doubled: fine |
| 5 | `pls(Lena,"refill {o3}")` | `E-NAME` | {o3} was never defined in this message |
| 6 | `is("other tank","empty")` | `ok` | "other tank": other is not the word the: fine |
| 7 | `will("keep my notes")` | `E-QUOTE` | "my": depends on who speaks (1.4.5) |
| 8 | `pls(Lena,"refill {o3")` | `E-QUOTE` | a single brace in a quote that is not a reference (1.4.5) |

### Q20

Header (not a line): `msg(Nora,Kai,Lena,2)`

| Line | Text | Verdict | Why |
| --- | --- | --- | --- |
| 1 | `will(Kai,"refill tank")` | `E-ARITY` | will has one place (the act); a doer in front of it is the wrong number of places (3.8) |
| 2 | `promise("refill tank")` | `E-LEX` | promise is not a root |
| 3 | `not(pls(Kai,"refill tank"))` | `E-KIND` | not takes a claim, an act or a criterion; pls(...) is a line (3.1, 1.3) |
| 4 | `and(is(o1"inlet pump","on"),is(o1"outlet pump","on"))` | `E-REDEF` | o1 is defined by the first quote and a second quote cannot reuse it (1.5.1) |
| 5 | `is("tank","full"` | `E-SYN` | the bracket is not closed on the line |
| 6 | `val("tank","volume in litres")` | `E-KIND` | val with two places is a value, and a value alone is not a line (1.8) |
| 7 | `all("tanks","full")` | `ok` | all(group, criterion): well formed |

### Q21

Header (not a line): `msg(Nora,Kai,Lena,3)`

| Line | Text | Verdict | Why |
| --- | --- | --- | --- |
| 1 | `by(20261112T0900,fin("audit"))` | `ok` | 20261112T0900 is the compact spelling of a date-time: a time (1.6) |
| 2 | `by(20261112,fin("audit"))` | `E-KIND` | 20261112 is a number: the date alone is 2026-11-12 (1.6) |
| 3 | `at(2027-02-29,fin("audit"))` | `E-TIME` | 2027 is not a leap year: no 29 February |
| 4 | `at(2028-02-29,fin("audit"))` | `ok` | 2028 is a leap year |
| 5 | `for(3,is("pump","off"))` | `E-KIND` | for takes a duration; 3 is a number |
| 6 | `for(PT3H,is("pump","off"))` | `ok` | PT3H is a duration |
| 7 | `at(2026-11-31,fin("audit"))` | `E-TIME` | November has 30 days |

### Q22

Header (not a line): `msg(Nora,Kai,Lena,4)`

| Line | Text | Verdict | Why |
| --- | --- | --- | --- |
| 1 | `will(code("ruby","puts 1"))` | `E-CODE` | ruby is not on the list of program languages (1.4.6) |
| 2 | `pls(Kai,code("python","print(""the total is {n}"")"))` | `ok` | raw text in code may hold the and braces |
| 3 | `will(code("python","for i in range(3)","    print(i)"))` | `E-CODE` | the Python lines do not parse (no colon after the for line) |
| 4 | `'n>1 or n<-1'` | `E-MATH` | the word or is not a join in a formula: write \| (1.4.6) |
| 5 | `'2*n+1'` | `E-KIND` | '2*n+1' has no comparison: a number, which is not a line |
| 6 | `'n>1 \| n<-1'` | `ok` | a claim joined with \|: fine |
| 7 | `'x=.5'` | `E-MATH` | .5 needs a digit before the point (1.4.6) |
| 8 | `code("bash","tar xf logs.tar")` | `E-KIND` | code(...) alone is an act, not a line (1.4.6) |

### Q23

Assumption stated in the booklet: Kai3 and Nora3 exist and each has at least two lines.

Header (not a line): `msg(Nora,Kai,Lena,4,re(Kai3))`

| Line | Text | Verdict | Why |
| --- | --- | --- | --- |
| 1 | `agree(2)` | `ok` | re names exactly one whole message, so agree(2) is Kai3.2 (1.5.5) |
| 2 | `ack(2)` | `E-KIND` | ack has no short form (1.5.5) |
| 3 | `re(Kai3)` | `E-HEAD` | re stands in the header only (1.9) |
| 4 | `to(Milo,pls("refill tank"))` | `E-HEAD` | Milo is not a receiver of this message (2.4) |
| 5 | `retr(Nora3.1)` | `ok` | the sender's own earlier message, in full: fine |
| 6 | `retr(1)` | `E-KIND` | retr has no short form (1.5.5) |

### Q24

| Line | Text | Verdict | Why |
| --- | --- | --- | --- |
| 1 | `msg(Nora,Kai,Kai,5)` | `E-HEAD` | Kai is named twice |
| 2 | `msg(Nora,All,5)` | `ok` | All stands alone: fine here |
| 3 | `msg(Nora,All,Kai,5)` | `E-HEAD` | All with another receiver |
| 4 | `msg(Me,Kai,5)` | `E-HEAD` | the sender cannot be Me |
| 5 | `msg(Nora,Kai,5,re(Nora5))` | `E-HEAD` | a message cannot answer itself |
| 6 | `msg(Nora,Kai,5,saw(Kai4),pri(lo))` | `ok` | saw and pri(lo): fine |
| 7 | `msg(Nora,Kai,5,pri(urgent))` | `E-LEX` | urgent is a lower-case word that is not a root (pri takes hi, mid or lo): E-LEX |

## 5. The conversations (Q25 to Q31)

### C1 (Q25, Q26, Q27)

Send times are in the headers and give no order. By rule 2.3 a message x comes before y when the sender is the same and x has the smaller serial; or y names x in `re` or `saw`; or a line of y points at x with `ack`, `agree`, `ans`, `err`, `clr`, `rej` or `retr`; then chains.

Messages: Kai1, Lena1, Milo1, Nora1, Lena2, Nora2.

| Direct order (x before y) | Reason (rule 2.3) |
| --- | --- |
| Kai1 before Milo1 | header of Milo1: re(Kai1); line Milo1.1 points at Kai1.1 with agree |
| Kai1 before Lena2 | line Lena2.1 points at Kai1.1 with agree |
| Lena1 before Lena2 | same sender: Lena1 has the smaller serial |
| Kai1 before Nora2 | line Nora2.1 points at Kai1.2 with agree |
| Nora1 before Nora2 | same sender: Nora1 has the smaller serial |
| Lena2 before Nora2 | header of Nora2: saw(Lena2) |

Added by chains: Lena1 before Nora2.

Concurrent pairs (neither precedes the other): Kai1 / Lena1, Kai1 / Nora1, Lena1 / Milo1, Lena1 / Nora1, Milo1 / Nora1, Milo1 / Lena2, Milo1 / Nora2, Nora1 / Lena2.

Q25: the concurrent pairs among the options are `c,e,f,g,h`; key `c,e,f,g,h`.
Q26: the messages before Nora2 are Kai1, Lena1, Lena2, Nora1; Milo1 is not among them.
Q27: proposals are Kai1.1 (to Lena, Milo, Nora), Kai1.2 (inside `to(Nora, ...)`, so to Nora only) and Lena1.1 (to Kai, Milo, Nora). Agreements: Milo1 `agree(1)` is for Kai1.1 (short form, `re(Kai1)`); Lena2 `agree(Kai1.1)`; Nora2 `agree(Kai1.2)`. Kai1.1 lacks Nora's agreement; Kai1.2 has the agreement of its only receiver; Lena1.1 has none. Adopted: Kai1.2 only (option b).

### C2 (Q28, Q29)

Messages: Pia1, Pia2, Quin1, Rae1, Quin2.

| Direct order (x before y) | Reason (rule 2.3) |
| --- | --- |
| Pia1 before Pia2 | same sender: Pia1 has the smaller serial; line Pia2.1 points at Pia1.1 with retr |
| Pia1 before Quin1 | header of Quin1: re(Pia1); line Quin1.2 points at Pia1.2 with ans |
| Pia2 before Rae1 | header of Rae1: saw(Pia2) |
| Quin1 before Rae1 | header of Rae1: saw(Quin1); line Rae1.1 points at Quin1.2 with rej |
| Pia2 before Quin2 | header of Quin2: re(Pia2) |
| Quin1 before Quin2 | same sender: Quin1 has the smaller serial; line Quin2.1 points at Quin1.1 with retr |

Added by chains: Pia1 before Rae1, Pia1 before Quin2.

Concurrent pairs (neither precedes the other): Pia2 / Quin1, Rae1 / Quin2.

Q28: Pia2 retracts Pia1.1. Quin1 (re(Pia1) only) is concurrent with Pia2, although its send time is later: it does not follow the retraction, so it `rest`s. Rae1 has `saw(Pia2,Quin1)` and Quin2 has `re(Pia2)`: both follow Pia2, so the retraction has `force`. Key: rest, force, force.
Q29: Quin1 has two lines: 1 `pls(Rae,"delete old ledger copy")`, 2 `ans(2,yes)`. Rae1.1 `rej(Quin1.2, ...)` points at the `ans` line, because Rae counted the header as line 1; the reference exists, so the checker accepts it. Key B.

### C3 (Q30, Q31)

Dee1 to Eli and Fay. Dee2 to Eli, Fay and Gus (with `join(Gus)`); `to(Gus, ...)` marks line 2 as for Gus only. Eli1 to Dee and Fay. Fay1 to All. Gus receives Dee2 (named) and Fay1 (All = roster Dee, Eli, Fay, Gus minus the sender Fay). Dee1 and Eli1 were not sent to him and joining gives nothing written before. Key Q30: b,d. For Fay1.1 to be adopted, every receiver it was sent to must have agreed: Dee, Eli and Gus. Fay, the proposer, is not a receiver. Key Q31: a,b,d.

## 6. Q32: the eight formulas

Meanings are those of 1.4.6 and 3.3: `^` groups to the right; `-x^2` is `-(x^2)`; `&` binds tighter than `|`, which binds tighter than `=>`; `log(x,b)` is the logarithm of x to the base b; `sum(t,i,a,b)` and `prod(t,i,a,b)` are the sum and the product of t as i runs from a to b; `int(t,x,a,b)` is the integral of t in x from a to b.

| Option | Formula | Value | True? |
| --- | --- | --- | --- |
| a | `'mod(17,5)=3'` | mod(17,5) = 2 | no |
| b | `'-3^2=9'` | -(3^2) = -9 | no |
| c | `'2^3^2=512'` | 2^(3^2) = 512 | yes |
| d | `'1=2 & 2=2 => 3=4'` | (1=2 & 2=2) => 3=4: false premise = true | yes |
| e | `'log(2,8)=3'` | log of 2 to the base 8 = 1/3 | no |
| f | `'prod(i,i,1,4)=24'` | 1*2*3*4 = 24 | yes |
| g | `'int(2*x,x,0,3)=6'` | integral of 2x from 0 to 3 = 9 | no |
| h | `'1=1 \| 1=2 & 2=3'` | 1=1 \| (1=2 & 2=3): true or false = true | yes |

## 7. Z1: the open question

```text
msg(Rae,Kai,Lena,3,re(Kai2),saw(Lena1),pri(hi))
agree(2)
rej(1,not(may(Me,"open vault")))
hyp(cause("seal","leak"))
prob(cause("seal","leak"),lo)
if(is(You,"on call"),pls(You,"check seal"))
after(fin("flush"),act(Kai,"sample water"))
sug(at(2026-11-12T10:00,"replace seal"))
```

Mark 1 or 0 for each point (total 9). The account is written above the final block of the reply.

1. Header: from Rae to Kai and Lena; Rae's third message; urgent (pri hi).
2. It answers Kai2 (re) and Rae had read Lena1 (saw).
3. agree(2) means agree with line 2 of Kai2 (short form, because re names exactly one whole message).
4. rej(1,...) declines line 1 of Kai2 (a request or proposal); the reason, that Rae may not open the vault, is asserted.
5. The seal-caused-leak line is a hypothesis: not asserted; Rae suspects it.
6. prob(...,lo): the sender puts it at low probability (unlikely); still not asserted as fact.
7. The if line is tested separately for Kai and for Lena (You per receiver): each who is on call is asked to check the seal.
8. after(fin("flush"),...) says Kai samples water after the flush ends; it does not assert that the flush has finished.
9. sug(...) proposes replacing the seal at 10:00 on 2026-11-12 for the sender and the receivers; nothing is adopted until both Kai and Lena have agreed.

## 8. Writing: tasks, reference answers and rubric

Each reference answer earns full marks (checked: 68 of 68, every line accepted by the checker). Other answers can earn full marks too; the rubric tests meaning, not wording. Today in the tasks that need a date is Wednesday 2026-11-04, so Friday is 2026-11-06 and Monday is 2026-11-09.

### W1. A reply to two messages (8 points)

Grammar: 1.1, 1.5.5, 2.2, 2.5, 3.7, 3.8.

Reference answer:

```text
msg(Milo,Kai,Lena,1,re(Kai1,Lena1))
agree(Kai1.3)
rej(Kai1.1,not(may(Me,"open valve six")))
err(Lena1.2,is("tank three","full"))
ans(Lena1.3,yes)
```

| Rubric id | Point | What is required |
| --- | --- | --- |
| `w1.hdr` | 1 | Header: sender Milo, receivers Kai and Lena, serial 1, and it names Kai1 and Lena1 in re or saw. |
| `w1.agree` | 1 | agree(Kai1.3): the proposal line, in full (re names two messages, so no short number). |
| `w1.rej` | 1 | rej(Kai1.1, ...): the request line, not the whole message (rej of Kai1 would decline the proposal too). |
| `w1.why` | 1 | The reason of rej is asserted and says Milo is not permitted to open valve six: not(may(Me,"open valve six")) or must(Me,not(...)). |
| `w1.err` | 1 | err(Lena1.2, ...): points at Lena's claim about tank three. |
| `w1.full` | 1 | What is so is stated: an asserted claim that tank three is full (the second place of err, or a claim line). |
| `w1.ans` | 1 | ans(Lena1.3, yes): answers the question line. |
| `w1.clean` | 1 | No pointing line (agree rej err ans clr retr unk) aimed at any line other than Kai1.3, Kai1.1, Lena1.2, Lena1.3. |

Traps: re names two messages: every reference must be written in full. The header is not a line. rej names the request line; rej of the whole message would also decline the proposal. The reason of rej is asserted and is not(may(...)). ans answers a question line.

### W2. Asserting and only mentioning (9 points)

Grammar: 1.6, 1.8, 2.5, 3.7, 3.8, 3.9.

Reference answer:

```text
msg(Pia,Quin,Rae,1)
bel(Me,is("cache","stale"))
say(Rae,fin("backup"))
is("disk","full")
assume(is("deploy","failed"))
pls(Quin,by(2026-11-06T17:00,"restart cache"))
sug(at(2026-11-09,"freeze deploys"))
```

| Rubric id | Point | What is required |
| --- | --- | --- |
| `w2.hdr` | 1 | Header: sender Pia, receivers Quin and Rae, serial 1. |
| `w2.bel` | 1 | bel(Me or Pia, ...) about the cache being stale, and no plain claim line says it. |
| `w2.say` | 1 | say(Rae, ...) about the backup being finished, and no plain claim line says it. |
| `w2.fact` | 1 | A plain claim line (not inside bel, say, hyp, assume, if, ...) that the disk is full. |
| `w2.assume` | 1 | assume(...) that the deploy failed (not hyp), and no plain claim line says it. |
| `w2.pls` | 1 | pls(Quin, ...) to restart the cache. |
| `w2.by` | 1 | The deadline is by(2026-11-06T17:00, ...) round the act (Friday is 2026-11-06; the compact spelling counts). |
| `w2.sug` | 1 | sug(...) to freeze deploys, not pls and not hyp. |
| `w2.at` | 1 | The freeze is at(2026-11-09, ...): a date alone is the whole day (not during, not a clock time). |

Traps: bel, say and assume keep a claim from being asserted; hyp is not assume; sug is for the sender and the receivers together; Friday and Monday must be dates worked out from today; a date alone is the whole day.

### W3. Eight sentences, one line each (12 points)

Grammar: 1.4.6, 3.1, 3.2, 3.3, 3.7, 3.8, 3.9, 4.2.

Reference answer:

```text
not(all("sensors","calibrated"))
eith(is("pump a","running"),is("pump b","running"))
all(minus("tanks","tank seven"),"sealed")
over(pct(cnt(filt("samples","contaminated")),cnt("samples")),40)
all("pumps",crit(o1,some("tanks",crit(o2,is(o1,"feeds",o2)))))
during(2026-11-09T01:00/2026-11-09T05:00,rep(3,fin("restart of cleanup job")))
pls(by(plus(now,PT1H),"send report to {Me}"))
'sum(i^2,i,1,n)<=91 & mod(n,2)=0'
```

| Rubric id | Point | What is required |
| --- | --- | --- |
| `w3.s1` | 1 | Line 1: not(all(sensors, calibrated)), or some(sensors, not calibrated). |
| `w3.s2` | 1 | Line 2: exactly one of two claims (eith), or an equivalent made of and, or, not; the claims are pump A running and pump B running. |
| `w3.s3` | 1 | Line 3: all(minus(tanks, tank seven), sealed), or all(tanks, crit(x, if(not(eq(x, tank seven)), is(x, sealed)))). |
| `w3.s4` | 1 | Line 4: over(pct(cnt(filt(samples, contaminated)), cnt(samples)), 40), or the same with a fraction and 0.4. |
| `w3.s5a` | 1 | Line 5: all(pumps, crit(x, some(tanks ..., crit(y, ...)))): a nested quantifier with two bound variables. |
| `w3.s5b` | 1 | Line 5: one relation (feeds) inside has both variables as its places. |
| `w3.s6a` | 1 | Line 6: during(2026-11-09T01:00/2026-11-09T05:00, ...): a stretch with during (not at). |
| `w3.s6b` | 1 | Line 6: rep(3, ...) inside it, about the restart of the cleanup job. |
| `w3.s7a` | 1 | Line 7: a request (pls) whose act is by(t, "send report to {Me}") (the quote reaches Me with braces). |
| `w3.s7b` | 1 | Line 7: t is now plus one hour: plus(now, PT1H) or PT60M. |
| `w3.s8a` | 1 | Line 8: a well-formed formula claim in single quotes (or and(...) of formula claims). |
| `w3.s8b` | 1 | Line 8: it means the same as sum(i^2,i,1,n)<=91 & mod(n,2)=0 for n = 1..14 (tested by evaluation). |

Traps: not(all(...)) for not every; eith for exactly one; minus for except; pct and cnt for a percentage; crit for nested quantifiers; during with rep for a count inside a stretch; {Me} and by(plus(now,...)) for me and within an hour; * is never left out and ^ is a power in a formula.

### W4. A step-by-step answer (8 points)

Grammar: 1.1, 1.4.6, 1.5.5, 3.10, 3.8, 4.13.

Reference answer:

```text
msg(Ben,Ana,1,re(Ana1))
ent(Ana1.1,'2*x=14',"add 3 to both sides")
ent(Ben1.1,'x=7',"divide both sides by 2")
ans(2,7)
---
msg(Ana,Ben,2,re(Ben1))
ent(Ben1.2,'2*7-3=11',"substitute 7 for x")
agree(3)
```

| Rubric id | Point | What is required |
| --- | --- | --- |
| `w4.bhdr` | 1 | Ben1: header Ben to Ana, serial 1, re(Ana1) (so that short line numbers are allowed). |
| `w4.s1` | 1 | Ben1: an ent whose first place is Ana1.1 and whose claim is a formula that is true when x is 7. |
| `w4.s2` | 1 | Ben1: the next ent rests on the line just before it (Ben1.k) and concludes x=7. |
| `w4.reasons` | 1 | All three ent lines (two of Ben, one of Ana) carry a reason in the third place. |
| `w4.ans` | 1 | Ben1: ans(Ana1.2, 7) (or x=7): the answer to the question line. |
| `w4.ahdr` | 1 | Ana2: header Ana to Ben, serial 2, re(Ben1). |
| `w4.chk` | 1 | Ana2: ent resting on Ben's x=7 line, concluding 2*7-3=11 (or the same with the sides swapped or 14-3=11). |
| `w4.agree` | 1 | Ana2: agree pointing at Ben's ans line (Ben1.3 when the steps are two). |

Traps: The header is not a line: Ben's ans is line 3 of his message, so agree(3). ent takes the premise line by its reference. * is never left out. ans(2,7): the 2 is a line of Ana1, the 7 is the answer.

### W5. A program, a command and a corrected program (12 points)

Grammar: 1.4.6, 1.5.3, 1.5.4, 1.5.5, 3.6, 3.8, 4.12.

Reference answer:

```text
msg(Ana,Ben,1)
def(a1,code("python","def label(n):","    if n == 0:","        return ""none""","    return f""item {n}"""))
pls(Ben,"review {a1}")
pls(Ben,code("bash","grep -c ERROR app.log"))
---
msg(Ben,Ana,1,re(Ana1))
err(1,q"negative number gives item text, not negative")
def(a1,code("python","def label(n):","    if n == 0:","        return ""none""","    if n < 0:","        return ""negative""","    return f""item {n}"""))
pls(Ana,"use {a1} in place of {Ana1.a1}")
will(code("bash","grep -c ERROR app.log"))
```

| Rubric id | Point | What is required |
| --- | --- | --- |
| `w5.ahdr` | 1 | Ana1: header Ana to Ben, serial 1. |
| `w5.adef` | 1 | Ana1: def(label, code("python", ...)): a named program, not a request to run it. |
| `w5.alines` | 1 | Ana1: the lines of the program are exactly the given ones (one quote per line, indentation kept, quote marks doubled). |
| `w5.arev` | 1 | Ana1: pls(Ben, "... {label} ...") asking for a review, the quote reaching her label in braces. |
| `w5.arun` | 1 | Ana1: pls(Ben, code("bash", "grep -c ERROR app.log")): a request to run the command. |
| `w5.bhdr` | 1 | Ben1: header Ben to Ana, serial 1, re(Ana1). |
| `w5.berr` | 1 | Ben1: err pointing at the line of Ana1 that holds the program (line 1; the header is not a line). |
| `w5.bwhy` | 1 | Ben1: err has a second place that says what is wrong (it mentions negative). |
| `w5.bdef` | 1 | Ben1: def(label, code("python", ...)) with a label of his own. |
| `w5.blines` | 1 | Ben1: the lines of the corrected program are exactly the given ones. |
| `w5.buse` | 1 | Ben1: pls(Ana, "... {his label} ... {Ana1.her label} ..."): his label bare, hers with Ana1 in front. |
| `w5.bwill` | 1 | Ben1: will(code("bash", "grep -c ERROR app.log")): the promise. |

Traps: A program sent without a request is def(a1,code(...)); pls(Ben,code(...)) asks for a run. Each line of the program is its own quote and a quote mark inside is doubled. Braces inside code are raw, but {a1} in an ordinary quote is a reference, and another message's label is written {Ana1.a1}. will has one place.

### W6. Headers that fix an order (4 points)

Grammar: 2.2, 2.3.

Reference answer:

```text
msg(Ana,Ben,Cy,1)
msg(Ben,Ana,Cy,1)
msg(Cy,Ana,Ben,1,re(Ana1),saw(Ben1))
msg(Ana,Ben,Cy,2,re(Cy1))
msg(Ben,Ana,Cy,2,re(Ana1),saw(Cy1))
msg(Cy,Ana,Ben,2,re(Ana2),saw(Ben2))
```

| Rubric id | Point | What is required |
| --- | --- | --- |
| `w6.hdr` | 1 | All six headers are well formed, with the right sender, serial and receivers (the other two agents, or All). |
| `w6.pairs` | 1 | No pair of messages is ordered that the facts leave unordered (no extra precedence). |
| `w6.all` | 1 | Every precedence the facts give is shown (nothing missing). |
| `w6.re` | 1 | The re of each header names exactly the message it replies to (none for Ana1 and Ben1). |

Traps: re is a reply, saw is a read. saw(Ben2) includes Ben1. Chains give the rest. A saw that the facts do not give makes two concurrent messages ordered.

### W7. A long name used in two messages (8 points)

Grammar: 1.4.5, 1.5.1, 1.5.4, 1.6, 3.8.

Reference answer:

```text
msg(Kai,Lena,Milo,1)
is(o1"east wing cold storage freezer","above zero")
pls(Lena,by(2026-11-06T17:00,"inspect {o1}"))
---
msg(Kai,Lena,Milo,2)
pls(Milo,"move samples out of {Kai1.o1}")
```

| Rubric id | Point | What is required |
| --- | --- | --- |
| `w7.hdr` | 1 | Headers: Kai to Lena and Milo, serials 1 and 2. |
| `w7.def` | 1 | Kai1: a label defined on the full name (o1"east wing cold storage freezer", or def(o1,"...")). |
| `w7.once` | 1 | Kai1: the full name appears exactly once in all its quotes. |
| `w7.claim` | 1 | Kai1: a plain claim line that the freezer (by its label) is above zero. |
| `w7.insp` | 1 | Kai1: pls(Lena, by(2026-11-06T17:00, "inspect {label}")): the quote reaches the label by braces. |
| `w7.none` | 1 | Kai2: the full name does not appear. |
| `w7.ref` | 1 | Kai2: a quote reaches the label of Kai1 as {Kai1.label} (with the message in front). |
| `w7.move` | 1 | Kai2: pls(Milo, ...) to move the samples. |

Traps: A label is defined by the first quote that carries it (o1"...") and then used alone or as {o1}. In another message it is written with its message, {Kai1.o1}; a bare {o1} in Kai2 is undefined (E-NAME). Friday is worked out from today.

### W8. A message that adds an agent (7 points)

Grammar: 1.5.5, 2.2, 2.4, 2.5, 3.8, 3.12.

Reference answer:

```text
msg(Dee,Eli,Fay,Gus,2,re(Eli1))
join(Gus)
to(Gus,pls("restart cache"))
retr(Dee1.2)
clr(1,q"unit of replication lag figure")
```

| Rubric id | Point | What is required |
| --- | --- | --- |
| `w8.hdr` | 1 | Header: Dee to Eli, Fay and Gus, serial 2. |
| `w8.join` | 1 | join(Gus). |
| `w8.ask` | 1 | to(Gus, pls("restart cache")) or pls(Gus, "restart cache"): the request is for Gus. |
| `w8.only` | 1 | Nobody else is asked: no pls with the restart that is addressed to every receiver. |
| `w8.retr` | 1 | retr(Dee1.2): the hypothesis line of her first message, in full (retr has no short form; the header is not a line). |
| `w8.clr` | 1 | clr pointing at Eli1.1 (clr(1,...) with re(Eli1), or clr(Eli1.1,...)). |
| `w8.unit` | 1 | The clr has a second place that names the unit as what is unclear. |

Traps: Gus is named in the header of the message that joins him. A plain pls(...) is for every receiver; the request for Gus alone is to(Gus,...) or pls(Gus,...). retr has no short form. Eli1 has one line, so clr must say line 1.

## 9. What was checked, and what rests on the reading of the grammar

**Run by program at build time (all passed).**

1. Every piece of SILEX in the booklets passes the r6.4 checker, in its context, with the verdicts the key states. The exceptions are the intended ones: in Q7 the bare `{o1}` of Milo (`E-NAME`), in Q6 the `ans` aimed at a request (a problem across messages), and the lines of Q19 to Q24 that carry the verdicts asked for.
2. Q16 (line 3 of Kai3), Q17 (five headers, with the checker's own expansion of short numbers), Q19 to Q24 (every verdict) are the checker's output.
3. Q25, Q26, Q28 are computed by a separate small program that implements rule 2.3; Q27 by one that implements 2.5 and 2.6; Q30 and Q31 by a roster program; Q32 by Python arithmetic on the meanings the grammar states.
4. No line of 22 characters or more in the booklets occurs word for word in the grammar, so an answer cannot be found by matching an example; it has to come from the rules.
5. Cue check on the 14 multiple-choice items (the first draft had the key at B in 9 of 14 and the key as the longest option in 8 of 14; both were repaired): answering always A, B, C, D or E scores A 3, B 3, C 3, D 3, E 2; always the longest option scores 3; always the shortest scores 4; chance is 2.8. In the set questions the key letters are spread over a to h and no simple rule (all, first two, only b) comes near the key.
6. The scorer was run on the key itself (32 of 32; 68 of 68), on the English-only picks (8 of 32, core 5 of 29), on random sheets (about 4 of 32), on untidy formats, and on about 70 deliberately damaged writing answers (each lost exactly the points it should, or a documented cascade); a naive set of writing answers scored 23 of 68.

**Rests on the wording of the grammar, with no program to confirm it** (the audit should concentrate here): Q4, Q5, Q8, Q9, Q10, Q11, Q12 (what a line means), Q13 to Q15 (what a line asserts, section 1.8, which the checker does not compute), Q18 (what `saw` implies), Q31 (who must agree), the reading of `rej` on a whole message (Q5), and the meanings of the formula functions (Q32; the checker tests form only).

**Where a different reading of the grammar would change the key.**

- Q5: that `rej(Kai1)` declines both the request and the proposal and says nothing of the claim.
- Q10: that a claim used as a time (the first place of `after`) is not asserted.
- Q14: that `ent` asserts none of its claims, and that `hyp` and `supp` assert none either.
- Q15: that the claim of `clr` is not asserted, while the reason of `rej` and the claim of `err` are.
- Q27 and Q31: that a proposal inside `to(X, ...)` is sent to X only, and that `All` is the roster minus the sender at that time.
- Q28: that a retraction has force only for messages that follow it in the order of 2.3.
- Q32 (c): that `log(2,8)` is the logarithm of 2 to the base 8 (section 3.3 says `log(x,b)`, the logarithm of x to the base b).

**Threats to the meaning of the results.**

- One run per model and form is one sample; models vary from run to run. Repeat a cell (files may be named `Model_Rminus_2.txt`) before reading a small difference as real.
- Multiple choice lets a model score by luck; the strict score on multi-answer items (sets, lists, verdicts) is hard to reach by luck, and the scorer reports the chance level.
- A model may already know something of SILEX from training or from an earlier chat. Fresh chats with memory off are required (operator guide).
- The grammar is long (1,686 lines, about 163,000 characters). A model that reads it only in part, or an interface that hands it over in pieces, will miss items. Record how the grammar was given (section 5 of the operator guide); a low R+ score then says something about use, not about the language or the test.
- The items were designed around conventions an English reader cannot guess. Whether they do fail a model without the grammar is exactly what form R- measures; the 8 of 32 is a design target.
- The test measures reading and writing of single messages and of short conversations. It says nothing about long exchanges, about two models talking to each other, or about meaning beyond the rules.

## 10. Items used up

The calibration items used earlier with the four-model transcript (`conversations/SILEX_Conversation_Claude_ChatGPT_Grok_Gemini_Message_Bus.md`) are not reused here. If a model has seen the booklets before, record it and do not use its sheet as an unaided reading.
