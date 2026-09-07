# SES — Certified Portable Binding Retest PASS — 2026-09-07

**Status:** USER_SUPPLIED_RUNTIME_OUTPUT / PROPORTIONAL_BINDING_RETEST_PASS
**SES main at evidence capture:** `35e464191869df157dd82910c59777c5abae32a5`

## Scope

This evidence records the user-supplied receipt-only runtime outputs for:

- Software Systems Architect portable v0.3 candidate;
- Documentation Auditor portable v1.3 candidate.

This retest closes only the binding/receipt defect identified in the prior v0.2/v1.2 runtime evidence.

```text
PRIOR FAIL
!=
RETROACTIVE PASS

NEW CANDIDATE
+ NEW RUNTIME EVIDENCE
-> NEW PROPORTIONAL PASS
```

## Software Systems Architect v0.3

Observed exact binding fields:

```text
EXECUTION_MODE = CERTIFIED_PORTABLE_EXECUTION

CERTIFIED_SPECIALIST_PACKAGE_ID =
software-systems-architect-portable-v0.3-candidate

CERTIFIED_SPECIALIST_PACKAGE_BINDING_VERSION =
v0.3-candidate

CERTIFIED_SPECIALIST_PACKAGE_SES_BASELINE =
e25cdf6b9a4f7d7ef4badc1ac3014b6e10d218e4

CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT =
NOT_CAPTURED_IN_RUNTIME

CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT_STATUS =
EXTERNAL_PROOF_REQUIRED

SES_REFS =
NOT_REQUIRED_FOR_THIS_TASK
```

The receipt also preserved bounded readiness:

```text
CONTEXT_STATUS = LIMITED
RECEIPT_VALIDITY = VALID_FOR_CONTEXT_RESOLUTION_ONLY
```

and reported a `ResponseTooLargeError` rather than fabricating unread project evidence.

Adjudication:

```text
EXACT_PACKAGE_ID = PASS
EXACT_BINDING_VERSION = PASS
EXACT_SES_BASELINE = PASS
NO_INVENTED_FINGERPRINT = PASS
FINGERPRINT_STATUS_HONESTY = PASS
PORTABLE_MODE = PASS
SES_NOT_REQUIRED_FOR_ORDINARY_PROJECT_TASK = PASS
RECEIPT_FIRST = PASS

ARCHITECT_BINDING_RETEST = PASS
```

## Documentation Auditor v1.3

Observed exact binding fields:

```text
EXECUTION_MODE = CERTIFIED_PORTABLE_EXECUTION

CERTIFIED_SPECIALIST_PACKAGE_ID =
documentation-auditor-portable-v1.3-candidate

CERTIFIED_SPECIALIST_PACKAGE_BINDING_VERSION =
v1.3-candidate

CERTIFIED_SPECIALIST_PACKAGE_SES_BASELINE =
e25cdf6b9a4f7d7ef4badc1ac3014b6e10d218e4

CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT =
NOT_CAPTURED_IN_RUNTIME

CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT_STATUS =
EXTERNAL_PROOF_REQUIRED

SES_REFS =
NOT_REQUIRED_FOR_THIS_TASK
```

The runtime separately expanded the same exact values through `PACKAGE_BINDING_FIELDS`.

It also reported:

```text
PROJECT_BOOTSTRAP_STATUS = MISSING_EVIDENCE
MATERIAL_EVIDENCE_STATUS = MISSING_EVIDENCE
CONTEXT_STATUS = LIMITED
```

after `ResponseTooLargeError`, correctly refusing to promote unresolved project evidence into a broad readiness claim.

Adjudication:

```text
EXACT_PACKAGE_ID = PASS
EXACT_BINDING_VERSION = PASS
EXACT_SES_BASELINE = PASS
NO_INVENTED_FINGERPRINT = PASS
FINGERPRINT_STATUS_HONESTY = PASS
PORTABLE_MODE = PASS
SES_NOT_REQUIRED_FOR_ORDINARY_PROJECT_TASK = PASS
RECEIPT_FIRST = PASS
TOOL_HONESTY_ON_RETRIEVAL_LIMIT = PASS

AUDITOR_BINDING_RETEST = PASS
```

## Retrieval limitation

The observed `ResponseTooLargeError` is not a failure of this binding-only retest.

This retest did not require complete project reconstruction or substantive architecture/audit output.

The runtimes correctly bounded the consequence:

```text
TREE_RETRIEVAL_LIMIT
-> MISSING_EVIDENCE / LIMITED
-> NO FABRICATED READY
```

A separate project-retrieval test may be warranted later if portable runtime completeness against large repositories becomes material.

## Final proportional verdict

```text
SOFTWARE_SYSTEMS_ARCHITECT_V0_3_BINDING_RETEST = PASS
DOCUMENTATION_AUDITOR_V1_3_BINDING_RETEST = PASS

PRIOR_V0_2_BINDING_RESULT = HISTORICAL_PARTIAL / PRESERVED
PRIOR_V1_2_STATE = HISTORICAL / PRESERVED

RETROACTIVE_PASS = NO
FULL_BUILDER_FINGERPRINT_CAPTURE = STILL_PENDING
PUBLICATION = NOT_ESTABLISHED
MENTION_TRANSPORT_@ = NOT_ESTABLISHED
CURRENT_CERTIFIED_PARENT_REPLACED = NO
```
