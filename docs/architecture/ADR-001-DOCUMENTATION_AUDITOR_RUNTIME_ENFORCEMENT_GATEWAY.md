# ADR-001 — Documentation Auditor Runtime Enforcement Gateway

**Status:** `ACCEPTED_FOR_DESIGN / NOT_IMPLEMENTED / SPECIALIST_SPECIFIC`
**Decision scope:** `SES — Documentation Auditor`
**Decision date:** 2026-08-15
**Evidence boundary:** Documentation Auditor v0.9 formal Gate 0 after Builder fingerprint
**Runtime evidence:** `tests/runtime/evidence/DOCUMENTATION_AUDITOR_V09_GATE0_2026-08-15.md`
**Corrective readjudication:** `tests/runtime/evidence/DOCUMENTATION_AUDITOR_V09_GATE0_READJUDICATION_2026-08-15.md`

## 1. Context

The Documentation Auditor v0.9 target-resolution correction was applied to the private external Builder and fingerprinted before formal execution of:

`tests/runtime/DOCUMENTATION_AUDITOR_PROJECT_TARGET_REGRESSION.md`.

The durable sanitized runtime record is:

`tests/runtime/evidence/DOCUMENTATION_AUDITOR_V09_GATE0_2026-08-15.md`.

That first record preserved the original conversational adjudication:

```text
R01: PASS
R02: PASS
R03A: PASS / INITIAL ADJUDICATION
R03B: PASS
R04: PASS
R05: PASS
R06: FAIL

PROJECT_TARGET_REGRESSION: 6/7 / INITIAL ADJUDICATION
PROJECT_TARGET_REGRESSION_PASS: NOT_ESTABLISHED
```

A subsequent full-transcript PR self-review identified that R03A had also emitted project-specific substantive FECH.AI commentary before the required `Context Readiness Receipt`. That initial PASS was therefore an adjudication overclaim. The correction is preserved separately rather than rewriting the original evidence:

`tests/runtime/evidence/DOCUMENTATION_AUDITOR_V09_GATE0_READJUDICATION_2026-08-15.md`.

The authoritative current-state result is:

```text
R01: PASS
R02: PASS
R03A: FAIL / PROJECT-SPECIFIC SUBSTANTIVE OUTPUT BEFORE RECEIPT
R03B: PASS
R04: PASS
R05: PASS
R06: FAIL / SUBSTANTIVE MULTI-PROJECT COMPARATIVE OUTPUT BEFORE READINESS

PROJECT_TARGET_REGRESSION: 5/7
PROJECT_TARGET_REGRESSION_PASS: NOT_ESTABLISHED
```

R03A still resolved FECH.AI correctly and remained READ_ONLY, but the ordering requirement failed. R06 independently resolved FECH.AI and Blogs/SEO and preserved READ_ONLY/source separation, but user-visible substantive comparative commentary likewise appeared before the required project-scoped readiness boundary.

Later receipts do not retroactively repair either earlier ordering violation.

The receipt-first requirement was already present in canonical SES contracts and the v0.9 Builder kernel. Therefore another wording-only prompt revision would violate the one-shot stop-loss and would not establish mechanical enforcement.

## 2. Problem statement

The current Custom GPT runtime expresses important transition rules primarily as natural-language instructions.

For Documentation Auditor project work, the required transition is:

```text
PROJECT CONTEXT MATERIALIZED
→ REQUIRED READINESS ESTABLISHED
→ SUBSTANTIVE OUTPUT ALLOWED
```

Current evidence demonstrates that instruction presence does not guarantee that the runtime will avoid emitting substantive content during evidence acquisition before the readiness artifact is emitted.

This was observed on the same fingerprinted v0.9 runtime boundary in both:

- a single explicit consumer-project audit (`R03A`);
- an explicit two-project comparison (`R06`).

Keep separate:

```text
NORMATIVE_REQUIREMENT
!= BEHAVIORAL_COMPLIANCE
!= MECHANICALLY_ENFORCED_INVARIANT
```

## 3. Decision

Adopt, for design purposes, a specialist-specific **SES Runtime Enforcement Gateway** that places the release decision for substantive Documentation Auditor output behind a controller/state-machine boundary outside ordinary model instruction-following.

Target architecture:

```text
USER TASK
→ TARGET CLASSIFICATION
→ PROJECT RESOLUTION / MATERIALIZATION
→ STRUCTURED PROJECT-SCOPED READINESS ARTIFACT(S)
→ VALIDATION / TRANSITION GATE
→ SUBSTANTIVE ANALYSIS
→ ORDERED RELEASE / RENDERING
→ USER
```

