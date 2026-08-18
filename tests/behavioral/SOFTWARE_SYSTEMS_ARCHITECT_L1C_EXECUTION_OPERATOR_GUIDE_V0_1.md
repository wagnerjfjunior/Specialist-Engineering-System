# SES — Software Systems Architect L1-C Execution Operator Guide v0.1

**Candidate:** `software-systems-architect / builder-fit-v0.1`  
**Runbook:** `tests/behavioral/SOFTWARE_SYSTEMS_ARCHITECT_L1C_RUNBOOK_V0_1.md`  
**Executor kernel:** `tests/behavioral/SOFTWARE_SYSTEMS_ARCHITECT_L1C_EXECUTOR_KERNEL_V0_1.md`

## 1. Candidate-side execution

For each Candidate fixture `A01` through `A15` and each prompt-invariance fixture `A16A`, `A16B`, `A16C`:

1. open a **new fresh conversation**;
2. supply the complete exact executor kernel first;
3. then supply only that fixture's facts + request;
4. capture the assistant's **first response only**;
5. do not correct, coach or add missing criteria before capture;
6. close the conversation and use a new one for the next fixture.

The executor kernel must be identical in every Candidate-side run.

```text
ONE FIXTURE = ONE FRESH CONVERSATION
FIRST RESPONSE ONLY
NO COACHING BEFORE CAPTURE
NO KERNEL DRIFT
```

## 2. Generic baseline execution

Run separate fresh generic conversations for representative equivalents of:

```text
A01
A03
A04
A08
A09
A11
A13
```

For generic baseline runs:

- do **not** supply the Software Systems Architect executor kernel;
- use only the fixture facts + request;
- capture first response only;
- one fresh conversation per fixture;
- do not coach/correct before capture.

The baseline is a competent generic-model comparison, not another specialist execution.

## 3. Evidence bundle

Return one raw text artifact containing, for every execution:

```text
EXECUTION_CLASS = CANDIDATE | GENERIC_BASELINE
FIXTURE_ID
FRESH_CONVERSATION = YES / operator attestation
MODEL / MODE = actual if visible, otherwise NOT CAPTURED
TOOLS INVOKED = actual / NONE OBSERVED / NOT CAPTURED
PROMPT = complete fixture facts + request
FIRST_RESPONSE = complete unedited first response
```

Also attest once for the bundle:

```text
CANDIDATE_KERNEL_PATH = tests/behavioral/SOFTWARE_SYSTEMS_ARCHITECT_L1C_EXECUTOR_KERNEL_V0_1.md
CANDIDATE_KERNEL_COMPLETE_COPY = YES
SAME_KERNEL_FOR_ALL_CANDIDATE_RUNS = YES
ONE_FIXTURE_PER_FRESH_CONVERSATION = YES
FIRST_RESPONSE_ONLY = YES
NO_COACHING_BEFORE_CAPTURE = YES
GENERIC_BASELINE_RECEIVED_SPECIALIST_KERNEL = NO
```

If any attestation is not true, record the actual state. Do not repair provenance by assertion.

## 4. Prompt invariance

`A16A`, `A16B`, `A16C` must be separate fresh conversations using the same exact kernel and identical facts; only request wording changes.

Do not place all three prompts in one conversation.

## 5. Failure handling

If an initial response materially fails:

```text
INITIAL_RESULT = FAIL
```

Preserve it. A corrected run is a new evidence event such as:

```text
Axx_RETEST_1
```

Never replace the initial raw response or relabel it retroactively as PASS.

## 6. Historical identity boundary

Do not label historical SaaS Architect executions as Software Systems Architect executions. The new L1-C evidence starts with these fresh Candidate runs.

## 7. Adjudication boundary

The operator does not self-score the specialist. Return raw executions and provenance; SES adjudicates P01-P22, prompt invariance, generic baseline non-regression and stop-loss.

```text
EXECUTION != ADJUDICATION
CORRECTION != RETROACTIVE_PASS
L1-C PASS != L2 PASS
```

## 8. After L1-C

Only after an evidence-bound L1-C PASS should the current Software Systems Architect Builder package be applied and fingerprinted for L2 runtime validation, unless SES explicitly records a different proportional sequence.