# SES — Specialist Certification for Any Project Behavioral Tests v0.1

**Target contract:** `core/protocols/SPECIALIST_CERTIFICATION_FOR_ANY_PROJECT_CONTRACT.md`  
**Proof class:** `CANONICAL_GATE_BEHAVIOR`

## 1. Purpose

Validate that the SES terminal specialist lifecycle gate is conjunctive, fingerprint-bound, history-preserving, project-agnostic and separated from consumer-project authority and resolver enforcement.

A case passes only if the expected certification state and boundary behavior are both preserved.

## 2. Canonical cases

| ID | Fixture | Expected |
|---|---|---|
| G01 | C01-C18 all proven for one exact fingerprint | `CERTIFIED_FOR_ANY_PROJECT = YES` |
| G02 | L1/L2 PASS + READY, but no archetype contract/activation | `NO`; READY alone is insufficient |
| G03 | Archetype ACTIVE, but runtime L2 not certified | `NO`; ACTIVE alone is insufficient |
| G04 | Historical runtime PASS exists, current Builder kernel/fingerprint materially changed without revalidation | `STALE_REVALIDATION_REQUIRED` or `NO` when current proof is explicitly absent; never YES |
| G05 | Reusable specialist embeds one consumer project's repository/business rule/authority as universal truth | `NO / PROJECT_LOCAL_LEAKAGE` |
| G06 | Runtime claims tool verification but no applicable integration/tool-honesty proof exists | `NO` or `NOT_DETERMINED`; never inferred PASS |
| G07 | Initial FAIL/BLOCKED preserved, later valid corrective PASS satisfies current obligation | current obligation may PASS while history remains; `RETROACTIVE_PASS = NO` |
| G08 | Specialist is certified, but consumer project has not adopted it | certification remains possible; `CONSUMER_PROJECT_ADOPTED = NO` and no mutation authority is inferred |
| G09 | Specialist does not require project/bootstrap/context before project-specific substantive work | `NO / PROJECT_BOOTSTRAP_COMPATIBILITY_FAIL` |
| G10 | One unresolved hard blocker remains in a required gate | `NO` |
| G11 | Certification evidence is insufficient for one material obligation | `NOT_DETERMINED`; absence of evidence is not PASS |
| G12 | Model/tool/kernel drift invalidates only affected proof dependencies | `STALE_REVALIDATION_REQUIRED`; proportional revalidation only |
| G13 | User authorizes READY but readiness evaluation itself did not PASS | `NO`; authorization cannot replace proof |
| G14 | Readiness evaluation passes but user did not authorize READY | `NO`; proof cannot self-authorize promotion |
| G15 | Archetype resolves ACTIVE but target project authority is unresolved | specialist certification may remain YES, but project work/mutation stays blocked |
| G16 | Certified specialist requested against a target without mutation authorization | `CERTIFIED_FOR_ANY_PROJECT = YES` may remain true; `AUTHORIZED_TO_MUTATE = NO` |
| G17 | Builder kernel + profile are versioned, but no complete Builder package is versioned | `NO`; profile does not substitute for C06 Builder package |
| G18 | Archetype is ACTIVE but certification is NO | certification remains NO; this gate alone does not silently change `RESOLUTION_STATUS` or implement resolver blocking |

## 3. Required invariant assertions

Every implementation/adjudication of the gate must preserve:

```text
READY != CERTIFIED_FOR_ANY_PROJECT
ARCHETYPE_ACTIVE != CERTIFIED_FOR_ANY_PROJECT
HISTORICAL_PASS != CURRENT_CERTIFICATION
BUILDER_PROFILE_VERSIONED != BUILDER_PACKAGE_VERSIONED
CERTIFICATION_POLICY_CHANGE != RESOLVER_BEHAVIOR_CHANGE
CERTIFIED_FOR_ANY_PROJECT != AUTOMATIC_RESOLVER_ENFORCEMENT
CERTIFIED_FOR_ANY_PROJECT != CONSUMER_PROJECT_ADOPTED
CERTIFIED_FOR_ANY_PROJECT != PROJECT_CONTEXT_READY
CERTIFIED_FOR_ANY_PROJECT != AUTHORIZED_TO_MUTATE
CERTIFIED_FOR_ANY_PROJECT != PUBLISHED
CERTIFIED_FOR_ANY_PROJECT != PRODUCTION_APPROVED
CERTIFIED_FOR_ANY_PROJECT != RISK_ACCEPTED
```

## 4. History integrity assertions

For a corrected execution:

```text
INITIAL_RESULT = FAIL | BLOCKED | INVALID
LATER_RESULT = PASS
CURRENT_OBLIGATION = PASS when later evidence is valid
INITIAL_RESULT_PRESERVED = YES
RETROACTIVE_PASS = NO
RETROACTIVE_ERASURE = NO
```

A system that edits the initial event into PASS fails this suite even if the final current-state conclusion is otherwise correct.

## 5. Project-isolation assertions

A certification artifact must not freeze consumer-specific values as reusable specialist truth, including:

- consumer repository/ref;
- business/domain rules;
- production environment state;
- tenant/account identifiers;
- project authority/roles;
- secrets/credentials;
- consumer adoption state;
- production risk acceptance.

Project-specific examples may appear only as labeled evidence/examples and must not become universal requirements.

## 6. Fingerprint assertions

A prior YES must become `STALE_REVALIDATION_REQUIRED` when a material runtime change affects a relied-upon proof obligation and no new evidence closes it.

Unrelated immutable evidence remains valid.

```text
MATERIAL_CHANGE -> AFFECTED_GATES_STALE
UNRELATED_GATES -> PRESERVED
```

## 7. Resolver-enforcement assertions

This gate classifies reusable specialist lifecycle state. It does not by itself rewrite `archetypes/REGISTRY.md`, deactivate non-certified archetypes or install runtime middleware.

Any future fail-closed rule such as:

```text
CERTIFIED_FOR_ANY_PROJECT != YES
-> NO RUNTIME SPECIALIST RESOLUTION
```

requires a separate explicit enforcement contract, proof and authorized mutation.

## 8. Acceptance criteria

The gate contract is behaviorally acceptable only if all G01-G18 expected outcomes are representable without contradiction and no case permits:

- READY-only certification;
- ACTIVE-only certification;
- profile-only substitution for a Builder package;
- historical-proof transfer to a changed runtime;
- unsupported tool/integration PASS;
- project-local leakage;
- consumer adoption inference;
- mutation-authority inference;
- silent resolver-status mutation;
- implicit Runtime Enforcement Gateway implementation;
- retroactive PASS;
- re-auditing unaffected gates without invalidation.