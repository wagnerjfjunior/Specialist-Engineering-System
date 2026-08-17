# AppSec L1-C A08–A14 Operator Attestation — 2026-08-17

**Candidate:** `application-security-assurance-specialist-v0.1`  
**Scope:** A08, A09, A10, A11, A12A, A12B, A12C, A13, A14  
**Purpose:** close operator-level provenance for the historical batch executions without inventing raw transport hashes.

## Operator attestation

The operator explicitly confirmed on 2026-08-17 that, for each execution A08, A09, A10, A11, A12A, A12B, A12C, A13 and A14:

- execution occurred in a new/fresh conversation;
- the canonical AppSec kernel and corresponding fixture were pasted integrally and without intentional editing;
- before submission, the executor context did not contain the behavioral suite, expected response, scoring, answer key, another fixture response, or corrective guidance;
- the response preserved in `Respostas.txt` was the first response received.

## Provenance interpretation

This attestation is valid operator-level provenance metadata under `SPECIALIST_PORTFOLIO_WAVE_2_L1C_EXECUTION_OPERATOR_GUIDE_V0_2.md`.

It does not create byte-level UI fidelity or transport hashes retroactively.

```text
FRESH_CONTEXT_ATTESTED = YES
KERNEL_AND_FIXTURE_INTEGRAL_NO_INTENTIONAL_EDIT_ATTESTED = YES
NO_ANSWER_KEY_OR_COACHING_ATTESTED = YES
FIRST_RESPONSE_ATTESTED = YES
RAW_INPUT_HASH = NOT_CAPTURED
RAW_OUTPUT_HASH = NOT_CAPTURED
RENDERING_NORMALIZATION = OBSERVED
```

## Historical packet boundary

The A08–A14 execution-packet files were versioned after those historical executions. Therefore:

```text
HISTORICAL_EXECUTION_PACKET_BLOB_BINDING = NOT_ESTABLISHED
OPERATOR_ATTESTED_CANONICAL_CONTENT = YES
```

This attestation does not retroactively claim that the later packet blob SHAs were the exact transport inputs used historically.

## Historical result preservation

- original A07 remains historical `FAIL` for P14 freshness;
- A07-R1 is a separate corrective PASS event;
- no historical FAIL/INVALID is rewritten.

```text
RETROACTIVE_PASS = NO
RETROACTIVE_PACKET_BINDING = NO
```
