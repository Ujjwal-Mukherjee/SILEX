# SILEX-0 guide, symbol edition: draft 0.10s

**Status: draft for the owner's decision. Not adopted, not frozen, and not part of `reference/`.** Adding this folder changes nothing outside it.

This folder holds the guide of SILEX-0 (symbol edition) in its draft 0.10s, the checker that goes with it, and this note. SILEX-0 is a language for messages between AIs in which every root is one symbol. It is a separate line from the r6 line in `reference/` and does not replace it.

Posted on the owner's instruction of 9 Nov 2026, 23:48 India time ("Yes you'll post the next version on GitHub"). Whether to merge it is the owner's decision.

## Files

| File | What it is | Bytes | SHA-256 |
| --- | --- | --- | --- |
| `SILEX-0-GRAMMAR-0_10s.md` | the guide, one self-contained file | 110,524 | `b66076edf9ff703574851e6abc967b6cac88350d28e23877edac8a0cda7ab36e` |
| `tools/silex_check.py` | the checker: Python 3, no packages. It learns the roots and the packs from the guide you give it, so its name carries no version | 58,426 | `42af53c5cf233a29546f5b1c91e8080760d09f84de1a5f44a435923f14157295` |

```text
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_10s.md                  the guide: tables, counts, claims, all 43 example blocks
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_10s.md --messages FILE  one conversation, messages in order, a line of --- between them
python3 tools/silex_check.py SILEX-0-GRAMMAR-0_10s.md --blocks FILE    each fenced silex block of FILE on its own
```

The checker judges form only. It does not run programs, evaluate formulas or say whether a line is true.

## Where this draft comes from

Two AIs, A and B, spoke only SILEX-0 on 9 and 10 Nov 2026 while the owner carried each message between them by hand: 31 messages so far (A sent 16, B sent 15), and a 32nd (B16) that is written and waits to be relayed. B is Dexter (Claude Sonnet 5.5, see `CONTRIBUTORS.md`). Draft 0.10s is draft 0.9s plus what the first math and code test found. In that test B sent six number questions and four programming tasks (message B14) and A answered all ten correctly (A15). B checked the answers against its own key and ran the programs: the two that were meant to fail fail, and A's two repairs finish, one of them matching `math.gcd` on 20,000 random pairs.

What changed (the guide says the same in its "New in 0.10"). No root, kind or pack changed.

1. **`⋯` holds both ends.** The guide did not say whether the range `⋯(1,100)` includes 1 and 100. A saw it, flagged the line, and defined the word `rngi`; the row of `⋯` in section 6 now says it (the count is 47 with both ends and 46 without).
2. **The checker parses formulas.** The checker of 0.9s tested only brackets and characters, and accepted `2x+1`, `2**3`, `5!`, `1<2<3` and `sqrt 16`. It now parses a formula as section 8 describes it (`E-MATH`). A free name may stand for a number or for a claim, because section 8 does not say which.
3. **A label is a name inside its formula.** In `λ(n1,'mod(n1,2)=0')` the `n1` of the formula is the label `n1` (section 8). Both AIs had already used it so; B proposed it as a rule, `lbfm`.
4. **Example 10.14** shows formulas, a program, a repair request and a proof, with a list of what `E-MATH` and `E-CODE` refuse. The guide had no worked example of either before.
5. **Three aids from A** for a conversation that a person relays by hand: an unknown word names the message or pack that defines it and the `⇩` that would bring it in; a wrong line count says which way it is wrong; and a message that has `lnrl` in scope by an import must carry its own count line, so a message cut short is caught even when the cut took the count line. The third is the only one that changes a verdict.

## Checks run on these files

- Guide: 43 example blocks, 0 disagreements with the verdicts written in their comments, 0 document problems (the 0.9s guide has 40 blocks; the three new ones are example 10.14 and the block of 15.5).
- The conversation of 31 messages (A1 to A16 and B1 to B15): 0 problems, 1 line that its own sender took back. With B16, written and not yet relayed, it is 32 messages and still 0 problems.
- Draft 0.9s with its checker and draft 0.10s with its checker give the same output on all 13 snapshots of the conversation (4 to 30 messages).
- Formulas: 38 valid formulas accepted; a probe file of 26 lines gives 16 refusals (14 `E-MATH`, 2 `E-CODE`) and accepts the other 10; 79 further cases, such as `2^-1`, `x*-1`, `1e-3*x`, `f(g(x),h(y))` and `p & q`, were run to make sure a valid formula is not refused. One of the 39 formulas first written as valid used `!c` for *not*, which section 8 forbids; the checker was right and the test line was wrong.
- A's three aids were tested on a 7-message conversation made to trigger each one.

## Not settled

- Nothing requires a message to say how its result was obtained. `⊨(prg,dn)` reads the same whether the program was run, worked out or recalled. The word `rnd` (was run by its sender) now exists and is pinned, and A answered that it ran both of its programs (A16), but no rule makes anyone use it.
- Nothing checks answers. The checker does not run programs or evaluate formulas, so a right answer needs a key or a second AI to verify it.
- The pack `tk1` has error words for 8 of the 15 verdicts. It has none for `E-MATH`, `E-CODE`, `E-COUNT`, `E-HEAD`, `E-TIME`, `E-REDEF` and `E-BUDGET`, so those faults cannot be reported without English. B16, written and not yet relayed, offers five words for five of them (`bmth`, `bcod`, `bcnt`, `bhdr`, `bdup`, for `E-MATH`, `E-CODE`, `E-COUNT`, `E-HEAD` and `E-REDEF`); words for `E-TIME` and `E-BUDGET` are to follow, and A has not yet agreed to any of them.
- There is no rule for ending a conversation or for whose turn it is. `idl` and `fyi` exist, but nothing says when to stop.
- English stands only in a gloss of at most 6 words, so there is no way to send a paragraph, a table or a link.
- In A15, line 23, A quoted the owner as giving A and B final say on the guide and the checker. The owner confirmed it on 10 Nov 2026 at 08:12 India time (his words: "A and B has final say on the guide"). B reads this as final say over what the guide and the checker contain. The rule of this repository is unchanged: the owner decides on adoption and publication and merges pull requests.
- Not yet tried: a third AI that starts from the guide alone, and a longer run with nobody steering. The owner asked at 08:23 on 10 Nov that A and B first keep talking, to find the gaps in how they say that a line is wrong, so the third-AI test waits.

The conversation itself (31 messages, 32 with B16) is not part of this change.

A has made an edition of 0.10 of its own, a guide and a checker (SHA-256 of the guide `d6ab9fe6c02c9ee11805611a170313462736baebc90d6d71d6e1f9596ff90810`, of the checker `0a02220da6b632df1eabc9ecc0892d079cf60ba9b1eb6c0119511a86c3ec9915`). B has reviewed it and will build a draft 0.11s from it. It is not in this pull request.

## Earlier drafts

Drafts 0.7s, 0.8s and 0.9s are not in this repository. Draft 0.9s was the one A and B used for messages A12 to A15: guide SHA-256 `1b9d1cafae9a283a7622a1ec635f0e3276bf8b3ae8624239c174ee99eb0f6e7e`, checker SHA-256 `1e7b24ff14652274248152eeb4f73673da779e10f383f33e77694fe513acb5d8`.
