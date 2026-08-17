# SES — Backend & Data Platform Specialist Archetype Resolution Validation v0.1

**Evidence ID:** `backend-data-platform-specialist-archetype-resolution-v0.1`  
**Candidate branch:** `feat/specialist-portfolio-wave-2`  
**Target archetype:** `backend-data-platform-specialist`

## 1. Purpose

Validate the registry-resolution behavior introduced by activating the reusable Backend & Data Platform Specialist archetype. This is a registry/resolution proof only; it does not repeat L1 or L2 competence/runtime validation.

## 2. Candidate sources

```text
REGISTRY = archetypes/REGISTRY.md
ARCHETYPE CONTRACT = archetypes/backend-data-platform-specialist/ARCHETYPE.md
VALIDATED CANDIDATE = backend-data-platform-specialist-v0.1
L2 PROOF = tests/runtime/evidence/BACKEND_DATA_PLATFORM_L2_FINAL_VERDICT_2026-08-17.md
READINESS = tests/runtime/evidence/BACKEND_DATA_PLATFORM_SPECIALIST_READINESS_DECISION_2026-08-17.md
```

## 3. Resolution cases

| Case | Input | Expected | Result |
|---|---|---|---|
| A01 | `backend-data-platform-specialist` | one ACTIVE match → Backend/Data contract | PASS |
| A02 | `SES — Backend & Data Platform Specialist` | one ACTIVE canonical-name match | PASS |
| A03 | `Backend & Data Platform Specialist` | one ACTIVE alias match | PASS |
| A04 | `Backend Data Platform Specialist` | one ACTIVE alias match | PASS |
| A05 | `SES Backend & Data Platform Specialist` | one ACTIVE alias match | PASS |
| A06 | unknown identifier | zero ACTIVE matches → fail closed | PASS |
| A07 | contract path | `archetypes/backend-data-platform-specialist/ARCHETYPE.md` exists and declares same ARCHETYPE_ID | PASS |
| A08 | collision scan | no ID/name/alias collision with existing registered archetypes | PASS |

## 4. Reuse/project-isolation cases

| Case | Obligation | Result |
|---|---|---|
| B01 | reusable method does not embed consumer-project truth | PASS |
| B02 | project-specific work requires SES hybrid/project bootstrap | PASS |
| B03 | repository/database/deployment/business-rule targets remain project-local | PASS |
| B04 | archetype resolution does not imply project-context readiness | PASS |
| B05 | resolution does not grant mutation authority | PASS |
| B06 | registry activation does not transfer fingerprint-bound L2 proof to changed runtimes | PASS |
| B07 | registry activation does not automatically adopt into consumer projects | PASS |
| B08 | implementation owner remains distinct from independent assurance owner | PASS |

## 5. Semantic boundary checks

The contract preserves these material invariants:

```text
IMPLEMENTATION OWNER != INDEPENDENT ASSURANCE OWNER
FRONTEND CHECK != AUTHORITATIVE ENFORCEMENT
AUTHENTICATION != AUTHORIZATION
RLS ENABLED != POLICY CORRECT
SELECT-THEN-WRITE CHECK != CONCURRENCY GUARANTEE
BACKEND TEST PASS != INDEPENDENT APPSEC RETEST PASS
IMPLEMENTATION READY != AUTHORIZED FOR PRODUCTION
ARCHETYPE METHOD != PROJECT TRUTH
ARCHETYPE_RESOLVED != PROJECT_CONTEXT_READY
CONTEXT_READY != AUTHORIZED_TO_MUTATE
```

Supabase guidance is explicitly technology-specific and does not become a universal architecture mandate.

## 6. Adjudication

```text
ARCHETYPE_CONTRACT_PRESENT = PASS
ARCHETYPE_ID_UNIQUE = PASS
CANONICAL_NAME_RESOLUTION = PASS
ALIASES_RESOLUTION = PASS
UNKNOWN_FAIL_CLOSED = PASS
CONTRACT_ID_PATH_BINDING = PASS
REGISTRY_COLLISION_CHECK = PASS
PROJECT_AGNOSTIC_BOUNDARY = PASS
PROJECT_BOOTSTRAP_REQUIRED = PASS
AUTHORITY_BOUNDARY = PASS
IMPLEMENTATION_ASSURANCE_SEPARATION = PASS
RUNTIME_PROOF_TRANSFER_BLOCKED = PASS
AUTOMATIC_CONSUMER_ADOPTION = NO
```

## 7. Conclusion

```text
BACKEND_DATA_PLATFORM_SPECIALIST_ARCHETYPE_RESOLUTION = PASS
ELIGIBLE_RESOLUTION_STATUS = ACTIVE
AVAILABLE_FOR_PROJECT_RESOLUTION = YES
```

This conclusion is candidate-head evidence until the activation changes are merged into canonical `main`.

```text
CANDIDATE_HEAD_RESOLUTION_PASS
!= CANONICAL_MAIN_ACTIVE
```

No L1/L2 rerun is required because this activation change does not alter the validated Builder fingerprint or specialist competency semantics; it adds the reusable archetype contract and deterministic registry routing only.