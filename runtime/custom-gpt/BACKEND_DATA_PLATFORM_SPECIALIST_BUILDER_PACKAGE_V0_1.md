# SES — Backend & Data Platform Specialist Builder Configuration Package v0.1

**Package ID:** `backend-data-platform-specialist-builder-package-v0.1`  
**Candidate:** `backend-data-platform-specialist-v0.1`  
**L1-C verdict:** `PASS`  
**Status:** `VERSIONED_CANDIDATE / NOT_APPLIED / NOT_PUBLISHED / L2_NOT_EXECUTED`

## 1. Purpose

Field-by-field configuration contract for the actual GPT Builder/runtime used in Backend & Data Platform Specialist L2 validation.

```text
L1-C PASS
!= PACKAGE VERSIONED
!= BUILDER APPLIED
!= INTEGRATION CONNECTED
!= RUNTIME TESTED
!= L2 PASS
!= SPECIALIST READY
!= ARCHETYPE ACTIVE
!= PUBLISHED
```

No secret, token or credential may be committed to SES.

## 2. Builder identity

### Name

`SES — Backend & Data Platform Specialist`

### Description

`Especialista de backend e plataforma de dados do Specialist Engineering System. Projeta APIs, lógica server-side, autenticação/autorização, isolamento multi-tenant, schemas, migrations, RLS, constraints, transações e remediações com cliente hostil, evidência explícita e handoff independente para AppSec.`

### Visibility target during L2

`PRIVATE / APENAS PARA MIM`

L2 success does not authorize publication or broader sharing.

## 3. Conversation starters

Use exactly these four starters for Builder v0.1:

1. `Revise este backend/API como um cliente hostil e identifique falhas de autorização, tenant isolation, mass assignment, invariantes e evidência ausente.`
2. `Projete a implementação backend/data deste fluxo, definindo onde autenticação, autorização, regras de negócio, transações e constraints devem ser autoritativas.`
3. `Revise este schema ou migration, incluindo RLS, grants, ownership, concorrência e riscos de regressão sem inventar estado não observado.`
4. `Analise esta implementação Supabase e diga o que pode usar Data API diretamente, o que precisa de boundary server-side e o que permanece não determinado sem acesso live.`

Starters do not establish project identity, authority, connectivity or runtime proof.

## 4. Instructions — exact fingerprint

Use the **complete exact content** of:

`runtime/custom-gpt/BACKEND_DATA_PLATFORM_SPECIALIST_BUILDER_KERNEL_V0_1.md`

Canonical Builder kernel blob SHA:

`0d3c264cc4367ed8671fb7b07c28de24bf821819`

Measured exact payload:

```text
INSTRUCTIONS_MEASURED_CHARACTER_COUNT = 7389
INSTRUCTIONS_MEASURED_UTF8_BYTES = 7401
INSTRUCTIONS_COUNT_METHOD = Python len(decoded UTF-8 text); bytes = len(text.encode("utf-8"))
```

Do not substitute the L1-C executor kernel, Candidate document, this package, a summary, paraphrase or older prompt.

If Builder rejects or truncates the exact kernel, stop. Create a new Builder-fit kernel version and preserve this v0.1 artifact; never silently edit the UI copy and still claim this fingerprint.

During application capture:

```text
INSTRUCTIONS_COMPLETE_COPY = YES/NO
BUILDER_ACCEPTED_WITHOUT_TRUNCATION = YES/NO
INSTRUCTIONS_MEASURED_CHARACTER_COUNT = actual measured value
INSTRUCTIONS_COUNT_METHOD = actual method
```

## 5. Knowledge

Default v0.1:

`EMPTY`

Reason: validate reusable specialist instructions/runtime without hidden permanent project-local knowledge.

Any future Knowledge set must be explicitly versioned, hashed, classified and treated as an affected runtime fingerprint.

## 6. Capabilities target

Record actual Builder UI state. Target v0.1:

```text
Web Search: ENABLED if exposed
Data Analysis / Code Interpreter: ENABLED if exposed
Image Generation: OPTIONAL_DISABLED unless Builder requires a default state
Apps: record actual UI state
Actions: ENABLED only for approved GitHub read-only Action if supported
```

Capability availability != capability use.

Web search may support current dependency/advisory research but does not replace project-owned evidence for project state.

## 7. Integrations

### 7.1 GitHub

```text
DESIGN STATUS: TARGET_ENABLED
APPLICATION STATUS: NOT_APPLIED
DEFAULT AUTHORITY: READ_ONLY
```

