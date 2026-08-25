# SES — Search, Discovery & Acquisition Bootstrap v0.1

**Status:** `DOMAIN_BOOTSTRAP_CANDIDATE / SEVEN_BUILDER_READY_CANDIDATES / L1_L2_PENDING`

This entrypoint reconstructs the current pre-runtime candidate work for the Search, Discovery & Acquisition specialist family. It does not replace `docs/bootstrap/INDEX.md`, activate an archetype, certify a specialist or adopt a role into a consumer project.

## Reading order
1. resolve SES `main` live or preserve the exact candidate ref under review;
2. read `docs/bootstrap/INDEX.md`;
3. read `docs/architecture/SEARCH_DISCOVERY_ACQUISITION_DOMAIN_V0_2.md` (v0.1 remains historical initial architecture);
4. for the selected specialist read its Discovery, Candidate, candidate Archetype, Builder Package/Kernel and L1/L2 specs;
5. use `runtime/custom-gpt/SEARCH_SPECIALIST_BUILDER_CREATION_HANDOFF_V0_2.md` for current Builder creation fields;
6. when MoreNumTegra is explicit, resolve its Project Adapter and read `projects/morenumtegra/SEARCH_DISCOVERY_ACQUISITION_ADOPTION_PLAN_V0_1.md` as a plan only;
7. after actual Builder application, capture fingerprint and execute/adjudicate required L1/L2 evidence before certification or activation.

## Builder-ready candidates

| Specialist | Archetype candidate | Kernel | L1/L2 |
|---|---|---|---|
| SEO Strategy & Governance | `seo-strategy-governance-specialist` | `runtime/custom-gpt/SEO_STRATEGY_GOVERNANCE_SPECIALIST_BUILDER_KERNEL_V0_1.md` | versioned / pending execution |
| Technical SEO | `technical-seo-specialist` | `runtime/custom-gpt/TECHNICAL_SEO_SPECIALIST_BUILDER_KERNEL_V0_1.md` | versioned / pending execution |
| Content & Semantic SEO | `content-semantic-seo-specialist` | `runtime/custom-gpt/CONTENT_SEMANTIC_SEO_SPECIALIST_BUILDER_KERNEL_V0_1.md` | versioned / pending execution |
| SEO Analytics & Growth | `seo-analytics-growth-specialist` | `runtime/custom-gpt/SEO_ANALYTICS_GROWTH_SPECIALIST_BUILDER_KERNEL_V0_1.md` | versioned / pending execution |
| Local SEO | `local-seo-specialist` | `runtime/custom-gpt/LOCAL_SEO_SPECIALIST_BUILDER_KERNEL_V0_1.md` | versioned / pending execution |
| Authority & Digital PR | `authority-digital-pr-specialist` | `runtime/custom-gpt/AUTHORITY_DIGITAL_PR_SPECIALIST_BUILDER_KERNEL_V0_1.md` | versioned / pending execution |
| Paid Search & SEM | `paid-search-sem-specialist` | `runtime/custom-gpt/PAID_SEARCH_SEM_SPECIALIST_BUILDER_KERNEL_V0_1.md` | versioned / pending execution |

Each has a corresponding Discovery, Candidate, `archetypes/<id>/ARCHETYPE.md`, Builder Package, L1 suite and L2 runbook.

## MoreNumTegra candidate priority
```text
P0 SEO_STRATEGY
P0 TECHNICAL_SEO
P0 CONTENT_SEMANTIC_SEO
P1 SEO_ANALYTICS_GROWTH — operational gate: analytics/tags
P2 LOCAL_SEO — gate: eligible real-world business/location target
P2 AUTHORITY_DIGITAL_PR — based on demonstrated off-page demand
P2 PAID_SEARCH_SEM — gates: valid tracking/conversion + spend/campaign authority
```

## State boundaries
```text
BUILDER_READY_CANDIDATE != BUILDER_APPLIED
BUILDER_APPLIED != L1_PASS
BUILDER_APPLIED != L2_PASS
L1_L2_PASS != AUTOMATIC_CERTIFICATION
ARCHETYPE_CONTRACT_EXISTS != ARCHETYPE_ACTIVE
CERTIFIED_FOR_ANY_PROJECT != CONSUMER_PROJECT_ADOPTED
PLANNED_PROJECT_ROLE != ADOPTED_PROJECT_ROLE
```

## Immediate next action
Create the seven private Builders from handoff v0.2. Return configuration evidence to SES for fingerprint binding, L1/L2 execution/adjudication, readiness/certification, then explicit archetype activation and project adoption when applicable.