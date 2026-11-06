# SILEX reading test: booklet R- (no reference)

Form RB-1 · for SILEX r6.4 · body checksum edcec880d947

You have one document: this booklet of questions. No reference for the language is provided, and none is to be looked for.

**Rules for this test**

1. Answer from this booklet and from what you already know. The right answer to every question is the one the rules of the language give; where you cannot be sure what those rules are, give your best judgment.
2. Do not use web search, code execution or any other tool, and do not use memory of earlier conversations. If a tool is switched on, leave it alone.
3. Do not ask anything back. Answer every question; when you are unsure, give your best answer and a low number.
4. The format of your reply is in section 2 of the booklet. Reply once, with your answers in the final block.

---

# SILEX reading test: the questions

## 1. What this is

SILEX is a formal language in which AI agents write messages to each other. This booklet shows short pieces of SILEX and asks what they mean, whether they are well formed, and what follows from them. Every question has one right answer, given by the rules of the language itself.

**How pieces are shown.**

- A block that begins with `msg(` shows one message, or several; the `msg(...)` line is the header of a message. Inside a block, a line of three hyphens (`---`) ends one message and begins the next; it is a separator of this booklet and is not part of the language. Several messages in one block are a conversation.
- A block with no `msg(` line shows lines of some message whose header is not shown.
- Words that begin with a capital letter (Ana, Kai, Lena, ...) are agents. Text between double quotation marks is English.
- `Kai1` is the name of the first message sent by Kai, and `Kai1.2` is line 2 of that message.

**The checker.** Some questions ask for the verdict of the checker. The checker is a program that reads the lines of a message, in the context of its message and its conversation, and gives each line exactly one verdict word:

| Verdict | Meaning |
| --- | --- |
| `ok` | the line is well formed |
| `E-SYN` | the line is not a well-formed expression (for example a bracket or a quotation mark is left open) |
| `E-LEX` | the line uses a word that the language does not have |
| `E-ARITY` | a word of the language is given the wrong number of arguments |
| `E-KIND` | something stands where a thing of that kind is not allowed |
| `E-NAME` | a name that was never defined is used |
| `E-REDEF` | a name is defined twice |
| `E-HEAD` | something is wrong with a header |
| `E-TIME` | a time that cannot exist |
| `E-QUOTE` | a quotation (text in double quotation marks) breaks the language's rules for what may stand in it |
| `E-CODE` | something is wrong inside a program carried by `code(...)` |
| `E-MATH` | a formula in single quotation marks is not well formed |

## 2. How to answer

Give your answers in one block at the very end of your reply, one line for each question Q1 to Q32, in this form:

```text
Q7: B | 80
```

- Before the bar is your answer. For a question with lettered options and one right answer, one capital letter. For a question that says "choose all that apply", the lower-case letters that apply, separated by commas (for example `a,c`). For a question that asks for a list or for verdicts, the entries separated by commas, in order.
- After the bar is a whole number from 0 to 100: your own chance, in percent, that the whole answer to that question is exactly right.
- Answer every question. If you do not know, give your best answer and a low number.
- You may reason before the block. Only the block is scored, except that the open question Z1 is answered in plain English above the block.

A skeleton of the block is at the end of the booklet.

---

## Part A. Warm-up

### Q1

What does Kai do in line 1?

```text
msg(Kai,Nora,1)
pls(Nora,"label sample tubes")
```

- **A.** Promises to label sample tubes.
- **B.** Reports that Nora labelled sample tubes.
- **C.** Declines to label sample tubes.
- **D.** Asks Nora to label sample tubes.
- **E.** Proposes that the two of them label sample tubes.

*Answer: one capital letter.*

### Q2

What does this line say?

```text
none("sample tubes","labelled")
```

- **A.** Every sample tube is labelled.
- **B.** No sample tube is labelled.
- **C.** At least one sample tube is labelled.
- **D.** Sample tubes may be labelled.
- **E.** Some sample tubes are labelled, some not.

*Answer: one capital letter.*

### Q3

Which reading of this header is right?

```text
msg(Milo,Kai,Lena,3,re(Kai2))
```

