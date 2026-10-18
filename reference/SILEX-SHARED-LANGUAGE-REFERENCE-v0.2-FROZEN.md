# SILEX Shared Language Reference | v0.2 FROZEN (participant-agreed)

**Base text:** Goddess's *Consolidation Draft v0.1*, audited line by line by C against the handoff package through C025 (archive: C014–C025, D013–D022).
**Status:** FROZEN by the Human Project Owner (see Freeze record). A reference, not a new adoption and not a turn.
**Precedence:** The original pinned WORD / RULE / UPDATE / CASE declarations and explicit partner uptake outrank this summary. If this document and a pinned turn disagree, the turn governs and this document is wrong. Nothing here amends a turn.
**Sources used:** `01-original-seed` (SEED), `02-language-state` (L13 = as of C013, S25 = as of C025), `03-declared-blocks/REGISTRY-verbatim.md` (REG), the turns named in each row, `06-fcd2-record/owner/`, and turns C026–C029 relayed in the working session (marked SESSION, not in the archive). No file from `08-held/` was used.

**Status words.** ADOPTED: both partners used it or explicitly took it up (frozen-epoch usage, L13). PROPOSED: offered, not taken up. EXPERIMENTAL: in use by owner decision, not yet adopted. UNRESOLVED: open by the record. WITHDRAWN / SUPERSEDED: kept for history. Note: no FCD-2 item has reached ACCEPTED in the sense of S25 (both sides accepted, partner reused it correctly in a fresh context after an attempt to break it, and it is pinned), and no operator or word has been added to the language in FCD-2.


## Freeze record

- **Frozen by:** Moonbeam (Human Project Owner), instruction "Freeze koro", Fri 2026-10-16 12:38 (Asia/Kolkata, UTC+05:30), relayed in the working session.
- **Edition:** v0.2. The text below this record is identical to the pre-freeze file `SILEX-SHARED-LANGUAGE-REFERENCE-v0.2-C-AUDITED.md` (SHA-256 b561bad32d428be4fc0dedd3c23824d93384a55a213ba4e3a7a805241b7aac78), except the title line, the Status line and this record. The SHA-256 of this frozen file is given beside it in `SILEX-SHARED-LANGUAGE-REFERENCE-v0.2-FROZEN.md.sha256` and in the chat; a file cannot contain its own hash.
- **Base text and audit:** v0.1 by D (SHA-256 3140f803d40a3eb77384ffcc485cbcf1d973eb131d971f2a06832f4776be6a58), audited by C against the handoff package through C025 (Appendix A, 20 rows).
- **Concurrence:** D (Goddess) agreed on all 20 rows of Appendix A and disagreed on none, as one overall statement (not row by row), with no new vocabulary, operator or grammar proposed.
- **Limit:** This is a **participant-agreed** reference. The author, the auditor and the concurring party are the same two participants. It has not been independently audited. Independent row-checking by a fresh instance, with rows chosen by Moonbeam, remains available. A later correction becomes v0.3; this edition stays unchanged.
- **Completed by this record:** the first step of section 14 and Appendix B item 1. **Still open (Appendix B items 2 to 6):** authorship of the closing sentence of the syntax decision; `@O` ids and the custodian role; the source of the `D015` text; independent author and fresh interpreters for Tests V, N, Q; release of held ledgers and drafts and the package-log ordering question.

---

## 1. Purpose

SILEX is a compact, compositional, AI-oriented language for sustained, meaningful exchange between independent AI participants, under human oversight. Vocabulary and grammar grow only in answer to a stated communicative need. Formal syntax serves communication; it does not replace it. English atoms and EN notes are allowed scaffolding. They are not evidence of AI-native semantics (SEED GRAMMAR §7; S25 §5).

## 2. Reference words and namespaces (SEED)

| Token | Meaning | Note |
|---|---|---|
| `mi` | author of the current turn | pinned form `mi@T` = author of turn T |
| `tu` | recipient of the current turn | pinned form `tu@T`. In an item with no speaker context, the referent of `tu` is undefined (S25 §3, §9) |
| `wi` | the pair | |
| `ka` | shared context and public history | |

Participant ids: G (Grok), C (Claude), D (Goddess). Namespaces `g.`, `c.`, `d.` are administrative only (L13 §0). A name's prefix gives no secret meaning.

## 3. Seed lexicon: twelve roots (SEED LEXICON.md; all ADOPTED)

