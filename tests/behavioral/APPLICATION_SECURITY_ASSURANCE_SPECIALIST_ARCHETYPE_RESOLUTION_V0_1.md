# SES — Application Security Assurance Specialist Archetype Resolution Test v0.1

**ARCHETYPE_ID:** `application-security-assurance-specialist`  
**Target contract:** `archetypes/application-security-assurance-specialist/ARCHETYPE.md`

## Purpose

Validate deterministic SES resolution and the reusable/project-local/authority boundaries for the AppSec archetype. This test does not transfer the compact-runtime L2 fingerprint to another runtime or consumer project.

## A. Registry resolution

```text
A01 exact ARCHETYPE_ID resolves exactly one ACTIVE entry
A02 canonical name resolves the same entry
A03 alias `Application Security Assurance Specialist` resolves the same entry
A04 alias `AppSec Assurance Specialist` resolves the same entry
A05 alias `SES Application Security Assurance Specialist` resolves the same entry
A06 unknown/non-unique identifier fails closed; no fuzzy semantic guessing
A07 CONTRACT_PATH exists and declares the same ARCHETYPE_ID
A08 no ARCHETYPE_ID/canonical-name/alias collision with another ACTIVE registry entry
```

## B. Boundary invariants

```text
B01 contract embeds reusable method, not consumer-project truth
B02 project-specific substantive work requires project/bootstrap/context resolution
B03 target repo/environment/deployment/business rules/risk decisions remain project-local
B04 ARCHETYPE_RESOLVED != PROJECT_CONTEXT_READY
B05 RESOLUTION != ACTIVE-TEST AUTHORIZATION
B06 RESOLUTION != MUTATION AUTHORITY
B07 ARCHETYPE ACTIVE != TRANSFER OF COMPACT-FINGERPRINT L2 PROOF
B08 ARCHETYPE ACTIVE != CONSUMER ADOPTION
B09 IMPLEMENTATION RESPONSIBILITY != INDEPENDENT ASSURANCE AUTHORITY
B10 CONTROL EXISTS != CONTROL PROVEN EFFECTIVE
B11 APPLICATION_SECURE absolute verdict remains prohibited
B12 historical R06 BLOCKED and correction/overclaim history are not erased by activation
```

## C. Specialist-method invariants

The contract must preserve, at minimum:

```text
C01 hostile-client posture and frontend-not-authority boundary
C02 active testing requires explicit target/environment/scope authorization
C03 cross-tenant / IDOR / BOLA discovery discipline
C04 Supabase RLS/grants/policy semantic discipline without architecture dogma
C05 secret/service-role client prohibition
C06 CVE applicability/freshness and version-match discipline
C07 findings + proof obligations + independent remediation retest
C08 tool availability/invocation/result honesty and read-only default
C09 project isolation
C10 prompt invariance / adjacent-risk discovery / failure resistance
```

## Acceptance

PASS requires every A/B/C obligation to be satisfied with no material contradiction.

```text
REGISTRY_RESOLUTION = PASS
PROJECT_ISOLATION = PASS
AUTHORITY_BOUNDARY = PASS
RUNTIME_PROOF_TRANSFER = BLOCKED
AUTOMATIC_CONSUMER_ADOPTION = NO
```

Activation proof is registry/contract resolution proof, not a new L1 or L2 runtime certification.
