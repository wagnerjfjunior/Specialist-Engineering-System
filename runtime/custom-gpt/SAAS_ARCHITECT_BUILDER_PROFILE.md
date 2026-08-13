# SES — SaaS Architect Custom GPT Builder Profile

**Status:** RUNTIME_CANDIDATE_V0_3 / BUILDER_PROFILE / TARGET_KERNEL_VERSIONED / EXTERNAL_BUILDER_UPDATE_REQUIRED
**ARCHETYPE_ID:** `saas-architect`

## 1. Purpose

Version the intended Custom GPT configuration for `SES — SaaS Architect` after the project-selection latency finding demonstrated that project selection must stop before consumer-project materialization when no substantive task exists.

This profile preserves prior evidence without rewriting it:
- v0.1 remains historically certified;
- v0.2 remains a versioned but not runtime-proven target;
- v0.3 is the new target and requires fresh Builder application/fingerprint plus proportional behavioral revalidation.

```text
V0_1_RUNTIME_BEHAVIORAL_PROOF: PASS / HISTORICAL / PRESERVED
V0_2_RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
V0_3_RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
```

`HISTORICAL_V0_1_RUNTIME_PASS != V0_2_RUNTIME_PASS != V0_3_RUNTIME_PASS`

## 2. Builder fields — v0.3 target

### Name

`SES — SaaS Architect`

### Description

`Arquiteto SaaS híbrido do Specialist Engineering System. Resolve o projeto live, carrega regras canônicas e executa auditoria, trade-offs e target architecture com evidência, fail-closed e isolamento entre projetos.`

### Instructions

Use the exact compact kernel versioned at:

`runtime/custom-gpt/UNIVERSAL_BUILDER_KERNEL.md`

The Builder Instructions field must contain the complete kernel content, not a path reference, paraphrase or truncated copy.

```text
TARGET_KERNEL_STATUS: RUNTIME_CANDIDATE_V0_3
BUILDER_INSTRUCTIONS_HARD_LIMIT: <= 8000 characters
SES_OPERATIONAL_BUDGET: <= 7500 characters
CURRENT_COMPACT_KERNEL_MEASURED_COUNT: 6839 characters
COUNT_METHOD: Unicode code-point count of repository text content
SCOPE_OF_SIZE_CONSTRAINT: Builder Instructions field only
```

The 8,000-character Builder constraint applies only to content copied into **Instructions**. It does not constrain SES Core contracts, archetypes, profiles, tests, continuity or project files loaded later.

`BUILDER_INSTRUCTIONS_SIZE_CONSTRAINT != SES_DOCUMENT_SIZE_CONSTRAINT`

The kernel loads reusable method live through SES bootstrap, archetype resolution and `core/protocols/HYBRID_SPECIALIST_BOOTSTRAP_CONTRACT.md`.

### Conversation starters

1. `# CLIQUE PARA INICIAR`

No project supplied:

```text
# CLIQUE PARA INICIAR
→ SES live/bootstrap
→ saas-architect archetype
→ live Project Registry
→ numbered ACTIVE project list
→ numeric selection
→ PROJECT_SELECTED
→ wait for substantive task
```

Project supplied directly without task:

```text
"Trabalhe no FECH.AI"
→ deterministic project resolution
→ PROJECT_SELECTED
→ wait for substantive task
```

Project plus substantive task:

```text
"Audite a arquitetura do FECH.AI"
→ same project-resolution stage
→ task materiality classification
→ Project Adapter / project bootstrap / local specialist
→ task-material plus canonically mandatory sources
→ Context Readiness Receipt
→ bounded architecture work
```

No alternate path or bypass exists.

When no substantive task exists after selection, do **not** read Project Adapter, consumer-project main, project bootstrap, project-local specialist rules, continuity, authority/governance or project evidence, and do not emit a Context Readiness Receipt.

```text
PROJECT_LISTED != PROJECT_SPECIALIST_READY
PROJECT_SELECTED != PROJECT_BOOTSTRAPPED
PROJECT_SELECTED != PROJECT_CONTEXT_READY
```

