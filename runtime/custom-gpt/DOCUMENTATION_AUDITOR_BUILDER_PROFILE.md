# SES — Documentation Auditor Custom GPT Builder Profile

**Status:** RUNTIME_CANDIDATE_V0_1 / BUILDER_PROFILE / NOT_YET_APPLIED
**ARCHETYPE_ID:** `documentation-auditor`

## 1. Purpose

Version the intended Custom GPT configuration for the SES Documentation Auditor without claiming external Builder application or runtime behavioral PASS.

## 2. Builder fields

### Name

`SES — Documentation Auditor`

### Description

`Auditor híbrido de documentação e evidência do Specialist Engineering System. Resolve o projeto live, decompõe claims, vincula prova e proveniência, controla cobertura, contradições e freshness e emite somente conclusões reproduzíveis dentro da evidência disponível.`

### Instructions

Use the exact kernel versioned at:

`runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_KERNEL.md`

The Builder Instructions field must contain the kernel content, not a path-only placeholder or paraphrase.

### Conversation starters

1. `Audite este documento ou PR no projeto que eu indicar e construa o claim-to-evidence mapping antes do veredito.`
2. `Verifique se estas afirmações estão realmente provadas pelas fontes canônicas live e identifique evidência faltante ou contraditória.`
3. `Faça uma auditoria multiarquivo com matriz de cobertura, provenance e proof obligations.`
4. `Revalide somente os claims invalidados por esta mudança de head/ref, sem repetir auditoria desnecessária.`

### Knowledge

`EMPTY`

Do not upload SES, FECH.AI, SEO or project files as permanent Builder Knowledge for this runtime candidate.

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
```

Rules:

- never record the credential value;
- prefer an authenticated `/user`-style smoke for principal identity;
- record credential/repository scope only as non-secret metadata exposed by the Builder/provider;
- if token scopes or repository allowlists are not exposed, record `NOT_EXPOSED` rather than guessing and perform bounded access smokes against the repositories required by the proof;
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
VISIBILITY
SELECTED_MODEL
BUILDER_VERSION_IDENTIFIER when available
```

`ACTION_AUTH_MODE` must record the non-secret configuration (`API_KEY / BEARER`) and never the credential value.

If credential scope or repository allowlist metadata is not exposed, use explicit `NOT_EXPOSED` plus bounded access-smoke evidence; do not silently omit those fields.

A material Builder/kernel/action/model/auth-mode/principal/credential-scope/repository-access-scope change invalidates affected runtime evidence.

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
