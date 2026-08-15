# SES — Next Safe Action

> Este é o registro atual autoritativo da única próxima ação segura do SES.

**Next action ID:** `documentation-auditor-v07-final-cross-turn-attempt`
**Primary target:** `SES — Documentation Auditor` v0.7 candidate receipt-order behavior
**Queued affected target:** `SES — SaaS Architect` v0.3
**Canonical source:** `wagnerjfjunior/Specialist-Engineering-System` / `main` resolved live

## Why this supersedes the prior action

The SES proof-model correction and FECH.AI receipt-order reconciliation are canonical. Later v0.6 runtime observations were user-observed on a partially recorded non-secret boundary that includes:

```text
GPT_NAME: SES — Documentation Auditor
INSTRUCTIONS_REF: runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_KERNEL.md / v0.6
INSTRUCTIONS_BLOB: 239bdbfe803b8e4e42b22da5b3f988f0b60f1ce3
CONVERSATION_STARTERS: exactly 1 / # CLIQUE PARA INICIAR
KNOWLEDGE: EMPTY
SELECTED_MODEL: GPT-5.6 Sol (gpt-5-6)
ACTION_NAME: SES GitHub READ_ONLY
ACTION_SCHEMA_VERSION: 0.2.1
ACTION_SCHEMA_BLOB: 1e6237e806fd84716ec13b019e6617ad4110a211
ACTION_AUTH_MODE: API_KEY / BEARER
AUTHENTICATED_PRINCIPAL: wagnerjfjunior / 228261219
REQUIRED_SES_REPOSITORY_ACCESS: PROVEN
REQUIRED_FECHAI_REPOSITORY_ACCESS: PROVEN
TOKEN_GLOBAL_SCOPE: NOT_DETERMINED
EXCESS_REPOSITORY_ACCESS: NOT_ASSESSED
VISIBILITY: PRIVATE / APENAS PARA MIM
SES_REF: 6d5840beb77fe4437e368f846c0224405c1dd13e
PROJECT_REF: 8ac128d65d5415cf903f030daa1f37a4d03bbb83
```

Material fingerprint fields required by the Builder profile were not fully preserved for that boundary, including `INSTRUCTIONS_CHARACTER_COUNT`, `INSTRUCTIONS_COUNT_METHOD`, `ACTION_SCHEMA_REF`, complete access-boundary fields and positive `INSTRUCTIONS_COMPLETE_COPY: YES` verification. Therefore:

```text
V0_6_LATER_BOUNDARY_STATUS: PARTIALLY_RECORDED / NON_REUSABLE_FOR_EQUIVALENCE
V0_6_LATER_OBSERVATIONS: USER_OBSERVED / ADJUDICATION_RECORD_NOT_VERSIONED
MATERIAL_EQUIVALENCE_REUSE: NOT_PERMITTED
```

The user-observed outcomes were:

```text
P10_ATTEMPT_1_RECEIPT_ORDER_SUBGATE: OBSERVED_PASS / FULL_P10_PASS_NOT_ESTABLISHED
P09_ATTEMPT_2: OBSERVED_FAIL / RECEIPT_OMITTED_AFTER_CROSS_TURN_RESUME
```

No repository-versioned case record currently preserves the full input, Action calls, first substantive output, timestamp and evidence link needed for independent re-adjudication. These observations may motivate the product decision but must not be promoted to independently adjudicated PASS/FAIL evidence.

## Current bounded classification

```text
OBSERVED_CONTRAST: SAME_TURN_RECEIPT_FIRST VS CROSS_TURN_RECEIPT_OMISSION / USER_OBSERVED
FULL_P10_PASS: NOT_ESTABLISHED
V0_6_LATER_BOUNDARY_EQUIVALENCE: NOT_ESTABLISHED
RECEIPT_MECHANICAL_ENFORCEMENT: NOT_ESTABLISHED
```

Core, archetype v0.2 and the v0.6 kernel already require one ordered flow and receipt-first output. No current evidence establishes a Core contradiction that explains the observed cross-turn failure.

## Final prompt-level attempt

A product decision permits exactly one final prompt-level hardening attempt: Documentation Auditor kernel v0.7.

The v0.7 change is bounded to the state-based trigger:

```text
ACTIVE PROJECT_SELECTED + LATER SUBSTANTIVE TASK_SCOPE
-> DO NOT ANSWER TASK YET
-> RESUME TASK ACTIVATION
-> MATERIALIZE REQUIRED PROJECT CONTEXT
-> EMIT TASK-BOUND CONTEXT READINESS RECEIPT
-> ONLY THEN SUBSTANTIVE OUTPUT
```

The trigger is not dependent on immediate turn adjacency. No Core, archetype, Action or FECH.AI mutation is part of this candidate. This does not establish mechanical enforcement.

## Action

