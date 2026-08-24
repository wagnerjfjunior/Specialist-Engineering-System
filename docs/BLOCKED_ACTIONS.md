# SES — Blocked Actions

**Status:** `MANUAL_SPECIALIST_HANDOFF / CURRENT_OPERATIONAL_BOUNDARY`  
**Canonical source:** `wagnerjfjunior/Specialist-Engineering-System`

Absence from this document does not create authorization. Capability, certification, prior approval, conversation history or a derived summary do not substitute for current applicable authority.

## 1. General blocks

Without separate explicit applicable authorization, block:

- direct/unreviewed canonical SES mutation;
- merge/publication not authorized for the exact scope;
- consumer-project mutation from SES central evolution;
- automatic specialist adoption/propagation into consumer projects;
- legacy retirement/deletion without mapping, evidence and explicit decision;
- rewriting historical proof/adjudication;
- storing secrets in SES artifacts or handoff packets;
- treating tool capability as authority.

```text
GENERATE != AUTHORIZE != PUBLISH
TOOL_CAPABILITY != AUTHORIZATION
CONTEXT_READY != AUTHORIZED_TO_MUTATE
```

## 2. Certification gate blocks

Terminal specialist state:

```text
CERTIFIED_FOR_ANY_PROJECT = YES
```

Block certification based solely on READY, ACTIVE, historical PASS for another fingerprint, spec conformance without actual Builder/runtime proof, missing tool evidence, absence of observed failure, one consumer-project success, or unresolved hard blockers.

```text
READY != CERTIFIED_FOR_ANY_PROJECT
ARCHETYPE_ACTIVE != CERTIFIED_FOR_ANY_PROJECT
HISTORICAL_PASS != CURRENT_CERTIFICATION
ABSENCE_OF_FINDING != PROOF_OF_ABSENCE
```

## 3. Certified reusable specialists

```text
ux-ui-app-specialist = YES
backend-data-platform-specialist = YES
application-security-assurance-specialist = YES
software-systems-architect = YES
documentation-auditor = YES / v1.1 / KERNEL_BLOB 5bc10297d9e655cf169d2680f914e446232992e0
```

For certified specialists, block without separate authority: publication/broader visibility, automatic project adoption, transfer of proof to a changed fingerprint, mutation authority, production approval, risk acceptance, or claims that every consumer project is correct/secure/production-ready.

## 4. Historical integrity

Preserve historical AppSec events including `A03_INITIAL=INVALID`, `A07_INITIAL=FAIL`, `R06_INITIAL=BLOCKED`, later retests, `INITIAL_OVERCLAIM`, `USER_CORRECTED`, `RETROACTIVE_PASS=NO` and `RETROACTIVE_ERASURE=NO`.

Preserve historical Software Systems Architect failures/retests as recorded in its final certification evidence. Current certification does not rewrite them.

Preserve legacy SaaS Architect evidence under its original identity/fingerprint; do not transfer that historical runtime PASS to a changed current fingerprint or use legacy aliases to rewrite history.

Preserve historical Runtime Enforcement Gateway and Specialist Router PASS evidence under its exact proof boundary. The current operational correction does not erase those results and does not allow them to prove current end-to-end workflow usability.

```text
HISTORICAL_GATEWAY_PASS != CURRENT_OPERATIONAL_ACCEPTANCE
ENDPOINT_TEST_PASS != END_TO_END_WORKFLOW_USABLE
RETROACTIVE_ERASURE = NO
```

## 5. Documentation Auditor

Historical v0.9 and v1.0 evidence remains immutable, including:

```text
V0.9 R03A = FAIL
V0.9 R05 = FAIL
V0.9 R06 = FAIL
V1.0 G01 ATTEMPT 1 = FAIL
V1.0 G01 ATTEMPT 2 = FAIL
RETROACTIVE_PASS = NO
RETROACTIVE_ERASURE = NO
```

Current certified v1.1 fingerprint:

```text
KERNEL = runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_KERNEL_V1_1.md
KERNEL_BLOB = 5bc10297d9e655cf169d2680f914e446232992e0
BUILDER_PACKAGE = VERSIONED
BUILDER_APPLIED = PASS
RUNTIME_FINGERPRINT_CAPTURED = PASS_WITH_PROVENANCE_LIMITATION
C01-C18 = PASS
CERTIFIED_FOR_ANY_PROJECT = YES
```

Block converting historical FAIL to retroactive PASS, transferring v1.1 certification to a changed fingerprint without proportional revalidation, automatic consumer-project adoption, or treating certification as project readiness/mutation authority/production approval/risk acceptance.

## 6. Current manual specialist handoff boundary

