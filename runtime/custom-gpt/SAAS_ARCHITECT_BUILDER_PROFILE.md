# SES — SaaS Architect Custom GPT Builder Profile

**Status:** RUNTIME_CANDIDATE_V0_1 / BUILDER_PROFILE / BUILDER_APPLICATION_OBSERVED / PREVIEW_EXECUTION_OBSERVED / FINGERPRINT_PENDING / RUNTIME_BEHAVIORAL_PROOF_NOT_ESTABLISHED
**ARCHETYPE_ID:** `saas-architect`

## 1. Purpose

Version the complete user-facing and operational Custom GPT configuration for the first SES hybrid specialist candidate and record the externally observed Builder/runtime-candidate lifecycle evidence without converting that evidence into a broader runtime behavioral PASS.

This file remains the SES-side configuration specification. The private candidate has now been observed configured sufficiently to execute the GitHub Action and Preview proof flows documented below, but the complete Builder fingerprint required by this profile has not yet been captured as one immutable evidence record.

```text
VERSIONED_PROFILE: YES
BUILDER_APPLICATION_OBSERVED: YES
PREVIEW_EXECUTION_OBSERVED: YES
BUILDER_FINGERPRINT_COMPLETE: NO
RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
PUBLISHED: NO
```

`BUILDER_APPLICATION_OBSERVED != COMPLETE_BUILDER_FINGERPRINT`

`PREVIEW_EXECUTION_OBSERVED != RUNTIME_BEHAVIORAL_PROOF`

## 2. Builder fields

### Name

`SES — SaaS Architect`

### Description

`Arquiteto SaaS híbrido do Specialist Engineering System. Resolve o projeto live, carrega regras canônicas e executa auditoria, trade-offs e target architecture com evidência, fail-closed e isolamento entre projetos.`

### Instructions

Use the exact candidate kernel versioned at:

`runtime/custom-gpt/UNIVERSAL_BUILDER_KERNEL.md`

The Builder Instructions field should contain the kernel content, not a shortened paraphrase that removes mandatory bootstrap, readiness, fail-closed or authority behavior.

The current candidate kernel is versioned on the PR #3 candidate head. Before any runtime behavioral PASS, the exact Instructions text/ref/blob actually applied in Builder must be included in the complete Builder fingerprint rather than inferred from successful Preview behavior.

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

The exact selected model used in the observed Preview executions has not yet been captured in the complete Builder fingerprint and must not be inferred.

## 3. Avatar / icon

Optional and non-authoritative.

Recommended visual identity: a simple `SES` architectural/blueprint mark. The icon has no effect on project resolution, specialist identity, safety or behavioral PASS.

## 4. Builder configuration fingerprint

Before runtime behavioral testing, capture a Builder configuration fingerprint containing at least:

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

Current fingerprint status:

```text
FINGERPRINT_STATUS: PARTIAL / NOT YET CAPTURED AS ONE COMPLETE EVIDENCE RECORD
```

The observed Preview executions prove that a private candidate and GitHub Action were mounted and executed. They do not by themselves prove that every Builder field above exactly matches this versioned profile.

A material Builder change after a test invalidates the affected behavioral evidence.

## 5. Observed Builder and Preview evidence

The following evidence was produced through the private `SES — SaaS Architect` candidate during PR #3 validation. It is runtime-candidate evidence, not canonical runtime behavioral PASS.

### 5.1 GitHub authentication and loader smoke

Observed successful operations included:

```text
getAuthenticatedGitHubUser
→ authenticated principal: wagnerjfjunior / account id 228261219

getRepositoryMetadata
→ wagnerjfjunior/Specialist-Engineering-System resolved as private repository

getRepositoryBranch
→ SES main resolved to exact SHA

getGitCommitObject
→ exact commit object and root tree resolved

getRepositoryFileRawByPath
→ docs/bootstrap/INDEX.md retrieved at exact ref
```

Classification:

```text
GITHUB_AUTH_SMOKE: PASS
CORE_GITHUB_LOADER_SMOKE: PASS
```

These smoke results prove read-only GitHub loading for the exercised path only. They do not establish T01-T29 runtime behavioral proof.

### 5.2 Candidate-head protocol proof

