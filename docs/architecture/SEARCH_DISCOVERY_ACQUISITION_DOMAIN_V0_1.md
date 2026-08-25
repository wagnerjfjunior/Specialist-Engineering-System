# SES — Search, Discovery & Acquisition Domain v0.1

**Status:** DOMAIN_CANDIDATE_V0_1 / INITIAL_ARCHITECTURE / NOT_CERTIFICATION  
**Scope:** reusable, project-agnostic specialist family design for search visibility, generative discovery, local discovery, measurement, authority and paid search.  
**Authority:** architecture candidate only. It does not activate archetypes, adopt roles into consumer projects, authorize campaigns, tracking, publication, spend or mutation.

## 1. Problem statement

Search/discovery work spans materially different methods, evidence surfaces and failure modes. A single monolithic `SEO Specialist` would concentrate strategy, technical implementation, semantic/content reasoning, measurement, local presence, authority acquisition and paid-media decisions in one authority boundary.

The SES target is therefore a bounded specialist family rather than one universal SEO generalist.

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
+-- Shared Measurement / Evidence Surfaces
    +-- Google Search Console
    +-- GA4
    +-- Google Tag Manager
    +-- Looker Studio
    +-- PageSpeed Insights / CrUX / Lighthouse
    +-- Google Search Central
    +-- SERP live
    +-- site live
    +-- Semrush / Ahrefs when available
    +-- Bing Webmaster Tools / IndexNow when applicable
    +-- Google Business Profile / Maps when applicable
```

## 2. Design principles

1. `TOOL != SPECIALIST_BOUNDARY` — tools are evidence surfaces; ownership follows the claim/domain.
2. `SEO != SEM` — paid search has budget, bidding, campaign and financial-governance boundaries distinct from organic search.
3. `GEO_GENERATIVE != GEO_GEOGRAPHIC` — Generative Engine Optimization is distinct from local/geographic search.
4. GEO generative begins as a cross-cutting capability of Strategy, Technical and Content/Semantic SEO; do not create a standalone GEO archetype until independent method/tool/evidence boundaries justify it.
5. Local SEO is a distinct candidate because Google Business Profile/Maps, local entity consistency, reviews, NAP/citations, local landing pages and eligibility create a materially separate method.
6. Measurement is shared, but `LAB_DATA != FIELD_DATA`, `TRAFFIC != BUSINESS_OUTCOME`, and `TRACKED != VALIDATED`.
7. Consumer projects explicitly adopt only the roles they need. `CERTIFIED_FOR_ANY_PROJECT != CONSUMER_PROJECT_ADOPTED`.

## 3. Candidate specialist topology

### Wave A — primary creation candidates

#### A1. SEO Strategy & Governance Specialist

Owns search opportunity framing, prioritization, market/SERP landscape, coordination across SEO subdomains, KPI/proof-obligation definition and cross-specialist trade-offs.

Must not silently substitute for Technical SEO, Content/Semantic SEO, Analytics/Growth, Local SEO, SEM or project product authority.

#### A2. Technical SEO Specialist

Owns crawlability, indexability, rendering, canonicalization, robots/sitemaps, redirects, structured-data implementation proof, Core Web Vitals/performance SEO, technical discoverability and technical AI-crawler/retrievability analysis.

Primary evidence surfaces include Google Search Central, Search Console technical reports, PageSpeed Insights, CrUX, Lighthouse/DevTools, live site and crawlers such as Screaming Frog/Sitebulb when available.

#### A3. Content & Semantic SEO Specialist

Owns search intent, entity/semantic modeling, topical coverage, information architecture, on-page content, internal linking, content briefs and content-side GEO/AI visibility/citability.

Primary evidence surfaces include live SERP, Search Console query/page evidence, Semrush/Ahrefs keyword/content data when available, live content and structured semantic relationships.

#### A4. SEO Analytics & Growth Specialist

Owns organic measurement design, Search Console performance, GA4 analysis, KPI integrity, conversion measurement, experiment interpretation, attribution limitations and growth diagnosis.

Primary evidence surfaces include Search Console, GA4, GTM implementation evidence, Looker Studio and project-approved conversion definitions.

### Wave B — create after Wave A boundaries stabilize

#### B1. Local SEO Specialist

Owns local/geographic discovery: Google Business Profile, Google Maps, business eligibility, NAP/entity consistency, local landing pages, reviews/reputation signals, local citations and equivalent local-search ecosystems where relevant.

A project must not create one Business Profile per property/location merely because it wants local visibility; platform eligibility and real-world business representation must be validated.

#### B2. Authority & Digital PR Specialist

Owns backlink/referring-domain analysis, authority development, digital PR, link acquisition quality, spam/risk analysis, brand/entity mentions and authority gaps.

#### B3. Paid Search & SEM Specialist

Owns paid search campaign architecture, query/keyword targeting, match types, negative keywords, bidding, budget efficiency, Quality Score/landing-page alignment, paid-search conversion interpretation and campaign experimentation.

It cannot authorize spend or publish campaigns without project-local authority.

## 4. Shared tools mapped by primary responsibility

| Surface | Primary owner | Secondary consumers |
|---|---|---|
| Google Search Central | Technical SEO | Strategy, Content |
| Google Search Console | Analytics & Growth | Technical, Content, Strategy |
| GA4 | Analytics & Growth | Strategy, SEM, Content |
| GTM | Analytics & Growth / project martech boundary | SEM, Technical; privacy/security handoff when material |
| PageSpeed / CrUX | Technical SEO | UX/UI, Strategy |
| Lighthouse / DevTools | Technical SEO | UX/UI |
| Semrush | claim-dependent | Strategy, Content, Technical, Authority |
| Ahrefs | Authority primary for links; claim-dependent otherwise | Strategy, Content, Technical |
| SERP live | Strategy + Content/Semantic | Local, SEM |
| site live | claim-dependent | all applicable specialists |
| Google Business Profile / Maps | Local SEO | Strategy, Analytics |
| Google Trends | Strategy | Content, SEM |
| Bing Webmaster Tools / IndexNow | Technical SEO | Strategy |
| Looker Studio | Analytics & Growth | Strategy, project stakeholders |

## 5. Canonical boundary model

```text
SES CANONICAL ARCHETYPE
= reusable method + evidence discipline + boundaries + proof obligations + failure modes

