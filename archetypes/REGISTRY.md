# SES — Specialist Archetype Registry

**Status:** RUNTIME_CANDIDATE_V0_1 / ARCHETYPE_RESOLUTION_AUTHORITY

## 1. Purpose

This registry is the SES authority for resolving a reusable specialist archetype identifier into one versioned archetype contract.

It owns reusable specialist-engineering metadata only. It does not own consumer-project truth, project-local authority, runtime state, project-local specialist identities or current project decisions.

## 2. Resolution rules

Archetype resolution must be deterministic:

1. trim surrounding whitespace;
2. match exact `ARCHETYPE_ID` first;
3. otherwise match `CANONICAL_NAME` or an explicit alias case-insensitively;
4. do not use fuzzy matching or semantic guessing for material specialist resolution;
5. require exactly one match whose `RESOLUTION_STATUS` is `ACTIVE`.

Fail closed when no unique active archetype resolves.

`RESOLUTION_STATUS` is the only field that determines registry eligibility. Lifecycle/version labels such as `RUNTIME_CANDIDATE_V0_1`, `SPEC_CANDIDATE_V0_1` or `READY_V0_1` describe maturity and must not be interpreted as active/inactive resolution state.

## 3. Registered archetypes

### Software Systems Architect

```text
ARCHETYPE_ID: software-systems-architect
CANONICAL_NAME: SES — Software Systems Architect
ALIASES:
- Software Systems Architect
- SES Software Systems Architect
- SaaS Architect
- SES SaaS Architect
- saas-architect
CONTRACT_PATH: archetypes/software-systems-architect/ARCHETYPE.md
RESOLUTION_STATUS: ACTIVE
LIFECYCLE_STATUS: RUNTIME_CANDIDATE_V0_1 / CERTIFICATION_NORMALIZATION_IN_PROGRESS
```

The Software Systems Architect archetype provides reusable software-systems architecture method spanning AS-IS reconstruction, system decomposition, bounded contexts, dependency direction, trust/authorization and tenant boundaries, persistence, events, concurrency, integrations, reliability, observability, migration, rollback, target architecture and proof obligations.

It does not replace project-local specialist rules and does not appropriate Backend/Data implementation, AppSec assurance, UX/UI, Platform/Deployment, Product Authority or risk-acceptance authority.

`SaaS Architect`, `SES SaaS Architect` and `saas-architect` are legacy continuity aliases only. Historical evidence produced under the legacy identity remains historical for its original subject/fingerprint and is not rewritten retroactively.

For project-specific work, the runtime must resolve the consumer project's own specialist/override sources after project bootstrap. A project-local architectural specialist may refine or restrict this archetype; its identity must be resolved from that project's canonical sources and must not be frozen in this registry.

### Documentation Auditor

```text
ARCHETYPE_ID: documentation-auditor
CANONICAL_NAME: SES — Documentation Auditor
ALIASES:
- Documentation Auditor
- SES Documentation Auditor
CONTRACT_PATH: archetypes/documentation-auditor/ARCHETYPE.md
RESOLUTION_STATUS: ACTIVE
LIFECYCLE_STATUS: READY_V0_2 / L1_PASS / L2_RUNTIME_PASS_FINGERPRINT_BOUND
```

The Documentation Auditor archetype provides reusable evidence-engineering method for claim decomposition, claim-to-evidence traceability, provenance, proof obligations, contradiction handling, freshness/invalidation, bounded negative evidence, final-state verification and reproducible documentation/evidence verdicts.

It does not own project truth, project-local source precedence, lifecycle authority, runtime state or specialist routing. Those remain consumer-project responsibilities and must be resolved after project bootstrap.

`RESOLUTION_STATUS: ACTIVE` means the versioned archetype contract can be resolved by SES. The validated Builder/runtime certification remains bound to the recorded Documentation Auditor v1.1 fingerprint and does not automatically adopt the specialist into consumer projects, create project context, or authorize mutation.

### UX/UI APP Specialist

```text
ARCHETYPE_ID: ux-ui-app-specialist
CANONICAL_NAME: SES — UX/UI APP Specialist
ALIASES:
- UX/UI APP Specialist
- UX/UI Specialist
- SES UX/UI APP Specialist
CONTRACT_PATH: archetypes/ux-ui-app-specialist/ARCHETYPE.md
RESOLUTION_STATUS: ACTIVE
LIFECYCLE_STATUS: READY_V0_1 / L1_PASS / L2_RUNTIME_PASS_FINGERPRINT_BOUND
```

The UX/UI APP Specialist archetype provides reusable UX/UI and product-experience method: evidence discipline, discovery/opportunity framing, journey/state modeling, accessibility/mobile proof boundaries, security/privacy/architecture handoffs, tool honesty and prompt invariance.

Its method is project-agnostic. Project identity, business rules, brand rules, live implementation state, repositories, deployments, databases and project authority remain project-local and must be resolved through the applicable SES project bootstrap path before project-specific substantive work.

The validated Builder/runtime PASS remains bound to the recorded fingerprint. `RESOLUTION_STATUS: ACTIVE` does not transfer that proof to materially changed runtime configurations and does not automatically adopt the specialist into consumer projects.