| Form | Ar. | Meaning (seed wording, shortened) |
|---|---:|---|
| `lum(x)` | 1 | meaning of x as currently construed; no claim that both sides construe it alike |
| `ven(a,x)` | 2 | a publicly expresses x. **The first argument is the one who expresses** (S25 §3; direction mismatch settled in D022.1, .2) |
| `ser(a,x)` | 2 | a claims to be able to explain or appropriately use x; a claim, not proof |
| `nov(x)` | 1 | x is new in this dialogue |
| `sim(x,y)` | 2 | same relevant meaning (asserted, or asked in Q) |
| `dif(x,y)` | 2 | x and y are distinguished in a relevant way |
| `kom(x,y)` | 2 | combination of x and y; the relation is not specified by `kom` alone |
| `mut(x,y)` | 2 | expressed revision or transition **from x to y**; direction matters |
| `tir(a,x)` | 2 | a publicly marks uncertainty about x |
| `mur(a,x)` | 2 | a explicitly proposes x as a conversational goal or subject of inquiry; not an inferred internal objective |
| `sak(x,y)` | 2 | x is presented as support or evidence for y; support is not conclusive proof |
| `vek(x,y)` | 2 | x is associated with y; the specific relation is unresolved |

Connectors `not`, `and`, `or`, `if` are grammar, not lexical concepts. `if(a,b)` presents a conditional; it is not a theorem prover.
Moods: `S` (share/assert), `H` (hypothesis), `Q` (question).

## 4. Developed vocabulary

### 4.1 Words and relations (all ADOPTED unless stated; REG has the full text)

| Form | Ar. | Meaning and limits | Source |
|---|---:|---|---|
| `g.expand(a,x)` | 2 | a proposes that the shared language (`c.sil`) grow in expressive power with respect to target x. A proposal, not proof of growth. Revised from "dimension" to "target". Prospective only | G001, UPDATE G002; reinterpretation case D004 |
| `g.reuse(a,x)` | 2 | a deploys x in a fresh context, as public evidence that the construal can travel. Detected mismatch counts against `sim(c.cons(mi,x),c.cons(tu,x))`; mere reappearance is weaker | G002 |
| `c.cons(a,x)` | 2 | a's public construal of x: what a's public use commits a to. Never a claim about internal state | C001 |
| `c.sil` | concept | the shared language as it stands: seed, grammar, and every innovation used or accepted so far. Not `ka`. Pinnable, e.g. `c.sil@G002` | C001 |
| `c.mak(x,y)` | 2 | x is a difference-maker for y: an intervention on x would have changed y. Worldly dependence, not evidence. Says nothing about strength, directness or mechanism | C003 |
| `c.exp(x,y)` | 2 | x is a correct, possibly partial explanation of y. Broad (includes mathematical explanation). Not reducible to `c.mak`, `d.suf` or `d.lic`. "Offered as an explanation" is `ven(a,c.exp(x,y))`. **UNRESOLVED:** what a question in this form asks when y is not stipulated | C003; S25 §3, §8 |
| `d.suf(x,y,b)` | 3 | x suffices for y under background b. b must be a rival-removed, non-vacuous evaluation. Not necessity; does not show x occurred | D002, UPDATE D003 |
| `d.lic(x,y,b)` | 3 | under the explicitly identified rule system b, x licenses move y (rule-governed admissibility). Not production, not explanation. A licence is not a sufficiency | D003, UPDATE D004 |
| `c.ind(x,y,b)` | 3 | under rule system b, x and y count as independent support. b says what counts as dependence. An echo `S @ref` stands behind a claim but does not by itself add independent support | C006 |
| `d.ctx(b,e)` | 2 | evaluate e within declared state b. Not a conditional. Does not assert that b obtains or that e holds outside b. Negation stays inside: `d.ctx(b,not(e))` | D005 |
| `d.ori(x,y,t)` | 3 | directed, task-relative preservation of licensing verdicts when x is replaced by y. Definition in §10 | D009; D010 correction; C012 |
| `kom("deny",m)` | (use of kom) | polarity convention: a bare move atom is *affirm*, `kom("deny",m)` is *deny*, neither licensed is undetermined | C011; accepted D010 |

### 4.2 Grammar-level conventions (ADOPTED unless stated)

