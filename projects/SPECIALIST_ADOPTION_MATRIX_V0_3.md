# SES — Certified Specialist Adoption Matrix v0.3

**Status:** `PROJECT_PORTFOLIO_DECISION / USER_AUTHORIZED / REPRESENTATION_CORRECTED / 2026-08-26`
**Previous version:** `projects/SPECIALIST_ADOPTION_MATRIX_V0_2.md`
**Correction:** preserves the same MoreNumTegra/Blogs product decision while restoring canonical `ADOPTION_STATUS: ADOPTED`; provider/delegation is represented separately as project-local execution metadata.

## Scope

This matrix records which currently certified SES specialists are adopted by registered consumer projects and which repositories remain pending classification. It is not a rule that future certified specialists are automatically adopted.

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

## Matrix

| Repository / project | Decision |
|---|---|
| `wagnerjfjunior/fecha.ai` / `fechai` | adopt all currently certified specialists |
| `wagnerjfjunior/Blogs-sites-portais-seo` / `blogs-sites-portais-seo` | adopt all currently certified specialists except `backend-data-platform-specialist` |
| `wagnerjfjunior/MoreNumTegra` / `morenumtegra` | direct adoption for Documentation Auditor, Software Systems Architect, UX/UI and AppSec; Search roles (`seo_strategy`, `technical_seo`, `content_semantic_seo`, `seo_analytics_growth`, `paid_search_sem`) are `ADOPTED`; their project-local execution mode delegates Search work to provider `blogs-sites-portais-seo`; `backend-data-platform-specialist` remains not adopted |
| `wagnerjfjunior/StopJuniorMode` | `PENDING_PROJECT_CLASSIFICATION`; no consumer adoption inferred |
| `wagnerjfjunior/sfjm-workspace` | `PENDING_PROJECT_CLASSIFICATION`; no consumer adoption inferred |
| `wagnerjfjunior/orquestrador-ai` | `PENDING_PROJECT_CLASSIFICATION / ROLE_FIT`; no consumer adoption inferred |
| `wagnerjfjunior/Specialist-Engineering-System` | not treated as a consumer project; specialists remain available for engineering, testing and reference implementations without circular consumer adoption |

## Current-state consequence

FECH.AI already satisfied the authorized matrix before this change and therefore requires no no-op adapter mutation.

Blogs/Sites/Portais/SEO is the explicit Search Center of Expertise / provider for MoreNumTegra's currently certified Search roles. MoreNumTegra retains product, implementation, deploy, budget, publication and risk authority.

Local SEO and Authority & Digital PR are future service intent only; they are not current certification/adoption and require a later explicit activation decision after certification.

Backend/Data remains explicitly not adopted in MoreNumTegra and Blogs/Sites/Portais/SEO. This is a current product/project decision, not a universal claim that those repositories can never need backend/data specialization.

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
```

Future portfolio changes require an explicit adoption decision; they do not mutate this matrix automatically.