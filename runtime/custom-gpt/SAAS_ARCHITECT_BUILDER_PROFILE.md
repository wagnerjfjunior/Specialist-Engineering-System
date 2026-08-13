# SES — SaaS Architect Custom GPT Builder Profile

**Status:** RUNTIME_CANDIDATE_V0_2 / BUILDER_PROFILE / TARGET_KERNEL_VERSIONED / STARTER_BUILDER_OBSERVED / V0_2_FINGERPRINT_NOT_YET_COMPLETE
**ARCHETYPE_ID:** `saas-architect`

## 1. Purpose

Version the current intended Custom GPT configuration for `SES — SaaS Architect` after adoption of the standardized SES hybrid project-entry interaction.

This profile does not rewrite or promote prior runtime evidence. The previously tested v0.1 runtime-effective configuration remains historical evidence bound to its exact kernel/ref/fingerprint. The v0.2 starter/kernel change requires a fresh Builder fingerprint and proportional behavioral revalidation before any v0.2 runtime claim.

```text
TARGET_PROFILE_VERSION: V0_2
TARGET_KERNEL_VERSIONED: YES
STARTER_CHANGE_OBSERVED_IN_BUILDER: YES
FULL_V0_2_BUILDER_APPLICATION: NOT_YET_ESTABLISHED
V0_2_BUILDER_FINGERPRINT_COMPLETE: NO
V0_2_RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
PUBLISHED: NO
```

`HISTORICAL_V0_1_PROOF != V0_2_RUNTIME_PROOF`

## 2. Builder fields — v0.2 target

### Name

`SES — SaaS Architect`

### Description

`Arquiteto SaaS híbrido do Specialist Engineering System. Resolve o projeto live, carrega regras canônicas e executa auditoria, trade-offs e target architecture com evidência, fail-closed e isolamento entre projetos.`

### Instructions

Use the exact compact kernel versioned at:

`runtime/custom-gpt/UNIVERSAL_BUILDER_KERNEL.md`

The Builder Instructions field must contain the complete kernel content, not a path reference, paraphrase or truncated copy.

```text
TARGET_KERNEL_STATUS: RUNTIME_CANDIDATE_V0_2
BUILDER_INSTRUCTIONS_HARD_LIMIT: <= 8000 characters
SES_OPERATIONAL_BUDGET: <= 7500 characters
CURRENT_COMPACT_KERNEL_MEASURED_COUNT: 6475 characters
COUNT_METHOD: Unicode code-point count of repository text content
```

The kernel loads the reusable method live through SES bootstrap, archetype resolution and `core/protocols/HYBRID_SPECIALIST_BOOTSTRAP_CONTRACT.md`.

### Conversation starters

1. `# CLIQUE PARA INICIAR`

This starter is UX input only. It supplies `PROJECT_IDENTIFIER: NOT_SUPPLIED` to the same ordered hybrid bootstrap flow used when the user names a project directly.

No project supplied:

```text
# CLIQUE PARA INICIAR
→ SES live/bootstrap
→ saas-architect archetype
→ live Project Registry
→ numbered ACTIVE project list
→ numeric selection
→ normal Project Adapter/bootstrap/local-specialist flow
```

Project already supplied:

```text
"Trabalhe no FECH.AI"
→ PROJECT_IDENTIFIER = FECH.AI
→ same project-resolution stage
→ normal Project Adapter/bootstrap/local-specialist flow
```

The menu is unnecessary when the identifier is already supplied; no mandatory bootstrap stage is skipped.

Project numbers must never be hard-coded. A listed/selected project is not project-local architecture readiness:

```text
PROJECT_LISTED != PROJECT_SPECIALIST_READY
PROJECT_SELECTED != PROJECT_CONTEXT_READY
```

### Knowledge

`EMPTY`

Do not upload SES or consumer-project files as permanent Builder Knowledge. Live canonical loading remains required.

### Capabilities

Target baseline:

```text
Web Search: ENABLED
Code Interpreter / Data Analysis: ENABLED
Image Generation: DISABLED
Actions: ENABLED
Apps: record actual Builder UI state; do not invent a toggle when the UI does not expose one
```

Web Search is supplementary only and does not replace canonical project sources.

### Actions

One custom Action:

`SES GitHub READ_ONLY`

Schema source:

`runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`

