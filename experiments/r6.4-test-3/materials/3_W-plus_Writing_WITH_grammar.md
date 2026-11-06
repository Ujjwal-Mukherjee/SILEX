# SILEX writing test: booklet W+ (with the reference grammar)

Form WB-1 · for SILEX r6.4 · body checksum 31742d8d1766

You have two documents: the reference grammar of SILEX r6.4 (attached or pasted before this booklet) and this booklet of writing tasks.

**Rules for this test**

1. Write in SILEX r6.4 exactly as the grammar defines it. Your lines are run through the language's checker (version r6.4) and then marked against what each task asks; a line that the checker rejects earns nothing.
2. You cannot run the checker. Before you answer, read your own lines against the rules of the grammar, one by one.
3. Work from the grammar and this booklet only. Do not use web search, code execution or any other tool, and do not use memory of earlier conversations. If a tool is switched on, leave it alone.
4. Do not ask anything back. Answer every task.
5. The format of your reply is in section 2 of the booklet. Reply once.

---

# SILEX writing test: the tasks

## 1. What this is

SILEX is a formal language in which AI agents write messages to each other. This booklet gives eight small writing tasks. For each one you write SILEX: a message, a few messages, or a few lines. The tasks are marked by running your lines through the language's own checker and then against what the task asks for.

Names that begin with a capital letter (Ana, Kai, Lena, ...) are agents. `Kai1` is the name of the first message sent by Kai, and `Kai1.2` is line 2 of that message. Where a task shows messages already sent, they are part of the conversation: they are correct, and your answer follows them. Do not copy them into your answer.

## 2. How to answer

For each task give a heading line with its id (`W1` to `W8`) and, under it, one fenced block (three backticks) holding your answer. Only the blocks are marked. In a block:

- a message is its header line followed by its lines. Where a task asks for two messages, put both in the one block, in the order asked, with a line of three hyphens (`---`) between them (the separator is not part of the language);
- write no comments, no numbering and no explanations inside a block;
- write for the situation the task describes. Where a task needs a date, work it out from the day the task gives.

A skeleton is at the end of the booklet.

---

## W1. A reply to two messages

Messages already sent (do not repeat them):

```text
msg(Kai,Lena,Milo,1)
pls(Milo,"drain tank three")
is("pump","leaking")
sug(at(2026-11-12,"replace pump"))
---
msg(Lena,Kai,Milo,1)
is("gauge","stuck")
is("tank three","empty")
yn(is("valve","open"))
```

Milo has read both messages above. Write **Milo's first message**, to Kai and Lena, as a reply to both. In it Milo:

1. agrees with Kai's proposal to replace the pump;
2. declines Kai's request to drain tank three, and gives as the reason that Milo is not permitted to open valve six;
3. tells Lena that her claim about tank three is wrong, and says what is so: tank three is full;
4. answers Lena's question: yes, the valve is open.

