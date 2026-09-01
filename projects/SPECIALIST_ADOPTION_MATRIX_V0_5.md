# SES — Certified Specialist Adoption Matrix v0.5

**Status:** `PROJECT_PORTFOLIO_DECISION / USER_AUTHORIZED / LEADOPS_CERTIFIED_AND_FECHAI_ADOPTED / 2026-09-01`
**Previous version:** `projects/SPECIALIST_ADOPTION_MATRIX_V0_4.md`
**Change:** adds the newly certified `lead-operations-crm-specialist` to the SES portfolio and explicitly adopts it only in FECH.AI. Existing adoption decisions for other projects remain unchanged.

## Scope

This matrix records which currently certified SES specialists are adopted by registered consumer projects and which repositories remain pending classification.

It is not a rule that future certified specialists are automatically adopted.

Current certified portfolio at the decision point:

- `documentation-auditor`
- `software-systems-architect`
- `ux-ui-app-specialist`
- `backend-data-platform-specialist`
- `application-security-assurance-specialist`
- `seo-strategy-governance-specialist`
- `technical-seo-specialist`
- `content-semantic-seo-specialist`
- `seo-analytics-growth-specialist`
- `paid-search-sem-specialist`
- `lead-operations-crm-specialist`

## Matrix

| Repository / project | Decision |
|---|---|
| `wagnerjfjunior/fecha.ai` / `fechai` | adopt all currently certified specialists, now including `lead_operations -> lead-operations-crm-specialist` |
| `wagnerjfjunior/Blogs-sites-portais-seo` / `blogs-sites-portais-seo` | existing adoption unchanged; `lead-operations-crm-specialist` is NOT_ADOPTED |
| `wagnerjfjunior/MoreNumTegra` / `morenumtegra` | existing adoption unchanged; `lead-operations-crm-specialist` is NOT_ADOPTED |
| `wagnerjfjunior/sfjm-workspace` / `sfjm-workspace` | adopt `documentation-auditor` only; `lead-operations-crm-specialist` is NOT_ADOPTED and must not be inferred |
| `wagnerjfjunior/StopJuniorMode` | `PENDING_PROJECT_CLASSIFICATION`; no consumer adoption inferred |
| `wagnerjfjunior/orquestrador-ai` | `PENDING_PROJECT_CLASSIFICATION / ROLE_FIT`; no consumer adoption inferred |
| `wagnerjfjunior/Specialist-Engineering-System` | not treated as a consumer project; specialists remain available for engineering, testing and reference implementations without circular consumer adoption |

## SFJM Workspace decision

The SFJM Workspace classification is deliberately minimal.

```text
PROJECT_ID: sfjm-workspace
CURRENT_ADOPTED_ROLE:
  documentation_audit -> documentation-auditor

ALL_OTHER_CURRENT_CERTIFIED_SPECIALISTS:
  NOT_ADOPTED / NO INFERENCE
```

This decision exists to support bounded independent documentation auditing through a deterministic SES project-resolution path.

It does not imply adoption of architecture, UX/UI, AppSec, Backend/Data, Search or any future specialist merely because SFJM Workspace may later need those disciplines.

Later role adoption requires a separate explicit decision.

## Current-state consequence

FECH.AI, Blogs/Sites/Portais/SEO and MoreNumTegra retain the exact adoption decisions recorded in v0.3.

Blogs/Sites/Portais/SEO remains the explicit Search Center of Expertise / provider for MoreNumTegra's currently certified Search roles. MoreNumTegra retains product, implementation, deploy, budget, publication and risk authority.

Local SEO and Authority & Digital PR remain future service intent only; they are not current certification/adoption and require a later explicit activation decision after certification.

Backend/Data remains explicitly not adopted in MoreNumTegra and Blogs/Sites/Portais/SEO.

SFJM Workspace is now a registered consumer project with only Documentation Auditor adopted. Its product truth remains in `wagnerjfjunior/sfjm-workspace`, while SFJM protocol truth remains in `wagnerjfjunior/StopJuniorMode`.

## Boundaries

```text
CERTIFIED_FOR_ANY_PROJECT != CONSUMER_PROJECT_ADOPTED
SPECIALIST_AVAILABLE != SPECIALIST_ADOPTED_BY_PROJECT
ADOPTED != PROJECT_CONTEXT_READY
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
CURRENT_MATRIX != FUTURE_AUTO_ADOPTION
PENDING_PROJECT_CLASSIFICATION != PROJECT_REGISTERED
SES_ENGINEERING_USE != SES_CONSUMER_ADOPTION
CROSS_PROJECT_SERVICE != PROJECT_OWNERSHIP_TRANSFER
PROVIDER_SPECIALIST_WORK != CONSUMER_PROJECT_MUTATION
FUTURE_SERVICE_INTENT != CURRENT_ADOPTION
PROJECT_LOCAL_EXECUTION_MODE != UNIVERSAL_ADOPTION_STATUS
SFJM_WORKSPACE_REGISTERED != ALL_SPECIALISTS_ADOPTED
WORKSPACE_PRODUCT != SFJM_PROTOCOL
```

Future portfolio changes require an explicit adoption decision; they do not mutate this matrix automatically.


## Lead Operations & CRM adoption decision

```text
ARCHETYPE_ID = lead-operations-crm-specialist
CERTIFIED_FOR_ANY_PROJECT = YES

FECHAI:
  ROLE = lead_operations
  ADOPTION_STATUS = ADOPTED
  PROJECT_LOCAL_RULES = docs/skills/fechai-gpt7-leadops-crm-discador.md
  LEGACY_CONTINUITY = GPT7 / FECH.AI LeadOps CRM Discador

BLOGS_SITES_PORTAIS_SEO = NOT_ADOPTED
MORENUMTEGRA = NOT_ADOPTED
SFJM_WORKSPACE = NOT_ADOPTED
```

This adoption changes FECH.AI routing only. It does not grant mutation authority and does not cause central SES evolution to mutate other consumer projects automatically.
