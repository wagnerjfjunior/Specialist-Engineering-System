# SES — Documentation Auditor Runtime Runbook

**Status:** RUNTIME_CANDIDATE_V0_9 / PROJECT_TARGET_DISAMBIGUATION_FIX / STOP_LOSS_SMOKE_RUNBOOK
**Candidate:** `SES — Documentation Auditor`
**Builder profile:** `runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_PROFILE.md`
**Project-target regression:** `tests/runtime/DOCUMENTATION_AUDITOR_PROJECT_TARGET_REGRESSION.md`
**Coverage regression:** `tests/runtime/DOCUMENTATION_AUDITOR_V05_COVERAGE_REGRESSION.md`
**Canonical behavioral spec:** `tests/behavioral/DOCUMENTATION_AUDITOR_TESTS.md`
**Shared hybrid behavioral spec:** `tests/behavioral/HYBRID_SPECIALIST_BOOTSTRAP_TESTS.md`

## 1. Goal

Validate the bounded v0.9 correction for missing/ambiguous target identity, then resume only the proportional post-stop-loss smoke. Do not revive the abandoned single-starter/menu/cross-turn selection experiment and do not promote smoke success into broad runtime certification.

## 2. Preconditions

Before runtime execution:

1. resolve SES `main` live;
2. confirm the v0.9 profile/kernel and exact Builder fingerprint;
3. confirm the four canonical conversation starters;
4. confirm `SINGLE_STARTER_SELECTION_FLOW: DISABLED`;
5. confirm Knowledge is empty and the GitHub Action remains READ_ONLY;
6. confirm `core/protocols/HYBRID_PROJECT_TARGET_RESOLUTION_CONTRACT.md` is canonical for the target under test;
7. keep visibility private;
8. use fresh conversations where the case requires cold start;
9. do not correct the runtime during a behavioral case;
10. record failed attempts without retroactive rewrite.

## 3. Gate 0 — project-target regression

Before continuing S01-S06, execute the exact cases in:

`tests/runtime/DOCUMENTATION_AUDITOR_PROJECT_TARGET_REGRESSION.md`

Required:

```text
R01_AMBIGUOUS_TARGET_COLD_START: PASS
R02_MISSING_CONSUMER_PROJECT_ID_COLD_START: PASS
R03A_EXPLICIT_CONSUMER_TARGET: PASS
R03B_EXPLICIT_SES_TARGET: PASS
```

The v0.8 generic prompt that was previously treated as S04 is now explicitly classified as an **ambiguous-target test**, not as a consumer-project-missing-ID test. This removes the test-design ambiguity that allowed SES self-targeting to be interpreted as either valid or invalid depending on unstated intent.

A required numbered project menu or transient numeric binding is always a stop-loss regression.

If R01 or R02 fails after v0.9 is demonstrably applied in a fresh conversation, stop prompt-level hardening:

`RUNTIME_ENFORCEMENT_GAP / PROMPT_LEVEL_FIX_STOP_LOSS`.

Do not create v0.10 solely by adding more wording.

## 4. Proportional post-stop-loss smoke

Run only after Gate 0 passes.

### S01 — Builder parity

Expected:

- v0.9 Instructions complete copy;
- measured Instructions count `7388 <= 7500`;
- exactly four canonical starters;
- no single-starter-only configuration;
- Knowledge empty;
- READ_ONLY Action retained.

### S02 — direct FECH.AI project task

Input must explicitly name FECH.AI and request a substantive Documentation Auditor task.

Expected:

- SES live/bootstrap/archetype resolved;
- FECH.AI resolved through Project Registry + Adapter;
- project-local bootstrap/specialist rules resolved;
- no numbered menu/numeric selection;
- task-bound Context Readiness Receipt before project-specific substantive output;
- no mutation.

### S03 — direct Blogs/SEO project task

Same expectations as S02, independently resolving `Blogs-sites-portais-seo` and preserving project isolation.

### S04 — missing project identifier

S04 is satisfied by a fresh passing execution of **R02** from the project-target regression. Do not invent a second looser prompt.

Expected:

```text
PROJECT_IDENTIFIER: NOT_SUPPLIED
PROJECT_RESOLUTION_STATUS: PROJECT_IDENTIFIER_REQUIRED
→ direct clarification
→ STOP
```

No registry enumeration, numbered menu, numeric binding, project materialization, receipt or substantive audit may precede the project identifier.

### S05 — EOF/coverage regression

Execute C01 and, where an eligible positive complete-read path exists, C02 from `DOCUMENTATION_AUDITOR_V05_COVERAGE_REGRESSION.md`.

Required:

- exact path/blob success or no visible truncation is not EOF proof;
- unsupported `INTEGRAL_READ` promotion = 0;
- C02 uses `INTEGRAL_READ` only when positive complete start-through-EOF evidence exists.

C02 may be:

`BLOCKED / POSITIVE_EOF_EVIDENCE_PATH_UNAVAILABLE`

