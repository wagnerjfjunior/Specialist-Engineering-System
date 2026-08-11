# SES — Specialist Archetype Registry

**Status:** RUNTIME_CANDIDATE_V0_1 / ARCHETYPE_RESOLUTION_AUTHORITY

## 1. Purpose

This registry is the SES authority for resolving a reusable specialist archetype identifier into one versioned archetype contract.

It owns reusable specialist-engineering metadata only. It does not own consumer-project truth, project-local authority, runtime state, project-local specialist identities or current project decisions.

## 2. Resolution rules

Archetype resolution must be deterministic:

1. trim surrounding whitespace;
2. match exact `ARCHETYPE_ID` first;
3. otherwise match `CANONICAL_NAME` or an explicit alias case-insensitively;
4. do not use fuzzy matching or semantic guessing for material specialist resolution;
5. require exactly one match whose `RESOLUTION_STATUS` is `ACTIVE`.

Fail closed when no unique active archetype resolves.

`RESOLUTION_STATUS` is the only field that determines registry eligibility. Lifecycle/version labels such as `RUNTIME_CANDIDATE_V0_1` describe maturity and must not be interpreted as active/inactive resolution state.

## 3. Registered archetypes

### SaaS Architect

```text
ARCHETYPE_ID: saas-architect
CANONICAL_NAME: SES — SaaS Architect
ALIASES:
- SaaS Architect
- SES SaaS Architect
CONTRACT_PATH: archetypes/saas-architect/ARCHETYPE.md
RESOLUTION_STATUS: ACTIVE
LIFECYCLE_STATUS: RUNTIME_CANDIDATE_V0_1
```

The SaaS Architect archetype provides reusable architecture method, reasoning modes, trust-boundary analysis and proof obligations. It does not replace project-local specialist rules.

For project-specific work, the runtime must resolve the consumer project's own specialist/override sources after project bootstrap. A project-local architectural specialist may refine or restrict this archetype; its identity must be resolved from that project's canonical sources and must not be frozen in this registry.

## 4. Boundary

```text
ARCHETYPE = REUSABLE METHOD
PROJECT SPECIALIST = PROJECT-LOCAL OVERRIDE / AUTHORITY BOUNDARY
```

`ARCHETYPE_RESOLVED != PROJECT_CONTEXT_READY`

`ARCHETYPE_RESOLVED != AUTHORIZED_TO_MUTATE`

## 5. Change discipline

Adding, removing, renaming, aliasing or changing `RESOLUTION_STATUS` of an archetype changes specialist-resolution behavior and requires a versioned SES change with behavioral evidence proportional to the impact.