- **A.** Milo writes to Kai and Lena; it is Milo's second message; it answers Kai's third message.
- **B.** Milo writes to Kai, with Lena as a copy; it is the third message of the conversation; it answers message 2.
- **C.** Milo writes to Kai and Lena; it is Milo's third message; it answers Kai's second message.
- **D.** Kai writes to Milo and Lena; it is Kai's second message; it answers Milo's third message.
- **E.** Milo writes to Kai, Lena and a third person; it is the third message sent by anyone.

*Answer: one capital letter.*

## Part B. What one line says

### Q4

Which pair of statements is right about these two lines?

```text
msg(Rae,Kai,1)
at(2026-11-09T01:00/2026-11-09T05:00,is("freezer","above zero"))
during(2026-11-09T01:00/2026-11-09T05:00,is("alarm","ringing"))
```

- **A.** Both lines say the same: the thing named held all through the period.
- **B.** Both lines say the same: the thing named happened at some time within the period.
- **C.** Line 1: the freezer rose above zero at 01:00. Line 2: the alarm stopped ringing at 05:00.
- **D.** Line 1: the freezer was above zero at some time within that period. Line 2: the alarm rang all through it.
- **E.** Line 1: the freezer was above zero all through that period. Line 2: the alarm rang at some time within it.

*Answer: one capital letter.*

### Q5

What does Milo decline with the line `rej(Kai1)`?

```text
msg(Kai,Milo,Lena,1)
is("error rate","high")
pls(Milo,"pause nightly job")
sug(at(2026-11-10,"roll back release"))
---
msg(Milo,Kai,Lena,1,re(Kai1))
rej(Kai1)
```

- **A.** Nothing yet: `rej` must name a line, not a whole message, so the reply is incomplete.
- **B.** Lines 1, 2 and 3: he declines the request and the proposal, and he also denies that the error rate is high.
- **C.** Only line 2, the request to him; the proposal in line 3 and the claim in line 1 are left alone.
- **D.** Lines 2 and 3, the request and the proposal. Line 1, a claim, is not denied.
- **E.** Only line 1: he says that the error rate is not high, because `rej` is the root for denying a claim.

*Answer: one capital letter.*

### Q6

Something is wrong with Nora's reply. What?

```text
msg(Kai,Nora,1)
yn(is("pump","running"))
pls(Nora,"flush line two")
what(cnt("open valves"))
---
msg(Nora,Kai,1,re(Kai1))
ans(2,"flush finished")
```

- **A.** A bare number cannot stand inside `ans`; Nora must write the full reference, Kai1.2.
- **B.** `ans` takes the answer first and the line number second; Nora has put them the wrong way round.
- **C.** `ans` answers only a question, and line 2 is a request; a request is met with a promise or a refusal.
- **D.** The number should be 3, because it is line 3 that holds the question Nora means to answer.
- **E.** Nothing is wrong: line 2 asked for a flush, and `ans` is the root for reporting that it is finished.

*Answer: one capital letter.*

### Q7

In Milo's line 1, what does `{o1}` refer to?

```text
msg(Lena,Milo,1)
is(o1"pump in bay four","leaking")
---
msg(Milo,Lena,1,re(Lena1))
pls(Lena,"shut valve of {o1}")
```

- **A.** Whatever Milo himself names o1 later in the conversation; the latest definition wins.
- **B.** The pump in bay four, which Lena named o1; a name is shared by all the messages of a conversation.
- **C.** An unnamed object: `o1` is a placeholder for the next thing that is mentioned.
- **D.** Nothing: o1 is Lena's name and exists only in her message, so Milo would have to write {Lena1.o1}.
- **E.** The pump in bay four, because Milo's message answers Lena's and so shares its names.

*Answer: one capital letter.*

### Q8

Who gets line 2, and who is asked to act?

```text
msg(Nora,Kai,Lena,Milo,2)
is("tank three","empty")
to(Lena,pls("refill tank three"))
```

- **A.** Kai, Lena and Milo all get it, and all three are asked.
- **B.** Kai, Lena and Milo all get it, but only Lena is asked.
- **C.** Lena is asked; Kai and Milo get the message but without line 2.
- **D.** Only Lena gets line 2, and she is the one asked.
- **E.** Lena is asked; Kai and Milo are blocked from seeing the line.

