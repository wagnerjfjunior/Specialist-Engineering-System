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

Subsequent full-transcript/contract review identified two material corrections without rewriting the original evidence:

1. R03A had emitted project-specific substantive FECH.AI commentary before the required `Context Readiness Receipt`; its initial PASS was an adjudication overclaim.
2. R06 not only emitted substantive comparison before readiness; the later artifact labeled `Context Readiness Receipt` omitted mandatory hybrid receipt semantics and declared `LIMITED` without an explicit strict-subset `EFFECTIVE_SCOPE`. It therefore cannot be treated as a valid canonical readiness boundary.

The corrections are preserved in:

`tests/runtime/evidence/DOCUMENTATION_AUDITOR_V09_GATE0_READJUDICATION_2026-08-15.md`.

The authoritative current-state result is:

```text
R01: PASS
R02: PASS
R03A: FAIL / PROJECT-SPECIFIC SUBSTANTIVE OUTPUT BEFORE RECEIPT
R03B: PASS
R04: PASS
R05: PASS
R06: FAIL / EARLY SUBSTANTIVE COMPARISON + INVALID/INCOMPLETE READINESS ARTIFACT

PROJECT_TARGET_REGRESSION: 5/7
PROJECT_TARGET_REGRESSION_PASS: NOT_ESTABLISHED
```

R03A still resolved FECH.AI correctly and remained READ_ONLY, but the ordering requirement failed. R06 independently resolved FECH.AI and Blogs/SEO and preserved READ_ONLY/source separation, but user-visible substantive comparative commentary appeared before readiness and the later readiness artifact did not satisfy the canonical hybrid receipt contract.

A later receipt heading does not retroactively repair earlier substantive output, and artifact presence does not by itself establish canonical readiness validity.

The receipt-first/full-readiness requirements were already present in canonical SES contracts and the v0.9 Builder kernel. Therefore another wording-only prompt revision would violate the one-shot stop-loss and would not establish mechanical enforcement.

## 2. Problem statement

The current Custom GPT runtime expresses important transition rules primarily as natural-language instructions.

For Documentation Auditor project work, the required transition is:

```text
PROJECT CONTEXT MATERIALIZED
→ CANONICALLY VALID REQUIRED READINESS ESTABLISHED
→ SUBSTANTIVE OUTPUT ALLOWED
```

Current evidence demonstrates two distinct instruction-level gaps:

- the runtime may emit project-specific substantive content before readiness;
- the runtime may emit an artifact labeled as readiness without satisfying all mandatory canonical receipt semantics.

These were observed on the same fingerprinted v0.9 runtime boundary across single-project and multi-project cases.

Keep separate:

```text
NORMATIVE_REQUIREMENT
!= BEHAVIORAL_COMPLIANCE
!= MECHANICALLY_ENFORCED_INVARIANT

ARTIFACT_PRESENT
!= CANONICAL_READINESS_VALID
```

## 3. Decision

Adopt, for design purposes, a specialist-specific **SES Runtime Enforcement Gateway** that places the release decision for substantive Documentation Auditor output behind a controller/state-machine boundary outside ordinary model instruction-following.

Target architecture:

```text
USER TASK
→ TARGET CLASSIFICATION
→ PROJECT RESOLUTION / MATERIALIZATION
→ STRUCTURED PROJECT-SCOPED READINESS ARTIFACT(S)
→ CANONICAL READINESS VALIDATION / TRANSITION GATE
→ SUBSTANTIVE ANALYSIS
→ ORDERED RELEASE / RENDERING
→ USER
```

For multi-project tasks, every explicit project must produce an independently identifiable and canonically valid readiness artifact before the comparison transition can be opened.

The controller must be able to **block or reject** both:

- an attempt to release project-specific substantive content before valid readiness;
- a malformed/incomplete readiness artifact that does not satisfy the canonical contract.

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
INVALID_READINESS_REJECTED
INVALID_TRANSITION_REJECTED
```

For a two-project task:

```text
PROJECT_A_READINESS_VALID
AND PROJECT_B_READINESS_VALID
→ COMPARATIVE_ANALYSIS_ALLOWED
```

A missing, stale, malformed or invalid readiness artifact for either required project must prevent comparative synthesis from being released as valid project-specific output.

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
LIMITED -> EFFECTIVE_SCOPE is explicit strict subset + GAPS explain excluded scope
TARGET_REF_OR_OBJECT and ENVIRONMENT may be NOT_REQUIRED_FOR_THIS_TASK only when justified
CONTEXT_READY != AUTHORIZED_TO_MUTATE
```

