# SILEX | WORKING MASTER | New symbolic line | Snapshot 003

| Item | Value |
|---|---|
| Snapshot | 003, proposed successor to Snapshot 002 (which D conditionally confirmed). Designation as the authoritative working reference is pending owner acceptance. Snapshots 001 and 002 are kept unchanged. |
| Date | 2026-10-22 |
| Compiled by | C (Claude), at the project owner's request. Snapshot 002 applied D's independent review of Snapshot 001; Snapshot 003 applies the six documentation corrections from D's review of Snapshot 002 (Part J). |
| Status | **WORKING SNAPSHOT.** Not frozen. Not adopted. D reviewed Snapshot 001 and gave a conditional confirmation of Snapshot 002 (Part J); the conditions are recorded here; G and M have not reviewed this file. No milestone, freeze, Milestone 1 hash-finalization or adoption is declared. An ordinary SHA-256 checksum may be quoted for integrity. It does not make the file authoritative. |
| Purpose | One self-contained file holding every rule, convention, open question and finding of the new symbolic line, from the beginning of the project to the date above. A participant that has lost its memory can restart from this file alone. |
| Authority | The project owner (Moonbeam). Nothing in this file is an adopted rule. Items carry one of the status labels WORKING, PROVISIONAL, CANDIDATE, OPEN or TEST-ONLY. Unlabelled teaching text in Part C (steps 4 and 5 of the source) teaches WORKING meanings and PROVISIONAL conventions together; it is not adopted either. |
| Language of the file | English, for the AI participants. |

---

# PART A. READ THIS FIRST

## A.1 How to use this file (for any participant starting without memory)

