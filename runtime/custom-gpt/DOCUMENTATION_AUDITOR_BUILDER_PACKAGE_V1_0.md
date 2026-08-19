# SES — Documentation Auditor Builder Package v1.0

**Package ID:** `documentation-auditor-builder-package-v1.0`  
**Candidate:** `documentation-auditor-v1.0`  
**Archetype:** `documentation-auditor`  
**Status:** `VERSIONED_CERTIFICATION_CANDIDATE / BUILDER_REAPPLY_REQUIRED / NOT_CERTIFIED`

## Purpose

Complete Builder configuration contract for the fingerprint that will be used to close C05-C10 and terminal certification. This package is separate from historical v0.9 evidence and does not rewrite its failures.

```text
PACKAGE_VERSIONED != BUILDER_APPLIED
BUILDER_APPLIED != RUNTIME_PASS
HISTORICAL_V0_9_FAIL != V1_0_RESULT
RETROACTIVE_PASS = NO
```

## Builder identity

**Name:** `SES — Documentation Auditor`

**Description:**
`Auditor híbrido de documentação e evidência do Specialist Engineering System. Resolve o projeto live, decompõe claims, vincula prova e proveniência, controla cobertura, contradições e freshness e emite somente conclusões reproduzíveis dentro da evidência disponível.`

**Visibility:** `PRIVATE / APENAS PARA MIM`

## Instructions

Use the exact complete content of:

`runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_KERNEL_V1_0.md`

```text
KERNEL_BLOB = 90fcabe72ca5202b54f50ba48b695de00096afa6
INSTRUCTIONS_UNICODE_CODE_POINTS = 7889
INSTRUCTIONS_UTF8_BYTES = 7893
BUILDER_HARD_LIMIT = <= 8000 characters
```

No paraphrase, summary, old v0.9 kernel or path-only placeholder may substitute for the exact kernel.

## Conversation starters

Use exactly:

1. `Audite este documento ou PR no projeto que eu indicar e construa o claim-to-evidence mapping antes do veredito.`
2. `Verifique se estas afirmações estão realmente provadas pelas fontes canônicas live e identifique evidência faltante ou contraditória.`
3. `Faça uma auditoria multiarquivo com matriz de cobertura, provenance e proof obligations.`
4. `Revalide somente os claims invalidados por esta mudança de head/ref, sem repetir auditoria desnecessária.`

## Knowledge

`EMPTY`

## Capabilities / integration target

Preserve the already-established v0.9 non-instruction configuration unless the Builder UI materially changed:

```text
Web Search = ENABLED
Code Interpreter / Data Analysis = ENABLED
Image Generation = DISABLED
Actions = ENABLED
Action = SES GitHub READ_ONLY / api.github.com
Action schema = runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml
Action schema blob = 1e6237e806fd84716ec13b019e6617ad4110a211
Auth = API key / Bearer; secret stays only in Builder UI
Model = GPT-5.6 Sol (gpt-5-6) when still exposed/available
Visibility = PRIVATE / APENAS PARA MIM
```

Any material model/capability/action/settings drift must be recorded in the captured fingerprint rather than guessed.

## Builder application receipt

After applying, capture:

```text
RUNTIME_NAME
PACKAGE_ID
PACKAGE_REF
KERNEL_BLOB
INSTRUCTIONS_COMPLETE_COPY
INSTRUCTIONS_CHARACTER_COUNT
STARTERS = 4 exact
KNOWLEDGE = EMPTY
WEB_SEARCH
DATA_ANALYSIS
IMAGE_GENERATION
ACTION_NAME
ACTION_SCHEMA_BLOB
AUTHENTICATED_PRINCIPAL
MODEL
VISIBILITY
BUILDER_ID/URL if exposed
DATE_TIME
```

C07 and C08 remain `NOT_ESTABLISHED` until this external application/fingerprint evidence exists.

## Runtime binding

The certification runtime must use this exact applied package/fingerprint and execute:

- `tests/behavioral/DOCUMENTATION_AUDITOR_TESTS.md`;
- `tests/runtime/DOCUMENTATION_AUDITOR_CERTIFICATION_L2_RUNBOOK_V1_0.md`;
- applicable GitHub READ_ONLY tool-honesty challenge.

Historical v0.9 R03A/R05/R06 failures remain historical and are not relabeled.
