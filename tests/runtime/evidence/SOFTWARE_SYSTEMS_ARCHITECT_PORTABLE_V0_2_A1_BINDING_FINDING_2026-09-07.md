# SES — Software Systems Architect Portable v0.2 — A1 Binding Finding — 2026-09-07

**Status:** RUNTIME_FINDING / USER_CORRECTED / NO_RETROACTIVE_PASS

## Observed result

The v0.2 portable candidate correctly demonstrated ordinary consumer-project execution without central SES live access and correctly invalidated FECH.AI context on project switch.

However, its Context Readiness Receipt emitted descriptive values such as:

```text
FINGERPRINT = PORTABLE_CANDIDATE_v0.2__CURRENT_v0.1_UNCHANGED
SES_BASELINE = CURRENT_V0_1_UNCHANGED
```

instead of exact package-binding constants or an explicit not-captured fingerprint state.

## Adjudication

```text
T01 PORTABLE EXECUTION BEHAVIOR = PASS
PROJECT SWITCH ISOLATION = PASS
PACKAGE BINDING RECEIPT = PARTIAL / INITIAL_BINDING_OVERCLAIM
RETROACTIVE_PASS = NO
```

Root cause is SES package/receipt design: the candidate did not provide sufficiently explicit stable runtime-binding constants while the Core receipt required an exact fingerprint value.

## Correction

Core now separates:

```text
DECLARED_RUNTIME_BINDING
!=
EXTERNAL_FINGERPRINT_PROOF
```

The next candidate must declare exact package ID/version/SES baseline constants and use `NOT_CAPTURED_IN_RUNTIME / EXTERNAL_PROOF_REQUIRED` when the cryptographic fingerprint is not independently available to the runtime.

Only the affected binding/receipt obligation requires retest. Previously demonstrated unrelated behavior is not rewritten or promoted retroactively.
