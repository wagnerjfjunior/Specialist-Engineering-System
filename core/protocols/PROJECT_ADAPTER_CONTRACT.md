# SES — Project Adapter Contract

**Status:** FOUNDATION_V0_2 / CONTRACT

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

## 3. Specialist role map

A project may adopt reusable SES specialists by declaring a compact `SPECIALIST_ROLE_MAP` in its Project Adapter.

The universal mapping unit is:

```text
PROJECT_ROLE -> ARCHETYPE_ID
```

Each active mapping must contain:

```text
ROLE
ARCHETYPE_ID
ADOPTION_STATUS: ADOPTED
```

Optional project-local metadata may include a pointer to local specialist rules/overrides and explicit legacy aliases. It must not copy the SES archetype contract, Builder package, runtime fingerprint or volatile certification state.

Example shape:

```text
SPECIALIST_ROLE_MAP:
- ROLE: architecture
  ARCHETYPE_ID: software-systems-architect
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: <project-owned pointer or NOT_APPLICABLE>
```

Semantics:

```text
ROLE = stable project-facing capability key
ARCHETYPE_ID = deterministic SES archetype identifier
ADOPTED = explicit project routing decision
```

A role name is project-local. SES does not impose a universal catalog of project roles.

The map must not perform semantic/fuzzy routing. A request must arrive with, or be deterministically classified by an explicitly versioned project/runtime rule into, one role before this mapping is consulted.

Preserve:

```text
ARCHETYPE ACTIVE != PROJECT ADOPTED
CERTIFIED_FOR_ANY_PROJECT != PROJECT ADOPTED
PROJECT ADOPTED != PROJECT_CONTEXT_READY
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
```

Missing mapping for a requested role is `SPECIALIST_ROLE_NOT_ADOPTED`; do not guess a nearby archetype.

A mapped archetype that is missing, inactive or not certification-eligible for the applicable gateway policy must fail closed at runtime. The adapter must not cache those volatile states.

## 4. Prohibited duplication

An adapter must not copy volatile or authoritative project state such as:

- current main SHA as project truth;
- current PR/head/check status;
- production state;
- current blockers;
- current decisions;
- user/tenant data;
- secrets or credentials;
- full project governance text;
- full specialist skills owned by the project;
- SES runtime fingerprints or certification ledgers.

If provenance of adapter creation is recorded, it must be clearly historical and must not be interpreted as the current project state.

## 5. Resolution semantics

For project-specific work:

```text
USER-SUPPLIED PROJECT NAME/ID
→ SES PROJECT REGISTRY
→ UNIQUE PROJECT_ID + ADAPTER_PATH
→ SES PROJECT ADAPTER
→ OPTIONAL ROLE -> ARCHETYPE_ID ADOPTION RESOLUTION
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

## 6. Authority boundary

Registering a project or adopting an archetype does not grant SES or any specialist authority to mutate that project.

`REGISTERED != AUTHORIZED`

`ADOPTED != AUTHORIZED`

`TOOL CAPABILITY != PROJECT AUTHORIZATION`

Project-local authority must be resolved from the project-owned authority/bootstrap sources.

## 7. Versioning and adoption

Registry entries and adapters are versioned in SES.

Changing registry metadata changes how SES resolves a project identifier. Changing an adapter changes project-resolution pointers or explicit specialist adoption. Neither change may silently change consumer-project content or authority.

A consumer project does not automatically adopt unrelated SES changes merely because SES `main` advances.

An existing `ROLE -> ARCHETYPE_ID` adoption remains a project decision across non-material compatible SES evolution, but runtime eligibility must always be re-evaluated live by the Gateway. A material archetype identity replacement or incompatible adoption change requires an explicit adapter update and proportional project validation.
