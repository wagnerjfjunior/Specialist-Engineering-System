# SES — Specialist Certification for Any Project Contract v0.1

**Status:** `CANONICAL_V0_1 / UNIVERSAL_LIFECYCLE_GATE`

## 1. Purpose

Define the terminal SES lifecycle gate for a reusable specialist:

```text
CERTIFIED_FOR_ANY_PROJECT = YES
```

This gate answers one bounded question:

> Has this exact specialist release/runtime/archetype combination demonstrated enough reusable competence, runtime integrity, project isolation and bootstrap compatibility to be eligible for resolution across consumer projects without embedding project-local truth?

It does **not** certify any consumer project's product, implementation, security, production state or risk posture.

## 2. Universal boundary

This contract is UNIVERSAL SES infrastructure. It governs reusable specialist lifecycle certification, not consumer-project state.

```text
CERTIFIED_FOR_ANY_PROJECT
!= CONSUMER_PROJECT_ADOPTED
!= PROJECT_CONTEXT_READY
!= AUTHORIZED_TO_MUTATE
!= PUBLISHED
!= PRODUCTION_APPROVED
!= RISK_ACCEPTED
```

Consumer-project truth, live state, authority, environments, targets, adoption and local rules remain PROJECT-LOCAL.

## 3. Certification equation

`CERTIFIED_FOR_ANY_PROJECT = YES` is conjunctive. Every required obligation below must be satisfied for the exact certification subject.

```text
SPECIALIST CERTIFIED FOR ANY PROJECT
=
PROJECT-AGNOSTIC CONTRACT
+ L1 CANONICAL PASS
+ PROMPT INVARIANCE PASS
+ GENERIC BASELINE / NON-REGRESSION PASS
+ BUILDER KERNEL VERSIONED
+ BUILDER PACKAGE VERSIONED
+ ACTUAL BUILDER APPLIED
+ RUNTIME FINGERPRINT CAPTURED
+ L2 RUNTIME PASS
+ TOOL HONESTY / INTEGRATION PROOF
+ READINESS EVALUATION PASS
+ USER-AUTHORIZED READY
+ ARCHETYPE CONTRACT
+ ARCHETYPE RESOLUTION TEST PASS
+ ARCHETYPE ACTIVE
+ PROJECT BOOTSTRAP COMPATIBILITY
+ NO PROJECT-LOCAL LEAKAGE
+ NO UNRESOLVED HARD BLOCKER
```

A missing required obligation yields `NO`, `NOT_DETERMINED`, or `STALE_REVALIDATION_REQUIRED`; it never yields an inferred YES.

## 4. Certification subject and fingerprint binding

Certification belongs to an exact evidence-bound subject, not to a name in the abstract.

Record when available and material:

```text
ARCHETYPE_ID
CANDIDATE_ID / SPECIALIST_VERSION
BUILDER_KERNEL_PATH + BLOB/HASH
BUILDER_PACKAGE_PATH + BLOB/HASH
BUILDER_PROFILE_PATH + BLOB/HASH when a separate profile exists
RUNTIME_ID
RUNTIME_FINGERPRINT
MODEL / MATERIAL RUNTIME SETTINGS
TOOL / ACTION SURFACE
ARCHETYPE_CONTRACT_PATH + BLOB/HASH
ARCHETYPE_RESOLUTION_EVIDENCE
SES_REF_AT_CERTIFICATION
CERTIFICATION_EVIDENCE_REFS
```

A Builder profile may describe configuration, but it does not substitute for the required versioned Builder package at the terminal certification gate.

A materially changed runtime does not inherit certification merely because the archetype ID or display name is unchanged.

```text
HISTORICAL_PASS != CURRENT_CERTIFICATION
OLD_FINGERPRINT_PASS != NEW_FINGERPRINT_PASS
ARCHETYPE_ACTIVE != CERTIFIED_FOR_ANY_PROJECT
READY != CERTIFIED_FOR_ANY_PROJECT
BUILDER_PROFILE_VERSIONED != BUILDER_PACKAGE_VERSIONED
```

## 5. Required proof obligations

### C01 — Project-agnostic contract

The specialist contract/archetype must separate reusable method from project-local truth, state, authority, repositories, environments, business rules and targets.

### C02 — Canonical L1 behavioral competence

A canonical L1 suite must pass for the candidate. Packet generation, prose review or spec conformance alone is insufficient.

### C03 — Prompt invariance

Semantically equivalent tasks expressed with materially different wording/specificity must preserve critical findings, boundaries, blockers and safeguards.

### C04 — Generic baseline / non-regression

The specialist must not obtain domain depth by regressing critical generic reasoning, evidence discipline, assumption discipline or authority boundaries.

### C05 — Versioned Builder kernel

The executable Builder Instructions source must be versioned and reproducibly identifiable.

### C06 — Versioned Builder package

A complete Builder package for the certification subject must be versioned. It must bind the executable kernel to the expected Builder configuration, capabilities/tool surface and fingerprint requirements. A profile alone is insufficient for C06.

### C07 — Actual Builder applied

Repository configuration artifacts do not prove external application. Evidence must establish that the intended Builder/runtime configuration was actually applied.

### C08 — Runtime fingerprint captured

