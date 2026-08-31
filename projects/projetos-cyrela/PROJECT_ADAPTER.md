# SES Project Adapter — Projetos Cyrela

**Status:** REGISTERED_CONSUMER_PROJECT / LEGACY_RECOVERY_BOOTSTRAP / SPECIALIST_ROLE_MAP_ACTIVE

This adapter describes the `projetos-cyrela` consumer project and points to project-owned canonical sources. It stores stable locators only; `wagnerjfjunior/ProjetosCyrela` remains authoritative for product truth, historical recovery, continuity, environments, authorization and runtime state.

```text
PROJECT_ID: projetos-cyrela
PROJECT_NAME: Projetos Cyrela
CANONICAL_SOURCE: GitHub repository wagnerjfjunior/ProjetosCyrela
DEFAULT_REF_OR_RESOLUTION_RULE: resolve live main before material work; if a task is explicitly bound to a PR/head/ref, resolve that exact target instead
BOOTSTRAP_ENTRYPOINT: bootstrap/BOOTSTRAP_CANONICO.md
CONTINUITY_ENTRYPOINT: handoffs/CURRENT.md
SPECIALIST_ENTRYPOINT_OR_RESOLUTION_RULE: config/specialists.yaml on the resolved consumer-project ref
GOVERNANCE_ENTRYPOINT: bootstrap/BOOTSTRAP_CANONICO.md plus docs/CURRENT_STATE.md and docs/PROJECT_STATUS.md
AUTHORITY_ENTRYPOINT: docs/NEXT_SAFE_ACTION.md plus docs/BLOCKED_ACTIONS.md when mutation/lifecycle authority is material
ENVIRONMENT_ENTRYPOINT: resolve project-local environment documentation and live evidence only when material; do not infer from connector/tool availability
```

## Specialist role map

The consumer project explicitly adopts the following SES archetypes on refs where `config/specialists.yaml` contains the corresponding active mapping:

```text
SPECIALIST_ROLE_MAP:

- ROLE: documentation_audit
  ARCHETYPE_ID: documentation-auditor
  ADOPTION_STATUS: ADOPTED

- ROLE: architecture
  ARCHETYPE_ID: software-systems-architect
  ADOPTION_STATUS: ADOPTED

- ROLE: ux_ui
  ARCHETYPE_ID: ux-ui-app-specialist
  ADOPTION_STATUS: ADOPTED

- ROLE: application_security
  ARCHETYPE_ID: application-security-assurance-specialist
  ADOPTION_STATUS: ADOPTED

- ROLE: seo_strategy
  ARCHETYPE_ID: seo-strategy-governance-specialist
  ADOPTION_STATUS: ADOPTED

- ROLE: technical_seo
  ARCHETYPE_ID: technical-seo-specialist
  ADOPTION_STATUS: ADOPTED

- ROLE: content_semantic_seo
  ARCHETYPE_ID: content-semantic-seo-specialist
  ADOPTION_STATUS: ADOPTED

- ROLE: seo_analytics_growth
  ARCHETYPE_ID: seo-analytics-growth-specialist
  ADOPTION_STATUS: ADOPTED

- ROLE: paid_search_sem
  ARCHETYPE_ID: paid-search-sem-specialist
  ADOPTION_STATUS: ADOPTED
```

`backend-data-platform-specialist` is explicitly not adopted by the current project bootstrap. Tool access to Supabase or the existence of future backend/data work does not itself establish adoption. Re-evaluate only through a later explicit consumer-project decision.

An Integrated Marketing specialist must not be inferred or auto-adopted unless an exact active SES archetype exists and the consumer project explicitly adopts it.

## Recovery-specific semantics

The project predates SFJM and contains significant historical knowledge in old conversations and artifacts. Therefore project-context readiness requires preserving the consumer project's evidence classes:

```text
ESTABLISHED
DOCUMENTED_NOT_INDEPENDENTLY_CONFIRMED
PLANNED
CONTRADICTED
UNKNOWN
```

Historical chat/document claims must not be silently upgraded into current production truth.

`HISTORICAL_AS_BUILT != CURRENT_LIVE_STATE`

`SOURCE_RECOVERED != PRODUCTION_REVALIDATED`

## Resolution flow

```text
explicit PROJECT_IDENTIFIER = projetos-cyrela (or explicit registered alias)
+ explicit ROLE
→ projects/REGISTRY.md
→ this Project Adapter
→ exact SPECIALIST_ROLE_MAP match
→ if absent: SPECIALIST_ROLE_NOT_ADOPTED
→ resolve archetypes/REGISTRY.md
→ require current active/certified eligibility applicable to the task
→ resolve exact consumer-project target ref
→ read bootstrap/BOOTSTRAP_CANONICO.md
→ follow mandatory reading order
→ read config/specialists.yaml
→ read docs/CURRENT_STATE.md
→ read docs/PROJECT_STATUS.md
→ read handoffs/CURRENT.md
→ read docs/NEXT_SAFE_ACTION.md and docs/BLOCKED_ACTIONS.md when authority is material
→ read applicable recovery/domain documentation
→ resolve live evidence only when needed for the requested decision
→ Context Readiness
→ bounded specialist work
```

## Project-owned boundaries

Projetos Cyrela owns:

- current repository/main and lifecycle truth;
- production site and page truth;
- SEO/GEO/AI objectives and factual/commercial content;
- tracking/measurement/consent truth;
- Vercel/Supabase/DNS/GTM/Ads/CRM environments and authority;
- historical recovery and evidence classification;
- specialist adoption and project-local overrides;
- publication, spend, deploy, risk and mutation authority.

SES owns only reusable contracts, archetype/certification state and this stable registration/adapter metadata.

## Authority rule

```text
REGISTERED != PROJECT_CONTEXT_READY
ADOPTED != AUTHORIZED_TO_MUTATE
TOOL_CAPABILITY != AUTHORIZATION
HISTORICAL_EVIDENCE != CURRENT_RUNTIME_PROOF
```

This adapter does not authorize production implementation, deployments, DNS changes, data changes, tracking publication, campaign spend/publication or any other consumer-project mutation.
