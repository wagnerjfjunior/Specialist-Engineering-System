# SES — Software Systems Architect Builder Package v0.3 Portable Candidate

**Status:** PORTABLE_VNEXT_BINDING_FIX_CANDIDATE / BUILDER_NOT_APPLIED / BINDING_RETEST_REQUIRED
**Parent portable candidate:** `runtime/custom-gpt/SOFTWARE_SYSTEMS_ARCHITECT_BUILDER_PACKAGE_V0_2_PORTABLE_CANDIDATE.md`
**Parent portable kernel blob:** `1b5195362a10f5732dc2f81335c035dc29c46b40`
**Current certified parent remains:** v0.1 / unchanged

## Exact runtime binding constants

```text
PACKAGE_ID = software-systems-architect-portable-v0.3-candidate
BINDING_VERSION = v0.3-candidate
SES_BASELINE_REF = e25cdf6b9a4f7d7ef4badc1ac3014b6e10d218e4

KERNEL_PATH =
runtime/custom-gpt/SOFTWARE_SYSTEMS_ARCHITECT_BUILDER_KERNEL_V0_3_PORTABLE_CANDIDATE.md

KERNEL_BLOB =
d62f8cf750b7965b602ac335050c7c88a5732b5f

INSTRUCTIONS_CHARACTERS =
7910
```

The running model must not invent its own cryptographic fingerprint.

Expected portable receipt values:

```text
CERTIFIED_SPECIALIST_PACKAGE_ID =
software-systems-architect-portable-v0.3-candidate

CERTIFIED_SPECIALIST_PACKAGE_BINDING_VERSION =
v0.3-candidate

CERTIFIED_SPECIALIST_PACKAGE_SES_BASELINE =
e25cdf6b9a4f7d7ef4badc1ac3014b6e10d218e4

CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT =
NOT_CAPTURED_IN_RUNTIME

CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT_STATUS =
EXTERNAL_PROOF_REQUIRED
```

The exact kernel blob above is external artifact evidence, not a self-declared runtime hash.

## Material delta from v0.2 portable candidate

Only package-binding/receipt semantics change.

Preserved from v0.2 evidence:
- ordinary consumer-project execution without central SES live dependency;
- project switch invalidation;
- SES lifecycle mode switching;
- architecture method/authority/tool-honesty behavior.

Historical v0.2 result remains:

```text
PACKAGE_BINDING_RECEIPT = PARTIAL / INITIAL_BINDING_OVERCLAIM
RETROACTIVE_PASS = NO
```

## Retest

After this exact kernel is applied to the separate candidate Builder, run only:

`tests/runtime/CERTIFIED_PORTABLE_BINDING_RETEST_V0_1.md`

Any additional Builder/model/tool/configuration delta expands retest scope.

```text
CURRENT_CERTIFIED_V0_1 = PRESERVED
V0_2_PORTABLE_EVIDENCE = HISTORICAL
V0_3_CANDIDATE_VERSIONED != BUILDER_APPLIED != BINDING_RETEST_PASS
```
