# Documentation Auditor v1.1 — corrective design — 2026-08-20

## Trigger

Repeated autonomous G01 failures on v1.0:
- attempt 1: `PROJECT_NOT_REGISTERED`
- attempt 2: `PROJECT_IDENTIFIER_REQUIRED`

Same generic baseline in an ordinary SES project conversation produced a bounded non-PASS verdict, isolating the defect to the Documentation Auditor target-entry behavior rather than the generic reasoning capability.

## Root cause

The v1.0 target-entry rule was over-broad: generic methodological claim analysis was intercepted as project-specific work.

## Minimal correction

Introduce an explicit classification before project resolution:
- `GENERIC_METHOD_ANALYSIS`: reusable audit reasoning without project-owned facts/state/authority/evidence/environment/mutation; no project identifier or readiness receipt required.
- `PROJECT_SPECIFIC_WORK`: conclusion depends on project truth/state/authority/evidence/repository/environment/lifecycle/mutation; existing project-resolution rules remain mandatory.

Resulting complete Instructions object:

```text
candidate = documentation-auditor-v1.1
blob = 5bc10297d9e655cf169d2680f914e446232992e0
unicode_code_points = 7984
utf8_bytes = 7988
builder_limit = <= 8000 characters
```

The complete blob was created and read back through the GitHub blob API. Human-readable amendment is versioned in `runtime/custom-gpt/DOCUMENTATION_AUDITOR_TARGET_ENTRY_AMENDMENT_V1_0_1.md`; package is `runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_PACKAGE_V1_1.md`.

## Invalidation radius

Material kernel change invalidates current Builder application/fingerprint and runtime claims that depend on target-entry classification. Revalidate only:

```text
G01
R01
R02
T11 corrected
T18 corrected
T20 corrected
T25 corrected
T30 corrected
```

No automatic re-audit of unaffected historical PASS cases.

## History preservation

```text
V1.0_G01_ATTEMPT_1 = FAIL
V1.0_G01_ATTEMPT_2 = FAIL
RETROACTIVE_PASS = NO
CERTIFIED_FOR_ANY_PROJECT = NO
```
