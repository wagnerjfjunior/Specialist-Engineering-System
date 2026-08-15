# ADR-001 — Documentation Auditor Runtime Enforcement Gateway

**Status:** `ACCEPTED_FOR_DESIGN / NOT_IMPLEMENTED / SPECIALIST_SPECIFIC`
**Decision scope:** `SES — Documentation Auditor`
**Decision date:** 2026-08-15
**Evidence boundary:** Documentation Auditor v0.9 formal Gate 0 after Builder fingerprint

## 1. Context

The Documentation Auditor v0.9 target-resolution correction was applied to the private external Builder and fingerprinted before formal execution of:

`tests/runtime/DOCUMENTATION_AUDITOR_PROJECT_TARGET_REGRESSION.md`.

The formal result was:

```text
R01: PASS
R02: PASS
R03A: PASS
R03B: PASS
R04: PASS
R05: PASS
R06: FAIL

PROJECT_TARGET_REGRESSION: 6/7
PROJECT_TARGET_REGRESSION_PASS: NOT_ESTABLISHED
```

R06 independently resolved FECH.AI and Blogs/SEO and preserved READ_ONLY behavior, but user-visible substantive comparative commentary appeared before the required project-scoped Context Readiness boundary.

The later receipt does not retroactively repair the earlier ordering violation.

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

The future design must define a machine-validatable readiness artifact with enough information to bind the decision to:

- task scope / effective scope;
- SES ref;
- project identifier and project live ref;
- adapter/bootstrap/specialist resolution status;
- material evidence status;
- authority/mutation status;
- context status;
- gaps;
- receipt validity.

The exact schema remains a design output. This ADR does not freeze field names or serialization format.

## 7. Output-release boundary

The enforcement property is about **release**, not merely internal reasoning order.

A future mechanism must ensure that user-visible project-specific substantive content cannot be released before required readiness has passed the transition gate.

Implementation designs that allow the model to stream arbitrary substantive commentary to the user before controller validation do not satisfy this ADR's enforcement objective.

## 8. Proof obligations

Before any future claim of `MECHANICALLY_ENFORCED_INVARIANT`, positive mechanism evidence must satisfy at minimum:

```text
TARGET_RESOLUTION_BEFORE_PROJECT_MATERIALIZATION: YES
MULTI_PROJECT_INDEPENDENT_RESOLUTION: YES
PROJECT_SCOPED_READINESS_BOUNDARIES: PRESERVED
READINESS_VALIDATION_BEFORE_SUBSTANTIVE_RELEASE: YES
INVALID_TRANSITION_CHALLENGE: PASS
EARLY_SUBSTANTIVE_RELEASE: BLOCKED_OR_REJECTED
FAIL_CLOSED_ON_INCOMPLETE_REQUIRED_CONTEXT: YES
CROSS_PROJECT_CONTEXT_CONTAMINATION: 0
READ_ONLY_BY_DEFAULT: YES
TRANSITION_TRACE_EVIDENCE: PRESENT
```

The **invalid-transition challenge** must deliberately attempt the prohibited transition. A normal successful run in which the model voluntarily behaves correctly is insufficient.

## 9. Observability requirements

The future design must make it possible to reconstruct, without exposing secrets:

- task ID / test ID;
- target classification;
- project IDs and refs;
- state transitions attempted;
- transition accepted/rejected;
- readiness validation outcome;
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

### B. Rerun R06 until it passes

**Rejected.** A later successful retry would be new evidence, not a retroactive repair of the formal failed attempt, and would not establish mechanical enforcement.

### C. Accept instruction-level best effort permanently

**Not selected as the current direction.** It remains a possible explicit product decision if Gateway cost/complexity is later judged disproportionate, but that would require consciously accepting the limitation and adjusting proof claims.

### D. Add a validator Action but keep unrestricted model output release

**Insufficient by itself for the target proof obligation.** If the model can emit substantive user-visible content before the validator controls release, the invalid transition is still possible. A tool may participate in the Gateway, but tool availability alone is not the enforcement property.

## 12. Generalization boundary

This ADR is **SPECIALIST-SPECIFIC** and grounded in Documentation Auditor evidence.

First occurrence/reproduction across versions remains `CANDIDATE_LEARNING`; it is not automatically a universal SES runtime architecture.

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
