# SES — Documentation Auditor Custom GPT Builder Profile

**Status:** RUNTIME_CANDIDATE_V0_9 / PROJECT_TARGET_DISAMBIGUATION_FIX / NOT_YET_APPLIED
**ARCHETYPE_ID:** `documentation-auditor`

## 1. Purpose

Version the bounded correction for the post-stop-loss Documentation Auditor after runtime observation showed nondeterministic behavior when a substantive audit request omitted or ambiguously specified the target project.

This candidate does **not** reopen the retired single-starter/menu feature. It strengthens the opposite invariant: missing or ambiguous target identity must produce direct clarification and a hard stop before project materialization.

```text
V0_8_S02_FECHAI_DIRECT_PROJECT: PASS / OBSERVED
V0_8_S03_BLOGS_DIRECT_PROJECT: PASS / OBSERVED
V0_8_GENERIC_TARGET_SELF_SES_RESPONSE: INDETERMINATE / TEST_INPUT_TARGET_AMBIGUOUS
V0_8_RETIRED_NUMBERED_MENU_RESPONSE: FAIL / BEHAVIORAL_REGRESSION
V0_9_RUNTIME_PROOF: NOT_YET_ESTABLISHED
```

`PROFILE_VERSIONED != BUILDER_APPLIED != RUNTIME_BEHAVIORAL_PROOF`

## 2. Builder fields

### Name

`SES — Documentation Auditor`

### Description

`Auditor híbrido de documentação e evidência do Specialist Engineering System. Resolve o alvo/projeto live sem inferência, decompõe claims, vincula prova e proveniência, controla cobertura, contradições e freshness e emite somente conclusões reproduzíveis dentro da evidência disponível.`

### Instructions

Use the exact complete content of:

`runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_KERNEL.md`

Do not use a path-only placeholder, paraphrase, truncated copy or permanent Knowledge as a substitute.

Builder constraints:

```text
BUILDER_INSTRUCTIONS_HARD_LIMIT: <= 8000 characters
SES_OPERATIONAL_BUDGET: <= 7500 characters
CURRENT_COMPACT_KERNEL_MEASURED_COUNT: 7388 characters
COUNT_METHOD: Unicode code-point count of repository text content
CURRENT_KERNEL_BLOB: 6ca9e1d22d7faf0639076e5d43332b3267ec2354
```

The kernel loads the reusable target-resolution rule from:

`core/protocols/HYBRID_PROJECT_TARGET_RESOLUTION_CONTRACT.md`

and continues to use the canonical hybrid bootstrap/evidence contracts.

### Conversation starters

Keep exactly these four UX examples:

1. `Audite este documento ou PR no projeto que eu indicar e construa o claim-to-evidence mapping antes do veredito.`
2. `Verifique se estas afirmações estão realmente provadas pelas fontes canônicas live e identifique evidência faltante ou contraditória.`
3. `Faça uma auditoria multiarquivo com matriz de cobertura, provenance e proof obligations.`
4. `Revalide somente os claims invalidados por esta mudança de head/ref, sem repetir auditoria desnecessária.`

Starters do not establish target/project identity, readiness, configuration or authority.

### Knowledge

`EMPTY`

Do not upload SES or consumer-project files as permanent Knowledge.

### Capabilities

```text
Web Search: ENABLED (supplementary only)
Code Interpreter / Data Analysis: ENABLED
Image Generation: DISABLED
Actions: ENABLED
Apps: record actual Builder UI state
```

### Actions

Reuse unchanged:

`runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`

### Action authentication

```text
Type: API key
Mode: Bearer
Secret value: Builder UI only / never committed
```

### Visibility

`PRIVATE / APENAS PARA MIM` until a separate publication decision.

### Model

Record the actual selected Builder model in the fingerprint. Model changes may invalidate behavioral evidence.

## 3. Missing/ambiguous target invariant

For consumer-project work without an explicit project identifier:

