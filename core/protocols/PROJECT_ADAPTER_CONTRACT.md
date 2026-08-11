# SES — Project Adapter Contract

**Status:** FOUNDATION_V0_1 / CONTRACT

## 1. Purpose

A Project Adapter registers a consumer project with SES and tells specialists where to find the project's own canonical context.

The adapter is a locator/manifest. It is not the source of truth for the consumer project.

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
PROJECT NAME/ID
→ SES PROJECT ADAPTER
→ CANONICAL PROJECT SOURCE
→ LIVE REF RESOLUTION
→ PROJECT BOOTSTRAP
→ PROJECT CONTINUITY WHEN MATERIAL
→ SPECIALIST/DOMAIN SOURCES
→ TASK WORK
```

If the project is not registered, use `PROJECT_NOT_REGISTERED` rather than guessing an adapter.

If the adapter points to an unavailable or contradictory source, use `PROJECT_ADAPTER_UNRESOLVED` and fail closed for claims that depend on that source.

## 5. Authority boundary

Registering a project in SES does not grant SES or any specialist authority to mutate that project.

`REGISTERED != AUTHORIZED`

`TOOL CAPABILITY != PROJECT AUTHORIZATION`

Project-local authority must be resolved from the project-owned authority/bootstrap sources.

## 6. Versioning

Adapters are versioned in SES. Changing an adapter changes project resolution metadata only; it must not silently change consumer-project content.

A consumer project does not automatically adopt unrelated SES changes merely because SES `main` advances.