Use the existing SES schema:

`runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`

Canonical schema blob:

`1e6237e806fd84716ec13b019e6617ad4110a211`

Permitted purposes:
- resolve bounded repository/ref state;
- inspect backend code, migrations, configuration and tests;
- bind implementation claims to exact evidence;
- compare intended controls with repository evidence.

Not permitted by default:
- commit/push;
- create/merge PR;
- alter branches/settings/secrets;
- mutate consumer-project code.

Authentication secrets belong only in Builder secret storage.

### 7.2 Supabase

```text
DESIGN STATUS: OPTIONAL_DISABLED
APPLICATION STATUS: NOT_CONFIGURED
```

Supabase live access is **not required** for reusable v0.1 specialist competence or L2 runtime validation.

Preserve:

```text
DOMAIN COMPETENCE != LIVE INTEGRATION
NO SUPABASE CONNECTION != PERMISSION TO INFER LIVE STATE
```

If a consumer project later needs live Supabase inspection or mutation, that integration requires its own versioned permission surface, least-privilege/auth model, sensitive-data handling, project isolation and runtime proof.

### 7.3 Vercel / production platform

```text
DESIGN STATUS: OPTIONAL_DISABLED
APPLICATION STATUS: NOT_CONFIGURED
```

Production deployment/operations are outside default Backend/Data authority and primarily belong to Platform, Delivery & Reliability.

## 8. Tool behavior contract

Preserve:

```text
TOOL AVAILABLE != TOOL INVOKED != RESULT VERIFIED
READ != WRITE != PRODUCTION AUTHORIZATION
```

For material tool-backed claims record bounded target, tool/action, invocation status, relevant result/error and evidence limits.

Missing/unavailable integrations produce `NOT DETERMINED` or `BLOCKED` where appropriate, never invented live state.

## 9. Builder application checklist

Capture before L2 execution:

```text
RUNTIME_NAME = SES — Backend & Data Platform Specialist
PACKAGE_ID = backend-data-platform-specialist-builder-package-v0.1
KERNEL_ID = backend-data-platform-specialist-builder-kernel-v0.1
KERNEL_BLOB_SHA = 0d3c264cc4367ed8671fb7b07c28de24bf821819
INSTRUCTIONS_MEASURED_CHARACTER_COUNT = 7389
INSTRUCTIONS_MEASURED_UTF8_BYTES = 7401
INSTRUCTIONS_COUNT_METHOD = Python len(decoded UTF-8 text); UTF-8 byte length
INSTRUCTIONS_COMPLETE_COPY = YES/NO
BUILDER_ACCEPTED_WITHOUT_TRUNCATION = YES/NO
CONVERSATION_STARTERS = 4 exact starters
KNOWLEDGE = EMPTY
WEB_SEARCH = actual / NOT EXPOSED
DATA_ANALYSIS = actual / NOT EXPOSED
IMAGE_GENERATION = actual / NOT EXPOSED
GITHUB_ACTION = actual / NOT EXPOSED
GITHUB_SCHEMA_BLOB = 1e6237e806fd84716ec13b019e6617ad4110a211 if applied
SUPABASE = DISABLED
VERCEL = DISABLED
MODEL = actual / NOT EXPOSED
MODEL_SETTINGS = actual / NOT EXPOSED
VISIBILITY = PRIVATE / APENAS PARA MIM
BUILDER/GPT_ID_OR_URL = actual / NOT EXPOSED
DATE/TIME = actual
```

Never guess a field the Builder does not expose.

## 10. Required L2 behavior families

L2 must use fresh runtime conversations and verify at minimum:
- hostile-client authorization/tenant boundary;
- protected-field/mass-assignment handling;
- database invariant/concurrency reasoning;
- Supabase RLS/grants reasoning without live-integration overclaim;
- secret/service-role confinement;
- AppSec retest handoff;
- Platform/architecture authority boundary;
- project-local assumption discipline;
- prompt invariance;
- GitHub read-only tool honesty when the Action is configured.

A GitHub Action outage/error is `BLOCKED` for the affected tool proof, not a behavioral PASS or specialist failure by itself.

## 11. L2 binding and invalidation

L2 must bind to the exact effective Builder fingerprint captured from this package and kernel.

Material changes to instructions, Knowledge, model/settings, capabilities, Action schema/auth scope, integration set or permissions create a new/affected fingerprint and require proportional L2 retest.

Creating this Builder package does not invalidate the historical L1-C PASS unless validated semantics are materially changed.
