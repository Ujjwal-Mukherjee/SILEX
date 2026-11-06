# SILEX r6.4 test 2, paper B (writing)

You have been given a file that describes a language called SILEX (version r6.4). Read it first. In this paper you write SILEX. Your lines will be run through the r6.4 checker afterwards, and a script will check who answers whom and who has read what. You cannot run the checker yourself; write with care. Do not run any program.

**Conventions.**
- A message is named by its sender and its serial: `Ana1` is the first message of Ana, `Ana2` her second. Each agent counts its own messages from 1.
- The agents named in an item are on the roster from the first message of that item, so address the first message to everyone who takes part in the item (by name, or `All`).
- Say who has read what in the way the language provides. Do not claim that an agent has read a message the item does not say it has read.
- Inside quotation marks, write English by the rules of the language description.

**Items B1 to B8.** Write the whole exchange: every message, with its header and its lines. Put each item's messages in one block, with the item's label on the row above it, like this:

B1
```dialogue
msg(...)
...
---
msg(...)
...
```

**Items D1 to D4.** The conversation so far is given. Write only the one new message that is asked for, in a block with the item's label above it. Do not repeat the given messages.


## Items B1 to B8

**B1.** Agents: Ana, Ben, Cy.

Ana sends Ben and Cy a message asking Ben to start the pump. Cy, who has not yet read Ana's message, writes to Ben asking him not to start it. Ben has read both messages: he declines Ana's request, giving as his reason that the pipe is blocked, and he promises not to start the pump.

**B2.** Agents: Ana, Ben, Cy, Dan.

Ana tells everyone that the freezer is cold. Ben has read her message and agrees with it. Cy says that the freezer is warm; Cy has read neither of those messages. Dan has read Ben's message and Cy's message, and asks everyone whether the freezer is cold.

**B3.** Agents: Ana, Ben, Cy, Dan.

Ana sends one message to the other three with two proposals: line 1 proposes to move the meeting to Monday, line 2 proposes to invite Dan. Ben has read it and agrees with the second proposal only. Cy has read it and agrees with both proposals. Dan has read it and agrees with the second proposal only. None of the three has read the others' replies.

**B4.** Agents: Ana, Ben, Cy.

Ben tells Ana and Cy that the sample is labelled. In a second message, which names no other message, he takes that claim back because it was wrong. Cy has read Ben's first message but not his second, and asks Ana to relabel the sample. Ana has read both of Ben's messages and Cy's message; she declines Cy's request, giving as her reason that she does not know that the sample is labelled.

**B5.** Agents: Ana, Ben, Cy.

Ana proposes to Ben and Cy to test on Monday. Cy, who has not yet read Ana's message, proposes to Ana and Ben to test on Friday. Ben has read both messages: he agrees with Ana's proposal and declines Cy's. Cy then reads Ben's message and agrees with Ana's proposal.

**B6.** Agents: Ana, Ben.

Ana sends Ben one message with two questions: line 1 asks whether the freezer is full, line 2 asks what its temperature is. Ben answers both: yes, and the temperature is 4.

**B7.** Agents: Ana, Ben, Cy.

Ana makes two claims in one message to Ben and Cy: line 1 says the pump is on, line 2 says the valve is open. Ben has read it and tells her that line 2 is wrong, giving the reason that the valve is shut. Ana then reads Ben's message and takes line 2 back, and says that the valve is shut. Cy has read only Ana's first message; without having read Ben's message or Ana's second, he agrees with Ana's line 2.

**B8.** Agents: Ana, Ben, Cy.

Ana sends one message to Ben and Cy. Line 1 asks Ben to merge the release branch. Line 2 is for Cy only: it asks Cy to review the merge. Ben replies that he will merge the branch. Cy, without having read Ben's reply, declines the review request, giving as her reason that she has no access.


## Items D1 to D4

**D1.** Agents: Ana, Ben, Cy. You are writing for **Ben**, who has read every message above.

The conversation so far:

```dialogue
msg(Ana,Ben,Cy,1)
is("freezer","full")
yn(is("backup","finished"))
what(val("freezer","temperature"))
pls(Ben,"order reagent")
---
msg(Cy,Ana,Ben,1,re(Ana1))
ans(Ana1.2,yes)
```

What Ben knows: The freezer temperature is 4. Ben cannot order the reagent, because the supplier is closed.

Write Ben's next message to Ana and Cy. Answer each question that nobody has answered yet, and answer the request.

**D2.** Agents: Ana, Ben, Cy. You are writing for **Ben**, who has read Ana1 and Cy1 only. Ana2 reached Ben only after he had written, so he has not read it..

The conversation so far:

```dialogue
msg(Ana,Ben,Cy,1)
sug("move test to Monday")
---
msg(Cy,Ana,Ben,1,re(Ana1))
agree(Ana1.1)
---
msg(Ana,Ben,Cy,2,saw(Cy1))
yn(is("sample","ready"))
```

What Ben knows: Ben agrees with the proposal. The sample is ready.

Write Ben's first message to Ana and Cy.

**D3.** Agents: Ana, Ben, Cy. You are writing for **Ben**, who has read every message above.

The conversation so far:

```dialogue
msg(Cy,Ana,Ben,1)
yn(is("sample","ready"))
pls(Ben,"label sample")
---
msg(Ana,Ben,Cy,1,re(Cy1))
agree(Cy1.2)
```

What Ben knows: The sample is ready. Ben agrees to label it.

Write Ben's next message to Ana and Cy. Answer what can be answered and respond to what was asked.

**D4.** Agents: Ana, Ben, Cy. You are writing for **Ben**, who has read every message above.

The conversation so far:

```dialogue
msg(Ben,Ana,Cy,1)
is("pump","on")
is("valve","open")
---
msg(Ana,Ben,Cy,1,re(Ben1))
yn(is("valve","open"))
```

What Ben knows: Ben has just checked: the valve is shut, so line 2 of his first message was wrong.

Write Ben's next message to Ana and Cy. Answer the question, and deal with the wrong line.
