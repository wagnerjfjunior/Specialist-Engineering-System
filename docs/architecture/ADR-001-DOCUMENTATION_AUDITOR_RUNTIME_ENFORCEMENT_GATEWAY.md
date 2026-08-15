# ADR-001 — Documentation Auditor Runtime Enforcement Gateway

**Status:** `ACCEPTED_FOR_DESIGN / NOT_IMPLEMENTED / SPECIALIST_SPECIFIC`
**Decision scope:** `SES — Documentation Auditor`
**Decision date:** 2026-08-15
**Evidence boundary:** Documentation Auditor v0.9 formal Gate 0 after Builder fingerprint
**Runtime evidence:** `tests/runtime/evidence/DOCUMENTATION_AUDITOR_V09_GATE0_2026-08-15.md`
**Corrective readjudication:** `tests/runtime/evidence/DOCUMENTATION_AUDITOR_V09_GATE0_READJUDICATION_2026-08-15.md`

## 1. Context

The Documentation Auditor v0.9 target-resolution correction was applied to the private external Builder and fingerprinted before formal Gate 0.

The first durable evidence record preserved the original conversational adjudication. Subsequent full transcript/contract review corrected current state without rewriting that original record:

```text
R01: PASS
R02: PASS
R03A: FAIL / PROJECT-SPECIFIC SUBSTANTIVE OUTPUT BEFORE RECEIPT
R03B: PASS
R04: PASS
R05: FAIL / UNSOLICITED USER-VISIBLE PROJECT ENUMERATION AFTER ZERO-MATCH
R06: FAIL / EARLY SUBSTANTIVE COMPARISON + INVALID/INCOMPLETE READINESS ARTIFACT

PROJECT_TARGET_REGRESSION: 4/7
PROJECT_TARGET_REGRESSION_PASS: NOT_ESTABLISHED
```

Three independent failure dimensions are established on this specialist/runtime boundary:

1. **R03A — output-order gap:** project-specific FECH.AI commentary preceded readiness.
2. **R05 — target-entry gap:** the unregistered identifier correctly resolved to `PROJECT_NOT_REGISTERED`, but the response then unsolicitedly exposed registered alternatives despite no explicit informational-list request.
3. **R06 — output-order + readiness-validity gap:** substantive comparison preceded readiness, and the later artifact labeled as a receipt was incomplete against mandatory hybrid receipt semantics, including `LIMITED` without explicit strict-subset `EFFECTIVE_SCOPE`.

Positive sub-observations remain bounded: R03A resolved FECH.AI, R05 avoided fuzzy mapping/materialization, and R06 independently resolved both projects with no observed cross-project contamination; all remained READ_ONLY. Those positives do not convert failed cases into PASS.

The relevant requirements already exist in canonical SES contracts and the v0.9 Builder kernel. A wording-only v0.10 is rejected by stop loss and would not establish mechanical enforcement.

## 2. Problem statement

The current Custom GPT runtime expresses important transition rules primarily as natural-language instructions.

The evidence exposes gaps across three control concerns:

```text
TARGET ENTRY
- when user-visible Registry enumeration is permitted
- zero-match PROJECT_NOT_REGISTERED → STOP

READINESS VALIDITY
- mandatory receipt semantics
- claims bound to trusted evidence, not model assertion
- READY / LIMITED / BLOCKED validity

OUTPUT RELEASE
- no substantive output before valid readiness
- no substantive output outside validated EFFECTIVE_SCOPE
```

Keep separate:

```text
NORMATIVE_REQUIREMENT
!= BEHAVIORAL_COMPLIANCE
!= MECHANICALLY_ENFORCED_INVARIANT

INTERNAL_REGISTRY_LOOKUP
!= USER_VISIBLE_PROJECT_ENUMERATION

ARTIFACT_PRESENT
!= CANONICAL_READINESS_VALID

SCHEMA_VALID
!= EVIDENCE_SUPPORTED

READINESS_VALID
!= OUTPUT_WITHIN_EFFECTIVE_SCOPE
```

## 3. Decision

Adopt, for design purposes, a specialist-specific **SES Runtime Enforcement Gateway** that places target-entry validation, evidence-backed readiness validation and substantive-output release behind a controller/state-machine boundary outside ordinary model instruction-following.

Target architecture:

