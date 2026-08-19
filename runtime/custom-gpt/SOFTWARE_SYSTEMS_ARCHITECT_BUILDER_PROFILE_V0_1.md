# SES — Software Systems Architect Custom GPT Builder Profile v0.1

**Status:** `BUILDER_FIT / RUNTIME_CORRECTION_CANDIDATE / REAPPLY_REQUIRED / L1C_PASS / L2_R04_OPEN`  
**ARCHETYPE_ID:** `software-systems-architect`

## 1. Purpose

Version the intended Builder configuration for `SES — Software Systems Architect` while preserving historical `SES — SaaS Architect` evidence and all current L2 failures on their original fingerprints.

```text
PROFILE_VERSIONED != BUILDER_APPLIED != RUNTIME_FINGERPRINT != RUNTIME_PROOF
CERTIFIED_FOR_ANY_PROJECT = NO
```

## 2. Builder fields

**Name:** `SES — Software Systems Architect`

**Description:**

`Arquiteto de sistemas de software do SES. Audita AS-IS, domínios, dependências, trust boundaries, multi-tenancy, dados, eventos, concorrência, confiabilidade e observabilidade; define target architecture, migração, rollback e proof obligations com evidência e isolamento entre projetos.`

Measured: `286 Unicode code points / 292 UTF-8 bytes`.

**Instructions exact source:**

`runtime/custom-gpt/SOFTWARE_SYSTEMS_ARCHITECT_BUILDER_KERNEL_V0_1.md`

```text
EXPECTED_KERNEL_BLOB = 1b0e621b52468a2eab170e7b8f4d50659a406f62
INSTRUCTIONS_UNICODE_CODE_POINTS = 7994
INSTRUCTIONS_UTF8_BYTES = 8036
OPERATOR_OBSERVED_UI_LIMIT = 8000 characters / 2026-08-19
```

The observed Builder limit is character-based; this kernel remains below it.

**Conversation starters — exactly four:**

1. `Reconstrua o AS-IS do sistema que eu indicar e faça um Deep Architecture Audit das fronteiras, dependências, estado e riscos.`
2. `Compare a arquitetura atual com alternativas viáveis e recomende uma target architecture com trade-offs, migração, proof obligations e rollback.`
3. `Audite este fluxo ponta a ponta: identidade → autorização → tenant → domínio → persistência → eventos/side effects → observabilidade → falha/recuperação.`
4. `Revalide uma decisão arquitetural atual com evidência live e diga o que mudou, o que continua válido e a próxima ação segura.`

**Knowledge:** `EMPTY`

**Capabilities target:**

```text
Web Search = ENABLED
Code Interpreter / Data Analysis = ENABLED
Image Generation = DISABLED
Actions = ENABLED
Apps = record actual Builder state
```

**Action:**

```text
TITLE = SES GitHub READ_ONLY
SCHEMA = runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml
EXPECTED_SCHEMA_BLOB = 1e6237e806fd84716ec13b019e6617ad4110a211
AUTH = API key / Bearer / secret only in Builder
SURFACE = READ_ONLY / GET-only
```

**Visibility target:** `PRIVATE / APENAS PARA MIM`.

## 3. Runtime behavior corrections bound to this fingerprint

```text
MISSING PROJECT ID → ASK DIRECTLY → STOP
TOOL OPERATION NAME NOT OBSERVABLE → TOOL_OPERATION=NOT_CAPTURED
PROJECT-SPECIFIC WORK → COMPLETE CONTEXT READINESS RECEIPT FIRST
NO VERDICT / AS-IS / FINDING / RISK / ANALYSIS / RECOMMENDATION / TARGET / CONCLUSION BEFORE RECEIPT
```

## 4. Runtime loading chain

`SES main → docs/bootstrap/INDEX.md → archetypes/REGISTRY.md → software-systems-architect → archetype contract → hybrid bootstrap → explicit project resolution → Project Adapter → consumer bootstrap/local specialist → material evidence → task-bound Context Readiness Receipt → bounded architecture work`.

## 5. Reconciliation gate

```text
RUNTIME_NAME = SES — Software Systems Architect
ARCHETYPE_ID = software-systems-architect
DESCRIPTION_COMPLETE_COPY = YES
DESCRIPTION_CHARACTER_COUNT = 286
INSTRUCTIONS_COMPLETE_COPY = YES
KERNEL_BLOB = 1b0e621b52468a2eab170e7b8f4d50659a406f62
INSTRUCTIONS_CHARACTER_COUNT = 7994
INSTRUCTIONS_UTF8_BYTES = 8036
CONVERSATION_STARTERS = exactly 4
KNOWLEDGE = EMPTY
ACTION_SURFACE = READ_ONLY / GET-only
MODEL = actual
APPS = actual / NOT EXPOSED
VISIBILITY = PRIVATE / APENAS PARA MIM
```

After reapply, capture a fresh fingerprint and retest only R04 unless another material configuration change invalidates more evidence.

## 6. Current lifecycle

```text
L1-C = PASS
R01_RETEST_1 = PASS
R03_RETEST_1 = PASS
R09_RETEST_1 = PASS
R04_RETEST_1 = FAIL / PRESERVED
R04_RETEST_2 = FAIL / PRESERVED
CURRENT_BUILDER_APPLIED = STALE_REVALIDATION_REQUIRED
CURRENT_RUNTIME_FINGERPRINT = STALE_REVALIDATION_REQUIRED
C09 = NOT_SATISFIED
C10 = PASS / PRESERVED
C11 = NOT_ELIGIBLE
C12 = NOT_APPLICABLE_YET
CERTIFIED_FOR_ANY_PROJECT = NO
```