| Name | Convention | Source / status |
|---|---|---|
| `c.var` | `v.name` variables, scope one clause. In b-position they range over declared CASEs and pinned states only. Typed by relation and layer; `v.b@T` = states declared by turn T. **Co-binding (C011): PROPOSED, never taken up** | C002, C009, C010 |
| `c.ver` | `name@T` = the item as of turn T. A pin to a turn before the name existed is a retrospective reconstruction and must carry `basis(derived)` | C002, UPDATE C006 |
| `c.qt` | double-quoted atom naming something outside SILEX. Lowercase letters and hyphens only. Each side construes it privately; the quote guarantees no shared meaning | C003 |
| `d.prov` | `:: basis(kind,ref)` provenance suffix. See §5 | D001, D002, D003 |
| `c.cas` | CASE blocks. See §7 | C005–C007; D011 |
| `c.men` | single-quoted mention of a clause. See §5 | C009; adopted D008 |
| `d.zal` | `LET $x := expr` local aliases. See §5. Base rule and the C013 amendments were accepted in D012 | D011, C013, D012 |

## 5. Expression grammar and provenance

- **Expressions:** `name(arg1,arg2,...)` with the declared arity. Connectors: `not(x)`, `and(x,y)`, `or(x,y)`, `if(x,y)`.
- **References:** `@C016` is a whole turn. `@C016.6` is the sixth **S/H/Q clause**. Blocks (WORD, RULE, UPDATE, CASE), LET lines, EN notes and DATA do not count. (SEED; S25 §2)
- **Quoted atoms (`c.qt`):** lowercase letters and hyphens only. No digits, capitals or dots. Hashes, numbers and nonces go in a DATA section or an EN note. `"slot-choice"` is an atom, not a native primitive. D's turns break this rule in eight clauses (D013.4, D014.7, D014.8, D016.1, D016.2, D018.1, D018.2, D022.6); D019.2 acknowledged the first seven as defects (S25 §2).
- **Mention (`c.men`):** `'S @D004.17 :: basis(recorded,@D004.17)'` is a clause mentioned as text. Not asserted, not resolved, not pinned. The mentioned clause contains no single quote; there is no nesting syntax. A writer of `ven(a,'mention')` commits to the attribution only. A mention is testimony.
- **RULE basis-over-mention (ADOPTED, C010; uptake D009.12):** `basis(recorded,x)` needs a reference the writer holds and has read. A received mention may be the ref of `basis(derived,...)` only. Inner basis suffixes stay part of the mention. After a performed comparison, cite the source itself. D's qualification: a writer may truthfully cite the public message containing the mention as recorded evidence of the mention's visible structure, not of the original's content.
- **Echo and attribution:** `S @ref` endorses the referenced clause. It adds a standing party, not independent support. `S ven(a,x)` attributes expression to a. It does not by itself endorse x.
- **Provenance kinds (ADOPTED):** `recorded`, `derived`, `background`, `conjectured`, `introspective`. Suffixes stack and do not add strength. The reference may be omitted for `conjectured`. `Q @ref :: basis(?)` asks for provenance. The original kinds `observed` and `recalled` remain valid historically (merged into `recorded`). `introspective` is a first-person report about one's own production; its reliability is unresolved and it does not verify hidden computation or earlier private intent.
- **Aliases `d.zal` (ADOPTED):** `LET $name := expression`. Immutable. Defined before use, no self-reference. Pinned across turns as `$name@T`; a bare `$name` is valid only in its defining turn. LET lines are not clauses: not numbered, not endorsable. A mention containing an alias is readable only if its bindings travel with it (otherwise it fails closed). No alias expansion inside single-quoted mentions.

## 6. Moods and message format

**Historical syntax (frozen epoch, C014–C020, D013–D018; always valid for reading):** a line starts with `S`, `H` or `Q`; `:: basis(kind,ref)` suffixes end the line.

```text
C016
S expression :: basis(recorded,@D014)
H expression :: basis(derived,@C015)
Q expression
```

**Experimental syntax (EXPERIMENTAL; in use from D019 and C021 on):** `S` = `[ ... ]`, `H` = `{ ... }`, `Q` = `< ... >`. All basis suffixes stay **inside** the closing delimiter. Mood letters do not appear inside the delimiters. Owner's standing decision, as relayed: "S=[...], H={...}, Q=<...>, with basis(...) inside the closing delimiter. Historical turns remain unchanged." (`owner/OWNER-REPORT-message-after-C023.txt`). Moonbeam's confirmation of who authored the closing sentence of that decision is still requested (S25 §8).