The current accepted specialist-consultation transport is human-mediated copy/paste governed by:

`core/protocols/MANUAL_SPECIALIST_HANDOFF_CONTRACT.md`

Block:

- claiming the Router/Gateway is the current operational consultation path;
- claiming `routeSpecialistRole`, an Action or a specialist executed when no such invocation occurred;
- requiring a live Gateway receipt as a prerequisite for the current manual consultation path;
- silently converting an ad-hoc consultation into project adoption;
- treating a specialist recommendation/result as SES approval or project authorization;
- treating a copied SHA/state as necessarily current when freshness is material;
- embedding or requesting secrets in a handoff packet;
- silently substituting a different project, role or specialist through fuzzy matching;
- letting copy/paste transport expand project mutation authority;
- automatically accepting pasted specialist output as canonical truth without proportional evidence review.

```text
CONSULTED != ADOPTED
ADOPTED != EXECUTED
EXECUTED != AUTHORIZED_TO_MUTATE
SPECIALIST_OUTPUT != SES_APPROVAL
COPIED_CONTEXT != LIVE_EVIDENCE
```

## 7. Runtime Enforcement Gateway boundary

Historical origin:

```text
DOCUMENTATION_AUDITOR_GATEWAY = SPECIALIST_SPECIFIC / CANDIDATE_LEARNING
```

Gateway contract scope:

```text
RUNTIME_ENFORCEMENT_GATEWAY_CONTRACT = UNIVERSAL ROUTING/ENFORCEMENT SEMANTICS / CANDIDATE_V0_1
```

This promotion remains limited to deterministic SES routing/enforcement semantics captured in the versioned contract. It does not universalize consumer-project role maps, local rules, authority, state or adoption.

Gateway/Router are currently historical/runtime-candidate assets rather than the accepted operational specialist-consultation path.

Block:

- presenting historical Gateway/Router test evidence as current operational acceptance;
- automatically re-adopting or redeploying the Gateway because manual handoff is now current;
- treating Gateway proof as Documentation Auditor C09 or any specialist certification proof;
- claiming Action/tool integration before an actual invocation is observed;
- hardcoding volatile certification/archetype/project truth into the HTTP wrapper;
- reusing stale canonical snapshots as current after a material load failure;
- semantic/fuzzy role guessing in Gateway v0.1;
- automatic consumer-project mutation/adoption from Gateway work;
- storing GitHub tokens or deployment secrets in SES artifacts.

```text
SPECIALIST_CERTIFICATION != GATEWAY_DEPLOYMENT
GATEWAY_PROOF != SPECIALIST_CERTIFICATION_PROOF
IMPLEMENTED != DEPLOYED
DEPLOYED != INVOKED
INVOKED != END_TO_END_WORKFLOW_USABLE
REFERENCE_IMPLEMENTATION != UNIVERSAL PROJECT TRUTH
```

A future Router/Gateway re-adoption requires explicit SES approval and new end-to-end proof in the intended user workflow.

## 8. Portfolio stop-loss

The Documentation Auditor normalization is closed. Continue to block uncontrolled specialist waves without requirements/interview/challenge/evidence discipline, collapsing Backend/Data implementation authority with independent AppSec assurance, and universalizing consumer-specific modules or routing without cross-domain evidence.

## 9. Adoption/retirement boundary

```text
CERTIFIED SES SPECIALIST
-> EXPLICIT PROJECT RESOLUTION
-> PROJECT BOOTSTRAP / CONTINUITY / AUTHORITY
-> DELTA / OVERRIDE REVIEW WHEN NEEDED
-> EXPLICIT PROJECT ADOPTION IF APPLICABLE
-> PROJECT-LOCAL EVIDENCE WHEN REQUIRED
-> EQUIVALENCE / RESIDUAL-GAP REVIEW
-> RETIREMENT DECISION
```

Ad-hoc consultation is permitted when explicitly requested but does not traverse the `EXPLICIT PROJECT ADOPTION` state:

```text
EXPLICIT_AD_HOC_CONSULTATION != PROJECT_ADOPTION
```

```text
CENTRAL EVOLUTION != AUTOMATIC PROJECT MUTATION
TARGET CONSOLIDATION != AUTHORIZED RETIREMENT
```

## 10. Conflict and anti-loop

If `docs/NEXT_SAFE_ACTION.md` conflicts materially with bootstrap, certification contract/ledger, live authority, archetype registry or newer evidence: stop and reconcile.

```text
MATERIAL_CHANGE -> PROPORTIONAL_REVALIDATION
NO_MATERIAL_CHANGE -> NO_REAUDIT_LOOP
NEW_TRANSPORT_AVAILABLE != NEW_TRANSPORT_ADOPTED
```