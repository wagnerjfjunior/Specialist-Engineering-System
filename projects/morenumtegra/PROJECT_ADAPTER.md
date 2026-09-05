# SES Project Adapter — MoreNumTegra

**Status:** FOUNDATION_V0_9 / REGISTERED_CONSUMER_PROJECT / SPECIALIST_ROLE_MAP_ACTIVE / PROJECT_LOCAL_SEARCH_PROVIDER_MODEL_APPLIED

This adapter describes the `morenumtegra` consumer project registered in the SES Project Registry and points to project-owned canonical sources. It stores stable locators only; MoreNumTegra remains authoritative for product truth, continuity, environments, authorization and runtime state.

```text
PROJECT_ID: morenumtegra
PROJECT_NAME: MoreNumTegra
CANONICAL_SOURCE: GitHub repository wagnerjfjunior/MoreNumTegra
DEFAULT_REF_OR_RESOLUTION_RULE: resolve live main before material work
BOOTSTRAP_ENTRYPOINT: bootstrap/BOOTSTRAP_CANONICO.md
CONTINUITY_ENTRYPOINT: handoffs/CURRENT.md
SPECIALIST_ENTRYPOINT_OR_RESOLUTION_RULE: bootstrap/BOOTSTRAP_CANONICO.md section 10 "Integração SES / SFJM" plus this adapter SPECIALIST_ROLE_MAP
MANUAL_HANDOFF_CONTRACT: core/protocols/MANUAL_SPECIALIST_HANDOFF_CONTRACT.md
GOVERNANCE_ENTRYPOINT: bootstrap/BOOTSTRAP_CANONICO.md plus docs/PROJECT_STATUS.md when project governance/state is material
AUTHORITY_ENTRYPOINT: bootstrap/BOOTSTRAP_CANONICO.md plus docs/NEXT_SAFE_ACTION.md and docs/BLOCKED_ACTIONS.md when mutation/lifecycle authority is material
ENVIRONMENT_ENTRYPOINT: docs/baseline/TECHNICAL_BASELINE_V2_2.md plus docs/PROJECT_STATUS.md when environment/architecture state is material
```

## Specialist role map

MoreNumTegra uses two execution modes: direct project-local adoption for core product/engineering roles, and a project-local cross-project specialist service for the Search domain. The service provider is `blogs-sites-portais-seo`; MoreNumTegra retains product, implementation, deploy, budget, publication and risk authority.

```text
SPECIALIST_ROLE_MAP:

- ROLE: documentation_audit
  ARCHETYPE_ID: documentation-auditor
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: NOT_APPLICABLE; resolve MoreNumTegra documentation, evidence, lifecycle and authority truth through project bootstrap and current project sources

- ROLE: architecture
  ARCHETYPE_ID: software-systems-architect
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: NOT_APPLICABLE; resolve MoreNumTegra architecture, environments, deployment topology and target-state authority through project bootstrap and current project sources

- ROLE: ux_ui
  ARCHETYPE_ID: ux-ui-app-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: NOT_APPLICABLE; resolve MoreNumTegra product, brand, UX, accessibility, mobile and implementation truth through project bootstrap and current project sources

- ROLE: application_security
  ARCHETYPE_ID: application-security-assurance-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: NOT_APPLICABLE; resolve MoreNumTegra security scope, data handling, active-test authority, risk acceptance and implementation truth through project bootstrap and current project sources

- ROLE: seo_strategy
  ARCHETYPE_ID: seo-strategy-governance-specialist
  ADOPTION_STATUS: ADOPTED
  EXECUTION_MODE: PROJECT_LOCAL_CROSS_PROJECT_SERVICE
  SERVICE_PROVIDER_PROJECT_ID: blogs-sites-portais-seo
  PROJECT_LOCAL_RULES: MoreNumTegra owns product/search objectives, implementation authority and acceptance boundaries; provider resolves Search method/evidence through its own project context and returns bounded recommendations/results

- ROLE: technical_seo
  ARCHETYPE_ID: technical-seo-specialist
  ADOPTION_STATUS: ADOPTED
  EXECUTION_MODE: PROJECT_LOCAL_CROSS_PROJECT_SERVICE
  SERVICE_PROVIDER_PROJECT_ID: blogs-sites-portais-seo
  PROJECT_LOCAL_RULES: MoreNumTegra owns implementation/runtime truth; provider may diagnose/recommend Technical SEO changes but cannot mutate MoreNumTegra without separate authorization

- ROLE: content_semantic_seo
  ARCHETYPE_ID: content-semantic-seo-specialist
  ADOPTION_STATUS: ADOPTED
  EXECUTION_MODE: PROJECT_LOCAL_CROSS_PROJECT_SERVICE
  SERVICE_PROVIDER_PROJECT_ID: blogs-sites-portais-seo
  PROJECT_LOCAL_RULES: MoreNumTegra owns brand/product/commercial/factual truth and publication authority; provider performs Content/Semantic SEO analysis and recommendations against supplied/live evidence

- ROLE: seo_analytics_growth
  ARCHETYPE_ID: seo-analytics-growth-specialist
  ADOPTION_STATUS: ADOPTED
  EXECUTION_MODE: PROJECT_LOCAL_CROSS_PROJECT_SERVICE
  SERVICE_PROVIDER_PROJECT_ID: blogs-sites-portais-seo
  PROJECT_LOCAL_RULES: MoreNumTegra owns KPI/conversion definitions, consent/privacy constraints and business-value truth; provider performs Search analytics/growth analysis without redefining project truth

- ROLE: paid_search_sem
  ARCHETYPE_ID: paid-search-sem-specialist
  ADOPTION_STATUS: ADOPTED
  EXECUTION_MODE: PROJECT_LOCAL_CROSS_PROJECT_SERVICE
  SERVICE_PROVIDER_PROJECT_ID: blogs-sites-portais-seo
  PROJECT_LOCAL_RULES: MoreNumTegra owns ad accounts, billing, budgets, conversion definitions, tracking/consent constraints and spend/publication authority; provider may design/recommend/measure campaigns but cannot spend or publish without separate MoreNumTegra authorization
```

