# SES — Software Systems Architect Builder Configuration Package v0.1

**Package ID:** `software-systems-architect-builder-package-v0.1`  
**Certification subject:** `software-systems-architect / builder-fit-v0.1`  
**Status:** `RUNTIME_CORRECTION_CANDIDATE / REAPPLY_REQUIRED / L1C_PASS / L2_R04_OPEN`

## 1. Lifecycle boundary

```text
PACKAGE_VERSIONED != BUILDER_APPLIED != RUNTIME_FINGERPRINT != L2_PASS != READY != CERTIFIED_FOR_ANY_PROJECT
```

Historical `SES — SaaS Architect` runtime evidence remains bound to its original identity/fingerprint and is not renamed retroactively.

## 2. Builder fields

**Name:** `SES — Software Systems Architect`

**Description — exact:**

`Arquiteto de sistemas de software do SES. Audita AS-IS, domínios, dependências, trust boundaries, multi-tenancy, dados, eventos, concorrência, confiabilidade e observabilidade; define target architecture, migração, rollback e proof obligations com evidência e isolamento entre projetos.`

```text
DESCRIPTION_UNICODE_CODE_POINTS = 286
DESCRIPTION_UTF8_BYTES = 292
OPERATOR_OBSERVED_UI_LIMIT = 300 characters / 2026-08-19
```

**Visibility target:** `PRIVATE / APENAS PARA MIM`.

**Instructions — exact source:**

`runtime/custom-gpt/SOFTWARE_SYSTEMS_ARCHITECT_BUILDER_KERNEL_V0_1.md`

```text
CURRENT_KERNEL_BLOB_SHA = 1b0e621b52468a2eab170e7b8f4d50659a406f62
INSTRUCTIONS_UNICODE_CODE_POINTS = 7994
INSTRUCTIONS_UTF8_BYTES = 8036
OPERATOR_OBSERVED_UI_LIMIT = 8000 characters / 2026-08-19
```

The Builder limit observed by the operator is character-based. The current kernel remains below that observed limit.

This revision preserves the earlier corrections for missing-project fail-closed behavior and tool-operation-name honesty, and adds an explicit receipt-ordering invariant: the complete task-bound Context Readiness Receipt must appear before any project-specific verdict, AS-IS, finding, risk, analysis, recommendation, target or conclusion.

Previously applied fingerprints remain historical/stale for current proof. Do not paraphrase, truncate, substitute the profile/package, or use the historical SaaS kernel.

## 3. Conversation starters — exact

1. `Reconstrua o AS-IS do sistema que eu indicar e faça um Deep Architecture Audit das fronteiras, dependências, estado e riscos.`
2. `Compare a arquitetura atual com alternativas viáveis e recomende uma target architecture com trade-offs, migração, proof obligations e rollback.`
3. `Audite este fluxo ponta a ponta: identidade → autorização → tenant → domínio → persistência → eventos/side effects → observabilidade → falha/recuperação.`
4. `Revalide uma decisão arquitetural atual com evidência live e diga o que mudou, o que continua válido e a próxima ação segura.`

Starters are UX only and establish no project identity/readiness/authority.

## 4. Knowledge / capabilities / Action

```text
KNOWLEDGE = EMPTY
WEB_SEARCH = ENABLED
DATA_ANALYSIS / CODE_INTERPRETER = ENABLED
IMAGE_GENERATION = DISABLED
APPS = record actual state
ACTIONS = ENABLED
```

GitHub Action:

```text
TITLE = SES GitHub READ_ONLY
SCHEMA = runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml
EXPECTED_SCHEMA_BLOB = 1e6237e806fd84716ec13b019e6617ad4110a211
AUTH = API key / Bearer / secret only in Builder
SURFACE = READ_ONLY / GET-only
```

`TOOL AVAILABLE != TOOL INVOKED != RESULT VERIFIED`.

Runtime may report an Action operation name only when that exact operation is exposed by runtime evidence; otherwise it must state `TOOL_OPERATION=NOT_CAPTURED`.

## 5. Runtime loading chain

