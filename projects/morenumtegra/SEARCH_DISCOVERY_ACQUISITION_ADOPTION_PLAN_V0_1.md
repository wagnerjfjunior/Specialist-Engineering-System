# MoreNumTegra — Search, Discovery & Acquisition Adoption Plan v0.1

**Status:** PROJECT_ADOPTION_PLAN_CANDIDATE / NO_ROLE_ADOPTED / NO_MUTATION_AUTHORITY

This document records a candidate adoption path for future SES Search, Discovery & Acquisition specialists. It does not modify the authoritative `SPECIALIST_ROLE_MAP` in `projects/morenumtegra/PROJECT_ADAPTER.md`.

## 1. Current project state

The current Project Adapter remains authoritative and currently declares:

```text
NO_SPECIALIST_ROLES_ADOPTED
SPECIALIST_ROLE_MAP: <empty>
```

This plan must not be interpreted as adoption.

## 2. Candidate adoption order after certification

When the corresponding reusable SES archetypes reach the required lifecycle/certification state, MoreNumTegra should evaluate explicit adoption in this order:

```text
P0  SEO_STRATEGY
    -> candidate: seo-strategy-governance-specialist

P0  TECHNICAL_SEO
    -> candidate: technical-seo-specialist

P0  CONTENT_SEMANTIC_SEO
    -> candidate: content-semantic-seo-specialist

P1  SEO_ANALYTICS_GROWTH
    -> candidate: seo-analytics-growth-specialist
    -> blocked from operational adoption until project analytics/tags/pixels authority gate is opened

P2  LOCAL_SEO
    -> future candidate only after eligible real-world local business/entity target is defined

P2  PAID_SEARCH_SEM
    -> future candidate only after tracking/conversion and campaign/spend authority gates are opened

P2  AUTHORITY_DIGITAL_PR
    -> future candidate based on demonstrated off-page/authority demand
```

## 3. Current exclusions

Backend & Data Platform is not a Search-domain prerequisite for the current MoreNumTegra V1 and is not proposed here merely because a certified SES archetype exists.

Application Security Assurance remains available for explicit consultation/adoption when the task creates a material AppSec surface; this plan does not silently adopt it.

## 4. MoreNumTegra reference-use cases

Potential bounded cases for future specialist validation/adoption include:

- mobile-first and performance-first technical SEO;
- Vercel Preview/Production index-control and canonicality;
- catalog crawlability/indexability;
- real-estate entity and semantic modeling;
- neighborhood, typology and development search intent;
- GEO / generative-discovery citability and entity clarity;
- Search Console/GA4 only after project measurement gates are explicitly opened;
- Google Business Profile/Maps only after eligible business/location representation is established;
- SEM only after conversion measurement and spend/campaign authority are established.

## 5. Adoption gate

No role may be added to `PROJECT_ADAPTER.md` until all applicable conditions are satisfied:

```text
REUSABLE ARCHETYPE EXISTS
+ required certification/evidence state is satisfied
+ project role need is confirmed
+ project-local delta/boundary review is complete
+ explicit project adoption decision exists
= role may be versioned into SPECIALIST_ROLE_MAP
```

Preserve:

```text
PLANNED != ADOPTED
CERTIFIED_FOR_ANY_PROJECT != CONSUMER_PROJECT_ADOPTED
ADOPTED != EXECUTED
EXECUTED != AUTHORIZED_TO_MUTATE
CENTRAL_EVOLUTION != AUTOMATIC_PROJECT_MUTATION
```