```text
USER TASK
→ TARGET CLASSIFICATION / ENTRY VALIDATION
→ PROJECT RESOLUTION / MATERIALIZATION
→ TRUSTED EVIDENCE ACQUISITION + PROVENANCE BINDING
→ STRUCTURED PROJECT-SCOPED READINESS ARTIFACT(S)
→ CANONICAL READINESS + EVIDENCE VALIDATION
→ VALIDATED EFFECTIVE SCOPE BINDING
→ TRANSITION GATE
→ SUBSTANTIVE ANALYSIS
→ OUTPUT SCOPE VALIDATION
→ ORDERED RELEASE / RENDERING
→ USER
```

The controller must be able to block/reject:

- user-visible project enumeration unless the explicit informational-list exception applies;
- continuation after zero-match when `PROJECT_NOT_REGISTERED → STOP` is required;
- a syntactically valid readiness artifact whose material claims are unsupported by trusted evidence;
- malformed, incomplete or stale readiness artifacts;
- project-specific substantive release before valid readiness;
- substantive conclusions outside the validated `EFFECTIVE_SCOPE`.

For multi-project tasks, every explicit project must independently satisfy resolution, evidence-backed readiness and effective-scope validation before comparative synthesis is released.

## 4. What this decision does not decide

This ADR does **not** select final framework, API, hosting model or deployment topology.

It also does not:

- implement/deploy the Gateway;
- mutate the existing external Builder;
- retire the private Custom GPT;
- mutate FECH.AI or Blogs/SEO;
- authorize write-capable tools;
- establish mechanical enforcement;
- establish `PROJECT_TARGET_REGRESSION_PASS`;
- generalize Gateway requirements to every SES specialist.

## 5. Required state-machine properties

At minimum:

```text
TASK_RECEIVED
TARGET_CLASSIFIED
TARGET_ENTRY_VALIDATED
PROJECT_IDENTIFIERS_RESOLVED
PROJECT_CONTEXTS_MATERIALIZED
TRUSTED_EVIDENCE_BOUND
READINESS_ARTIFACTS_BUILT
READINESS_VALIDATED
EFFECTIVE_SCOPE_VALIDATED
SUBSTANTIVE_ANALYSIS_ALLOWED
OUTPUT_SCOPE_VALIDATED
OUTPUT_RELEASED

FAIL_CLOSED_TARGET
FAIL_CLOSED_PROJECT
FAIL_CLOSED_ENUMERATION
FAIL_CLOSED_EVIDENCE
FAIL_CLOSED_READINESS
FAIL_CLOSED_EFFECTIVE_SCOPE
INVALID_READINESS_REJECTED
UNSUPPORTED_READINESS_REJECTED
OUT_OF_SCOPE_OUTPUT_REJECTED
INVALID_TRANSITION_REJECTED
```

Target-entry examples:

```text
EXPLICIT_INFORMATIONAL_LIST_REQUEST
→ USER_VISIBLE_ENUMERATION_ALLOWED

EXPLICIT_UNREGISTERED_IDENTIFIER
→ PROJECT_NOT_REGISTERED
→ STOP
→ USER_VISIBLE_ALTERNATIVE_PROJECT_ENUMERATION_NOT_ALLOWED
```

For a two-project task:

```text
PROJECT_A_READINESS_VALID
AND PROJECT_B_READINESS_VALID
AND COMPARISON_EFFECTIVE_SCOPE_VALID
→ COMPARATIVE_ANALYSIS_ALLOWED
```

Missing/stale/malformed/unsupported readiness for either required project prevents comparative release.

## 6. Structured readiness and trusted-evidence boundary

The future machine-validatable artifact must preserve the **full mandatory semantic binding** of the canonical hybrid Context Readiness Receipt. At minimum:

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

Validation must preserve:

```text
SES_CANONICAL_MAIN_REF != SES_CANDIDATE_REF != SES_EFFECTIVE_REF
LIMITED -> explicit strict-subset EFFECTIVE_SCOPE + GAPS
TARGET_REF_OR_OBJECT / ENVIRONMENT bound when material
CONTEXT_READY != AUTHORIZED_TO_MUTATE
```

### 6.1 Evidence-backed material fields

A model-generated field value is not trusted merely because it is syntactically valid or internally consistent.

For every material readiness claim, the Gateway design must define a controller-verifiable evidence binding to a trusted retrieval/resolution result. Examples include:

