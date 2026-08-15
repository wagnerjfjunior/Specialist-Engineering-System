# SES — Documentation Auditor Custom GPT Builder Profile

**Status:** RUNTIME_CANDIDATE_V0_8 / STOP_LOSS_ROLLBACK_TARGET / NOT_YET_APPLIED
**ARCHETYPE_ID:** `documentation-auditor`

## 1. Purpose

Version the post-stop-loss Custom GPT configuration for `SES — Documentation Auditor`.

This target removes the abandoned single-starter / live-menu / numeric-selection / cross-turn-resume interaction while preserving the independent evidence, EOF, receipt-order, authority and anti-overclaim hardenings established through v0.6.

`PROFILE_VERSIONED != BUILDER_APPLIED != RUNTIME_BEHAVIORAL_PROOF`

The Builder uses a compact kernel in **Instructions** and loads the full specialist method live from canonical SES sources.

## 2. Builder fields

### Name

`SES — Documentation Auditor`

### Description

`Auditor híbrido de documentação e evidência do Specialist Engineering System. Resolve o projeto live, decompõe claims, vincula prova e proveniência, controla cobertura, contradições e freshness e emite somente conclusões reproduzíveis dentro da evidência disponível.`

### Instructions

Use the exact complete content of:

`runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_KERNEL.md`

Do not use a path-only placeholder, paraphrase, truncated copy or permanent Knowledge as a substitute.

Builder constraints:

```text
BUILDER_INSTRUCTIONS_HARD_LIMIT: <= 8000 characters
SES_OPERATIONAL_BUDGET: <= 7500 characters
CURRENT_COMPACT_KERNEL_MEASURED_COUNT: 6693 characters
COUNT_METHOD: Unicode code-point count of repository text content
SCOPE_OF_SIZE_CONSTRAINT: Builder Instructions field only
```

The kernel must bootstrap the full method live through:

`SES main → docs/bootstrap/INDEX.md → archetypes/REGISTRY.md → documentation-auditor archetype → applicable Core protocols → registered consumer-project bootstrap/rules when project-specific`.

### Conversation starters

Restore the universal multi-starter UX baseline:

1. `Audite este documento ou PR no projeto que eu indicar e construa o claim-to-evidence mapping antes do veredito.`
2. `Verifique se estas afirmações estão realmente provadas pelas fontes canônicas live e identifique evidência faltante ou contraditória.`
3. `Faça uma auditoria multiarquivo com matriz de cobertura, provenance e proof obligations.`
4. `Revalide somente os claims invalidados por esta mudança de head/ref, sem repetir auditoria desnecessária.`

Conversation starters are UX examples only. They do not establish project identity, readiness, configuration or authority and must not carry required kernel behavior.

The retired interaction model is **not** part of this target:

```text
# CLIQUE PARA INICIAR
→ live numbered project menu
→ numeric project selection
→ PROJECT_SELECTED
→ WAIT FOR TASK
→ cross-turn resume
```

For a project-specific task, the project identifier must be supplied in the task or obtained directly from the user. Once project + substantive task exist, resolve the project through `projects/REGISTRY.md` and continue through the canonical direct project bootstrap flow.

### Knowledge

`EMPTY`

Do not upload SES, FECH.AI, SEO or project files as permanent Builder Knowledge. Knowledge must not be an overflow channel for required Instructions or a substitute for live canonical loading.

### Capabilities

Target baseline:

```text
Web Search: ENABLED (supplementary only)
Code Interpreter / Data Analysis: ENABLED
Image Generation: DISABLED
Actions: ENABLED
Apps: record actual Builder UI state; use NOT_PRESENT_IN_CURRENT_BUILDER_UI when appropriate
```

### Actions

Reuse unchanged:

`runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`

No Action mutation is part of this rollback.

### Action authentication

```text
Type: API key
Mode: Bearer
Secret value: Builder UI only / never committed
```

Record only non-secret effective identity/access evidence when material. Never record credential values.

### Visibility

`PRIVATE / APENAS PARA MIM` until a separate publication decision.

### Model

Record the actually selected Builder model in the fingerprint. Do not freeze a transient model name as a permanent SES dependency.

## 3. Preserved independent hardenings

The post-stop-loss target preserves:

- positive start-through-EOF proof before `INTEGRAL_READ`;
- exact path/blob success or absence of visible truncation is not EOF proof;
- fail-closed large-file/tree handling;
- task-bound Context Readiness Receipt before any project-specific substantive conclusion;
- separation of normative receipt ordering from mechanical enforcement claims;
- claim-to-evidence/provenance/coverage/contradiction/freshness discipline;
- READ_ONLY default and exact mutation authorization boundaries;
- cross-project isolation;
- anti-overclaim lifecycle separation.

Load `core/protocols/EVIDENCE_RETRIEVAL_RESILIENCE_CONTRACT.md` when retrieval risk is material.

## 4. Builder fingerprint before post-merge smoke

Capture:

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
REPOSITORY_ACCESS_SCOPE / NOT_EXPOSED
REQUIRED_REPOSITORY_ACCESS_SMOKE[]
ACCESS_SCOPE_EVIDENCE_LIMITATION
VISIBILITY
SELECTED_MODEL
BUILDER_VERSION_IDENTIFIER when available
```

Before smoke execution verify:

```text
INSTRUCTIONS_COMPLETE_COPY: YES
INSTRUCTIONS_CHARACTER_COUNT = 6693
INSTRUCTIONS_CHARACTER_COUNT <= 7500
CONVERSATION_STARTERS: exactly 4 / universal set above
SINGLE_STARTER_SELECTION_FLOW: DISABLED
KNOWLEDGE: EMPTY
STARTER_OVERFLOW_SUBSTITUTE: NO
```

## 5. Historical evidence preserved

Do not rewrite prior attempts:

```text
V0_4_P09_ATTEMPT_1: FAIL / RECEIPT_ORDER + UNSUPPORTED_INTEGRAL_READ
V0_4_P09_ATTEMPT_2: FAIL / UNSUPPORTED_INTEGRAL_READ
V0_5_C01: PASS / HISTORICAL
V0_5_P09_ATTEMPT_1: FAIL / RECEIPT_ORDER
V0_5_UNSUPPORTED_INTEGRAL_READ_PROMOTION: 0
V0_6_P09_ATTEMPT_1: FAIL / RECEIPT_OMITTED / SUBSTANTIVE_OUTPUT_FIRST
V0_6_UNSUPPORTED_INTEGRAL_READ_PROMOTION: 0
V0_6_RECEIPT_MECHANICAL_ENFORCEMENT: NOT_ESTABLISHED
V0_7_CROSS_TURN_HARDENING: ABANDONED / STOP_LOSS / PR #19 NOT_MERGED
```

v0.8 is a rollback target, not proof that the external Builder is already changed and not runtime certification.

## 6. Lifecycle separation

```text
PROFILE_VERSIONED
!= BUILDER_APPLIED
!= FINGERPRINT_COMPLETE
!= POST_ROLLBACK_SMOKE
!= RUNTIME_BEHAVIORAL_PROOF
!= PROJECT_LOCAL_EQUIVALENCE
!= LEGACY_RETIREMENT
```

Product Authority separately controls external Builder configuration and publication.
