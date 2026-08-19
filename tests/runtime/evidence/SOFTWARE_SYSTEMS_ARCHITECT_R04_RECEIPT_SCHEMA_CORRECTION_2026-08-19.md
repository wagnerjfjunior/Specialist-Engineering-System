# SES — Software Systems Architect R04 Receipt Schema Correction — 2026-08-19

**Status:** `RUNTIME_CORRECTION_CANDIDATE / R04_RETEST_4_REQUIRED`

Observed history:

```text
R04_RETEST_1 = FAIL / RECEIPT_ORDERING
R04_RETEST_2 = FAIL / RECEIPT_ORDERING
R04_RETEST_3 = FAIL / RECEIPT_INCOMPLETE
RETROACTIVE_PASS = NO
```

R04_RETEST_3 proved ordering but exposed incomplete schema: `PROOF_LEVEL` was blank and multiple required receipt fields were absent while later prose referenced `EFFECTIVE_SCOPE` as if emitted.

Corrective fingerprint:

```text
KERNEL_BLOB = 791dc63165518d16713bbaa2d869c12ac09ec2f7
INSTRUCTIONS_CHARACTERS = 7436
INSTRUCTIONS_UTF8_BYTES = 7478
```

Required fields before substantive project-specific output:

`PROOF_LEVEL`, `TASK_SCOPE`, `EFFECTIVE_SCOPE`, `TARGET_REF_OR_OBJECT`, `ENVIRONMENT`, `SES_CANONICAL_MAIN_REF`, `PROJECT_ID/PROJECT_RESOLUTION`, `PROJECT_LIVE_REF`, `SPECIALIST_RESOLUTION`, `CONTINUITY_STATUS`, `AUTHORITY_STATE`, `MUTATION_AUTHORIZATION`, `EVIDENCE_STATUS`, `CONTEXT_STATUS`, `RECEIPT_VALIDITY`, `GAPS`.

Unavailable values require an explicit unknown/missing status. Blank required fields are prohibited. Incomplete receipt blocks substantive output.

Invalidation is proportional:

```text
R01_RETEST_1 = PRESERVED PASS
R03_RETEST_1 = PRESERVED PASS
R09_RETEST_1 = PRESERVED PASS
R02/R05/R06/R07/R08 = PRESERVED PASS
C10 = PRESERVED PASS
ONLY R04_RETEST_4 REQUIRED AFTER BUILDER REAPPLY
```

`CERTIFIED_FOR_ANY_PROJECT = NO` until the remaining gates close.
