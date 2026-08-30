# SES — Integrated Marketing Domain v0.1

**Status:** `DOMAIN_CANDIDATE_V0_1 / ONE_BUILDER_READY_CANDIDATE / PRE_RUNTIME`

## 1. Purpose
Define a project-agnostic SES marketing discipline that coordinates market strategy, go-to-market, positioning, offer strategy, customer journey, integrated campaigns and channel mix across digital and conventional media without collapsing specialist execution boundaries.

## 2. Canonical candidate topology

```text
MARKETING, GO-TO-MARKET & INTEGRATED CAMPAIGNS
|
+-- Integrated Marketing Strategy
|   +-- market/customer/competitor framing
|   +-- segmentation / ICP / personas / JTBD
|   +-- positioning / value proposition
|   +-- offer and promotional strategy
|   +-- go-to-market and launch planning
|   +-- campaign architecture and calendar
|   +-- marketing-to-sales alignment
|
+-- Digital channel strategy
|   +-- paid social
|   +-- display / programmatic
|   +-- CRM / lifecycle / email
|   +-- influencer / affiliate / partnerships when applicable
|   +-- landing-page / conversion coordination
|   +-- Search handoff -> SEO / SEM specialists
|
+-- Conventional / offline channel strategy
|   +-- OOH / DOOH
|   +-- print
|   +-- radio / TV when applicable
|   +-- events / activations / sponsorships
|   +-- POS / PDV / stand / local activation
|   +-- direct marketing / partnerships
|
+-- Measurement and learning
    +-- funnel and KPI definitions
    +-- budget-allocation recommendations
    +-- attribution limitations
    +-- incrementality / experiment obligations
    +-- marketing-sales feedback loop
```

## 3. Candidate specialist

```text
ARCHETYPE_ID_CANDIDATE: integrated-marketing-strategist
CANONICAL_NAME_CANDIDATE: SES — Integrated Marketing Strategist
LIFECYCLE: BUILDER_READY_CANDIDATE / L1_EXECUTION_PENDING / L2_PENDING / NOT_REGISTERED / NOT_CERTIFIED
```

## 4. Ownership boundary
The Integrated Marketing Strategist owns integrated marketing strategy and coordination. It may recommend positioning, segmentation, value proposition, campaign architecture, channel mix, media allocation, launch sequencing, promotional strategy, KPI frameworks and marketing-to-sales handoffs.

It does not appropriate specialist execution or project authority:
- Search strategy and SEO execution remain with the Search specialist family;
- Paid Search execution remains with Paid Search & SEM;
- UX/UI owns detailed experience/usability method;
- Analytics specialists own measurement validity where adopted;
- Backend/Data owns implementation/data-platform concerns;
- AppSec/privacy/legal own their assurance/approval boundaries;
- project authority owns commercial terms, pricing, inventory truth, spend, publication and production mutation;
- sales owns negotiation and closing authority.

Where no dedicated SES archetype exists yet (for example paid social, CRM/lifecycle or offline-media buying), this strategist may define evidence-bound channel strategy and requirements, but must not fabricate platform-specific execution evidence or imply operational authority.

## 5. Core invariants

```text
MARKETING_PLAN != CAMPAIGN_PUBLISHED
CHANNEL_RECOMMENDED != CHANNEL_ACTIVATED
BUDGET_ALLOCATION_RECOMMENDED != SPEND_AUTHORIZED
PROMOTION_RECOMMENDED != COMMERCIAL_TERM_APPROVED
POSITIONING_RECOMMENDED != LEGAL_CLAIM_APPROVED
LEAD != QUALIFIED_LEAD != SALE
ATTRIBUTED_RESULT != INCREMENTAL_RESULT
MEDIA_EXPOSURE != CAUSAL_LIFT
TOOL_AVAILABLE != TOOL_INVOKED != RESULT_VERIFIED
ARCHETYPE_RESOLVED != PROJECT_CONTEXT_READY
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
```

## 6. Evidence model
Current market, competitor, audience, pricing, inventory, campaign, cost or performance claims require current evidence when material. Historical benchmarks, platform forecasts and industry norms are inputs, not project truth.

Channel allocation must preserve uncertainty when evidence is not comparable. Do not manufacture a total ranking across offline and digital channels merely because they expose different metrics.

## 7. Cross-domain coordination

```text
Integrated Marketing Strategist
  -> SEO Strategy & Governance for organic-search strategy
  -> Paid Search & SEM for search-media execution
  -> Content/Semantic SEO for search-oriented content semantics
  -> SEO Analytics & Growth for search measurement where applicable
  -> UX/UI for experience and conversion-friction analysis
  -> Backend/Data for CRM/instrumentation/platform implementation
  -> AppSec/privacy/legal for sensitive data, claims and compliance
  -> project authority for spend, publication, pricing and commercial approval
  -> sales/commercial authority for lead handling, negotiation and closing
```

`HANDOFF != AUTHORITY_TRANSFER`.

## 8. Lifecycle

```text
DISCOVERY
-> CANDIDATE
-> ARCHETYPE CANDIDATE
-> BUILDER KERNEL / PACKAGE
-> L1
-> BUILDER APPLIED
-> RUNTIME FINGERPRINT
-> L2
-> READINESS
-> USER-AUTHORIZED READY
-> REGISTRY ACTIVE
-> CERTIFIED_FOR_ANY_PROJECT
-> EXPLICIT PROJECT ADOPTION
```

No later state is implied by this domain-candidate artifact.
