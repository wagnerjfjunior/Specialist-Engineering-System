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

Observed result after self-audit correction:

```text
L01 project registry parsing = PASS
L02 archetype registry parsing = PASS
L03 certification ledger parsing + explicit current subject = PASS
L04 project adapter role-map parsing = PASS
L05 resolved snapshot routes with pinned SES_REF = PASS
L06 legacy/unmapped role fails closed = PASS
L07 missing registry records fail closed = PASS
L08 Certification=YES without identifiable current subject => UNSUPPORTED = PASS
TOTAL = 8/8 PASS
```

Initial implementation review identified that treating every ledger `YES` as `fingerprint_status=CURRENT` would overclaim eligibility when the current certified subject was not explicit. The loader was corrected before merge, and `docs/SPECIALIST_CERTIFICATION_STATUS.md` was normalized to expose the current certified subjects for all five certified archetypes.

```text
INITIAL_LOADER_ASSUMPTION = YES_IMPLIES_CURRENT
SELF_AUDIT_RESULT = UNSAFE / CORRECTED
RETROACTIVE_PASS = NO
```

The execution used deterministic in-memory GitHub client fixtures matching the canonical Markdown shapes. It did not claim a live external GitHub network invocation from the candidate runtime service.

## Security / authority properties

```text
GITHUB_CLIENT = READ_ONLY
SECRET_IN_REPOSITORY = NO
SES_REF_PINNING_PER_SNAPSHOT = YES
CERTIFICATION_SUBJECT_REQUIRED_FOR_CURRENT = YES
FUZZY_ROLE_ROUTING = NO
AUTOMATIC_PROJECT_ADOPTION = NO
MUTATION_AUTHORITY = NO
STALE_FALLBACK_AFTER_LOAD_FAILURE = NO / CALLER MUST FAIL CLOSED
```

## Bounded verdict

```text
CANONICAL_LOADER_UNIT_TESTS = PASS / 8_OF_8
CONTROLLER_HISTORICAL_G01_G12 = UNCHANGED
EXTERNAL_HTTP_RUNTIME = NOT_YET_PROVEN
DEPLOYMENT = NOT_CLAIMED
ACTION_TOOL_INVOCATION = NOT_CLAIMED
REPOSITORY_CI = NO STATUS CHECKS OBSERVED ON PR HEAD AT REVIEW TIME
```
