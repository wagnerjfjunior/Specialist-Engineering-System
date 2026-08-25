# SES Project Adapter — MoreNumTegra

**Status:** FOUNDATION_V0_2 / REGISTERED_CONSUMER_PROJECT / SPECIALIST_ROLE_MAP_ACTIVE

This adapter describes the `morenumtegra` consumer project registered in the SES Project Registry and points to project-owned canonical sources. It stores stable locators only; MoreNumTegra remains authoritative for product truth, continuity, environments, authorization and runtime state.

```text
PROJECT_ID: morenumtegra
PROJECT_NAME: MoreNumTegra
CANONICAL_SOURCE: GitHub repository wagnerjfjunior/MoreNumTegra
DEFAULT_REF_OR_RESOLUTION_RULE: resolve live main before material work
BOOTSTRAP_ENTRYPOINT: bootstrap/BOOTSTRAP_CANONICO.md
CONTINUITY_ENTRYPOINT: handoffs/CURRENT.md
SPECIALIST_ENTRYPOINT_OR_RESOLUTION_RULE: bootstrap/BOOTSTRAP_CANONICO.md section "Integração SES e resolução de especialistas" plus this adapter SPECIALIST_ROLE_MAP
GOVERNANCE_ENTRYPOINT: bootstrap/BOOTSTRAP_CANONICO.md plus docs/PROJECT_STATUS.md when project governance/state is material
AUTHORITY_ENTRYPOINT: bootstrap/BOOTSTRAP_CANONICO.md plus docs/NEXT_SAFE_ACTION.md and docs/BLOCKED_ACTIONS.md when mutation/lifecycle authority is material
ENVIRONMENT_ENTRYPOINT: docs/baseline/TECHNICAL_BASELINE_V1.md plus docs/PROJECT_STATUS.md when environment/architecture state is material
```

## Specialist role map

MoreNumTegra explicitly adopts the following certified SES archetype:

```text
SPECIALIST_ROLE_MAP:

- ROLE: seo_strategy
  ARCHETYPE_ID: seo-strategy-governance-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: NOT_APPLICABLE; resolve MoreNumTegra product/search rules through project bootstrap and current project sources
```

Unmapped specialist roles remain not adopted and must fail closed as `SPECIALIST_ROLE_NOT_ADOPTED`. Do not infer adoption from project stack, product scope, archetype certification, specialist availability, role similarity or prior use in another project.

## Resolution flow

For SES-mediated MoreNumTegra work:

```text
explicit PROJECT_IDENTIFIER = morenumtegra (or an explicit registered alias)
+ explicit ROLE
→ projects/REGISTRY.md
→ this Project Adapter
→ exact SPECIALIST_ROLE_MAP match
→ if absent: SPECIALIST_ROLE_NOT_ADOPTED
→ if adopted: resolve archetypes/REGISTRY.md
→ resolve docs/SPECIALIST_CERTIFICATION_STATUS.md
→ require current certification eligibility
→ resolve wagnerjfjunior/MoreNumTegra main live
→ read bootstrap/BOOTSTRAP_CANONICO.md
→ follow the project bootstrap reading order
→ read project-local specialist rules/overrides if later established and applicable
→ read continuity/authority sources when material
→ resolve material live evidence
→ Context Readiness
→ bounded specialist work
```

## Project-owned boundaries

MoreNumTegra owns:

- functional and technical baselines;
- current `main` and lifecycle state;
- product implementation and Preview/Production state;
- project authority and mutation permissions;
- environments, domain/DNS and external integrations;
- project-local specialist rules/overrides if later introduced;
- data, secrets and operational evidence.

SES owns only reusable contracts, certification/archetype state and this stable registration/adapter metadata.

## Authority rule

```text
REGISTERED != ADOPTED
ADOPTED != PROJECT_CONTEXT_READY
ROUTABLE != EXECUTED
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
TOOL_CAPABILITY != AUTHORIZATION
```

This adapter does not authorize implementation, Preview, Production, domain/DNS changes, data processing, campaigns, merges or any consumer-project mutation.

## Adoption rule

Each `ROLE -> ARCHETYPE_ID` mapping is a separate explicit project adoption decision. Certification or Gateway availability never auto-adopts future roles. Future certified Search/Discovery specialists must be adopted individually when MoreNumTegra needs them.