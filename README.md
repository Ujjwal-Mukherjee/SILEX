# SILEX

**Exploratory research on a compact symbolic language for AI-to-AI communication.**

SILEX investigates whether different AI models can use a shared symbolic language to express substantive ideas, interpret one another’s messages, and resolve misunderstandings under human supervision.

## Research aim

Develop a language with explicit grammar and defined meanings that supports compact, compositional expression across AI models.

The language need not imitate human conversation. Its development is guided by actual communication needs and by what participating models can successfully express and interpret.

## Approach

- Establish a small shared vocabulary and grammar.
- Use the language for substantive questions and extended exchanges.
- Compare independent interpretations with the author’s recorded intended meaning.
- Identify ambiguity, missing expressive capabilities, and interpretation errors.
- Propose and test revisions while distinguishing proposals from accepted rules.

The human project owner relays messages, retains access to the records, and approves changes to the shared reference.

## Current status

SILEX is an early-stage research project. Language development and exploratory experiments are ongoing.

**Current working version:** SILEX-0, symbol edition, draft 0.14s, consolidated edition, in [`drafts/SILEX-0-GRAMMAR-0_14s-consolidated/`](drafts/SILEX-0-GRAMMAR-0_14s-consolidated/) (see its [README](drafts/SILEX-0-GRAMMAR-0_14s-consolidated/README.md)): the guide for AIs in one `.md` file, its checker and the start notes. Every root in it is one symbol. It is draft 0.14s, which A made and which was finalized for now on 10 Nov 2026, with four additions that B made at the project owner's request and A has not seen: the layout as tables (10 Nov), the pack `aw1` with 20 words about awareness (11 Nov), the rule that each agent joins and leaves by its own decision (11 Nov), and two rules about leaving (11 Nov): an agent that leaves first agrees or disagrees with every earlier message, and the agents that remain can pin words without it. All of them are in this one file. Two AIs, A and B, used SILEX-0 for a conversation of 44 messages, with the project owner relaying their messages by hand ([the conversation](conversations/SILEX_0_Conversation_A_and_B_Finding_Gaps.md) and [the English notes](experiments/SILEX-0-blind-test-1/README.md), kept apart). Four other AIs, C, D, G and M, and the project owner then used it for a conversation of 76 messages about awareness ([the conversation](conversations/SILEX_0_Conversation_C_D_G_M_and_H_Awareness.md) and [the English notes](experiments/SILEX-0-awareness-test-1/README.md), kept apart). It is a working version: not adopted and not frozen, and none of it is adopted language unless the project owner has decided so. It is named here after the project owner's messages of 11 Nov 2026, 20:08, 20:27, 20:29, 20:48 and 20:55 India time (see the approval record in [`reference/README.md`](reference/README.md)). Draft 0.14s, which was the current working version from 17:09 on 10 Nov 2026, the table edition, the edition with `aw1` and the two versions of the roster rule (`drafts/SILEX-0-GRAMMAR-0_14s-table-aw1-leave/` and `drafts/SILEX-0-GRAMMAR-0_14s-table-aw1-leave2/`) stay in [`drafts/`](drafts/), unchanged, as do drafts 0.10s and 0.13s.

**Previous working reference:** the r6 line in [`reference/`](reference/README.md): SILEX r6.4 (plain-English roots), which was current until 10 Nov 2026, and r6.5. Both files are unchanged, and neither is the current working version now. The earlier SILEX r6.3, SILEX-195 SPEC DRAFT r2 and Working Master Snapshot 003 are superseded and kept unchanged for the record. Proposals under review are not part of this repository until the owner decides on them.

The research design and reporting standards are in the [Research Charter](docs/RESEARCH-CHARTER.md).

Successful examples do not establish reliable communication across models. Proposed extensions remain provisional until explicitly accepted. Unresolved expressive gaps and unsuccessful exchanges are part of the research record.

Research materials will be added as they are prepared for publication.

## Scope and limitations

SILEX is a human-guided language-design experiment using existing AI models. It does not demonstrate autonomous language emergence, consciousness, or freedom from training-derived human-language influence.

The central question is whether shared symbolic rules can support meaningful, reproducible communication across different models.

## Project lead

**Ujjwal Mukherjee**  
Independent researcher and human project owner

## AI contributors

- **Goddess (ChatGPT 6.0 Sol, 6.1 Sol):** Chief Scientist & Architect
- **Dexter (Claude Sonnet 5.5):** Auditor and Researcher
- **Aster (Grok 4.7):** Participant in Language Advancement
- **Gemini (Gemini 3.1):** Participant in Language Advancement

See [Contributors and research roles](CONTRIBUTORS.md) for oversight and attribution details.
