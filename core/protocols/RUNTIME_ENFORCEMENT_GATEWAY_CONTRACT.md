# SES — Runtime Enforcement Gateway Contract v0.1

**Status:** `CANDIDATE_V0_1 / UNIVERSAL_RUNTIME_ENFORCEMENT_CONTRACT`

## 1. Purpose

Define the smallest universal runtime contract that turns certified reusable SES specialists into deterministic, project-bounded routable capabilities without creating automatic project adoption or mutation authority.

The Gateway answers one bounded question:

> Given an explicit project and project role, is there one adopted, active, certification-eligible SES archetype that may be routed for project bootstrap under the current runtime policy?

The Gateway is enforcement infrastructure. It is not a Product Authority, project source of truth, specialist implementation, Builder, deployment service or autonomous intent router.

## 2. Boundary

```text
CORE CONTRACT = UNIVERSAL SEMANTICS
RUNTIME GATEWAY = EXECUTION OF THOSE SEMANTICS
PROJECT ADAPTER = PROJECT-LOCAL ROLE -> ARCHETYPE ADOPTION
ARCHETYPE REGISTRY = REUSABLE SPECIALIST RESOLUTION
CERTIFICATION LEDGER = CURRENT CERTIFICATION ELIGIBILITY
CONSUMER PROJECT = TRUTH / AUTHORITY / STATE / LOCAL RULES
```

Preserve:

```text
CERTIFIED_FOR_ANY_PROJECT != CONSUMER_PROJECT_ADOPTED
ARCHETYPE_ACTIVE != CONSUMER_PROJECT_ADOPTED
PROJECT_ADOPTED != PROJECT_CONTEXT_READY
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
TOOL_CAPABILITY != AUTHORIZATION
ROUTABLE != EXECUTED
```

## 3. Inputs

Minimum routing input:

```text
PROJECT_IDENTIFIER
ROLE
TASK_SCOPE
```

`ROLE` must already be explicit or deterministically produced by a separately versioned caller/project rule. Gateway v0.1 does not semantically guess role from free text.

## 4. Authoritative resolution chain

For project-specialist routing:

```text
PROJECT_IDENTIFIER
→ projects/REGISTRY.md
→ unique ACTIVE Project Adapter
→ SPECIALIST_ROLE_MAP
→ exact ROLE match
→ ARCHETYPE_ID
→ archetypes/REGISTRY.md
→ unique ACTIVE archetype
→ docs/SPECIALIST_CERTIFICATION_STATUS.md
→ CERTIFIED_FOR_ANY_PROJECT = YES for that archetype
→ project bootstrap compatibility path
→ ROUTABLE
```

All resolution is fail-closed and exact according to the applicable registries/contracts.

## 5. Required gateway decisions

Gateway v0.1 emits exactly one primary routing state:

```text
ROUTABLE
PROJECT_NOT_REGISTERED
PROJECT_ID_AMBIGUOUS
PROJECT_ADAPTER_UNRESOLVED
SPECIALIST_ROLE_NOT_ADOPTED
ARCHETYPE_NOT_RESOLVED
ARCHETYPE_NOT_ACTIVE
SPECIALIST_NOT_CERTIFIED
PROJECT_BOOTSTRAP_UNRESOLVED
RUNTIME_FINGERPRINT_STALE_OR_UNSUPPORTED
BLOCKED
```

A `ROUTABLE` decision means only that the selected specialist may enter the project bootstrap/context process. It does not authorize substantive conclusions or mutation before the applicable specialist/bootstrap readiness and authority rules are satisfied.

## 6. Adoption semantics

The Gateway does not create adoption. It reads the project's explicit adapter mapping:

```text
ROLE -> ARCHETYPE_ID
ADOPTION_STATUS = ADOPTED
```

If the role is absent, inactive or not explicitly `ADOPTED`, emit `SPECIALIST_ROLE_NOT_ADOPTED`.

