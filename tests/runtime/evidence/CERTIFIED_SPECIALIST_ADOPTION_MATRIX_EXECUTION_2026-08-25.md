# Certified Specialist Adoption Matrix — Execution Evidence — 2026-08-25

**Decision source:** explicit Product Authority approval of the proposed matrix in conversation.  
**SES base SHA:** `a3e59795c06d6447caa5ec6771aaa5991f537fd3`

## Preconditions

The canonical certification ledger at the base SHA listed ten `Certification = YES` archetypes: Documentation Auditor, Software Systems Architect, UX/UI APP, Backend & Data Platform, Application Security Assurance, SEO Strategy & Governance, Technical SEO, Content & Semantic SEO, SEO Analytics & Growth, and Paid Search & SEM.

## Applied decisions

### FECH.AI
Already had all ten currently certified archetypes adopted before this change. No no-op mutation was made.

### MoreNumTegra
Expanded from the five Search/Discovery roles to the complete currently certified applicable portfolio by adding:
- `documentation_audit -> documentation-auditor`
- `architecture -> software-systems-architect`
- `ux_ui -> ux-ui-app-specialist`
- `application_security -> application-security-assurance-specialist`

Existing Search/Discovery adoptions remain intact. `backend-data-platform-specialist` is explicitly not adopted under the current V1 architecture decision.

### Blogs-sites-portais-seo
Added the complete currently certified applicable SES portfolio while preserving the project-owned `config/gpts.yaml` contracts and legacy Builder lifecycle. Adopted roles are Documentation Audit, Architecture, UX/UI, Application Security, SEO Strategy, Technical SEO, Content & Semantic SEO, SEO Analytics & Growth, and Paid Search & SEM.

`backend-data-platform-specialist` is explicitly not adopted at this time.

### Repositories intentionally unchanged
- `wagnerjfjunior/StopJuniorMode`: `PENDING_PROJECT_CLASSIFICATION`
- `wagnerjfjunior/sfjm-workspace`: `PENDING_PROJECT_CLASSIFICATION`
- `wagnerjfjunior/orquestrador-ai`: `PENDING_PROJECT_CLASSIFICATION / ROLE_FIT`
- `wagnerjfjunior/Specialist-Engineering-System`: not modeled as a consumer project; specialist use remains engineering/testing/reference-implementation use.

## Safety properties

```text
NO_FUTURE_AUTO_ADOPTION = TRUE
NO_LEGACY_BUILDER_RETIREMENT = TRUE
NO_CONSUMER_REPOSITORY_MUTATION = TRUE
NO_CAMPAIGN_OR_RUNTIME_MUTATION = TRUE
ADOPTED != PROJECT_CONTEXT_READY
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
```

This change updates SES-side adapters/matrix only. It does not alter any consumer repository or grant mutation authority.