# SES — Blocked Actions

**Status:** `SPECIALIST_CERTIFICATION_NORMALIZATION / GATE_V0_1`  
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
- storing secrets in SES artifacts;
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
```

For certified specialists, block without separate authority: publication/broader visibility, automatic project adoption, transfer of proof to a changed fingerprint, mutation authority, production approval, risk acceptance, or claims that every consumer project is correct/secure/production-ready.

## 4. Historical integrity

Preserve historical AppSec events including `A03_INITIAL=INVALID`, `A07_INITIAL=FAIL`, `R06_INITIAL=BLOCKED`, later retests, `INITIAL_OVERCLAIM`, `USER_CORRECTED`, `RETROACTIVE_PASS=NO` and `RETROACTIVE_ERASURE=NO`.

Preserve historical Software Systems Architect failures/retests as recorded in its final certification evidence. Current certification does not rewrite them.

Preserve legacy SaaS Architect evidence under its original identity/fingerprint; do not transfer that historical runtime PASS to a changed current fingerprint or use legacy aliases to rewrite history.

## 5. Documentation Auditor

Historical v0.9 remains:

```text
R01 = PASS
R02 = PASS
R03A = FAIL
R03B = PASS
R04 = PASS
R05 = FAIL
R06 = FAIL
PROJECT_TARGET_REGRESSION = 4/7
PROMPT_LEVEL_FIX_STOP_LOSS = TRIGGERED FOR V0_9 COSMETIC RETRY LOOP
RETROACTIVE_PASS = NO
CERTIFIED_FOR_ANY_PROJECT = NO
```

Initial R03A/R05 PASS adjudications remain historical `INITIAL_OVERCLAIM` records.

Current v1.0 certification candidate:

```text
KERNEL_BLOB = 90fcabe72ca5202b54f50ba48b695de00096afa6
BUILDER_PACKAGE = VERSIONED
C01/C05/C06/C13-C17 = PASS
C02-C04 = PENDING EXECUTION
C07-C10 = PENDING BUILDER/RUNTIME EVIDENCE
C11-C12/C18 = PENDING
CERTIFIED_FOR_ANY_PROJECT = NO
```

Block:

- converting any v0.9 FAIL to retroactive PASS;
- declaring v1.0 certified from design intent or repository artifacts alone;
- C07/C08 without actual Builder application/fingerprint evidence;
- C09/C10 without actual configured-runtime execution;
- C11 before the required behavioral/runtime obligations close;
- C12 without applicable user READY authorization for the exact final fingerprint;
- certification while C18 has an unresolved blocker.

The v0.9 prompt-level stop-loss forbids repeated wording-only retries on that same failed fingerprint. It does **not** prohibit a separately versioned new certification subject from being tested as a new fingerprint, provided historical failures remain preserved and all certification obligations are freshly satisfied where invalidated.

```text
OLD_FINGERPRINT_FAIL != NEW_FINGERPRINT_RESULT
NEW_FINGERPRINT_RESULT REQUIRES NEW EVIDENCE
```

## 6. Documentation Auditor Gateway boundary

The Documentation Auditor Runtime Enforcement Gateway is separate second-phase runtime/enforcement research. Its design or proof-runtime implementation does not substitute for specialist runtime certification and is not a prerequisite imposed by `SPECIALIST_CERTIFICATION_FOR_ANY_PROJECT_CONTRACT.md`.

Block:

- treating Gateway design as deployed enforcement;
- treating local Gateway proof as Documentation Auditor C09;
- universalizing the specialist-specific Gateway from a single-domain occurrence;
- automatic consumer-project mutation/adoption from Gateway work.

```text
SPECIALIST_CERTIFICATION != GATEWAY_DEPLOYMENT
GATEWAY_PROOF != C09
CANDIDATE_LEARNING != UNIVERSAL_PRINCIPLE
```

## 7. Portfolio stop-loss

Unless explicitly reprioritized, block creating large new specialist waves before the current Documentation Auditor normalization is closed. Continue to block collapsing Backend/Data implementation authority with independent AppSec assurance and universalizing FECH.AI-specific modules, Supabase specifics, MesaCliente, LeadOps or project routing without cross-domain evidence.

## 8. Adoption/retirement boundary

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

```text
CENTRAL EVOLUTION != AUTOMATIC PROJECT MUTATION
TARGET CONSOLIDATION != AUTHORIZED RETIREMENT
```

## 9. Conflict and anti-loop

If `docs/NEXT_SAFE_ACTION.md` conflicts materially with bootstrap, certification contract/ledger, live authority, archetype registry or newer evidence: stop and reconcile.

```text
MATERIAL_CHANGE -> PROPORTIONAL_REVALIDATION
NO_MATERIAL_CHANGE -> NO_REAUDIT_LOOP
```