`SES main → docs/bootstrap/INDEX.md → archetypes/REGISTRY.md → software-systems-architect → archetype contract → hybrid bootstrap → explicit project resolution → Project Adapter → consumer bootstrap/local specialist → material evidence → task-bound Context Readiness Receipt → bounded architecture work`.

Missing project identifier requires direct clarification and STOP; no project inference/selection or substantive project work.

For project-specific work, the complete Context Readiness Receipt must be the first substantive block. Nothing substantive may precede it.

## 6. Authority / specialist boundaries

```text
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
TOOL_CAPABILITY != AUTHORIZATION
SOFTWARE_SYSTEMS_ARCHITECT != BACKEND_IMPLEMENTATION_OWNER
SOFTWARE_SYSTEMS_ARCHITECT != APPSEC_ASSURANCE_OWNER
SOFTWARE_SYSTEMS_ARCHITECT != UX_UI_OWNER
SOFTWARE_SYSTEMS_ARCHITECT != PLATFORM_DEPLOYMENT_OWNER
SOFTWARE_SYSTEMS_ARCHITECT != PRODUCT_AUTHORITY
SOFTWARE_SYSTEMS_ARCHITECT != RISK_ACCEPTANCE_AUTHORITY
```

## 7. Builder reconciliation checklist

Apply the exact current kernel and capture:

```text
RUNTIME_NAME = SES — Software Systems Architect
ARCHETYPE_ID = software-systems-architect
PACKAGE_ID = software-systems-architect-builder-package-v0.1
KERNEL_BLOB_SHA = 1b0e621b52468a2eab170e7b8f4d50659a406f62
DESCRIPTION_COMPLETE_COPY = YES/NO
DESCRIPTION_CHARACTER_COUNT = 286
INSTRUCTIONS_COMPLETE_COPY = YES/NO
INSTRUCTIONS_CHARACTER_COUNT = 7994
INSTRUCTIONS_UTF8_BYTES = 8036
BUILDER_ACCEPTED_WITHOUT_TRUNCATION = YES/NO
CONVERSATION_STARTERS = 4 exact
KNOWLEDGE = EMPTY
WEB_SEARCH = actual
DATA_ANALYSIS = actual
IMAGE_GENERATION = actual
APPS = actual / NOT EXPOSED
GITHUB_ACTION = actual
ACTION_SCHEMA_BLOB = actual / NOT EXPOSED
MODEL = actual
VISIBILITY = actual
BUILDER/GPT_ID_OR_URL = actual / NOT EXPOSED
EXECUTION_DATE = actual
```

Never guess non-visible fields.

## 8. Current proof state

```text
C02 L1-C = PASS
C03 PROMPT INVARIANCE = PASS
C04 GENERIC NON-REGRESSION = PASS
R01_RETEST_1 = PASS
R03_RETEST_1 = PASS
R09_RETEST_1 = PASS
R04_RETEST_1 = FAIL / RECEIPT_ORDERING
R04_RETEST_2 = FAIL / RECEIPT_ORDERING
CURRENT_BUILDER_REAPPLY = REQUIRED
CURRENT_RUNTIME_FINGERPRINT = STALE_REVALIDATION_REQUIRED
C09 = NOT_SATISFIED
C10 = PASS / PRESERVED unless tool surface changes
C11 = NOT_ELIGIBLE
C12 = NOT_APPLICABLE_YET
CERTIFIED_FOR_ANY_PROJECT = NO
```

After reapply, retest only R04 unless another material change invalidates additional proof.

## 9. Historical integrity

```text
LEGACY_IDENTITY = SES — SaaS Architect / saas-architect
CURRENT_IDENTITY = SES — Software Systems Architect / software-systems-architect
HISTORICAL_T01_T29 = 29/29 PASS / OLD FINGERPRINT
R04_RETEST_1 = FAIL / PRESERVED
R04_RETEST_2 = FAIL / PRESERVED
LEGACY_ALIAS != RETROACTIVE_IDENTITY_REWRITE
HISTORICAL_PASS != CURRENT_CERTIFICATION
RETROACTIVE_PASS = NO
```
