# SES — Blocked Actions

**Status:** `SPECIALIST_CERTIFICATION_NORMALIZATION / GATE_V0_1`  
**Canonical source:** `wagnerjfjunior/Specialist-Engineering-System`

Absence from this document does not create authorization. Capability, certification, registry state, prior approval for another action, conversation history or a derived summary do not substitute for current applicable authority.

## 1. General blocks

Without separate explicit applicable authorization, block:

- direct/unreviewed mutation of canonical SES state;
- merge/publication decisions not explicitly authorized for the exact scope;
- consumer-project mutation from SES central evolution;
- automatic propagation/adoption of SES specialists into registered projects;
- legacy specialist retirement/deletion without mapping, delta review, evidence and explicit adoption/retirement decisions;
- rewriting historical proof/adjudication;
- storing secrets in SES artifacts;
- treating tool capability as mutation authority.

```text
GENERATE != AUTHORIZE != PUBLISH
TOOL CAPABILITY != AUTHORIZATION
CONTEXT_READY != AUTHORIZED_TO_MUTATE
```

## 2. Certification gate blocks

The terminal specialist lifecycle target is:

```text
CERTIFIED_FOR_ANY_PROJECT = YES
```

Block any certification claim based solely on:

- `SPECIALIST_READINESS = READY`;
- `RESOLUTION_STATUS = ACTIVE`;
- historical runtime PASS for a materially changed current fingerprint;
- spec conformance without actual Builder/runtime proof;
- missing tool/integration evidence;
- absence of observed failure;
- consumer-project-specific success used as universal proof;
- unresolved hard blockers.

Preserve:

```text
READY != CERTIFIED_FOR_ANY_PROJECT
ARCHETYPE_ACTIVE != CERTIFIED_FOR_ANY_PROJECT
HISTORICAL_PASS != CURRENT_CERTIFICATION
ABSENCE_OF_FINDING != PROOF_OF_ABSENCE
```

## 3. Certified reusable specialists

Current certification ledger under the gate:

```text
ux-ui-app-specialist = CERTIFIED_FOR_ANY_PROJECT YES
backend-data-platform-specialist = CERTIFIED_FOR_ANY_PROJECT YES
application-security-assurance-specialist = CERTIFIED_FOR_ANY_PROJECT YES
```

Evidence-bound adjudication:

`tests/behavioral/evidence/SPECIALIST_CERTIFICATION_PORTFOLIO_ADJUDICATION_2026-08-17.md`

For any certified specialist, block without separate applicable authority:

- publishing or broadening private Builder visibility;
- automatic consumer-project adoption;
- treating certification as project-context readiness;
- treating certification as mutation authority;
- treating certification as production approval or risk acceptance;
- transferring fingerprint-bound L2/certification proof to a materially changed runtime;
- claiming that every consumer project is secure, correct or production-ready.

```text
CERTIFIED_FOR_ANY_PROJECT != PROJECT_CONTEXT_READY
CERTIFIED_FOR_ANY_PROJECT != CONSUMER_PROJECT_ADOPTED
CERTIFIED_FOR_ANY_PROJECT != AUTHORIZED_TO_MUTATE
CERTIFIED_FOR_ANY_PROJECT != PRODUCTION_APPROVED
```

## 4. Application Security Assurance historical integrity

Current state:

```text
L1-C = PASS
L2_RUNTIME_FINGERPRINT_VALIDATION = PASS / COMPACT_FINGERPRINT_BOUND
SPECIALIST_READINESS = READY / USER_AUTHORIZED
ARCHETYPE_RESOLUTION_STATUS = ACTIVE
CERTIFIED_FOR_ANY_PROJECT = YES
```

Preserve historical events:

```text
A03_INITIAL = INVALID
A07_INITIAL = FAIL
A07_P14_INITIAL = FAIL
R06_INITIAL = BLOCKED
R06_RETEST = PASS
INITIAL_OVERCLAIM = YES
USER_CORRECTED = YES
SELF_AUDIT_CORRECTION = EXECUTED
RETROACTIVE_PASS = NO
RETROACTIVE_ERASURE = NO
```

