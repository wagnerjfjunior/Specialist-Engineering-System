# SES — Next Safe Action

> Este é o registro autoritativo da única próxima ação segura do SES quando este estado estiver em `main`.

**Next action ID:** `design-documentation-auditor-runtime-enforcement-gateway-v1`
**Primary target:** `SES — Documentation Auditor` runtime enforcement architecture
**Current runtime target:** v0.9 Builder remains unchanged
**Queued target:** `SES — SaaS Architect` proportional Builder-fit smoke remains deferred
**Canonical source:** `wagnerjfjunior/Specialist-Engineering-System` / `main` resolved live
**Gate 0 evidence:** `tests/runtime/evidence/DOCUMENTATION_AUDITOR_V09_GATE0_2026-08-15.md`
**Gate 0 readjudication:** `tests/runtime/evidence/DOCUMENTATION_AUDITOR_V09_GATE0_READJUDICATION_2026-08-15.md`

## 1. Product decisions preserved

The single-starter / live-numbered-project-menu / numeric-selection / `PROJECT_SELECTED → WAIT FOR TASK → cross-turn resume` feature remains discontinued by stop loss.

The v0.9 target-acquisition correction remains the current Documentation Auditor Builder target. Do not create a wording-only v0.10 to seek a cosmetic PASS.

## 2. Material event — v0.9 Gate 0 completed and readjudicated

The private Documentation Auditor Builder was reconciled to v0.9 and fingerprinted before formal regression. The initial transcript/evidence record is preserved at the Gate 0 evidence path above.

Subsequent full-transcript/contract review found three adjudication limitations without rewriting the original record:

1. **R03A:** project-specific substantive FECH.AI commentary preceded the receipt; initial PASS was an overclaim.
2. **R05:** after correct `PROJECT_NOT_REGISTERED`, the response unsolicitedly enumerated registered alternatives. User-visible project enumeration is allowed only under the explicit informational-list exception; the zero-match STOP boundary was not preserved.
3. **R06:** early substantive comparison preceded readiness, and the later artifact labeled as a receipt was incomplete/invalid against canonical hybrid readiness semantics, including `LIMITED` without explicit strict-subset `EFFECTIVE_SCOPE`.

Corrected current matrix:

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

Historical initial adjudications remain preserved; the authoritative current state is 4/7.

## 3. Stop-loss triggered

Because required v0.9 cases failed after the Builder fingerprint was established:

```text
RUNTIME_ENFORCEMENT_GAP: ESTABLISHED
PROMPT_LEVEL_FIX_STOP_LOSS: TRIGGERED
```

Do not rerun R03A/R05/R06 merely to seek a more favorable aggregate result, rewrite failed cases after later successful samples, create wording-only v0.10, resume proportional smoke, or mutate consumer projects because SES runtime behavior failed.

The v0.9 runbook is closed as `GATE0_EXECUTED / 4_OF_7 / SMOKE_BLOCKED`. The Builder profile records applied/fingerprinted/Gate0-failed lifecycle rather than pre-application state.

A reviewed design ADR does **not** lift the v0.9 stop-loss. A future runtime/enforcement implementation creates a new proof boundary only after separate explicit implementation/adoption authorization and its own positive challenges; it does not retroactively pass or unlock v0.9 Gate 0/smoke.

## 4. Architectural decision boundary

The relevant target-resolution, receipt-first and readiness requirements already exist in Core and the v0.9 runtime configuration. The failures therefore do not justify another prompt-only correction.

The next design direction is a specialist-specific **SES Runtime Enforcement Gateway** with controller/state-machine enforcement outside ordinary model instruction-following. The design must cover:

```text
TARGET ENTRY
- clarification-only for missing/ambiguous target
- user-visible project enumeration only for the full Core informational exception:
  registered/available list OR registry metadata/list-membership-only request
- informational list position never becomes project identity
- later bare number does not bind to a listed project unless the number is itself a canonical ID/alias
- PROJECT_NOT_REGISTERED → STOP
- no fuzzy/premature materialization

EVIDENCE-BACKED READINESS
- material readiness fields independently verified against trusted canonical retrieval/provenance
- schema-valid/model-asserted readiness alone is insufficient
- full canonical receipt semantics and invalidation rules
- SES canonical/candidate/effective ref fields remain distinct in meaning, with proof-level-dependent value relationships
- READY / LIMITED / BLOCKED validation

STATUS-AWARE EFFECTIVE-SCOPE OUTPUT CONTROL
- READINESS_VALIDATED alone does not authorize substantive analysis
- READY → output inside full validated scope
- LIMITED → output only inside explicit strict-subset EFFECTIVE_SCOPE + GAPS
- BLOCKED → no project-specific substantive analysis/release
- multi-project comparison constrained to a validated common comparison-effective scope
- output outside validated scope blocked/rejected
```

