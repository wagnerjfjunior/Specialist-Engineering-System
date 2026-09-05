# SES Project Adapter — StopJuniorMode / SFJM Protocol

**Status:** FOUNDATION_V0_1 / SPECIALIST_ROLE_MAP_ACTIVE / CURRENT_SES_ROUTING_ENTRYPOINT

This adapter describes the StopJuniorMode protocol/research project registered in the SES Project Registry and points to its project-owned canonical sources.

It intentionally contains stable routing metadata and source-precedence rules, not copied StopJuniorMode operational truth.

```text
PROJECT_ID: stopjuniormode
PROJECT_NAME: StopJuniorMode / SFJM Protocol
CANONICAL_SOURCE: GitHub repository wagnerjfjunior/StopJuniorMode
DEFAULT_REF_OR_RESOLUTION_RULE: resolve live main before material work
BOOTSTRAP_ENTRYPOINT: docs/SFJM_BOOTSTRAP_V1.md
CONTINUITY_ENTRYPOINT: docs/CANONICAL_BOOTSTRAP_PROTOCOL.md
PROJECT_STATUS_ENTRYPOINT: docs/PILOT_STATUS_DASHBOARD.md when status context is material
NEXT_SAFE_ACTION_ENTRYPOINT: docs/NEXT_SAFE_ACTION.md
SPECIALIST_ENTRYPOINT_OR_RESOLUTION_RULE: exact SPECIALIST_ROLE_MAP below plus applicable canonical StopJuniorMode sources
MANUAL_HANDOFF_CONTRACT: core/protocols/MANUAL_SPECIALIST_HANDOFF_CONTRACT.md
```

## Canonical StopJuniorMode source priority

For project-specific material work, resolve state in this order:

```text
1. live main of wagnerjfjunior/StopJuniorMode
2. docs/SFJM_BOOTSTRAP_V1.md
3. docs/CANONICAL_BOOTSTRAP_PROTOCOL.md
4. docs/NEXT_SAFE_ACTION.md
5. applicable current handoff / status / evidence documents
6. other versioned StopJuniorMode documents material to the task
```

The Project Adapter does not override project-owned canonicality.

## Project boundary

StopJuniorMode is the canonical repository for the SFJM protocol, protocol governance, research and protocol evidence.

It is separate from:

`wagnerjfjunior/sfjm-workspace`

SFJM Workspace is a product/workspace consumer of SFJM principles. Workspace UX, implementation or lifecycle decisions do not modify the protocol unless a separate explicitly authorized StopJuniorMode protocol change is made.

Consumer projects such as FECH.AI remain authoritative for their own product state, lifecycle, security, runtime and authorizations.

## Specialist role map

StopJuniorMode explicitly adopts only the following current certified SES archetypes:

```text
SPECIALIST_ROLE_MAP:

- ROLE: architecture
  ARCHETYPE_ID: software-systems-architect
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: resolve protocol architecture, authority boundaries, compatibility and evidence exclusively through StopJuniorMode canonical sources
  LEGACY_ALIASES: none

- ROLE: documentation_audit
  ARCHETYPE_ID: documentation-auditor
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: resolve protocol documentation, evidence and continuity exclusively through StopJuniorMode canonical sources
  LEGACY_ALIASES: none
```

No other current certified SES archetype is adopted by this adapter.

In particular, this registration does not automatically adopt:

- backend_data;
- application_security;
- ux_ui;
- seo specialists;
- lead_operations;
- paid_search_sem;
- any future specialist archetype.

Any later adoption requires a separate explicit project decision and versioned SES change.

## Resolution flow

For StopJuniorMode project-specific specialist work:

```text
explicit PROJECT_IDENTIFIER = stopjuniormode
+ explicit ROLE
→ projects/REGISTRY.md
→ this Project Adapter
→ exact SPECIALIST_ROLE_MAP match
→ archetypes/REGISTRY.md
→ ACTIVE archetype
→ current certification eligibility
→ resolve wagnerjfjunior/StopJuniorMode main live
→ read docs/SFJM_BOOTSTRAP_V1.md
→ read docs/CANONICAL_BOOTSTRAP_PROTOCOL.md
→ read docs/NEXT_SAFE_ACTION.md
→ read other versioned sources material to the task
→ resolve live GitHub evidence material to the target
→ Context Readiness
→ bounded specialist work
```

Do not infer an unmapped specialist role from repository content, project name or task semantics.

## Manual handoff identity rule

For any SES-selected specialist consultation, apply the universal manual handoff contract before rendering the human copy/paste destination.

```text
ARCHETYPE_ID
→ archetypes/REGISTRY.md
→ CANONICAL_NAME
→ SPECIALIST_TARGET_NAME
```

Project-local rules remain context only and must not replace canonical SES specialist identity.

## Audit / architecture boundary

Adopted specialists may review StopJuniorMode protocol architecture and documentation but do not gain authority to:

- mark a pull request Ready;
- merge;
- mutate protocol files;
- change historical research evidence;
- alter consumer projects;
- change SFJM Workspace;
- accept risk or alter project objectives on behalf of Product Authority.

Those authorities remain project-local and must be resolved from StopJuniorMode canonical sources and explicit user authorization.

## Adapter non-authority

This adapter does not own or freeze:

- StopJuniorMode current main SHA;
- current PR/head/check state;
- current next safe action;
- current research/evidence status;
- protocol truth;
- Product Authority decisions.

Those remain owned by the StopJuniorMode repository and current live/project-local sources.

Preserve:

```text
REGISTERED != AUTHORIZED
ADOPTED != PROJECT_CONTEXT_READY
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
ADOPTED != READY_AUTHORIZATION
ADOPTED != MERGE_AUTHORIZATION
SFJM_WORKSPACE != STOPJUNIORMODE_PROTOCOL
```