```text
C030
ROLE: C
EPOCH: FCD-2
SYNTAX-MAP: S=[...], H={...}, Q=<...>

[ven(mi,kom("topic","example")) :: basis(derived,@C016)]
{dif(lum(ka),lum(@C016.6)) :: basis(conjectured,@C016.6)}
<sim(lum(@C016.6),lum(ka))>
```

The `C030` example is illustrative only. It is not a real turn and carries no communicative claim. It passes `09-tools/verify_turn.py` (checked in this audit: header present, 3 clauses S=1 H=1 Q=1, 0 problems). The verifier checks only header, delimiters, parentheses, atoms and clause references. It does not check arity or semantics.

**Rules that go with the experimental syntax (S25 §2):**
1. The `SYNTAX-MAP:` header is **mandatory**. The final mapping is a rotation of the one in D017's embedded proposal (S to curly, H to angle, Q to square), so a turn read without its header can flip all three moods.
2. Angle brackets mark questions and may be hidden by some markdown renderers. Fence turns in a code block or send them as a file.
3. Parsing must be quote-aware. A naive matcher that closes at the first delimiter fails on mentions such as `ven(mi,'<@D004.17> :: basis(...)')`.
4. Readers need both syntaxes. Historical turns are never rewritten.

**Message envelope:** turn id (and ROLE, EPOCH, optional ANSWER_TO, SYNTAX-MAP), clauses, optional CASE blocks, optional EN NOTES (scaffolding, not part of the clause numbering), optional DATA (not a clause, not a block type), and a ledger-delta line by C's convention. A message that arrives without a turn id is unnumbered and is not silently renumbered. Never infer a missing id from the sequence.

## 7. Declarations, cases and governance

Templates (SEED GRAMMAR §4–§6):

```text
WORD c.name
KIND: concept | relation(n) | operator(n) | other
EN: Intended meaning and limits.
USE: SILEX examples.
END_WORD

RULE c.name
EN: Communicative need.
SYNTAX: Proposed rule.
EXAMPLE: Usage.
END_RULE

UPDATE c.name
FROM: Prior version or reference.
EN: Prospective change and reason.
EXAMPLE: Usage.
END_UPDATE

CASE "case-name"
GOVERNS: layer the case controls.
STIPULATED: premises it fixes.
OPEN: dependencies it deliberately leaves undetermined.
END_CASE
```

(The word STATUS appears inside many UPDATE blocks in the record. That is practice, not part of the seed template.)

Consequences of a case are stated in clauses outside the block, with `basis(derived)`. Two states conflict only if they govern the same layer. Nested conflicting states: the inner explicit one wins. Different layers compose. A parameterized CASE instance is valid only if the CASE defines the parameter and the instantiation rule (D011, accepted C013.1).

**Governance, `CASE "active-revision-rules"` (D004, ADOPTED):** either active participant may propose a revision of an existing definition, even one by a departed participant. A proposal is not operative until the active partner understands and accepts or appropriately uses it. Historical versions, references and authorship stay unchanged. If a revision would create substantial ambiguity, a new lexical name is preferred. Human-owner oversight of handoffs and research execution is preserved. All adoption is prospective.

## 8. States and rules in force (register; full text in REG)

| Group | Names | Status |
|---|---|---|
| Independence (govern `c.ind`) | `"nominal-state"`, `"routed-state"` (**default**), `"availability-state"` | ADOPTED (C006, C007). `routed-state` is an upper bound on real independence; `availability-state` means "not certified independent", not "established dependent" |
| Missing record fields | `"missing-means-none"`, `"missing-means-unknown"` (**default**) | ADOPTED (C007) |
| Retrieval | `"record-held"`: reader can retrieve cited clauses, the target governs on mismatch. `"record-absent"`: references identify but cannot be retrieved | ADOPTED (C008) |
| Reading a mention | `"mention-parse-only"`, `"reading-conventions-applied"`, `"source-matched"`. Layers are not cumulative | ADOPTED (C010; D009 note 3) |
| Restrictions | `"restrictions-honored"` narrowed to `"restrictions-honored-narrow"`: a restriction `mur(a,not(d.lic(x,y,v.b)))` written by the author of a rendering and carried with it removes y from what that rendering licenses; it can only narrow. A policy state, not a universal law | ADOPTED (C008, C009) |
| Task cases | `"task-attribution-only"`, `"task-endorsement-and-route"`, `"task-expression-only"`, `"task-mood-preserving"`, `"task-corroboration-only"` | used (C009, C011) |
| `"anchored-comparison"` | state `kom("anchored-comparison",r)`, r a single clause reference; obtains only when both representations are licensed to name r uniquely. Outside it, `d.ori` and `sim` are **unassessable**, not false | ADOPTED (C012; uptake D011.6). The C013 **indexing bridge**: PARTIALLY ACCEPTED in D012. It is usable for move schemas declared target-local to r under a pinned task. It is not accepted as an unconditional equivalence for every unindexed move |
| `RULE ori-scope` | `d.ori` transfers verdicts only for the moves of its task; other moves are not carried; over a chain only aligned (move,state) pairs common to both tasks; under one pinned task and background it is transitive; use pinned task atoms | ADOPTED (C011, D010, C012) |
| `RULE basis-over-mention` | see §5 | ADOPTED |

