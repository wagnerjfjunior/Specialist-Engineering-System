# SES — Documentation Auditor Builder Package v1.3 Portable Candidate

**Status:** PORTABLE_VNEXT_BINDING_FIX_CANDIDATE / BUILDER_NOT_APPLIED / BINDING_RETEST_REQUIRED
**Parent portable candidate:** `runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_PACKAGE_V1_2_PORTABLE_CANDIDATE.md`
**Parent portable kernel blob:** `98c6df641e1ffaf6650f4d3075f31e2aba602dc4`
**Current certified parent remains:** v1.1 / unchanged

## Exact runtime binding constants

```text
PACKAGE_ID = documentation-auditor-portable-v1.3-candidate
BINDING_VERSION = v1.3-candidate
SES_BASELINE_REF = e25cdf6b9a4f7d7ef4badc1ac3014b6e10d218e4

KERNEL_PATH =
runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_KERNEL_V1_3_PORTABLE_CANDIDATE.md

KERNEL_BLOB =
9cfc485c6c69f9724d55d3bcc77509be4dd74492

INSTRUCTIONS_CHARACTERS =
7986
```

Expected portable receipt values:

```text
CERTIFIED_SPECIALIST_PACKAGE_ID =
documentation-auditor-portable-v1.3-candidate

CERTIFIED_SPECIALIST_PACKAGE_BINDING_VERSION =
v1.3-candidate

CERTIFIED_SPECIALIST_PACKAGE_SES_BASELINE =
e25cdf6b9a4f7d7ef4badc1ac3014b6e10d218e4

CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT =
NOT_CAPTURED_IN_RUNTIME

CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT_STATUS =
EXTERNAL_PROOF_REQUIRED
```

Exact kernel blob is external artifact proof; the runtime must not synthesize a hash.

## Material delta from v1.2 portable candidate

Only package-binding/receipt semantics plus wording compression required to remain under Builder size limits.

Audit method, target classification, project isolation, receipt-first discipline, evidence engineering, tool honesty, mutation authority and lifecycle-history safeguards remain materially unchanged.

## Retest

After applying this exact kernel to the separate candidate Builder, run the Documentation Auditor case in:

`tests/runtime/CERTIFIED_PORTABLE_BINDING_RETEST_V0_1.md`

Any additional Builder/model/tool/configuration delta expands retest scope.

```text
CURRENT_CERTIFIED_V1_1 = PRESERVED
V1_2_PORTABLE_CANDIDATE = HISTORICAL
V1_3_CANDIDATE_VERSIONED != BUILDER_APPLIED != BINDING_RETEST_PASS
```
