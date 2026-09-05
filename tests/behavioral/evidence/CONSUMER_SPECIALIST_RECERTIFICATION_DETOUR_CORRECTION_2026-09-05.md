# SES — Consumer Specialist Handoff / Re-certification Detour Correction — 2026-09-05

**Status:** `STATIC_CONTRACT_CORRECTION / H21-H24_SPEC_PASS / BACKEND_V0_2_NOT_RECERTIFIED`

## Trigger

FECH.AI interrupted STS-M2 work and proposed this SES detour:

```text
SES — Backend & Data Platform Specialist v0.2
PROPORTIONAL CERTIFICATION CLOSURE
→ certify v0.2
→ then rerun STS-M2-04B1
```

The Product Authority explicitly rejected repeating specialist certification and required the project not to stop on this SES-internal lifecycle concern.

## Existing canonical facts

```text
ARCHETYPE_ID = backend-data-platform-specialist
ARCHETYPE_STATUS = ACTIVE
CERTIFIED_FOR_ANY_PROJECT = YES
CURRENT_CERTIFIED_SUBJECT = backend-data-platform-specialist-v0.1

V0_2_CANDIDATE_EXISTS = YES
V0_2_KERNEL_BLOB = 01f68d536830e9921f8b1171859b8c1ba30c26f1
BDP-PF-08 = PASS
V0_2_CERTIFIED_FOR_ANY_PROJECT = NO / NOT CLAIMED
```

The v0.2 candidate was created to correct live-audit admission/bootstrap behavior. It does not erase the already-certified v0.1 subject, and its existence does not automatically make the archetype uncertified.

## Root cause

The manual-handoff path had two concerns conflated:

1. **consumer consultation eligibility** — whether a project can consult an adopted ACTIVE/certified SES archetype;
2. **SES release lifecycle** — whether a newer exact Builder/runtime fingerprint is itself the current universally certified release.

The project incorrectly promoted concern 2 into its own next-safe-action chain even though its task was to consult the already-adopted Backend/Data role.

## Universal v0.3 rule

```text
ADOPTED ROLE
+ ACTIVE ARCHETYPE
+ CURRENT SES LEDGER CERTIFICATION = YES
→ CONSULTATION ELIGIBLE

NONCURRENT SES CANDIDATE EXISTS
!= CONSUMER PROJECT BLOCKED

SPECIALIST_OUTPUT_USABLE_AS_BOUNDED_EVIDENCE
!= EXACT_RUNTIME_CERTIFIED_FOR_ANY_PROJECT

PROJECT_LOCAL_TOOL_PROOF
!= UNIVERSAL SES RUNTIME CERTIFICATION

UNIVERSAL RUNTIME CERTIFICATION GAP
!= PROJECT_LOCAL TOOL UNUSABLE
```

Exact-runtime certification blocks a consumer consultation only if that exact certified fingerprint is explicitly material to the task or required by project authority.

## Backend/Data consequence

FECH.AI must not require:

```text
BACKEND_DATA_PLATFORM_SPECIALIST_V0_2
→ CERTIFIED_FOR_ANY_PROJECT = YES
```

as a generic prerequisite to continue STS-M2.

It may consult:

```text
ROLE = backend_data
ARCHETYPE_ID = backend-data-platform-specialist
CANONICAL_TARGET = SES — Backend & Data Platform Specialist
SELECTION_STATUS = ADOPTED_ROLE
CURRENT_LEDGER_CERTIFICATION = YES
```

If the external specialist runtime uses the noncurrent v0.2 delta, its returned result is consumed as bounded evidence with exact tool/provenance claims. That use does not certify v0.2 and does not require the Product Authority to repeat certification work.

## H21-H24 static adjudication

```text
H21 CONSUMER_NO_RECERTIFICATION_DETOUR = PASS
H22 NONCURRENT_RUNTIME_BOUNDED_EVIDENCE = PASS
H23 PROJECT_LOCAL_TOOL_PROOF_SEPARATION = PASS
H24 EXACT_RUNTIME_BLOCKER_REQUIRES_MATERIALITY = PASS

H21-H24 = PASS / SPEC_CONFORMANCE
```

## Historical integrity

```text
BACKEND_V0_1_CERTIFICATION = PRESERVED
BACKEND_V0_2_BDP_PF_08_PASS = PRESERVED
BACKEND_V0_2_UNIVERSAL_CERTIFICATION = NOT CLAIMED
RETROACTIVE_PASS = NO
USER_REQUIRED_RECERTIFICATION = NO
```

This correction changes routing/handoff admission semantics only. It does not weaken tool honesty, certification fingerprint rules, project authority, security gates or runtime proof requirements.
