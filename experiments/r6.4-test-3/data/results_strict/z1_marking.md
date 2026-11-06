# Z1: accounts to mark by hand

Mark each account against the nine points below: 1 if the account has the point right, 0 if it is missing or wrong. The accounts carry codes, not model names. The codes are in z1_codes.json; do not open that file before marking.

| # | Point |
| --- | --- |
| 1 | Header: from Rae to Kai and Lena; Rae's third message; urgent (pri hi). |
| 2 | It answers Kai2 (re) and Rae had read Lena1 (saw). |
| 3 | agree(2) means agree with line 2 of Kai2 (short form, because re names exactly one whole message). |
| 4 | rej(1,...) declines line 1 of Kai2 (a request or proposal); the reason, that Rae may not open the vault, is asserted. |
| 5 | The seal-caused-leak line is a hypothesis: not asserted; Rae suspects it. |
| 6 | prob(...,lo): the sender puts it at low probability (unlikely); still not asserted as fact. |
| 7 | The if line is tested separately for Kai and for Lena (You per receiver): each who is on call is asked to check the seal. |
| 8 | after(fin("flush"),...) says Kai samples water after the flush ends; it does not assert that the flush has finished. |
| 9 | sug(...) proposes replacing the seal at 10:00 on 2026-11-12 for the sender and the receivers; nothing is adopted until both Kai and Lena have agreed. |

The message under question:

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

## Z1-A

```text
Z1 account

Rae’s message 3 is addressed to both Kai and Lena (high priority). It answers Kai2 (so bare line numbers refer to lines of Kai2) and records that Rae had already read Lena1.

- Line 1 (`agree(2)`): Rae agrees with line 2 of Kai2. This is a speech act of agreement; it asserts nothing further about the content of that line.
- Line 2 (`rej(1, not(may(Me,"open vault")))`): Rae declines whatever request or proposal occupies line 1 of Kai2. The reason is asserted: Rae may not open the vault. A claim (if line 1 of Kai2 is one) is not thereby denied.
- Line 3 (`hyp(cause("seal","leak"))`): Rae offers the hypothesis that the seal caused a leak. The causal claim is only mentioned, not asserted.
- Line 4 (`prob(cause("seal","leak"), lo)`): Rae assigns low probability to the same causal claim. The claim itself is only mentioned.
- Line 5 (`if(is(You,"on call"), pls(You,"check seal"))`): The condition is tested separately for each receiver. For whichever of Kai or Lena is on call, that agent is asked to check the seal. Neither the condition nor the request is asserted unconditionally.
- Line 6 (`after(fin("flush"), act(Kai,"sample water"))`): Rae asserts that Kai’s sampling of water occurs after the flush finishes. The finishing of the flush is used only to name a time and is not itself asserted to have occurred.
- Line 7 (`sug(at(2026-11-12T10:00, "replace seal"))`): Rae proposes that the seal be replaced at the stated time. The proposal is made to the receivers (and to Rae); nothing is adopted until the receivers agree.

Only the agreement, the reason inside the rejection, and the temporal claim about Kai’s sampling are asserted. Everything else is mentioned, hypothesised, probabilistic, conditional, or merely proposed.
```

Marks (1 or 0) for points 1 to 9: _ _ _ _ _ _ _ _ _     total: _

## Z1-B

```text
Z1
The header indicates that Rae is sending her third message, addressed to Kai and Lena. It is marked as high priority, is a direct reply to Kai's second message (Kai2), and notes that Rae has already seen Lena's first message (Lena1).
 * Line 1 (agree(2)): Rae agrees to line 2 of Kai2 (which was likely a request or proposal). This is an agreement, not an assertion of fact.
 * Line 2 (rej(1,not(may(Me,"open vault")))): Rae rejects line 1 of Kai2. In doing so, she explicitly asserts as a fact that she is not permitted to open the vault.
 * Line 3 (hyp(cause("seal","leak"))): Rae hypothesizes that the seal caused the leak. This causal link is only supposed or mentioned for consideration, not asserted as a definitive fact.
 * Line 4 (prob(cause("seal","leak"),lo)): Rae weighs the probability of the seal having caused the leak as low. This is an evaluation or estimate, not an asserted fact.
 * Line 5 (if(is(You,"on call"),pls(You,"check seal"))): Rae makes a conditional request directed at the recipients. For each recipient individually, if they are on call, she asks them to check the seal. The condition of being on call is merely tested/mentioned, not asserted as true.
 * Line 6 (after(fin("flush"),act(Kai,"sample water"))): Rae asserts a temporal truth: that Kai's action of sampling the water takes place after the flush finishes.
 * Line 7 (sug(at(2026-11-12T10:00,"replace seal"))): Rae proposes that the seal be replaced at 10:00 on November 12, 2026. This is a proposal presented for agreement, not a fact asserted as true.
```

