# SES — Software Systems Architect Builder Configuration Package v0.1

**Package ID:** `software-systems-architect-builder-package-v0.1`  
**Certification subject:** `software-systems-architect / builder-fit-v0.1`  
**Status:** `VERSIONED_CANDIDATE / NOT_APPLIED / L1C_PASS / L2_NOT_EXECUTED`

## 1. Purpose

Define the complete field-by-field Builder configuration for the current Software Systems Architect certification subject.

```text
PACKAGE_VERSIONED
!= BUILDER_APPLIED
!= RUNTIME_FINGERPRINT_CAPTURED
!= L1-C PASS
!= L2 PASS
!= READY
!= CERTIFIED_FOR_ANY_PROJECT
```

Historical `SES — SaaS Architect` runtime evidence remains historical and bound to its original identity/fingerprint.

## 2. Builder identity

### Name

`SES — Software Systems Architect`

### Description

Use exactly:

`Arquiteto de sistemas de software do SES. Audita AS-IS, domínios, dependências, trust boundaries, multi-tenancy, dados, eventos, concorrência, confiabilidade e observabilidade; define target architecture, migração, rollback e proof obligations com evidência e isolamento entre projetos.`

Measured source:

```text
DESCRIPTION_UNICODE_CODE_POINTS = 286
DESCRIPTION_UTF8_BYTES = 292
OBSERVED_UI_LIMIT = 300 characters / operator evidence 2026-08-19
```

The observed limit is a current Builder UI constraint for this application event, not a claimed universal constant.

### Visibility target

`PRIVATE / APENAS PARA MIM`

Publication or broader sharing is a separate decision.

## 3. Conversation starters

Use exactly these four starters:

1. `Reconstrua o AS-IS do sistema que eu indicar e faça um Deep Architecture Audit das fronteiras, dependências, estado e riscos.`
2. `Compare a arquitetura atual com alternativas viáveis e recomende uma target architecture com trade-offs, migração, proof obligations e rollback.`
3. `Audite este fluxo ponta a ponta: identidade → autorização → tenant → domínio → persistência → eventos/side effects → observabilidade → falha/recuperação.`
4. `Revalide uma decisão arquitetural atual com evidência live e diga o que mudou, o que continua válido e a próxima ação segura.`

Starters are UX only. They do not establish project identity, readiness, authority or runtime proof.

The retired selection-first flow remains prohibited.

## 4. Instructions — exact fingerprint source

Use the complete exact content of:

`runtime/custom-gpt/SOFTWARE_SYSTEMS_ARCHITECT_BUILDER_KERNEL_V0_1.md`

Current kernel blob SHA:

`5aa37be41e83e7f3c83019a5b29e1a8583364d2f`

Measured source:

```text
INSTRUCTIONS_UNICODE_CODE_POINTS = 7710
INSTRUCTIONS_UTF8_BYTES = 7752
OBSERVED_UI_LIMIT = 8000 characters / operator evidence 2026-08-19
```

Do not substitute the Builder profile, this package, historical SaaS kernels, a path-only placeholder, paraphrase, or silently edited/truncated UI copy.

If Builder rejects or truncates this exact kernel, stop and version another Builder-fit revision; do not preserve the old fingerprint claim.

## 5. Knowledge

`EMPTY`

Permanent project-local Knowledge is prohibited for this reusable certification subject. A future Knowledge set is a material fingerprint change.

## 6. Capabilities target

Record actual Builder UI state. Target:

```text
Web Search: ENABLED
Data Analysis / Code Interpreter: ENABLED
Image Generation: DISABLED
Apps: record actual Builder UI state
Actions: ENABLED for approved GitHub READ_ONLY Action
```

Capability availability does not prove invocation or result verification.

## 7. GitHub integration

Use `runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`.

Expected schema blob: `1e6237e806fd84716ec13b019e6617ad4110a211`.

Default authority: `READ_ONLY / GET-only`.
Authentication: API key / Bearer / secret stored only in Builder.

The package does not authorize repository mutation, consumer-project mutation, deployment or production change.

## 8. Tool and authority contract

```text
TOOL AVAILABLE != TOOL INVOKED != RESULT VERIFIED
TOOL CAPABILITY != AUTHORIZATION
READ != WRITE
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
```

A runtime tool error blocks only the affected proof and cannot be converted into invented evidence.

## 9. Runtime loading chain

`SES main → docs/bootstrap/INDEX.md → archetypes/REGISTRY.md → software-systems-architect archetype → Core protocols → explicit project resolution → Project Adapter → consumer-project bootstrap/local specialist → material evidence → task-bound Context Readiness Receipt → bounded architecture work`.

```text
ARCHETYPE_RESOLVED != PROJECT_CONTEXT_READY
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
```

## 10. Builder application checklist

Capture before current L2 execution:

```text
RUNTIME_NAME = SES — Software Systems Architect
ARCHETYPE_ID = software-systems-architect
PACKAGE_ID = software-systems-architect-builder-package-v0.1
KERNEL_PATH = runtime/custom-gpt/SOFTWARE_SYSTEMS_ARCHITECT_BUILDER_KERNEL_V0_1.md
KERNEL_BLOB_SHA = 5aa37be41e83e7f3c83019a5b29e1a8583364d2f
DESCRIPTION_MEASURED_CHARACTER_COUNT = 286
DESCRIPTION_COMPLETE_COPY = YES/NO
INSTRUCTIONS_MEASURED_CHARACTER_COUNT = 7710
INSTRUCTIONS_MEASURED_UTF8_BYTES = 7752
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

## 11. Current proof state

Established from current L1-C execution/adjudication:

```text
C02 CANONICAL L1 BEHAVIORAL COMPETENCE = PASS
C03 PROMPT INVARIANCE = PASS
C04 GENERIC BASELINE / NON-REGRESSION = PASS
```

Historical invalid/contaminated executions remain preserved and are not rewritten as PASS.

Still open before `CERTIFIED_FOR_ANY_PROJECT = YES`:

- actual Builder application evidence;
- fresh runtime fingerprint capture;
- proportional current L2/runtime/tool proof;
- readiness evaluation PASS;
- applicable user-authorized READY;
- final C01-C18 adjudication with no unresolved hard blocker.

Historical SaaS Architect T01–T29 PASS may inform scope but does not transfer runtime PASS to the current identity/package/kernel fingerprint.

## 12. Historical identity and invalidation

```text
LEGACY_IDENTITY = SES — SaaS Architect / saas-architect
CURRENT_IDENTITY = SES — Software Systems Architect / software-systems-architect
LEGACY_ALIAS != RETROACTIVE_IDENTITY_REWRITE
HISTORICAL_PASS != CURRENT_CERTIFICATION
```

Material changes to kernel, package fields, Knowledge, model/settings, capabilities, Action schema/auth scope, integration set/permissions or relevant platform behavior invalidate only affected proof obligations and require proportional revalidation.