Do not route to a merely similar role or archetype.

No SES central change silently adds a role to a consumer project.

## 7. Archetype and certification eligibility

A mapped archetype is routable only when:

```text
RESOLUTION_STATUS = ACTIVE
AND
CERTIFIED_FOR_ANY_PROJECT = YES
```

The Gateway must resolve both states live from their canonical SES sources for the effective ref used by the routing decision.

The Gateway must not infer certification from archetype lifecycle labels, Builder names, historical evidence or previous conversations.

## 8. Runtime fingerprint policy

Certification is fingerprint-bound. Gateway v0.1 may use the canonical certification ledger as the routing eligibility source when it identifies the current certified subject/fingerprint.

If a material runtime change is known to invalidate the certified subject and the ledger has not established a current eligible fingerprint, fail closed as `RUNTIME_FINGERPRINT_STALE_OR_UNSUPPORTED` or `SPECIALIST_NOT_CERTIFIED` as applicable.

The Gateway must not silently transfer an old fingerprint PASS to a changed runtime.

## 9. Project bootstrap and authority

After routing eligibility, the specialist must still execute the applicable project bootstrap and project-local resolution contracts.

The Gateway may verify required entrypoints/pointers exist, but it must not fabricate project context or authority.

```text
ROUTABLE
→ PROJECT BOOTSTRAP
→ PROJECT-LOCAL SPECIALIST/RULES
→ CONTINUITY/AUTHORITY WHEN MATERIAL
→ CONTEXT READINESS
→ SUBSTANTIVE WORK
```

Mutation remains separately authorized.

## 10. Project isolation

Each project is resolved independently. A route, local rule, authority decision, environment, continuity state or evidence from one project must not be reused as project truth for another.

A project switch invalidates project-scoped routing/context state except universal SES contracts and current registry/certification evidence.

## 11. Traceability

Each material routing decision should be reproducible from a compact receipt containing, when available:

```text
SES_REF
PROJECT_IDENTIFIER_SUPPLIED
PROJECT_ID
PROJECT_ADAPTER_PATH
ROLE
ADOPTION_STATUS
ARCHETYPE_ID
ARCHETYPE_CONTRACT_PATH
ARCHETYPE_RESOLUTION_STATUS
CERTIFICATION_STATUS
CERTIFIED_FINGERPRINT_OR_SUBJECT
PROJECT_BOOTSTRAP_ENTRYPOINT
DECISION
BLOCKER
```

Do not include secrets or unnecessary project data.

## 12. Non-goals v0.1

Gateway v0.1 does not require or provide:

- database-backed policy storage;
- dashboard/UI;
- automatic free-text intent classification;
- automatic project mutation;
- automatic specialist adoption;
- automatic specialist version upgrade;
- autonomous Builder creation/configuration;
- production deployment service;
- broad permissions language;
- centralized storage of consumer-project truth.

These may be considered only after observed use demonstrates a material need.

## 13. Acceptance criteria

The v0.1 implementation must prove at minimum:

1. registered project + adopted role + ACTIVE + certified archetype => `ROUTABLE`;
2. unknown project => fail closed;
3. unmapped role => fail closed without guessing;
4. inactive/unresolved archetype => fail closed;
5. non-certified/stale specialist => fail closed;
6. same role name in different projects may map differently without cross-project contamination;
7. `ROUTABLE` never becomes mutation authorization;
8. evidence receipt identifies the actual resolved project, adapter, role and archetype;
9. no semantic/fuzzy role or archetype fallback occurs;
10. historical aliases do not override current explicit project adoption mapping.

## 14. Invalidation

Material changes to project-resolution semantics, role-map semantics, archetype resolution, certification eligibility policy or gateway decision semantics require proportional revalidation.

Adding a new certified archetype alone does not invalidate the Gateway. Adding or changing a project's role mapping affects that project mapping and its compatibility tests, not unrelated projects.