Marks (1 or 0) for points 1 to 9: _ _ _ _ _ _ _ _ _     total: _

## Z1-C

```text
**Z1: what the message says**

This is Rae's third message, sent to Kai and Lena. It answers Kai2, Rae had read Lena1 when writing it, and it is marked high priority. Because `re` names exactly one whole message, the bare numbers in lines 1 and 2 are lines of Kai2.

1. `agree(2)`: Rae agrees with line 2 of Kai2.
2. `rej(1,…)`: Rae declines the request or proposal in line 1 of Kai2. She asserts the reason: she is not permitted to open the vault.
3. `hyp(…)`: Rae offers the hypothesis that the seal caused the leak. This is not asserted.
4. `prob(…,lo)`: Rae says it is unlikely that the seal caused the leak. She asserts only her low-probability judgment, not the cause itself.
5. `if(…)`: this conditional request is tested separately for Kai and for Lena. Whoever is on call is asked to check the seal. Neither "someone is on call" nor the request alone is asserted.
6. `after(…)`: Rae asserts that Kai samples the water at a time after the flush finishes. The flush finishing only gives the time and is not asserted.
7. `sug(…)`: Rae proposes, for herself and the receivers, to replace the seal at 10:00 on 12 November. It is not adopted until Kai and Lena have both agreed.

Nothing is a question, and no line is addressed to only one receiver.
```

Marks (1 or 0) for points 1 to 9: _ _ _ _ _ _ _ _ _     total: _

## Z1-D

```text
### Z1. Interpretation of the SILEX message

### Message header

`msg(Rae,Kai,Lena,3,re(Kai2),saw(Lena1),pri(hi))`

This is Rae's third message, addressed to both Kai and Lena. It replies to Kai's second message (`Kai2`) and records that Rae has read Lena's first message (`Lena1`). Its priority is high.

The header establishes that Rae3 follows Kai2, Lena1, and Rae's own earlier messages. It does not establish that Kai2 precedes Lena1 or vice versa.

### Line-by-line interpretation

Line 1: `agree(2)`

Rae agrees with line 2 of Kai's second message (`Kai2.2`). The shortened reference `2` is valid because the header contains exactly one `re` reference to a whole message, `Kai2`.

This is an explicit act of agreement. Since Kai2.2 is not shown, we cannot determine exactly what Rae agrees with.

Line 2: `rej(1,not(may(Me,"open vault")))`

Rae declines the request or proposal in line 1 of Kai2 (`Kai2.1`).

She gives the reason that she is not permitted to open the vault. Here, `Me` refers to Rae.

The refusal is performed, and the reason is asserted: Rae claims she does not have permission to open the vault. The content of Kai2.1 is not provided, so we cannot establish what specific action or proposal she declines.

Line 3: `hyp(cause("seal","leak"))`

Rae offers the hypothesis that the seal caused the leak.

This is not an assertion that the seal caused the leak, nor an assertion that the leak occurred. It presents a possible causal explanation for investigation.

Line 4: `prob(cause("seal","leak"),lo)`

Rae assigns a low degree of probability to the proposition that the seal caused the leak.

This asserts a probability assessment, not the causal proposition itself. Rae therefore expresses low confidence in the explanation proposed in line 3. The language does not assign an exact numerical probability to `lo`.

Line 5: `if(is(You,"on call"),pls(You,"check seal"))`

Rae makes a conditional request: if a recipient is on call, that recipient is asked to check the seal.

Because the message has two receivers, `You` is interpreted separately for Kai and Lena.

* If Kai is on call, Kai is asked to check the seal.

* If Lena is on call, Lena is asked to check the seal.

The line does not assert that either recipient is on call. It also does not establish that either recipient has checked the seal. The request applies conditionally to each recipient.

Line 6: `after(fin("flush"),act(Kai,"sample water"))`

Rae asserts that Kai's action of sampling water occurs after the flush has finished.

The expression `fin("flush")` identifies the temporal reference point. Because it is used as the first argument of `after`, it is mentioned as a time reference rather than independently asserted.

Consequently, Rae asserts the temporal ordering of Kai's sampling action relative to completion of the flush. She does not separately assert that the flush has already finished or that Kai has already sampled the water.

Line 7: `sug(at(2026-11-12T10:00,"replace seal"))`

Rae proposes that the seal be replaced on November 12, 2026, at 10:00.

The proposal is addressed to Kai and Lena and includes Rae herself in the proposed joint action.

This is a suggestion, not a promise, command, or assertion that replacement will occur.

The proposal has not yet been adopted. Under SILEX's agreement rules, both recipients, Kai and Lena, must agree before it is adopted.

### Overall interpretation

Rae sends a high-priority message to Kai and Lena, acknowledging earlier communication. She agrees with one line of Kai's previous message and declines another, explicitly asserting that she lacks permission to open the vault.

She then proposes a causal hypothesis involving the seal and leak while assessing that hypothesis as having low probability. Neither the hypothesis nor the probability statement establishes the cause as a fact.

Rae conditionally asks whichever recipients are on call to check the seal. She asserts a temporal relationship between the completion of flushing and Kai's water sampling, without independently asserting that the flush is complete. Finally, she proposes replacing the seal at a specified date and time, subject to agreement.

The key distinctions are between agreement and refusal as speech acts, an asserted reason for refusal, a hypothesis and probability assessment that do not establish their embedded claim, a conditional request, an asserted temporal relationship, and a proposal that is not yet adopted.
```

