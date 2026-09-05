# SES Project Adapter — FECH.AI

**Status:** REFERENCE_IMPLEMENTATION / FOUNDATION_V0_8 / SPECIALIST_ROLE_MAP_ACTIVE / CURRENT_SES_ROUTING_ENTRYPOINT

This adapter describes the FECH.AI project registered in the SES Project Registry and points to its project-owned canonical sources. It intentionally contains pointers, not copied FECH.AI operational truth.

```text
PROJECT_ID: fechai
PROJECT_NAME: FECH.AI — Projeto Principal / Master Project
CANONICAL_SOURCE: GitHub repository wagnerjfjunior/fecha.ai
DEFAULT_REF_OR_RESOLUTION_RULE: resolve live main before material work
BOOTSTRAP_ENTRYPOINT: docs/bootstrap/INDEX.md
CONTINUITY_ENTRYPOINT: docs/sfjm/INDEX.md
SPECIALIST_ENTRYPOINT_OR_RESOLUTION_RULE: docs/skills/SES_SPECIALIST_ROUTING.md for SES-adopted roles; docs/skills/fechai-gpt-registry.md only for unmapped project-local domains and explicit legacy continuity
MANUAL_HANDOFF_CONTRACT: core/protocols/MANUAL_SPECIALIST_HANDOFF_CONTRACT.md
GOVERNANCE_ENTRYPOINT: docs/governance/INDEX.md when applicable
AUTHORITY_ENTRYPOINT: resolve through the FECH.AI bootstrap and applicable canonical governance/continuity sources
ENVIRONMENT_ENTRYPOINT: docs/bootstrap/2026-06-10-fechai-saas-current-state-index.md
```

## Specialist role map

FECH.AI explicitly adopts the following current certified SES archetypes for these project-facing roles:

```text
SPECIALIST_ROLE_MAP:

- ROLE: documentation_audit
  ARCHETYPE_ID: documentation-auditor
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: docs/skills/fechai-gpt0-documentation-auditor.md
  LEGACY_ALIASES: GPT0 / FECH.AI Documentation Auditor

- ROLE: architecture
  ARCHETYPE_ID: software-systems-architect
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: docs/skills/fechai-gpt1-architect-saas.md
  LEGACY_ALIASES: GPT1 / GPT1.5 / FECH.AI Arquiteto SaaS

- ROLE: ux_ui
  ARCHETYPE_ID: ux-ui-app-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: docs/skills/fechai-gpt2-ux-ui-app-specialist.md
  LEGACY_ALIASES: GPT2 / FECH.AI UX/UI APP Specialist

- ROLE: backend_data
  ARCHETYPE_ID: backend-data-platform-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: docs/skills/fechai-gpt3-supabase-security-specialist.md
  LEGACY_ALIASES: GPT3 for project-local Supabase/data continuity only

- ROLE: application_security
  ARCHETYPE_ID: application-security-assurance-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: NOT_APPLICABLE; resolve FECH.AI security/project rules through project bootstrap
  LEGACY_ALIASES: none

- ROLE: seo_strategy
  ARCHETYPE_ID: seo-strategy-governance-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: NOT_APPLICABLE; resolve FECH.AI search/product/commercial rules through project bootstrap and current project sources
  LEGACY_ALIASES: none

- ROLE: technical_seo
  ARCHETYPE_ID: technical-seo-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: NOT_APPLICABLE; resolve FECH.AI technical/search implementation truth through project bootstrap and current project sources
  LEGACY_ALIASES: none

- ROLE: content_semantic_seo
  ARCHETYPE_ID: content-semantic-seo-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: NOT_APPLICABLE; resolve FECH.AI content, brand, product, commercial, legal and factual truth through project bootstrap and current project sources
  LEGACY_ALIASES: none

- ROLE: seo_analytics_growth
  ARCHETYPE_ID: seo-analytics-growth-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: NOT_APPLICABLE; resolve FECH.AI KPIs, conversion definitions, analytics properties, consent/privacy/legal rules and business-value truth through project bootstrap and current project sources
  LEGACY_ALIASES: none

- ROLE: lead_operations
  ARCHETYPE_ID: lead-operations-crm-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: docs/skills/fechai-gpt7-leadops-crm-discador.md
  LEGACY_ALIASES: GPT7 / FECH.AI LeadOps CRM Discador Specialist

- ROLE: paid_search_sem
  ARCHETYPE_ID: paid-search-sem-specialist
  ADOPTION_STATUS: ADOPTED
  PROJECT_LOCAL_RULES: NOT_APPLICABLE; resolve FECH.AI ad accounts, budgets, billing, conversion definitions, tracking/consent/privacy/legal rules, campaign targets and spend/publication authority through project bootstrap and current project sources
  LEGACY_ALIASES: none
```