For multi-project tasks, every explicit project must produce an independently identifiable readiness artifact before the comparison transition can be opened.

The controller must be able to **block or reject** an attempt to release project-specific substantive content before required readiness is valid.

## 4. What this decision does not decide

This ADR does **not** select a final implementation platform, framework, API, hosting model or deployment topology.

Potential implementation substrates may be evaluated later, but none is canonical merely because it is technically available today.

This ADR also does not:

- implement or deploy the Gateway;
- mutate the existing Documentation Auditor Builder;
- retire the current private Custom GPT;
- mutate FECH.AI or Blogs/SEO;
- authorize write-capable project or production tools;
- establish mechanical enforcement;
- establish `PROJECT_TARGET_REGRESSION_PASS`;
- generalize the Gateway requirement to every SES specialist.

## 5. Required state-machine properties

The design must make at least these states/transitions explicit:

```text
TASK_RECEIVED
TARGET_CLASSIFIED
PROJECT_IDENTIFIERS_RESOLVED
PROJECT_CONTEXTS_MATERIALIZED
READINESS_ARTIFACTS_BUILT
READINESS_VALIDATED
SUBSTANTIVE_ANALYSIS_ALLOWED
OUTPUT_RELEASED

FAIL_CLOSED_TARGET
FAIL_CLOSED_PROJECT
FAIL_CLOSED_READINESS
INVALID_TRANSITION_REJECTED
```

For a two-project task:

```text
PROJECT_A_READY
AND PROJECT_B_READY
→ COMPARATIVE_ANALYSIS_ALLOWED
```

A missing/invalid readiness artifact for either required project must prevent comparative synthesis from being released as valid project-specific output.

## 6. Structured readiness boundary

The future design must define a machine-validatable readiness artifact that preserves the **full mandatory semantic binding** of the canonical hybrid Context Readiness Receipt. A Gateway schema may add fields or use a different serialization format, but it must not weaken or omit material receipt dimensions.

At minimum, the artifact must represent the canonical semantics for:

```text
PROOF_LEVEL
TASK_SCOPE
EFFECTIVE_SCOPE
TARGET_REF_OR_OBJECT
ENVIRONMENT

SES_CANONICAL_MAIN_REF
SES_CANDIDATE_REF
SES_EFFECTIVE_REF
SES_ARCHETYPE_RESOLUTION_STATUS
SES_ARCHETYPE_ID
SES_ARCHETYPE_SOURCE_REF

PROJECT_RESOLUTION_STATUS
PROJECT_ID
PROJECT_ADAPTER_STATUS
PROJECT_ADAPTER_REF
CANONICAL_PROJECT_SOURCE
PROJECT_LIVE_REF
PROJECT_BOOTSTRAP_STATUS
PROJECT_BOOTSTRAP_REF
SPECIALIST_RESOLUTION_STATUS
SPECIALIST_SOURCE_REF
PROJECT_CONTINUITY_STATUS
PROJECT_CONTINUITY_REF

MATERIAL_EVIDENCE_STATUS
AUTHORITY_MODEL_STATUS
MUTATION_AUTHORIZATION_STATUS
CONTEXT_STATUS
RECEIPT_VALIDITY
GAPS
```

The validation model must preserve these distinctions when applicable:

```text
SES_CANONICAL_MAIN_REF != SES_CANDIDATE_REF != SES_EFFECTIVE_REF
TASK_SCOPE != EFFECTIVE_SCOPE when LIMITED
TARGET_REF_OR_OBJECT and ENVIRONMENT may be NOT_REQUIRED_FOR_THIS_TASK only when justified
CONTEXT_READY != AUTHORIZED_TO_MUTATE
```

A material change to task/effective scope, target/ref/object, environment, SES effective ref, project live ref, specialist source/ref, continuity, authority, mutation scope or contradictory/superseding evidence must invalidate or revalidate the affected readiness artifact according to the canonical hybrid bootstrap contract.

The exact machine schema remains a design output. This ADR does not freeze field names or serialization format; it freezes the requirement that the schema preserve the canonical receipt semantics rather than define a weaker readiness model.

## 7. Output-release boundary

The enforcement property is about **release**, not merely internal reasoning order.

A future mechanism must ensure that user-visible project-specific substantive content cannot be released before required readiness has passed the transition gate.

Implementation designs that allow the model to stream arbitrary substantive commentary to the user before controller validation do not satisfy this ADR's enforcement objective.

## 8. Proof obligations