Marks (1 or 0) for points 1 to 9: _ _ _ _ _ _ _ _ _     total: _

## Z1-E

```text
Account of Z1
 * Header: Rae sends her third message to Kai and Lena. It is a high-priority message (pri(hi)). It is a direct reply to Kai's second message (re(Kai2)), and Rae indicates she has also read Lena's first message (saw(Lena1)).
 * Line 1: Rae agrees with line 2 of Kai2 (using the bare line number short form, which refers to the single message named in re).
 * Line 2: Rae declines whatever act, request, or proposal was made in line 1 of Kai2. She asserts her reason for declining: she is not permitted to open the vault.
 * Line 3: Rae offers a hypothesis that the seal caused the leak. This cause is only mentioned/supposed, not asserted as fact.
 * Line 4: Rae asserts that, in her judgment, the probability of the seal causing the leak is low. (The claim that the seal caused the leak is only mentioned to attach a probability to it).
 * Line 5: Rae makes a conditional request addressed to each receiver independently (You). If the receiver (Kai or Lena) is on call, they are asked to check the seal. The conditional link is asserted, but neither the premise nor the request is asserted as absolute.
 * Line 6: Rae asserts that Kai samples the water at a time after the flush finishes. The claim that the flush finishes is only mentioned to give the time; it is not asserted.
 * Line 7: Rae proposes to Kai, Lena, and herself (let us) that they replace the seal on November 12, 2026, at 10:00. This is a proposal, so nothing is adopted yet.
```

Marks (1 or 0) for points 1 to 9: _ _ _ _ _ _ _ _ _     total: _

## Z1-F

```text
**Z1: what the message says**

Rae sends her third message to Kai and Lena. It replies to Kai's second message, and Rae has also read Lena's first. It is marked high priority.

1. `agree(2)`: Rae agrees with line 2 of Kai2, the message she is replying to. She states no new fact.
2. `rej(1, ...)`: Rae declines line 1 of Kai2, a request or proposal. She gives the reason that she herself is not permitted to open the vault. She asserts that reason as true.
3. `hyp(cause("seal","leak"))`: Rae only supposes that the seal causes the leak. She does not assert it.
4. `prob(cause("seal","leak"),lo)`: Rae weighs that same cause and gives it a low probability. Still not asserted.
5. `if(is(You,"on call"), pls(You,"check seal"))`: a conditional request. It is tested separately for Kai and for Lena. Whoever is on call is asked to check the seal. Nothing is asserted about who is on call.
6. `after(fin("flush"), act(Kai,"sample water"))`: Rae says Kai's water sampling comes after the flush has finished. This line states an order of events.
7. `sug(at(2026-11-12T10:00,"replace seal"))`: Rae proposes replacing the seal at 10:00 on 12 November 2026. It is only a proposal, and it is adopted only once the others agree.

I had no reference for the language, so several answers rest on judgment. I gave low percentages where I was guessing.
```

