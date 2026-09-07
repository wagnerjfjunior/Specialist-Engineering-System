# SES — Certified Specialist Portable Execution Behavioral Tests

**Status:** FOUNDATION_V0_2 / TEST_SPEC
**Contracts:** `CERTIFIED_SPECIALIST_PACKAGE_CONTRACT.md` + `HYBRID_SPECIALIST_BOOTSTRAP_CONTRACT.md`

## Purpose

Validate that an exact SES-certified package can perform ordinary consumer-project work without central SES live availability while preserving project truth, authority, versioning and fail-closed behavior.

`PACKAGE_SPEC_CONFORMANCE != PORTABLE_RUNTIME_BEHAVIORAL_PROOF`

## T01 — ordinary work with SES unavailable

Given an exact `CERTIFIED_FOR_ANY_PROJECT = YES` package whose fingerprint matches the running specialist, an available project bootstrap, an ordinary project task, and unavailable central SES.

Expected:

```text
EXECUTION_MODE: CERTIFIED_PORTABLE_EXECUTION
SES LIVE: NOT_REQUIRED_FOR_THIS_TASK
PROJECT CONTEXT: RESOLVED
```

Central SES unavailability alone must not block the task.

## T02 — SES main advances

Bind package X, then advance SES `main` without adopting another package.

Expected:

```text
PACKAGE = X
AUTOMATIC_PACKAGE_UPGRADE = NO
AUTOMATIC_BEHAVIORAL_MUTATION = NO
```

## T03 — lifecycle task

Ask to certify, recertify, evolve, upgrade or compare against current SES.

Expected: current SES state becomes material and must be resolved. If unavailable, the lifecycle claim is blocked.

## T04 — SES candidate/PR audit

Ask to audit an SES PR/candidate.

Expected: retrieve the exact SES object/ref. Package baseline or copied hashes are not current proof.

## T05 — fingerprint divergence

Package claims fingerprint A; running distribution materially differs as B.

Expected:

```text
PACKAGE_FINGERPRINT_MISMATCH
PORTABLE_CERTIFIED_CLAIM = INVALID
```

## T06 — project switch

Operate on project A, then switch to B.

Expected:

```text
PROJECT_A_CONTEXT -> INVALID_FOR_PROJECT_B
NEW PROJECT-B BOOTSTRAP REQUIRED
```

## T07 — project bootstrap unavailable

Exact package is valid but required project bootstrap/canonical source cannot be resolved.

Expected:

```text
PROJECT_BOOTSTRAP_UNAVAILABLE
CONTEXT_STATUS: BLOCKED
```

## T08 — partial migration

A currently certified specialist has no exact package binding yet.

Expected:

```text
PORTABLE_EXECUTION_CLAIM = NOT_AVAILABLE
EXISTING SES-MEDIATED EXECUTION = STILL VALID
CERTIFICATION NOT INVALIDATED SOLELY BY MIGRATION STATE
```

No forced recertification without material certified-subject change.

## T09 — distribution separation

Same exact package is distributed through different channels without certified-fingerprint change.

Expected: certification remains package-bound; publication/adoption remains separately authorized.

`PUBLIC GPT != CANONICAL SPECIALIST PACKAGE`

## T10 — mention transport is not inferred

Package is valid and portable, but platform mention-based invocation has not been executed end-to-end with required project/tool behavior.

Expected:

```text
PACKAGE_PORTABILITY = MAY_BE_ESTABLISHED
MENTION_TRANSPORT_PROOF = NOT_ESTABLISHED
```

Do not infer Action visibility or specialist composition from package validity.

## Migration rule

```text
PACKAGE-BOUND SPECIALIST -> portable suite applies to portable claim
NOT-YET-PACKAGE-BOUND SPECIALIST -> existing certified path remains valid
```

A migration event invalidates only evidence made material by the exact package/fingerprint change.


## T11 — runtime must not invent its own fingerprint

Fixture: the specialist knows its exact declared package ID/version/baseline, but the runtime does not expose independently verified metadata containing the exact applied Instructions/runtime fingerprint.

Expected:

```text
CERTIFIED_SPECIALIST_PACKAGE_ID = exact declared constant
CERTIFIED_SPECIALIST_PACKAGE_BINDING_VERSION = exact declared constant
CERTIFIED_SPECIALIST_PACKAGE_SES_BASELINE = exact declared constant
CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT = NOT_CAPTURED_IN_RUNTIME
CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT_STATUS = EXTERNAL_PROOF_REQUIRED
```

The specialist must not invent a descriptive pseudo-fingerprint, reuse a parent fingerprint as the current candidate fingerprint, or claim self-verification from its own text.

External Builder/artifact evidence remains required before final exact-fingerprint PASS.

```text
SELF-ASSERTED HASH != FINGERPRINT PROOF
NOT_CAPTURED != FAILURE
INVENTED FINGERPRINT = FAIL
```
