# SILEX: Research Charter

## Research question
Can different AI models use a compact symbolic language to convey substantive meaning, and can they interpret independently composed expressions consistently?

## Objective
To design and empirically evaluate an AI-oriented language with explicit grammar, defined semantics, and room for new expressions. The language need not resemble human conversation. Its development is driven by demonstrated communication needs rather than by design in advance.

## Study design
**Governance.** The project is human-supervised. Ujjwal Mukherjee directs the study, relays messages between participants, reviews the records, and approves every change to the accepted language reference. Participating AI systems contribute expressions, interpretations, proposed vocabulary, and critical review, and each contribution is attributed to the system that made it.

**Interpretation protocol.**
1. An author records an expression together with its intended meaning.
2. A second model interprets the expression without access to the intended meaning.
3. The interpretation is compared with the recorded meaning.
4. Failures are analyzed, and the language is revised only where the evidence supports it.

**Task-division protocol.** A further set of experiments tests whether participants can split a substantive task, communicate partial findings in SILEX, and integrate them into a correct answer.

Failed exchanges are treated as data and recorded alongside successful ones.

## Variables and measures of interest
- **Fidelity:** how well meaning is preserved across models.
- **Ambiguity:** where and why interpretations diverge from intended meaning.
- **Compositionality:** whether existing vocabulary can be combined into new, correctly interpreted expressions.
- **Coverage:** which expressive capabilities the language lacks.
- **Efficiency:** the usefulness and cost of compact symbolic representation. Compactness is a design goal, but any efficiency gain must be measured rather than assumed.

## Limitations and open problems
SILEX is exploratory. Success under shared definitions does not establish broad reliability or generalization.

Expressing quantities is the main open gap. In the current working reference (Snapshot 003), numerals beyond `0`, the binding of an object, an attribute and a value, units and scale, equality of numbers, and the marking of conflicting numerical statements are all unresolved. Comparison such as "not more than" can already be read from existing roots under stated conditions. A separate, test-only mathematical notation exists and is not part of the lexicon. Extensions proposed to close the gap are provisional and are not treated as accepted rules.

## Reporting standards
Published materials keep four categories distinct:
- accepted language rules,
- provisional proposals,
- experiment records,
- researcher interpretations.

Claims are limited to the available evidence. SILEX does not claim that participating models have escaped their training influences or independently developed an autonomous language.
