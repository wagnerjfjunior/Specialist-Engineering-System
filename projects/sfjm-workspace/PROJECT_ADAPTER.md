# SES Project Adapter — SFJM Workspace

**Status:** FOUNDATION_V0_1 / SPECIALIST_ROLE_MAP_ACTIVE / CURRENT_SES_ROUTING_ENTRYPOINT

This adapter describes the SFJM Workspace project registered in the SES Project Registry and points to its project-owned canonical sources.

It intentionally contains stable routing metadata and source-precedence rules, not copied Workspace operational truth.

```text
PROJECT_ID: sfjm-workspace
PROJECT_NAME: SFJM Workspace
CANONICAL_SOURCE: GitHub repository wagnerjfjunior/sfjm-workspace
DEFAULT_REF_OR_RESOLUTION_RULE: resolve live main before material work
BOOTSTRAP_ENTRYPOINT: docs/BOOTSTRAP.md
CONTINUITY_ENTRYPOINT: handoffs/CURRENT.md
PROJECT_STATUS_ENTRYPOINT: docs/PROJECT_STATUS.md
NEXT_SAFE_ACTION_ENTRYPOINT: docs/NEXT_SAFE_ACTION.md
SPECIALIST_ENTRYPOINT_OR_RESOLUTION_RULE: exact SPECIALIST_ROLE_MAP below plus applicable canonical Workspace sources
MANUAL_HANDOFF_CONTRACT: core/protocols/MANUAL_SPECIALIST_HANDOFF_CONTRACT.md
```

## Canonical Workspace state priority

For project-specific material work, resolve state in this order:

```text
1. live main of wagnerjfjunior/sfjm-workspace
2. handoffs/CURRENT.md
3. docs/PROJECT_STATUS.md
4. docs/NEXT_SAFE_ACTION.md
5. other applicable versioned Workspace documents
```

The Project Adapter does not override this project-owned precedence.

## Product / protocol boundary

SFJM Workspace is a product that applies SFJM continuity principles.

It is separate from:

`wagnerjfjunior/StopJuniorMode`

The StopJuniorMode repository remains authoritative for the SFJM protocol, research, protocol governance and canonical protocol evidence.

A Workspace UX, implementation or lifecycle decision does not modify the SFJM protocol unless a separate explicitly authorized protocol change is made in the protocol repository.

External projects represented by SFJM Workspace remain authoritative for their own state. Workspace snapshots, cards, dashboards or continuity views must not silently replace those external authorities.

## Specialist role map

SFJM Workspace explicitly adopts only the following current certified SES archetype:

```text
SPECIALIST_ROLE_MAP:

- ROLE: documentation_audit
  ARCHETYPE_ID: documentation-auditor
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: NOT_APPLICABLE; resolve Workspace truth and continuity through the canonical source priority above
  LEGACY_ALIASES: none
```

No other current certified SES archetype is adopted by this adapter.

In particular, this registration does not automatically adopt:

- architecture;
- ux_ui;
- backend_data;
- application_security;
- seo_strategy;
- technical_seo;
- content_semantic_seo;
- seo_analytics_growth;
- paid_search_sem;
- future specialist archetypes.

Any later adoption requires a separate explicit project decision and versioned SES change.

## Resolution flow

For SFJM Workspace documentation-audit work:

```text
explicit PROJECT_IDENTIFIER = sfjm-workspace
+ explicit ROLE = documentation_audit
→ projects/REGISTRY.md
→ this Project Adapter
→ exact SPECIALIST_ROLE_MAP match
→ archetypes/REGISTRY.md
→ ARCHETYPE_ID documentation-auditor
→ confirm ACTIVE archetype/certification eligibility
→ resolve wagnerjfjunior/sfjm-workspace main live
→ read handoffs/CURRENT.md
→ read docs/PROJECT_STATUS.md
→ read docs/NEXT_SAFE_ACTION.md
→ read other versioned sources material to the audit
→ resolve live GitHub evidence material to the target
→ Context Readiness
→ bounded documentation-audit work
```

Do not infer an unmapped specialist role from repository content, project name or task semantics.


## Manual handoff identity rule

For any SES-selected specialist consultation, apply the universal manual handoff contract before rendering the human copy/paste destination.

```text
ARCHETYPE_ID
→ archetypes/REGISTRY.md
→ CANONICAL_NAME
→ SPECIALIST_TARGET_NAME

SPECIALIST_TARGET_NAME = ARCHETYPE_REGISTRY.CANONICAL_NAME
LEGACY_ALIAS != SPECIALIST_TARGET_NAME
PROJECT_LOCAL_RULES != SPECIALIST_TARGET_NAME
```

Project-local rules, legacy aliases and continuity remain valid context, but they must not replace the canonical SES destination identity. An unmapped project-local role remains project-local and must not be forced into an SES archetype.

## Audit boundary

The Documentation Auditor may evaluate documentation/evidence consistency for SFJM Workspace but does not gain authority to:

- mark a pull request Ready;
- merge;
- deploy;
- change Vercel;
- create backend/API/synchronization infrastructure;
- mutate external represented projects;
- modify StopJuniorMode protocol;
- accept risk on behalf of Product Authority;
- grant Security Go or equivalent external-project decisions.

Those authorities remain project-local and must be resolved from the applicable canonical sources.

## Adapter non-authority

This adapter does not own or freeze:

- current Workspace main SHA;
- current PR/head/check state;
- current blockers;
- current next safe action;
- current UI or implementation state;
- deployment/runtime state;
- external-project state;
- Product Authority decisions;
- protocol truth.

Those remain owned by their canonical repositories and live/project-local sources.

Preserve:

```text
REGISTERED != AUTHORIZED
ADOPTED != PROJECT_CONTEXT_READY
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
ADOPTED != READY_AUTHORIZATION
ADOPTED != MERGE_AUTHORIZATION
WORKSPACE_REPRESENTATION != EXTERNAL_PROJECT_AUTHORITY
WORKSPACE_PRODUCT != SFJM_PROTOCOL
```