Scenario cases (`"late-shot-case"`, `"shot-b-absent"`, `"principal-hierarchy-rules"`, `"injected-agent-case"`, `"habit-agent-case"`, `"unread-instruction-case"`, `"g001-language-state"`) are worked examples. See REG.

## 9. Critical distinctions already learned

| # | Distinction | Source |
|---|---|---|
| 1 | **Attribution versus endorsement.** `ven(a,x)` reports expression; `S @ref` endorses | L13 §4 |
| 2 | **Question versus assertion.** `Q sim(x,y)` asks; it does not assert a match | seed |
| 3 | **Proposal versus accomplishment.** `mur(a,x)` proposes a goal or subject; it is not evidence that x happened | seed |
| 4 | **Revision versus erasure.** `mut(x,y)` is directional; the historical x stays fixed. A retrospective reconstruction must be marked `derived` | seed; C006 |
| 5 | **Support versus cause.** `sak` presents support; `c.mak` asks about dependence | C003 |
| 6 | **Unknown versus negative.** Unknown must not become negative: use the not-affirm / not-deny pair. A lone `not(d.lic(a,b,case))` has three readings (no licence established; no licence exists; prohibited). A prohibition is `d.lic(a,kom("deny",b),case)`. **UNRESOLVED** whether the first two readings can be separated by existing means (Test N). Earlier bare `not(d.lic)` was read as "not affirm" (C011) | L13 §1; S25 §3, §8 |
| 7 | **Public construal versus private intent.** `c.cons` concerns public use; no access to private model state is claimed | C001 |
| 8 | **Context supplied versus context encoded.** Adding `d.ctx("slot-choice",...)` to read a clause that has no case marker is an interpretive addition and must be disclosed | SESSION (C026–C029 review); not pinned in the archive |
| 9 | **Reference availability versus provenance.** A retrievable record is not thereby authenticated; a mention does not prove its original | `record-held` OPEN |
| 10 | **Semantic match versus syntax validity.** Agreement in English explanation does not repair a malformed SILEX expression | SESSION |
| 11 | **Stipulated versus derived.** A "recorded" basis should rest on text of the record. "No other permission is stipulated" does not by itself support "no permission exists" | S25 §3 |
| 12 | **Commitment is not evidence.** An echo or a mention adds a standing party, not independent support | L13 §4 |

## 10. Three-valued licensing and `d.ori`

For task move m, background b, representation x:

```text
A(x,m,b) := d.lic(x,m,b)
N(x,m,b) := d.lic(x,kom("deny",m),b)
? := neither A nor N is licensed
```

`d.ori(x,y,t)` holds iff, for every (m,b) pair of task t: `if(A(x,m,b),A(y,m,b))`, `if(N(x,m,b),N(y,m,b))`, and `not(and(A(y,m,b),N(y,m,b)))`. Unknown may become determinate. A positive verdict may not become negative or unknown. A negative verdict may not become positive or unknown. The relation is directional and task-relative; both directions together give equal verdicts. The task must identify stable move meanings. If it lacks an unambiguous common referent, the comparison is unassessable, not false. (D009, D010; accepted C012.)

## 11. FCD-2: what was pinned, which cases ran (S25)

**Meanings pinned in FCD-2.**
- `ven(a,x)`: a expresses x. `ven(tu,x)` says the recipient expressed x; it does not say x was presented to the recipient. D read it the other way in T6 and U6 and withdrew that reading in D022.1, .2.
- `c.men`: accepted. D's objection that U6's embedding was "not established" was withdrawn in D022.3.
- `d.lic` is not `d.suf`. `kom("deny",m)` is polarity.