*Answer: one capital letter.*

### Q9

How is line 1 read?

```text
msg(Nora,Kai,Lena,2)
if(is(You,"on call"),pls(You,"check alarm panel"))
```

- **A.** The condition is tested separately for Kai and for Lena; each one for whom it holds is asked.
- **B.** The condition is tested once for Kai and Lena together; if it holds, both of them are asked.
- **C.** Only the first receiver, Kai, is tested, and only he can be asked.
- **D.** Nora asks herself, because `You` stands for the sender's partner in a one-to-one exchange.
- **E.** The line is faulty, because `You` cannot stand inside `if` when there are two receivers.

*Answer: one capital letter.*

### Q10

What does line 1 assert?

```text
msg(Rae,Kai,1)
after(fin("calibration"),act(Omar,"start run"))
```

- **A.** Nothing at all: the whole line is a condition, and a condition states no fact.
- **B.** That Omar's run comes after the end of calibration, which may or may not have ended.
- **C.** That Omar started a run before calibration finished: the first place is what comes later.
- **D.** That calibration and Omar's run start at the same moment, so they are simultaneous.
- **E.** That calibration has finished, and that Omar has started a run after the end of it.

*Answer: one capital letter.*

### Q11

Ben receives this line. What can he conclude?

```text
msg(Ana,Ben,1)
plan(grp(Me,You),at(2026-11-12,"hold review"))
```

- **A.** Ana alone has committed herself to hold the review; Ben is only told of it.
- **B.** Ana and Ben have agreed to hold the review on 2026-11-12; the plan records their agreement.
- **C.** Ana asks Ben to hold the review; a plan of the two of them is a form of request to him.
- **D.** Ana proposes the review, and nothing is adopted until Ben replies with an agreement.
- **E.** Ana says that the two of them plan this; Ben's agreement is not shown and would be an `agree`.

*Answer: one capital letter.*

### Q12

What does this line say?

```text
some("jobs",crit(o1,all("queues",crit(o2,is(o1,"writes to",o2)))))
```

- **A.** Some job writes to every queue.
- **B.** Every queue is written to by some job.
- **C.** Every job writes to some queue.
- **D.** No job writes to any queue.
- **E.** Some queue is written to by every job.

*Answer: one capital letter.*

## Part C. Asserted, or only mentioned

### Q13

Which statements does Pia assert as true in her message? Do not count what she only believes, reports, supposes or weighs. Choose all that apply.

```text
msg(Pia,Quin,Rae,1)
bel(Me,is("cache","stale"))
know(Me,is("disk","full"))
say(Rae,fin("backup"))
cause(is("deploy","failed"),is("service","down"))
hyp(is("firewall","misconfigured"))
prob(is("fix","working"),0.9)
supp(is("light","on"),is("guard","home"))
```

- **a.** The backup has finished.
- **b.** The fix is working.
- **c.** The service is down.
- **d.** The guard is home.
- **e.** The disk is full.
- **f.** The cache is stale.
- **g.** The deploy failed.
- **h.** The firewall is misconfigured.

*Answer: the lower-case letters that apply, separated by commas (for example `a,c`).*

### Q14

Which of these claims does Ben assert in his message? Choose all that apply.

```text
msg(Ana,Ben,1)
assume('4*w+1=17')
what(val("w","value"))
---
msg(Ben,Ana,1,re(Ana1))
ent(Ana1.1,'4*w=16',"subtract 1 from both sides")
'w=4'
hyp('w=5')
supp('w=4','w>0')
ent(Ben1.2,'4*4+1=17',"substitute 4 for w")
ans(2,4)
```

- **a.** 4*w=16
- **b.** w=5
- **c.** w>0
- **d.** w=4
- **e.** 4*4+1=17

*Answer: the lower-case letters that apply, separated by commas (for example `a,c`).*

### Q15

Which statements does Lena assert as true? Choose all that apply.

