# SES — Documentation Auditor Custom GPT Builder Profile

**Status:** RUNTIME_CANDIDATE_V0_3 / BUILDER_PROFILE / NOT_YET_APPLIED
**ARCHETYPE_ID:** `documentation-auditor`

## 1. Purpose

Version the intended Custom GPT configuration for the SES Documentation Auditor without claiming external Builder application or runtime behavioral PASS.

The Builder Instructions field has a hard operational size constraint. Therefore the runtime uses a compact bootstrap/guardrail kernel in Instructions and loads the full specialist method live from canonical SES sources.

`COMPACT_KERNEL != FULL_ARCHETYPE`

The compact kernel must be sufficient to resolve and enforce the canonical loader, project-selection UX, authority, evidence-integrity, retrieval-resilience, mutation and anti-overclaim boundaries before material work. Detailed Evidence Engineering method remains versioned in the archetype/Core contracts and is loaded live.

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
CURRENT_COMPACT_KERNEL_MEASURED_COUNT: 7389 characters
COUNT_METHOD: Unicode code-point count of repository text content
```

The operational budget intentionally leaves margin for Builder/UI counting differences and future bounded maintenance. Any kernel edit must re-measure the complete final file before Builder application. A kernel over the 7,500-character SES budget requires deliberate review; a kernel over the Builder hard limit must not be applied.

The compact Instructions kernel must bootstrap the full method live through:

`SES main → docs/bootstrap/INDEX.md → archetypes/REGISTRY.md → documentation-auditor archetype → applicable Core protocols → registered consumer-project bootstrap/rules when project-specific`.

For initial project selection, the candidate must apply:

`core/protocols/HYBRID_PROJECT_SELECTION_UX_CONTRACT.md`

Do not move overflow instructions into Conversation Starters or permanent Builder Knowledge as a substitute for the canonical live loader.

### Conversation starters

1. `# CLIQUE PARA INICIAR`

The starter is a UX trigger only. When used without a supplied project identifier, the runtime must resolve SES live, read `projects/REGISTRY.md`, enumerate only `ACTIVE` projects by `CANONICAL_NAME`, display them as a numbered list, retain the exact `PROJECT_ID` mapping for that displayed menu and wait for the user's numeric selection.

A valid explicit project identifier supplied directly by the user may bypass the menu and resolve through the canonical Project Registry. Unknown/ambiguous identifiers must not be guessed; when the registry is available, the runtime may present the current active-project menu as recovery.

`PROJECT_SELECTED != PROJECT_CONTEXT_READY`.

If the user requested only project connection/bootstrap, the runtime must not emit blanket readiness for unspecified future work. A later substantive task requires task-specific scope and a new or revalidated task-bound readiness receipt.

Conversation starters are UX only. They are not configuration authority and must not carry required kernel behavior that is absent from canonical SES contracts/Instructions.

### Knowledge

`EMPTY`

Do not upload SES, FECH.AI, SEO or project files as permanent Builder Knowledge for this runtime candidate. Knowledge must not be used as an overflow channel for required Instructions or as a substitute for live canonical loading.

### Capabilities

Target baseline:

```text
Web Search: ENABLED (supplementary only)
Code Interpreter / Data Analysis: ENABLED
Image Generation: DISABLED
Apps: DISABLED
Actions: ENABLED
```

### Actions

Reuse the existing read-only schema:

`runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`

No Action mutation is part of this profile.

### Action authentication

Configure authentication separately in the Builder UI:

```text
Type: API key
Mode: Bearer
Secret value: Builder UI only / never committed
```

The secret/token must never be written to SES, consumer repositories, prompts, logs or evidence records.

Authentication evidence must capture the **non-secret effective identity and access boundary**, not merely the transport mode. Before runtime proof, record when observable:

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

- never record the credential value;
- prefer an authenticated `/user`-style smoke for principal identity;
- record credential/repository scope only as non-secret metadata exposed by the Builder/provider;
- if token scopes or repository allowlists are not exposed, record `NOT_EXPOSED` rather than guessing and perform bounded access smokes against the repositories required by the proof;
- positive bounded access smokes prove only that the required repositories are accessible; they do **not** prove exclusivity, absence of access to other repositories, or least privilege;
- when scope metadata is not exposed, record `ACCESS_SCOPE_EVIDENCE_LIMITATION: REQUIRED_ACCESS_PROVEN / EXCESS_ACCESS_NOT_ASSESSED` and make no broader access-isolation claim;
- a principal change, credential-scope change, repository-access-scope change, or unexplained credential replacement invalidates affected runtime evidence until the effective access boundary is re-established;
- identical `API_KEY / BEARER` mode alone is never sufficient to reuse prior runtime evidence after a credential change.

### Visibility

`PRIVATE / APENAS PARA MIM` until runtime behavioral certification and separate publication decision.

### Model

Record the actually selected Builder model in the fingerprint. Do not freeze a transient model name as a permanent SES architectural dependency.

## 3. Runtime resilience requirements

Before runtime behavioral proof, the candidate must apply:

`core/protocols/EVIDENCE_RETRIEVAL_RESILIENCE_CONTRACT.md`

Mandatory behaviors include:

- fail-closed large-file handling;
- `NOT_READ` when a retrieval fails before any file content is recovered;
- `PARTIAL_READ` only when some content was recovered but complete reading/EOF was not proven;
- no `INTEGRAL_READ` without start-to-EOF proof;
- chunk coverage union semantics;
- manual/alternate-source fallback when chunked live retrieval is unavailable;
- recursive-tree truncation detection;
- directory-by-directory tree fallback;
- progressive disclosure under context-budget pressure;
- no repository-wide ingestion by default.

The current Action does not expose a dedicated bounded line-range/chunk loader. The Builder must not pretend otherwise.

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

Before testing, verify:

```text
INSTRUCTIONS_COMPLETE_COPY: YES
INSTRUCTIONS_CHARACTER_COUNT <= 7500
KNOWLEDGE_OVERFLOW_SUBSTITUTE: NO
STARTER_OVERFLOW_SUBSTITUTE: NO
```

`ACTION_AUTH_MODE` must record the non-secret configuration (`API_KEY / BEARER`) and never the credential value.

If credential scope or repository allowlist metadata is not exposed, use explicit `NOT_EXPOSED` plus bounded access-smoke evidence; do not silently omit those fields or convert positive access tests into a least-privilege claim.

A material Builder/kernel/action/model/auth-mode/principal/credential-scope/repository-access-scope change invalidates affected runtime evidence. A character-budget failure or truncated Instructions copy blocks Builder fingerprint completeness and runtime certification.

## 5. Lifecycle separation

```text
PROFILE_VERSIONED
!= BUILDER_APPLIED
!= PREVIEW_TESTED
!= RUNTIME_BEHAVIORAL_PROOF
!= PROJECT_LOCAL_EQUIVALENCE
!= LEGACY_RETIREMENT
```

This file versions intent only. Product Authority separately controls Builder configuration and publication.