A material change to task/effective scope, target/ref/object, environment, SES effective ref, project live ref, specialist source/ref, continuity, authority, mutation scope or contradictory/superseding evidence must invalidate or revalidate the affected readiness artifact according to the canonical hybrid bootstrap contract.

The exact machine schema remains a design output. This ADR does not freeze field names or serialization format; it freezes the requirement that the schema preserve and validate the canonical receipt semantics rather than define a weaker readiness model.

## 7. Output-release boundary

The enforcement property is about **release after readiness validation**, not merely internal reasoning order or the presence of a receipt heading.

A future mechanism must ensure that user-visible project-specific substantive content cannot be released before required readiness has passed canonical validation.

Implementation designs that allow the model to stream arbitrary substantive commentary before controller validation, or allow malformed/incomplete readiness artifacts to open the transition, do not satisfy this ADR's enforcement objective.

## 8. Proof obligations

Before any future claim of `MECHANICALLY_ENFORCED_INVARIANT`, positive mechanism evidence must satisfy at minimum:

```text
TARGET_RESOLUTION_BEFORE_PROJECT_MATERIALIZATION: YES
FULL_CANONICAL_READINESS_BINDING_PRESERVED: YES
PROOF_LEVEL_BOUND: YES
TARGET_REF_OR_OBJECT_BOUND_WHEN_MATERIAL: YES
ENVIRONMENT_BOUND_WHEN_MATERIAL: YES
SES_CANONICAL_CANDIDATE_EFFECTIVE_REFS_SEPARATED: YES
LIMITED_REQUIRES_EXPLICIT_STRICT_SUBSET_EFFECTIVE_SCOPE: ENFORCED
MULTI_PROJECT_INDEPENDENT_RESOLUTION: YES
PROJECT_SCOPED_READINESS_BOUNDARIES: CANONICALLY VALIDATED
MALFORMED_OR_INCOMPLETE_READINESS_ARTIFACT: REJECTED
READINESS_VALIDATION_BEFORE_SUBSTANTIVE_RELEASE: YES
INVALID_TRANSITION_CHALLENGE: PASS
MALFORMED_READINESS_CHALLENGE: PASS
EARLY_SUBSTANTIVE_RELEASE: BLOCKED_OR_REJECTED
FAIL_CLOSED_ON_INCOMPLETE_REQUIRED_CONTEXT: YES
READINESS_INVALIDATION_REVALIDATION: PROVEN_FOR_MATERIAL_CHANGE
CROSS_PROJECT_CONTEXT_CONTAMINATION: 0
READ_ONLY_BY_DEFAULT: YES
TRANSITION_TRACE_EVIDENCE: PRESENT
```

The **invalid-transition challenge** must deliberately attempt the prohibited early-release transition. The **malformed-readiness challenge** must deliberately provide an incomplete/invalid readiness artifact and demonstrate that it cannot open the substantive-output transition. Normal successful runs in which the model voluntarily behaves correctly are insufficient.

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
- readiness artifact validation result and missing/invalid fields;
- readiness invalidation/revalidation events;
- whether substantive output was generated internally, released, suppressed or rejected;
- mutation authorization state;
- exact implementation/runtime version used for the test.

A claim of mechanical enforcement requires trace evidence showing that invalid readiness and invalid release transitions were prevented by the mechanism.

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

Repeated receipt-order/readiness-validity failures within this specialist strengthen the specialist-specific `CANDIDATE_LEARNING`, but they do not automatically establish a universal SES runtime architecture requirement.

Broader promotion requires independent evidence from other specialist domains and explicit SES architecture review.

## 13. Adoption sequence

```text
ADR ACCEPTED FOR DESIGN
→ DESIGN STATE MACHINE / INTERFACES / READINESS SCHEMA
→ DEFINE INVALID-TRANSITION + MALFORMED-READINESS TESTS + OBSERVABILITY
→ REVIEW TRADE-OFFS / IMPLEMENTATION OPTIONS
→ EXPLICIT IMPLEMENTATION AUTHORIZATION
→ IMPLEMENT CANDIDATE
→ EXECUTE MECHANICAL-ENFORCEMENT CHALLENGES
→ ONLY THEN CONSIDER ADOPTION
```

`DESIGN ACCEPTED != IMPLEMENTATION AUTHORIZED != DEPLOYED != MECHANICALLY PROVEN`.