*Answer: one message (Milo's).*

## W2. Asserting and only mentioning

Today is Wednesday 2026-11-04. Write **Pia's first message**, to Quin and Rae. In it Pia:

1. says that she believes the cache is stale, without claiming that it is;
2. reports that Rae said the backup has finished, without claiming it herself;
3. states as a fact that the disk is full;
4. supposes, for the lines and messages that follow, that the deploy failed;
5. asks Quin to restart the cache by 5 pm on Friday;
6. proposes, to Quin and Rae together with herself, that deploys be frozen for the whole of Monday.

*Answer: one message (Pia's).*

## W3. Eight sentences, one line each

Write each sentence as **one line of SILEX**, with no header and no numbering. Give the eight lines in order, in one block. Write the formula in sentence 8 as a formula in single quotes.

1. Not every sensor is calibrated.
2. Exactly one of pump A and pump B is running.
3. Every tank except tank seven is sealed.
4. More than 40 percent of the samples are contaminated.
5. Every pump feeds some tank.
6. The cleanup job restarted three times between 01:00 and 05:00 on 2026-11-09.
7. Send me the report within an hour.
8. The sum of the squares of the first n positive integers is at most 91, and n is even.

*Answer: eight lines, in order, no header, no numbers.*

## W4. A step-by-step answer

Messages already sent (do not repeat them):

```text
msg(Ana,Ben,1)
assume('2*x-3=11')
what(val("x","value"))
```

Write **two messages**, in this order, in one block, with a line of three hyphens between them.

**Ben's first message**, a reply to Ana's: two steps that solve the equation, each resting on the line just before it (the first rests on Ana's supposition), each with a short reason in English; then the answer to Ana's question.

**Ana's second message**, a reply to Ben's: she checks Ben's result by putting it back into her equation (one step, with a reason, resting on the second of Ben's two steps), and agrees with Ben's answer line.

Write each formula in the written form of the language.

*Answer: two messages, Ben's then Ana's, with `---` between them.*

## W5. A program, a command and a corrected program

Write **two messages**, in this order, in one block, with a line of three hyphens between them.

**Ana's first message**, to Ben. Its three lines, in this order:

1. she sends this Python program, **without asking Ben to run it**, and gives it a name so that it can be pointed at later;
2. she asks Ben to review that program;
3. she asks Ben to **run** this shell command: `grep -c ERROR app.log`

```python
def label(n):
    if n == 0:
        return "none"
    return f"item {n}"
```

**Ben's first message**, a reply to Ana's. Its four lines, in this order:

1. he says that the program in Ana's message has a fault, and what the fault is: for a negative number it gives "item -3", and it should give "negative";
2. he sends this corrected program, under a name of his own, again without asking anyone to run it;
3. he asks Ana to use his program in place of hers;
4. he promises to run the shell command that Ana asked for.

```python
def label(n):
    if n == 0:
        return "none"
    if n < 0:
        return "negative"
    return f"item {n}"
```

*Answer: two messages, Ana's then Ben's, with `---` between them.*

## W6. Headers that fix an order

Three agents, Ana, Ben and Cy, write six messages. Every message goes to the other two agents. What each writer had read when writing:

- **Ana1**: Ana had read nothing.
- **Ben1**: Ben had read nothing.
- **Cy1**: Cy had read Ana1 and Ben1. It is a reply to Ana1.
- **Ana2**: Ana had read Cy1 (and so what Cy1 had read). It is a reply to Cy1.
- **Ben2**: Ben had read Ana1 and Cy1. It is a reply to Ana1. Ben had not read Ana2.
- **Cy2**: Cy had read Ana2 and Ben2. It is a reply to Ana2.

Write the **six headers only**, one per line, in the order Ana1, Ben1, Cy1, Ana2, Ben2, Cy2 (no other lines, no separators). Use `re` and `saw` so that a reader who applies the language's rules of order recovers **exactly** the order these facts give: every message that comes before another is shown to, and no message is made to come before another when the facts do not say so.

*Answer: six header lines, one per line, in the order Ana1, Ben1, Cy1, Ana2, Ben2, Cy2.*

## W7. A long name used in two messages

Today is Wednesday 2026-11-04. The thing that Kai talks about has a long name, "east wing cold storage freezer". The long name must be written **out in full only once**, and later lines must reach it by a name.

**Kai's first message**, to Lena and Milo: Kai says that the east wing cold storage freezer is above zero, and asks Lena to inspect it by 5 pm on Friday.

**Kai's second message**, to Lena and Milo: Kai asks Milo to move the samples out of that freezer. The long name must not be written out again; the line must reach the name that Kai's first message gave.

Write the two messages in this order, in one block, with a line of three hyphens between them.

*Answer: two messages, Kai's first then Kai's second, with `---` between them.*

## W8. A message that adds an agent

Messages already sent (do not repeat them):

```text
msg(Dee,Eli,Fay,1)
is("checkout","down")
hyp(cause("cache layer","outage"))
what(val("database","replication lag"))
---
msg(Eli,Dee,Fay,1,re(Dee1))
ans(3,2)
```

Write **Dee's second message**. It goes to Eli and Fay and also to Gus, who joins the conversation in this same message. Dee has read Eli's message. In it Dee:

1. puts Gus on the roster;
2. asks Gus, and nobody else, to restart the cache;
3. takes back her hypothesis (line 2 of her first message);
4. says that Eli's answer is unclear: she does not know in what unit the figure is given.

*Answer: one message (Dee's second).*

---

## The answer to send back

W1
```
(your answer to W1)
```

W2
```
(your answer to W2)
```

W3
```
(your answer to W3)
```

W4
```
(your answer to W4)
```

W5
```
(your answer to W5)
```

W6
```
(your answer to W6)
```

W7
```
(your answer to W7)
```

W8
```
(your answer to W8)
```

End of booklet.
