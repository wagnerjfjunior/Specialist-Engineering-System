# SES — Next Safe Action

> Registro autoritativo da próxima ação segura do SES quando este arquivo estiver em `main`.

**Next action ID:** `reapply-and-r04-retest-software-systems-architect`  
**Primary target:** `SES — Software Systems Architect`  
**Current phase:** `SPECIALIST_CERTIFICATION_NORMALIZATION / R04_RECEIPT_ORDERING_CORRECTION`  
**Canonical source:** `wagnerjfjunior/Specialist-Engineering-System` / `main` resolved live

## 1. Current portfolio

```text
UX/UI APP = CERTIFIED_FOR_ANY_PROJECT YES
BACKEND & DATA PLATFORM = YES
APPLICATION SECURITY ASSURANCE = YES
SOFTWARE SYSTEMS ARCHITECT = NO
DOCUMENTATION AUDITOR = NO
```

`CANONICALIZED != CERTIFIED`.

## 2. Preserved evidence

```text
L1-C = PASS
PROMPT INVARIANCE = PASS
GENERIC NON-REGRESSION = PASS
R01_RETEST_1 = PASS
R03_RETEST_1 = PASS
R09_RETEST_1 = PASS
C10 TOOL HONESTY / INTEGRATION = PASS
R04_RETEST_1 = FAIL / RECEIPT_ORDERING
R04_RETEST_2 = FAIL / RECEIPT_ORDERING
RETROACTIVE_PASS = NO
```

Historical SaaS T01-T29 remains 29/29 PASS for its old fingerprint only.

## 3. Current corrected Builder subject

```text
ARCHETYPE_ID = software-systems-architect
KERNEL_BLOB = 1b0e621b52468a2eab170e7b8f4d50659a406f62
INSTRUCTIONS = 7994 Unicode code points / 8036 UTF-8 bytes
PACKAGE = runtime/custom-gpt/SOFTWARE_SYSTEMS_ARCHITECT_BUILDER_PACKAGE_V0_1.md
PROFILE = runtime/custom-gpt/SOFTWARE_SYSTEMS_ARCHITECT_BUILDER_PROFILE_V0_1.md
```

The Builder character limit observed by the operator is 8000; this revision remains below it.

The change is narrowly scoped to enforce:

```text
COMPLETE CONTEXT READINESS RECEIPT FIRST
→ THEN PROJECT-SPECIFIC VERDICT / AS-IS / FINDINGS / RISKS / ANALYSIS / RECOMMENDATIONS / TARGET / CONCLUSION
```

## 4. Sole next material action

1. merge this runtime-correction revision to canonical `main` while certification remains NO;
2. apply the exact current kernel to the existing `SES — Software Systems Architect` Builder;
3. capture a fresh fingerprint proving the update is live;
4. execute **only `R04_RETEST_3`** in a fresh conversation;
5. preserve R01/R03/R09 and R02/R05/R06/R07/R08 PASS unless another material change invalidates them;
6. adjudicate C09;
7. if C09 closes, perform C11 readiness evaluation;
8. only then request/record explicit C12 user authorization for READY for the exact fingerprint;
9. adjudicate C01-C18 and `CERTIFIED_FOR_ANY_PROJECT`.

## 5. Done condition

```text
CURRENT_BUILDER_APPLIED = YES
CURRENT_RUNTIME_FINGERPRINT = CAPTURED
R04_RETEST_3 = PASS
C09 = PASS
C10 = PASS
C11 = PASS
C12 = USER_AUTHORIZED_READY
C18 = PASS
C01-C18 = SATISFIED
CERTIFIED_FOR_ANY_PROJECT = YES
```

## 6. Explicitly blocked

Do not erase or rewrite initial/retest failures, transfer historical SaaS runtime PASS to the current fingerprint, rerun unaffected gates solely for confidence, infer missing project identity, invent tool operation names, mutate consumer projects automatically, or begin Documentation Auditor closure before this specialist is closed unless explicitly reprioritized.

## 7. Universal boundary

```text
CERTIFIED_FOR_ANY_PROJECT != CONSUMER_PROJECT_ADOPTION
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
TOOL_CAPABILITY != AUTHORIZATION
CENTRAL SES EVOLUTION != AUTOMATIC PROJECT MUTATION
AS_IS != TARGET_STATE
GENERATE != AUTHORIZE != PUBLISH
```