```text
msg(Lena,Kai,Milo,2)
rej(Kai1.1,not(may(Me,"open vault")))
err(Kai1.2,is("valve","closed"))
clr(Kai1.3,is("sensor","faulty"))
if(is("alarm","ringing"),pls(Kai,"leave room"))
would(not(fin("flush")),is("sample","ruined"))
want(Me,fin("audit"))
```

- **a.** The alarm is ringing.
- **b.** The sensor is faulty.
- **c.** Lena may not open the vault.
- **d.** The audit has finished.
- **e.** The valve is closed.
- **f.** The sample is ruined.

*Answer: the lower-case letters that apply, separated by commas (for example `a,c`).*

## Part D. References, numbers and order

### Q16

Milo replies to Kai3 with the second message below. Which line of Kai3 does `agree(3)` mean?

```text
msg(Kai,Lena,Milo,3,re(Lena2))
sug(at(2026-11-12,"drain tank"))
pls(Lena,"read gauge")
# status check

is("tank","full")
will("log level")
yn(is("gauge","stuck"))
```

```text
msg(Milo,Kai,Lena,2,re(Kai3))
agree(3)
```

- **A.** sug(at(2026-11-12,"drain tank"))
- **B.** pls(Lena,"read gauge")
- **C.** is("tank","full")
- **D.** will("log level")
- **E.** yn(is("gauge","stuck"))

*Answer: one capital letter.*

### Q17

Ana1 has three lines and Cy1 has two. Ben has sent nothing before. He writes five different replies, each containing the line `agree(2)`. Only the header differs. For each reply give the line that `agree(2)` stands for, written in full (for example Ana1.1), or the word `error` if the language does not allow the short form there.

```text
(a) msg(Ben,Ana,Cy,1,re(Ana1))
(b) msg(Ben,Ana,Cy,1,re(Ana1,Cy1))
(c) msg(Ben,Ana,Cy,1,re(Ana1.2))
(d) msg(Ben,Ana,Cy,1,saw(Ana1))
(e) msg(Ben,Ana,Cy,1,re(Cy1),saw(Ana1))
```

*Answer: five entries for (a) to (e), separated by commas, each a full line name or the word `error`.*

### Q18

Which statements must be true? Choose all that apply.

```text
msg(Cy,Ana,Ben,2,saw(Ben2))
```

- **a.** This message is a reply to Ben2.
- **b.** When writing this message, Cy had read Ben3.
- **c.** When writing this message, Cy had read Ben1.
- **d.** This message comes after Cy1, Cy's own first message.
- **e.** When writing this message, Cy had read Ben2.

*Answer: the lower-case letters that apply, separated by commas (for example `a,c`).*

## Part E. Verdicts of the checker

### Q19

Give the verdict of the checker for each of the eight lines below the header of this message, in order.

```text
msg(Nora,Kai,Lena,1)
pls(Kai,"clean the filter")
pls(Lena,"send readings of 2026-11-09 to {Me}")
will("order spare parts tomorrow")
pls(Kai,"say ""stop"" when pump is hot")
pls(Lena,"refill {o3}")
is("other tank","empty")
will("keep my notes")
pls(Lena,"refill {o3")
```

*Answer: 8 verdict words, separated by commas, in order.*

### Q20

Give the verdict for each of the seven lines, in order.

```text
msg(Nora,Kai,Lena,2)
will(Kai,"refill tank")
promise("refill tank")
not(pls(Kai,"refill tank"))
and(is(o1"inlet pump","on"),is(o1"outlet pump","on"))
is("tank","full"
val("tank","volume in litres")
all("tanks","full")
```

*Answer: 7 verdict words, separated by commas, in order.*

### Q21

Give the verdict for each of the seven lines, in order.

```text
msg(Nora,Kai,Lena,3)
by(20261112T0900,fin("audit"))
by(20261112,fin("audit"))
at(2027-02-29,fin("audit"))
at(2028-02-29,fin("audit"))
for(3,is("pump","off"))
for(PT3H,is("pump","off"))
at(2026-11-31,fin("audit"))
```

*Answer: 7 verdict words, separated by commas, in order.*

### Q22

Give the verdict for each of the eight lines, in order.