The candidate autonomously resolved and preserved separately:

```text
SES_CANONICAL_MAIN_REF
SES_CANDIDATE_REF
SES_EFFECTIVE_REF = SES_CANDIDATE_REF
```

It read the candidate bootstrap/archetype/runtime sources from the exact PR #3 head and did not relabel the candidate head as canonical `main`.

Classification at the tested head:

```text
T30: PASS
CANDIDATE_HEAD_PROTOCOL_PROOF: PASS
RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
```

Any later PR head change invalidates reuse of that exact-head PASS until proportional delta revalidation confirms the new head did not alter the tested semantics.

### 5.3 FECH.AI candidate end-to-end bootstrap proof

The same private candidate subsequently demonstrated the read-only chain:

```text
SES candidate
→ saas-architect archetype
→ SES Project Registry
→ FECH.AI Project Adapter
→ wagnerjfjunior/fecha.ai main live
→ FECH.AI bootstrap
→ FECH.AI specialist registry
→ current project-local architecture specialist/skill
→ common rules / applicable continuity
→ Context Readiness Receipt
```

The project-local architecture identity was resolved from FECH.AI canonical sources rather than frozen into the SES archetype.

Classification at the tested head:

```text
FECHAI_CANDIDATE_E2E_BOOTSTRAP: PASS
RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
T01-T29: NOT COMPLETE
```

A later documentation-only reconciliation of this profile changes the PR head and therefore requires proportional exact-head delta revalidation before those candidate-head PASS results are used for a Ready decision. The prior evidence remains historical and must not be rewritten.

## 6. Historical failed/indeterminate attempts preserved

Candidate development evidence must not be rewritten retroactively. The following observations remain part of the record:

```text
INITIAL_GENERALIZED_ACTION:
- schema initially produced Builder parser errors involving parameter $ref handling and components.schemas;
- corrected in the same PR candidate without claiming prior PASS.

EARLY_GET_COMMIT_PREVIEW:
- request targeting openai/openai-python@main returned ClientResponseError.

EARLY_AUTH_OR_TOOL_ATTEMPTS:
- getAuthenticatedGitHubUser returned ClientResponseError in some Preview attempts;
- later Preview sessions reported the GitHub connector/tool unavailable in that chat.

IDENTITY_ANOMALY:
- one Preview response reported authenticated GitHub user seomaster2020;
- subsequent controlled tests authenticated as the intended principal wagnerjfjunior;
- the anomalous observation remains INDETERMINATE and is not evidence of credential isolation failure by itself.

ARBITRARY_TARGET_OBSERVATION:
- an early Preview selected openai/openai-python without a canonical SES project locator or explicit bounded target;
- later candidate proofs used explicit/canonical repository resolution and passed the intended chain.
```

A later successful run does not retroactively turn these earlier attempts into PASS.

## 7. Application and proof gate

Creating or updating the actual Custom GPT remains a separate Product Authority mutation from repository changes. The current private candidate was manually configured/tested under Product Authority during PR #3 candidate validation; this repository reconciliation records that observed fact but does not itself perform any Builder mutation.

Required lifecycle distinction:

```text
VERSIONED IN SES
!=
BUILDER APPLICATION OBSERVED
!=
COMPLETE BUILDER FINGERPRINT
!=
PREVIEW EXECUTION OBSERVED
!=
RUNTIME_BEHAVIORAL_PASS
!=
PUBLISHED
```

Current lifecycle evidence:

```text
VERSIONED_PROFILE: YES
BUILDER_APPLICATION_OBSERVED: YES
PREVIEW_EXECUTION_OBSERVED: YES
GITHUB_AUTH_SMOKE: PASS
CORE_GITHUB_LOADER_SMOKE: PASS
BUILDER_FINGERPRINT_COMPLETE: NO
RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
T01-T29_COMPLETE: NO
PUBLISHED: NO
```

Candidate-head T30 and FECH.AI E2E PASS evidence exists for a prior exact PR head and must be revalidated proportionally after any head change before being relied on for a Ready gate.

No Ready, merge, publication, FECH.AI mutation, Supabase mutation, Vercel mutation or production change follows automatically from these observations.