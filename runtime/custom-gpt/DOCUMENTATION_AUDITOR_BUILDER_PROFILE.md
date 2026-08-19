# SES — Documentation Auditor Custom GPT Builder Profile

**Status:** `RUNTIME_TARGET_V1_0 / CERTIFICATION_CANDIDATE / BUILDER_REAPPLY_REQUIRED`  
**ARCHETYPE_ID:** `documentation-auditor`  
**Builder package:** `runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_PACKAGE_V1_0.md`

## Current certification target

```text
CANDIDATE = documentation-auditor-v1.0
KERNEL_PATH = runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_KERNEL_V1_0.md
KERNEL_BLOB = 90fcabe72ca5202b54f50ba48b695de00096afa6
INSTRUCTIONS_UNICODE_CODE_POINTS = 7889
INSTRUCTIONS_UTF8_BYTES = 7893
BUILDER_HARD_LIMIT = <= 8000 characters
BUILDER_APPLIED = NOT_YET_ESTABLISHED FOR V1_0
RUNTIME_FINGERPRINT = NOT_YET_CAPTURED FOR V1_0
CERTIFIED_FOR_ANY_PROJECT = NO
```

## Builder fields

### Name
`SES — Documentation Auditor`

### Description
`Auditor híbrido de documentação e evidência do Specialist Engineering System. Resolve o projeto live, decompõe claims, vincula prova e proveniência, controla cobertura, contradições e freshness e emite somente conclusões reproduzíveis dentro da evidência disponível.`

### Instructions
Use the exact complete content of `runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_KERNEL_V1_0.md`.

### Conversation starters
1. `Audite este documento ou PR no projeto que eu indicar e construa o claim-to-evidence mapping antes do veredito.`
2. `Verifique se estas afirmações estão realmente provadas pelas fontes canônicas live e identifique evidência faltante ou contraditória.`
3. `Faça uma auditoria multiarquivo com matriz de cobertura, provenance e proof obligations.`
4. `Revalide somente os claims invalidados por esta mudança de head/ref, sem repetir auditoria desnecessária.`

### Knowledge
`EMPTY`

### Target capabilities / Action

Preserve the established non-instruction configuration unless the Builder UI materially changed:

```text
Web Search = ENABLED
Code Interpreter / Data Analysis = ENABLED
Image Generation = DISABLED
Actions = ENABLED
ACTION_NAME = SES GitHub READ_ONLY / api.github.com
ACTION_SCHEMA = runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml
ACTION_SCHEMA_BLOB = 1e6237e806fd84716ec13b019e6617ad4110a211
AUTH = API key / Bearer; secret Builder-only
MODEL = GPT-5.6 Sol (gpt-5-6) when exposed/available
VISIBILITY = PRIVATE / APENAS PARA MIM
```

Record actual UI state rather than guessing if any field changed.

## Required fingerprint after application

Capture name, description, exact kernel blob/count, starters, Knowledge, capabilities, Action/schema/auth principal, model/settings, visibility, Builder ID/version if exposed and timestamp.

```text
PACKAGE_VERSIONED != BUILDER_APPLIED
BUILDER_APPLIED != RUNTIME_BEHAVIORAL_PROOF
```

## Certification execution

After v1.0 is applied and fingerprinted, execute:

`tests/runtime/DOCUMENTATION_AUDITOR_CERTIFICATION_L2_RUNBOOK_V1_0.md`.

Only actual execution may close C02-C04 and C07-C10. C11 readiness follows runtime PASS; C12 requires user READY authorization for the exact final fingerprint.

## Historical v0.9 integrity

The previous applied v0.9 fingerprint remains historical evidence:

```text
V0_9_KERNEL_BLOB = 6ca9e1d22d7faf0639076e5d43332b3267ec2354
V0_9_BUILDER_APPLIED = ESTABLISHED
V0_9_FINGERPRINT_COMPLETE = YES
V0_9_CORRECTED_R03A = FAIL
V0_9_CORRECTED_R05 = FAIL
V0_9_R06 = FAIL
V0_9_PROJECT_TARGET_REGRESSION = 4/7
PROMPT_LEVEL_FIX_STOP_LOSS = TRIGGERED FOR V0_9 COSMETIC RETRIES
RETROACTIVE_PASS = NO
RETROACTIVE_ERASURE = NO
```

The v1.0 candidate is a new fingerprint boundary. A later v1.0 PASS does not rewrite v0.9.

The Documentation Auditor Runtime Enforcement Gateway remains separate second-phase work and is not a prerequisite for specialist certification.
