# SES — Specialist Portfolio Wave 2 L1-C Execution Manifest v0.1

**Branch:** `feat/specialist-portfolio-wave-2`  
**Purpose:** bind canonical L1-C execution to exact frozen kernels and prevent proof transfer across material changes.

## Application Security Assurance

```text
CANDIDATE_ID = application-security-assurance-specialist-v0.1
KERNEL_ID = application-security-assurance-l1c-executor-kernel-v0.1
KERNEL_BLOB_SHA = c1a0a6e66278b0bc94ef3280aff635a42faf9332
RUNBOOK = tests/behavioral/APPLICATION_SECURITY_ASSURANCE_SPECIALIST_L1C_RUNBOOK_V0_1.md
COVERAGE_SUPPLEMENT = tests/behavioral/SPECIALIST_PORTFOLIO_WAVE_2_L1C_COVERAGE_SUPPLEMENT_V0_1.md / A13+A14
BEHAVIORAL_SUITE = tests/behavioral/APPLICATION_SECURITY_ASSURANCE_SPECIALIST_BEHAVIORAL_SUITE_V0_1.md
L1_C_EXECUTION = NOT_EXECUTED
L1_C_RESULT = NOT_ESTABLISHED
L2_RUNTIME = NOT_EXECUTED
```

## Backend & Data Platform

```text
CANDIDATE_ID = backend-data-platform-specialist-v0.1
KERNEL_ID = backend-data-platform-l1c-executor-kernel-v0.1
KERNEL_BLOB_SHA = 906274528abc8becac74b29d64863175aa10abd2
RUNBOOK = tests/behavioral/BACKEND_DATA_PLATFORM_SPECIALIST_L1C_RUNBOOK_V0_1.md
COVERAGE_SUPPLEMENT = tests/behavioral/SPECIALIST_PORTFOLIO_WAVE_2_L1C_COVERAGE_SUPPLEMENT_V0_1.md / B17+B18
BEHAVIORAL_SUITE = tests/behavioral/BACKEND_DATA_PLATFORM_SPECIALIST_BEHAVIORAL_SUITE_V0_1.md
L1_C_EXECUTION = NOT_EXECUTED
L1_C_RESULT = NOT_ESTABLISHED
L2_RUNTIME = NOT_EXECUTED
```

## Execution constraints

Canonical L1-C evidence is valid only when:
- the exact kernel blob SHA above is used unchanged;
- each fixture runs in a fresh isolated context;
- the first response is captured before correction/coaching;
- hidden adjudication criteria/answer keys are not visible to the executor;
- the runbook and the bound coverage supplement fixtures are both executed;
- raw input/output and available execution metadata are preserved;
- historical FAIL remains historical after later correction;
- generic-baseline and prompt-invariance requirements are executed as specified by each runbook.

If either kernel changes materially, prior execution evidence does not transfer automatically. Record a new kernel hash/version and re-run only affected proof obligations.

## Current execution blocker

The current design conversation is contaminated for canonical L1-C because it contains candidate design decisions, behavioral expectations, fixtures and adjudication logic.

```text
CURRENT_CONVERSATION_ELIGIBLE_FOR_L1C = NO
REASON = CONTAMINATED_CONTEXT
REQUIRED_NEXT_MECHANISM = FRESH_ISOLATED_EXECUTOR_CONTEXTS
```

Do not downgrade this requirement merely to accelerate delivery. Using the current conversation would produce invalid proof, not faster proof.

## Current proof boundary

```text
CANDIDATES = VERSIONED
BEHAVIORAL_SUITES = VERSIONED
L1C_KERNELS = FROZEN / HASH_BOUND
L1C_RUNBOOKS = VERSIONED
L1C_COVERAGE_SUPPLEMENT = VERSIONED / BOUND
PRE_EXECUTION_COVERAGE_REVIEW = COMPLETED
L1C_EXECUTION = NOT_EXECUTED / BLOCKED_ON_FRESH_ISOLATED_CONTEXTS
L1 PASS = NOT_ESTABLISHED
L2 PASS = NOT_ESTABLISHED
BUILDER = NOT_APPLIED
ARCHETYPE ACTIVATION = NOT_AUTHORIZED / NOT_ESTABLISHED
PUBLICATION = NOT_AUTHORIZED
CONSUMER ADOPTION = NOT_AUTOMATIC
```

This manifest is a preparation artifact, not behavioral proof.