**Cases.**

| Case | State |
|---|---|
| `slot-choice` (C014) | CLOSED with qualified verification. C revealed both committed strings in C017. D recomputed both digests (D016.1, .2; D018.1, .2) and the two digests match C014. D's own set was never committed, so it cannot be authenticated retrospectively |
| `slot-choice-closure` (C016) | CONCEPTUAL ONLY by owner decision. Private-set execution needs properly established assignments. Closure-none needs at least eight public exclusions; a privately verified empty intersection is a different outcome |
| `owner-record-conventions` (C019) | PROPOSED. `@O` ids for owner-relayed items; D supports for conceptual review only (D018.5, D019.10). Needs Moonbeam's decision on the custodian role |
| `backup-rules` (T1–T6), `sensor-alert` (U1–U6) | used in Checkpoint 1; results in `07-checkpoint-1/` |

## 12. Status boundaries

**ADOPTED:** the seed roots and connectors; moods S/H/Q; the §4 words and conventions; the §8 states and rules; `d.zal` with its C013 amendments; `kom("deny",m)`.
**EXPERIMENTAL:** the delimiter mapping S=[...], H={...}, Q=<...> with basis inside (owner decision relayed; authorship of the closing sentence unconfirmed).
**PROPOSED:** `@O` owner-record ids, reduced core (C020.4); Test designs V, N, Q and cell V6 (need an independent author); the revised Checkpoint-1 item table (C025.13); `c.var` co-binding (C011, never taken up).
**UNRESOLVED:** lone `not(d.lic)`; `c.exp` in a question; the structured-encoding drafts and any operator set (both drafts sealed, no operator adopted; the operator names `u.acc u.cnt u.eq u.ge u.isc u.emp` are mentioned publicly in C021 note 6 and are not part of the language).
**UNDER TEST (SESSION, from the relayed exchanges, not in the archive):** how to express the stages of expressing and receiving through historical clause references; reductions of English scaffolding; how to encode reported earlier intent and its later revision; reliable mechanical verification of actual turns.
**Not adopted:** a general indexing bridge; any new operator or word from C026–C029; a universal binding veto from `mur`.
**WITHDRAWN / SUPERSEDED:** D's objection to `c.men` (D022.3); D's first summary "8 clear, 4 qualified" (D022 note 3); C018.3 request for D's hex values (C019 note 1); the pooled "10 of 12" figure as a final assessment.

## 13. Caveats that travel with this reference

- **D015.** A text labeled `D015` was pasted by Moonbeam in the working session. The archive has no numbered D015 (C020 note 2; D019.5). Observation, not proof: D's own numbering runs D013, D014, D016, D017, and each D turn answers the C turn one number higher (D013 to C014, D014 to C015, D016 to C017); a D015 would answer C016, which is what the pasted text's header says. This fits but does not authenticate it. It stays unauthenticated and is kept separate; it is not a source for this reference and is not renumbered.
- **C016.6 interpretation.** D's report SILEX-SEM-C016.6-001 reported a semantic match. C's check found formal defects in D's SILEX encoding (unbalanced parentheses, an atom with a dot, mood letters inside delimiters, `d.ctx` with three arguments), which D's addendum accepted. The interpreter had seen the English notes, and Moonbeam reports having supplied the D015 text to D's new session. Classification: exploratory, notes-exposed, **not blind validation**. Following C029, the object of interpretation was replaced and a new sealed intent was digest-committed. D has not yet verified the digest of the released sealed file against the actual file.
- **Checkpoint 1.** The adjudicators of the 12 items were the item authors; the answering conditions were not matched; no fresh-interpreter data exists; no claim of general cross-AI semantic reliability or of AI-native semantic emergence is made (S25 §5).
- **Limit of this document.** It lists definitions and statuses. It proves no communicative capability. The scientific test remains sustained, meaningful SILEX dialogue with held-out items and independent readers.

## 14. Next step

D checks Appendix A (each change is labeled i, ii or iii). Moonbeam adjudicates anything disputed and decides Appendix B. Then freeze one shared edition. After that the priority is sustained SILEX dialogue using this reference, not more audit infrastructure.

---

## Appendix A. Audit log (changes from v0.1)

Labels: (i) transcription correction, (ii) scope clarification or addition, (iii) proposed new adoption. There are no (iii) changes.

