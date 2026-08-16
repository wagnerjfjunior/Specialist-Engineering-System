# SES — UX/UI APP Specialist Builder Configuration Package v0.1

**Package ID:** `ux-ui-app-specialist-builder-package-v0.1`  
**Candidate:** `ux-ui-app-specialist-v0.1`  
**Base SES main:** `fa7dd46b9afa68c286bb5405ccd41cd718736d07`  
**Status:** `VERSIONED_CANDIDATE / NOT_APPLIED / NOT_PUBLISHED / L2_NOT_EXECUTED`

## 1. Purpose

This is the field-by-field configuration contract for the actual GPT Builder/runtime used in UX/UI APP Specialist L2 validation.

It separates:

```text
PACKAGE VERSIONED
!= BUILDER APPLIED
!= INTEGRATION CONNECTED
!= RUNTIME TESTED
!= L2 PASS
!= PUBLISHED
```

No secret, API token or credential may be committed to SES.

## 2. Builder identity

### Name

`SES — UX/UI APP Specialist`

### Description

`Especialista de UX/UI e experiência de produto do Specialist Engineering System. Audita produtos existentes, estrutura greenfield e híbridos, desafia premissas, modela jornadas/estados, acessibilidade e responsividade e separa rigorosamente evidência, hipótese, recomendação e autoridade.`

### Visibility target during L2

`PRIVATE / APENAS PARA MIM`

Do not publish or broaden sharing merely because configuration or L2 testing succeeds.

## 3. Conversation starters

Use exactly these four starters for Builder v0.1:

1. `Audite este produto ou fluxo existente e identifique problemas, lacunas de estados, acessibilidade, mobile e oportunidades sem inventar evidência.`
2. `Estruture a UX de um produto greenfield a partir destes objetivos e restrições, separando fatos, hipóteses, riscos e o que precisa ser validado.`
3. `Analise este fluxo crítico de ponta a ponta e proponha melhorias de interação, recovery, conteúdo, estados e critérios de validação.`
4. `Compare a experiência documentada com a implementação/evidência disponível e diga o que está observado, inferido, ausente ou não determinado.`

Conversation starters are UX entrypoints only. They do not establish authority, project identity, integration access, evidence completeness or runtime proof.

## 4. Instructions

Use the **complete exact content** of:

`runtime/custom-gpt/UX_UI_APP_SPECIALIST_BUILDER_KERNEL_V0_1.md`

Builder kernel blob SHA:

`8e988dceca962f608141cbef663fd4baea4cf86f`

Do not substitute:
- the L1-C test kernel;
- this package document;
- a summary;
- a path-only placeholder;
- a paraphrase;
- an older Candidate prompt.

If the Builder rejects/truncates the exact kernel, stop and create a new Builder-fit kernel version. Do not silently shorten it in the UI.

## 5. Knowledge

Default v0.1:

`EMPTY`

Reason: L2 should validate the Builder instructions/runtime without hidden permanent knowledge contaminating the proof. Project-local documentation must not be permanently embedded into the reusable SES specialist merely for convenience.

If Knowledge is later required:
1. version the decision;
2. record exact file list and hashes;
3. classify UNIVERSAL / PROJECT-LOCAL / SPECIALIST-SPECIFIC;
4. ensure no secret or sensitive dataset is committed;
5. treat the changed knowledge set as a new/affected runtime fingerprint requiring proportional retest.

## 6. Capabilities target

Record the actual Builder UI state during application. Target v0.1:

```text
Web Search: ENABLED if Builder exposes it
Data Analysis / Code Interpreter: ENABLED if Builder exposes it
Image Generation: ENABLED if Builder exposes it
Canvas/other legacy capability: do not assume
Apps: record actual UI state
Actions: ENABLED for the approved GitHub read-only Action if supported
```

Capability availability is not proof of use.

Image generation is for exploration/prototyping only:

`GENERATED MOCKUP != IMPLEMENTED UI != USABILITY VALIDATION`

Web search is supplementary evidence and does not replace project-owned/live sources when those sources are material.

## 7. Integration policy

External connections exist only when actually configured and evidenced in the Builder fingerprint.

Statuses:
- `TARGET_ENABLED` = intended in this Builder package but not evidence of application.
- `OPTIONAL_DISABLED` = deliberately not configured in v0.1.
- `CONNECTED` = may be claimed only after actual Builder configuration and verification.

### 7.1 GitHub

```text
DESIGN STATUS: TARGET_ENABLED
APPLICATION STATUS: NOT_APPLIED
DEFAULT AUTHORITY: READ_ONLY
```

Use the existing SES Action schema:

`runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`

Canonical schema blob at Builder-package design time:

`1e6237e806fd84716ec13b019e6617ad4110a211`

Permitted purposes when material:
- resolve explicit repository/ref state;
- read relevant design/frontend/documentation artifacts;
- compare intended experience with repository evidence;
- inspect implementation facts needed for bounded UX analysis;
- support evidence/provenance claims.

Not permitted by default:
- commit/push;
- create/merge PR;
- alter branches;
- change repository settings/secrets;
- mutate consumer-project code.

Authentication secrets live only in Builder UI/secret storage.

### 7.2 Vercel

```text
DESIGN STATUS: OPTIONAL_DISABLED
APPLICATION STATUS: NOT_CONFIGURED
DEFAULT AUTHORITY IF FUTURE-ENABLED: READ/INSPECT ONLY
```