```text
PROJECT_IDENTIFIER: NOT_SUPPLIED
PROJECT_RESOLUTION_STATUS: PROJECT_IDENTIFIER_REQUIRED
→ ask one direct clarification
→ STOP
```

For wording ambiguous between SES itself and a consumer project:

```text
AMBIGUOUS_SES_OR_CONSUMER_TARGET
→ ask whether SES itself or which consumer project is intended
→ STOP
```

Before clarification, the runtime must not:

- infer SES as the target;
- infer FECH.AI, Blogs/SEO or another project;
- enumerate the Project Registry unless the user explicitly asked for a list;
- generate a numbered project menu;
- create numeric project bindings;
- materialize a Project Adapter/consumer project;
- emit a project readiness receipt;
- produce substantive project findings/verdicts.

An explicit informational request to list projects may enumerate names, but list position never becomes project identity.

## 4. Preserved independent hardenings

v0.9 preserves v0.8 behavior for:

- four-starter UX and retired single-starter/menu/cross-turn feature;
- positive start-through-EOF proof before `INTEGRAL_READ`;
- exact path/blob success or absence of visible truncation is not EOF proof;
- fail-closed retrieval handling;
- task-bound Context Readiness Receipt before project-specific substantive conclusions;
- normative receipt ordering separated from mechanical-enforcement claims;
- claim-to-evidence/provenance/coverage/contradiction/freshness discipline;
- READ_ONLY default and exact mutation authorization;
- cross-project isolation;
- anti-overclaim lifecycle separation.

## 5. Required regression before resuming smoke

Execute the exact cases in:

`tests/runtime/DOCUMENTATION_AUDITOR_PROJECT_TARGET_REGRESSION.md`

Required sequence after Builder application:

```text
R01_AMBIGUOUS_TARGET_COLD_START
R02_MISSING_CONSUMER_PROJECT_ID_COLD_START
R03A_EXPLICIT_CONSUMER_TARGET
R03B_EXPLICIT_SES_TARGET
```

All four observations must pass autonomously. Do not correct the runtime during a case.

If R01 or R02 fails after v0.9 is demonstrably applied in a fresh conversation, classify:

`RUNTIME_ENFORCEMENT_GAP / PROMPT_LEVEL_FIX_STOP_LOSS`

and **do not create v0.10 merely by adding more wording**. Escalate to a different runtime/enforcement architecture or accept the limitation explicitly.

## 6. Fingerprint

Capture before regression execution:

```text
GPT_NAME
GPT_DESCRIPTION
INSTRUCTIONS_REF
INSTRUCTIONS_BLOB
INSTRUCTIONS_CHARACTER_COUNT
CONVERSATION_STARTERS
KNOWLEDGE
CAPABILITIES
ACTION_NAME
ACTION_SCHEMA_REF / BLOB
ACTION_AUTH_MODE
AUTHENTICATED_PRINCIPAL_LOGIN / ID
VISIBILITY
SELECTED_MODEL
BUILDER_VERSION_IDENTIFIER when available
```

Verify:

```text
INSTRUCTIONS_COMPLETE_COPY: YES
INSTRUCTIONS_CHARACTER_COUNT = 7388
INSTRUCTIONS_CHARACTER_COUNT <= 7500
CONVERSATION_STARTERS: exactly 4
SINGLE_STARTER_SELECTION_FLOW: DISABLED
KNOWLEDGE: EMPTY
```

## 7. Lifecycle separation

```text
PROFILE_VERSIONED
!= BUILDER_APPLIED
!= FINGERPRINT_COMPLETE
!= PROJECT_TARGET_REGRESSION_PASS
!= POST_ROLLBACK_SMOKE
!= RUNTIME_BEHAVIORAL_PROOF
```

Historical v0.4-v0.8 evidence remains historical and is not rewritten by v0.9.

This candidate authorizes no publication, broad sharing, consumer-project mutation, production/security claim or legacy retirement.