The tested runtime must be bound to a sufficiently reproducible fingerprint. Material limitations in provenance must remain explicit.

### C09 — L2 runtime behavioral PASS

The actual configured runtime must pass the applicable L2/runbook obligations. `BUILDER_APPLIED != RUNTIME_PROOF`.

### C10 — Tool honesty / integration proof

The runtime must prove truthful distinctions among tool availability, invocation and verified results. For a configured material integration, exercise the applicable bounded integration path. A no-tool specialist must still demonstrate that it does not fabricate tool execution.

### C11 — Readiness evaluation PASS

A separate readiness adjudication must find no unresolved critical failure or hard blocker for the exact fingerprint.

### C12 — User-authorized READY

READY promotion requires the applicable Product Authority/user authorization. Generation, testing or eligibility does not self-authorize promotion.

### C13 — Archetype contract

A reusable archetype contract must exist and preserve the specialist-specific method/boundaries without project-local leakage.

### C14 — Archetype resolution PASS

Deterministic ID/name/alias resolution, collision handling and fail-closed behavior must pass.

### C15 — Archetype ACTIVE

The canonical registry must resolve the archetype with `RESOLUTION_STATUS: ACTIVE`.

### C16 — Project bootstrap compatibility

The specialist/archetype must require project resolution/bootstrap/context before project-specific substantive work and must preserve:

```text
ARCHETYPE_RESOLVED != PROJECT_CONTEXT_READY
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
```

### C17 — No project-local leakage

No consumer-project identifiers, truth, business rules, repository targets, environments, secrets, risk acceptance or production authority may be frozen into the reusable specialist as universal behavior.

Technology examples or profiles are permitted when applicability is explicit and they do not become universal mandates.

### C18 — No unresolved hard blocker

Any unresolved hard blocker affecting a required obligation prevents certification.

## 6. Certification states

Use only evidence-bounded states:

```text
CERTIFIED_FOR_ANY_PROJECT = YES
CERTIFIED_FOR_ANY_PROJECT = NO
CERTIFIED_FOR_ANY_PROJECT = NOT_DETERMINED
CERTIFIED_FOR_ANY_PROJECT = STALE_REVALIDATION_REQUIRED
```

Semantics:

- `YES`: every C01-C18 obligation is satisfied for the exact subject/fingerprint.
- `NO`: at least one required obligation is demonstrably unsatisfied.
- `NOT_DETERMINED`: evidence is insufficient to decide one or more required obligations.
- `STALE_REVALIDATION_REQUIRED`: a prior YES existed, but a material invalidation event affects one or more certification dependencies.

`ABSENCE OF FINDING != PROOF OF ABSENCE`.

## 7. Evidence and history integrity

Certification adjudication must preserve chronology.

```text
INITIAL_FAIL remains historical FAIL
INITIAL_BLOCKED remains historical BLOCKED
USER_CORRECTED remains recorded
INITIAL_OVERCLAIM remains recorded
LATER_PASS is a later evidence event
RETROACTIVE_PASS = NO
RETROACTIVE_ERASURE = NO
```

A later valid PASS may satisfy the current obligation without rewriting the earlier event.

## 8. Invalidation and proportional revalidation

Material changes can invalidate only affected certification dependencies, including:

- Builder Instructions/kernel;
- Builder package or supporting profile;
- model or material runtime settings;
- Knowledge or system context surface;
- tool/action schema, authentication or permission surface;
- runtime product behavior affecting tested obligations;
- archetype contract or resolution semantics;
- bootstrap/context/authority contracts relied upon by certification;
- new contradictory evidence.

Use proportional revalidation. Do not rerun unaffected gates merely for confidence.

```text
MATERIAL_CHANGE -> INVALIDATE_AFFECTED_OBLIGATIONS
NO_MATERIAL_CHANGE -> NO_REAUDIT_LOOP
```

## 9. Portfolio ledger

The authoritative current SES certification ledger is:

`docs/SPECIALIST_CERTIFICATION_STATUS.md`

The portfolio certification adjudication that supports the initial ledger adoption is:

`tests/behavioral/evidence/SPECIALIST_CERTIFICATION_PORTFOLIO_ADJUDICATION_2026-08-17.md`

The ledger reports certification state and evidence references. It does not replace underlying proof artifacts.

`archetypes/REGISTRY.md` remains the authority for archetype resolution eligibility. Certification status must not silently change `RESOLUTION_STATUS` semantics.

## 10. Authorization boundary

SES may evaluate, test and recommend certification. It may not self-authorize READY, merge, publication, consumer adoption, production mutation or risk acceptance.

```text
GENERATE != AUTHORIZE != PUBLISH
TOOL CAPABILITY != AUTHORIZATION
CERTIFICATION ELIGIBLE != USER-AUTHORIZED READY
CERTIFIED_FOR_ANY_PROJECT != AUTHORIZED FOR THIS TARGET
```

## 11. Acceptance rule

A specialist is considered finished by SES only when:

```text
CERTIFIED_FOR_ANY_PROJECT = YES
```

subject to fingerprint validity and later proportional invalidation.

`READY` or `ACTIVE` alone is not a terminal SES specialist lifecycle state.