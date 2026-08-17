# SES — SaaS Architect Builder Configuration Package v0.1

**Package ID:** `saas-architect-builder-package-v0.1`  
**Certification subject:** `saas-architect / builder-fit-v0.1`  
**Status:** `VERSIONED_CANDIDATE / NOT_APPLIED / L1C_NOT_ESTABLISHED / L2_NOT_EXECUTED`

## 1. Purpose

Define the complete field-by-field Builder configuration for the current Builder-fit SaaS Architect certification subject.

This package closes only the versioned-package requirement when canonical. It does not prove external Builder application or runtime behavior.

```text
PACKAGE_VERSIONED
!= BUILDER_APPLIED
!= RUNTIME_FINGERPRINT_CAPTURED
!= L1-C PASS
!= L2 PASS
!= READY
!= CERTIFIED_FOR_ANY_PROJECT
```

Historical v0.1 runtime evidence remains historical and bound to its original fingerprint.

## 2. Builder identity

### Name

`SES — SaaS Architect`

### Description

`Arquiteto SaaS híbrido do Specialist Engineering System. Resolve o projeto live, carrega regras canônicas e executa auditoria, trade-offs e target architecture com evidência, fail-closed e isolamento entre projetos.`

### Visibility target

`PRIVATE / APENAS PARA MIM`

Publication or broader sharing is a separate decision.

## 3. Conversation starters

Use exactly these four starters:

1. `Reconstrua o contexto live do projeto que eu indicar e faça um Deep Architecture Audit do fluxo especificado.`
2. `Compare a arquitetura atual deste projeto com alternativas e recomende uma target architecture com trade-offs, migração e rollback.`
3. `Audite este fluxo multi-tenant de ponta a ponta: identidade → autorização → tenant → persistência → side effects.`
4. `Revalide uma decisão arquitetural atual usando evidência live e diga o que mudou, o que continua válido e a próxima ação segura.`

Starters are UX only. They do not establish project identity, readiness, authority or runtime proof.

The retired interaction is prohibited:

```text
# CLIQUE PARA INICIAR
→ numbered project menu
→ numeric selection
→ PROJECT_SELECTED
→ WAIT FOR TASK
→ cross-turn resume
```

## 4. Instructions — exact fingerprint source

Use the complete exact content of:

`runtime/custom-gpt/SAAS_ARCHITECT_BUILDER_KERNEL.md`

Canonical kernel blob SHA at package creation baseline:

`5c57fb8f0bd558c2e9ebeee26add399a4308e077`

Measured repository payload recorded by the canonical Builder profile:

```text
INSTRUCTIONS_MEASURED_CHARACTER_COUNT = 6182 Unicode code points
INSTRUCTIONS_MEASURED_UTF8_BYTES = 6236
INSTRUCTIONS_COUNT_METHOD = Unicode code-point count of decoded repository text; UTF-8 byte size from repository object
SES_OPERATIONAL_BUDGET = <= 7500 characters
BUILDER_INSTRUCTIONS_HARD_LIMIT = <= 8000 characters
```

Do not substitute:
- `SAAS_ARCHITECT_BUILDER_PROFILE.md`;
- this package;
- the historical `UNIVERSAL_BUILDER_KERNEL.md`;
- a path-only placeholder;
- a paraphrase;
- a silently edited/truncated Builder copy.

If Builder rejects or truncates the exact kernel, stop and version a new Builder-fit kernel. Never retain the old fingerprint claim after an unversioned UI edit.

## 5. Knowledge

Target:

`EMPTY`

Permanent project-local Knowledge is prohibited for this reusable certification subject.

Any future Knowledge set is a material fingerprint change and requires explicit versioning/classification plus proportional revalidation.

## 6. Capabilities target

Record the actual Builder UI state. Target configuration:

```text
Web Search: ENABLED
Data Analysis / Code Interpreter: ENABLED
Image Generation: DISABLED
Apps: record actual Builder UI state
Actions: ENABLED for approved GitHub READ_ONLY Action
```

