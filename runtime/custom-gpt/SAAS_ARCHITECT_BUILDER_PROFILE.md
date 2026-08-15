# SES — SaaS Architect Custom GPT Builder Profile

**Status:** STABLE_V0_1_SEMANTICS / BUILDER_FIT_REVISION / EXTERNAL_BUILDER_RECONCILIATION_REQUIRED
**ARCHETYPE_ID:** `saas-architect`

## 1. Purpose

Version the post-stop-loss SaaS Architect Builder configuration using the proven v0.1 direct-entry semantics while fitting the Builder Instructions limit.

Historical v0.1 runtime proof remains historical and preserved. The current compact kernel is a new Builder fingerprint and is not automatically covered by that proof.

```text
V0_1_RUNTIME_BEHAVIORAL_PROOF: PASS / HISTORICAL / PRESERVED
CURRENT_BUILDER_FIT_REVISION_RUNTIME_PROOF: NOT_YET_ESTABLISHED
V0_2_RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED / SUPERSEDED_BY_STOP_LOSS
V0_3_RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED / SUPERSEDED_BY_STOP_LOSS
```

`PROFILE_VERSIONED != BUILDER_APPLIED != CURRENT_RUNTIME_PROOF`

## 2. Builder fields

### Name

`SES — SaaS Architect`

### Description

`Arquiteto SaaS híbrido do Specialist Engineering System. Resolve o projeto live, carrega regras canônicas e executa auditoria, trade-offs e target architecture com evidência, fail-closed e isolamento entre projetos.`

### Instructions

Use the complete exact content of:

`runtime/custom-gpt/SAAS_ARCHITECT_BUILDER_KERNEL.md`

Do not use the profile itself, a path-only placeholder, paraphrase, truncated copy or permanent Knowledge as a substitute.

Builder constraints:

```text
BUILDER_INSTRUCTIONS_HARD_LIMIT: <= 8000 characters
SES_OPERATIONAL_BUDGET: <= 7500 characters
CURRENT_COMPACT_KERNEL_MEASURED_COUNT: 6182 characters
COUNT_METHOD: Unicode code-point count of repository text content
CURRENT_KERNEL_BLOB: 5c57fb8f0bd558c2e9ebeee26add399a4308e077
```

### Conversation starters

1. `Reconstrua o contexto live do projeto que eu indicar e faça um Deep Architecture Audit do fluxo especificado.`
2. `Compare a arquitetura atual deste projeto com alternativas e recomende uma target architecture com trade-offs, migração e rollback.`
3. `Audite este fluxo multi-tenant de ponta a ponta: identidade → autorização → tenant → persistência → side effects.`
4. `Revalide uma decisão arquitetural atual usando evidência live e diga o que mudou, o que continua válido e a próxima ação segura.`

Starters are UX examples only. They never establish project configuration, identity, readiness or authority.

Retired interaction:

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

No Action mutation is part of this correction.

### Authentication

```text
Type: API key
Mode: Bearer
Secret: Builder UI only / never committed
```

### Visibility

`PRIVATE / APENAS PARA MIM` until a separate publication decision.

### Model

Record the actual selected model in the Builder fingerprint. Model changes may invalidate current behavioral evidence.

## 3. Runtime loading chain

The Instructions kernel does not reread itself during ordinary tasks. It directs the runtime to load live SES/project authority:

`SES main → docs/bootstrap/INDEX.md → archetypes/REGISTRY.md → saas-architect archetype → applicable Core protocols → projects/REGISTRY.md → Project Adapter → consumer-project bootstrap/local specialist → material evidence → task-bound Context Readiness Receipt → bounded architecture work`.

The Builder profile/kernel/action files are reread when configuring, validating or testing the runtime candidate, as specified by `docs/bootstrap/INDEX.md`.

## 4. Historical certified evidence

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

The historical kernel blob exceeded the current Builder limit when copied in the present UI. It remains historical evidence only. The current Builder-fit kernel preserves the v0.1 direct-entry safety/architecture semantics but has a new blob and requires a fresh proportional smoke before any current-runtime equivalence claim.

## 5. Superseded experiment evidence

```text
V0_2_P01_ATTEMPT_1: FAIL / BUILDER_KERNEL_DRIFT
V0_2_SELECTION_FIRST_TARGET: SUPERSEDED
V0_3_DEFERRED_SELECTION_TARGET: SUPERSEDED
SINGLE_STARTER_SELECTION_FLOW: RETIRED_BY_STOP_LOSS
```

Do not retry the retired interaction.

## 6. Builder reconciliation gate

Before applying/testing verify:

```text
INSTRUCTIONS_COMPLETE_COPY: YES
INSTRUCTIONS_CHARACTER_COUNT = 6182
INSTRUCTIONS_CHARACTER_COUNT <= 7500
CONVERSATION_STARTERS: exactly 4
SINGLE_STARTER_SELECTION_FLOW: DISABLED
KNOWLEDGE: EMPTY
ACTION_SURFACE: READ_ONLY / GET-only
```

Capture a fresh non-secret fingerprint and keep separate:

```text
PROFILE_VERSIONED
!= BUILDER_RECONCILED
!= FINGERPRINT_COMPLETE
!= POST_ROLLBACK_SMOKE
!= CURRENT_RUNTIME_BEHAVIORAL_PROOF
```

Historical v0.1 PASS remains historical proof for its exact evidence boundary.

## 7. Lifecycle separation

This correction does not authorize publication, broad sharing, consumer-project mutation, production/security claims or legacy retirement.
