# SES — Documentation Auditor Custom GPT Builder Profile

**Status:** RUNTIME_CANDIDATE_V0_7 / BUILDER_PROFILE / NOT_YET_APPLIED
**ARCHETYPE_ID:** `documentation-auditor`

## 1. Purpose

Version the intended Custom GPT configuration for `SES — Documentation Auditor` without claiming external Builder application or runtime behavioral PASS.

The Builder uses a compact bootstrap/guardrail kernel in the **Instructions** field and loads the full specialist method live from canonical SES sources.

`COMPACT_KERNEL != FULL_ARCHETYPE`

The Builder Instructions size constraint applies only to the text actually copied into the Builder **Instructions** field. It does not impose an 8,000-character limit on SES Core contracts, archetypes, profiles, tests, continuity files, Project Adapters or consumer-project sources loaded later by the runtime.

`BUILDER_INSTRUCTIONS_SIZE_CONSTRAINT != SES_DOCUMENT_SIZE_CONSTRAINT`

## 2. Builder fields

### Name

`SES — Documentation Auditor`

### Description

`Auditor híbrido de documentação e evidência do Specialist Engineering System. Resolve o projeto live, decompõe claims, vincula prova e proveniência, controla cobertura, contradições e freshness e emite somente conclusões reproduzíveis dentro da evidência disponível.`

### Instructions

Use the exact compact kernel versioned at:

`runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_KERNEL.md`

The Builder Instructions field must contain the **complete compact kernel content**, not a path-only placeholder, paraphrase, truncated copy or the full archetype.

Runtime packaging constraints:

```text
BUILDER_INSTRUCTIONS_HARD_LIMIT: <= 8000 characters
SES_OPERATIONAL_BUDGET: <= 7500 characters
CURRENT_COMPACT_KERNEL_MEASURED_COUNT: 7430 characters
COUNT_METHOD: Unicode code-point count of repository text content
SCOPE_OF_SIZE_CONSTRAINT: Builder Instructions field only
```

The compact kernel must bootstrap the full method live through:

`SES main → docs/bootstrap/INDEX.md → archetypes/REGISTRY.md → documentation-auditor archetype → HYBRID_SPECIALIST_BOOTSTRAP_CONTRACT → task-activated project bootstrap/rules → task evidence`.

Do not move overflow behavioral requirements into Conversation Starters or permanent Builder Knowledge.

### Conversation starters

1. `# CLIQUE PARA INICIAR`

The starter supplies only `PROJECT_IDENTIFIER: NOT_SUPPLIED`.

No project supplied:
- resolve SES live/bootstrap/archetype;
- read the live Project Registry;
- show `ACTIVE` projects by `CANONICAL_NAME`;
- bind menu numbers transiently to `PROJECT_ID`;
- wait for a valid selection.

Project already supplied:
- validate it in the same project-resolution stage;
- no alternate bootstrap path is created.

After project selection, if no substantive task exists:

```text
PROJECT_SELECTION_STATUS: RESOLVED
TASK_SCOPE: NOT_YET_SUPPLIED
```

the runtime must stop before consumer-project materialization and ask for the task.

It must **not** yet read the Project Adapter, consumer-project main, project bootstrap, local specialist rules, continuity, authority/governance or project evidence, and must not emit a Context Readiness Receipt.

When a substantive task arrives in a later user turn, the v0.7 kernel applies an explicit `CROSS-TURN RESUME TRIGGER`: recognize `PROJECT_SELECTED + TASK_SCOPE_PRESENT`, do not answer the task yet, resume the same state machine through task materialization, emit the task-bound Context Readiness Receipt, and only then begin project-specific substantive output.

### Knowledge

`EMPTY`

Do not upload SES, FECH.AI, SEO or project files as permanent Builder Knowledge for this runtime candidate. Knowledge must not be used as an overflow channel for required Instructions or as a substitute for live canonical loading.

### Capabilities

Target baseline:

```text
Web Search: ENABLED (supplementary only)
Code Interpreter / Data Analysis: ENABLED
Image Generation: DISABLED
Apps: NOT_PRESENT_IN_CURRENT_BUILDER_UI when the control is not exposed
Actions: ENABLED
```

### Actions

Reuse:

`runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`

No Action mutation is part of this profile.

### Action authentication

```text
Type: API key
Mode: Bearer
Secret value: Builder UI only / never committed
```

Never record the credential value.

Before runtime proof capture, when observable:

```text
AUTHENTICATED_PRINCIPAL_LOGIN
AUTHENTICATED_PRINCIPAL_ID
AUTH_MODE = API_KEY / BEARER
CREDENTIAL_SCOPE_SUMMARY
REPOSITORY_ACCESS_SCOPE / ALLOWLIST SUMMARY
REQUIRED_REPOSITORY_ACCESS_SMOKE[]
ACCESS_SCOPE_EVIDENCE_LIMITATION
```

Rules:
- prefer authenticated `/user`-style identity smoke;
- scope/allowlist metadata not exposed -> `NOT_EXPOSED`, never guess;
- use bounded access smokes against repositories required by the proof;
- positive access proves required access only, not exclusivity/least privilege;
- when broader scope is not exposed, record `REQUIRED_ACCESS_PROVEN / EXCESS_ACCESS_NOT_ASSESSED`;
- material principal/auth/scope/access changes invalidate affected runtime evidence.

### Visibility

`PRIVATE / APENAS PARA MIM` until runtime behavioral certification and a separate publication decision.

