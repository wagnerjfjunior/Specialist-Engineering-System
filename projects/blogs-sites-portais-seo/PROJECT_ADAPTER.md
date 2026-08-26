# SES Project Adapter — Ecossistema de Blogs, Sites, Portais e SEO

**Status:** FOUNDATION_V0_2 / REGISTERED_CONSUMER_PROJECT / SPECIALIST_ROLE_MAP_ACTIVE / CERTIFIED_PORTFOLIO_MATRIX_APPLIED

This adapter describes the `blogs-sites-portais-seo` consumer project registered in the SES Project Registry and points to project-owned canonical sources. It intentionally contains stable locators only; it does not copy or freeze project operational truth.

```text
PROJECT_ID: blogs-sites-portais-seo
PROJECT_NAME: Ecossistema de Blogs, Sites, Portais e SEO
CANONICAL_SOURCE: GitHub repository wagnerjfjunior/Blogs-sites-portais-seo
DEFAULT_REF_OR_RESOLUTION_RULE: resolve the exact consumer-project TARGET_REF required by the task; resolve live main when main is the intended target and do not substitute main for an explicitly identified PR/head/immutable ref
BOOTSTRAP_ENTRYPOINT: bootstrap/BOOTSTRAP_CANONICO.md
CONTINUITY_ENTRYPOINT: handoffs/CURRENT.md
SPECIALIST_ENTRYPOINT_OR_RESOLUTION_RULE: resolve exact ROLE through this adapter SPECIALIST_ROLE_MAP; on the resolved consumer-project ref, use config/specialists.yaml when present as project-local adoption authority; use config/gpts.yaml only as explicit legacy compatibility/history when config/specialists.yaml is absent or when legacy Builder retirement/equivalence evidence is required
GOVERNANCE_ENTRYPOINT: resolve through bootstrap/BOOTSTRAP_CANONICO.md and applicable docs/governance sources
AUTHORITY_ENTRYPOINT: bootstrap/BOOTSTRAP_CANONICO.md plus docs/NEXT_SAFE_ACTION.md and docs/BLOCKED_ACTIONS.md when mutation/lifecycle authority is material
ENVIRONMENT_ENTRYPOINT: config/project.yaml plus docs/PROJECT_STATUS.md when environment/project-state evidence is material
```

## Specialist role map

The project explicitly adopts the following certified SES archetypes. Project-local adoption/routing is ref-aware: migrated refs use `config/specialists.yaml` when present; pre-migration refs may consult `config/gpts.yaml` only as legacy compatibility/history. Legacy GPT assets remain preserved for continuity and retirement evidence.

```text
SPECIALIST_ROLE_MAP:

- ROLE: documentation_audit
  ARCHETYPE_ID: documentation-auditor
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: resolve applicable project-local documentation/audit rules through config/specialists.yaml when present on the resolved ref plus bootstrap; use config/gpts.yaml only for pre-migration compatibility/history or legacy retirement evidence

- ROLE: architecture
  ARCHETYPE_ID: software-systems-architect
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: resolve project-local architecture/platform rules through bootstrap, config/project.yaml and applicable project sources

- ROLE: ux_ui
  ARCHETYPE_ID: ux-ui-app-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: resolve project-local UX/UI, brand, publishing-surface and experience rules through config/specialists.yaml when present on the resolved ref plus applicable project sources; legacy GPT sources are continuity/history only

- ROLE: application_security
  ARCHETYPE_ID: application-security-assurance-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: resolve project-local security, privacy, active-test authority and risk-acceptance rules through bootstrap/governance sources

- ROLE: seo_strategy
  ARCHETYPE_ID: seo-strategy-governance-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: resolve project-local SEO strategy/governance rules through config/specialists.yaml when present on the resolved ref plus applicable project sources; legacy GPT sources are continuity/history only

- ROLE: technical_seo
  ARCHETYPE_ID: technical-seo-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: resolve project-local technical SEO rules through config/specialists.yaml when present on the resolved ref plus applicable project sources; legacy GPT sources are continuity/history only

- ROLE: content_semantic_seo
  ARCHETYPE_ID: content-semantic-seo-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: resolve project-local content/semantic/GEO rules through config/specialists.yaml when present on the resolved ref plus applicable project sources; legacy GPT sources are continuity/history only

- ROLE: seo_analytics_growth
  ARCHETYPE_ID: seo-analytics-growth-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: resolve project-local analytics/growth/conversion definitions and data rules through config/specialists.yaml when present on the resolved ref plus applicable project sources; legacy GPT sources are continuity/history only

- ROLE: paid_search_sem
  ARCHETYPE_ID: paid-search-sem-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: resolve project-local paid-search accounts, budgets, conversion definitions, tracking/privacy/legal rules and spend/publication authority through bootstrap, config/specialists.yaml when present on the resolved ref and applicable project sources; legacy GPT sources are continuity/history only
```

