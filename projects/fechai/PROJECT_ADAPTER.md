# SES Project Adapter — FECH.AI

**Status:** REFERENCE_IMPLEMENTATION / FOUNDATION_V0_3 / SPECIALIST_ROLE_MAP_ACTIVE

This adapter describes the FECH.AI project registered in the SES Project Registry and points to its project-owned canonical sources. It intentionally contains pointers, not copied FECH.AI operational truth.

```text
PROJECT_ID: fechai
PROJECT_NAME: FECH.AI — Projeto Principal / Master Project
CANONICAL_SOURCE: GitHub repository wagnerjfjunior/fecha.ai
DEFAULT_REF_OR_RESOLUTION_RULE: resolve live main before material work
BOOTSTRAP_ENTRYPOINT: docs/bootstrap/INDEX.md
CONTINUITY_ENTRYPOINT: docs/sfjm/INDEX.md
SPECIALIST_ENTRYPOINT_OR_RESOLUTION_RULE: docs/skills/fechai-gpt-registry.md
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
```

The GPT labels above are continuity/history pointers, not current SES archetype identities. They do not override the explicit role map.

Unmapped FECH.AI-local specialist domains (for example current CI/CD, SRE/observability, Ads/tracking, LeadOps, MesaCliente, integrations and monetization roles) remain project-local until FECH.AI explicitly adopts an applicable certified SES archetype. The Gateway must not infer or auto-adopt a replacement.

## Resolution flow

For FECH.AI project-specific specialist work routed through the Runtime Enforcement Gateway:

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
→ ROUTABLE
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

For FECH.AI-local domains not adopted through the role map, continue using the project-owned specialist registry/rules. `SPECIALIST_ROLE_NOT_ADOPTED` must not trigger semantic guessing.

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
ROUTABLE != EXECUTED
```

## Reference-implementation rule

FECH.AI may provide evidence for reusable SES patterns, but a FECH.AI rule does not become universal merely because this is the first registered project.

`REFERENCE IMPLEMENTATION != UNIVERSAL AUTHORITY`
