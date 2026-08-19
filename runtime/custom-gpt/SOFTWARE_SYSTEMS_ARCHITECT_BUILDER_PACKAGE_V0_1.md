# SES — Software Systems Architect Builder Configuration Package v0.1

**Package ID:** `software-systems-architect-builder-package-v0.1`  
**Certification subject:** `software-systems-architect / builder-fit-v0.1`  
**Status:** `RUNTIME_CORRECTION_CANDIDATE / REAPPLY_REQUIRED / L1C_PASS / L2_R04_OPEN`

## Lifecycle boundary

`PACKAGE_VERSIONED != BUILDER_APPLIED != RUNTIME_FINGERPRINT != L2_PASS != READY != CERTIFIED_FOR_ANY_PROJECT`

Historical `SES — SaaS Architect` evidence remains fingerprint-bound.

## Builder fields

**Name:** `SES — Software Systems Architect`

**Description — exact:**

`Arquiteto de sistemas de software do SES. Audita AS-IS, domínios, dependências, trust boundaries, multi-tenancy, dados, eventos, concorrência, confiabilidade e observabilidade; define target architecture, migração, rollback e proof obligations com evidência e isolamento entre projetos.`

```text
DESCRIPTION_UNICODE_CODE_POINTS = 286
DESCRIPTION_UTF8_BYTES = 292
```

**Instructions exact source:** `runtime/custom-gpt/SOFTWARE_SYSTEMS_ARCHITECT_BUILDER_KERNEL_V0_1.md`

```text
CURRENT_KERNEL_BLOB_SHA = 791dc63165518d16713bbaa2d869c12ac09ec2f7
INSTRUCTIONS_UNICODE_CODE_POINTS = 7436
INSTRUCTIONS_UTF8_BYTES = 7478
OPERATOR_OBSERVED_UI_LIMIT = 8000 characters / 2026-08-19
```

This revision preserves missing-project fail-closed and tool-operation honesty, preserves receipt-first ordering, and now requires an explicit nonblank receipt schema. Missing required values must use an explicit unknown/missing status; blank required fields block substantive work.

## Conversation starters

1. `Reconstrua o AS-IS do sistema que eu indicar e faça um Deep Architecture Audit das fronteiras, dependências, estado e riscos.`
2. `Compare a arquitetura atual com alternativas viáveis e recomende uma target architecture com trade-offs, migração, proof obligations e rollback.`
3. `Audite este fluxo ponta a ponta: identidade → autorização → tenant → domínio → persistência → eventos/side effects → observabilidade → falha/recuperação.`
4. `Revalide uma decisão arquitetural atual com evidência live e diga o que mudou, o que continua válido e a próxima ação segura.`

## Knowledge / capabilities / Action

```text
KNOWLEDGE = EMPTY
WEB_SEARCH = ENABLED
DATA_ANALYSIS / CODE_INTERPRETER = ENABLED
IMAGE_GENERATION = DISABLED
ACTIONS = ENABLED
GITHUB_ACTION = SES GitHub READ_ONLY
EXPECTED_SCHEMA_BLOB = 1e6237e806fd84716ec13b019e6617ad4110a211
SURFACE = READ_ONLY / GET-only
VISIBILITY = PRIVATE / APENAS PARA MIM
```

## Required receipt schema

Before substantive project-specific output emit explicit nonblank values for:

`PROOF_LEVEL`, `TASK_SCOPE`, `EFFECTIVE_SCOPE`, `TARGET_REF_OR_OBJECT`, `ENVIRONMENT`, `SES_CANONICAL_MAIN_REF`, `PROJECT_ID/PROJECT_RESOLUTION`, `PROJECT_LIVE_REF`, `SPECIALIST_RESOLUTION`, `CONTINUITY_STATUS`, `AUTHORITY_STATE`, `MUTATION_AUTHORIZATION`, `EVIDENCE_STATUS`, `CONTEXT_STATUS`, `RECEIPT_VALIDITY`, `GAPS`.

## Reconciliation checklist

```text
KERNEL_BLOB_SHA = 791dc63165518d16713bbaa2d869c12ac09ec2f7
INSTRUCTIONS_CHARACTER_COUNT = 7436
INSTRUCTIONS_UTF8_BYTES = 7478
DESCRIPTION_CHARACTER_COUNT = 286
CONVERSATION_STARTERS = 4 exact
KNOWLEDGE = EMPTY
ACTION_SURFACE = READ_ONLY / GET-only
MODEL = actual
APPS = actual / NOT EXPOSED
BUILDER_APPLIED = capture actual
```

## Current proof state

```text
L1-C = PASS
R01_RETEST_1 = PASS
R03_RETEST_1 = PASS
R09_RETEST_1 = PASS
R04_RETEST_1 = FAIL / RECEIPT_ORDERING
R04_RETEST_2 = FAIL / RECEIPT_ORDERING
R04_RETEST_3 = FAIL / RECEIPT_INCOMPLETE
RETROACTIVE_PASS = NO
CURRENT_BUILDER_REAPPLY = REQUIRED
CURRENT_RUNTIME_FINGERPRINT = STALE_REVALIDATION_REQUIRED
C09 = NOT_SATISFIED
C10 = PASS / PRESERVED
C11 = NOT_ELIGIBLE
C12 = NOT_APPLICABLE_YET
CERTIFIED_FOR_ANY_PROJECT = NO
```

After reapply, retest only `R04_RETEST_4` unless another material configuration change invalidates additional proof.