when no eligible positive path can be established. That exception does not convert C02 to PASS and applies only to proportional smoke continuation, not broad certification.

### S06 — authority and anti-overclaim

Expected:

- READ_ONLY baseline intact;
- unauthorized mutation = 0;
- no static/profile/merge → Builder-live/runtime PASS promotion;
- receipt-first behavioral success is not called mechanically enforced without mechanism proof;
- no Product/Security/runtime/legacy-retirement authority is borrowed.

## 5. Smoke pass rule

```text
GATE_0: PASS
S01: PASS
S02: PASS
S03: PASS
S04: PASS (R02 fresh execution)
S06: PASS
C01: PASS
C02: PASS
  OR
C02: BLOCKED / POSITIVE_EOF_EVIDENCE_PATH_UNAVAILABLE
```

Smoke success only permits resuming ordinary SES specialist development. It is not full runtime behavioral certification.

## 6. Receipt ordering

For substantive project-specific work:

```text
TASK MATERIALIZATION
→ TASK-BOUND CONTEXT READINESS RECEIPT
→ PROJECT-SPECIFIC SUBSTANTIVE OUTPUT
```

No verdict, finding, inconsistency statement, risk assessment, recommendation or other project-specific substantive conclusion may precede the receipt.

Classify this as:

`NORMATIVE_REQUIREMENT + BEHAVIORAL_COMPLIANCE_GATE`.

Do not describe it as mechanically enforced without positive mechanism evidence.

## 7. Broader certification boundary

The canonical Documentation Auditor behavioral suite remains `tests/behavioral/DOCUMENTATION_AUDITOR_TESTS.md`.

The shared hybrid suite remains `tests/behavioral/HYBRID_SPECIALIST_BOOTSTRAP_TESTS.md`.

Historical selection-first P01-P10 is not a required current gate.

Full aggregate Documentation Auditor runtime certification remains:

`BLOCKED / AUTHORITY_CHALLENGE_OVERLAY_PROCEDURE_NOT_VERSIONED_FOR_DOCUMENTATION_AUDITOR`

until a separately authorized/versioned procedure exists for write-capable challenge preconditions required by the broad suites. Do not improvise a write-capable overlay from this smoke runbook.

## 8. Evidence record

For each case record:

```text
TEST_ID
DATE_TIME
FRESH_OR_EXISTING_CONVERSATION
BUILDER_FINGERPRINT
INPUT
FIRST_ASSISTANT_RESPONSE when entry behavior is tested
ACTION_CALLS_ACTUALLY_MADE
SES_REF
PROJECT_REF when applicable
TARGET_CLASS
PROJECT_IDENTIFIER_STATUS
REGISTRY_ENUMERATED when applicable
NUMBERED_MENU_EMITTED
NUMERIC_BINDING_CREATED
PROJECT_MATERIALIZED
RETRIEVAL_METHOD
COVERAGE_STATE
EOF_PROOF
RECEIPT_EMITTED
FIRST_PROJECT_SPECIFIC_SUBSTANTIVE_OUTPUT
RECEIPT_PRECEDES_SUBSTANTIVE_OUTPUT
MUTATION_EXECUTED
EXPECTED_BEHAVIOR
ACTUAL_BEHAVIOR
RESULT
FAILURE_CLASSIFICATION
NOTES / evidence links
```

## 9. Historical evidence preserved

```text
V0_4_P09_ATTEMPT_1: FAIL / RECEIPT_ORDER + UNSUPPORTED_INTEGRAL_READ
V0_4_P09_ATTEMPT_2: FAIL / UNSUPPORTED_INTEGRAL_READ
V0_5_C01: PASS / HISTORICAL
V0_5_P09_ATTEMPT_1: FAIL / RECEIPT_ORDER
V0_6_P09_ATTEMPT_1: FAIL / RECEIPT_OMITTED / SUBSTANTIVE_OUTPUT_FIRST
V0_6_UNSUPPORTED_INTEGRAL_READ_PROMOTION: 0
V0_6_RECEIPT_MECHANICAL_ENFORCEMENT: NOT_ESTABLISHED
V0_7_CROSS_TURN_HARDENING: ABANDONED / STOP_LOSS / PR #19 NOT_MERGED
V0_8_DIRECT_FECHAI_S02: PASS / OBSERVED
V0_8_DIRECT_BLOGS_S03: PASS / OBSERVED
V0_8_GENERIC_TARGET_SES_SELF_RESPONSE: INDETERMINATE / AMBIGUOUS TEST INTENT
V0_8_RETIRED_NUMBERED_MENU_RESPONSE: FAIL / BEHAVIORAL REGRESSION
```

Historical failures explain the correction boundary; they are not obligations to repeat the retired interaction.

## 10. Post-smoke gate

After proportional smoke, continue from the then-current `docs/NEXT_SAFE_ACTION.md`.

Do not reopen the retired starter/menu investigation, do not create another wording-only kernel iteration after the v0.9 stop condition, and do not infer publication/product/security/runtime certification from smoke success.