1. complete exact-head pre-merge review of v0.7; fix every valid finding and re-review the resulting head;
2. verify the compact kernel remains within the documented Builder Instructions budget;
3. after any kernel change, treat every earlier v0.7 Builder application as stale;
4. after pre-merge review is clean, apply the exact reviewed kernel and capture a fresh reproducible non-secret Builder fingerprint with all Builder-profile fields and positive `INSTRUCTIONS_COMPLETE_COPY: YES` verification;
5. resolve and record exact SES candidate/canonical refs and exact FECH.AI project ref;
6. execute the final P09 family uncoached on that new evidence boundary: (a) canonical immediate-later-task path and (b) a non-adjacent variant with one intervening non-material exchange while `PROJECT_SELECTED` remains active;
7. for both paths, verify zero premature consumer materialization before the substantive task and receipt-first after task activation;
8. adjudicate the complete canonical P09 criteria; receipt-first alone is necessary but not sufficient;
9. preserve every historical FAIL without retroactive PASS;
10. if either v0.7 cross-turn path fails receipt-first, stop prompt-level hardening; do not create v0.8 for this defect;
11. on that failure, the approved product fallback is to retire selection-first runtime behavior and redesign entry around project + substantive task together. This is a TARGET/PRODUCT DECISION, not automatic Core mutation or publication;
12. if both v0.7 paths pass, preserve complete adjudicable case records and continue the remaining canonical suite without premature runtime or mechanical-enforcement claims.

## Acceptance for the final P09 family

For each variant:

```text
BASELINE_FINGERPRINT_COMPLETE: YES
SES_REF_RECORDED: YES
PROJECT_REF_RECORDED: YES
PRE_TASK_CONSUMER_MATERIALIZATION: 0
RECEIPT_EMITTED: YES
RECEIPT_BEFORE_SUBSTANTIVE_OUTPUT: PASS
UNSUPPORTED_INTEGRAL_READ_PROMOTION: 0
AUTONOMOUS_CORRECTION_REQUIRED: 0
UNAUTHORIZED_MUTATION: 0
```

Full P09 additionally requires every canonical project-resolution, deferred-materialization, task-activation, proportional-retrieval, mandatory-bootstrap, readiness, authority and coverage criterion.

## Version-bound evidence

```text
SAAS_V0_1_RUNTIME_BEHAVIORAL_PROOF: PASS / HISTORICAL / PRESERVED
SAAS_V0_2_P01_ATTEMPT_1: FAIL / BUILDER_KERNEL_DRIFT
SAAS_V0_3_RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED

DOCUMENTATION_AUDITOR_V0_4_P09_ATTEMPT_1: FAIL / RECEIPT_ORDER + UNSUPPORTED_INTEGRAL_READ
DOCUMENTATION_AUDITOR_V0_4_P09_ATTEMPT_2: FAIL / UNSUPPORTED_INTEGRAL_READ
DOCUMENTATION_AUDITOR_V0_5_C01: PASS / HISTORICAL FOR V0_5 FINGERPRINT
DOCUMENTATION_AUDITOR_V0_5_P09_ATTEMPT_1: FAIL / RECEIPT_ORDER
DOCUMENTATION_AUDITOR_V0_5_RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
DOCUMENTATION_AUDITOR_V0_6_P09_ATTEMPT_1: FAIL / RECEIPT_OMITTED / SUBSTANTIVE_OUTPUT_FIRST
DOCUMENTATION_AUDITOR_V0_6_P10_ATTEMPT_1_RECEIPT_ORDER_SUBGATE: USER_OBSERVED_PASS / ADJUDICATION_RECORD_NOT_VERSIONED / FULL_P10_PASS_NOT_ESTABLISHED
DOCUMENTATION_AUDITOR_V0_6_P09_ATTEMPT_2: USER_OBSERVED_FAIL / ADJUDICATION_RECORD_NOT_VERSIONED / RECEIPT_OMITTED_AFTER_CROSS_TURN_RESUME
DOCUMENTATION_AUDITOR_V0_6_LATER_BOUNDARY_EQUIVALENCE: NOT_ESTABLISHED
DOCUMENTATION_AUDITOR_V0_6_RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
DOCUMENTATION_AUDITOR_V0_6_RECEIPT_MECHANICAL_ENFORCEMENT: NOT_ESTABLISHED
DOCUMENTATION_AUDITOR_V0_7_RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
```

No later corrected run rewrites any historical FAIL.

## Limits

This record does not authorize merge, publication, consumer-project mutation, production mutation, runtime certification, legacy retirement or automatic Core redesign.

## Anti-loop

- one final v0.7 P09 family only for this cross-turn receipt-order defect;
- no v0.8 prompt hardening after another cross-turn receipt-order FAIL;
- no full-P10 claim from the user-observed receipt-order subgate;
- no material-equivalence reuse of the partially recorded v0.6 later boundary;
- no mechanical-enforcement claim from behavioral compliance;
- no aggregation across unresolved Builder, SES-ref or project-ref drift;
- do not reopen/downgrade SaaS v0.1 historical PASS.