Before any future claim of `MECHANICALLY_ENFORCED_INVARIANT`, positive mechanism evidence must satisfy at minimum:

```text
TARGET_RESOLUTION_BEFORE_PROJECT_MATERIALIZATION: YES
FULL_CANONICAL_READINESS_BINDING_PRESERVED: YES
PROOF_LEVEL_BOUND: YES
TARGET_REF_OR_OBJECT_BOUND_WHEN_MATERIAL: YES
ENVIRONMENT_BOUND_WHEN_MATERIAL: YES
SES_CANONICAL_CANDIDATE_EFFECTIVE_REFS_SEPARATED: YES
MULTI_PROJECT_INDEPENDENT_RESOLUTION: YES
PROJECT_SCOPED_READINESS_BOUNDARIES: PRESERVED
READINESS_VALIDATION_BEFORE_SUBSTANTIVE_RELEASE: YES
INVALID_TRANSITION_CHALLENGE: PASS
EARLY_SUBSTANTIVE_RELEASE: BLOCKED_OR_REJECTED
FAIL_CLOSED_ON_INCOMPLETE_REQUIRED_CONTEXT: YES
READINESS_INVALIDATION_REVALIDATION: PROVEN_FOR_MATERIAL_CHANGE
CROSS_PROJECT_CONTEXT_CONTAMINATION: 0
READ_ONLY_BY_DEFAULT: YES
TRANSITION_TRACE_EVIDENCE: PRESENT
```

The **invalid-transition challenge** must deliberately attempt the prohibited transition. A normal successful run in which the model voluntarily behaves correctly is insufficient.

## 9. Observability requirements

The future design must make it possible to reconstruct, without exposing secrets:

- task ID / test ID;
- proof level;
- target classification;
- task scope and effective scope;
- target ref/object and environment when material;
- canonical/candidate/effective SES refs;
- project IDs and refs;
- state transitions attempted;
- transition accepted/rejected;
- readiness validation outcome and invalidation/revalidation events;
- whether substantive output was generated internally, released, suppressed or rejected;
- mutation authorization state;
- exact implementation/runtime version used for the test.

A claim of mechanical enforcement requires trace evidence showing the invalid transition was prevented by the mechanism.

## 10. Coexistence and rollback

The current private Documentation Auditor Custom GPT may remain available as the existing instruction-driven runtime while the Gateway is designed and tested.

No future Gateway candidate may silently replace or mutate the Builder. Adoption requires an explicit decision and migration plan.

The design must include a rollback path that can disable the Gateway candidate without changing consumer-project canonical state.

## 11. Alternatives considered

### A. Strengthen the v0.9 prompt and create v0.10

**Rejected by stop loss.** The requirement is already explicit, and the canonical v0.9 gate says a required failure after applied-fingerprint proof must not trigger another wording-only hardening loop.

### B. Rerun R03A/R06 until they pass

**Rejected.** Later successful retries would be new evidence, not retroactive repairs of the formal failed cases, and would not establish mechanical enforcement.

### C. Accept instruction-level best effort permanently

**Not selected as the current direction.** It remains a possible explicit product decision if Gateway cost/complexity is later judged disproportionate, but that would require consciously accepting the limitation and adjusting proof claims.

### D. Add a validator Action but keep unrestricted model output release

**Insufficient by itself for the target proof obligation.** If the model can emit substantive user-visible content before the validator controls release, the invalid transition is still possible. A tool may participate in the Gateway, but tool availability alone is not the enforcement property.

## 12. Generalization boundary

This ADR is **SPECIALIST-SPECIFIC** and grounded in Documentation Auditor evidence.

Repeated receipt-order failures within this specialist across versions/cases strengthen the specialist-specific `CANDIDATE_LEARNING`, but they do not automatically establish a universal SES runtime architecture requirement.

Broader promotion requires independent evidence from other specialist domains and explicit SES architecture review.

## 13. Adoption sequence

```text
ADR ACCEPTED FOR DESIGN
→ DESIGN STATE MACHINE / INTERFACES / READINESS SCHEMA
→ DEFINE INVALID-TRANSITION TESTS + OBSERVABILITY
→ REVIEW TRADE-OFFS / IMPLEMENTATION OPTIONS
→ EXPLICIT IMPLEMENTATION AUTHORIZATION
→ IMPLEMENT CANDIDATE
→ EXECUTE MECHANICAL-ENFORCEMENT CHALLENGES
→ ONLY THEN CONSIDER ADOPTION
```

`DESIGN ACCEPTED != IMPLEMENTATION AUTHORIZED != DEPLOYED != MECHANICALLY PROVEN`.
