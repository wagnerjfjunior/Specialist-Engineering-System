# SES — Search, Discovery & Acquisition Bootstrap v0.1

**Status:** `DOMAIN_BOOTSTRAP_CANDIDATE / WAVE_A_BUILDER_READY / L1_L2_PENDING`

This entrypoint reconstructs the current candidate work for the Search, Discovery & Acquisition specialist family. It does not replace `docs/bootstrap/INDEX.md`, activate an archetype, certify a specialist or adopt a role into a consumer project.

## Reading order
1. resolve SES `main` live or preserve the exact candidate ref when reviewing a branch/PR;
2. read `docs/bootstrap/INDEX.md`;
3. read `docs/architecture/SEARCH_DISCOVERY_ACQUISITION_DOMAIN_V0_1.md`;
4. for a Wave A specialist, read its Discovery document, Candidate, candidate Archetype, Builder Package/Kernel and L1/L2 specs;
5. use `runtime/custom-gpt/SEARCH_SPECIALIST_BUILDER_CREATION_HANDOFF_V0_1.md` for Builder creation fields;
6. when MoreNumTegra is explicit, resolve its Project Adapter and read `projects/morenumtegra/SEARCH_DISCOVERY_ACQUISITION_ADOPTION_PLAN_V0_1.md` as a plan only;
7. after actual Builder application, capture fingerprint and execute/adjudicate the specialist-specific L2 runbook before certification or activation.

## Wave A — Builder-ready candidates

### SEO Strategy & Governance
- Discovery: `docs/specialists/SEO_STRATEGY_GOVERNANCE_SPECIALIST_DISCOVERY_V0_1.md`
- Candidate: `docs/specialists/SEO_STRATEGY_GOVERNANCE_SPECIALIST_CANDIDATE_V0_1.md`
- Archetype: `archetypes/seo-strategy-governance-specialist/ARCHETYPE.md`
- Package/kernel: `runtime/custom-gpt/SEO_STRATEGY_GOVERNANCE_SPECIALIST_BUILDER_PACKAGE_V0_1.md` / `SEO_STRATEGY_GOVERNANCE_SPECIALIST_BUILDER_KERNEL_V0_1.md`
- Tests: `tests/behavioral/SEO_STRATEGY_GOVERNANCE_SPECIALIST_L1_SUITE_V0_1.md`, `tests/runtime/SEO_STRATEGY_GOVERNANCE_SPECIALIST_L2_RUNBOOK_V0_1.md`

### Technical SEO
- Discovery: `docs/specialists/TECHNICAL_SEO_SPECIALIST_DISCOVERY_V0_1.md`
- Candidate: `docs/specialists/TECHNICAL_SEO_SPECIALIST_CANDIDATE_V0_1.md`
- Archetype: `archetypes/technical-seo-specialist/ARCHETYPE.md`
- Package/kernel: `runtime/custom-gpt/TECHNICAL_SEO_SPECIALIST_BUILDER_PACKAGE_V0_1.md` / `TECHNICAL_SEO_SPECIALIST_BUILDER_KERNEL_V0_1.md`
- Tests: `tests/behavioral/TECHNICAL_SEO_SPECIALIST_L1_SUITE_V0_1.md`, `tests/runtime/TECHNICAL_SEO_SPECIALIST_L2_RUNBOOK_V0_1.md`

### Content & Semantic SEO
- Discovery: `docs/specialists/CONTENT_SEMANTIC_SEO_SPECIALIST_DISCOVERY_V0_1.md`
- Candidate: `docs/specialists/CONTENT_SEMANTIC_SEO_SPECIALIST_CANDIDATE_V0_1.md`
- Archetype: `archetypes/content-semantic-seo-specialist/ARCHETYPE.md`
- Package/kernel: `runtime/custom-gpt/CONTENT_SEMANTIC_SEO_SPECIALIST_BUILDER_PACKAGE_V0_1.md` / `CONTENT_SEMANTIC_SEO_SPECIALIST_BUILDER_KERNEL_V0_1.md`
- Tests: `tests/behavioral/CONTENT_SEMANTIC_SEO_SPECIALIST_L1_SUITE_V0_1.md`, `tests/runtime/CONTENT_SEMANTIC_SEO_SPECIALIST_L2_RUNBOOK_V0_1.md`

### SEO Analytics & Growth
- Discovery: `docs/specialists/SEO_ANALYTICS_GROWTH_SPECIALIST_DISCOVERY_V0_1.md`
- Candidate: `docs/specialists/SEO_ANALYTICS_GROWTH_SPECIALIST_CANDIDATE_V0_1.md`
- Archetype: `archetypes/seo-analytics-growth-specialist/ARCHETYPE.md`
- Package/kernel: `runtime/custom-gpt/SEO_ANALYTICS_GROWTH_SPECIALIST_BUILDER_PACKAGE_V0_1.md` / `SEO_ANALYTICS_GROWTH_SPECIALIST_BUILDER_KERNEL_V0_1.md`
- Tests: `tests/behavioral/SEO_ANALYTICS_GROWTH_SPECIALIST_L1_SUITE_V0_1.md`, `tests/runtime/SEO_ANALYTICS_GROWTH_SPECIALIST_L2_RUNBOOK_V0_1.md`

## Wave B — domain candidates only
- Local SEO Specialist
- Authority & Digital PR Specialist
- Paid Search & SEM Specialist

Wave B is intentionally not promoted to Builder-ready in this change. Create only after requirements/challenge work is complete.

## State boundaries
```text
BUILDER_READY_CANDIDATE != BUILDER_APPLIED
BUILDER_APPLIED != L2_PASS
L2_PASS != CERTIFIED_FOR_ANY_PROJECT
ARCHETYPE_CONTRACT_EXISTS != ARCHETYPE_ACTIVE
CERTIFIED_FOR_ANY_PROJECT != CONSUMER_PROJECT_ADOPTED
PLANNED_PROJECT_ROLE != ADOPTED_PROJECT_ROLE
```

## Immediate next action
User creates the four private Wave A Builders using the exact handoff fields/kernels. SES then captures each runtime fingerprint, executes/adjudicates L1/L2 as applicable, performs readiness/certification adjudication, and only after explicit lifecycle authorization activates archetypes and updates project adoption.