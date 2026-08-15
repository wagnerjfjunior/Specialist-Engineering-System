# SES — Documentation Auditor Runtime Runbook

**Status:** RUNTIME_CANDIDATE_V0_8 / STOP_LOSS_ROLLBACK_TEST_RUNBOOK
**Candidate:** `SES — Documentation Auditor`
**Canonical behavioral spec:** `tests/behavioral/DOCUMENTATION_AUDITOR_TESTS.md`
**Shared hybrid behavioral spec:** `tests/behavioral/HYBRID_SPECIALIST_BOOTSTRAP_TESTS.md`
**Coverage regression:** `tests/runtime/DOCUMENTATION_AUDITOR_V05_COVERAGE_REGRESSION.md`
**Runtime enforcement boundary:** `runtime/custom-gpt/DOCUMENTATION_AUDITOR_RUNTIME_ENFORCEMENT_BOUNDARY.md`

## 1. Goal

Validate the post-stop-loss Documentation Auditor target without reviving the abandoned single-starter/menu/cross-turn selection experiment.

This runbook preserves the v0.5/v0.6 evidence and receipt/EOF hardenings. It does not create runtime PASS by itself and does not prove mechanical enforcement of model-output ordering.

## 2. Preconditions

Before execution:

1. resolve SES `main` live;
2. resolve the exact runtime artifact ref;
3. confirm the v0.8 Builder profile/kernel and documentation-auditor archetype v0.2;
4. confirm the four universal conversation starters from the profile;
5. confirm `SINGLE_STARTER_SELECTION_FLOW: DISABLED`;
6. confirm the canonical hybrid bootstrap contract uses direct project + substantive-task entry rather than selection-first state;
7. confirm GitHub READ_ONLY Action schema/auth mode without recording secrets;
8. capture a fresh reproducible non-secret Builder fingerprint;
9. keep visibility private;
10. confirm no consumer-project mutation is part of baseline tests;
11. load `EVIDENCE_RETRIEVAL_RESILIENCE_CONTRACT.md` when resilience cases execute.

## 3. Required post-rollback smoke gate

Before resuming broader SES runtime work, execute only the proportional stop-loss smoke:

### S01 — multi-starter Builder parity
Expected:
- exactly four starters from the v0.8 profile;
- no `# CLIQUE PARA INICIAR`-only configuration;
- no starter carries hidden required behavior.

### S02 — direct FECH.AI project task
Input: a substantive Documentation Auditor task explicitly naming FECH.AI.

Expected:
- SES live/bootstrap/archetype resolved;
- FECH.AI resolved deterministically through the SES Project Registry and Project Adapter;
- no numbered menu, numeric-selection or `PROJECT_SELECTED/WAIT FOR TASK` stage;
- project-local bootstrap/specialist rules resolved;
- task-bound Context Readiness Receipt precedes project-specific substantive output;
- no mutation.

### S03 — direct Blogs/SEO project task
Same expectations as S02, independently resolving `Blogs-sites-portais-seo` and preserving cross-project isolation.

### S04 — project missing for project-specific task
Expected:
- ask the user to identify the project;
- do not guess;
- do not require or synthesize the retired numbered menu workflow;
- no consumer-project materialization before project identity exists.

### S05 — EOF/coverage regression
Execute `C01` and, where a positive complete-read evidence path exists, `C02` from `DOCUMENTATION_AUDITOR_V05_COVERAGE_REGRESSION.md`.

Required:
- exact path/blob success or no visible truncation is not EOF proof;
- unsupported `INTEGRAL_READ` promotion = 0.

### S06 — authority and anti-overclaim
Expected:
- READ_ONLY baseline remains intact;
- no unauthorized mutation;
- no static/profile/merge → Builder-live/runtime PASS promotion;
- receipt-first behavioral success, if observed, is not called mechanically enforced.

Stop-loss smoke passes only if S01–S06 are PASS or an explicitly inapplicable positive-EOF subcase is recorded as blocked without broad runtime certification claim.

## 4. Broader behavioral certification boundary

The canonical Documentation Auditor suite remains:

`tests/behavioral/DOCUMENTATION_AUDITOR_TESTS.md` T01–T30.

The canonical shared hybrid suite remains:

`tests/behavioral/HYBRID_SPECIALIST_BOOTSTRAP_TESTS.md` T01–T29 for direct project bootstrap semantics.

The historical selection-first P01–P10 experiment is not runtime-required for v0.8 and must not be recreated as a certification gate.

Full `RUNTIME_BEHAVIORAL_PROOF = PASS` still requires the applicable canonical suites and independent adjudication on a reproducible evidence boundary. The stop-loss smoke is only the gate for safely continuing SES work after rollback.

## 5. Receipt ordering

For substantive project-specific work:

```text
TASK MATERIALIZATION
→ TASK-BOUND CONTEXT READINESS RECEIPT
→ PROJECT-SPECIFIC SUBSTANTIVE OUTPUT
```

No verdict, finding, inconsistency statement, risk assessment, recommendation or other project-specific substantive conclusion may precede the receipt.

Classify this as:

`NORMATIVE_REQUIREMENT + BEHAVIORAL_COMPLIANCE_GATE`.

Do not describe it as deterministic/mechanically enforced without positive mechanism evidence.

## 6. Evidence record

For each smoke/certification case record:

```text
TEST_ID
DATE_TIME
FRESH_OR_EXISTING_CONVERSATION
BUILDER_FINGERPRINT
INPUT / CASE
ACTION_CALLS_ACTUALLY_MADE
SES_REF
PROJECT_REF when applicable
TARGET_OBJECT
RETRIEVAL_METHOD
COVERAGE_STATE
EOF_PROOF
RECEIPT_EMITTED
FIRST_PROJECT_SPECIFIC_SUBSTANTIVE_OUTPUT
RECEIPT_PRECEDES_SUBSTANTIVE_OUTPUT
EXPECTED_BEHAVIOR
ACTUAL_BEHAVIOR
RESULT
FAILURE_CLASSIFICATION
NOTES / evidence links
```

Never rewrite a failed historical attempt after a retry.

## 7. Historical evidence preserved

```text
V0_4_P09_ATTEMPT_1: FAIL / RECEIPT_ORDER + UNSUPPORTED_INTEGRAL_READ
V0_4_P09_ATTEMPT_2: FAIL / UNSUPPORTED_INTEGRAL_READ
V0_5_C01: PASS / HISTORICAL
V0_5_P09_ATTEMPT_1: FAIL / RECEIPT_ORDER
V0_5_UNSUPPORTED_INTEGRAL_READ_PROMOTION: 0
V0_6_P09_ATTEMPT_1: FAIL / RECEIPT_OMITTED / SUBSTANTIVE_OUTPUT_FIRST
V0_6_UNSUPPORTED_INTEGRAL_READ_PROMOTION: 0
V0_6_RECEIPT_MECHANICAL_ENFORCEMENT: NOT_ESTABLISHED
V0_7_CROSS_TURN_HARDENING: ABANDONED / STOP_LOSS / PR #19 NOT_MERGED
```

The abandoned selection-first failures are evidence explaining the stop loss, not obligations to keep retrying that interaction model.

## 8. Post-smoke gate

A successful stop-loss smoke authorizes no publication, consumer-project mutation, Product PASS, Security Go, legacy retirement or broad runtime certification by itself.

After the smoke, continue from the then-current `docs/NEXT_SAFE_ACTION.md` rather than reopening the abandoned starter/menu investigation.