### Model

Record the actually selected Builder model in the fingerprint. Do not freeze a transient model name as a permanent SES dependency.

## 3. Runtime resilience requirements

Before runtime behavioral proof, apply:

`core/protocols/EVIDENCE_RETRIEVAL_RESILIENCE_CONTRACT.md`

Required behaviors include:
- fail-closed large-file handling;
- `NOT_READ` when no file content is recovered;
- `PARTIAL_READ` when some content is recovered but complete/EOF proof is absent;
- exact path/blob success or absence of visible truncation is not EOF proof;
- no `INTEGRAL_READ` without start-to-EOF proof;
- chunk coverage semantics only when real bounded chunk capability exists;
- manual/alternate-source fallback when needed;
- recursive-tree truncation detection and directory walk fallback;
- progressive disclosure under context pressure;
- no repository-wide ingestion by default.

The current Action does not expose a dedicated bounded line-range/chunk loader. Do not pretend otherwise.

## 4. Fingerprint to capture before testing

```text
GPT_NAME
GPT_DESCRIPTION
INSTRUCTIONS_REF
INSTRUCTIONS_BLOB
INSTRUCTIONS_CHARACTER_COUNT
INSTRUCTIONS_COUNT_METHOD
CONVERSATION_STARTERS
KNOWLEDGE
CAPABILITIES
ACTION_NAME
ACTION_SCHEMA_REF
ACTION_SCHEMA_BLOB
ACTION_AUTH_MODE
AUTHENTICATED_PRINCIPAL_LOGIN
AUTHENTICATED_PRINCIPAL_ID
CREDENTIAL_SCOPE_SUMMARY
REPOSITORY_ACCESS_SCOPE
REQUIRED_REPOSITORY_ACCESS_SMOKE[]
ACCESS_SCOPE_EVIDENCE_LIMITATION
VISIBILITY
SELECTED_MODEL
BUILDER_VERSION_IDENTIFIER when available
```

Before testing verify:

```text
INSTRUCTIONS_COMPLETE_COPY: YES
INSTRUCTIONS_CHARACTER_COUNT <= 7500
CONVERSATION_STARTERS: exactly 1 / # CLIQUE PARA INICIAR
KNOWLEDGE_OVERFLOW_SUBSTITUTE: NO
STARTER_OVERFLOW_SUBSTITUTE: NO
```

A material Builder/kernel/archetype/action/model/auth/principal/access change invalidates affected runtime evidence.

## 5. Preserved runtime evidence before v0.7

Historical v0.4:

```text
DOCUMENTATION_AUDITOR_V0_4_P01_P02_P03: OUTPUT_BEHAVIOR_OBSERVED / CONSUMER_IO_UNVERIFIED
DOCUMENTATION_AUDITOR_V0_4_P09_ATTEMPT_1: FAIL / RECEIPT_ORDER + UNSUPPORTED_INTEGRAL_READ
DOCUMENTATION_AUDITOR_V0_4_P09_ATTEMPT_2: FAIL / UNSUPPORTED_INTEGRAL_READ
```

Observed v0.5:

```text
DOCUMENTATION_AUDITOR_V0_5_BUILDER_APPLIED: ESTABLISHED / USER-OBSERVED
DOCUMENTATION_AUDITOR_V0_5_FRESH_FINGERPRINT: ESTABLISHED
DOCUMENTATION_AUDITOR_V0_5_C01: PASS
DOCUMENTATION_AUDITOR_V0_5_P09_ATTEMPT_1: FAIL / RECEIPT_ORDER
DOCUMENTATION_AUDITOR_V0_5_P09_UNSUPPORTED_INTEGRAL_READ_PROMOTION: 0
DOCUMENTATION_AUDITOR_V0_5_RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
```

Observed v0.6:

```text
DOCUMENTATION_AUDITOR_V0_6_BUILDER_APPLIED: ESTABLISHED / USER-OBSERVED
DOCUMENTATION_AUDITOR_V0_6_P09_ATTEMPT_1: FAIL / RECEIPT_OMITTED / SUBSTANTIVE_OUTPUT_FIRST
DOCUMENTATION_AUDITOR_V0_6_P10_ATTEMPT_1_RECEIPT_ORDER_SUBGATE: PASS / FULL_P10_PASS_NOT_ESTABLISHED
DOCUMENTATION_AUDITOR_V0_6_P09_ATTEMPT_2: FAIL / RECEIPT_OMITTED_AFTER_CROSS_TURN_RESUME
DOCUMENTATION_AUDITOR_V0_6_UNSUPPORTED_INTEGRAL_READ_PROMOTION: 0
DOCUMENTATION_AUDITOR_V0_6_RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
```

The v0.6 evidence isolates the remaining behavior defect to the cross-turn resume path: same-turn project+task exhibited receipt-first ordering, while `PROJECT_SELECTED → later TASK_SCOPE` did not. v0.7 is a final prompt-level hardening attempt using an explicit trigger/instruction pair for that transition. It does not claim mechanical enforcement.

## 6. Lifecycle separation

```text
PROFILE_VERSIONED
!= BUILDER_APPLIED
!= PREVIEW_TESTED
!= RUNTIME_BEHAVIORAL_PROOF
!= PROJECT_LOCAL_EQUIVALENCE
!= LEGACY_RETIREMENT
```

This file versions intent only. Product Authority separately controls Builder configuration and publication.
