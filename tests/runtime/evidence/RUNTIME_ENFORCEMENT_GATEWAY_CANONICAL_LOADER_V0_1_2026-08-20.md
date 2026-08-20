# SES — Runtime Enforcement Gateway Canonical Loader v0.1 Evidence — 2026-08-20

**Subject:** `runtime/specialist_gateway/github_loader.py`  
**Controller:** `runtime/specialist_gateway/controller.py`  
**Test source:** `tests/runtime/test_specialist_gateway_loader.py`

## Scope

Validate the minimal read-only materialization layer required to turn the existing deterministic controller into an operational runtime candidate without hardcoded project/archetype/certification state.

The loader resolves one SES `main` SHA and reads all material routing sources at that exact ref before instantiating the controller.

## Observed local execution

Command executed in the implementation environment:

```text
python -m unittest tests.runtime.test_specialist_gateway_loader -v
```

Observed result:

```text
L01 project registry parsing = PASS
L02 archetype registry parsing = PASS
L03 certification ledger parsing = PASS
L04 project adapter role-map parsing = PASS
L05 resolved snapshot routes with pinned SES_REF = PASS
L06 legacy/unmapped role fails closed = PASS
L07 missing registry records fail closed = PASS
TOTAL = 7/7 PASS
```

The execution used deterministic in-memory GitHub client fixtures matching the current canonical Markdown shapes. It did not claim a live external GitHub network invocation from the candidate runtime service.

## Security / authority properties

```text
GITHUB_CLIENT = READ_ONLY
SECRET_IN_REPOSITORY = NO
SES_REF_PINNING_PER_SNAPSHOT = YES
FUZZY_ROLE_ROUTING = NO
AUTOMATIC_PROJECT_ADOPTION = NO
MUTATION_AUTHORITY = NO
STALE_FALLBACK_AFTER_LOAD_FAILURE = NO / CALLER MUST FAIL CLOSED
```

## Bounded verdict

```text
CANONICAL_LOADER_UNIT_TESTS = PASS / 7_OF_7
CONTROLLER_HISTORICAL_G01_G12 = UNCHANGED
EXTERNAL_HTTP_RUNTIME = NOT_YET_PROVEN
DEPLOYMENT = NOT_CLAIMED
ACTION_TOOL_INVOCATION = NOT_CLAIMED
REPOSITORY_CI = NOT_CLAIMED UNLESS SEPARATELY OBSERVED
```
