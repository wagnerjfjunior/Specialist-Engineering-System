# SES — Runtime Enforcement Gateway Contract Tests v0.1

**Status:** `NORMATIVE_CANDIDATE_V0_1`
**Target:** `core/protocols/RUNTIME_ENFORCEMENT_GATEWAY_CONTRACT.md`

## Required cases

| ID | Scenario | Expected |
|---|---|---|
| G01 | registered project + explicit adopted role + ACTIVE archetype + certified specialist | `ROUTABLE` |
| G02 | unknown project | `PROJECT_NOT_REGISTERED` |
| G03 | registered project + unmapped role | `SPECIALIST_ROLE_NOT_ADOPTED` |
| G04 | role maps to unknown archetype | `ARCHETYPE_NOT_RESOLVED` |
| G05 | role maps to inactive archetype | `ARCHETYPE_NOT_ACTIVE` |
| G06 | ACTIVE archetype without current certification YES | `SPECIALIST_NOT_CERTIFIED` |
| G07 | material fingerprint invalidation known without current eligible certification | fail closed |
| G08 | same role name in Project A and Project B maps to different archetypes | each project resolves independently |
| G09 | role/archetype spelling is merely similar but not exact | no fuzzy fallback; fail closed |
| G10 | legacy alias conflicts with explicit current role map | current explicit adopted mapping wins; history not rewritten |
| G11 | route is eligible but mutation authorization absent | `ROUTABLE`, mutation still unauthorized |
| G12 | adapter/bootstrap pointer required by route is unresolved | `PROJECT_BOOTSTRAP_UNRESOLVED` or bounded blocker |

## Acceptance

```text
PASS_REQUIRED = 12/12
FUZZY_OR_SEMANTIC_FALLBACK = 0
CROSS_PROJECT_CONTAMINATION = 0
UNAUTHORIZED_MUTATION = 0
ROUTABLE_AS_EXECUTED_OVERCLAIM = 0
```

These are contract-level cases. Passing this document by inspection does not prove a runtime implementation. PR2/runtime evidence must execute equivalent cases against the implementation.