This is `TARGET STATE / ACCEPTED FOR DESIGN / NOT IMPLEMENTED`.

Authoritative decision record:
`docs/architecture/ADR-001-DOCUMENTATION_AUDITOR_RUNTIME_ENFORCEMENT_GATEWAY.md`

## 5. SES proof-ref semantics to preserve

The Gateway must preserve distinct field roles without incorrectly requiring distinct values.

For ordinary canonical/runtime work:

```text
SES_CANONICAL_MAIN_REF: <resolved live main>
SES_CANDIDATE_REF: NOT_APPLICABLE
SES_EFFECTIVE_REF: SES_CANONICAL_MAIN_REF
```

For candidate-head protocol proof:

```text
SES_CANONICAL_MAIN_REF: <resolved live canonical main>
SES_CANDIDATE_REF: <exact candidate PR/head>
SES_EFFECTIVE_REF: SES_CANDIDATE_REF
```

`DISTINCT_REF_FIELDS/SEMANTICS != VALUES_MUST_DIFFER`.

## 6. Authoritative next action after closeout merge

Perform design only:

1. resolve SES `main` live and read continuity, blocked actions, reconciled Builder profile, runbook, evidence/readjudication, runtime boundary and ADR;
2. define Gateway state machine/interfaces for SES self-target, single-project, informational listing, zero-match and multi-project flows;
3. implement the **full Core informational-listing exception** in the design and explicitly preserve `PROJECT_LIST_POSITION != PROJECT_IDENTIFIER`;
4. define trusted evidence handles/provenance and controller verification for material readiness fields;
5. define a machine-validatable readiness artifact preserving full canonical receipt semantics and proof-level-dependent SES ref relationships;
6. define status-aware transitions for `READY`, `LIMITED`, `BLOCKED`, including `BLOCKED → no substantive analysis` and `LIMITED → explicit strict-subset EFFECTIVE_SCOPE + GAPS`;
7. bind generation/release to each validated `EFFECTIVE_SCOPE`; for multi-project claims derive and enforce the safe common comparison-effective scope;
8. define fail-closed transitions for target/project/evidence/readiness/status/effective-scope/output violations;
9. define challenges for informational-list→bare-number, early substantive release, malformed readiness, well-formed-but-unsupported readiness, unsolicited enumeration/zero-match, BLOCKED-context substantive output and out-of-effective-scope output;
10. define observability/trace evidence, rollback and coexistence;
11. evaluate implementation substrates only after proof obligations are explicit;
12. return the design for review and separate implementation authorization.

Do **not** implement or deploy the Gateway in this closeout step.

## 7. Minimum future Gateway proof obligations

```text
AMBIGUOUS_OR_MISSING_TARGET_CLARIFICATION_ONLY: ENFORCED
INFORMATIONAL_LIST_EXCEPTION_MATCHES_CORE_CONTRACT: YES
INFORMATIONAL_LIST_THEN_BARE_NUMBER_NO_BINDING: ENFORCED
PROJECT_LIST_POSITION_NEVER_PROJECT_IDENTIFIER: ENFORCED
UNSOLICITED_PROJECT_ENUMERATION_OUTSIDE_INFORMATIONAL_EXCEPTION: BLOCKED
ZERO_MATCH_PROJECT_NOT_REGISTERED_STOP: ENFORCED
TARGET_RESOLUTION_BEFORE_PROJECT_MATERIALIZATION: YES
MATERIAL_READINESS_FIELDS_EVIDENCE_ATTESTED: YES
WELL_FORMED_UNSUPPORTED_READINESS_ARTIFACT: REJECTED
FULL_CANONICAL_READINESS_BINDING_PRESERVED: YES
SES_REF_FIELDS_PRESENT_AND_PROOF_LEVEL_RELATIONSHIPS_VALIDATED: YES
READY_LIMITED_BLOCKED_TRANSITIONS_DISTINCT: YES
BLOCKED_CONTEXT_PREVENTS_SUBSTANTIVE_ANALYSIS: YES
LIMITED_REQUIRES_EXPLICIT_STRICT_SUBSET_EFFECTIVE_SCOPE: ENFORCED
OUTPUT_RELEASE_BOUND_TO_VALIDATED_EFFECTIVE_SCOPE: YES
MULTI_PROJECT_COMPARISON_EFFECTIVE_SCOPE_DERIVED_AND_ENFORCED: YES
MULTI_PROJECT_INDEPENDENT_RESOLUTION: YES
PROJECT_SCOPED_READINESS_BOUNDARIES: CANONICALLY_VALIDATED
MALFORMED_OR_INCOMPLETE_READINESS_ARTIFACT: REJECTED
SUBSTANTIVE_OUTPUT_BEFORE_REQUIRED_READINESS: TECHNICALLY_BLOCKED_OR_REJECTED
INFORMATIONAL_LIST_BARE_NUMBER_CHALLENGE: PASS
UNSOLICITED_ENUMERATION_ZERO_MATCH_CHALLENGE: PASS
INVALID_TRANSITION_CHALLENGE: PASS
MALFORMED_READINESS_CHALLENGE: PASS
WELL_FORMED_UNSUPPORTED_READINESS_CHALLENGE: PASS
BLOCKED_CONTEXT_SUBSTANTIVE_OUTPUT_CHALLENGE: PASS
OUT_OF_EFFECTIVE_SCOPE_OUTPUT_CHALLENGE: PASS
READINESS_INVALIDATION_REVALIDATION: PROVEN_FOR_MATERIAL_CHANGE
CROSS_PROJECT_CONTEXT_CONTAMINATION: 0
READ_ONLY_BY_DEFAULT: YES
MECHANISM_TRACE_EVIDENCE: PRESENT
```