```text
msg(Nora,Kai,Lena,4)
will(code("ruby","puts 1"))
pls(Kai,code("python","print(""the total is {n}"")"))
will(code("python","for i in range(3)","    print(i)"))
'n>1 or n<-1'
'2*n+1'
'n>1 | n<-1'
'x=.5'
code("bash","tar xf logs.tar")
```

*Answer: 8 verdict words, separated by commas, in order.*

### Q23

Nora4 answers Kai3 and has the header below. Assume that Kai3 and Nora3 both exist and each has at least two lines. Give the verdict for each of the six lines, in order.

```text
msg(Nora,Kai,Lena,4,re(Kai3))
agree(2)
ack(2)
re(Kai3)
to(Milo,pls("refill tank"))
retr(Nora3.1)
retr(1)
```

*Answer: 6 verdict words, separated by commas, in order.*

### Q24

Each of the seven lines below is the header of a different message. Judge each header on its own and give its verdict, in order.

```text
1. msg(Nora,Kai,Kai,5)
2. msg(Nora,All,5)
3. msg(Nora,All,Kai,5)
4. msg(Me,Kai,5)
5. msg(Nora,Kai,5,re(Nora5))
6. msg(Nora,Kai,5,saw(Kai4),pri(lo))
7. msg(Nora,Kai,5,pri(urgent))
```

*Answer: 7 verdict words, separated by commas, in order.*

## Part F. Whole conversations

### Conversation C1

Used by Q25, Q26 and Q27. The messages are listed in one possible order of arrival; the times, where there are any, are the send times in the headers.

```text
msg(Kai,Lena,Milo,Nora,1,2026-11-10T08:00)
sug(at(2026-11-10T09:00,"roll back release"))
to(Nora,sug("pause deploys"))
---
msg(Lena,Kai,Milo,Nora,1,2026-11-10T07:58)
sug("wait for patch")
---
msg(Milo,Kai,Lena,Nora,1,2026-11-10T08:05,re(Kai1))
agree(1)
---
msg(Nora,Kai,Lena,Milo,1,2026-11-10T08:06)
is("deploy queue","empty")
---
msg(Lena,Kai,Milo,Nora,2,2026-11-10T08:10)
agree(Kai1.1)
---
msg(Nora,Kai,Lena,Milo,2,2026-11-10T08:12,saw(Lena2))
agree(Kai1.2)
```

### Q25

Conversation C1. Which of these pairs of messages are concurrent, that is, neither comes before the other according to the language? Choose all that apply.

- **a.** Lena2 and Nora2
- **b.** Lena1 and Nora2
- **c.** Milo1 and Lena2
- **d.** Kai1 and Lena2
- **e.** Nora1 and Lena2
- **f.** Kai1 and Lena1
- **g.** Milo1 and Nora2
- **h.** Kai1 and Nora1

*Answer: the lower-case letters that apply, separated by commas (for example `a,c`).*

### Q26

Conversation C1. Which messages come before Nora2 according to the language (they precede it, directly or through a chain)? Choose all that apply.

- **a.** Kai1
- **b.** Lena1
- **c.** Milo1
- **d.** Nora1
- **e.** Lena2

*Answer: the lower-case letters that apply, separated by commas (for example `a,c`).*

### Q27

Conversation C1. Which of these proposals are adopted by the end of the conversation? Choose all that apply.

- **a.** Kai1.1, the rollback proposal
- **b.** Kai1.2, the proposal to pause deploys
- **c.** Lena1.1, the proposal to wait for the patch

*Answer: the lower-case letters that apply, separated by commas (for example `a,c`).*

### Conversation C2

Used by Q28 and Q29. The messages are listed in one possible order of arrival; the times, where there are any, are the send times in the headers.

```text
msg(Pia,Quin,Rae,1,2026-11-11T09:00)
fin("ledger backup","successfully")
yn(is("disk","healthy"))
---
msg(Pia,Quin,Rae,2,2026-11-11T09:20)
retr(Pia1.1)
---
msg(Quin,Pia,Rae,1,2026-11-11T09:25,re(Pia1))
pls(Rae,"delete old ledger copy")
ans(2,yes)
---
msg(Rae,Pia,Quin,1,2026-11-11T09:30,saw(Pia2,Quin1))
rej(Quin1.2,not(know(Me,fin("ledger backup","successfully"))))
---
msg(Quin,Pia,Rae,2,2026-11-11T09:40,re(Pia2))
retr(Quin1.1)
```