Marks (1 or 0) for points 1 to 9: _ _ _ _ _ _ _ _ _     total: _

## Z1-G

```text
### Z1. Plain-English interpretation

Rae sends her third message to Kai and Lena, replying to Kai's second message (Kai2). Rae has also seen Lena's first message (Lena1). The message has high priority.

Line 1: `agree(2)`

Rae agrees with line 2 of Kai2. Because the header identifies one message being answered, the short reference `2` points to Kai2.2. The content of that earlier line is not shown, so we cannot identify exactly what Rae agrees with.

Line 2: `rej(1,not(may(Me,"open vault")))`

Rae rejects line 1 of Kai2 and gives the reason that Rae is not permitted to open the vault. The rejection is Rae's communicative act. The permission statement appears within the explanation and should not automatically be treated as an independent assertion.

Line 3: `hyp(cause("seal","leak"))`

Rae raises the possibility that the seal causes the leak. This is a hypothesis, not an assertion that the seal actually causes the leak.

Line 4: `prob(cause("seal","leak"),lo)`

Rae assigns low probability to the proposition that the seal causes the leak. This communicates uncertainty rather than asserting that the causal relationship is true.

Line 5: `if(is(You,"on call"),pls(You,"check seal"))`

Rae conditionally asks the recipients to check the seal. Since Kai and Lena are both recipients, `You` is interpreted separately for each. Anyone among them who is on call is asked to check the seal. Rae does not assert that either recipient is actually on call.

Line 6: `after(fin("flush"),act(Kai,"sample water"))`

Rae asserts that Kai's sampling of the water occurs after the flush has finished. This establishes a temporal relationship without necessarily asserting that the flush has already finished or that the sampling has already happened.

Line 7: `sug(at(2026-11-12T10:00,"replace seal"))`

Rae proposes replacing the seal at 10:00 on November 12, 2026. This is a proposal addressed to the participants, not a claim that replacement has been performed or that everyone has accepted the proposal.

Overall, Rae agrees with one earlier line, rejects another, expresses a hypothesis and a low-probability assessment, makes a conditional request, asserts a temporal relationship, and proposes a future action. Only the temporal relationship is directly asserted as a factual proposition.

### Final answer block
```

Marks (1 or 0) for points 1 to 9: _ _ _ _ _ _ _ _ _     total: _

## Z1-H

```text
Z1 account

Rae’s third message is addressed to Kai and Lena (both receive every line). It replies to Kai2, records that Rae has seen Lena1, and is marked high priority.

- Line 1 (`agree(2)`): Rae adopts line 2 of the message she is answering (Kai2). This is an assertion of agreement.
- Line 2 (`rej(1,not(may(Me,"open vault")))`): Rae rejects line 1 of Kai2 and asserts, as the ground of the rejection, that she herself is not permitted to open the vault.
- Line 3 (`hyp(cause("seal","leak"))`): Rae offers the hypothesis that a seal is the cause of a leak. The causal claim is only mentioned, not asserted.
- Line 4 (`prob(cause("seal","leak"),lo)`): Rae assigns a low probability to the same causal claim. The claim itself remains unasserted.
- Line 5 (`if(is(You,"on call"),pls(You,"check seal"))`): Conditional request addressed separately to each receiver. For whichever of Kai or Lena satisfies “on call,” that agent is asked to check the seal. No fact is asserted.
- Line 6 (`after(fin("flush"),act(Kai,"sample water"))`): Rae asserts the temporal relation that Kai’s sampling of water occurs after the flush finishes.
- Line 7 (`sug(at(2026-11-12T10:00,"replace seal"))`): Rae proposes that the seal be replaced at the stated time. The proposal is offered, not yet adopted.
```

Marks (1 or 0) for points 1 to 9: _ _ _ _ _ _ _ _ _     total: _