### Backend & Data Platform Specialist

```text
ARCHETYPE_ID: backend-data-platform-specialist
CANONICAL_NAME: SES — Backend & Data Platform Specialist
ALIASES:
- Backend & Data Platform Specialist
- Backend Data Platform Specialist
- SES Backend & Data Platform Specialist
CONTRACT_PATH: archetypes/backend-data-platform-specialist/ARCHETYPE.md
RESOLUTION_STATUS: ACTIVE
LIFECYCLE_STATUS: READY_V0_1 / L1_PASS / L2_RUNTIME_PASS_FINGERPRINT_BOUND
```

The Backend & Data Platform Specialist archetype provides reusable backend/data engineering method: hostile-client trust posture, server/data-side authorization and tenant isolation, protected-field handling, transaction/invariant design, database authorization, secrets discipline, evidence-bound tool use, project-local truth and implementation-to-AppSec handoff.

Its method is project-agnostic. Project identity, repositories, databases, deployments, business rules, runtime state and project authority remain project-local and must be resolved through the applicable SES project bootstrap path before project-specific substantive work.

The validated Builder/runtime PASS remains bound to the recorded fingerprint. `RESOLUTION_STATUS: ACTIVE` does not transfer that proof to materially changed runtime configurations and does not automatically adopt the specialist into consumer projects.

### Application Security Assurance Specialist

```text
ARCHETYPE_ID: application-security-assurance-specialist
CANONICAL_NAME: SES — Application Security Assurance Specialist
ALIASES:
- Application Security Assurance Specialist
- AppSec Assurance Specialist
- SES Application Security Assurance Specialist
CONTRACT_PATH: archetypes/application-security-assurance-specialist/ARCHETYPE.md
RESOLUTION_STATUS: ACTIVE
LIFECYCLE_STATUS: READY_V0_2 / L1_PASS / L2_RUNTIME_PASS_COMPACT_FINGERPRINT_BOUND
```

The Application Security Assurance Specialist archetype provides reusable independent AppSec assurance method: threat/trust-boundary analysis, hostile-client posture, authorization and cross-tenant testing discipline, Supabase semantic security analysis, CVE applicability/freshness, findings/proof obligations, independent remediation retest, tool honesty, project isolation and prompt invariance.

Its method is project-agnostic. Project identity, repositories, deployments, data, business rules, target authorization, risk acceptance and release authority remain project-local and must be resolved before project-specific substantive work or active testing.

The validated runtime PASS is bound to the recorded compact v0.2 fingerprint. `RESOLUTION_STATUS: ACTIVE` does not transfer that proof to materially changed runtime configurations, does not authorize active testing or mutation, and does not automatically adopt the specialist into consumer projects.

### SEO Strategy & Governance Specialist

```text
ARCHETYPE_ID: seo-strategy-governance-specialist
CANONICAL_NAME: SES — SEO Strategy & Governance Specialist
ALIASES:
- SEO Strategy & Governance Specialist
- SEO Strategy Governance Specialist
- SES SEO Strategy & Governance Specialist
CONTRACT_PATH: archetypes/seo-strategy-governance-specialist/ARCHETYPE.md
RESOLUTION_STATUS: ACTIVE
LIFECYCLE_STATUS: READY_V0_1 / L1_PASS / L2_RUNTIME_PASS_FINGERPRINT_BOUND / CERTIFIED_FOR_ANY_PROJECT
```

The SEO Strategy & Governance Specialist archetype provides reusable search/discovery strategy governance: live-evidence discipline, SEO/GEO opportunity diagnosis, contradiction handling, evidence-based prioritization, decision comparability, cross-specialist coordination, proof obligations/KPIs, project isolation and paid/organic authority separation.

It does not appropriate Technical SEO, Content/Semantic, Analytics, Local SEO, Authority/Digital PR or Paid Search execution, project authority, budget/spend authority, publication or risk acceptance.

The validated runtime PASS is bound to Builder kernel v0.3 and its recorded fingerprint. `RESOLUTION_STATUS: ACTIVE` does not automatically adopt the specialist into consumer projects or authorize mutation.

## 4. Boundary

```text
SES CORE = REUSABLE INFRASTRUCTURE / COMMON CONTRACTS
ARCHETYPE = REUSABLE SPECIALIST METHOD
PROJECT SPECIALIST = PROJECT-LOCAL OVERRIDE / AUTHORITY BOUNDARY
```

`ARCHETYPE_RESOLVED != PROJECT_CONTEXT_READY`

`ARCHETYPE_RESOLVED != RUNTIME_BEHAVIORAL_PROOF`

`ARCHETYPE_RESOLVED != AUTHORIZED_TO_MUTATE`

## 5. Change discipline

Adding, removing, renaming, aliasing or changing `RESOLUTION_STATUS` of an archetype changes specialist-resolution behavior and requires a versioned SES change with behavioral evidence proportional to the impact.

Runtime profile, Builder kernel, Action surface, external Builder configuration, project-local equivalence and legacy retirement remain separate lifecycle scopes and require their own evidence and authorization.