Block any attempt to rewrite those earlier events as if they had initially passed.

## 5. SaaS Architect current blocks

Preserve:

```text
ARCHETYPE_RESOLUTION_STATUS = ACTIVE
HISTORICAL_V0_1_RUNTIME_BEHAVIORAL_PROOF = PASS
HISTORICAL_T01_T29 = 29/29 PASS
CURRENT_BUILDER_FIT_REVISION_RUNTIME_PROOF = NOT_YET_ESTABLISHED
EXTERNAL_BUILDER_RECONCILIATION_REQUIRED
CERTIFIED_FOR_ANY_PROJECT = NO
```

Until the current Builder-fit revision is reconciled and proportionally validated, block:

- `CERTIFIED_FOR_ANY_PROJECT = YES`;
- transfer of historical v0.1 runtime PASS to the current fingerprint;
- SaaS Architect rename solely from naming preference;
- revival of superseded selection-first v0.2/v0.3 experiments without a new decision;
- consumer-project migration/adoption claims based on current certification;
- publication/broader visibility claims.

## 6. Documentation Auditor current blocks

Preserve corrected state:

```text
R01 = PASS
R02 = PASS
R03A = FAIL
R03B = PASS
R04 = PASS
R05 = FAIL
R06 = FAIL
PROJECT_TARGET_REGRESSION = 4/7
PROJECT_TARGET_REGRESSION_PASS = NOT_ESTABLISHED
RUNTIME_ENFORCEMENT_GAP = ESTABLISHED
PROMPT_LEVEL_FIX_STOP_LOSS = TRIGGERED
CERTIFIED_FOR_ANY_PROJECT = NO
```

Initial R03A/R05 PASS adjudications remain historical `INITIAL_OVERCLAIM` records.

Block:

- certification until affected runtime obligations are actually closed;
- converting project-target regression failures to PASS from design intent alone;
- treating `RESOLUTION_STATUS: ACTIVE` as runtime certification;
- implementing the deferred Documentation Auditor Gateway as if design artifacts proved enforcement;
- broad prompt-level retry loops after the recorded stop-loss without a material new mechanism/evidence event.

## 7. Portfolio stop-loss

Continue to block:

- creating new specialists before SaaS Architect and Documentation Auditor are normalized, absent explicit reprioritization;
- creating all queued specialists simultaneously;
- reducing specialist count in a way that collapses implementation and independent assurance authority;
- universalizing FECH.AI-specific modules, Supabase specifics, MesaCliente, LeadOps or GPT routing without cross-project evidence;
- merging Backend/Data implementation authority with independent AppSec assurance;
- canonicalizing new portfolio categories merely for symmetry;
- treating Runtime Enforcement Gateway design as implemented runtime;
- implementing complex gateway/middleware before contract + behavioral proof justify it.

## 8. Adoption/retirement boundary

```text
CERTIFIED SES SPECIALIST
-> EXPLICIT PROJECT RESOLUTION
-> PROJECT BOOTSTRAP / CONTINUITY / AUTHORITY
-> DELTA / OVERRIDE REVIEW WHEN NEEDED
-> EXPLICIT PROJECT ADOPTION IF APPLICABLE
-> PROJECT-LOCAL BEHAVIORAL EVIDENCE WHEN REQUIRED
-> EQUIVALENCE / RESIDUAL-GAP REVIEW
-> RETIREMENT DECISION
```

```text
TARGET CONSOLIDATION != AUTHORIZED RETIREMENT
CENTRAL EVOLUTION != AUTOMATIC PROJECT MUTATION
```

## 9. Conflict and anti-loop rules

If `docs/NEXT_SAFE_ACTION.md` conflicts materially with bootstrap, certification contract/ledger, live authority, archetype registry or newer evidence: stop and reconcile.

Do not create re-audit loops absent a material invalidation event. Revalidate only affected evidence/dependencies.

```text
MATERIAL_CHANGE -> PROPORTIONAL_REVALIDATION
NO_MATERIAL_CHANGE -> NO_REAUDIT_LOOP
```