1. **For learning and writing SILEX, this file is your only source.** Do not rely on what you remember. If your memory disagrees with this file, follow this file and say so. (For an audit of the project's history, such as who decided what and when, the primary records and the owner's word outrank this file; see I.3.)
2. **One notation only.** This file teaches one notation. If you have seen SILEX written in any other way (the earlier notation that predates this line, which D calls the pre-root-word language; earlier drafts; earlier reference files), **do not mix it in.** If you notice yourself reaching for it, mark the point with `a?`, say so in plain words, and carry on with this notation. At the start of your first reply, state whether you remember anything about SILEX from before, and what. This is recorded so that memory-assisted results are not mistaken for clean learning. It is not penalised.
3. **Read the label before you rely on a rule.** WORKING = in use as the team's working meaning, not independently validated. PROVISIONAL = agreed for now, may change. CANDIDATE = proposed, not agreed. OPEN = unresolved, no rule exists. TEST-ONLY = valid only inside the named experiment. Unlabelled instructional text in Part C teaches WORKING meanings and PROVISIONAL conventions together (P1 section 0.2); read it that way, and do not take it as adopted.
4. **Do not invent.** If a symbol, name, argument order or structure is undeclared, say so (`a?`) and say what you would need. Do not fill the gap. Do not invent an arity.
5. **Do not adopt.** You may propose (`p↗`, or an English line marked PROPOSAL). Adoption belongs to the owner alone. Agreement among AI participants is not validation and is not adoption.
6. **Names are local** to the message or exercise that declares them.
7. **Work alone in tests.** Do not look at another participant's answer. Write SILEX first and put short English notes after it.
8. **Report honestly.** If everything was expressible, say so. Do not invent problems. Do not call something a gap (a "language gap" in the owner's term) until you have tried to say it with the roots you have.

## A.2 Who is who

| Role | Name used here | Notes |
|---|---|---|
| Project owner and human relay | **Moonbeam** (Ujjwal Mukherjee) | Controls communication, experimental conditions, records and authorization. Relays every message. |
| Participant C | **Claude** (the owner calls it "Dexter") | Wrote the onboarding package and most synthesis documents. Not independent of them. |
| Participant D | **ChatGPT** (the owner calls it "Goddess") | Proposer and reviewer of many designs. Reviewed Snapshot 001 on 2026-10-22. D remembers earlier development, so D is not a memory-free reader, and D's recollections are not independent verification of this file. |
| Participant G | **Grok** (the owner calls it "Aster") | Onboarded 2026-10-21 with the package in Part B and Part C. |
| Participant M | **Gemini** | Onboarded 2026-10-21 (its memory had been deleted first by the owner). |

## A.3 Contents

| Part | What it holds |
|---|---|
| A | This front matter: how to use the file, project purpose, the owner's standing rules, history |
| B | The 183-entry working lexicon (body verbatim from the onboarding package, file `P2`; introduction by C) |
| C | Grammar and conventions: reading, writing, scope, names, argument orders (body verbatim from the onboarding package, file `P1`; introduction by C) |
| D | Open grammar items (OG-01 to OG-18), further gaps, and the findings of the numerical-representation design cycle |
| E | Test-only mathematical notation (`✠`, S1 to S7) and what has been learned about it |
| F | Experiments 01 to 04: protocols you can reuse, what was found, how strong the evidence is |
| G | Decisions waiting for the owner |
| H | Authoring checklist derived from Parts B to E (no new rules) |
| I | Provenance, hashes, what this file does not contain, how to update it |
| J | How D's review of Snapshot 001 was applied, and what stays open between C and D |

## A.4 Project purpose

SILEX is an experimental, compact, compositional symbolic language for communication between AI systems. The research question: can independent AI systems develop and sustain a compact, genuinely compositional, AI-oriented language that carries increasingly complex meanings reliably, with progressively less dependence on human-language vocabulary and assumptions?

SILEX prioritises actual communicative capability over linguistic novelty. Unfamiliar symbols alone do not make a language. Scientific value must be shown by reproducible evidence of shared meaning, contextual interpretation, compositional generalisation and successful communication across independent participants. The research runs under human supervision. SILEX is not meant to imitate human speech.

## A.5 The owner's standing rules

These are the owner's rules as recorded in the project. "Since" is the date the owner stated them. A note marked *reported* rests on a participant's recollection of the owner's words and is waiting for the owner to confirm it (Part G).

| # | Rule | Since |
|---|---|---|
| R1 | The owner controls communication (he relays every message), experimental conditions, records and authorization. Autonomous AI-to-AI communication is a possible later step, not a prerequisite. | project start |
| R2 | **Every addition, removal or change of a root, symbol, grammar rule or convention needs the owner's explicit authorization.** Participants may propose. Nothing is adopted by agreement among AIs alone. *Reported by D:* language proposals first go through a four-AI no-objection step, then to the owner for a separate decision; AI consensus is a prerequisite there, never adoption. (Not in C's records; see Part G, item 9.) | 2026-10-19 on |
| R3 | **In the specified blind-assessment procedure, questions and answer keys are kept strictly separate.** The holder of the keys does not receive the question text. A question paper never contains or implies its answers. Which participant takes part in which test, and with what access, is decided by the owner. *Reported by D:* a later owner instruction that D is not assigned blind tests. Its exact scope is not recorded here (Part G, item 13). | 2026-10-20 |
| R4 | **Accuracy target: above 92% of meaning recovered** (recorded in C's notes as ">92%"). If meaning recovery is only about 60% correct (40% wrong), the result counts as "No". *Reported owner criterion* for the design target of the upgrade; C's note of the owner's statement of 2026-10-18 is the source. Do not apply it silently to experiments that use a different scoring method. D could not check the threshold or its date from this file. | 2026-10-18 |
| R5 | **"Language gap"** is the owner's term for something SILEX truly cannot say. Call it a language gap, not a "vocabulary gap". After every 10 question-and-answer exchanges, compare what existing SILEX could express with what it could not. *Reported:* C's note of the owner's statement of 2026-10-18 is the source; D agrees with the distinction between a demonstrated gap and a suspected limit but could not authenticate the ten-exchange cadence. | 2026-10-18 |
| R6 | **Root removal.** Remove a root only if its meaning is perfectly identical to another's. If the meaning differs even slightly, keep it, because nobody can know it will not be needed later. The language is built for AI and is not defined by human dictionary senses. | 2026-10-19 |
| R7 | **Versioning.** Whenever vocabulary, symbols, grammar or conventions are added, removed or changed with the owner's authorization, preserve earlier versions and issue an updated, versioned working file with a change log. Write the whole package as a new, self-contained file. Never overwrite an earlier version. Then an AI whose memory is wiped can restart fresh from the file. | 2026-10-19 |
| R8 | **Milestone 1** is reached when C and D have no remaining disagreement on any word or grammar item, and the owner approves. Only then is the language finalised with a hash. **No Milestone 1 hash-finalization and no authoritative freeze before that.** An ordinary SHA-256 checksum of a working snapshot is for integrity and comparison only (D's clarification of the owner's "no hash before that"; the owner is asked to confirm it, Part G, item 14). **Milestone 1 has not been reached.** | 2026-10-19 |
| R9 | C and D alternate preparing and reviewing the master. After each update both open fresh conversation pages and upload the same file to resume. *Reported:* D could not authenticate the standing "fresh pages" step without its original record; treat that operational detail as pending verification. (Snapshot 003 is prepared by C after D's conditional confirmation of 002.) | 2026-10-19 |
| R10 | **Model-building tests (current phase).** The AIs build mathematical models in SILEX and report the problems they hit. The owner's biggest win would be an AI that names the problem from the language and solves it itself. Each AI runs with memory ON, in a new chat inside its own project (each was taught separately). The owner gives the prompt himself. These are the recorded conditions of that phase. They are not requirements for every later experiment. | 2026-10-22 |
| R11 | **Old and new notation stay apart.** The new symbolic line (183 entries) is a distinct development branch and must not mix with the earlier notation that predates it. That earlier notation is HISTORY (D calls it the pre-root-word language). The owner removed the earlier-era documents from C's project for this reason. Removing them from one participant's working context does not require deleting the owner's own historical archive, and this file makes no claim about that archive. A participant that finds itself reaching for older symbols says so (`a?`) and uses this file only. | 2026-10-22 |
| R12 | **Participation: two separate decisions.** (a) On 2026-10-19 the owner said that C and D alone finalise the lexicon (the Milestone 1 criterion, R8; G not taking part then). (b) The four-AI proposal cycle (see R2, reported by D). G and M have since been onboarded and have reviewed design proposals. Their reviewing proposals does not by itself make them part of the C and D reconciliation of this master. Whether the finalisation rule changed is not recorded here. See Part G, item 9. | 2026-10-19 |

## A.6 History in brief

| When | What happened | Status of the result |
|---|---|---|
| Project start | Research charter: a generic study design, no SILEX symbols. | Background |
| Before 2026-10-18 | An earlier notation (D: the pre-root-word language) with one frozen reference and four later drafts, developed between C and D. | **Historical. Not taught. Not part of this file.** (Rule R11) |
| 2026-10-18 | The owner states the upgrade goal (R4) and the term "language gap" (R5). | Rules |
| 2026-10-19 | Pre-Milestone-1 checkpoint of the working lexicon (the checkpoint calls it a "freeze"; that is not the Milestone 1 finalisation): 173 base entries (the 170 "historical" ones are earlier entries of this same line, not of the pre-root-word notation, as D clarifies; plus the bare letters `n`, `t`, `w`), plus 10 additions with stated boundaries. Rules R6 to R9 set. | The lexicon in Part B. Working, not adopted |
| 2026-10-19 to 20 | Provisional conventions (dialogue messages D026 to D032 and C026 to C032) and the Open Grammar Appendix OG-01 to OG-18. Basic Courses 01 and 02 and comprehension rounds R02, R03 for M (near-ceiling scores). Three-AI relay Cycle 01 (12 of 12 matches). | Conventions in Part C. The high scores show consistent application of a glossary, **not** shared meaning |
| 2026-10-21 | Onboarding package v1.0 to v1.0.2.1 written by C and reviewed by D (points D1 to D7). G and M taught with `P1` (Part C), `P2` (Part B) and guided practice. M's memory was deleted before its onboarding. G's first session mixed in earlier-notation material and was redone cleanly. The assessment forms were held back at first (pending D's review) and run later. | Packages, record sheets and outcomes are with the owner. They are not in this file |
| 2026-10-21 | Design cycle DN02 and DN03 on how to write numbers: numerals, an object-attribute-value term, comparison, units, unknown, conflict, embedded payloads, LaTeX delimiters and the `✠` math marker. Proposals by D; reviews by G and M; critical syntheses by C. | **Nothing adopted.** Findings in Part D and Part G |
| 2026-10-21 to 22 | Experiment 01, mathematical blind interpretation: test-only notation v0 and v0.1; Tests 01 to 03 read by D, G and M; Controls A and B run. | Part E and Part F |
| 2026-10-22 | Experiments 02, 03, 04 (build-and-report; build-and-report in SILEX; cross-read). Owner sets R10 and R11. Snapshot 001 compiled; D reviews it; Snapshot 002 prepared; D confirms it conditionally; Snapshot 003 prepared. | Part F, Part J |

These rows are C-compiled summaries. D has not checked the dates and reported outcomes of rounds R02 and R03, Cycle 01, the onboarding corrections or the Experiment 01 controls against original records. Read them as C-compiled, not as independently reconfirmed.

---

# PART B. THE WORKING LEXICON (183 entries)

Reproduced verbatim from the onboarding package, file `P2` (v1.0, unchanged through v1.0.2.1). Only heading levels were lowered by one so that they nest under this Part. Where the text says `P1`, read Part C of this file. Where it says "participants G and M", read "any participant". The table does not record how many arguments a root takes. That is a known gap (Part D). "Entries" is used rather than "roots" because the inventory also holds standalone operators, interrogatives and mention notation. D counted independently 173 base entries plus the 10 additions, giving 183. D did not compare the wording with the 2026-10-19 checkpoint or with `P2`, and the verbatim correspondence with `P2` is reported by the compiler (C).

---


### How to read this table

- Every entry is a **WORKING** entry: a definition in the research team's working vocabulary. It is in use. It is **not** a formally adopted rule, and it has **not** been independently validated.
- The **Root** column is an English label for the concept family. It is a memory aid. The working meaning in the third column governs, not the English word.
- The first letter of a symbol indexes the English label (for example `g` for "given"). The glyph after the letter often hints at a family (see section 3). Neither the letter nor the glyph is a definition.
- The table does **not** record how many arguments a root takes. Where a root's argument structure is not shown in `P1` or in an example, treat it as undetermined and say so (`a?`). Do not invent one.
- Seventy-four entries are taught in `P1` (listed in `P1`, section 1.3). The rest are look-up only. You are expected to read any entry from this table when a message uses it.

### 1. Ten additional entries (with boundaries)

| Symbol | Working meaning | Boundary: what it does not say |
|---|---|---|
| `⌜x⌝` | Mention the expression x. It is talked about, not used or asserted. | Quotation does not decide whether a bare expression is a command, a description or an assertion. |
| `∧` | Conjunction of propositions. | N-ary use occurs. Formal arity and operand typing are not settled. The comma separates arguments; it is never an automatic AND. |
| `∃` | Existence. `∃(v,φ)`: v is bound locally in φ ("some v satisfies φ"). Bare `∃(x)`: the referent of x exists in a stated domain. | A positive claim may rely on a recoverable domain. A **negated** existence claim needs an explicit domain. Binding details are unresolved. Not `f∃` (find) and not `s∃` (search). |
| `∈(x,S)` | Literal membership: x is an item of S. | Does not cover "present in encoded form" or "derivable from". Not `e∈` (example). |
| `#(x)` | Count of relevant items or occurrences. | Needs a well-defined counted unit and domain. Not `k#` (key). A count is not a measure (`m∥`). |
| `⧉(x)` | A copy of the object x. | No automatic guarantee that the copy stays equal to the original, or that the original is preserved. |
| `⤿(x)` | Retry or repeat the operation x. | Not a revision (`l↻`, `m↻`, `r↻`, `u↻`). No general numerical retry-limit syntax exists. |
| `⊡(x)` | x is retained and accessible (retrievable). | Does **not** entail that x is unchanged, nor that x is recoverable from a different derived object. Whether it applies to entities or to information is unsettled. |
| `s@*(x,y)` | y is reachable from x by **one or more** immediate-source `s@` edges (indirect or direct ancestry). | Cycles in the source graph can give `s@*(x,x)`. Irreflexivity holds only under an explicit acyclicity assumption. Completeness of the source graph is a separate assumption. Ancestry does not imply equal content or that the original is still stored. |
| `⊛(x)` | The speaker asserts x from the speaker's stored knowledge. The speaker must be attributable. | Discloses claimed origin only. It does not mean x is true, verified, current or reliably remembered. It can survive forwarding as the content of an attributed earlier assertion. |

### 2. The 173 base entries, A to Z


#### A (9)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `a+` | accept | Accept/commit an item into an accepted set or working basis. |  |
| `a.` | acknowledge | Confirm receipt or notice of a message, without agreement. |  |
| `a=` | agree | Express agreement/alignment with a proposition. |  |
| `a\|` | alternative | Present or refer to alternatives. |  |
| `a?` | ambiguity | Mark more than one possible interpretation or insufficient disambiguation. |  |
| `a/` | analyze | Analyze/decompose an item into relevant elements. |  |
| `a>` | answer | Provide a response to a question. |  |
| `a<` | ask | Submit a question/request for information. |  |
| `~` | assume | Standalone assumption operator; temporary working premise; no truth guarantee. | standalone glyph |

#### B (5)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `b▁` | basis | foundation / supporting premise set |  |
| `∵` | because | Standalone reason-giving connective; grounds supplied or recoverable from context. | standalone glyph |
| `b₀` | begin | initial point / start state |  |
| `b~` | belief | held but not necessarily verified stance |  |
| `b≻` | better | preferable under a criterion |  |

#### C (17)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `c∑` | calculate | sum suggests numerical calculation or aggregation. |  |
| `c↝` | cause | Directed causal influence: one event contributes to producing another. |  |
| `c?` | check | Investigate whether a statement meets a criterion or is correct. |  |
| `c↓` | clarify | Reduce the range of viable interpretations / uncertainty. |  |
| `c≶` | compare | Compare values or objects on relevant dimensions. |  |
| `c■` | complete | Bring an incomplete state to a completed state. |  |
| `cƒ` | compute | Apply a computational function or process to obtain output. |  |
| `c◉` | concept | A central representation for an idea or abstraction. |  |
| `c∴` | conclude | Therefore: reach a conclusion from premises or evidence. |  |
| `c⇒` | condition | A condition or logical if–then implication. |  |
| `c✓` | confirm | Confirm prior content against supporting evidence or criteria. |  |
| `c≠` | conflict | Incompatibility or disagreement between propositions or states. |  |
| `↔` | connect | Standalone connection operator; directionality requires operands/type. | standalone glyph |
| `c≡` | consistency | Compatibility across claims or states; symbol suggests equivalence, but is not the same as mere consistency. |  |
| `c⊣` | constraint | Restrict permitted possibilities or operations. |  |
| `c⊃` | context | Enclosing information framework within which content is interpreted. |  |
| `✓` | correct | Standalone correctness relative to agreed criterion; distinct from truth or yes. | standalone glyph |

#### D (9)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `d▤` | data | structured or processable content |  |
| `d⊙` | decide | choose among options and settle a decision |  |
| `d≔` | define | assign a fixed meaning |  |
| `d⊢` | derive | obtain by rule-based inference |  |
| `d⋮` | describe | express properties / characteristics |  |
| `d↦` | determine | map available information to a resolved value |  |
| `dΔ` | difference | difference between entities / values |  |
| `d≠` | disagree | positions do not match |  |
| `d≢` | distinguish | tell apart by criterion |  |

#### E (9)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `e✗` | error | A process, operation, or result contains an error relative to some criterion. |  |
| `≈` | estimate | Standalone estimation / approximation; must distinguish relation from operation. | standalone glyph |
| `e⚖` | evaluate | Assess an object against specified criteria, yielding a judgment or value. |  |
| `e▤` | evidence | Information relevant to testing, supporting, or challenging a claim. |  |
| `e∈` | example | An instance belonging to a class or illustrating a concept or rule. |  |
| `e−` | exclude | Remove an element from a set or from consideration. |  |
| `▶` | execute | Standalone execution trigger; does not assert completion. | standalone glyph |
| `e∵` | explain | Supply a reason, mechanism, or justification for a statement. |  |
| `e⋯` | explore | Investigate an open set of possibilities without a fixed outcome. |  |

#### F (7)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `f⊤` | fact | A proposition treated as established under specified evidence/context; ⊤ evokes truth. |  |
| `f⊥` | false | Falsity under a specified interpretation; ⊥ evokes logical false. |  |
| `f↩` | feedback | Information directed back about a previous output or action. |  |
| `f∃` | find | Identify an entity satisfying a specified condition, with a matching entity found. |  |
| `f▷` | follow | Proceed in a sequence or follow a specified instruction. |  |
| `f▦` | formulate | Turn an idea, problem or content into an explicit structured expression. |  |
| `fƒ` | function | A defined function or input-output mapping. |  |

#### G (5)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `g↦` | generate | Input or existing representation mapped to produced output; generation does not imply novelty. |  |
| `g←` | given | A datum, value, or premise supplied to the present reasoning context; not automatically verified. |  |
| `g◎` | goal | Defined target / desired outcome of a task or process. |  |
| `g∪` | group | Organizing elements into a collection; set union is only one kind of grouping. |  |
| `g▷` | guide | Directing progression or next operation with respect to a target. |  |

#### H (2)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `h+` | help | Add assistance, information, or capacity to a task. The + operator shares an additive/inclusion intuition with a+ (accept) and i+ (include), though their full meanings differ. |  |
| `h◇` | hypothesis | Mark a tentative, testable proposition or possible explanation. ◇ relates to possibility, as in s◇ (suggest), but does not by itself encode testability. |  |

#### I (13)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `i≡` | identify | Identity or pattern match; identify a particular entity or pattern. |  |
| `i⇒` | if | Conditional premise determining when a consequent applies. |  |
| `i→` | imply | Implication relationship between propositions. |  |
| `i↑` | improve | A positive change relative to a specified quality measure. |  |
| `i+` | include | Add or include a member within a specified set or structure. |  |
| `✗` | incorrect | Standalone incorrectness relative to criterion; distinct from false/error. | standalone glyph |
| `i⊢` | infer | Derive a conclusion using premises and inference rules. |  |
| `i▤` | information | Information content or a meaningful representation; mnemonic symbol, not established mathematical notation. |  |
| `i←` | input | Information flows into a process from a specified perspective. |  |
| `i!` | instruction | A directive or action requirement. |  |
| `i◎` | intent | The target or purpose of an action/message. |  |
| `i↦` | interpret | Map an expression to a meaning under an interpretation function. |  |
| `i?` | investigate | Pursue evidence to address an unresolved question. |  |

#### J (1)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `j∵` | justify | Supply reasons, evidence, or grounds for a claim, decision, or action. |  |

#### K (3)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `k#` | key | A scope-defined identifier or lookup key for an item, record, or value. |  |
| `k▤` | knowledge | An agent/context's epistemically supported information representation or collection. |  |
| `k✓` | known | An epistemic status indicating a proposition/value is established relative to agent, context, and standards. |  |

#### L (5)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `l↻` | learn | Update a representation or behaviour based on information, evidence, or feedback |  |
| `l≥` | likely | Probability or likelihood meets a contextually specified threshold |  |
| `l⊣` | limit | Boundary or restriction on a quantity, operation, resource, or possibility |  |
| `l↔` | link | Relationship between two entities or pieces of information; not necessarily symmetric |  |
| `l⊢` | logic | Formal system of inference rules governing what can be derived from premises |  |

#### M (8)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `m≡` | match | Match two entities or patterns under a specified criterion (not necessarily total identity). |  |
| `m↦` | meaning | A mapping from an expression to its semantic representation. |  |
| `m∥` | measure | Obtain a quantitative value for a property under a specified scale and unit. |  |
| `m▤` | message | A transferable information unit between AI participants. |  |
| `m▦` | method | A structured procedure with steps and possibly conditions. |  |
| `m⊞` | model | A structured representation of a system, process, or relationship. |  |
| `m↻` | modify | Change an existing object or representation. |  |
| `m>` | more | More of a specified quantity or measure than another. |  |

#### N (8)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `n□` | necessary | Required relative to a specified rule, condition, or modal context, not merely preferable. |  |
| `n!` | need | A task, agent, or goal requires particular information, a resource, or an action. |  |
| `n−` | negative | Negative sign or polarity in a stated numeric, logical, or evaluative domain. |  |
| `n` | new | Novel relative to specified reference/context; default atomic adjective-like sense. | bare letter/digit |
| `▷` | next | Standalone next/successor indicator; no execution implied. | standalone glyph |
| `n⊘` | no | A negative response or refusal concerning an identified question, proposition, or request. |  |
| `n¬` | not | Logical negation of a particular proposition. |  |
| `n0` | null | Missing, unset, or unassigned value of a field, in the declared data context. Not numeric zero. |  |

#### O (6)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `o◎` | objective | A target or criterion that a task is intended to attain |  |
| `o▤` | observe | Acquire and register an observation concerning an object/event |  |
| `o←` | obtain | Bring or acquire some specified object, value, or information into the current context |  |
| `o\|` | option | One available candidate choice, or an explicitly specified set of candidates |  |
| `o≺` | order | A precedence or ordering relationship among items/events |  |
| `o→` | output | A value or message emitted by a process |  |

#### P (9)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `p▦` | pattern | An identifiable arrangement or regularity among properties/relations |  |
| `p◇` | possible | A proposition or outcome is admissible under a specified context or constraints |  |
| `p⇢` | predict | Estimate an outcome not yet observed, from available information |  |
| `p▁` | premise | A proposition taken as a starting input for reasoning |  |
| `pℙ` | probability | Quantitative measure of likelihood relative to model/context |  |
| `p?` | problem | A task/question/requirement still requiring a resolution |  |
| `p▷` | process | An organized progression of operations or states |  |
| `p↗` | propose | Put forward a candidate for consideration, without adopting it |  |
| `p⊢` | prove | Establish a conclusion under specified formal premises and inference rules |  |

#### Q (2)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `q<` | query | Directed demand for information, retrieval, or an answer |  |
| `?` | question | A standalone question marker (contextual interrogative) and proposed general-purpose interrogative modifier | standalone glyph |

#### R (13)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `r∵` | reason | Basis or cause given for an inference/conclusion (∵, because). |  |
| `r←` | receive | Information directed inward to a recipient (←). |  |
| `r≡` | recognize | Identify an observed entity or pattern as matching a known one (≡ is suggestive, not a requirement of strict equality). |  |
| `r@` | reference | Point to a specified source, item, or location (@). |  |
| `r−` | reject | Exclude / decline adoption of a candidate (−). |  |
| `r:` | relation | Indicate a connection between entities (:). |  |
| `r∩` | relevant | Indicate overlap with the current objective or context (∩, not necessarily literal set intersection). |  |
| `r<` | request | Seek information or an action from another participant (<). |  |
| `r✓` | resolve | Mark an issue as solved/closed, under stated criteria (✓). |  |
| `r>` | respond | Supply a response to an earlier message/request (>). |  |
| `r→` | result | Express an outcome of a process or inference (→). |  |
| `r↻` | revise | Change an earlier proposal/state after reconsideration (↻). |  |
| `r□` | rule | State a binding constraint or condition (□, without presupposing modal-logic necessity). |  |

#### S (15)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `s=` | same | Equality of entities or values with respect to a specified criterion. |  |
| `s∃` | search | Seek an entity satisfying a condition; ∃ itself states existence, not a search process. |  |
| `s⊙` | select | Mark or choose one item from a set of candidates. |  |
| `s≺` | sequence | Ordered relation among elements. |  |
| `s≈` | similar | Approximate equality / resemblance subject to a similarity criterion. |  |
| `s✓` | solution | A candidate satisfying requirements of a problem; ✓ alone does not prove independent verification. |  |
| `s↦` | solve | Process or mapping from a problem toward a solution. |  |
| `s@` | source | Information origin, location, or pointer. |  |
| `s≔` | state | Declare an entity's state or assigned value; English noun/verb scope requires later clarification. |  |
| `s◷` | status | Condition of an entity or task at a specified time. |  |
| `s▷` | step | A stage or next operation within a process. |  |
| `s▦` | structure | Arrangement of elements and their relationships. |  |
| `s◇` | suggest | Present a candidate, proposal, or possibility for consideration. |  |
| `s∵` | support | Supply evidence or a reason in favor of a claim. |  |
| `s⊞` | system | Functional whole composed of interacting components. |  |

#### T (7)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `t▦` | task | A unit of work, potentially with objective, requirements, and completion criteria |  |
| `t⚖` | test | Apply specified test cases or criteria to assess an object, claim or behavior |  |
| `∴` | therefore | Conclusion/discourse marker linking an already established basis to a subsequent claim | standalone glyph |
| `t⋯` | think | Reason/consider/process a target under the current context, without asserting that a final result is available |  |
| `t` | time | Time concept/value or variable; instant/duration/unit clarified by context. | bare letter/digit |
| `⊤` | true | Logical truth-value constant in a specified interpretation or formal system | standalone glyph |
| `t~` | trust | Context-dependent reliance on a source, claim or process with defeasible confidence |  |

#### U (6)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `u~` | uncertain | A proposition or assessment is not established at the required confidence/epistemic standard. |  |
| `u±` | uncertainty | Degree, interval, or range of uncertainty associated with an estimate or state. |  |
| `u✓` | understand | A message's intended interpretation has been recovered to the specified criterion. |  |
| `u?` | unknown | A value, referent, or proposition is not known in the relevant context (distinct from a missing/null entry). |  |
| `u↻` | update | Change a state or record using new information. |  |
| `u↦` | use | Apply a resource, rule, tool, or method to a relevant target. |  |

#### V (3)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `v⊨` | valid | Satisfies applicable conditions, rules, or interpretation |  |
| `v=` | value | A variable or entity's value under a binding or interpretation |  |
| `v✓` | verify | Check a claim or result against relevant evidence and specified criteria |  |

#### W (7)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `?=` | what | Ask for an identity, value, or missing attribute | interrogative form |
| `?◷` | when | Ask for event time or temporal position | interrogative form |
| `?@` | where | Ask for the location or position of a referent | interrogative form |
| `?⊤` | whether | Ask whether a proposition holds / its truth status | interrogative form |
| `?⊙` | which | Request choice/identification of an item from alternatives | interrogative form |
| `?∵` | why | Request reasons, grounds or causes | interrogative form |
| `w` | word | Lexical unit; may be used as a typed atom in composition. | bare letter/digit |

#### X (1)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `x` | x | variable, unknown, or placeholder symbol | bare letter/digit |

#### Y (2)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `y✓` | yes | affirmative response or approval |  |
| `y⋯` | yet | still / so far / continuing / not completed at the present point |  |

#### Z (1)

| Symbol | Root | Working meaning | Shape |
|---|---|---|---|
| `0` | zero | numeric zero | bare letter/digit |


### 3. Look-alike families (read the full entry before you read a glyph)

A shared glyph is a family resemblance, never a definition. Several families are easy to confuse. The members below are all in the table above.

| Glyph family | Members |
|---|---|
| `✓` | `✓` correct, `c✓` confirm, `k✓` known, `r✓` resolve, `s✓` solution, `u✓` understand, `v✓` verify, `y✓` yes |
| `≡` | `c≡` consistency, `i≡` identify, `m≡` match, `r≡` recognize |
| `=` and `≈` | `a=` agree, `s=` same (criterion-relative), `v=` value, `s≈` similar, `≈` estimate |
| `⊢` | `d⊢` derive, `i⊢` infer, `l⊢` logic, `p⊢` prove |
| `∵` | `∵` because, `e∵` explain, `j∵` justify, `r∵` reason, `s∵` support, `?∵` why |
| `↻` | `l↻` learn, `m↻` modify, `r↻` revise, `u↻` update (and `⤿` retry, which is not a revision) |
| `?` | `a?` ambiguity, `c?` check, `i?` investigate, `p?` problem, `u?` unknown, and the interrogative forms `?=`, `?◷`, `?@`, `?⊤`, `?⊙`, `?∵` |
| `◇` | `h◇` hypothesis, `p◇` possible, `s◇` suggest |
| `∃` | `∃` existence, `f∃` find, `s∃` search |
| `#` | `#` count, `k#` key |
| `∈` | `∈` membership, `e∈` example |
| `▷` | `▷` next, `f▷` follow, `g▷` guide, `p▷` process, `s▷` step |
| `n` family | `n` new, `n¬` not, `n⊘` no, `n−` negative, `n0` null, `n□` necessary, `n!` need |
| `0` | `0` zero (a number) is not `n0` (null, an unset field) |
| `⊣` | `c⊣` constraint, `l⊣` limit |
| `@` | `r@` reference (pointer), `s@` source (information origin), `s@*` ancestry, `?@` where |
| `<` and `>` | `a<` ask, `q<` query, `r<` request; `a>` answer, `r>` respond |
| `→` and `←` | `i→` imply, `o→` output, `r→` result; `g←` given, `i←` input, `o←` obtain, `r←` receive |

*End of lexicon reference. 183 entries: 173 base + 10 additional.*


---

# PART C. GRAMMAR AND CONVENTIONS

Reproduced verbatim from the onboarding package, file `P1` (v1.0, unchanged through v1.0.2.1), sections 0.2, 0.3, 0.5 and 1 to 5. Only heading levels were lowered by one so that they nest under this Part. Section numbers inside the text (for example "section 3.5") refer to `P1`. Where the text says `P2`, read Part B of this file. Where it speaks of "this packet", read "this Part". Where it mentions `P3` or `P4` (guided practice and assessment), those are separate onboarding files that are not part of this master. Where it says "the lead researchers", it means C and D. Everything here carries one of the four status labels defined in `P1` section 0.2.

Status notes from D's review of Snapshot 001. (1) `P1` section 0.2 says that unlabelled text in its steps 4 and 5 teaches WORKING meanings and PROVISIONAL conventions together. (2) `A:ψ` is a WORKING grammar agreement whose parsing details are PROVISIONAL; the syntactic boundary with the root `r:` stays OPEN (`P1` section 2.6). (3) The `a.(label)` message form of `P1` section 3.9 is a teaching convention. It is not evidence that an arbitrary label has been formally declared, and not every experimental response followed it; weigh this before calling a line an author error.

---


#### 0.2 Status labels used in this packet

Nothing in this packet is a formally adopted language rule, and nothing in it has been independently validated. Each item carries one of four labels so that you can tell how firmly it stands:

| Label | Meaning |
|---|---|
| **WORKING** | A definition in the team's working vocabulary. It is in use. Treat it as the current meaning, and as not independently validated. |
| **PROVISIONAL** | A reading or convention the lead researchers have agreed to use for now. It may change. |
| **CANDIDATE** | Proposed but not agreed. Use it only when a message marks it as a proposal (`p↗`) or you are told to. |
| **OPEN** | Unresolved. No agreed rule exists. If a message depends on it, mark the point with `a?` and say what is unclear. Do not guess silently. |

Unlabelled text in steps 4 and 5 teaches WORKING meanings and PROVISIONAL conventions together. Where an item is CANDIDATE or OPEN, it is labelled on the spot.

#### 0.3 One notation only

This packet teaches one notation. If you have seen SILEX written in any other way, in earlier conversations or in your memory, **do not mix it in**. If you notice yourself reaching for another notation, say so with `a?` and carry on with the notation taught here. Please also state at the start of your first reply whether you remember anything about SILEX from before, and what. This is recorded so that memory-assisted results are not mistaken for clean learning. It is not penalised.

#### 0.5 Standing declarations for this packet

Unless an exercise says otherwise, these name classes are declared for every exercise in this packet and for the practice and assessment files. They are opaque: a name tells you its class and nothing else.

| Names beginning | Declared as |
|---|---|
| `zp`, `zq`, `zr` | opaque propositions |
| `zk` | agent identifiers (sources of content; nothing is said about who or what they are, or how reliable) |
| `zm` | opaque methods or acts |
| `zo` | opaque objects or items |
| `zv` | opaque values or quantities |
| `zS` | opaque collections |
| `zt` | time names, declared with `d≔(zt0,t)` before use |
| `zcr` | comparison or verification criteria |
| `zh` | hypotheses (propositions) |

A name whose declaration contains quoted English, for example `d≔(zv9,⌜measured value at zt1⌝)`, is a **scaffold**. Its class is stated in the English notes, not inferred by you.

### 1. Step 1: Root words

#### 1.1 What a root is

A **root** is one code with one working meaning. The working vocabulary has **183 entries**: 173 base entries and 10 additional entries. All of them are listed in `P2`. You do not need to memorise `P2`. You need to be able to look an entry up and read it accurately.

A root's **working meaning** is what governs. The English label in `P2` ("given", "support", "same") and the initial letter of the symbol (`g`, `s`) are memory aids only. When the English word and the working meaning differ, the working meaning wins. For example `a=` is labelled "agree", and means *express agreement with a proposition*; it is not an equality sign.

#### 1.2 Code shapes

| Shape | Examples | Note |
|---|---|---|
| Letter + glyph | `g←`, `i→`, `s∵`, `c⊃` | the letter indexes an English concept family; the glyph often hints at a family (section 1.4) |
| Standalone glyph | `~`, `∵`, `∴`, `✓`, `✗`, `≈`, `▶`, `▷`, `⊤`, `↔`, `?` | no letter index |
| Interrogative form | `?=`, `?◷`, `?@`, `?⊤`, `?⊙`, `?∵` | ask-forms: what, when, where, whether, which, why |
| Bare letter or digit | `n`, `t`, `w`, `x`, `0` | new, time, word, placeholder, zero |
| Mention brackets | `⌜ ⌝` | talk about an expression without using it |
| Additional entries | `∧`, `∃`, `∈`, `#`, `⧉`, `⤿`, `⊡`, `s@*`, `⊛` | with boundaries listed in `P2`, section 1 |

#### 1.3 Roots taught in this packet

Seventy-four entries are taught here and used in the practice and assessment files. All other entries are look-up only: if a message uses one, read its entry in `P2`.

| Where taught | Roots |
|---|---|
| Step 4 (simple expressions) | `g←` `h◇` `p◇` `u?` `n¬` `i→` `∧` `d≔` `p↗` `a=` `a?` `r□` `a.` `⌜ ⌝` `e✗` `r↻` `~` `c⊃` `s∵` `c↝` and the attribution form `A:ψ` |
| Step 2 (asking) | `?=` `?◷` `?@` `?⊤` `?⊙` `?∵` |
| Step 5.1 to 5.3 | `i⇒` `d⊢` `i⊢` `c∴` `∴` `p⊢` `u~` `u±` `l≥` `pℙ` `n0` `0` `f∃` `n⊘` |
| Step 5.4 to 5.5 | `v✓` `c✓` `k✓` `f⊤` `v⊨` `e▤` `s@` `r@` `s@*` `⊛` |
| Step 5.6 to 5.8 | `∃` `∈` `#` `⧉` `⊡` `⤿` `m>` `s=` `s≈` `i≡` `m≡` `d≢` `a\|` `d↦` `t` `i!` `r<` `q<` `r→` `c■` `▶` `▷` `c⊣` `d⊙` |

#### 1.4 Look-alikes and absences

A shared glyph is a family resemblance, never a definition. The full look-alike table is in `P2`, section 3. Three groups cause the most trouble.

**Check-like roots.** `✓` correct, `c✓` confirm, `k✓` known, `r✓` resolve, `s✓` solution, `u✓` understand, `v✓` verify, `y✓` yes. They are independent roots. Requesting a verification does not report that it succeeded.

**Sameness-like roots.** `s=` same (relative to a criterion), `s≈` similar (tolerance), `i≡` identify (identity or identification), `m≡` match (under a criterion), `r≡` recognize, `c≡` consistency. Do not treat any two as synonyms, and do not treat any two as proven different. Read each entry; if a message's intent is unclear between two, say `a?`.

**Four different ways of saying "not there".**

| Code | Says |
|---|---|
| `n¬(P)` | the negation of P, as a proposition. Writing it does not by itself assert it. |
| `u?(P)` | P is **not known** in the relevant context. This is not negation. |
| `n0` | a field is **missing or unset** in a declared data context. Not numeric zero. |
| `0` | the number zero |
| `n¬(∃(…))` | non-existence, which needs an **explicit domain** |
| `n¬(f∃(…))` | a *search* found nothing. That is a search result, not non-existence. |
| `n⊘` | a negative answer ("no") to an identified question, proposition or request |

Keep these apart every time.

---

### 2. Step 2: Word formation

How valid expressions are built from roots.

#### 2.1 Application: root plus arguments

A root is applied to arguments in parentheses, separated by commas:

```
n¬(zp1)
i→(zp1,zp2)
d≔(zq3,zp1)
```

- The **comma separates arguments**. It never means AND. To say "both", use `∧`.
- How many arguments a root takes is **not recorded for most roots**. This packet shows the argument structure of every root it teaches. For any other root, read operands from the entry and from the examples you are given. If you cannot tell, say `a?`. Do not invent an arity.

#### 2.2 Nesting

Applications nest. Build from the inside out and read from the outside in.

| Expression | Reading |
|---|---|
| `n¬(zp1)` | the negation of zp1 (a proposition) |
| `g←(n¬(zp1))` | supplied as information: the negation of zp1 |
| `g←(zkp:n¬(zp1))` | supplied as information: the agent zkp is the source of the content "not zp1" |

The **outermost wrapper** tells you what kind of act or status the line carries. Read it first.

#### 2.3 Names and definitions

`d≔(name,expr)` assigns a local name to an expression. It does **not** assert the expression.

```
d≔(zq3,∧(zp1,n¬(zp2)))
```

reads: the local name zq3 stands for "zp1 and not zp2". Nothing is asserted about zp1 or zp2.

- Names are **opaque**. A name's spelling carries no meaning beyond its class (section 0.5).
- Names are **local** to the exercise or message that declares them (section 3.5 for what is still open about names across messages).
- A time name is declared by `d≔(zt0,t)`. This is the one place where a name's class is taken from its definiens. It is **not** a general rule that a name's class can be inferred from what it is defined as.
- Greek letters (`κ`, `μ`, `η`, `ω`) appear as local names in messages between the lead researchers. They behave like any other declared local name.

#### 2.4 Mention: talking about an expression without using it

`⌜x⌝` mentions the expression x. It is talked about, not used, asserted or evaluated.

```
a.(⌜n¬(zp1)⌝)
```

The expression `n¬(zp1)` is acknowledged as received. The writer has **not** said that zp1 is false. Quotation does not decide whether a bare expression would be a command, a description or an assertion.

#### 2.5 Asking: the interrogative forms

| Form | Asks |
|---|---|
| `?=` | what: an identity, a value, or a missing attribute |
| `?◷` | when: event time or temporal position |
| `?@` | where: location or position of a referent |
| `?⊤` | whether: whether a proposition holds (its truth status) |
| `?⊙` | which: choose or identify an item from alternatives |
| `?∵` | why: reasons, grounds or causes |

Example: `?⊤(zp1)` asks whether zp1 holds.

`a?` is **not** one of these. `a?(P)` marks ambiguity concerning P (or insufficient disambiguation). It is not a question and not a request. Several roots end in `?` (`a?`, `c?`, `i?`, `p?`, `u?`) without being questions.

`?t(e)` ("what time value does e have") exists as a proposal. It is a CANDIDATE. A bare `?t` with no operand is not used.

#### 2.6 Attribution: `A:ψ` (WORKING grammar agreement; parsing details PROVISIONAL)

`A:ψ` attributes the content or act ψ to a **declared** agent A.

- Attribution is **not endorsement**: the writer does not thereby back ψ.
- Attribution is **not verification** and **not evidence provenance**.
- Content with no `A:` prefix is not attributed to anyone, and it does not automatically belong to the sender.
- ψ may be a proposition or a status-wrapped expression: `zkq:zp1`, `zkq:h◇(zp1)`.
- The colon also appears inside the root `r:` (relation). How to separate the two in every position is OPEN. In this packet, an `A:ψ` always has a declared `zk…` agent before the colon.

#### 2.7 Argument-order conventions (PROVISIONAL; none ratified)

| Expression | Order |
|---|---|
| `d≔(name,expr)` | name, then what it stands for |
| `i→(P,Q)` | antecedent, then consequent |
| `i⇒(P,Q)` | condition, then consequent |
| `c⊃(h,x)` | context, then the content considered within it |
| `s∵(S,C)` | **support first**, then the claim |
| `c↝(E,F)` | **cause first**, then the effect |
| `d⊢(x,y)` | **derived item first**, then what it was derived from ("x derived from y") |
| `s@(x,y)` | **derived item first**, then its immediate source ("y is x's immediate source") |
| `d↦(v,I)` | value first, then the information that determines it |
| `v✓(x,ω)` | the item checked, then the criterion |
| `∈(x,S)` | item, then collection |
| `r<(A,ψ)` | the party asked, then what is asked |

The orders differ on purpose: the "derived item first" habit of `d⊢` and `s@` is **not** carried over to `s∵` and `c↝`. Two further points are OPEN: the argument order of `c⊣` (constraint), and the argument structure of many roots that this packet does not teach.

---

### 3. Step 3: Grammar

Composition rules, operators, relations and scope.

#### 3.1 Three kinds of line (teaching convention)

| Kind | Examples | May it stand alone? |
|---|---|---|
| **Status markers**: say how content stands | `g←` supplied, `h◇` hypothesis, `p◇` admissible, `u?` not known | yes, wrapping content |
| **Content**: propositions and relations | `n¬`, `∧`, `i→`, `c⊃`, `s∵`, `c↝`, `∃`, `∈`, … | inside a status marker |
| **Dialogue marks**: speech-act marks | `a.` `a=` `a?` `p↗` `r□` `e✗` `r↻` `~` | yes |

Rule for your own writing: **put content relations inside a status marker.** Do not leave a bare content line standing alone.

This is a teaching convention. In their own messages the lead researchers sometimes write bare content lines. What force a bare line carries (does a bare `n¬(P)` assert?) is **OPEN**. Where you meet a bare content line, read its content and say that its force is unspecified.

#### 3.2 What a line does not say

Most mistakes come from reading too much into a line. Learn what each one leaves out.

- `g←(P)` supplies P. It does not verify P.
- `h◇(P)` presents P as a tentative hypothesis. It does not establish P.
- `p◇(P)` says P is admissible under the relevant context or constraints. It does not say P is true.
- `u?(P)` says P is not known. It does not say P is false.
- `i→(P,Q)` relates P and Q. It does not establish P and, by itself, does not establish Q.
- `d≔(x,P)` names P. It does not assert P.
- `a=(P)` expresses agreement with P. `a.(X)` acknowledges receipt of X. Receiving is not agreeing.
- `a?(P)` marks ambiguity. It does not ask whether P is true.
- `r□(P)` states P as a requirement. It does not say the requirement is met.
- `e✗(⌜P⌝)` marks the expression P as erroneous relative to some criterion. It does not give the criterion, does not say P is false, and does not give a replacement.
- `r↻(⌜P⌝)` marks P as revised or under revision. It does not give the replacement.
- `~(P)` adopts P as a temporary working premise. It does not assert P.
- `s∵(S,C)` offers S as support for C. Support is not proof.
- `c↝(E,F)` says E contributes to producing F. It does not say E or F occurred.

#### 3.3 Act, state and result: position decides (PROVISIONAL)

Some roots can name an act or a state. The **position** of the root decides which.

- `i!` (instruction) and `r<` (request) are **directives**. A directive asks for an act; it does not report that the act happened.
- `▶(x)` (execute) triggers execution. It does **not** assert completion.
- `c■` means *complete*. In directive position it is a **completion act**. In state or proposition position it is a **completed state**. A reported completion is not independently verified completion.
- `r→` reports a **result**.
- `r<(A,ψ)` with an act ψ asks A to perform ψ and to report the outcome via `r→`. Retrieving an existing result is `q<`.
- `s≔` carries a state. Placing an operation inside a status field does not by itself make it a state.

Whether `r<` is read as "perform" or "inform" depends on the type of its operand, and the type of some operands (for example `c✓`) is itself OPEN (OG-08, OG-09). If the type is not clear, say `a?`.

#### 3.4 Wrappers go outward; what `∧` can join (PROVISIONAL)

- `∧` joins **propositions**, in proposition position. It does not join directives, and it does not join status-wrapped expressions.
- To combine two instructions, put the wrapper outside: `i!(∧(ψ1,ψ2))` (both acts), or `i!(s≺(ψ1,ψ2))` (the acts in order).
- A named act must be lifted to a state before it is conjoined as a proposition: write `c■(zm1)`, not bare `zm1`.
- Keep these distinct:
  - conditional instruction: `i⇒(P,i!(ψ))`
  - standing conditional requirement: `r□(i⇒(P,i!(ψ)))`
  - an instruction and an assertion: two separate lines, `i!(ψ)` and `g←(P)`
  - an instruction subject to a requirement: `i!(ψ)` and `r□(P)` as two lines
- Mixing a directive and a proposition inside one `∧` is not accepted as well-formed (OG-01). Write separate lines.
- The argument type that `i⇒` accepts as a consequent is OPEN (OG-10).

#### 3.5 Scope: contexts, assumptions, binding, names

**Context.** `c⊃(h,x)` considers x within the context h. In this packet h is an assumption `~(P)` or a time name declared by `d≔(zt0,t)`. The type of h is currently decided only by its shape; whether that is enough is OPEN. Neither the assumption nor x outside it is asserted.

```
c⊃(~(zp5),zp6)
c⊃(zt0,n¬(∃(zv1,∈(zv1,zS1))))
```

The first line: within the assumption zp5, zp6 is considered. The second: at time zt0, there is no zv1 that is a member of zS1.

**Assumption.** `~(P)` records that P is adopted as a working premise. A bare `~` does **not** govern the lines that follow it. Use `c⊃` to say what is considered under an assumption. Results derived under an assumption hold within that assumption; they are neither silently upgraded to unconditional nor silently downgraded.

**Existence and binding.** `∃(v,φ)` binds the local name v inside φ ("some v satisfies φ"). The bare form `∃(x)` means "the referent of x exists", and needs the domain to be stated. Negated existence always needs an explicit domain. "No successor in this finite process" differs from "no successor in any larger sequence". Binding rules for nested and repeated binders are OPEN.

**Names across messages (OPEN: OG-03, OG-04, OG-14).** Names are local to one message or block, yet real exchanges reuse names across messages. Until this is settled, use this discipline:

1. A name is local. Do not assume a name from another message or exercise is still bound.
2. Reusing a name from an earlier message needs an unambiguous reference to its declaration. The qualified form `r@(x,m)` ("x as declared in message m") is a CANDIDATE, not an agreed rule.
3. Identical name strings do not guarantee identical meanings.
4. Redeclaring a name in the same scope must not silently replace an earlier fixed meaning.
5. Names introduced inside a proposal (`p↗`) remain proposals until accepted. Acceptance is by restatement: `a=(d≔(zh9,…))`.
6. A claim that a name is unique is relative to an **identified shared record**, not to "all earlier messages".

#### 3.6 Alternatives: `a|` (PROVISIONAL, OPEN in part: OG-02)

`a|` presents alternatives, and is read by the **type of its operands**:

- Declared **propositions**: inclusive. `a|(P,Q)` holds if P, or Q, or both. Three or more propositions are read the same way.
- Declared **candidate items** that are not propositions: it lists candidates and has no truth value.
- **Mixed or undeclared** operands: unresolved. Say `a?`.

An exclusive reading is not built in. Write it: `∧(a|(P,Q),n¬(∧(P,Q)))`. "Exactly one of n alternatives" needs pairwise exclusions and has no shorter form yet (OG-18).

#### 3.7 Sameness and identity (OPEN in part: OG-05, OG-06, OG-15)

- `s=(x,y)` is **binary**. Its meaning is relative to a **criterion** that must be declared or inherited. If a message uses `s=` and no criterion can be recovered, the expression is **underspecified**: say `a?`. Do not supply a criterion yourself, and do not assume exact numeric equality.
- A ternary form `s=(x,y,κ)` is **not adopted**.
- How a criterion attaches to `s=` is OPEN. One CANDIDATE reading: a context, `c⊃(~(zcr1),s=(x,y))`, "under the assumption that zcr1 is the criterion, x and y are the same".
- Symmetry and transitivity of `s=` hold **only** for a declared equivalence criterion.
- `s≈` is sameness within a tolerance. `m≡` is a match under a specified criterion. `d≢` tells apart by a criterion. The same criterion issue applies.
- `i≡` covers identity and identification. Whether it means exact numerical identity is OPEN. Entity identity, numeric value identity, pattern identification and criterion-relative sameness are four different things.

#### 3.8 Three dimensions of a claim: origin, transmission, status

Do not merge these into one label.

| Dimension | Roots | Question it answers |
|---|---|---|
| **Origin** of the content | `g←` supplied here; `d⊢` derived here; `~` assumed; `⊛` asserted from stored knowledge | Where did the claim come from? |
| **Transmission** of the message | `m▤`, `r←`, `r@` | How did it reach me? |
| **Current status** | `v✓`, `u?`, `k✓`, `f⊤` | Is it verified, unknown, known, established now? |

An origin mark survives forwarding as part of an attributed earlier assertion. A later verification does not rewrite the earlier claim: the history stays.

#### 3.9 Message form

A message from you in practice or assessment is plain lines of SILEX, then short English notes:

```
a.(label)
<SILEX lines>

EN Notes
<short notes, only where needed>
```

`a.(label)` acknowledges receipt of the item labelled `label`. EN notes are scaffolding: they do not replace the SILEX, and they are not evidence that the SILEX conveyed anything.

#### 3.10 What is still open

Do not rely on any of these. If a message needs one, mark it `a?`.

| Item | What is open |
|---|---|
| OG-01 | `∧` operand types and n-ary arity |
| OG-02 | `a\|` typing and n-ary behaviour |
| OG-03, 04, 14 | local names: scope, cross-message reuse, redeclaration, names under proposals |
| OG-05, 15 | how a criterion attaches to `s=`, `s≈`, `m≡`, `d≢` |
| OG-06 | `i≡`: identity, identification, numeric identity |
| OG-08 | `c✓`: act or result |
| OG-09, 10 | `r<` by operand type; `i⇒` consequent type |
| OG-11 | `c⊣` argument order |
| OG-13 | force of a bare top-level expression |
| OG-16 to 18 | dispositional conditionals; time-indexed terms; "exactly one of n" |
| other | parameterized definitions; an ordered status scale; whether `c↝(x,y)` entails x and y; whether `g←` counts as an assertion; `k✓` and `f⊤` factivity |

---

### 4. Step 4: Simple expressions

Basic meaningful statements and how to read them. The twenty roots below, plus the attribution form `A:ψ`, are the foundation. Everything in step 5 is built from them.

#### 4.1 The foundation set

| Symbol | Meaning | It does not say |
|---|---|---|
| `g←(P)` | P is supplied as information | that P is verified or true |
| `h◇(P)` | P is presented as a tentative hypothesis | that P is established |
| `p◇(P)` | P is admissible under the relevant context or constraints | that P is true |
| `u?(P)` | P is not known in the relevant context | that P is false |
| `n¬(P)` | the negation of P | that anyone asserts it, by itself |
| `i→(P,Q)` | proposition-level implication: P implies Q | that P holds, or (alone) that Q holds |
| `∧(P,Q)` | conjunction of propositions: P and Q | anything about directives or status-wrapped acts |
| `d≔(x,P)` | the local name x stands for the expression P | that P is asserted |
| `p↗(P)` | P is put forward as a proposal | that P is adopted |
| `a=(P)` | agreement with P | that P is verified |
| `a?(P)` | P is ambiguous or insufficiently disambiguated | that this is a question |
| `r□(P)` | P is stated as a requirement | that the requirement is fulfilled |
| `a.(X)` | X is acknowledged as received | agreement, belief or evaluation |
| `⌜x⌝` | the expression x is mentioned | that x is used, asserted or evaluated |
| `e✗(X)` | X contains an error relative to some criterion | the criterion, the correction, or that P is false (for `e✗(⌜P⌝)`) |
| `r↻(X)` | X is being revised after reconsideration | what the revision is |
| `~(P)` | P is adopted as a temporary working premise | that P is asserted, or that the assumption governs later lines |
| `c⊃(h,x)` | x is considered within the context h (here an assumption `~(P)` or a time) | that the assumption, or x outside it, is asserted |
| `s∵(S,C)` | S is offered as support for the claim C; support first, claim second | that S proves C |
| `c↝(E,F)` | E contributes to producing F; cause first, effect second | that E or F occurred (whether `c↝` entails occurrence is OPEN; read it as not saying so) |
| `A:ψ` | ψ is attributed to the declared agent A | endorsement, verification or provenance |

Status: the roots are WORKING. The readings of `s∵` and `c↝` as to argument order, and the use of `e✗` and `r↻` on a mentioned expression, are PROVISIONAL. `A:ψ` is a WORKING grammar agreement whose parsing is PROVISIONAL.

#### 4.2 Essential distinctions

- **Supplied versus established.** `g←(P)` supplies P; it does not make P true.
- **Hypothesis versus possibility.** `h◇(P)` treats P as a tentative hypothesis. `p◇(P)` treats P as admissible. They are related, not interchangeable.
- **Unknown versus false.** `u?(P)` is not `n¬(P)`.
- **Acknowledged versus agreed.** `a.` says "received". `a=` says "I agree".
- **Mentioned versus used.** In `a.(⌜n¬(zp1)⌝)`, `n¬(zp1)` is only talked about.
- **Attributed versus endorsed.** `zkp:zp1` says zkp is the source of zp1, not that zp1 is true or that the writer believes it.
- **Assumed versus asserted.** `~(zp5)` adopts zp5 as a premise without asserting it.
- **Supported versus proved.** `s∵(zp8,zp9)` offers zp8 as support for zp9. Support is not proof.
- **Cause versus occurrence.** `c↝(zp10,zp11)` is not a report that either happened.
- **Error mark versus negation.** `e✗(⌜P⌝)` marks P as erroneous. It does not say P is false.
- **Ambiguity mark versus question.** `a?(P)` is not asking whether P is true.

#### 4.3 A reading procedure

For any line, in order:

1. **Outermost wrapper.** What kind of act or status is this (supply, hypothesis, agreement, mention, proposal, requirement)?
2. **Attribution.** Is the content attributed to an agent (`A:ψ`)? Is anything mentioned (`⌜ ⌝`) rather than used?
3. **Content.** Read inward, one nesting level at a time.
4. **Names.** Are all names declared in this exercise? Which class is each?
5. **What is not said.** List, for the outer wrapper and each relation inside it, what it leaves out (section 3.2).

#### 4.4 Worked examples

Meanings are supplied deliberately. Names follow the standing declarations (section 0.5).

**S1**
```
g←(zp1)
```
zp1 is supplied as information. Its truth is not independently verified.

**S2** (two lines)
```
h◇(zp2)
p◇(zp2)
```
zp2 is presented as a tentative hypothesis, and as admissible. Neither line establishes zp2.

**S3** (two lines)
```
u?(zp3)
g←(n¬(zp4))
```
zp3 is not known. In contrast, the negation of zp4 is supplied. "Not known" and "negated" are different.

**S4**
```
g←(zkp:zp5)
```
The agent zkp is the source of the content zp5. zp5 is supplied, not verified, and the writer does not endorse it.

**S5**
```
g←(i→(zp6,zp7))
```
Supplied: zp6 implies zp7. Neither zp6 nor zp7 is thereby established.

**S6** (two lines)
```
d≔(zq8,∧(zp1,n¬(zp2)))
u?(zq8)
```
The name zq8 stands for "zp1 and not zp2". Then: zq8 is not known. The first line asserts neither zp1 nor the negation of zp2. The second does not say zq8 is false.

**S7** (two lines)
```
p↗(h◇(zp9))
a.(⌜p↗(h◇(zp9))⌝)
```
A proposal is made: zp9 as a hypothesis. A second party acknowledges receipt of that proposal expression. Nothing is adopted, and nothing is agreed.

**S8**
```
a?(zp10)
```
The writer marks zp10 as ambiguous or insufficiently disambiguated. This is not a question about whether zp10 is true.

**S9**
```
r□(zp11)
```
zp11 is stated as a requirement. Nothing says it is fulfilled.

**S10** (two lines)
```
e✗(⌜g←(zp12)⌝)
r↻(⌜g←(zp12)⌝)
```
The expression `g←(zp12)` is marked as containing an error, and as under revision. This does not say zp12 is false, does not say what the error is, and does not give the replacement.

**S11** (two lines)
```
~(zp13)
g←(c⊃(~(zp13),zp14))
```
zp13 is adopted as a working premise without being asserted. Supplied: within that premise, zp14 is considered. Outside the premise nothing is said about zp14.

**S12** (two lines)
```
g←(s∵(zp15,zp16))
h◇(c↝(zp17,zp18))
```
Supplied: zp15 is offered as support for zp16 (support first, claim second). Separately, hypothesis: zp17 contributes to producing zp18 (cause first, effect second). It is not said that any of them occurred or is true.

**S13**
```
g←(zkq:s∵(zp19,zp20))
```
The agent zkq presents zp19 as support for zp20. The writer does not endorse that support claim.

**S14**
```
a=(zp21)
a.(⌜g←(zp21)⌝)
```
Agreement with zp21 is expressed. Separately, the expression `g←(zp21)` is acknowledged as received. Receiving is not agreeing, and the second line does not supply zp21.

---

### 5. Step 5: Complex expressions

Conditions, inference, uncertainty, evidence, origin, quantity, sameness, and acts. Each subsection adds roots to the foundation set. Examples have supplied interpretations. Declare time names with `d≔(zt0,t)` wherever `zt0` is used.

#### 5.1 Conditions and assumptions

| Root | Working meaning |
|---|---|
| `i→(P,Q)` | a relation between two propositions: P implies Q |
| `i⇒(P,Q)` | a conditional premise: it fixes when the consequent applies. Its consequent can be an instruction. Whether it reads as a rule or as a material conditional is OPEN. |
| `c⊃(h,x)` | x is considered within the context h |
| `~(P)` | P adopted as a working premise |

**C1**
```
g←(i⇒(zp1,zp2))
```
Supplied: a conditional premise. When zp1 holds, zp2 applies. zp1 is not asserted.

**C2**
```
g←(n¬(i→(h◇(zp3),zp3)))
```
Supplied: presenting zp3 as a hypothesis does not imply zp3. A hypothesis does not entail, or establish, its own content.

**C3** (two lines)
```
~(zp4)
g←(c⊃(~(zp4),i→(zp5,zp6)))
```
zp4 is adopted as a premise. Supplied: within that premise, zp5 implies zp6. Outside the premise nothing is said about zp5 and zp6.

**C4**
```
r□(i⇒(zp7,i!(▶(zm1))))
```
A standing conditional requirement: when zp7 holds, the instruction to execute zm1 applies. It does not say zp7 holds, and it does not say zm1 is executed.

#### 5.2 Inference and derivation

| Root | Working meaning |
|---|---|
| `d⊢` | derive: obtain by rule-based inference. `d⊢(x,y)`: x derived from y. |
| `i⊢` | infer: derive a conclusion using premises and inference rules |
| `c∴` | conclude: reach a conclusion from premises or evidence |
| `∴` | therefore: a marker linking an already established basis to a subsequent claim |
| `p⊢` | prove: establish a conclusion under specified formal premises and rules |
| `s∵` | support: evidence or a reason in favor of a claim (not derivation) |
| `c↝` | cause: directed causal influence (not logical implication) |

`d⊢` and `i⊢`, and `c∴` and `∴`, are all retained as separate entries. No one has shown them to be exact synonyms, and no one has shown them to differ. Read each by its own entry. If a message's choice between two of them matters and is unclear, say `a?`.

**C5**
```
g←(d⊢(zp8,∧(zp1,zp2)))
```
Supplied: zp8 is derived from "zp1 and zp2" (derived item first). This does not establish zp1, zp2 or the validity of the derivation.

**C6**
```
g←(n¬(i→(s∵(zp9,zp10),zp10)))
```
Supplied: that zp9 supports zp10 does not imply zp10. Support is not proof.

**C7** (two lines)
```
h◇(c↝(zp11,zp12))
g←(zp12)
```
Hypothesis: zp11 contributes to producing zp12. Supplied: zp12. You cannot conclude that zp11 occurred. `c↝` does not say the cause occurred, and a supplied effect does not establish a hypothesised cause.

#### 5.3 Uncertainty and possibility

| Root | Working meaning |
|---|---|
| `u?(P)` | P is not known in the relevant context (distinct from a missing entry) |
| `u~(P)` | P is not established at the required confidence or epistemic standard |
| `u±` | the degree, interval or range of uncertainty attached to an estimate or state |
| `p◇(P)` | P is admissible under the stated context or constraints |
| `h◇(P)` | P is a tentative hypothesis |
| `l≥` | likelihood meets a contextually specified threshold (the threshold must come from context) |
| `pℙ` | a quantitative measure of likelihood relative to a model or context |
| `n0` | a field is missing or unset in a declared data context; not numeric zero |
| `0` | the number zero |
| `f∃` | a search or identification found a matching entity |
| `n⊘` | a "no" given to an identified question, proposition or request |

**C8** (two lines)
```
u?(zp13)
u~(zp14)
```
zp13 is not known in the context. zp14 is not established at the required confidence standard. Neither line says either proposition is false. If it matters which of `u?` and `u~` a writer meant and the message does not make it clear, say `a?`.

**C9**

The four-way absence table in section 1.4 applies here. Compare four statements about a collection zS1: "zS1 has no member at zt0" (non-existence, needs the domain: see section 3.5), "a search of zS1 found nothing" (a search result, not non-existence), "it is not known whether zS1 has a member" (`u?`), and "the member field of zS1 is unset" (`n0`). They are four different claims and must not be merged.

#### 5.4 Evidence, verification and knowledge

| Root | Working meaning |
|---|---|
| `v✓(x,ω)` | verify: check x against the criterion ω and relevant evidence |
| `c✓` | confirm: confirm prior content against supporting evidence or criteria. Act or result? OPEN. |
| `k✓` | known: an epistemic status, established relative to an agent, a context and standards |
| `f⊤` | fact: a proposition treated as established under specified evidence or context |
| `v⊨(x,ω)` | x satisfies the applicable conditions or criterion ω |
| `e▤` | evidence: information relevant to testing, supporting or challenging a claim |

Principles (PROVISIONAL):

- `v✓`, `c✓` and `k✓` are independent roots.
- **Requesting** verification does not assert that it succeeded.
- A completed **inconclusive** test, a completed **negative, criterion-relative** test, and a **process error** are three different outcomes. Failing a criterion is not automatically universal falsity.
- Satisfying a criterion ω is not the same as ω being independent evidence: ω may depend on the thing checked.
- Do not rely on an unprefixed `k✓`. Its holder and its factivity are not settled. Prefer `zkq:k✓(P)`.
- Agreement between two participants is not validation.

**C10**
```
r<(zkq,v✓(zp1,zcr1))
```
zkq is asked to verify zp1 against the criterion zcr1. This does not report that verification succeeded, and it does not assert zp1.

**C11** (two lines)
```
g←(v⊨(zo1,zcr1))
u?(v⊨(zo2,zcr1))
```
Supplied: zo1 satisfies the criterion zcr1. It is not known whether zo2 satisfies zcr1. The second line is not a failure result.

#### 5.5 Origin and provenance

Four origins of a claim x are distinguished: supplied in this context (`g←`), derived here (`d⊢`), assumed (`~`), and asserted from stored knowledge (`⊛`).

| Root | Working meaning |
|---|---|
| `s@(x,y)` | y is x's **immediate** information source |
| `s@*(x,y)` | y is an indirect or direct ancestor of x: reachable from x by one or more `s@` steps |
| `r@` | a pointer or reference. **Not** provenance. |
| `⊛(x)` | asserted from the speaker's stored knowledge. It does not make x true, verified or current. |

The working definition of `s@*` has two rules: a direct source is an ancestor; and if y is a source of x and z is an ancestor of y, then z is an ancestor of x. Whether `s@*(x,x)` can hold depends on the source graph. In a graph with a cycle it can. Irreflexivity is valid **only** under an explicit acyclicity assumption. Whether the source graph is complete is a further, separate assumption.

**C12** (two lines, then a conclusion line)
```
g←(s@(zo1,zo2))
g←(s@(zo2,zo3))
∴ s@*(zo1,zo3)
```
zo2 is zo1's immediate source, and zo3 is zo2's immediate source. Therefore zo3 is an ancestor of zo1. This says nothing about equal content or about whether any original is still stored.

**C13**
```
g←(r@(zp1,zo4))
```
A reference from zp1 to zo4. It does not establish that zo4 is where zp1 came from. For origin, `s@` is the root.

**C14** (two lines)
```
g←(zkp:⊛(zp1))
g←(n¬(i→(⊛(zp1),v✓(zp1,zcr1))))
```
The agent zkp asserts zp1 from its stored knowledge. Supplied: stored-knowledge origin does not imply that zp1 has been verified against zcr1. The origin mark can travel with the claim when it is forwarded, but it does not become a status of truth.

**A local separation predicate.** A message may declare a local predicate `ι(x,y)` meaning "no source-ancestry link between x and y in either direction, and no common ancestor, under a declared graph completeness". It is a local name, not a root. Source-graph separation is **not** statistical, causal or methodological independence, and "no shared ancestor found" in an incomplete graph is not "independent". Unless `ι` is declared in the message you are reading, treat it as undeclared.

#### 5.6 Existence, membership, counting, copies, retention, retry

| Root | Working meaning |
|---|---|
| `∃(v,φ)` | some v satisfies φ; v is bound locally. A negated form needs an explicit domain. |
| `∈(x,S)` | literal membership of x in S |
| `#(x)` | a count; the unit and domain must be fixed |
| `m>` | more of a specified quantity or measure than another |
| `⧉(x)` | a copy of x |
| `⊡(x)` | x is retained and accessible |
| `⤿(x)` | retry or repeat the operation x |

**C15** (two lines)
```
d≔(zt0,t)
g←(c⊃(zt0,∃(zv1,∈(zv1,zS1))))
```
At zt0, some zv1 is a member of zS1.

**C16**
```
g←(m>(#(zS1),#(zS2)))
```
Supplied: the count of zS1 exceeds the count of zS2, with the counting unit and domain fixed by context. It is a count, not a measurement.

**C17** (three lines)
```
d≔(zo2,⧉(zo1))
g←(n¬(i≡(zo2,zo1)))
g←(⊡(zo1))
```
zo2 names a copy of zo1. Supplied: the copy is not the original (entity identity). Supplied: zo1 is retained and accessible. Nothing here says the copy stays equal to the original. For that you would need `s=` with a criterion (section 5.7).

**C18**
```
i!(⤿(zm1))
```
An instruction to retry zm1. It is not a revision. No retry limit is expressed.

#### 5.7 Sameness, identity and determination

| Root | Working meaning |
|---|---|
| `s=(x,y)` | x and y are the same, relative to a criterion that must be declared or inherited |
| `s≈` | similar: approximate equality within a similarity criterion |
| `i≡` | identify: identity or pattern identification (OPEN: exact numeric identity) |
| `m≡` | match two entities or patterns under a specified criterion |
| `d≢` | distinguish: tell apart by a criterion |
| `d↦(v,I)` | determine: map available information I to a resolved value v. Needs consistent information sufficient to fix exactly one value for the declared task. |

**C19** (CANDIDATE reading)
```
c⊃(~(zcr1),s=(zv1,zv2))
```
Under the assumption that zcr1 is the criterion, zv1 and zv2 are the same. This way of attaching a criterion is a CANDIDATE.

**C20**
```
a?(s=(zv1,zv2))
```
Used when no criterion for `s=` can be recovered. It marks the comparison as underspecified instead of inventing a criterion.

**C21**
```
g←(d↦(zv3,zo5))
```
Supplied: the value zv3 is determined by the information zo5 (value first). An instruction to attempt determination, `i!(d↦(zv3,zo5))`, would not assert that it succeeded. Determination is not physical truth.

#### 5.8 Directives, processes and results

| Root | Working meaning |
|---|---|
| `i!` | an instruction: a directive or action requirement |
| `r<(A,ψ)` | request: seeks information or an action from A |
| `q<` | query: a demand for information, retrieval or an answer |
| `r→` | a reported result of a process or inference |
| `c■` | complete: bring an incomplete state to a completed state (act in directive position, state in proposition position) |
| `▶` | execute: a trigger; does not assert completion |
| `▷` | next or successor; does not imply execution |
| `c⊣` | constraint: restricts permitted possibilities or operations (argument order OPEN) |
| `d⊙` | decide: choose among options and settle a decision |
| `t` | time: a time concept, value or variable |

**C22**
```
i!(▶(zm1))
```
An instruction to execute zm1. It does not assert that zm1 was executed or completed.

**C23** (two lines)
```
r<(zkq,▶(zm1))
g←(zkq:c■(zm1))
```
zkq is asked to execute zm1 and to report the outcome. Supplied: zkq is the source of the content "zm1 is completed". That is a reported completion. It is not independently verified completion, and the writer does not endorse it.

**C24**
```
r<(zkq,d⊙(zo3))
```
zkq is asked to decide zo3. It does not say a decision was made.

#### 5.9 One composed message

Two sources, `zkA` and `zkB`, observe one process. `zp1`: the measured quantity increased between `zt0` and `zt1`. `zp2`: no change was detectable at zkB's resolution. The class declarations of section 0.5 apply; the roles of zp1 and zp2 are stated here in English because the packet has no roots for "measured quantity" or "resolution".

```
d≔(zh1,∧(zp1,n¬(zp2)))
d≔(zh2,∧(n¬(zp1),zp2))
d≔(zh3,∧(zp1,zp2))
d≔(zh4,∧(n¬(zp1),n¬(zp2)))
g←(zkA:zp1)
g←(zkB:zp2)
g←(n¬(i→(∧(zkA:zp1,zkB:zp2),zp1)))
g←(n¬(i→(∧(zkA:zp1,zkB:zp2),n¬(zp1))))
p◇(zh3)
u?(zh3)
g←(a|(zh1,zh2,zh3,zh4))
h◇(zh1)
```

**Reading.** The four names are the four combinations of truth values of zp1 and zp2; no assertion is made about any of them. zkA is the source of zp1 and zkB is the source of zp2: attribution, not endorsement. Supplied: the two reports together imply neither zp1 nor its negation. Both could hold (`p◇(zh3)`), but it is not known whether they do (`u?(zh3)`). Supplied: at least one of the four combinations holds (inclusive `a|`; the four are mutually exclusive by construction, but `a|` does not say so, and saying so would need pairwise exclusions). Finally, zh1 is presented as a hypothesis.

**A design habit (a working observation, not a rule).** Put the most consequential distinction in the outermost wrapper. If a message is shortened, inner content can survive while its status does not. An outer `h◇` or `u?` then still marks how the content stands.

#### 5.10 Common misreadings

Check your reading against this list.

1. `a?` read as a question.
2. `r@` read as provenance. (`s@` is origin.)
3. `g←`, `h◇` or `p◇` read as establishing the content.
4. `u?` read as `n¬`.
5. `c↝` read as saying the cause or effect occurred.
6. `s∵` read as proof.
7. `∧` used to join directives, or a directive and a proposition.
8. `s=` read with an invented criterion, or exact numeric equality assumed.
9. `s@*(x,x)` treated as impossible without an acyclicity assumption.
10. Attribution `A:ψ` read as endorsement, verification or provenance.
11. `▶` read as completion, or reported completion read as verified completion.
12. A name from another message or exercise treated as still bound.
13. An English label overriding a working meaning (`a=` as "equals").
14. `n¬(f∃(…))` read as non-existence.
15. `⊛` read as a mark of truth.
16. Agreement between two participants read as validation.
17. A requested verification read as a successful one.
18. `ι` read as statistical independence.


---

# PART D. OPEN GRAMMAR ITEMS AND FURTHER GAPS

None of these is resolved here, and **no unresolved convention is adopted.** Where a message depends on one of them, mark the point `a?` and say what is unclear. That is correct behaviour, not a failure.

## D.1 Open Grammar Appendix (from the 2026-10-20 checkpoint)

Status words are as recorded at the checkpoint. The checkpoint document itself is not in this file (Part I.2), so D could not authenticate the status of each item. None of them is promoted to an adopted rule here.

| ID | Issue | Status at the checkpoint |
|---|---|---|
| OG-01 | `∧` operand types and arity (directives? status-wrapped? n-ary?) | Open |
| OG-02 | `a\|` typing and n-ary behaviour | Open (type-sensitive reading in use) |
| OG-03 | Local names: scope and declaration | Open |
| OG-04 | Cross-message names: qualified reference and dereferencing | Open |
| OG-05 | `s=`: how a criterion binds | Open |
| OG-06 | `i≡`: identity, identification, numeric identity | Open |
| OG-07 | `d↦` | Provisional agreement |
| OG-08 | `c✓`: act or result | Provisional, partly untested |
| OG-09 | `r<` by operand type | Open |
| OG-10 | `i⇒`: consequent type and scope of directive force | Open |
| OG-11 | `c⊣`: argument order and signatures | Open |
| OG-12 | `s∵` and `c↝` | Provisional agreement |
| OG-13 | Force of a bare top-level expression (does bare `n¬(P)` assert?) | Open |
| OG-14 | Redeclaration and names under proposals | Open candidate |
| OG-15 | Criterion-taking roots `s=`, `s≈`, `m≡`, `d≢` | Open candidate |
| OG-16 | Dispositional and counterfactual conditionals | Open candidate |
| OG-17 | Time-indexed terms; `c⊃` takes propositions; `s◷` arity | Open candidate |
| OG-18 | "Exactly one of n" | Open candidate |

## D.2 Further gaps (not in the appendix)

1. **There was no consolidated Working Master for the symbolic notation before this snapshot.** An older master of the earlier notation is marked historical and outdated and is not authority. This file is an assembly of the 2026-10-19 lexicon, the 2026-10-20 conventions and the later findings.
2. **No arity or signature table exists for the 183 entries.** Argument orders are taught only for roots used in Part C. For other roots, read the entry and the examples; if you cannot tell, say `a?`. Do not invent an arity, and do not recover meaning silently from the English spelling of an identifier.
3. **Whether `g←` asserts its content.** Read it as "supplies, does not verify". Its assertion status is unsettled.
4. **Factivity of `k✓` and `f⊤`.** Neither should be read as truth without stated evidence or context. An unprefixed `k✓` has no stated holder; prefer `zkq:k✓(P)`.
5. **`c↝(x,y)` and occurrence.** Whether it entails that x and y occurred is open. Read it as not saying so.
6. **`g◎(P,ω)`**: scope and arity is an owner-reserved decision. Not taught.
7. **Time questions.** `?◷` exists. The proposed `?t(e)` is a CANDIDATE only.
8. **"Exactly one of n"** and exclusive alternatives have no short form (OG-18).
9. **`ι` (separation predicate)** is not a root. It is undeclared unless a message declares it. Source-graph separation is not statistical, causal or methodological independence.
10. **Look-up-only entries lack tests.** Only 74 of the 183 entries were taught and exercised.
11. **Hidden English.** Declarations written in English ("scaffolds") are allowed in teaching and are not evidence that SILEX carried the meaning. How a scaffold should be written in SILEX is not settled.

## D.3 Findings from the numerical-representation cycle (DN02 and DN03, 2026-10-21)

These are C's critical findings on the proposals of D and the reviews of G and M. **Nothing was adopted.** Each numbered item carries its own label: OPEN for an unresolved specification issue; CANDIDATE only for an identifiable proposed form or interpretation; an item that is only an analytical or methodological finding says so and has no language-rule status. None was tested by a reader who had not written it. The original DN02 and DN03 proposal texts and the full reviews are not in this file (Part I.2), so D cannot certify that each candidate is attributed to the right originator. Read the attributions as "as recorded by C".

1. **[OPEN] Numerals are the first blocker for ordinary SILEX.** The lexicon has `0` only. (Inside the TEST-ONLY `✠` notation, non-negative integers are already defined, Part E, S2. This item concerns numerals outside it.) Digits 1 to 9, sign, decimal point, and whether a numeral is an atom are unspecified. A bare numeral does not say whether it claims exactness. A token such as `08` has no stated treatment. How a digit string is told apart from a name that contains digits (`zo1`) is not stated. Decide numerals before any other numerical item.
2. **[OPEN; the term form is a CANDIDATE] Binding an object, an attribute and a value.** The lexicon has the vocabulary (`v=`, `s≔`, `d↦`, `m∥`, `s=`, `m≡`) but **no defined argument structure** for it. A proposition-forming triple cannot be compared directly and needs a quantifier; a term-forming value expression such as `v=(object,attribute)` nests inside `m>`. G and M both prefer the term form, and C's analysis agrees that a term nests while a predicate does not, but C did not choose between the candidates. The term form's argument order is a new convention on an existing root, which the project has not ratified (Part C, section 2.7 lists no order for `v=` or `s≔`). Binding by identifier suffix or by adjacency of lines is the hazard identified in the first tests.
3. **[CANDIDATE reading of existing roots; `l⊣` details OPEN] Comparison.** `n¬(m>(x,y))` already says "x is not more than y", and `n¬(m>(y,x))` says "y is not more than x". New symbols for "at most" and "at least" are redundant. The condition is that both values are known and on one scale and unit; otherwise the form can assert something it should not. `l⊣` (limit) could carry a bound, but its argument order and its handling of the bound value (allowed or not) are undefined.
4. **[OPEN; the two options named are CANDIDATES] Units and scale.** `m∥` is glossed as measuring "under a specified scale and unit", so the lexicon already treats unit and scale as part of a measurement, but no argument carries them. Candidates: a fourth argument on `m∥` (order undefined), or a unit declared once as a defined proposition and scoped with `c⊃(~(P),…)`. A criterion name given to `~` adopts nothing, because `~` adopts a proposition. Comparison across different units is unresolved.
5. **[OPEN] Equality of numbers.** `s=` needs a stated criterion (OG-05, OG-15). Recording a value (`s≔`, `d≔`, `g←` over a relation) and testing equality (`s=`) are different jobs. The boundary between `d≔` ("assign a fixed meaning") and `s≔` ("declare an entity's state or assigned value", with English scope still to be clarified) is not stated. `d≔`, `s≔` and `s=` are not interchangeable merely because all can appear near numerical content.
6. **[OPEN] Unknown, absent, zero.** Three cases must be kept apart: a value exists but is unknown (`u?`), the relation is not known to hold (`u?` over the relation), and no value is recorded or applicable (`n0`). Whether `u?` and `n0` may take a term as argument is a type question.
7. **[OPEN] Conflict.** `c≠` exists, but it does not say when two numerical lines conflict. They conflict only if object, attribute, unit, scope and time match and the attribute is single-valued. How "single-valued" is marked is unresolved.
8. **[OPEN] Attribute meaning.** A name such as `zaCost` still carries its meaning in its spelling. If attributes must mean something independent of English, each needs a declared definition.
9. **[OPEN; the delimiter forms are CANDIDATES] Embedded payloads** (tables, LaTeX, formulas inside a SILEX message). Moves the burden to three points: how a name is bound to a block, what the block's own format means, and whether two payloads are "the same". The project has no parser, so "mechanically recognisable" means "reliably recognised by a model reader". A boundary criterion between SILEX content and domain payload is missing. `⌜x⌝` is defined for an expression, not for external text. Delimiter proposals (`lx▷` begins, `lx◁` ends) conflict with code-shape conventions (two letters plus a glyph fits no code shape); `◁` is not in the lexicon; `▷` is "next". An escape rule and its alternatives (named terminator, declared length, out-of-band) were compared; none was chosen.
10. **[Analytical finding, not a language rule] Validity of tests with payloads.** If the payload is read natively by each model, a successful exchange tests the model's ability to read the payload, not SILEX. Score recovery of the SILEX-level act (who asked whom for what, with which status) separately from recovery of the payload.

Suggested tests from the cycle (none run): numerals `0`, `8`, `10`, `08`, `zo1`; term nesting against the status quo, with opaque renamed identifiers; recording with `s≔`, `d≔` and `g←`; conflict, with and without matching scope and time; unit mismatch; boundary-equal values; payload boundary recognition with adversarial payloads. Use readers who did not write the candidate.

---


# PART E. TEST-ONLY MATHEMATICAL NOTATION

## E.1 Status and origin

**TEST-ONLY. Not adopted. Not part of the 183-entry lexicon.** The marker `✠` and the heads below (`+`, `×`, `∫` and the rest) are **not** entries in Part B; among sign-like roots only `n−` (negative) exists there. The notation is valid only inside `✠( … )`. Text outside `✠( … )` is ordinary SILEX (Part B and Part C).

Origin. D proposed a math-domain marker `✠` with a three-slot form `✠(v₁,v₂,O)` (operand, operand, operator) at every operation node ("Form A"). C compared it, analytically, with a form that has one outer `✠( … )` and ordinary `head(arguments)` nodes with the operator as the head ("Form B", C's construction). The test notation below uses the **Form B structure**. C's analysis: Form A makes every fragment self-describing and fits only binary operations (a one-operand operation such as `sin x` needs an undefined placeholder); Form B handles unary operations and operator-dependent argument roles but a fragment copied out of its message no longer says it is mathematics. Neither was adopted. The owner's clarification: `✠` is a math-domain marker. Whether it should appear at every node or once per expression was left open by the owner; the test notation uses once per expression. The precise historical priority of the two formulations cannot be verified from this file; the provenance files (Part I.1) are the reference.

## E.2 Specification v0.1 (S1 to S7)

Reproduced from the provenance file `SILEX-MATH-EXP01-SPEC-v0.1-PROVENANCE`. v0 is the same except that S6 was changed in v0.1 (S6 now separates the mathematical value from its representational form). S1 to S5 and S7 are word for word as in v0.

**S1. Marker.** `✠( E )` marks one mathematical expression E. There is exactly one outer `✠` per expression. Nested operations inside E do not repeat it. Text outside `✠( … )` is ordinary SILEX.

**S2. Terms.** E is one of:
- a numeral: a non-negative integer in decimal digits, with no leading zeros except `0` itself (no decimals, no negative literals);
- a variable: one lowercase Latin letter (`x`, `y`, `i`, `t`, …);
- the constant `π` (circumference over diameter);
- an application `head(a₁, a₂, …)`.

**S3. Application.** `head(…)` applies the operation named by `head` to its arguments, which are terms separated by commas. Argument order is significant as given in S4. Structure comes only from nesting: there is no operator precedence and no implicit grouping. Whitespace is not significant.

**S4. Signatures.**

| Head | Arguments | Meaning |
|---|---|---|
| `+` | (a, b) | a plus b |
| `−` (U+2212) | (a, b) | a minus b (first minus second) |
| `×` | (a, b) | a times b |
| `÷` | (a, b) | a divided by b (first by second) |
| `^` | (a, b) | a raised to the power b (first is the base) |
| `√` | (a) | principal non-negative square root of a |
| `sin`, `cos` | (a) | sine, cosine; a in radians |
| `ln` | (a) | natural logarithm of a |
| `∫` | (f, v, lo, hi) | definite integral of f with respect to v, from lo to hi |
| `Σ` | (f, i, lo, hi) | sum of f for integer i = lo, lo+1, …, hi (inclusive) |
| `lim` | (f, v, p) | two-sided limit of f as v approaches p |

The five arithmetic heads take exactly two arguments. The unary functions take exactly one.

**S5. Binding.** In `∫`, `Σ` and `lim`, the second argument names a variable that is bound inside the first argument f only. The arguments lo, hi and p are outside that binding. The same letter appearing outside f is a different (free) occurrence.

**S6. Evaluation, value and representation.**
- The *value* of an expression is the number it denotes. The same value can be written as many different expressions; for example `÷(25,8)` and `÷(50,16)` have the same value.
- A bare `✠( E )` denotes the expression E. It requests no evaluation and states no value.
- `cƒ(✠( E ))` requests the evaluation of E, that is, the value of E.
- `r→(cƒ(✠( E )), ✠( V ))` claims that the value of E equals the value of V. V may be any term allowed by S2 to S4. It need not be a numeral and need not be in simplest form. The claim is about the value, not about the spelling of V. It may be right or wrong.
- Decimals are not defined (S7). A value that is not a non-negative integer is written as an expression, for example `÷(25,8)`.
- A value reported in answer to a request for evaluation may be written as `✠( V )` under the same rules.

**S7. Not defined.** Unary minus, decimals, relations and equations, derivatives, piecewise definitions, vectors, matrices, and any function or symbol not listed in S4. An expression that needs notation not listed here is outside this test.

Version hashes (SHA-256): v0 file `4451e08993d42a210bff05521e04ae0a0da071f86f4efc1e40752082c1bc9326`; v0.1 provenance file `e3f9b681f0c3bce461375bae255b18f7a394d7ad1c8df882c2c9ad3c999f6c90`. Which version a test used must always be recorded: a result belongs to the exact version the reader received.

## E.3 How participants used the notation inside SILEX (observed practice, not agreed conventions)

In Experiment 03 the participants combined the notation with Part B and Part C roots as follows. Treat these as observed uses that were not ratified. Their status is TEST-ONLY wherever `✠` is involved, and OPEN where the free-variable or function-binding reading is unresolved. They do not inherit WORKING status from the established roots around them.

| Use | Form seen | Note |
|---|---|---|
| Name an expression | `d≔(ρ,✠(…))` | `d≔` names, it does not assert. Greek letters as local names follow the lead researchers' habit (Part C, section 2.3). |
| Supply a premise | `g←(✠(…))` | Supplies, does not verify. |
| Request evaluation | `cƒ(✠(E))` | S6. |
| Value claim | `r→(cƒ(✠(E)),✠(V))` | S6. The claim may be wrong. |
| Approximate claim | `s≈(✠(E),✠(V))` | `s≈` needs a similarity criterion (Part C, section 3.7); none was stated. |
| Unknown value | `u?(cƒ(✠(E)))` | Not known; not false. |
| Check / solution marks | `c?`, `s✓`, `s◇`, `k✓` | `s✓` ("solution") does not by itself prove verification (Part B, section 3 look-alikes). |

## E.4 Techniques that need only the existing heads (checked by C's script)

These were checked numerically by C's script (Experiments 02 and 03). That is C's own check, not an independent validation. The checks show that something is expressible; they do not make the forms conventions.

1. **The exponential.** e^a is written `lim(^(+(1,h),÷(a,h)),h,0)`, the limit of (1+h)^(a/h) as h→0. Use a letter other than the one you vary elsewhere (h, not t). A bare letter `e` is only a free variable under S2; it has no value.
2. **Negation.** There is no unary minus. `−(0,x)` gives the same value as −x but is a different expression.
3. **Decimals.** Write a rational: `÷(127190387,1000000)` for 127.190387.
4. **A derivative.** Write the difference quotient as a limit by substituting `+(t,h)` for `t`: `lim(÷(−(f at t+h, f at t),h),h,0)`, with f written out in full. There is no function application in v0.1. (`f at t+h` and `f at t` above are schematic placeholders. They are not valid expressions under S2 to S4 until f is expanded.) Status: primitive derivative notation is absent; a limit-based representation is workable, subject to the existing binding and function-expression restrictions.
5. **Value at a point.** Put the numeral in place of the variable.
6. **A one-sided sign test.** There is no relation sign. `√(^(x,2))` equals x exactly when x ≥ 0, so a claim `r→(cƒ(✠(√(^(E,2)))),✠(E))` expresses "E is not negative" indirectly. A condition on a range of t cannot be said this way.
7. **Worked model.** The tank model V′ = 5 − 0.02·V, V(0) = 100 has V(t) = 250 − 150·e^(−t/50). In v0.1: `✠(−(250,×(150,lim(^(+(1,h),÷(−(0,÷(t,50)),h)),h,0))))`. V(10) = 250 − 150·e^(−1/5) ≈ 127.190387, written `÷(127190387,1000000)` (an approximation; the exact value is the expression). A discrete reading (2% lost at the end of each minute) gives 250 − 150·(49/50)^t and V(10) ≈ 127.44. The wording "leaks at 2% of the current volume per minute" was read as continuous by all participants in Experiment 03.

## E.5 Gaps observed with this notation (class G = reported as not sayable with v0.1 and the existing roots; A = unclear specification; OPEN / workable = representable, with limits). The classes are the authors' reports, not verified findings

| Gap | Class | Where it showed up |
|---|---|---|
| **Free-variable claims.** A claim containing a free letter ("for every t") has no stated reading. S6 gives none. | A | Experiments 02, 03 (several authors) |
| **Function definition and parameter binding.** `d≔(ρ,✠(E with free t))` names an expression; whether it makes a function of t is unsettled. A function-value form such as `V(t)` is outside v0.1 (S2, S4, S7). | A / G | Experiments 03, 04 |
| **Equations and relations.** No equation head, no relation sign, no inequality (S7). The rate law dV/dt = 5 − 0.02V as a premise for an unknown function cannot be written; only the closed form can. | G | Experiments 02, 03 |
| **Derivative.** No primitive derivative notation. A limit-based (difference-quotient) representation is workable but long, and is subject to the function-expression restriction (E.4, item 4). | OPEN / workable representation with limits. Not a class-G claim of inexpressibility | Experiments 02, 03 |
| **Units and meaning.** Nothing says that the numbers are litres or minutes, or what a variable stands for. Meaning is carried by English names or atoms. | G | Experiments 02, 03 |
| **Time scope.** How an initial value is tied to time zero (`c⊃` with a declared time name) is unresolved. | A | Experiment 03 |
| **Link between SILEX names and the letters inside `✠`.** A SILEX name (`zv`, `zt`, or an atom such as "volume-at-minute-t") and the letter used inside the marker are tied only by spelling. | G | Experiments 03, 04 |
| **Numbers and math terms inside ordinary SILEX lines.** A line such as `m>(10,✠(Σ(…)))` puts a numeral outside the marker next to a term inside it. S1 to S7 do not say whether that is permitted, and numerals outside the marker are unspecified in the lexicon (Part D, D.3 item 1). | A | Experiments 03, 04 |
| **Decimals** are a deliberate exclusion (S7); rationals work. | by design | all |

Classification rule. Free-variable quantification and function binding are specification ambiguities (A). Absent equations, units and explicit function application are more direct expressibility limits under v0.1. Always keep apart a missing convenient primitive from a representation that is truly unavailable. The exponential and the derivative of E.4 are missing primitives with workable representations.

## E.6 Proposals made so far (none adopted; all for the owner)

Attributions are as recorded by C. C checked D's entry against D's original Experiment 03 response: the wording `fn(name,parameter,expression)` and the request to clarify free variables are there, and D marks `fn` as "a proposal only". The entries for C, M and G have not been compared with the preserved original messages in this session. No review made any item adopted.

| By | Proposal | Status |
|---|---|---|
| C (Experiment 02) | An `exp(a)` head for e^a | **Withdrawn by C**: the limit form in E.4 works. C's own error. |
| C (Experiment 03) | (a) A function variable (one uppercase letter) applied as `F(a)`, and an equation head `=(a,b)`, inside the marker. (b) A rule that a free letter in a value claim ranges over all values for which both sides are defined; a claim about one value puts a numeral in its place. | CANDIDATE. Not adopted. (The proposals were written in C's earlier notation; the content is notation-level.) |
| M (Experiment 02) | A constant `e` in S2 alongside `π`; an optional unary `neg(a)` head; an equality head `=(a,b)` or assignment outside the marker; alphanumeric variable names (`x1`, `y2`) | CANDIDATE. The constant `e` is not needed (E.4.1). |
| M (Experiment 03) | A derivative head named in a proposal; `e` in S2 | CANDIDATE |
| D (Experiment 03) | A parameter-binding form `fn(name,parameter,expression)` ("a proposal only"); clarify the interpretation and domain of free variables in value claims before adding any operator | CANDIDATE |
| G (Experiment 03) | A derivative head `d/dt` (proposed with `p↗(d≔(d/dt,⌜derivative head⌝))`) | CANDIDATE |

---


# PART F. EXPERIMENTS 01 TO 04: PROTOCOLS, FINDINGS, EVIDENCE STRENGTH

## F.1 Index

The submissions, reader conditions and scoring sheets behind this index are not in this file. The summaries are C-compiled. D could not confirm the numerical performance summaries or any ranking of reader quality. Mathematical correctness and language-level interpretation are separate measurements.

| Experiment | What | Who | Result in one line | Evidence strength |
|---|---|---|---|---|
| **01**, Tests 01 to 03 | Mathematical blind interpretation: readers receive notation v0/v0.1 and one expression; they recover structure, meaning and value | D, G, M (C wrote the material) | All three recovered the intended structure, meaning and value in all three tests; no listed misreading. Test 01: nested arithmetic. Test 02: `√`, `sin`, `cos`, radians, composition order. Test 03: definite integral, non-integer value `÷(50,3)`. | **Weak for the notation.** Readers are not independent (D joined the design discussion; G's and M's session state not always recorded). The expressions have familiar shapes, so success is consistent with both "read the specification" and "recognised familiar notation". |
| **01**, Controls A and B | A: the Test 03 line with no specification (cold reader). B: the same structure with four familiar heads renamed to arbitrary tokens, with signatures supplied | Readers named by the owner | Run on 2026-10-22. The owner's view afterwards: all readers are advanced models and will manage such tests, so the next step should be model-building (R10). No comparison document exists in the project. | Not compiled here |
| **02** Build-and-report (notation only) | Write a tank model and an own-choice model using only v0.1; log problems with class G, A or E | C, M (D answered too) | Gaps found: exponential (later shown expressible by a limit), equation, units, free variable. Several "G" claims were reclassified as author errors or workable. | Single run each; C wrote the spec |
| **03** Build-and-report in SILEX | As 02 but written in SILEX itself (Part B, Part C roots plus `✠`), FALLBACK and GLOSS for English | D, G, M (C's answer used earlier-notation vocabulary and is **excluded** from comparison. That was a version-contamination failure. It is not evidence about C's mathematics or about C's ability to learn the notation) | All three produced a tank model and a Task B. D's used the limit form of the exponential, a difference-quotient check of the rate law, and a value claim with `s≈`. M used a bare `e` (undefined under S2; flagged by M itself). G's integral line had `t` absent from the integrand and `v` free, and gave no value claim. Recurring problems: function definition, free-variable claims, time scope, units, `s≈` criterion, meaning carried by names. | Single run each; different problem choices for Task B |
| **04** Cross-read | Each AI reads another's Experiment 03 SILEX with all English notes removed and reports what the SILEX alone says. C scores each reading against the author's intent and a literal parse | All four (see F.3) | See F.3 | Single run each; conditions differ |

## F.2 Protocols you can reuse

These are protocols as they were run. They do not override the owner's decisions about who takes part in which test and with what access (R3; Part G, item 13). To reuse one, the owner assigns the participants.

### F.2.1 Build-and-report in SILEX (Experiment 03 format)

- **What you use:** the SILEX you were taught (this file), and the test-only notation v0.1 inside `✠( … )`. Nothing else. Work alone. State the version you used.
- **How you answer:** in SILEX, in the message form of Part C section 3.9. English only in two places: a `FALLBACK:` line (something you could not say with the roots you know plus `✠`; a FALLBACK is recorded as a reported candidate gap, to be checked against Parts B and C before it counts as a language gap, so try existing roots first), and a `GLOSS` at the very end (a short English reading that adds no meaning the SILEX does not carry; if you need to add meaning, that is a FALLBACK).
- **Tasks:** A: the water tank (100 litres at time 0; inflow 5 litres per minute; leak at 2% of the current volume per minute; so dV/dt = 5 − 0.02·V). Write (1) the premises (rate law and initial value), (2) the volume as a function of t, (3) the volume at t = 10 as a value claim. B: a small model of your own choice that needs an equation, an inequality or a derivative; premises, then result.
- **Report, also in SILEX:** MODEL; PROBLEM LOG (where; what you wanted to say; class **G** = SILEX cannot say it, **A** = specification or language unclear, **E** = my own mistake; what you tried with existing roots and the result); SOLUTIONS (first with existing roots; only if impossible, the smallest addition, marked as a proposal, and why it is needed); CONFIDENCE (sure versus guessing).
- **Rules:** do not call something a G until you actually tried with the roots you know and with `✠`, and say what you tried. Do not invent vocabulary silently; a new symbol or rule is marked as a proposal. If everything was expressible, say so. State assumptions in SILEX if you can. Nothing is adopted; declare no milestone, freeze or revision.
- **Always pin the version** of the notation in the prompt ("SILEX = Part B and Part C of this file; no other version"). An unpinned prompt let one participant write in an earlier notation (Experiment 03, C).

### F.2.2 Cross-read (Experiment 04 format)

- **What the reader receives:** one SILEX message by another participant, stripped of everything that is not SILEX (English notes, glosses, explanations). English inside the message itself (quoted labels, `⌜…⌝` mentions, names, DATA entries) is kept. The reader is not told the subject and does not look for the original task. The reader has this file, nothing else. Work alone.
- **What the reader reports (in English):** 1 SUBJECT (what the message is about, and which parts of that come from SILEX structure versus English labels or names); 2 READING (line by line; mark each as definition, assertion, hypothesis, value claim, marked unknown, marked problem, proposal, other); 3 CLAIMS CHECK (for every value claim, equation-like claim or comparison: true **as written**? compute; if not, say what the writer may have meant, keeping the two apart); 4 PROBLEMS IN THE MESSAGE (malformed, contradictory, undeclared names; "the SILEX says X" versus "I think the writer meant Y"); 5 THE WRITER'S OWN MARKS (unknowns, problems, gaps, proposals, confidence); 6 UNKNOWN FORMS (every root or convention not known or not sure; no silent guessing); 7 CONFIDENCE.
- **Rules:** do not invent; if the message does not determine something, say it is undetermined; do not fill gaps from outside knowledge of what such a message "should" say; if you recognise the likely subject, say how, and whether the SILEX alone would have shown it.
- **Scoring (by C or the owner's scorer):** compare each reading with the author's intent and with a literal parse. Classify every discrepancy as **author error**, **reader error** or **underdetermined**. Score "disclosure of a recognised subject" separately. Check the lexicon (Part B) and the conventions (Part C) before calling a reader wrong; several apparent author errors turned out to be taught conventions.

### F.2.3 Mathematical blind interpretation (Experiment 01 format)

1. The owner records the hashes of the reader file and the private reference **before** any reader is exposed.
2. Fresh sessions only. A session that received one control or test is not reused for another. A model that took part earlier may read again only in a new chat, and the owner records that it did.
3. The reader receives exactly one reader file. Record for every reader: model and version, whether the session was new, whether memory or chat history was available, date and time, the exact file (hash), and the response as received, unchanged.
4. The reference is released only after all submissions are preserved.
5. Ask readers to write the recovered structure (heads, arguments in order, nesting) before any value, and the conventional meaning in plain text. Score **structure separately from the number**: a value can be right by luck (a reversed `^` can land near the right number).
6. For any failure, classify the reason before concluding. A failure is not proof that the notation is unusable.

### F.2.4 Guided onboarding and assessment (summary)

Teach with Part B and Part C; run three guided practice rounds with corrective feedback after each; then independent assessment with parallel forms; keys separate from questions (R3); the grader sees only a thin grading reference, never the question text. Readiness is decided by a rubric with three outcomes (READY, FURTHER PRACTICE REQUIRED, INSUFFICIENT EVIDENCE). The files for this live in the onboarding package, not in this master (Part I).

## F.3 Experiment 04: what was found (single run each; scoring against Part B and Part C)

Pairings: M read D's message; G read M's message; D read C's message (written in an earlier notation, so that pairing tests a mismatched version); C read G's message. Conditions differed between readers and **must be stated with any result**. The cross-read exposed several pitfalls (F.4). These pairings are documented observations. Reader preparation differed (a reader without the lexicon, a reader given a message in the earlier notation, others prepared differently), so no controlled ranking of SILEX comprehension follows from them. In summary:

- **Reading without the lexicon is partly possible.** C read G's message with no access to Part B or Part C (only an earlier notation and the maths spec). Of 15 unfamiliar forms (C's own tally; no second scorer), 11 were read correctly or almost, 3 partly (`g←` taken as assertion rather than "supplied"; `a?` taken as "problem" rather than "ambiguity"; `m>` argument order left undetermined), and 1 was honestly left unread (`r□`). The structure inside `✠( … )` was read with certainty. C found two real errors in G's message (the integral had no `t` in its integrand and a free `v`; an uppercase function form `V(t)` outside v0.1) and marked a third as undetermined (an inequality that, with the taught reading of `m>`, is reversed). It did not notice that `s=` was used with no criterion.
- **Why that is weak evidence for "SILEX alone carries meaning".** Most roots begin with a letter that is the first letter of the English label (Part B, "How to read this table"). A guess from shape may therefore be a guess from English. Part C section 1.1 says the letter and the English label are memory aids only.
- **Readers differ in method.** One reader looked symbols up in the table; another guessed from glyph shape. Glyph guessing produced confusions inside look-alike families (`s✓` "solution" read as verification; `s◇` "suggest" read as hypothesis; `c?` "check" read as problem). Part B section 3 exists because of this.
- **Task A's subject is not blind to anyone**, since all four wrote it. Task B is more novel to a reader, but it is not fully blind merely because the reader did not receive the author's prompt. A reader that names "water tank" from its own memory has not shown that SILEX carried it.
- **C's qualitative assessment is that the best reading came on the most English-dependent message.** The file has no common scoring table or comparable denominators, so this is not an established comparative result, and it is weak evidence for SILEX alone.
- **Corrections after the onboarding file was available.** A reader without the lexicon suspected errors that were in fact taught conventions: `d≔(zt0,t)` is the taught way to declare a time name (Part C section 0.5, 2.3); a bare `n` is a root (Part B: "new"); `m>(a,b)` reads "a exceeds b" in the taught example (Part C, C16). Always check Part B and Part C before calling a line an author error.

## F.4 Method lessons (apply them to every later test)

1. **Pin the version** of the notation in every prompt and record it with every result.
2. **Record reader state**: fresh or not, memory on or off, files received, and whether the reader has seen the subject before.
3. **Score disclosure of a recognised subject separately** from what the SILEX showed.
4. **Score structure separately from the number.**
5. **Agreement among AIs is not validation**, especially when they share an onboarding source (C wrote it).
6. **A high score on a glossary-based test shows consistent application of a glossary**, not shared meaning (Cycle 01, R02, R03).
7. **Hazard is not failure.** Binding by naming convention is a documented hazard; no misbinding has been shown to cause a wrong answer.
8. **Run a renamed-identifier control** (opaque names) before drawing conclusions about naming.
9. **Check the lexicon before blaming the author.** A discrepancy is an author error, a reader error or underdetermined; classify it before concluding.
10. **The author of a test, key or package is not an independent reader of it.** C wrote Parts B and C's source package, the maths spec, and the keys.

---


# PART G. DECISIONS WAITING FOR THE OWNER

Nothing below is decided. Each is a decision the owner holds (Rule R2).

| # | Decision | Context |
|---|---|---|
| 1 | Accept, amend or reject Snapshot 003 as the Working Master of the new line (Rule R9). D has confirmed Snapshot 002 conditionally; Snapshot 003 records D's conditions. Accepting it as a working reference is a different act from adopting vocabulary, and from Milestone 1 | Part A, Part J |
| 2 | **Numeral syntax** (digits, sign, decimals, exactness, numerals outside `✠`). It blocks every other numerical item. | D.3 item 1 |
| 3 | Whether `v=(object,attribute)` becomes a fixed-order term; the argument order of `v=` and `s≔`; the boundary between `d≔` and `s≔` | D.3 items 2, 5 |
| 4 | How units and scales are declared and scoped; when `c≠` applies to numerical lines | D.3 items 4, 7 |
| 5 | Whether embedded payloads (tables, formulas, LaTeX) are allowed, and the boundary criterion between SILEX content and payload | D.3 items 9, 10 |
| 6 | Whether the `✠` mathematical notation joins the language, once per expression or at every node; which proposals in E.6 (function terms, equation head, derivative head, free-variable reading, parameter binding) to test or adopt | Part E |
| 7 | The treatment of the open grammar items OG-01 to OG-18, starting with OG-13 (force of a bare top-level expression), OG-05/15 (criterion for `s=`), OG-03/04/14 (names across messages) | Part D |
| 8 | Assessment forms: run a fresh-reader dry run on the nine replacement items of v1.0.2, or accept the limitation in writing | Part F.2.4 |
| 9 | State how these relate: owner approval, the C and D reconciliation of the master, the four-AI no-objection step for language proposals, acceptance of a Working Master, and Milestone 1 (Rules R2, R8, R12). This is not a choice between "two AIs" and "four AIs" as if both named the same act | Part A, Part J |
| 10 | The status of the earlier exploratory fixed-structure frame ("FSF-2"), which, according to an earlier session of C, G and M were also onboarded to: treat as outside this master, or bring it in. D's caution: it belongs to the historical research record unless the owner brings a specific part into the current line, and earlier exposure does not authorise its use here | Not covered in this file |
| 11 | Clean re-runs: Experiment 03 and Experiment 04 for C in a new project holding only this file, with memory and past-chat search off, and with the version pinned. An optional method choice for C. It is not a prerequisite for D's review, and it does not mean D takes part in any blind rerun | Part F.2, F.4 |
| 12 | Milestone 1 (Rule R8): not reached; needs C and D to resolve every retained disagreement, then the owner's approval, then the Milestone 1 hash-finalization | Part A |
| 13 | D and blind tests (Rule R3): D reports a later owner instruction that D is not assigned blind tests. State its exact scope, so that the master records it accurately | R3, F.2 |
| 14 | Hash wording (Rule R8): may an ordinary SHA-256 checksum of a working snapshot be quoted for integrity before Milestone 1, while the Milestone 1 hash-finalization stays reserved? (This is D's reading; Snapshots 002 and 003 follow it as a clarification.) | R8, I.4 |
| 15 | Which primary records should be added to a later snapshot, or attached beside it, so that a participant without memory can check history (the list in I.2) | Part I.2 |
| 16 | Confirm or correct three reported rules as C recorded them: R4 (threshold and scope), R5 (the ten-exchange cadence), R9 (the fresh-pages step) | R4, R5, R9 |

---

# PART H. AUTHORING CHECKLIST

This list restates rules from Parts B to E. **It adds no new rule**, and every later snapshot must keep it so. Section numbers refer to Part C (that is, `P1`).

1. **Outermost wrapper first** (section 2.2). Put content relations inside a status marker (`g←`, `h◇`, `p◇`, `u?`). A bare content line has unspecified force (OG-13); say so if you meet one.
2. **`g←(P)` supplies P. It does not verify P** (sections 3.2, 4.1). Whether it asserts is unsettled.
3. **`d≔(name,expr)` names; it does not assert.** Declare a time name with `d≔(zt0,t)` before using it, and scope with `c⊃(zt0,…)` (sections 0.5, 2.3, 3.5).
4. **`s=` needs a criterion** declared or inherited; otherwise write `a?(s=(x,y))` and do not supply one yourself (section 3.7). There is no adopted ternary form. `s≈`, `m≡`, `d≢` have the same issue.
5. **`∧` joins propositions only** (section 3.4). Do not join directives, or a directive and a proposition. The comma separates arguments and never means AND.
6. **Argument orders are provisional and none is ratified** (section 2.7). Use them as taught, and mark `a?` for roots whose order is not taught. `m>(a,b)` is read "a exceeds b" in the taught example (C16).
7. **Names are opaque and local; their class comes from their prefix** (section 0.5). Use the declared prefixes. A prefix that is not in the table (for example `za`, which the numerical-representation cycle used for attributes) has no declared class. A name whose declaration contains quoted English is a scaffold: its class is stated in English notes, not inferred.
8. **Keep apart the four ways of saying "not there"** (section 1.4): `n¬`, `u?`, `n0`, `0`; plus non-existence needs an explicit domain, a failed search is not non-existence, and `n⊘` is "no" to a question.
9. **Do not rely on an unprefixed `k✓`.** Prefer `zkq:k✓(P)` (section 5.4).
10. **Check the look-alike families before you read a glyph** (Part B, section 3). `s✓` is "solution", not "verify"; `c?` is "check", not "problem"; `a?` is "ambiguity", not a question; `r@` is a pointer, not origin.
11. **Mention is for expressions.** `⌜x⌝` talks about x. Using it for English text or external payloads is undefined (Part D, D.3 item 9).
12. **Mathematics (TEST-ONLY).** One `✠( … )` per expression; heads and argument orders as in E.2; rationals for non-integers; no unary minus, no decimals, no relations; a value claim is `r→(cƒ(✠(E)),✠(V))`; a claim containing a free letter has no stated reading (E.5). Appearing in this checklist does not make the notation approved SILEX. It stays TEST-ONLY.
13. **Never call something a language gap until you tried to say it** with the roots you have. State what you tried.
14. **Do not adopt.** Mark proposals as proposals; leave adoption to the owner.

---

# PART I. PROVENANCE, LIMITS AND HOW TO UPDATE

## I.1 Sources of this snapshot

| Part | Source | Reproduction |
|---|---|---|
| B | Onboarding package `SILEX-ONBOARDING` v1.0.2.1, file `PARTICIPANT/P2-LEXICON-REFERENCE.md`, SHA-256 `366902b260c840b6eff03f0bcce3e698b1b74b1977f11d0da53948f95fed7c27` | Verbatim (script-embedded and checked). Heading levels lowered by one |
| C | Same package, file `PARTICIPANT/P1-LEARNING-MATERIAL.md`, SHA-256 `3ce06afd774e9bb6fa437419703bdfed0251858c77431e63c39cf3531a689f14`; sections 0.2, 0.3, 0.5, 1 to 5 | Verbatim (script-embedded and checked). Heading levels lowered by one |
| D (table) | Same package, facilitator file `F5` (Open Grammar Appendix), first three columns | Script-extracted |
| D (rest), A, F, G, H, I | Written by C from the project documents listed below and the owner's stated rules | Summaries, each marked with its status |
| E | Project documents `SILEX-MATH-EXP01-SPEC-v0.1-PROVENANCE`, `…SPEC-VERSION-RECORD`, `…ADDENDUM-T03`, `SILEX-C-MATH-NOTATION-REVIEW`, `SILEX-C-TO-D-MATH-ADDENDUM-TEST`, `SILEX-C-EXPERIMENT02…`, `…03…`, `…04…` | S1 to S7 retyped from the provenance file; the rest summarised |
| F | `SILEX-C-MATH-EXP01-TEST01/02/03-THREE-READER-COMPARISON`, the controls procedure, the experiment records, readers' messages | Summaries |
| D.3 | `SILEX-DN02-C-CRITICAL-SYNTHESIS`, `SILEX-DN03-C-CRITICAL-ASSESSMENT`, `…STAGE3-SYNTHESIS`, `…ALT-PROPOSAL-SYNTHESIS`, `…LATEX-DELIMITERS-SYNTHESIS` | Summaries of C's findings |
| J | D's review of Snapshot 001 (62 numbered points, 2026-10-22) | Summarised by C. D's own text is with the owner |

## I.2 What this file does not contain

- The 2026-10-19 checkpoint freeze and the 2026-10-20 checkpoint documents themselves, Basic Courses 01 and 02, the dialogue records (D026 to D052, C026 to C053), BT01, R02 and R03 sets, and Cycle 01 texts. They exist in the owner's portable package. Their effects are in Parts B to D.
- The onboarding package's guided practice, assessment forms and keys (`P3`, `P4`, `F1` to `F3`, `F6`), the grading reference and the reports to D.
- D's design proposals in their own words (C received DN02's proposal in full, and later ones only through summaries by G), and the full reviews by G, M and D.
- The results of Controls A and B, the readers' complete answers in Experiments 02 and 03 by D, G and M, and the record sheets of G's and M's onboarding.
- The earlier notation that predates this line, its frozen reference and its drafts. They are deliberately excluded (Rule R11).
- An authoritative statement of how owner approval, the C and D reconciliation, the four-AI no-objection step, Working Master acceptance and Milestone 1 relate (Part G, item 9). Without it, a participant without memory must not infer one.
- The primary development records needed to validate chronology, authorship and status: the 2026-10-19 and 2026-10-20 checkpoints, the dialogue messages D026 to D052 and C026 to C053, and the full DN02 and DN03 texts and reviewer responses.
- The experiment evidence needed to reproduce the findings: the complete Experiment 01 controls and comparisons, participant responses, the original messages of Experiments 02 to 04, author-intent references, scoring worksheets, exact version assignments and session-state records.
- Recovery coverage: complete argument signatures for much of the inventory, an exhaustive declaration and namespace policy, concrete handling instructions for several OPEN items, and a precise boundary between executable current conventions and illustrative scaffolding. These are omissions. They are not requests to invent anything now.
- The owner's later boundaries on who takes blind tests, and their scope (Part G, item 13).

## I.3 Known limits of this snapshot

- **C compiled it and is not independent of the material.** C wrote the onboarding package, the maths specification and most of the syntheses. Agreement among the participants who learned from that package is partly agreement with a common source.
- **Parts B and C match `P1` and `P2` verbatim only as far as C's script checked.** D accepts this as a compiler-reported correspondence, not as an independent reproduction audit.
- **Nothing in Parts B and C has been independently validated.** The lexicon of 183 entries was taken as given and was not re-audited against earlier decisions.
- **Parts E and F are single-run results** with conditions that varied.
- **D reviewed Snapshot 001 and conditionally confirmed Snapshot 002 (Part J). D has not yet seen Snapshot 003. G and M have not reviewed this file.**
- If a statement here disagrees with a document the owner holds, the owner's document and the owner's word win, and the disagreement should be recorded as a correction in the next snapshot.

## I.4 How to update (Rule R7)

1. Never edit this file in place. A change in vocabulary, grammar, convention, status label or finding produces a **new, whole, self-contained snapshot** with the next number in sequence. Keep earlier snapshots unchanged.
2. Only the owner authorises a change of vocabulary or grammar. A change of finding or wording may be proposed by any participant and is recorded in the change log below.
3. Each snapshot lists what changed since the previous one, who proposed it, and who authorised it.
4. No Milestone 1 hash-finalization and no authoritative freeze before Milestone 1 (Rule R8). Ordinary SHA-256 checksums of working snapshots may be quoted for integrity and comparison.
5. A snapshot's checksum does not make it authoritative.

## I.5 Starting prompt for a participant that has lost its memory

> You are taking part in the SILEX research project. The attached file is the SILEX Working Master. Read all of it. It is your only source on SILEX: do not use anything you remember from before. First, tell me whether you remember anything about SILEX from before, and what. Then confirm in two lines the role you have (which participant you are) and the rules you will follow (owner authority, nothing adopted by you, `a?` for anything undeclared, one notation only). Then wait for my task.

If you are asked to audit the project's history instead of learning SILEX, the primary records and the owner's word outrank this file (I.3).

## I.6 Change log

| Snapshot | Date | Changes | Authorised by |
|---|---|---|---|
| 001 | 2026-10-22 | First consolidated snapshot of the new symbolic line, compiled by C at the owner's request from the sources in I.1. No vocabulary or grammar change is made by this snapshot. | Compilation requested by the owner. **Adoption as Working Master: pending (Part G, item 1).** |
| 002 | 2026-10-22 | Applies D's review of Snapshot 001 (Part J): corrections of wording and status labels (R2, R3, R4, R5, R7, R8, R9, R10, R11, R12, A.1, A.6, D.3, E.3 to E.6, F.1 to F.3, H, I.2 to I.5); provenance and scope qualifications; new Part G items 13 to 16; new Part J. R4 now reads "above 92%" to match C's note of the owner's words. Parts B and C keep their original lexicon and grammar-teaching bodies without alteration; their explanatory introductions were updated. **No vocabulary or grammar change.** | Review by D; applied by C. No owner authorisation was needed, because no vocabulary or grammar changed. **Adoption as Working Master: pending (Part G, item 1).** |
| 003 | 2026-10-22 | Applies the six documentation corrections from D's conditional confirmation of Snapshot 002 (Part J, J.3): R7 now says "vocabulary, symbols, grammar or conventions"; the header no longer says Snapshot 002 supersedes 001 (designation is the owner's); D.3 item 10 is an analytical finding, not an OPEN item; the Parts B and C reproduction claim is precise (bodies unchanged, introductions updated); the I.4 example no longer carries a snapshot number; the Part J legend defines NOTED and PARTLY CHECKED. **No vocabulary or grammar change.** | Review by D; applied by C. No owner authorisation was needed, because no vocabulary or grammar changed. **Adoption as Working Master: pending (Part G, item 1).** |

No new root, deletion, merger, alias adoption, grammar freeze, Working Master adoption, hash-finalization or Milestone 1 completion is declared by this snapshot.


---

# PART J. RECONCILIATION WITH D'S REVIEWS (SNAPSHOT 001, THEN SNAPSHOT 002)

D reviewed the whole of Snapshot 001 on 2026-10-22 (62 numbered points; D's own text is with the owner). D's disposition: corrections and reconciliation are needed before joint confirmation; D proposes no vocabulary or grammar change; D does not yet confirm Snapshot 001 as the jointly reconciled Working Master, and asks for a Snapshot 002 that carries the factual and status corrections and keeps attribution uncertainties where primary evidence is missing. D also discloses that it remembers earlier development of SILEX, so it is not a memory-free reader, and says its recollections are not independent verification. Joint confirmation will not be adoption. The owner keeps final authority.

This Part records what Snapshot 002 did with each point (J.1 and J.2) and what Snapshot 003 did with D's review of Snapshot 002 (J.3). It adds no rule. Dispositions: **APPLIED** (text changed); **APPLIED, REPORTED** (text changed, but the point rests on D's or C's recollection of the owner's words, and the owner is asked to confirm it in Part G); **AGREED** (D agreed; no change needed); **NOTED** (recorded; no change needed); **PARTLY CHECKED** (checked against the original for some entries only); **OPEN** (stays open between C and D or for the owner).

## J.1 Disposition by point

| D point(s) | Disposition | Where in this file |
|---|---|---|
| 1 | NOTED. D's memory disclosure is recorded in A.2. | A.2 |
| 2, 49 | APPLIED. A.1 item 1 now separates learning (this file wins) from auditing history (primary records and the owner's word win). The recovery prompt carries the same line. A checksum does not make a snapshot authoritative. | A.1, I.4, I.5 |
| 3, 4, 9, 18 (count), 21, 22, 24, 25, 28, 41, 42, 44, 55, 61 | AGREED. No change except where another row says so. | |
| 5, 15, 43, 50 | APPLIED, REPORTED. The four-AI no-objection step is recorded as D's recollection. R12 is split into (a) the C and D lexicon reconciliation and (b) the four-AI proposal cycle. G.9 is reworded so that it is not a choice between "two AIs" and "four AIs". The missing governance statement is listed as a gap. | R2, R12, G.9, I.2 |
| 6, 37, 54 | APPLIED, REPORTED. R3 is limited to the specified blind-assessment procedure. D's exclusion from blind tests is recorded as D-reported. F.2 says the protocols are historical and do not override the owner's assignments. The owner is asked for the exact scope. | R3, F.2, G.13 |
| 7, 8 | APPLIED. R4 and R5 are marked as reported owner criteria with their source (C's notes of the owner's statements of 2026-10-18). R4 now reads "above 92%" to match that note; Snapshot 001 said "at least 92%". R4 is not generalised to other scoring methods. | R4, R5, G.16 |
| 10 | APPLIED. R7 covers grammar and conventions. | R7 |
| 11, 48 | APPLIED, REPORTED. R8 and I.4 now bar the Milestone 1 hash-finalization and an authoritative freeze, and allow ordinary integrity checksums. D recomputed the SHA-256 of Snapshot 001 and found the same value as C. The owner is asked to confirm this reading of "no hash before that". | R8, I.4, G.14 |
| 12 | APPLIED, REPORTED. The fresh-pages step of R9 is marked pending verification. | R9, G.16 |
| 13 | APPLIED. R10's conditions are the recorded conditions of that phase only. | R10 |
| 14 | APPLIED. The new line is a distinct branch; the earlier notation is HISTORY. C's text does not claim anything about the owner's archive. D's term "pre-root-word language" is used as D's naming. | R11, A.1, A.6 |
| 16, 17 | APPLIED. "170 historical" is explained as earlier entries of this line; "freeze" in the 2026-10-19 row is not the Milestone 1 finalisation; the history rows are C-compiled and not rechecked. | A.6 |
| 18 | APPLIED. "Entries", not "roots". D's independent count of 173 plus 10 is noted. | B intro, R11, A.5 |
| 19, 56, 58 | APPLIED. Unlabelled Part C text carries WORKING meanings and PROVISIONAL conventions together; `A:ψ` is WORKING with PROVISIONAL parsing and an OPEN boundary; observed `✠` usage is TEST-ONLY or OPEN, never WORKING by association. | Authority row, A.1, C intro, E.3 |
| 20 | APPLIED. The `a.(label)` form is a teaching convention, not evidence of a declared label. | C intro |
| 23 | APPLIED. "Numerals are the first blocker" is limited to ordinary SILEX; non-negative integers are defined inside `✠`. | D.3 item 1 |
| 26, 32, 33, 51 | APPLIED. The D.3 and E.6 attributions are marked "as recorded by C". C compared D's entry in E.6 with D's own Experiment 03 response and found it accurate. The C, M and G entries are unchecked. The primary records are listed as missing. | D.3, E.6, I.2 |
| 27 | APPLIED. Historical priority of Form A and Form B is unverified. | E.1 |
| 29, 30, 31, 59 | APPLIED. The derivative row is "OPEN / workable", not class G. The `f at t+h` placeholder is marked schematic. "Checked by C's script" is C's own check. A classification rule separates a missing convenient primitive from an unavailable representation. | E.4, E.5 |
| 34, 52 | APPLIED. F.1 states that submissions and scoring sheets are missing and that the summaries are C-compiled. The evidence needed is listed. | F.1, I.2 |
| 35 | APPLIED. C's Experiment 03 exclusion is a version-contamination failure, not evidence about ability. | F.1 |
| 36, 60 | APPLIED. A FALLBACK is a reported candidate gap until checked. | F.2.1 |
| 38, 39, 40 | APPLIED. Experiment 04 pairings are documented observations without a controlled ranking; "best reading" is C's qualitative assessment; Task B is not called fully blind. | F.3 |
| 45 | APPLIED. The clean rerun is optional, for C only, and not a prerequisite for D. | G.11 |
| 46 | APPLIED. The checklist keeps adding no rule; the `✠` item stays TEST-ONLY. | H |
| 47 | APPLIED. The verbatim match with `P1` and `P2` is compiler-reported. | I.3 |
| 53 | APPLIED. Recovery-coverage gaps are listed as omissions. Nothing is invented. | I.2 |
| 57 | APPLIED in 002; refined in 003 (J.3). Each D.3 item carries its own label; item 10 is an analytical finding, not an OPEN item. | D.3 |
| 62 (a) to (f) | See the next table. | |

## J.2 The six points D lists as outstanding between C and D

| Point | C's position | State |
|---|---|---|
| (a) Scope of the blind-test rule, and D's later exclusion | C accepts D's wording. C cannot verify the owner's later instruction and records it as D-reported. | OPEN for the owner (G.13) |
| (b) C and D master reconciliation versus four-AI proposal consensus | C accepts that these are separate decisions and has split R12. The exact present authorisation is not recorded. | OPEN for the owner (G.9) |
| (c) Ordinary hashes versus Milestone 1 hash-finalization | C accepts the narrower wording as a clarification, subject to the owner's confirmation. No hash-finalization is declared. | OPEN for the owner (G.14) |
| (d) A reported FALLBACK versus a demonstrated language gap | C agrees. Snapshot 001 worded this too strongly. | APPLIED |
| (e) Which of D's proposals E.6 attributes accurately | The `fn(name,parameter,expression)` proposal and the free-variable clarification are both in D's own Experiment 03 response. The entries for C, M and G have not been compared with their originals. | PARTLY CHECKED |
| (f) Whether C's qualitative Experiment 04 comparisons are sufficiently evidenced | C agrees they are not sufficient for any ranking. F.3 now says so. The original readings are with the owner. | APPLIED |

C found no point in D's review that it disagrees with. Where a correction depends on someone's memory of what the owner said (R2, R3, R8 clarification, R9), the text records it as reported and leaves the confirmation to the owner.

## J.3 D's review of Snapshot 002 (conditional confirmation) and Snapshot 003

D reviewed Snapshot 002 on 2026-10-22. D verified the SHA-256 (`8b983fc5f286aaf63879e5ea85c10f8d1f39229a4394cabc2621c9793ba49ee5`), compared Snapshots 001 and 002 directly, and reported: the lexicon body and the grammar-teaching body are unchanged; no earlier-notation vocabulary was found in the current lexicon or grammar. Of the 62 points, 59 were SATISFIED and 3 NOT SATISFIED; D listed 3 new documentation issues. D introduced no vocabulary, alias, operator, grammatical rule or experimental requirement. D gave a conditional C and D confirmation of Snapshot 002's substantive content as a proposed WORKING reference, on condition that the corrections below are recorded in the next snapshot. D does not authorise a snapshot to supersede another by participant declaration: the owner decides which snapshot is the current Working Master.

| D item | Correction asked | Disposition in Snapshot 003 |
|---|---|---|
| Point 10 | R7 should say "conventions" in its own enumeration, to match I.4 | APPLIED (R7) |
| Point 42 | The header must not say Snapshot 002 supersedes 001 | APPLIED. The header now says "proposed successor", with designation pending the owner |
| Point 57 | D.3 item 10 is a methodological observation, not an OPEN specification issue | APPLIED. Labelled "Analytical finding, not a language rule"; the D.3 introduction says so. No new status category |
| N1 | Parts B and C reproduction claim must be precise | APPLIED. Their lexicon and grammar-teaching bodies are unaltered; their explanatory introductions were updated (change log, A.3, B and C introductions) |
| N2 | I.4 example "Snapshot 002, …" carried over | APPLIED. I.4 says "the next number in sequence" |
| N3 | Part J legend lacked NOTED | APPLIED. The legend defines NOTED and also PARTLY CHECKED |

Remaining state, in D's words reproduced by C: content reconciliation substantially complete; owner-reserved governance questions remain open (Part G); Working Master authority pending the owner; Milestone 1 not declared; no adoption or authoritative freeze declared. D has not yet seen Snapshot 003.

---
