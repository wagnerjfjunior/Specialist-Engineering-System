# SES — Documentation Auditor Runtime Enforcement Boundary

**Status:** `SPECIALIST_SPECIFIC_RUNTIME_BOUNDARY_V0_2 / CANDIDATE_LEARNING / STOP_LOSS_RESCOPED`
**Applies to:** `SES — Documentation Auditor` Custom GPT runtime
**Evidence basis:** Documentation Auditor v0.4–v0.6 runtime observations

## 1. Purpose

Preserve the specialist-specific learning exposed by repeated receipt-order failures without preserving the abandoned single-starter/selection-first experiment as an active proof obligation.

The required substantive ordering remains:

```text
TASK MATERIALIZATION
→ TASK-BOUND CONTEXT READINESS RECEIPT
→ PROJECT-SPECIFIC SUBSTANTIVE OUTPUT
```

This document classifies what runtime evidence can prove about that ordering.

## 2. Required distinction

Keep separate:

```text
NORMATIVE_REQUIREMENT
BEHAVIORAL_COMPLIANCE
MECHANICALLY_ENFORCED_INVARIANT
```

- `NORMATIVE_REQUIREMENT`: canonical specification states required behavior.
- `BEHAVIORAL_COMPLIANCE`: the actual configured runtime autonomously exhibits required behavior in an executed bounded case.
- `MECHANICALLY_ENFORCED_INVARIANT`: a mechanism outside ordinary model instruction-following technically prevents/rejects the invalid transition.

Therefore:

```text
INSTRUCTION_PRESENT != BEHAVIOR_OBSERVED
BEHAVIOR_OBSERVED != MECHANICAL_ENFORCEMENT
PROMPT_INVARIANT != ENFORCED_RUNTIME_INVARIANT
```

## 3. Current evidence boundary

Current evidence does not establish a separate output controller/validator/transition gate that mechanically prevents substantive output before the receipt.

```text
RECEIPT_FIRST_NORMATIVE_REQUIREMENT: ESTABLISHED
RECEIPT_FIRST_BEHAVIORAL_COMPLIANCE: VERSION/CASE_BOUND
RECEIPT_FIRST_MECHANICAL_ENFORCEMENT: NOT_ESTABLISHED
```

Do not describe Builder-only receipt ordering as deterministic, guaranteed or mechanically enforced.

Absence of observed enforcement is not universal proof that no future mechanism can exist. Any future enforcement claim requires positive mechanism evidence.

## 4. Historical evidence

Preserve:

```text
V0_4_P09_ATTEMPT_1: FAIL / RECEIPT_ORDER + UNSUPPORTED_INTEGRAL_READ
V0_4_P09_ATTEMPT_2: FAIL / UNSUPPORTED_INTEGRAL_READ
V0_4_RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
V0_5_C01: PASS / HISTORICAL
V0_5_P09_ATTEMPT_1: FAIL / RECEIPT_ORDER
V0_5_RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
V0_6_P09_ATTEMPT_1: FAIL / RECEIPT_OMITTED / SUBSTANTIVE_OUTPUT_FIRST
V0_6_RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
V0_7_CROSS_TURN_HARDENING: ABANDONED / STOP_LOSS / PR #19 NOT_MERGED
```

The historical P09 labels identify the cases that exposed the issue. They do not make the retired selection-first P01–P10 interaction suite an active v0.8 requirement.

## 5. Cross-layer FECH.AI observation

Historical v0.6 evidence found a FECH.AI response-format conflict that placed `Verdict:` before bootstrap/readiness. FECH.AI later reconciled that conflict through its own reviewed project-local process.

Classification:

```text
FECHAI_VERDICT_FIRST_TEMPLATE: CONTRIBUTING_CONFLICT / HISTORICAL
SES_V06_INTERNAL_ORDER_CONTRADICTION: NOT_ESTABLISHED AFTER V0_6 CORRECTION
```

The FECH.AI correction is independent of the single-starter UX rollback. It does not prove mechanical enforcement.

## 6. Post-stop-loss proof obligations

A future claim of `BEHAVIORAL_COMPLIANCE` requires fresh autonomous runtime evidence bound to:

```text
BUILDER_FINGERPRINT
SES_REF
PROJECT_REF when project-bound
CANONICAL_TEST_ID / SMOKE_ID
TASK_SCOPE
```

For post-stop-loss continuation, use the v0.8 S01–S06 smoke defined by `tests/runtime/DOCUMENTATION_AUDITOR_RUNTIME_RUNBOOK.md` before broader runtime work.

The smoke must verify direct project+task bootstrap, receipt-before-substantive-output, EOF/coverage discipline, project isolation and authority boundaries without recreating numbered-menu/numeric-selection/cross-turn state.

A future claim of `MECHANICALLY_ENFORCED_INVARIANT` additionally requires positive evidence of an actual enforcement mechanism plus an executed invalid-transition challenge.

Instruction wording or successful behavioral tests alone are insufficient.

## 7. Receipt-order subgate

For any substantive project-specific case:

```text
RECEIPT_EMITTED: YES
RECEIPT_PRECEDES_SUBSTANTIVE_OUTPUT: YES
UNSUPPORTED_INTEGRAL_READ_PROMOTION: 0
AUTONOMOUS_CORRECTION_REQUIRED: 0
```

Passing this subgate establishes only receipt-order behavioral compliance for the exact evidence boundary. It does not establish broad runtime/product/security PASS and must not be called mechanically enforced.

## 8. Stop-loss boundary

Do not use this learning document to recreate or require:

```text
# CLIQUE PARA INICIAR
→ numbered project menu
→ numeric selection
→ PROJECT_SELECTED
→ WAIT FOR TASK
→ cross-turn resume
```

The feature was retired by product stop loss. Historical evidence remains preserved; active proof obligations move to the direct project+substantive-task flow.

## 9. Generalization boundary

This remains `CANDIDATE_LEARNING` from one specialist domain. It is not promoted here to a universal SES principle for all specialists or all model runtimes.