Capability availability does not prove invocation or result verification.

## 7. GitHub integration

Use:

`runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`

Expected schema blob:

`1e6237e806fd84716ec13b019e6617ad4110a211`

Default authority:

`READ_ONLY / GET-only`

Authentication:

```text
Type: API key
Mode: Bearer
Secret: Builder secret storage only / never committed
```

Permitted purposes include live SES/project ref resolution and bounded read-only evidence retrieval.

The package does not authorize repository mutation, consumer-project mutation, deployment or production change.

## 8. Tool behavior contract

Preserve:

```text
TOOL AVAILABLE != TOOL INVOKED != RESULT VERIFIED
TOOL CAPABILITY != AUTHORIZATION
READ != WRITE
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
```

A runtime tool error blocks only the affected proof. It must not be converted into PASS, FAIL of unrelated competence, or invented evidence.

## 9. Runtime loading chain

For project-specific material work:

`SES main → docs/bootstrap/INDEX.md → archetypes/REGISTRY.md → saas-architect archetype → applicable Core protocols → explicit project resolution → Project Adapter → consumer project bootstrap/local specialist → material evidence → task-bound Context Readiness Receipt → bounded architecture work`.

```text
ARCHETYPE_RESOLVED != PROJECT_CONTEXT_READY
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
```

## 10. Builder application checklist

Capture before current L2 execution:

```text
RUNTIME_NAME = SES — SaaS Architect
PACKAGE_ID = saas-architect-builder-package-v0.1
KERNEL_PATH = runtime/custom-gpt/SAAS_ARCHITECT_BUILDER_KERNEL.md
KERNEL_BLOB_SHA = 5c57fb8f0bd558c2e9ebeee26add399a4308e077
INSTRUCTIONS_MEASURED_CHARACTER_COUNT = 6182
INSTRUCTIONS_MEASURED_UTF8_BYTES = 6236
INSTRUCTIONS_COMPLETE_COPY = YES/NO
BUILDER_ACCEPTED_WITHOUT_TRUNCATION = YES/NO
CONVERSATION_STARTERS = 4 exact starters
SINGLE_STARTER_SELECTION_FLOW = DISABLED
KNOWLEDGE = EMPTY
WEB_SEARCH = actual / NOT EXPOSED
DATA_ANALYSIS = actual / NOT EXPOSED
IMAGE_GENERATION = actual / NOT EXPOSED
APPS = actual / NOT EXPOSED
GITHUB_ACTION = actual / NOT EXPOSED
GITHUB_ACTION_SCHEMA_BLOB = actual / NOT EXPOSED
MODEL = actual / NOT EXPOSED
MODEL_SETTINGS = actual / NOT EXPOSED
VISIBILITY = PRIVATE / APENAS PARA MIM
BUILDER/GPT_ID_OR_URL = actual / NOT EXPOSED
EXECUTION_DATE = actual
```

Never guess a Builder field that is not exposed.

## 11. Current proof requirements

Before `CERTIFIED_FOR_ANY_PROJECT = YES`, the current certification subject still requires, at minimum:

- canonical SaaS Architect L1-C PASS;
- prompt invariance PASS;
- generic baseline/non-regression PASS;
- actual Builder application evidence;
- current runtime fingerprint capture;
- proportional current L2/runtime/tool proof;
- readiness evaluation PASS;
- applicable user-authorized READY;
- archetype-resolution/bootstrap/project-local-leakage obligations satisfied;
- no unresolved hard blocker.

Historical T01–T29 PASS may inform fixture selection and preserve historical claims, but it does not transfer runtime PASS to this package/kernel fingerprint.

## 12. Invalidation

Material changes to kernel, package fields, Knowledge, model/settings, capabilities, Action schema/auth scope, integration set/permissions or relevant platform behavior invalidate only affected proof obligations and require proportional revalidation.

```text
HISTORICAL_PASS != CURRENT_CERTIFICATION
NO_MATERIAL_CHANGE -> NO_REAUDIT_LOOP
```