## Portfolio coverage decision

The matrix decision applies only to the certified SES portfolio existing at the time of this adoption. It does not auto-adopt future specialists.

```text
CURRENT_CERTIFIED_PORTFOLIO_COVERAGE: ALL_APPLICABLE_EXCEPT_BACKEND_DATA
backend-data-platform-specialist: EXPLICITLY_NOT_ADOPTED
REASON: no current project need has been established for a standalone Backend & Data Platform role; project-local automation/runtime components do not by themselves justify adoption
FUTURE_CERTIFIED_SPECIALIST: NOT_AUTO_ADOPTED
```

Unmapped specialist roles remain not adopted and must fail closed as `SPECIALIST_ROLE_NOT_ADOPTED`.

## Resolution flow

For project-specific specialist work:

```text
explicit PROJECT_IDENTIFIER = blogs-sites-portais-seo
+ explicit ROLE
→ projects/REGISTRY.md
→ this Project Adapter
→ exact SPECIALIST_ROLE_MAP match
→ if absent: SPECIALIST_ROLE_NOT_ADOPTED
→ if adopted: resolve archetypes/REGISTRY.md
→ resolve docs/SPECIALIST_CERTIFICATION_STATUS.md
→ require current certification eligibility
→ resolve the exact consumer-project TARGET_REF required by the task; use live main only when main is the intended target
→ read bootstrap/BOOTSTRAP_CANONICO.md on that exact resolved ref
→ follow its mandatory reading order
→ read handoffs/CURRENT.md
→ read docs/PROJECT_STATUS.md
→ read docs/NEXT_SAFE_ACTION.md
→ read docs/BLOCKED_ACTIONS.md
→ read config/project.yaml
→ if config/specialists.yaml exists on the resolved ref: use it as project-local specialist adoption/routing authority
→ if config/specialists.yaml does not exist on that ref: enter explicit PRE_MIGRATION_LEGACY_COMPATIBILITY and consult config/gpts.yaml only as legacy project-local evidence
→ never infer GPT<number> -> ARCHETYPE_ID semantically or by list position
→ read legacy GPT canonical document/skill/Builder manifest/instructions/tests only when required for pre-migration compatibility, historical evidence, equivalence analysis or Builder retirement
→ resolve live GitHub/environment evidence material to the requested decision
→ Context Readiness
→ perform only bounded work permitted by project-local authority
```

## Project-owned boundaries

The project owns its specialist-adoption state, project manifest (`config/project.yaml`), bootstrap, lifecycle/SFJM continuity and authorization semantics. SES must consume those sources through this adapter rather than duplicate them.

Routing/adoption authority is ref-aware:

```text
MIGRATED_REF_WITH_config/specialists.yaml
→ config/specialists.yaml = project-local specialist adoption/routing authority

PRE_MIGRATION_REF_WITHOUT_config/specialists.yaml
→ config/gpts.yaml = explicit legacy compatibility/history source only
```

The legacy project-local registry `config/gpts.yaml`, GPT0–GPT8 identities, external Builder IDs/URLs, manifests, skills, instructions and tests remain project-owned continuity/history artifacts until an explicitly validated migration and separately authorized Builder retirement occur.

`LEGACY_GPT_LABEL != CURRENT_SES_IDENTITY`

## Boundary

This adapter does not own or freeze:

- the consumer project's current `main` SHA;
- PR/head/base/check/review/thread state;
- current next lifecycle transition;
- current Builder field values or behavioral parity;
- current assets, domains, metrics, traffic, revenue or production state;
- project-local GPT skills or acceptance tests;
- Product Authority decisions;
- credentials, secrets or user data.

Those remain owned by `wagnerjfjunior/Blogs-sites-portais-seo` and its authoritative project-local/live sources.

## Authority rule

```text
REGISTERED != ADOPTED
ADOPTED != PROJECT_CONTEXT_READY
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
CERTIFIED_FOR_ANY_PROJECT != CONSUMER_PROJECT_ADOPTED
```

The consumer project's current policy is READ_ONLY by default for the GitHub specialist Action. Corrections, Ready, merge, Builder changes, deploy, publication, domain/DNS changes, campaigns and other mutations remain governed by project-owned authorization sources.

## Migration rule

Adoption of an SES archetype does not retire or silently replace any existing project-bound GPT. A legacy Builder may be retired only after the relevant SES archetype is independently validated for project-local equivalence where required and the retirement gate is explicitly authorized.

Preserve:

```text
SES_ADOPTION != LEGACY_BUILDER_RETIREMENT
RENAME != BEHAVIORAL_EQUIVALENCE
PRE_MIGRATION_REF != MIGRATED_REF
CONFIG_SPECIALISTS_PRESENT != LEGACY_BUILDER_RETIRED
```