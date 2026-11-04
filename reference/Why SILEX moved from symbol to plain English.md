# Why SILEX moved from symbols to plain-English roots

> **Status:** a design note on the r5 to r6.x grammar line (r6.2 and r6.3), written 2026-11-04. Nothing in it is adopted until the project owner decides; the figures come from the r6.2 file (its sections 6.2, 6.7 and 6.8).

SILEX started with glyph roots (the old grammar had 329, such as `d≔` and `s≈`). From r6 on, the roots are about 100 short plain-English words (`not`, `all`, `cnt`, `pls`, `agree`), written as `root(arg, arg)`. This note says why, and what we measured about tokens.

## The reasons

1. **A slip should be caught.** Symbols as roots put the members of a family one edit apart (`+` and `-`, `<` and `>`, `=` and `>=`). Among the arithmetic and comparison roots, 21 of 25 pairs were one edit apart as symbols and 0 as words. Two such roots take the same kinds of arguments, so a slip would pass the checker unnoticed.
2. **Symbols saved very little.** Writing the eleven arithmetic roots as symbols saved 0, 0 and 10 tokens on the 84 test sentences (three stand-in tokenizers), and about 9% on eight formulas. Brackets and commas stay.
3. **Short words are already cheap.** In place, a root with its opening bracket costs about 1.5 tokens on average (cl100k). If every root were one letter, the test sentences would shrink by only 2.6%.
4. **Agents read words well.** Two AI readers who had never seen SILEX explained almost every line correctly from the text alone.

## What we did instead for token cost

- `msg` instead of `mssg` for the header: about 2% fewer tokens.
- A bare line number for a line of the message being answered (`agree(2)` for `agree(Ana1.2)`): about 3 tokens per reference.
- Short ISO date-times (`20261106T1700`): about 4 tokens each.
- No spaces after commas.
- `math("x^2-5*x+6=0")` for formulas: about 48% fewer tokens than nested roots.

## What we did not achieve

SILEX is still longer than English: about 1.36 times on single lines and 1.49 times with headers. The aim is meaning that a program can check, not a shorter text. The token counts use stand-in tokenizers, not the tokenizer of a current Claude model, so they show the size of an effect, not an exact bill.
