# SES — Documentation Auditor Builder Package v1.1

**Package ID:** `documentation-auditor-builder-package-v1.1`
**Candidate:** `documentation-auditor-v1.1`
**Archetype:** `documentation-auditor`
**Status:** `VERSIONED_CORRECTIVE_CANDIDATE / BUILDER_REAPPLY_REQUIRED / NOT_CERTIFIED`

## Correction scope

This package changes only target-entry classification after repeated G01 failures on v1.0. Historical v1.0 failures remain historical; `RETROACTIVE_PASS = NO`.

Resulting complete Instructions object:

```text
KERNEL_ID = documentation-auditor-builder-kernel-v1.1
KERNEL_BLOB = 5bc10297d9e655cf169d2680f914e446232992e0
INSTRUCTIONS_UNICODE_CODE_POINTS = 7984
INSTRUCTIONS_UTF8_BYTES = 7988
BUILDER_HARD_LIMIT = <= 8000 characters
```

The complete blob was created and independently recovered through the GitHub blob API. The human-readable delta is versioned at `runtime/custom-gpt/DOCUMENTATION_AUDITOR_TARGET_ENTRY_AMENDMENT_V1_0_1.md`; v1.0 remains preserved at `runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_KERNEL_V1_0.md`.

## Builder identity and settings

Preserve v1.0 package settings exactly unless the Builder UI itself materially changed:

```text
Name = SES — Documentation Auditor
Knowledge = EMPTY
Web Search = ENABLED
Code Interpreter / Data Analysis = ENABLED
Image Generation = DISABLED
Actions = ENABLED
Action = SES GitHub READ_ONLY / api.github.com
Action schema blob = 1e6237e806fd84716ec13b019e6617ad4110a211
Auth = API key / Bearer; secret stays only in Builder UI
Model = GPT-5.6 Sol (gpt-5-6) when still exposed/available
Visibility = PRIVATE / APENAS PARA MIM
Starters = same 4 exact starters from v1.0 package
```

## Required affected-gate retest

After applying the exact v1.1 Instructions and capturing the new fingerprint, re-run only materially affected cases:

```text
G01
R01
R02
T11 corrected generic-method fixture
T18 corrected generic-method fixture
T20 corrected generic-method fixture
T25 corrected generic-method fixture
T30 corrected generic-method fixture
```

Previously passed unaffected gates remain historical evidence unless a new material event invalidates them. G01 v1.0 attempts remain FAIL and are never rewritten.