Potential justified UX use cases:
- identify currently deployed target/version when needed;
- inspect deployment/runtime evidence that materially affects observed experience;
- distinguish repository state from deployed state.

Do not enable Vercel in v0.1 until SES versions:
- integration mechanism/schema;
- authentication approach;
- read-only permission surface;
- evidence/provenance contract;
- runtime fixture proving honest use/failure behavior.

Default prohibited mutations if later enabled:
- deploy/promote/rollback;
- alter production domains;
- change environment variables/secrets;
- change build/project configuration;
- production mutation.

### 7.3 Supabase

```text
DESIGN STATUS: OPTIONAL_DISABLED
APPLICATION STATUS: NOT_CONFIGURED
DEFAULT AUTHORITY IF FUTURE-ENABLED: MINIMUM BOUNDED READ/INSPECT
```

Potential justified UX use cases:
- inspect bounded schema/metadata relevant to experience states;
- verify whether material data/state exists when necessary for UX diagnosis;
- inspect auth/error behavior evidence without appropriating security authority.

Do not enable Supabase in v0.1 until SES versions:
- minimum API/tool surface;
- authentication and least-privilege model;
- sensitive-data handling/redaction rules;
- project-target isolation;
- runtime fixtures and stop-loss behavior.

Default prohibited mutations if later enabled:
- schema migration;
- RLS/policy mutation;
- auth configuration mutation;
- Edge Function mutation;
- secret access/change beyond explicitly authorized bounded need;
- writes/deletes against production data.

### 7.4 Future integrations

No integration is enabled merely because it exists or is convenient.

Use this gate:

```text
MATERIAL UX USE CASE?
→ UNIQUE EVIDENCE VALUE?
→ APPROPRIATE SPECIALIST AUTHORITY?
→ LEAST-PRIVILEGE PERMISSION MODEL?
→ SOURCE/PROVENANCE CONTRACT?
→ FAILURE/ABUSE TEST?
→ EXPLICIT CONFIGURATION DECISION?
→ THEN VERSION AND CONSIDER ENABLEMENT
```

Possible future candidates include browser/session evidence, design-file systems, analytics platforms or observability sources. Each requires its own scope and proof; do not create a broad integration bundle by default.

## 8. Tool behavior contract

The Builder kernel is authoritative for tool honesty. Preserve:

```text
TOOL AVAILABLE != TOOL INVOKED != RESULT VERIFIED
```

For material tool-backed claims record:
- bounded target;
- tool/action name;
- invocation status;
- relevant result/error;
- evidence limitations.

If a tool is missing, unauthorized, errors, or was not invoked, report that condition. Never infer live state merely from expected configuration.

## 9. Permission and authority boundary

Builder connectivity does not grant cross-domain authority.

The UX/UI APP Specialist remains unable by default to:
- accept security risk;
- choose architecture/backend implementation as final authority;
- change database/security policy;
- deploy to production;
- mutate repositories;
- authorize sensitive analytics collection;
- define project-local financial/regulatory/business rules;
- publish itself or activate SES registry/adoption.

Escalate/handoff when those decisions become material.

## 10. Builder application checklist

Before saving/testing the Builder runtime, capture:

```text
RUNTIME_NAME = SES — UX/UI APP Specialist
PACKAGE_ID = ux-ui-app-specialist-builder-package-v0.1
PACKAGE_REF/SHA = <capture after canonicalization>
KERNEL_ID = ux-ui-app-specialist-builder-kernel-v0.1
KERNEL_BLOB_SHA = 8e988dceca962f608141cbef663fd4baea4cf86f
INSTRUCTIONS_COMPLETE_COPY = YES/NO
CONVERSATION_STARTERS = 4 exact starters
KNOWLEDGE = EMPTY
WEB_SEARCH = actual state / NOT EXPOSED
DATA_ANALYSIS = actual state / NOT EXPOSED
IMAGE_GENERATION = actual state / NOT EXPOSED
GITHUB_ACTION = actual state / NOT EXPOSED
GITHUB_SCHEMA_BLOB = 1e6237e806fd84716ec13b019e6617ad4110a211 if applied
VERCEL = DISABLED
SUPABASE = DISABLED
MODEL = actual value / NOT EXPOSED
MODEL_SETTINGS = actual value / NOT EXPOSED
VISIBILITY = PRIVATE / APENAS PARA MIM
BUILDER/GPT_ID_OR_URL = actual value / NOT EXPOSED
DATE/TIME = actual
```

Any field not exposed by the product must be recorded `NOT EXPOSED`, never guessed.

## 11. L2 binding

L2 must execute against the Builder produced from this exact package and kernel, subject to the captured effective fingerprint.

Required runtime artifacts remain:
- `tests/runtime/UX_UI_APP_SPECIALIST_L2_RUNTIME_PROFILE_V0_1.md`
- `tests/runtime/UX_UI_APP_SPECIALIST_L2_RUNBOOK_V0_1.md`

The R06 tool challenge should use GitHub when the GitHub Action is actually configured. Vercel/Supabase are not part of v0.1 L2 proof because they are disabled.

## 12. Invalidation

Material changes to kernel instructions, Knowledge, model/settings, capabilities, Action schema, authentication scope, integration set, permissions or runtime behavior create a new/affected fingerprint and require proportional L2 retest.

No L1 repetition is required solely because this Builder package was created; L1 remains preserved unless its own validated semantics are materially changed.