## Cross-project Search service

This is a PROJECT-LOCAL integration decision and a reference-implementation candidate, not a universal SES rule. The Search capabilities remain canonically `ADOPTED`; `EXECUTION_MODE: PROJECT_LOCAL_CROSS_PROJECT_SERVICE` is local execution/delegation metadata only and does not create a new SES adoption status or prove provider runtime execution.

```text
CONSUMER_PROJECT: morenumtegra
SERVICE_PROVIDER_PROJECT_ID: blogs-sites-portais-seo
SERVICE_DOMAIN: SEARCH_DISCOVERY_ACQUISITION

CURRENT_SERVICE_ROLES:
- seo_strategy
- technical_seo
- content_semantic_seo
- seo_analytics_growth
- paid_search_sem

FUTURE_SERVICE_INTENT:
- local_seo
- authority_digital_pr

FUTURE_SERVICE_INTENT != CURRENT_ADOPTION
FUTURE_SERVICE_INTENT != CERTIFIED_FOR_ANY_PROJECT
```

Operational semantics:

```text
MORENUMTEGRA
→ defines objective / target / authority boundary
→ explicit cross-project Search handoff
→ blogs-sites-portais-seo resolves its own live project context
→ exact Search ROLE -> ARCHETYPE_ID
→ bounded specialist analysis / strategy / recommendation / measurement
→ result returned to MoreNumTegra
→ MoreNumTegra adjudicates and authorizes any product/code/deploy/spend/publication mutation
```

Preserve:

```text
BLOGS_SEARCH_SERVICE != MORENUMTEGRA_PRODUCT_AUTHORITY
SEARCH_RECOMMENDATION != IMPLEMENTATION_AUTHORIZATION
BUDGET_RECOMMENDATION != SPEND_AUTHORIZATION
CAMPAIGN_DESIGNED != CAMPAIGN_PUBLISHED
CROSS_PROJECT_SERVICE != PROJECT_OWNERSHIP_TRANSFER
PROVIDER_CONTEXT_READY != CONSUMER_PROJECT_MUTATION_AUTHORITY
```
## Portfolio coverage decision

The matrix decision applies only to the certified portfolio existing at the time of this adoption. It does not auto-adopt future specialists.

```text
CURRENT_CERTIFIED_PORTFOLIO_COVERAGE: CORE_DIRECT_PLUS_SEARCH_VIA_BLOGS_EXCEPT_BACKEND_DATA
backend-data-platform-specialist: EXPLICITLY_NOT_ADOPTED
REASON: current MoreNumTegra V1 baseline does not require a project-owned backend/data-platform specialist; re-evaluate only after a material architecture change or explicit Product Authority decision
FUTURE_CERTIFIED_SPECIALIST: NOT_AUTO_ADOPTED
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
→ resolve docs/SPECIALIST_CERTIFICATION_STATUS.md
→ require current certification eligibility for the exact ARCHETYPE_ID
→ resolve wagnerjfjunior/MoreNumTegra main live
→ read bootstrap/BOOTSTRAP_CANONICO.md
→ follow the project bootstrap reading order
→ read project-local specialist rules/overrides if later established and applicable
→ read continuity/authority sources when material
→ resolve material MoreNumTegra live evidence and authority boundaries
→ MoreNumTegra Context Readiness
→ if ADOPTED and no project-local delegated execution mode applies: bounded specialist work in MoreNumTegra context
→ if ADOPTED with EXECUTION_MODE = PROJECT_LOCAL_CROSS_PROJECT_SERVICE: resolve SERVICE_PROVIDER_PROJECT_ID = blogs-sites-portais-seo through projects/REGISTRY.md and its Project Adapter
→ resolve the provider project's own live bootstrap/context required for the Search service
→ create an explicit provenance-preserving cross-project handoff bound to the MoreNumTegra task/target/evidence/authority boundary
→ bounded provider work + returned result
→ any MoreNumTegra mutation requires separate MoreNumTegra authority
```


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

This adapter does not authorize implementation, Preview, Production, domain/DNS changes, data processing, campaigns, spend, billing, publication, merges or any consumer-project mutation.

## Adoption rule

Each `ROLE -> ARCHETYPE_ID` mapping is a separate explicit project adoption decision. A Search role remains `ADOPTED`; when it carries `EXECUTION_MODE: PROJECT_LOCAL_CROSS_PROJECT_SERVICE`, execution is delegated through the named provider project without transferring MoreNumTegra authority. Certification or availability never auto-adopts future roles. Local SEO and Authority & Digital PR are recorded only as future service intent until they are certified and a later explicit activation/adoption decision is made.