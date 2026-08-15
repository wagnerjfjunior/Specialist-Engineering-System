# SES — SaaS Architect Custom GPT Builder Profile

**Status:** STABLE_V0_1_BASELINE_RESTORED / STOP_LOSS_ROLLBACK / EXTERNAL_BUILDER_RECONCILIATION_REQUIRED
**ARCHETYPE_ID:** `saas-architect`

## 1. Purpose

Restore the proven multi-starter SaaS Architect baseline after the single-starter/selection-first experiment was discontinued by stop loss.

The historical v0.1 runtime proof remains preserved. The rollback does not rewrite or invalidate that evidence and does not promote later v0.2/v0.3 selection-first targets into PASS.

```text
V0_1_RUNTIME_BEHAVIORAL_PROOF: PASS / HISTORICAL / PRESERVED
V0_2_RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED / SUPERSEDED_BY_STOP_LOSS
V0_3_RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED / SUPERSEDED_BY_STOP_LOSS
```

Repository profile state is not proof that the external Builder has already been reconciled.

## 2. Builder fields

### Name

`SES — SaaS Architect`

### Description

`Arquiteto SaaS híbrido do Specialist Engineering System. Resolve o projeto live, carrega regras canônicas e executa auditoria, trade-offs e target architecture com evidência, fail-closed e isolamento entre projetos.`

### Instructions

Use the complete exact kernel at:

`runtime/custom-gpt/UNIVERSAL_BUILDER_KERNEL.md`

The rollback restores the proven v0.1 direct project-entry kernel semantics. Do not replace the complete kernel with a path reference or paraphrase.

### Conversation starters

Restore the universal v0.1 set:

1. `Reconstrua o contexto live do projeto que eu indicar e faça um Deep Architecture Audit do fluxo especificado.`
2. `Compare a arquitetura atual deste projeto com alternativas e recomende uma target architecture com trade-offs, migração e rollback.`
3. `Audite este fluxo multi-tenant de ponta a ponta: identidade → autorização → tenant → persistência → side effects.`
4. `Revalide uma decisão arquitetural atual usando evidência live e diga o que mudou, o que continua válido e a próxima ação segura.`

Conversation starters are UX examples only. They never establish project configuration, identity, readiness or authority.

The retired interaction is not part of this profile:

```text
# CLIQUE PARA INICIAR
→ live numbered project menu
→ numeric selection
→ PROJECT_SELECTED
→ WAIT FOR TASK
→ cross-turn resume
```

### Knowledge

`EMPTY`

### Capabilities

Target/restored baseline:

```text
Web Search: ENABLED
Code Interpreter / Data Analysis: ENABLED
Image Generation: DISABLED
Actions: ENABLED
Apps: record actual Builder UI state
```

Web Search remains supplementary only.

### Actions

One custom Action:

`SES GitHub READ_ONLY`

Schema source:

`runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`

No Action mutation is part of this rollback.

### Authentication

```text
Type: API key
Mode: Bearer
Secret: Builder UI only / never committed
```

### Visibility

Private until a separate publication decision.

### Model

Record the actual selected model in the Builder fingerprint. Model choice remains a potential behavioral invalidation event.

## 3. Historical certified evidence

Canonical durable evidence:

`tests/runtime/evidence/HYBRID_SAAS_ARCHITECT_RUNTIME_PROOF_2026-08-12.md`

Preserve:

```text
HISTORICAL_PROFILE_VERSION: V0_1
HISTORICAL_RUNTIME_BEHAVIORAL_PROOF: PASS
HISTORICAL_T01_T29: 29/29 PASS
HISTORICAL_FAIL: 0
HISTORICAL_PENDING: 0
HISTORICAL_CERTIFIED_CANONICAL_MAIN_REF: 24089d8dbc1a90a6a0f15c5a86d9032d27f216b6
HISTORICAL_KERNEL_BLOB: 50672d09665035c0f60f18887f3295a5ea8cad03
HISTORICAL_ACTION_SCHEMA_BLOB: 1e6237e806fd84716ec13b019e6617ad4110a211
HISTORICAL_CONVERSATION_STARTERS: 4
HISTORICAL_FINAL_ACTION_SURFACE: READ_ONLY / GET-only
```

The stop-loss rollback intentionally restores kernel blob `50672d09665035c0f60f18887f3295a5ea8cad03` as the repository target.

## 4. Superseded experiment evidence

Preserve without retry obligation:

```text
V0_2_P01_ATTEMPT_1: FAIL / BUILDER_KERNEL_DRIFT
V0_2_SELECTION_FIRST_TARGET: SUPERSEDED
V0_3_DEFERRED_SELECTION_TARGET: SUPERSEDED
SINGLE_STARTER_SELECTION_FLOW: RETIRED_BY_STOP_LOSS
```

User-observed latency/premature-materialization evidence remains historical; it does not require the retired interaction to be fixed or certified.

## 5. Builder reconciliation gate

If the external SaaS Architect Builder currently differs from this restored profile, reconcile it only through a separately authorized Builder mutation.

Before any new runtime claim capture a fresh non-secret fingerprint and distinguish:

```text
PROFILE_RESTORED_IN_REPOSITORY
!= BUILDER_RECONCILED
!= FINGERPRINT_COMPLETE
!= NEW_RUNTIME_EVIDENCE
```

The historical v0.1 PASS remains historical proof for its exact evidence boundary; a changed current Builder is not automatically equivalent to that historical fingerprint.

## 6. Lifecycle separation

Repository rollback does not authorize publication, consumer-project mutation, replacement/removal of project-bound specialists or production/security claims.