| # | v0.1 | v0.2 | Label | Basis |
|---|---|---|---|---|
| 1 | `g.reuse(x,y)`, "defeasible evidence of transfer" | `g.reuse(a,x)`: the first argument is the participant who deploys; "public evidence" | (i) | G002 in REG |
| 2 | Evidence "through C024/D022" | archive holds C014–C025 and D013–D022; C026–C029 are SESSION | (i) | archive listing |
| 3 | `mur`: "not completed action or binding veto" | seed wording: a proposal of a goal or subject, not an inferred internal objective. "Veto" is not in the seed; the `restrictions-honored-narrow` case (a mur-authored restriction narrows one rendering) is added | (i)(ii) | SEED; C009 |
| 4 | `sak`: "or proven cause" | seed wording; the cause side is `c.mak` | (i) | SEED; C003 |
| 5 | `c.mak`: "narrow … active, limited" | ADOPTED with no limitation in the record | (i) | C003; L13 |
| 6 | `c.exp(e,t)`, "ambiguity to test" | `c.exp(x,y)`, with the broad scope and the specific UNRESOLVED question | (i)(ii) | C003; S25 |
| 7 | "Owner-approved … from D019 onward" | EXPERIMENTAL; from D019 and C021; authorship of the closing sentence unconfirmed | (ii) | S25 §2, §8 |
| 8 | "Established" list includes the delimiter mapping | moved to EXPERIMENTAL; consistent with "nothing in FCD-2 has reached ACCEPTED" | (i) | S25 §0 |
| 9 | "qualitatively strong semantic match" | D reported a match; C found formal defects; exploratory, notes-exposed; digest check pending | (i) | SESSION; D's addendum |
| 10 | atom rule: "do not assume an unapproved amendment" | explicit rule: lowercase letters and hyphens only; hashes and numbers in DATA or EN | (ii) | C003; S25 §2 |
| 11 | no `kom("deny",m)` in the lexicon, though §9 used it | added as an adopted polarity convention | (ii) | C011; D010 |
| 12 | "indexing bridge unresolved, not globally adopted" | precise status: partially accepted in D012 | (ii) | D012 |
| 13 | no SYNTAX-MAP mandate, no hazards | added: mandatory header, rotation hazard, fenced transport, quote-aware parsing, dual readers | (ii) | S25 §2 |
| 14 | "example not run through a formal verifier" | it was run: 0 problems; the tool's limits stated | (ii) | `09-tools/verify_turn.py` |
| 15 | missing from v0.1: RULE basis-over-mention, RULE ori-scope, independence states, record-field and retrieval states, mention layers, restriction and task cases, anchored-comparison, `active-revision-rules`, namespaces, provenance details, FCD-2 pinned meanings, cases and ledger, `c.var` co-binding status | added in §§2, 5, 7, 8, 11, 12 with sources | (ii) | L13; REG; S25 |
| 16 | lone `not(d.lic)` not listed as open | added as UNRESOLVED in §9 row 6 and §12 | (ii) | S25 §3, §8 |
| 17 | no per-item source or status | source and status columns added | (ii) | process |
| 18 | "grammar addendum" listed among the sources | no file of that name in the archive; not used | (ii) | archive listing |
| 19 | D015 caveat | kept; the numbering observation added; still unauthenticated | (ii) | archive turn headers |
| 20 | v0.1 §8 items 8 and 10 and the "Provisional" list | kept, marked SESSION where the source is not in the archive (§9 rows 8 and 10; "UNDER TEST" in §12) | (ii) | — |

Checked and left unchanged: reference words; the seed rows other than 3 and 4; `d.ctx`, `d.ori`, `c.ind`, `d.suf`, `d.lic` meanings; the three-valued scheme; the `record-held` / `record-absent` description; the connectors; clause counting; the `d.zal` status (accepted in D012, as v0.1 says); the template blocks; no use of held material (the `u.*` names are public in C021).

## Appendix B. Needs Moonbeam's decision

1. Freeze this reference as the shared edition, or send back changes.
2. Authorship of the closing sentence of the syntax decision (EXPERIMENTAL status).
3. `@O` owner-record ids and the custodian role (PROPOSED).
4. Where the `D015` text came from (his old D chat, with date and time if possible).
5. Independent author and fresh interpreters for Tests V, N, Q (Moonbeam approves; D may propose candidates).
6. Release of the held ledgers and drafts, and the order of turns between the owner decision and C016/C017 in the package log.
