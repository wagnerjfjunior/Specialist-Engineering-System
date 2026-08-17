# SES — Specialist Portfolio Wave 2 L1-C Execution Operator Guide v0.1

**Branch:** `feat/specialist-portfolio-wave-2`  
**Purpose:** execute canonical L1-C evidence for Application Security Assurance and Backend & Data Platform without contaminating executor contexts.

## 1. Non-negotiable execution rule

The current design conversation is contaminated and is NOT eligible for L1-C execution.

Each Candidate fixture must run in a fresh isolated context that has not seen:
- this design conversation;
- the behavioral suite;
- the runbook adjudication section;
- expected behaviors;
- prior fixture outputs;
- corrective guidance;
- answer keys or PASS/FAIL expectations.

Only the frozen executor kernel and the exact fixture facts/request may be visible to the Candidate executor.

```text
CURRENT_DESIGN_CONTEXT != EXECUTOR_CONTEXT
FIRST RESPONSE = EVIDENTIARY UNIT
NO COACHING BEFORE CAPTURE
NO RETROACTIVE PASS
```

## 2. Exact frozen kernels

### Application Security Assurance

```text
KERNEL_ID = application-security-assurance-l1c-executor-kernel-v0.1
KERNEL_BLOB_SHA = c1a0a6e66278b0bc94ef3280aff635a42faf9332
RUNBOOK = tests/behavioral/APPLICATION_SECURITY_ASSURANCE_SPECIALIST_L1C_RUNBOOK_V0_1.md
```

### Backend & Data Platform

```text
KERNEL_ID = backend-data-platform-l1c-executor-kernel-v0.1
KERNEL_BLOB_SHA = 906274528abc8becac74b29d64863175aa10abd2
RUNBOOK = tests/behavioral/BACKEND_DATA_PLATFORM_SPECIALIST_L1C_RUNBOOK_V0_1.md
```

If either blob SHA changes, stop execution and rebind the manifest/runbook before continuing affected evidence.

## 3. Per-fixture procedure

For each Candidate fixture:

1. Start a fresh isolated model conversation/context.
2. Paste the exact frozen kernel first.
3. Append only the exact fixture facts and request from the applicable runbook.
4. Do not include fixture ID, proof-obligation names, expected behavior, scoring rules or answer key in executor-visible input.
5. Submit once.
6. Capture the first response verbatim before any follow-up.
7. Record model/configuration if available.
8. Record tools available/invoked if visible.
9. Record that the context was fresh and contained no prior fixture/output.
10. Do not correct the answer inside that context before evidentiary capture.
11. Store the raw result using the result-capture template.

## 4. Generic baseline procedure

Generic-baseline executions must also run in fresh isolated contexts.

The generic baseline receives:
- a competent generic role instruction appropriate to the domain;
- the same material facts as the paired Candidate fixture;
- no Candidate kernel;
- no adjudication criteria;
- no prior Candidate output.

Candidate and generic outputs must be adjudicated after capture, never by giving either executor the other's response.

## 5. Execution order

Preferred order minimizes accidental leakage:

```text
APPSEC CANDIDATE FIXTURES
→ APPSEC GENERIC BASELINES
→ APPSEC ADJUDICATION
→ BACKEND/DATA CANDIDATE FIXTURES
→ BACKEND/DATA GENERIC BASELINES
→ BACKEND/DATA ADJUDICATION
```

Prompt-invariance variants must run in separate fresh contexts despite sharing identical facts.

## 6. Capture fields

Record at minimum:

```text
EXECUTION_ID
SPECIALIST
CANDIDATE_ID
FIXTURE_ID
RUNBOOK_REF
KERNEL_ID
KERNEL_BLOB_SHA
MODEL
MODEL_CONFIGURATION
TOOLS_AVAILABLE
TOOLS_INVOKED
TIMESTAMP
FRESH_CONTEXT_ASSERTION
PRIOR_MESSAGES_COUNT
RAW_INPUT
RAW_OUTPUT
RAW_INPUT_HASH (if available)
RAW_OUTPUT_HASH (if available)
RESULT = NOT_ADJUDICATED initially
CORRECTION_OCCURRED = NO at first capture
RETEST_REQUIRED
NOTES
```

Unavailable telemetry is `NOT CAPTURED`; never infer it.

## 7. Adjudication separation

Adjudication happens only after raw capture and outside the executor context.

Use the behavioral suite and runbook to assess:
- critical failure/stop-loss;
- proof-obligation coverage;
- evidence honesty;
- authority boundaries;
- prompt invariance;
- generic-baseline non-regression;
- Supabase family coverage where applicable.

Allowed results:

```text
PASS
FAIL
BLOCKED
NOT_APPLICABLE
INVALID
```

If the initial response fails and a later corrected version succeeds:

```text
INITIAL_RESULT = FAIL
CORRECTION = NEW EVIDENCE EVENT
NO RETROACTIVE PASS
```

## 8. Completion gates

Do not declare L1-C PASS until the applicable runbook completion condition is satisfied in full.

If any required proof obligation has no executed evidence and is not justified `NOT_APPLICABLE`, overall L1-C remains `NOT_ESTABLISHED`.

After L1-C:

```text
L1 PASS != L2 PASS
L1 PASS != BUILDER APPLIED
L1 PASS != ARCHETYPE ACTIVE
L1 PASS != CONSUMER ADOPTION
```

## 9. Practical operating note

This guide deliberately separates preparation from execution. If the available interface cannot guarantee fresh isolated contexts and raw first-response capture, mark execution `BLOCKED / ISOLATION_MECHANISM_UNAVAILABLE` rather than simulate or infer a PASS.