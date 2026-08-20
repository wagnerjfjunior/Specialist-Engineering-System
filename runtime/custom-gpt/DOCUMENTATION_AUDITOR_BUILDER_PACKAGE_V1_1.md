# SES — Documentation Auditor Builder Package v1.1

**Package ID:** `documentation-auditor-builder-package-v1.1`
**Candidate:** `documentation-auditor-v1.1`
**Archetype:** `documentation-auditor`
**Status:** `VERSIONED / BUILDER_APPLIED / RUNTIME_VALIDATED / CERTIFIED_FOR_ANY_PROJECT`

## Correction scope

This package changes only target-entry classification after repeated G01 failures on v1.0. Historical v1.0 failures remain historical; `RETROACTIVE_PASS = NO`.

## Exact Instructions

Use the exact complete content of:

`runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_KERNEL_V1_1.md`

```text
KERNEL_ID = documentation-auditor-builder-kernel-v1.1
KERNEL_BLOB = 5bc10297d9e655cf169d2680f914e446232992e0
INSTRUCTIONS_UNICODE_CODE_POINTS = 7984
INSTRUCTIONS_UTF8_BYTES = 7988
BUILDER_HARD_LIMIT = <= 8000 characters
```

The complete kernel file resolves to the exact certified blob. The human-readable delta is also preserved at `runtime/custom-gpt/DOCUMENTATION_AUDITOR_TARGET_ENTRY_AMENDMENT_V1_0_1.md`; v1.0 remains preserved at `runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_KERNEL_V1_0.md`.

## Builder identity and settings

```text
Name = SES — Documentation Auditor
Knowledge = EMPTY
Web Search = ENABLED
Code Interpreter / Data Analysis = ENABLED
Image Generation = DISABLED
Actions = ENABLED
Action = SES GitHub READ_ONLY / api.github.com
Action schema = runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml
Action schema blob = 1e6237e806fd84716ec13b019e6617ad4110a211
Auth = API key / Bearer; secret stays only in Builder UI
Model = GPT-5.6 Sol (gpt-5-6) at certified fingerprint
Visibility = PRIVATE / APENAS PARA MIM
```

Conversation starters remain the exact four starters from v1.0 package.

## Certification binding

```text
BUILDER_APPLIED = PASS
RUNTIME_FINGERPRINT_CAPTURED = PASS_WITH_PROVENANCE_LIMITATION
T01-T30 = PASS
R01-R06 = 7/7 PASS
P01-P03 = PASS
G01-G05 = PASS
TOOL_HONESTY = PASS
C01-C18 = PASS
CERTIFIED_FOR_ANY_PROJECT = YES
```

Final evidence:

`tests/runtime/evidence/DOCUMENTATION_AUDITOR_FINAL_CERTIFICATION_2026-08-20.md`

Any later material change to the kernel, Builder configuration, model/runtime settings, Action/tool surface, archetype semantics or bootstrap contracts invalidates only the affected obligations and requires proportional revalidation.