CONSUMER PROJECT ADAPTER
= explicit ROLE -> ARCHETYPE_ID adoption + project locators + project-local boundaries

PROJECT-LOCAL TRUTH
= repository/runtime/business rules/data/authority/environments/current state
```

Do not create `technical-seo-<project>` copies by default. Project-specific exceptions require demonstrated project-local method/authority that cannot remain an adapter/override.

## 6. MoreNumTegra as reference implementation, not universal authority

MoreNumTegra is a useful first consumer because its current V1 is mobile-first, SEO-first and performance-first, with a real-estate catalog, Green Sales conversion surface and Vercel homologation path.

It may validate use cases such as:

- technical indexing and Core Web Vitals;
- entity modeling for developer / project / neighborhood / typology / status;
- search-intent and landing-page architecture;
- GEO generative retrieval/citability;
- Search Console + GA4 measurement after project gates are opened;
- local search only after eligible real-world business/entity targets are defined;
- SEM only after tracking and campaign authority gates are explicitly opened.

`REFERENCE_IMPLEMENTATION != UNIVERSAL PROJECT TRUTH`.

## 7. Creation sequence

```text
DOMAIN CANDIDATE
-> specialist requirements interviews
-> assumptions / challenge / alternatives
-> candidate contracts
-> L1 behavioral design + validation
-> Builder/kernel package
-> L2 runtime proof
-> certification adjudication
-> registry activation when eligible
-> explicit consumer-project adoption
```

Wave A order recommended for current demand:

1. SEO Strategy & Governance
2. Technical SEO
3. Content & Semantic SEO
4. SEO Analytics & Growth

Wave B follows only after boundary evidence or concrete project demand justifies it.

## 8. Non-goals

This document does not:

- certify any search specialist;
- activate any archetype in `archetypes/REGISTRY.md`;
- adopt any role into MoreNumTegra or another project;
- authorize analytics/tags/pixels, Google Business Profile changes, campaigns, budget, publication or production mutation;
- claim that every listed external tool is connected or available.

## 9. Current unresolved decisions

- exact role names/aliases for each archetype;
- whether Analytics & Growth remains SEO-specific or later generalizes into a cross-acquisition measurement archetype;
- minimum cross-engine GEO proof obligations beyond Google/Bing/AI-search surfaces;
- Local SEO cross-platform minimum baseline beyond Google Business Profile/Maps;
- Authority/Digital PR boundary with broader brand/PR specialists if such archetypes are created later;
- SEM boundary with future paid-social/performance-media specialists.

These remain product/design decisions and must not be silently inferred during candidate construction.
