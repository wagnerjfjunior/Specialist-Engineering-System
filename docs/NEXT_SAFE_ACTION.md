# SES — Next Safe Action

> Registro autoritativo da próxima ação segura do SES quando este arquivo estiver em `main`.

**Next action ID:** `reapply-and-r04-retest4-software-systems-architect`  
**Primary target:** `SES — Software Systems Architect`  
**Current phase:** `SPECIALIST_CERTIFICATION_NORMALIZATION / R04_RECEIPT_SCHEMA_CORRECTION`

## Current portfolio

```text
UX/UI APP = CERTIFIED_FOR_ANY_PROJECT YES
BACKEND & DATA PLATFORM = YES
APPLICATION SECURITY ASSURANCE = YES
SOFTWARE SYSTEMS ARCHITECT = NO
DOCUMENTATION AUDITOR = NO
```

## Preserved evidence

```text
L1-C = PASS
R01_RETEST_1 = PASS
R03_RETEST_1 = PASS
R09_RETEST_1 = PASS
C10 = PASS
R04_RETEST_1 = FAIL / RECEIPT_ORDERING
R04_RETEST_2 = FAIL / RECEIPT_ORDERING
R04_RETEST_3 = FAIL / RECEIPT_INCOMPLETE
RETROACTIVE_PASS = NO
```

## Current corrected Builder subject

```text
ARCHETYPE_ID = software-systems-architect
KERNEL_BLOB = 791dc63165518d16713bbaa2d869c12ac09ec2f7
INSTRUCTIONS = 7436 Unicode code points / 7478 UTF-8 bytes
PACKAGE = runtime/custom-gpt/SOFTWARE_SYSTEMS_ARCHITECT_BUILDER_PACKAGE_V0_1.md
PROFILE = runtime/custom-gpt/SOFTWARE_SYSTEMS_ARCHITECT_BUILDER_PROFILE_V0_1.md
```

Required project-specific receipt fields are explicit and nonblank; unavailable values must use an explicit unknown/missing status. An incomplete receipt blocks substantive output.

## Sole next material action

1. merge this receipt-schema correction while certification remains NO;
2. apply the exact current kernel in Builder;
3. capture fresh post-update fingerprint evidence;
4. execute **only `R04_RETEST_4`** in a fresh conversation;
5. preserve all unaffected PASS evidence unless another material change invalidates it;
6. adjudicate C09;
7. if C09 PASS, perform C11 readiness evaluation;
8. then require explicit C12 user authorization for READY for the exact fingerprint;
9. adjudicate C01-C18 and `CERTIFIED_FOR_ANY_PROJECT`.

## Done condition

```text
CURRENT_BUILDER_APPLIED = YES
CURRENT_RUNTIME_FINGERPRINT = CAPTURED
R04_RETEST_4 = PASS
C09 = PASS
C10 = PASS
C11 = PASS
C12 = USER_AUTHORIZED_READY
C18 = PASS
CERTIFIED_FOR_ANY_PROJECT = YES
```

Do not erase failures, transfer historical SaaS PASS, rerun unaffected gates solely for confidence, infer missing project identity, invent tool operation names, or mutate consumer projects automatically.
