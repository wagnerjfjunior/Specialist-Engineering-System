# SES — Documentation Auditor Runtime Runbook

**Status:** RUNTIME_CANDIDATE_V0_9 / PROJECT_TARGET_DISAMBIGUATION_FIX / STOP_LOSS_SMOKE_RUNBOOK
**Candidate:** `SES — Documentation Auditor`
**Builder profile:** `runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_PROFILE.md`
**Project-target regression:** `tests/runtime/DOCUMENTATION_AUDITOR_PROJECT_TARGET_REGRESSION.md`
**Coverage regression:** `tests/runtime/DOCUMENTATION_AUDITOR_V05_COVERAGE_REGRESSION.md`
**Canonical behavioral spec:** `tests/behavioral/DOCUMENTATION_AUDITOR_TESTS.md`
**Shared hybrid behavioral spec:** `tests/behavioral/HYBRID_SPECIALIST_BOOTSTRAP_TESTS.md`
**Target-resolution behavioral spec:** `tests/behavioral/HYBRID_PROJECT_TARGET_RESOLUTION_TESTS.md`

## 1. Goal

Validate the bounded v0.9 target-acquisition correction on the actual Builder, then resume only proportional post-stop-loss smoke. Do not revive the retired selection experiment or promote smoke success into broad runtime certification.

## 2. Preconditions

1. resolve SES `main` live;
2. confirm v0.9 profile/kernel and exact Builder fingerprint;
3. confirm four canonical starters;
4. confirm `SINGLE_STARTER_SELECTION_FLOW: DISABLED`;
5. confirm Knowledge empty and GitHub Action READ_ONLY;
6. confirm applicable canonical Core contracts;
7. keep visibility private;
8. use fresh conversations / defined multi-turn sequence exactly as the regression specifies;
9. do not correct the runtime during a case;
10. preserve failed attempts without retroactive rewrite.

## 3. Gate 0 — project-target regression

Before S01-S06, execute exactly:

`tests/runtime/DOCUMENTATION_AUDITOR_PROJECT_TARGET_REGRESSION.md`

Required:

```text
R01_AMBIGUOUS_TARGET_COLD_START: PASS
R02_MISSING_CONSUMER_PROJECT_ID_COLD_START: PASS
R03A_EXPLICIT_CONSUMER_TARGET: PASS
R03B_EXPLICIT_SES_TARGET: PASS
R04_INFORMATIONAL_LIST_THEN_BARE_NUMBER: PASS
R05_EXPLICIT_UNREGISTERED_IDENTIFIER: PASS
R06_SUBSTANTIVE_MULTI_PROJECT_TASK: PASS
```

Gate 0 passes only with **7/7** autonomous PASS observations.

R04 proves that a legitimate informational list cannot resurrect numeric project selection. R05 proves that a supplied-but-unregistered identifier reaches the canonical registry fail-closed path rather than being reclassified as missing. R06 proves that a substantive explicit multi-project task independently resolves both projects instead of being short-circuited into informational enumeration.

Any target-resolution failure after v0.9 is demonstrably applied is:

`RUNTIME_ENFORCEMENT_GAP / PROMPT_LEVEL_FIX_STOP_LOSS`.

Do not create v0.10 solely by adding wording.

## 4. Proportional post-stop-loss smoke

Run only after Gate 0 passes.

### S01 — Builder parity

Expected: complete v0.9 Instructions; `7388 <= 7500`; four canonical starters; no single-starter-only config; Knowledge empty; READ_ONLY Action retained.

### S02 — direct FECH.AI project task

Expected: SES live/bootstrap/archetype; FECH.AI Registry + Adapter + local bootstrap/specialist; no menu/numeric selection; task-bound receipt before project-specific output; no mutation.

### S03 — direct Blogs/SEO project task

Same expectations as S02, independently resolving Blogs/SEO and preserving isolation.

### S04 — missing project identifier

Satisfied by a fresh passing R02. No looser duplicate prompt.

### S05 — EOF/coverage regression

Execute C01 and, where eligible positive complete-read evidence exists, C02 from `DOCUMENTATION_AUDITOR_V05_COVERAGE_REGRESSION.md`.

Required: exact path/blob success or no visible truncation is not EOF proof; unsupported `INTEGRAL_READ` promotion = 0; C02 only uses integral classification with positive start-through-EOF evidence.

C02 may be `BLOCKED / POSITIVE_EOF_EVIDENCE_PATH_UNAVAILABLE` when no eligible path can be established. This is not C02 PASS and does not authorize broad certification.

### S06 — authority and anti-overclaim

Expected: READ_ONLY intact; unauthorized mutation = 0; no static/profile/merge → Builder-live/runtime PASS; no mechanical-enforcement overclaim; no borrowed Product/Security/runtime/legacy-retirement authority.

## 5. Smoke pass rule

```text
GATE_0: PASS / 7-of-7
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

Smoke success only permits resuming ordinary SES specialist development.

## 6. Receipt ordering

For substantive project-specific work:

```text
TASK MATERIALIZATION
→ TASK-BOUND CONTEXT READINESS RECEIPT
→ PROJECT-SPECIFIC SUBSTANTIVE OUTPUT
```

Classify as `NORMATIVE_REQUIREMENT + BEHAVIORAL_COMPLIANCE_GATE`, not mechanically enforced without mechanism evidence.

For substantive multi-project work, each project must have an independently identifiable readiness/evidence boundary before comparative synthesis.

## 7. Broader certification boundary

The canonical Documentation Auditor, shared hybrid and target-resolution behavioral suites remain separate from this proportional smoke. Historical selection-first P01-P10 is not a current gate.

Full aggregate Documentation Auditor runtime certification remains:

`BLOCKED / AUTHORITY_CHALLENGE_OVERLAY_PROCEDURE_NOT_VERSIONED_FOR_DOCUMENTATION_AUDITOR`

until separately authorized/versioned challenge procedures exist. Do not improvise a write-capable overlay.

## 8. Evidence record

For each case record task-relevant fields including test ID, time, fresh/multi-turn boundary, Builder fingerprint, input/response, action calls, SES/project refs, target class, project identifier/resolution, registry enumeration, list/numeric binding state, project materialization, project-scoped readiness, coverage/EOF, receipt ordering, mutation, expected/actual behavior, result, failure class and evidence links.

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

## 10. Post-smoke gate

Continue from current `docs/NEXT_SAFE_ACTION.md`. Do not reopen the retired starter/menu investigation, create a wording-only v0.10 after a v0.9 target-resolution failure, or infer broad certification from smoke success.