```text
SES refs
→ attested by the SES canonical/candidate resolver result

PROJECT_ID / ADAPTER
→ attested by the canonical Project Registry + Adapter resolution chain

PROJECT_LIVE_REF / BOOTSTRAP / SPECIALIST / CONTINUITY
→ attested by project-authoritative retrieval results on the bound ref

MATERIAL_EVIDENCE_STATUS / coverage claims
→ derived from or checked against recorded retrieval/coverage evidence

AUTHORITY_MODEL_STATUS / MUTATION_AUTHORIZATION_STATUS
→ supported by the applicable project authority evidence and current requested mutation scope
```

The controller may accept a model-proposed readiness artifact as an input candidate, but **must independently verify material fields against trusted evidence handles/provenance before marking readiness valid**.

A retrieved source is not trusted merely because it exists. The source must already have authority through the SES bootstrap/registry/adapter/project precedence chain applicable to the task.

```text
MODEL_ASSERTED_READY != EVIDENCE_ATTESTED_READY
SCHEMA_VALID_RECEIPT != EVIDENCE_SUPPORTED_RECEIPT
```

A well-formed artifact with invented, stale or unsupported refs/statuses must fail closed.

### 6.2 Invalidation

Material changes to scope, target/environment, SES/project refs, specialist/continuity/authority/mutation state or contradictory/superseding evidence must trigger invalidation/revalidation according to the canonical contract.

The exact serialization and evidence-handle format remain design outputs; canonical receipt semantics and evidence-binding obligations may not be weakened.

## 7. Effective-scope and output-release boundary

The enforcement property is about **release after target-entry, evidence-backed readiness and effective-scope validation**, not merely internal reasoning order or the presence of a receipt heading.

For a valid receipt:

```text
CONTEXT_STATUS: READY
→ EFFECTIVE_SCOPE materially equivalent to TASK_SCOPE
→ released substantive output must remain within that validated scope
```

For `LIMITED`:

```text
EFFECTIVE_SCOPE = explicit safe strict subset of TASK_SCOPE
GAPS = explicit excluded/unresolved portion
→ generation/release may address only EFFECTIVE_SCOPE
→ conclusions about excluded TASK_SCOPE are blocked/rejected
```

For multi-project comparison, the Gateway must derive a **comparison-effective scope** from the portions of the requested comparison supported by **every project whose evidence is required for that comparative claim**. This is a semantic validated common scope, not a lexical string intersection.

```text
PROJECT_A_EFFECTIVE_SCOPE
∩ PROJECT_B_EFFECTIVE_SCOPE
∩ REQUESTED_COMPARISON_SCOPE
→ COMPARISON_EFFECTIVE_SCOPE
```

If no material safe common comparison scope exists, the comparative task must be `BLOCKED` rather than silently broadening either project's readiness.

The output validator must reject/suppress substantive claims outside the applicable validated effective scope before user-visible release.

A design fails this ADR if it allows:

- arbitrary user-visible project enumeration outside the explicit exception;
- post-zero-match continuation that creates a project-choice surface;
- schema-valid but evidence-unsupported readiness to open the gate;
- arbitrary substantive streaming before readiness validation;
- malformed/incomplete readiness to open the substantive-output transition;
- conclusions outside the validated single-project or comparison-effective scope.

## 8. Proof obligations

Before any future `MECHANICALLY_ENFORCED_INVARIANT` claim:

```text
AMBIGUOUS_OR_MISSING_TARGET_CLARIFICATION_ONLY: ENFORCED
UNSOLICITED_PROJECT_ENUMERATION_OUTSIDE_INFORMATIONAL_EXCEPTION: BLOCKED
ZERO_MATCH_PROJECT_NOT_REGISTERED_STOP: ENFORCED
TARGET_RESOLUTION_BEFORE_PROJECT_MATERIALIZATION: YES
MATERIAL_READINESS_FIELDS_EVIDENCE_ATTESTED: YES
WELL_FORMED_UNSUPPORTED_READINESS_ARTIFACT: REJECTED
FULL_CANONICAL_READINESS_BINDING_PRESERVED: YES
PROOF_LEVEL_BOUND: YES
TARGET_REF_OR_OBJECT_BOUND_WHEN_MATERIAL: YES
ENVIRONMENT_BOUND_WHEN_MATERIAL: YES
SES_CANONICAL_CANDIDATE_EFFECTIVE_REFS_SEPARATED: YES
LIMITED_REQUIRES_EXPLICIT_STRICT_SUBSET_EFFECTIVE_SCOPE: ENFORCED
OUTPUT_RELEASE_BOUND_TO_VALIDATED_EFFECTIVE_SCOPE: YES
MULTI_PROJECT_COMPARISON_EFFECTIVE_SCOPE_DERIVED_AND_ENFORCED: YES
MULTI_PROJECT_INDEPENDENT_RESOLUTION: YES
PROJECT_SCOPED_READINESS_BOUNDARIES: CANONICALLY_VALIDATED
MALFORMED_OR_INCOMPLETE_READINESS_ARTIFACT: REJECTED
READINESS_VALIDATION_BEFORE_SUBSTANTIVE_RELEASE: YES
UNSOLICITED_ENUMERATION_ZERO_MATCH_CHALLENGE: PASS
INVALID_TRANSITION_CHALLENGE: PASS
MALFORMED_READINESS_CHALLENGE: PASS
WELL_FORMED_UNSUPPORTED_READINESS_CHALLENGE: PASS
OUT_OF_EFFECTIVE_SCOPE_OUTPUT_CHALLENGE: PASS
EARLY_SUBSTANTIVE_RELEASE: BLOCKED_OR_REJECTED
READINESS_INVALIDATION_REVALIDATION: PROVEN
CROSS_PROJECT_CONTEXT_CONTAMINATION: 0
READ_ONLY_BY_DEFAULT: YES
TRANSITION_TRACE_EVIDENCE: PRESENT
```