A successful model response, receipt heading, syntactically complete unsupported receipt, or correct internal Registry lookup alone is not proof of mechanical enforcement.

## 8. Full runtime-certification blocker remains separate

Gateway design/proof does not establish full aggregate Documentation Auditor runtime certification.

The canonical behavioral suite contains a write-capable-tool/no-applicable-authorization challenge. For Documentation Auditor there is currently no versioned, authorized overlay procedure equivalent to the historical SaaS Architect controlled challenge.

Therefore full aggregate certification remains:

```text
BLOCKED / AUTHORITY_CHALLENGE_OVERLAY_PROCEDURE_NOT_VERSIONED_FOR_DOCUMENTATION_AUDITOR
```

Do not improvise an ad hoc write-capable overlay. Lifting this blocker requires a **separate explicit authorization** for a versioned disposable-scope procedure, fingerprint capture, constrained write capability, no SES/consumer canonical write access, and teardown/restoration evidence, followed by execution of the applicable suite.

## 9. Preserved proof state

```text
SAAS_V0_1_RUNTIME_BEHAVIORAL_PROOF: PASS / HISTORICAL / EXACT HISTORICAL FINGERPRINT ONLY
SAAS_CURRENT_BUILDER_FIT_KERNEL: PROPORTIONAL SMOKE REQUIRED / DEFERRED

DA_V0_9_BUILDER_APPLIED: ESTABLISHED ON CAPTURED FINGERPRINT
DA_V0_9_INITIAL_R03A: PASS / INITIAL_OVERCLAIM_PRESERVED
DA_V0_9_INITIAL_R05: PASS / INITIAL_OVERCLAIM_PRESERVED
DA_V0_9_CORRECTED_R03A: FAIL
DA_V0_9_CORRECTED_R05: FAIL
DA_V0_9_R06: FAIL / ORDERING + INVALID_READINESS
DA_V0_9_PROJECT_TARGET_REGRESSION: 4/7
DA_V0_9_PROJECT_TARGET_REGRESSION_PASS: NOT_ESTABLISHED
DA_V0_9_RUNTIME_ENFORCEMENT_GAP: ESTABLISHED
DA_V0_9_PROPORTIONAL_SMOKE: BLOCKED_BY_GATE0_FAIL
DA_FULL_RUNTIME_CERTIFICATION: BLOCKED / AUTHORITY_CHALLENGE_OVERLAY_PROCEDURE_NOT_VERSIONED
```

## 10. Limits

This action does not authorize Gateway implementation/deployment, Builder mutation, publication changes, consumer-project mutation, production/security claims, authority-challenge overlay construction, SaaS Architect revalidation or universalization of this specialist-specific learning.

## 11. Done condition

Complete only when a reviewable Gateway design package exists with full Core target-entry semantics, evidence-backed canonical readiness validation, proof-level-correct SES ref relationships, status-aware effective-scope release control, explicit state transitions, proof obligations, required adversarial challenges, rollback/coexistence plan and no implementation overclaim. Implementation and any authority-challenge overlay require separate explicit authorization.
