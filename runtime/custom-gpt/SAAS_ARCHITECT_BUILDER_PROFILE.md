# SES — SaaS Architect Custom GPT Builder Profile

**Status:** RUNTIME_CANDIDATE_V0_1 / BUILDER_PROFILE / PRIOR_BUILDER_APPLICATION_OBSERVED / CURRENT_VERSION_REAPPLICATION_REQUIRED / FINGERPRINT_PENDING / RUNTIME_BEHAVIORAL_PROOF_NOT_ESTABLISHED
**ARCHETYPE_ID:** `saas-architect`

## 1. Purpose

Version the complete user-facing and operational Custom GPT configuration for the first SES hybrid specialist candidate and record Builder/runtime-candidate lifecycle evidence without converting historical Preview evidence into proof for a materially changed current version.

The private candidate was previously observed configured sufficiently to execute the GitHub Action and candidate Preview proof flows. Subsequent PR #3 remediation changed the versioned Kernel and GitHub Action schema materially. Therefore the currently versioned candidate must be reapplied in Builder before new Preview evidence can be attributed to the current version.

```text
VERSIONED_PROFILE: YES
PRIOR_BUILDER_APPLICATION_OBSERVED: YES
PRIOR_PREVIEW_EXECUTION_OBSERVED: YES
CURRENT_VERSION_BUILDER_APPLICATION_OBSERVED: NO
CURRENT_VERSION_PREVIEW_EXECUTION_OBSERVED: NO
BUILDER_FINGERPRINT_COMPLETE: NO
RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
PUBLISHED: NO
```

`PRIOR_BUILDER_APPLICATION_OBSERVED != CURRENT_VERSION_BUILDER_APPLICATION_OBSERVED`

`PREVIEW_EXECUTION_OBSERVED != RUNTIME_BEHAVIORAL_PROOF`

## 2. Builder fields

### Name

`SES — SaaS Architect`

### Description

`Arquiteto SaaS híbrido do Specialist Engineering System. Resolve o projeto live, carrega regras canônicas e executa auditoria, trade-offs e target architecture com evidência, fail-closed e isolamento entre projetos.`

### Instructions

Use the exact current kernel versioned at:

`runtime/custom-gpt/UNIVERSAL_BUILDER_KERNEL.md`

The Builder Instructions field should contain the kernel content, not a shortened paraphrase that removes mandatory bootstrap, readiness, fail-closed or authority behavior.

After any material Kernel change, the prior Builder application/fingerprint is stale until the exact current Instructions text/ref/blob is manually reapplied and captured.

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

The current schema exposes GET/read operations only, includes pagination for pageable lifecycle evidence endpoints, and intentionally exposes no credential-global `/search/code` operation. No POST, PUT, PATCH, DELETE, merge, comment, branch-update or repository-write operation belongs in this runtime candidate.

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

The exact selected model used in prior Preview executions was not captured in a complete Builder fingerprint and must not be inferred.

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
FINGERPRINT_STATUS: STALE/PENDING — CURRENT VERSION NOT YET REAPPLIED AS ONE COMPLETE EVIDENCE RECORD
```

Historical Preview executions prove that an earlier private candidate and GitHub Action were mounted and executed. They do not prove the current remediated Kernel/Action version is applied.

A material Builder change after a test invalidates the affected behavioral evidence.

## 5. Historical Builder and Preview evidence

The following evidence was produced through the private `SES — SaaS Architect` candidate before the current material Kernel/Action remediation. It remains historical evidence only.

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

Historical classification:

```text
GITHUB_AUTH_SMOKE: PASS on prior applied version
CORE_GITHUB_LOADER_SMOKE: PASS on prior applied version
```

These results do not establish current-version Builder application or T01-T29 runtime behavioral proof.

### 5.2 Candidate-head protocol proof

The prior candidate autonomously resolved and preserved separately:

```text
SES_CANONICAL_MAIN_REF
SES_CANDIDATE_REF
SES_EFFECTIVE_REF = SES_CANDIDATE_REF
```

Historical classification at the previously tested head:

```text
T30: PASS
CANDIDATE_HEAD_PROTOCOL_PROOF: PASS
```

Because the current remediation changes Kernel ref-selection semantics, this PASS cannot be extended to the new head by documentation-only delta reasoning. After the current Kernel and Action schema are reapplied in Builder, T30 must be rerun against the exact current head.

### 5.3 FECH.AI candidate end-to-end bootstrap proof

The prior private candidate demonstrated the read-only chain:

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

Historical classification:

```text
FECHAI_CANDIDATE_E2E_BOOTSTRAP: PASS on prior applied version
RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
T01-T29: NOT COMPLETE
```

Because Kernel/Action semantics changed materially, the FECH.AI candidate E2E proof must also be rerun after current-version Builder reapplication before a new merge gate relies on it.

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

Creating or updating the actual Custom GPT remains a separate Product Authority mutation from repository changes. This repository remediation does not itself update Builder.

Required lifecycle distinction:

```text
VERSIONED IN SES
!=
BUILDER APPLICATION OBSERVED FOR CURRENT VERSION
!=
COMPLETE BUILDER FINGERPRINT
!=
PREVIEW EXECUTION OBSERVED FOR CURRENT VERSION
!=
RUNTIME_BEHAVIORAL_PASS
!=
PUBLISHED
```

Current lifecycle evidence after material remediation:

```text
VERSIONED_PROFILE: YES
CURRENT_VERSION_BUILDER_APPLICATION_OBSERVED: NO
CURRENT_VERSION_PREVIEW_EXECUTION_OBSERVED: NO
BUILDER_FINGERPRINT_COMPLETE: NO
CANDIDATE_HEAD_T30_CURRENT_VERSION: RERUN_REQUIRED
FECHAI_CANDIDATE_E2E_CURRENT_VERSION: RERUN_REQUIRED
RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
T01-T29_COMPLETE: NO
PUBLISHED: NO
```

No Ready, merge, publication, FECH.AI mutation, Supabase mutation, Vercel mutation or production change follows automatically from these observations.