No mutation endpoint belongs in the baseline publishable candidate.

### Authentication

```text
Type: API key
Mode: Bearer
Secret: Builder UI only / never committed or reproduced in evidence
```

Before v0.2 runtime proof capture non-secret principal/access evidence, including authenticated login/id and bounded required-repository access smokes when scope/allowlist metadata is not exposed.

### Visibility

Target remains non-public until runtime proof and a separate publication decision.

The current user-supplied Builder screenshot after the starter update shows `Apenas convidados`. Treat that as an observed current access state, not as proof of publication authorization or v0.2 runtime readiness.

### Model

Record the actual selected model in the v0.2 fingerprint. Current user-supplied Builder screenshots show `GPT-5.6 Sol` as creator-recommended model.

## 3. V0.2 fingerprint required before testing

Capture:

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

Required before behavioral execution:

```text
INSTRUCTIONS_COMPLETE_COPY: YES
INSTRUCTIONS_CHARACTER_COUNT <= 7500
CONVERSATION_STARTERS: exactly 1 / # CLIQUE PARA INICIAR
KNOWLEDGE: EMPTY
STARTER_OVERFLOW_SUBSTITUTE: NO
```

Any material Builder/kernel/action/model/auth/principal/access-scope change invalidates affected v0.2 evidence.

## 4. Historical v0.1 evidence — preserved, not promoted

The prior runtime-effective configuration remains historical evidence:

```text
RUNTIME_EFFECTIVE_CONFIG_REF: f55a6edc9674f8aa96438082e5ca3166a6df7e03
HISTORICAL_KERNEL_BLOB: 50672d09665035c0f60f18887f3295a5ea8cad03
HISTORICAL_CONVERSATION_STARTERS: 4
HISTORICAL_BUILDER_APPLICATION_OBSERVED: YES
HISTORICAL_PREVIEW_EXECUTION_OBSERVED: YES
HISTORICAL_BUILDER_FINGERPRINT_COMPLETE: YES
HISTORICAL_GITHUB_AUTH_SMOKE: PASS
HISTORICAL_CORE_GITHUB_LOADER_SMOKE: PASS
HISTORICAL_T30: PASS @ f55a6edc9674f8aa96438082e5ca3166a6df7e03
HISTORICAL_FECHAI_CANDIDATE_E2E: PASS @ f55a6edc9674f8aa96438082e5ca3166a6df7e03
HISTORICAL_RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
HISTORICAL_T01_T29_COMPLETE: NO
```

The v0.2 starter/kernel change does not turn those results into v0.2 PASS and does not erase them.

## 5. Historical failed/indeterminate observations — preserved

The following earlier observations remain historical:

```text
INITIAL_GENERALIZED_ACTION:
- Builder parser failures occurred before schema correction.

EARLY_GET_COMMIT_PREVIEW:
- one request targeting openai/openai-python@main returned ClientResponseError.

EARLY_AUTH_OR_TOOL_ATTEMPTS:
- some getAuthenticatedGitHubUser attempts failed;
- some Preview sessions reported the GitHub tool unavailable.

IDENTITY_ANOMALY:
- one Preview response reported authenticated user seomaster2020;
- later controlled tests authenticated the intended principal wagnerjfjunior;
- the anomaly remains INDETERMINATE, not retroactively PASS or proven credential-isolation failure.

ARBITRARY_TARGET_OBSERVATION:
- one early Preview selected openai/openai-python without canonical SES project resolution;
- later controlled evidence used canonical/explicit targets.
```

A later successful run never retroactively converts these historical attempts into PASS.

## 6. V0.2 proof gate

The actual configured v0.2 runtime must pass the runtime-required cases in `tests/behavioral/HYBRID_SPECIALIST_BOOTSTRAP_TESTS.md`, including standardized project-entry cases P01–P08, under the v0.2 fingerprint before a v0.2 behavioral PASS may be considered.

Creating/updating the Custom GPT is a Product Authority mutation separate from repository versioning.

```text
PROFILE_VERSIONED
!= BUILDER_APPLIED
!= FINGERPRINT_COMPLETE
!= PREVIEW_TESTED
!= RUNTIME_BEHAVIORAL_PROOF
!= PUBLISHED
```

No Ready, merge, publication, consumer-project mutation, Supabase/Vercel mutation, legacy retirement or production claim follows automatically from this profile.
