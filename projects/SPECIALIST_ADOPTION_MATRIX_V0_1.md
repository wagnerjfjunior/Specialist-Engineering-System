# SES — Certified Specialist Adoption Matrix v0.1

**Status:** `PROJECT_PORTFOLIO_DECISION / USER_AUTHORIZED / 2026-08-25`

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
| `wagnerjfjunior/MoreNumTegra` / `morenumtegra` | adopt all currently certified specialists except `backend-data-platform-specialist` |
| `wagnerjfjunior/StopJuniorMode` | `PENDING_PROJECT_CLASSIFICATION`; no consumer adoption inferred |
| `wagnerjfjunior/sfjm-workspace` | `PENDING_PROJECT_CLASSIFICATION`; no consumer adoption inferred |
| `wagnerjfjunior/orquestrador-ai` | `PENDING_PROJECT_CLASSIFICATION / ROLE_FIT`; no consumer adoption inferred |
| `wagnerjfjunior/Specialist-Engineering-System` | not treated as a consumer project; specialists remain available for engineering, testing and reference implementations without circular consumer adoption |

## Current-state consequence

FECH.AI already satisfied the authorized matrix before this change and therefore requires no no-op adapter mutation.

MoreNumTegra and Blogs/Sites/Portais/SEO require adapter expansion to reach the authorized matrix.

Backend/Data remains explicitly not adopted in those two projects. This is a current product/project decision, not a universal claim that those repositories can never need backend/data specialization.

## Boundaries

```text
CERTIFIED_FOR_ANY_PROJECT != CONSUMER_PROJECT_ADOPTED
SPECIALIST_AVAILABLE != SPECIALIST_ADOPTED_BY_PROJECT
ADOPTED != PROJECT_CONTEXT_READY
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
CURRENT_MATRIX != FUTURE_AUTO_ADOPTION
PENDING_PROJECT_CLASSIFICATION != PROJECT_REGISTERED
SES_ENGINEERING_USE != SES_CONSUMER_ADOPTION
```

Future portfolio changes require an explicit adoption decision; they do not mutate this matrix automatically.