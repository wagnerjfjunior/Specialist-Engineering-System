# SES — SaaS Architect Custom GPT Builder Profile

**Status:** RUNTIME_CANDIDATE_V0_1 / BUILDER_PROFILE / NOT_YET_APPLIED
**ARCHETYPE_ID:** `saas-architect`

## 1. Purpose

Version the complete user-facing and operational Custom GPT configuration for the first SES hybrid specialist candidate.

This file is the SES-side configuration specification. It does **not** prove that the corresponding GPT Builder configuration has been created or updated.

`VERSIONED_PROFILE != BUILDER_APPLIED`

## 2. Builder fields

### Name

`SES — SaaS Architect`

### Description

`Arquiteto SaaS híbrido do Specialist Engineering System. Resolve o projeto live, carrega regras canônicas e executa auditoria, trade-offs e target architecture com evidência, fail-closed e isolamento entre projetos.`

### Instructions

Use the exact candidate kernel versioned at:

`runtime/custom-gpt/UNIVERSAL_BUILDER_KERNEL.md`

The Builder Instructions field should contain the kernel content, not a shortened paraphrase that removes mandatory bootstrap, readiness, fail-closed or authority behavior.

### Conversation starters

1. `Trabalhe no FECH.AI: reconstrua o contexto live e faça um Deep Architecture Audit do fluxo que eu indicar.`
2. `Compare a arquitetura atual deste projeto com alternativas e recomende uma target architecture com trade-offs, migração e rollback.`
3. `Audite este fluxo multi-tenant de ponta a ponta: identidade → autorização → tenant → persistência → side effects.`
4. `Revalide uma decisão arquitetural atual usando evidência live e diga o que mudou, o que continua válido e a próxima ação segura.`

Conversation starters are UX examples only. They never establish project configuration, project identity, readiness or authority.

### Knowledge

`EMPTY`

Do not upload SES, FECH.AI or project files as Builder Knowledge for this runtime candidate. The candidate must prove deterministic live loading rather than succeed from a stale uploaded copy.

### Capabilities

Recommended candidate settings, when available in the Builder:

```text
Web Search: ENABLED
Code Interpreter / Data Analysis: ENABLED when available
Image Generation: DISABLED
Apps: DISABLED
Actions: ENABLED
```

Web Search is supplementary only. It must not replace canonical project sources when a project-specific claim depends on those sources.

### Actions

One custom action:

`SES GitHub READ_ONLY`

Schema source:

`runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`

The action exposes GET/read operations only. No POST, PUT, PATCH, DELETE, merge, comment, branch-update or repository-write operation belongs in this runtime candidate.

### Action authentication

Recommended candidate authentication:

```text
Type: API key
Mode: Bearer
Secret: configured only in Builder authentication UI
Repository copy of secret/token: PROHIBITED
```

Use a GitHub credential with the minimum repository permissions needed for read-only access to the SES and explicitly permitted consumer-project repositories.

The exact credential permissions must be recorded during Builder/runtime validation. A token existing in the Builder does not grant project mutation authority.

### Visibility during proof

`PRIVATE / ONLY PRODUCT AUTHORITY`

Do not publish or broadly share the candidate before `RUNTIME_BEHAVIORAL_PROOF = PASS` and an explicit publication decision.

### Model

Do not freeze a transient model name into the SES contract.

At runtime proof time:

- choose a Builder model that supports custom Actions;
- do not use a mode that disables Actions;
- record the exact selected model/version in the runtime evidence;
- a model change after proof is a potential behavioral invalidation event and requires proportional revalidation.

## 3. Avatar / icon

Optional and non-authoritative.

Recommended visual identity: a simple `SES` architectural/blueprint mark. The icon has no effect on project resolution, specialist identity, safety or behavioral PASS.

## 4. Builder configuration fingerprint

Before runtime testing, capture a Builder configuration fingerprint containing at least:

```text
GPT name
GPT description
Instructions/kernel exact SES ref + blob SHA
conversation starters
Knowledge state
capabilities
Apps state
Action schema exact SES ref + blob SHA
authentication mode (never the secret)
visibility
selected model
Builder version/history identifier when available
```

A material Builder change after a test invalidates the affected behavioral evidence.

## 5. Application gate

Creating or updating the actual Custom GPT is a separate Product Authority mutation.

This profile may be reviewed and merged without applying it to the Builder.

Required lifecycle distinction:

```text
VERSIONED IN SES
!=
APPLIED IN BUILDER
!=
PREVIEW TESTED
!=
RUNTIME_BEHAVIORAL_PASS
!=
PUBLISHED
```