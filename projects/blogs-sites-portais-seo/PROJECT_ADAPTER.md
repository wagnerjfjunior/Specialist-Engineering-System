# SES Project Adapter — Ecossistema de Blogs, Sites, Portais e SEO

**Status:** FOUNDATION_V0_2 / REGISTERED_CONSUMER_PROJECT / SPECIALIST_ROLE_MAP_ACTIVE / CERTIFIED_PORTFOLIO_MATRIX_APPLIED

This adapter describes the `blogs-sites-portais-seo` consumer project registered in the SES Project Registry and points to project-owned canonical sources. It intentionally contains stable locators only; it does not copy or freeze project operational truth.

```text
PROJECT_ID: blogs-sites-portais-seo
PROJECT_NAME: Ecossistema de Blogs, Sites, Portais e SEO
CANONICAL_SOURCE: GitHub repository wagnerjfjunior/Blogs-sites-portais-seo
DEFAULT_REF_OR_RESOLUTION_RULE: resolve live main before material work
BOOTSTRAP_ENTRYPOINT: bootstrap/BOOTSTRAP_CANONICO.md
CONTINUITY_ENTRYPOINT: handoffs/CURRENT.md
SPECIALIST_ENTRYPOINT_OR_RESOLUTION_RULE: config/gpts.yaml plus this adapter SPECIALIST_ROLE_MAP
GOVERNANCE_ENTRYPOINT: resolve through bootstrap/BOOTSTRAP_CANONICO.md and applicable docs/governance sources
AUTHORITY_ENTRYPOINT: bootstrap/BOOTSTRAP_CANONICO.md plus docs/NEXT_SAFE_ACTION.md and docs/BLOCKED_ACTIONS.md when mutation/lifecycle authority is material
ENVIRONMENT_ENTRYPOINT: config/project.yaml plus docs/PROJECT_STATUS.md when environment/project-state evidence is material
```

## Specialist role map

The project explicitly adopts the following certified SES archetypes while preserving its project-local GPT registry and specialist contracts:

```text
SPECIALIST_ROLE_MAP:

- ROLE: documentation_audit
  ARCHETYPE_ID: documentation-auditor
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: resolve applicable project-local documentation/audit contract through config/gpts.yaml and bootstrap

- ROLE: architecture
  ARCHETYPE_ID: software-systems-architect
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: resolve project-local architecture/platform rules through bootstrap, config/project.yaml and applicable project sources

- ROLE: ux_ui
  ARCHETYPE_ID: ux-ui-app-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: resolve project-local UX/UI, brand, publishing-surface and experience rules through config/gpts.yaml and applicable project sources

- ROLE: application_security
  ARCHETYPE_ID: application-security-assurance-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: resolve project-local security, privacy, active-test authority and risk-acceptance rules through bootstrap/governance sources

- ROLE: seo_strategy
  ARCHETYPE_ID: seo-strategy-governance-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: resolve project-local SEO strategy/governance contract through config/gpts.yaml and applicable project sources

- ROLE: technical_seo
  ARCHETYPE_ID: technical-seo-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: resolve project-local technical SEO contract through config/gpts.yaml and applicable project sources

- ROLE: content_semantic_seo
  ARCHETYPE_ID: content-semantic-seo-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: resolve project-local content/semantic/GEO contract through config/gpts.yaml and applicable project sources

- ROLE: seo_analytics_growth
  ARCHETYPE_ID: seo-analytics-growth-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: resolve project-local analytics/growth/conversion definitions and data rules through config/gpts.yaml and applicable project sources

- ROLE: paid_search_sem
  ARCHETYPE_ID: paid-search-sem-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: resolve project-local paid-search accounts, budgets, conversion definitions, tracking/privacy/legal rules and spend/publication authority through bootstrap, config/gpts.yaml and applicable project sources
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
→ resolve wagnerjfjunior/Blogs-sites-portais-seo main live
→ read bootstrap/BOOTSTRAP_CANONICO.md
→ follow its mandatory reading order
→ read handoffs/CURRENT.md
→ read docs/PROJECT_STATUS.md
→ read docs/NEXT_SAFE_ACTION.md
→ read docs/BLOCKED_ACTIONS.md
→ read config/project.yaml
→ resolve the applicable local specialist through config/gpts.yaml
→ for a specific GPT, read its canonical document, skill, Builder instructions/manifest and tests as required by project bootstrap
→ resolve live GitHub/environment evidence material to the requested decision
→ Context Readiness
→ perform only bounded work permitted by project-local authority
```

## Project-owned boundaries

The project currently defines its own specialist registry (`config/gpts.yaml`), project manifest (`config/project.yaml`), bootstrap, lifecycle/SFJM continuity and authorization semantics. SES must consume those sources through this adapter rather than duplicate them.

The project-local registry currently includes `gpt0` through `gpt8`. Their external Builder identities and project-specific contracts remain project-owned until an explicitly validated SES migration retires a legacy Builder.

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