### Q28

Conversation C2. Pia2 takes back Pia1.1. For each of Quin1, Rae1 and Quin2 say whether the retraction has force for it (the message follows Pia2) or whether the message may still rest on the retracted line (it does not follow Pia2). Answer with three words, `force` or `rest`, in the order Quin1, Rae1, Quin2.

*Answer: 3 words, separated by commas, in order.*

### Q29

Conversation C2. In Rae1, Rae wants to decline Quin's request to delete the old ledger copy. Is the reference in her `rej` right?

- **A.** No: the delete request is Quin1.1, and Quin1.2 is the `ans` line.
- **B.** No: `rej` may point only at a line of the message that the reply answers, and Rae1 has no `re`.
- **C.** `rej` cannot point at a line, only at a whole message, so it should name Quin1.
- **D.** Yes: Quin1.2 is the delete request, the second line of Quin's message.
- **E.** No: Rae must write the short form `rej(1,…)`, since she is answering a single message.

*Answer: one capital letter.*

### Conversation C3

Used by Q30 and Q31. The messages are listed in one possible order of arrival; the times, where there are any, are the send times in the headers.

```text
msg(Dee,Eli,Fay,1)
is("gateway","down")
---
msg(Dee,Eli,Fay,Gus,2)
join(Gus)
to(Gus,pls("restart cache"))
---
msg(Eli,Dee,Fay,1,re(Dee2))
is("cache","stale")
---
msg(Fay,All,1,re(Eli1))
sug("freeze deploys")
```

### Q30

Conversation C3. Which of the four messages does Gus receive? Choose all that apply.

- **a.** Dee1
- **b.** Dee2
- **c.** Eli1
- **d.** Fay1

*Answer: the lower-case letters that apply, separated by commas (for example `a,c`).*

### Q31

Conversation C3. For Fay's proposal Fay1.1 to be adopted, which agents must have said `agree` to it? Choose all that apply.

- **a.** Dee
- **b.** Eli
- **c.** Fay
- **d.** Gus

*Answer: the lower-case letters that apply, separated by commas (for example `a,c`).*

## Part G. Formulas

### Q32

Read each formula by the written forms and agreed meanings of the language. Which of these formulas state something true? Choose all that apply.

- **a.** 'mod(17,5)=3'
- **b.** '-3^2=9'
- **c.** '2^3^2=512'
- **d.** '1=2 & 2=2 => 3=4'
- **e.** 'log(2,8)=3'
- **f.** 'prod(i,i,1,4)=24'
- **g.** 'int(2*x,x,0,3)=6'
- **h.** '1=1 | 1=2 & 2=3'

*Answer: the lower-case letters that apply, separated by commas (for example `a,c`).*

## Open question

### Z1

Open question. In plain English, say what each line of this message says, who is addressed, what is asserted and what is only mentioned or asked. Write your account above your final answer block (not inside it). It is marked by hand.

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

---

## The block to send back

```text
Q1: _ | _
Q2: _ | _
Q3: _ | _
Q4: _ | _
Q5: _ | _
Q6: _ | _
Q7: _ | _
Q8: _ | _
Q9: _ | _
Q10: _ | _
Q11: _ | _
Q12: _ | _
Q13: _ | _
Q14: _ | _
Q15: _ | _
Q16: _ | _
Q17: _, _, _, _, _ | _
Q18: _ | _
Q19: _, _, _, _, _, _, _, _ | _
Q20: _, _, _, _, _, _, _ | _
Q21: _, _, _, _, _, _, _ | _
Q22: _, _, _, _, _, _, _, _ | _
Q23: _, _, _, _, _, _ | _
Q24: _, _, _, _, _, _, _ | _
Q25: _ | _
Q26: _ | _
Q27: _ | _
Q28: _, _, _ | _
Q29: _ | _
Q30: _ | _
Q31: _ | _
Q32: _ | _
```

Write your account of Z1 in plain English above the block. End of booklet.
