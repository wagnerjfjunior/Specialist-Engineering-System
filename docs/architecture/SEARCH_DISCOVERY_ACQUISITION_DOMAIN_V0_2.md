# SES — Search, Discovery & Acquisition Domain v0.2

**Status:** `DOMAIN_CANDIDATE_V0_2 / SEVEN_BUILDER_READY_CANDIDATES / PRE_RUNTIME`  
**Supersedes for current design:** v0.1, preserving v0.1 as historical initial architecture.

## Canonical candidate topology
```text
SEARCH, DISCOVERY & ACQUISITION
|
+-- Organic Search & Generative Discovery
|   +-- SEO Strategy & Governance
|   +-- Technical SEO
|   +-- Content & Semantic SEO
|   |   +-- GEO / Generative Engine Optimization capability
|   +-- SEO Analytics & Growth
|   +-- Local SEO
|   +-- Authority & Digital PR
|
+-- Paid Search
|   +-- Paid Search & SEM
|
+-- Shared evidence/measurement surfaces
    +-- Google Search Central / Search Console
    +-- GA4 / GTM / Looker Studio
    +-- PageSpeed / CrUX / Lighthouse
    +-- SERP + site live
    +-- Semrush / Ahrefs / equivalent when available
    +-- Google Business Profile / Maps / local ecosystems
    +-- Google Ads / Microsoft Ads when configured
```

## Boundary rules
- `TOOL != SPECIALIST_BOUNDARY`.
- `SEO != SEM`.
- `GEO_GENERATIVE != GEO_GEOGRAPHIC`.
- GEO generative remains cross-cutting across Strategy, Technical, Content/Semantic and measurement; no standalone GEO archetype yet.
- Local SEO owns geographic/local discovery, eligibility, profiles, NAP, reviews/citations and local landing architecture.
- Authority/Digital PR owns links/mentions/earned authority but not brand/legal/outreach authorization.
- Paid Search/SEM owns paid-search method but not spend/publication authority.
- Measurement evidence is shared; ownership follows the claim.

## Current candidate archetypes
```text
seo-strategy-governance-specialist
technical-seo-specialist
content-semantic-seo-specialist
seo-analytics-growth-specialist
local-seo-specialist
authority-digital-pr-specialist
paid-search-sem-specialist
```

All seven have Candidate contract, candidate Archetype, Builder Package/Kernel, L1 suite and L2 runbook. None is registry ACTIVE or certified until the runtime lifecycle is proven.

## Consumer-project model
One reusable SES archetype may be adopted by many projects through explicit `ROLE -> ARCHETYPE_ID` mappings. Do not create project-specific copies by default.

```text
SES ARCHETYPE = reusable method
PROJECT ADAPTER = adoption + locators/boundaries
PROJECT = truth/state/authority/environments
```

## MoreNumTegra adoption target
Priority after certification:
- P0 Strategy, Technical, Content/Semantic;
- P1 Analytics/Growth after measurement gate;
- P2 Local SEO after eligible local target;
- P2 Authority/Digital PR when off-page demand is demonstrated;
- P2 Paid Search/SEM after tracking/conversion and spend authority gates.

MoreNumTegra remains a reference implementation candidate, not universal authority.

## Lifecycle
```text
DISCOVERY -> CANDIDATE -> BUILDER PACKAGE/KERNEL -> L1 -> BUILDER APPLIED -> FINGERPRINT -> L2 -> READINESS -> USER READY -> ARCHETYPE ACTIVE -> CERTIFIED_FOR_ANY_PROJECT -> EXPLICIT PROJECT ADOPTION
```

These states are not interchangeable. `GENERATE != AUTHORIZE != PUBLISH`.