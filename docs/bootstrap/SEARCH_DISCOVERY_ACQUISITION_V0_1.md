# SES — Search, Discovery & Acquisition Bootstrap v0.1

**Status:** DOMAIN_BOOTSTRAP_CANDIDATE / DESIGN_AND_DISCOVERY_ONLY

This entrypoint reconstructs the current candidate work for the Search, Discovery & Acquisition specialist family. It does not replace `docs/bootstrap/INDEX.md` as the SES root bootstrap and does not activate or certify any archetype.

## Reading order

1. resolve SES `main` live or preserve the exact candidate ref when reviewing a branch/PR;
2. read `docs/bootstrap/INDEX.md`;
3. read `docs/architecture/SEARCH_DISCOVERY_ACQUISITION_DOMAIN_V0_1.md`;
4. read the applicable specialist discovery file(s):
   - `docs/specialists/SEO_STRATEGY_GOVERNANCE_SPECIALIST_DISCOVERY_V0_1.md`
   - `docs/specialists/TECHNICAL_SEO_SPECIALIST_DISCOVERY_V0_1.md`
   - `docs/specialists/CONTENT_SEMANTIC_SEO_SPECIALIST_DISCOVERY_V0_1.md`
   - `docs/specialists/SEO_ANALYTICS_GROWTH_SPECIALIST_DISCOVERY_V0_1.md`
5. when MoreNumTegra is the explicit reference/consumer target, resolve its Project Adapter and then read `projects/morenumtegra/SEARCH_DISCOVERY_ACQUISITION_ADOPTION_PLAN_V0_1.md` as a plan only;
6. continue the SES flow `INTERVIEW -> REQUIREMENTS -> ASSUMPTIONS -> CHALLENGE -> ALTERNATIVES -> DESIGN -> CANDIDATE -> TEST -> VALIDATE` before any terminal specialist claim.

## Current candidate portfolio

```text
WAVE A / DISCOVERY
- SEO Strategy & Governance Specialist
- Technical SEO Specialist
- Content & Semantic SEO Specialist
- SEO Analytics & Growth Specialist

WAVE B / DOMAIN-LEVEL CANDIDATES ONLY
- Local SEO Specialist
- Authority & Digital PR Specialist
- Paid Search & SEM Specialist
```

## State boundaries

```text
DOMAIN_DOCUMENTED != ARCHETYPE_CREATED
DISCOVERY_FILE != SPECIALIST_CANDIDATE_APPROVED
ARCHETYPE_CREATED != ACTIVE
ACTIVE != CERTIFIED_FOR_ANY_PROJECT
CERTIFIED_FOR_ANY_PROJECT != CONSUMER_PROJECT_ADOPTED
PLANNED_PROJECT_ROLE != ADOPTED_PROJECT_ROLE
```

## Immediate next design work

For each Wave A specialist, complete the adaptive requirements interview and explicitly adjudicate:

- mission and non-goals;
- authority boundaries;
- source hierarchy and evidence requirements;
- tools/capabilities and tool honesty;
- project-local versus reusable rules;
- negative assertions and missing-evidence handling;
- critical failure modes;
- proof obligations;
- behavioral invariance tests;
- cross-specialist handoffs and overlap resolution.

Only then generate the first Specialist Candidate contract.
