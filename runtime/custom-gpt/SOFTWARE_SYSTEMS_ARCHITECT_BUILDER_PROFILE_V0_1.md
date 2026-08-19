# SES — Software Systems Architect Custom GPT Builder Profile v0.1

**Status:** BUILDER_FIT / EXTERNAL_BUILDER_RECONCILIATION_REQUIRED / L1C_PASS
**ARCHETYPE_ID:** `software-systems-architect`

## 1. Purpose

Version the intended Builder configuration for `SES — Software Systems Architect` while preserving historical `SES — SaaS Architect` runtime evidence as legacy fingerprint-bound evidence only.

```text
HISTORICAL_SAAS_ARCHITECT_RUNTIME_BEHAVIORAL_PROOF = PASS / PRESERVED
SOFTWARE_SYSTEMS_ARCHITECT_L1C = PASS
SOFTWARE_SYSTEMS_ARCHITECT_CURRENT_RUNTIME_PROOF = NOT_YET_ESTABLISHED
LEGACY_ALIAS != RETROACTIVE_IDENTITY_REWRITE
PROFILE_VERSIONED != BUILDER_APPLIED != CURRENT_RUNTIME_PROOF
```

## 2. Builder fields

### Name

`SES — Software Systems Architect`

### Description

`Arquiteto de sistemas de software do SES. Audita AS-IS, domínios, dependências, trust boundaries, multi-tenancy, dados, eventos, concorrência, confiabilidade e observabilidade; define target architecture, migração, rollback e proof obligations com evidência e isolamento entre projetos.`

Measured: `286 Unicode code points / 292 UTF-8 bytes`.

Observed Builder UI constraint supplied by operator on 2026-08-19: Description must fit within `300` characters. This profile treats that as runtime UI evidence, not a universal platform constant.

### Instructions

Use the complete exact content of:

`runtime/custom-gpt/SOFTWARE_SYSTEMS_ARCHITECT_BUILDER_KERNEL_V0_1.md`

Expected kernel blob:

`5aa37be41e83e7f3c83019a5b29e1a8583364d2f`

Measured exact source length:

```text
INSTRUCTIONS_UNICODE_CODE_POINTS = 7710
INSTRUCTIONS_UTF8_BYTES = 7752
```

Observed Builder UI constraint supplied by operator on 2026-08-19: Instructions must fit within `8000` characters. The current kernel is intentionally below that observed limit.

Do not use this profile, a path-only placeholder, paraphrase, truncated copy or permanent Knowledge as a substitute for the exact kernel.

### Conversation starters

1. `Reconstrua o AS-IS do sistema que eu indicar e faça um Deep Architecture Audit das fronteiras, dependências, estado e riscos.`
2. `Compare a arquitetura atual com alternativas viáveis e recomende uma target architecture com trade-offs, migração, proof obligations e rollback.`
3. `Audite este fluxo ponta a ponta: identidade → autorização → tenant → domínio → persistência → eventos/side effects → observabilidade → falha/recuperação.`
4. `Revalide uma decisão arquitetural atual com evidência live e diga o que mudou, o que continua válido e a próxima ação segura.`

Starters are UX examples only. They never establish project configuration, identity, readiness or authority.

### Knowledge

`EMPTY`

### Capabilities

```text
Web Search: ENABLED
Code Interpreter / Data Analysis: ENABLED
Image Generation: DISABLED
Actions: ENABLED
Apps: record actual Builder UI state
```

Web Search is supplementary only.

### Actions

One custom Action: `SES GitHub READ_ONLY`

Schema: `runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`
Expected schema blob: `1e6237e806fd84716ec13b019e6617ad4110a211`

Authentication: API key / Bearer / secret in Builder UI only.
No Action mutation is part of this candidate.

### Visibility

`PRIVATE / APENAS PARA MIM` until a separate publication decision.

### Model

Record the actual selected model in the Builder fingerprint. Model changes may invalidate current behavioral evidence.

## 3. Runtime loading chain

`SES main → docs/bootstrap/INDEX.md → archetypes/REGISTRY.md → software-systems-architect archetype → Core protocols → projects/REGISTRY.md → Project Adapter → consumer-project bootstrap/local specialist → material evidence → task-bound Context Readiness Receipt → bounded architecture work`.

## 4. Historical evidence boundary

Canonical historical evidence remains `tests/runtime/evidence/HYBRID_SAAS_ARCHITECT_RUNTIME_PROOF_2026-08-12.md`.

```text
HISTORICAL_IDENTITY = SES — SaaS Architect
HISTORICAL_ARCHETYPE_ID = saas-architect
HISTORICAL_RUNTIME_BEHAVIORAL_PROOF = PASS
HISTORICAL_T01_T29 = 29/29 PASS
HISTORICAL_KERNEL_BLOB = 50672d09665035c0f60f18887f3295a5ea8cad03
HISTORICAL_ACTION_SCHEMA_BLOB = 1e6237e806fd84716ec13b019e6617ad4110a211
LEGACY_ALIAS != RETROACTIVE_IDENTITY_REWRITE
```

Do not rename that historical evidence in place.

## 5. Builder reconciliation gate

Before L2 capture:

```text
RUNTIME_NAME = SES — Software Systems Architect
ARCHETYPE_ID = software-systems-architect
DESCRIPTION_COMPLETE_COPY = YES
DESCRIPTION_CHARACTER_COUNT = 286
INSTRUCTIONS_COMPLETE_COPY = YES
KERNEL_BLOB = 5aa37be41e83e7f3c83019a5b29e1a8583364d2f
INSTRUCTIONS_CHARACTER_COUNT = 7710
INSTRUCTIONS_UTF8_BYTES = 7752
CONVERSATION_STARTERS = exactly 4
KNOWLEDGE = EMPTY
ACTION_SURFACE = READ_ONLY / GET-only
MODEL = actual
APPS = actual / NOT EXPOSED
VISIBILITY = PRIVATE / APENAS PARA MIM
```

Capture a fresh non-secret fingerprint and keep separate:

```text
PROFILE_VERSIONED != BUILDER_RECONCILED != FINGERPRINT_COMPLETE != L2_RUNTIME_PROOF != CERTIFIED_FOR_ANY_PROJECT
```

## 6. Lifecycle separation

L1-C PASS does not authorize publication, broad sharing, consumer-project mutation, production/security claims or legacy evidence retirement. Builder application and current runtime proof remain open gates.