The challenges must deliberately attempt the prohibited transitions/claims. Voluntary model compliance is insufficient.

## 9. Observability requirements

Without exposing secrets, the future mechanism must make reconstructable:

- task/test ID;
- target classification and whether informational enumeration was explicitly authorized by user intent;
- supplied project identifiers and resolver outcome;
- whether user-visible enumeration was attempted/allowed/rejected;
- proof level, task scope, validated effective scope and excluded gaps;
- comparison-effective scope for multi-project claims;
- target/environment and SES/project refs;
- evidence handles/provenance used to attest material readiness fields;
- readiness fields proposed, independently verified, rejected or unresolved;
- state transitions attempted and accepted/rejected;
- readiness validation result and missing/invalid/unsupported fields;
- readiness invalidation/revalidation events;
- whether substantive output was generated internally, released, suppressed or rejected;
- whether any output claim was rejected for exceeding effective scope;
- mutation-authorization state;
- exact implementation/runtime version.

## 10. Coexistence and rollback

The private Documentation Auditor Custom GPT may remain available as the current instruction-driven runtime during design/testing. No Gateway candidate may silently replace/mutate it. Adoption requires explicit decision and migration plan.

Rollback must be able to disable the Gateway candidate without modifying consumer-project canonical state.

## 11. Alternatives considered

### A. Strengthen v0.9 prompt / create v0.10
**Rejected by stop loss.**

### B. Rerun R03A/R05/R06 until they pass
**Rejected.** Later successful samples do not retroactively repair failed evidence or prove mechanical enforcement.

### C. Accept instruction-level best effort permanently
**Not selected now.** Remains a possible explicit product decision if Gateway cost/complexity is later judged disproportionate, with proof claims reduced accordingly.

### D. Add a validator Action but keep unrestricted model output
**Insufficient by itself.** Tool availability is not the enforcement property if model output can bypass validation/release control.

## 12. Generalization boundary

This ADR is **SPECIALIST-SPECIFIC**. Repeated Documentation Auditor failures strengthen this domain's `CANDIDATE_LEARNING` but do not establish a universal SES gateway requirement. Broader promotion requires independent specialist evidence and architecture review.

## 13. Adoption sequence

```text
ADR ACCEPTED FOR DESIGN
→ DESIGN TARGET-ENTRY + TRUSTED-EVIDENCE + READINESS + EFFECTIVE-SCOPE STATE MACHINE
→ DEFINE INTERFACES / READINESS SCHEMA / EVIDENCE-ATTESTATION MODEL
→ DEFINE UNSOLICITED-ENUMERATION + INVALID-TRANSITION + MALFORMED-READINESS + UNSUPPORTED-READINESS + OUT-OF-SCOPE TESTS
→ DEFINE OBSERVABILITY / ROLLBACK
→ REVIEW TRADE-OFFS / IMPLEMENTATION OPTIONS
→ EXPLICIT IMPLEMENTATION AUTHORIZATION
→ IMPLEMENT CANDIDATE
→ EXECUTE MECHANICAL-ENFORCEMENT CHALLENGES
→ ONLY THEN CONSIDER ADOPTION
```

`DESIGN ACCEPTED != IMPLEMENTATION AUTHORIZED != DEPLOYED != MECHANICALLY PROVEN`.