The GPT labels above are continuity/history pointers, not current SES archetype identities. They do not override the explicit role map.

Unmapped FECH.AI-local specialist domains (for example current CI/CD, SRE/observability, non-Search paid media/tracking implementation, MesaCliente, integrations and monetization roles) remain project-local until FECH.AI explicitly adopts an applicable certified SES archetype. The Gateway must not infer or auto-adopt a replacement.

## Resolution flow

For FECH.AI project-specific specialist work:

```text
explicit PROJECT_IDENTIFIER = fechai
+ explicit ROLE
→ projects/REGISTRY.md
→ this Project Adapter
→ exact SPECIALIST_ROLE_MAP match
→ archetypes/REGISTRY.md
→ ACTIVE archetype
→ docs/SPECIALIST_CERTIFICATION_STATUS.md
→ current certification eligibility
→ resolve current SES handoff/transport semantics when consultation is material
→ resolve wagnerjfjunior/fecha.ai main live
→ read docs/bootstrap/INDEX.md
→ read PROJECT_LOCAL_RULES when mapped/applicable
→ read common project operating rules required by bootstrap
→ read governance when applicable
→ read docs/sfjm/INDEX.md and required continuity views when current-state continuity is material
→ resolve live GitHub/environment evidence material to the decision
→ Context Readiness
→ bounded specialist work
```

For FECH.AI-local domains not adopted through the role map, continue using the project-owned specialist registry/rules. The legacy registry must not override any SES-adopted role. `SPECIALIST_ROLE_NOT_ADOPTED` must not trigger semantic guessing.


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


## Consumer handoff / certification boundary

Manual consultation of an adopted SES role follows the current SES Manual Specialist Handoff Contract.

```text
ADOPTED ROLE
+ ACTIVE ARCHETYPE
+ CURRENT SES LEDGER CERTIFICATION = YES
→ CONSUMER CONSULTATION ELIGIBLE

NONCURRENT SES CANDIDATE EXISTS
!= CONSUMER PROJECT BLOCKED

CONSUMER_RECERTIFICATION_DETOUR_FORBIDDEN = YES
```

A noncurrent Builder/runtime candidate must not become this consumer project's next safe action unless the project task explicitly requires that exact candidate fingerprint as a certified dependency. Project-local tool evidence remains usable within its own tool/evidence contract and must not be promoted to universal runtime certification.

## Boundary

This file does not own or freeze:

- FECH.AI current main SHA;
- current PR/head/check state;
- current production/deployment state;
- current blockers or next action;
- FECH.AI specialist skill contents;
- current SES runtime fingerprint/certification state;
- project authority decisions;
- security state;
- tenants, users or data.

Those remain owned by FECH.AI and its authoritative live/project-local sources, or by current SES canonical lifecycle sources where applicable.

Preserve:

```text
ADOPTED != PROJECT_CONTEXT_READY
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
SPECIALIST_AVAILABLE != EXECUTED
ADOPTED != EXECUTED
```

## Reference-implementation rule

FECH.AI may provide evidence for reusable SES patterns, but a FECH.AI rule does not become universal merely because this is the first registered project.

`REFERENCE IMPLEMENTATION != UNIVERSAL AUTHORITY`
