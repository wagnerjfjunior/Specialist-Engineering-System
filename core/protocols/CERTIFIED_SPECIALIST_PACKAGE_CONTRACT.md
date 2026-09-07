# SES — Certified Specialist Package Contract

**Status:** FOUNDATION_V0_1 / CORE_PROTOCOL / PORTABLE_EXECUTION_CANDIDATE

## 1. Purpose

Define the immutable certification-bound package that may execute ordinary consumer-project work without requiring central SES live access.

```text
SES -> DESIGN / TEST / CERTIFY -> CERTIFIED PACKAGE -> DISTRIBUTION -> PROJECT
SES AUTHORING DEPENDENCY != SES RUNTIME DEPENDENCY
```

## 2. Eligibility

Universal portable execution requires the exact certification subject to have:

`CERTIFIED_FOR_ANY_PROJECT = YES`

Project-specific packages may exist, but must not claim universal/public SES eligibility.

## 3. Required binding

A package must identify, when material:

```text
PACKAGE_ID
ARCHETYPE_ID
PACKAGE_VERSION
CERTIFICATION_STATUS
CERTIFICATION_SUBJECT / EVIDENCE_REF
SES_BASELINE_REF
ARCHETYPE_SOURCE_REF
KERNEL_OR_INSTRUCTIONS_REF + FINGERPRINT
ACTION_OR_TOOL_PROFILE_REF
MODEL_OR_RUNTIME_CONFIGURATION_BOUNDARY
PORTABLE_EXECUTION_ELIGIBILITY
PUBLICATION_STATUS
```

The binding must be sufficient to determine whether a running distribution still matches the certified subject.

## 4. Fingerprint discipline

```text
NO MATERIAL FINGERPRINT CHANGE -> NO AUTOMATIC RECERTIFICATION
MATERIAL DELTA -> INVALIDATE AFFECTED OBLIGATIONS ONLY -> PROPORTIONAL REVALIDATION
```

A material change to certification-bound Instructions/kernel, Action/tool surface, model/runtime configuration, authority/safety behavior, identity/scope or other fingerprint element creates a new package version or invalid binding.

## 5. Portable execution

For ordinary project work an exact valid package uses:

```text
CERTIFIED PACKAGE
+ EXPLICIT / DETERMINISTIC PROJECT
+ PROJECT BOOTSTRAP
+ PROJECT RULES / CONTINUITY / EVIDENCE
```

Central SES `main`, Registry, Archetype Registry and Project Adapter are not runtime prerequisites unless current SES state is material.

SES live is required again for SES governance, specialist creation/evolution/certification, package creation/upgrade, current SES compatibility, candidate validation, or current Registry/Adapter/adoption claims.

`NORMAL CONSUMER EXECUTION MUST NOT REQUIRE CENTRAL SES LIVE AVAILABILITY`

## 6. Project authority

```text
PACKAGE = REUSABLE METHOD + CERTIFIED RUNTIME BINDING
PROJECT = TRUTH + LIVE STATE + AUTHORITY + ENVIRONMENT + ADOPTION
PACKAGE_AVAILABLE != PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
```

Portable execution removes a central dependency; it does not remove project bootstrap, evidence or authorization requirements.

## 7. Versioning and adoption

```text
PROJECT/RUNTIME BINDS PACKAGE X
SES MAIN MOVES TO Y
-> PACKAGE X REMAINS X

CENTRAL EVOLUTION
!= AUTOMATIC PACKAGE UPGRADE
!= AUTOMATIC PROJECT MUTATION
```

Moving X -> Y is an explicit adoption/upgrade event.

## 8. Distribution

A package may be distributed as public GPT, private GPT, project-bound GPT, API/runtime or another deterministic channel.

```text
CERTIFIED PACKAGE != PUBLIC GPT
GENERATE != CERTIFY != AUTHORIZE != PUBLISH
```

A public SES specialist requires an exact `CERTIFIED_FOR_ANY_PROJECT = YES` package plus explicit publication authorization.

## 9. Migration safety

Existing certified specialists are not invalidated by this contract.

```text
NOT YET PACKAGE-BOUND -> EXISTING SES-MEDIATED PATH REMAINS VALID
EXISTING CERTIFICATION + EXACT PACKAGE BINDING + NO MATERIAL FINGERPRINT CHANGE
-> NO FULL RECERTIFICATION

PARTIAL MIGRATION MUST NOT BREAK EXISTING CERTIFIED SPECIALISTS
```

No specialist is forced onto portable execution without an exact package binding.

## 10. Transport boundary

```text
PORTABLE PACKAGE EXISTS
!= @-MENTION WORKS
!= ACTION IS EXPOSED THROUGH @
!= SPECIALIST-TO-SPECIALIST COMPOSITION WORKS
```

Those claims require end-to-end proof in the actual runtime.

## 11. Fail states

Use when applicable: `CERTIFIED_PACKAGE_UNAVAILABLE`, `CERTIFIED_PACKAGE_BINDING_INVALID`, `PACKAGE_FINGERPRINT_MISMATCH`, `PACKAGE_NOT_PORTABLE_ELIGIBLE`, `PROJECT_CANONICAL_SOURCE_UNRESOLVED`, `PROJECT_BOOTSTRAP_UNAVAILABLE`, `AUTHORITY_MODEL_UNRESOLVED`, `MISSING_EVIDENCE`, `MUTATION_NOT_AUTHORIZED`.

Missing central SES access alone is not a portable-execution failure unless current SES state is material.

## 12. Acceptance

Portable execution must prove:
1. exact certification/fingerprint binding;
2. ordinary project work without central SES availability;
3. no automatic change when SES `main` advances;
4. project evidence/authority remain mandatory;
5. project-switch isolation;
6. lifecycle tasks reintroduce SES live dependency;
7. fingerprint divergence invalidates the old binding;
8. non-migrated specialists keep their existing path;
9. distribution remains separate from certification;
10. no `@` success claim without runtime evidence.

Tests: `tests/behavioral/CERTIFIED_SPECIALIST_PORTABLE_EXECUTION_TESTS.md`.
