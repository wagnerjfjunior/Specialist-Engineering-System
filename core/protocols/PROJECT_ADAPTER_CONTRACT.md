# SES — Project Adapter Contract

**Status:** FOUNDATION_V0_1 / CONTRACT

## 1. Purpose

A Project Adapter describes one consumer project already registered in SES and tells specialists where to find that project's own canonical context.

The Project Registry performs SES-side project-name/ID resolution. The adapter is the next locator/manifest in the chain. It is not the source of truth for the consumer project.

## 2. Required fields

Every registered project adapter must identify:

```text
PROJECT_ID
PROJECT_NAME
CANONICAL_SOURCE
DEFAULT_REF_OR_RESOLUTION_RULE
BOOTSTRAP_ENTRYPOINT
CONTINUITY_ENTRYPOINT
SPECIALIST_ENTRYPOINT_OR_RESOLUTION_RULE
```

When applicable, it should also identify pointers for:

```text
GOVERNANCE_ENTRYPOINT
AUTHORITY_ENTRYPOINT
ENVIRONMENT_ENTRYPOINT
```

The adapter may declare `NOT_APPLICABLE` only when the project contract explicitly makes that category unnecessary.

## 3. Prohibited duplication

An adapter must not copy volatile or authoritative project state such as:

- current main SHA as project truth;
- current PR/head/check status;
- production state;
- current blockers;
- current decisions;
- user/tenant data;
- secrets or credentials;
- full project governance text;
- full specialist skills owned by the project.

If provenance of adapter creation is recorded, it must be clearly historical and must not be interpreted as the current project state.

## 4. Resolution semantics

For project-specific work:

```text
USER-SUPPLIED PROJECT NAME/ID
→ SES PROJECT REGISTRY
→ UNIQUE PROJECT_ID + ADAPTER_PATH
→ SES PROJECT ADAPTER
→ CANONICAL PROJECT SOURCE
→ LIVE REF RESOLUTION
→ PROJECT BOOTSTRAP
→ PROJECT CONTINUITY WHEN MATERIAL
→ SPECIALIST/DOMAIN SOURCES
→ TASK WORK
```

Project-name/ID mapping must be resolved by `projects/REGISTRY.md`. The adapter must not be guessed from a folder name or inferred alias.

If no unique registry entry resolves, use `PROJECT_NOT_REGISTERED` or `PROJECT_ID_AMBIGUOUS` rather than guessing an adapter.

If the registry is unavailable, use `PROJECT_REGISTRY_UNAVAILABLE`.

If the resolved adapter points to an unavailable or contradictory source, use `PROJECT_ADAPTER_UNRESOLVED` and fail closed for claims that depend on that source.

## 5. Authority boundary

Registering a project in SES does not grant SES or any specialist authority to mutate that project.

`REGISTERED != AUTHORIZED`

`TOOL CAPABILITY != PROJECT AUTHORIZATION`

Project-local authority must be resolved from the project-owned authority/bootstrap sources.

## 6. Versioning

Registry entries and adapters are versioned in SES.

Changing registry metadata changes how SES resolves a project identifier. Changing an adapter changes project-resolution pointers. Neither change may silently change consumer-project content or authority.

A consumer project does not automatically adopt unrelated SES changes merely because SES `main` advances.