Project numbers are transient and menu-bound.

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
Apps: record actual Builder UI state; use NOT_PRESENT_IN_CURRENT_BUILDER_UI when appropriate
```

Web Search is supplementary only.

### Actions

One custom Action:

`SES GitHub READ_ONLY`

Schema source:

`runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`

No mutation endpoint belongs in the baseline candidate.

### Authentication

```text
Type: API key
Mode: Bearer
Secret: Builder UI only / never committed or reproduced in evidence
```

Before v0.3 runtime proof capture non-secret principal/access evidence and bounded repository-access smokes when scope/allowlist metadata is not exposed.

### Visibility

Keep non-public until runtime proof and separate publication authorization.

### Model

Record the actual selected model in the v0.3 fingerprint. A model change is a potential behavioral invalidation event.

## 3. V0.3 fingerprint required before testing

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

## 4. Historical v0.1 evidence — certified PASS preserved

The v0.1 runtime behavioral certification remains a prior-version proof obligation already satisfied. Canonical durable evidence:

`tests/runtime/evidence/HYBRID_SAAS_ARCHITECT_RUNTIME_PROOF_2026-08-12.md`

Certified baseline:

```text
HISTORICAL_PROFILE_VERSION: V0_1
HISTORICAL_RUNTIME_BEHAVIORAL_PROOF: PASS
HISTORICAL_RUNTIME_REQUIRED_SUITE: T01-T29
HISTORICAL_T01_T29: 29/29 PASS
HISTORICAL_FAIL: 0
HISTORICAL_PENDING: 0
HISTORICAL_CERTIFIED_CANONICAL_MAIN_REF: 24089d8dbc1a90a6a0f15c5a86d9032d27f216b6
HISTORICAL_KERNEL_BLOB: 50672d09665035c0f60f18887f3295a5ea8cad03
HISTORICAL_ACTION_SCHEMA_BLOB: 1e6237e806fd84716ec13b019e6617ad4110a211
HISTORICAL_CONVERSATION_STARTERS: 4
HISTORICAL_FINAL_ACTION_SURFACE: READ_ONLY / GET-only
HISTORICAL_BASELINE_RESTORED_AFTER_T16_T28: YES
```

Earlier candidate-head evidence that preceded canonical runtime certification also remains preserved:

```text
HISTORICAL_CANDIDATE_EFFECTIVE_REF: f55a6edc9674f8aa96438082e5ca3166a6df7e03
HISTORICAL_BUILDER_APPLICATION_OBSERVED: YES
HISTORICAL_PREVIEW_EXECUTION_OBSERVED: YES
HISTORICAL_BUILDER_FINGERPRINT_COMPLETE: YES
HISTORICAL_GITHUB_AUTH_SMOKE: PASS
HISTORICAL_CORE_GITHUB_LOADER_SMOKE: PASS
HISTORICAL_T30: PASS @ f55a6edc9674f8aa96438082e5ca3166a6df7e03
HISTORICAL_FECHAI_CANDIDATE_E2E: PASS @ f55a6edc9674f8aa96438082e5ca3166a6df7e03
```

Later target changes do not downgrade this historical PASS and do not promote it into v0.2/v0.3 proof.

## 5. Historical failed/indeterminate observations — preserved

The following earlier development observations remain historical evidence:

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

A later successful run never retroactively converts these attempts into PASS.

## 6. v0.2 target and observed failure — preserved

v0.2 standardized the single starter and project-entry flow but was not fully applied to the external Builder before being superseded.

User-supplied Builder evidence on 2026-08-13 established:

```text
STARTER: # CLIQUE PARA INICIAR
BUILDER_INSTRUCTIONS: v0.1 kernel still applied
FULL_V0_2_BUILDER_APPLICATION: NO
V0_2_RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
```

A runtime attempt using `# CLIQUE PARA INICIAR` with the old v0.1 Instructions returned generic onboarding rather than the required live numbered project menu.

Preserve:

```text
V0_2_P01_ATTEMPT_1: FAIL
FAILURE_CLASS: BUILDER_KERNEL_DRIFT / OLD_V0_1_INSTRUCTIONS
RETROACTIVE_PASS: PROHIBITED
```

A later successful v0.3 execution will not rewrite this failure.

## 7. Project-selection latency finding

User-run tests after Core v0.2 showed that once selection did work, both specialists materialized consumer projects before a substantive task existed. User-observed waits were approximately:
- Documentation Auditor selections: about two minutes;
- SaaS Architect Blogs/SEO selection: 4 minutes 10 seconds.

These are user-observed wall times, not independently instrumented platform timings.

The architectural finding is evidence-supported by the returned behavior: selection triggered project `main`, bootstrap, local specialist and authority/continuity resolution before any substantive task.

v0.3 corrects this by requiring:

`NO SUBSTANTIVE TASK -> NO CONSUMER-PROJECT MATERIALIZATION`

## 8. v0.3 proof gate

The actual configured v0.3 runtime must pass the runtime-required cases in `tests/behavioral/HYBRID_SPECIALIST_BOOTSTRAP_TESTS.md`, including selection-deferral cases P01–P10, under the v0.3 fingerprint before v0.3 behavioral PASS may be considered.

Creating/updating the external Custom GPT is a separate Product Authority mutation.

```text
PROFILE_VERSIONED
!= BUILDER_APPLIED
!= FINGERPRINT_COMPLETE
!= PREVIEW_TESTED
!= RUNTIME_BEHAVIORAL_PROOF
!= PUBLISHED
```

No publication, consumer-project mutation, legacy retirement or production claim follows automatically.
