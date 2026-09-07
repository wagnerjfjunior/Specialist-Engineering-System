# SES — Certified Specialist Package Registry v0.1

**Status:** MIGRATION_V0_1 / PACKAGE_BINDING_REGISTRY
**Binding baseline:** `3e5a43ede1cd0977db8af1e45b93032483d97300`
**Certification ledger:** `docs/SPECIALIST_CERTIFICATION_STATUS.md`
**Certification ledger blob:** `616aeadec079cc1e236825a40d13f0f206bae9d8`

## 1. Purpose

Bind the currently certified reusable specialists to exact versioned Builder package/kernel evidence for the portable-execution migration without modifying any certified runtime.

This registry does not certify, recertify, publish, adopt, apply or mutate a GPT.

```text
PACKAGE BINDING
!= PORTABLE RUNTIME PASS
!= PUBLICATION
!= PROJECT ADOPTION
```

Current certified specialists remain valid on their existing execution path unless their exact certified subject changes.

## 2. Migration states

```text
EXACT_BINDING / PORTABLE_RUNTIME_PROOF_PENDING
= current certified subject is bound to exact package/kernel evidence
  and may proceed to portable runtime testing without kernel mutation.

PORTABLE_VNEXT_REQUIRED
= current certification remains valid,
  but portable execution requires a new kernel/package candidate
  because the certified instructions themselves require central SES live bootstrap.
```

No migration state below retroactively changes certification.

## 3. Current bindings

| ARCHETYPE_ID | Certified subject | Kernel blob | Builder package blob | Migration disposition |
|---|---|---|---|---|
| `ux-ui-app-specialist` | `ux-ui-app-specialist-v0.1` | `8e988dceca962f608141cbef663fd4baea4cf86f` | `8cd88c9214be032533bd56ff40ba768bc79be999` | `EXACT_BINDING / PORTABLE_RUNTIME_PROOF_PENDING` |
| `backend-data-platform-specialist` | `backend-data-platform-specialist-v0.1` | `0d3c264cc4367ed8671fb7b07c28de24bf821819` | `b5974bbd9e3d16c89f06e50c9be65abe07aeeb49` | `EXACT_BINDING / PORTABLE_RUNTIME_PROOF_PENDING` |
| `application-security-assurance-specialist` | `application-security-assurance-specialist-v0.1 / compact-v0.2 executable binding` | `bb4a776b8d67f16e89b30961a37c212ef2605c9f` | `98fe84e0c6dfe80be7e39d5ba4b71077ffa33cfc` | `EXACT_BINDING / PORTABLE_RUNTIME_PROOF_PENDING` |
| `seo-strategy-governance-specialist` | `seo-strategy-governance-specialist-v0.1 / kernel-v0.3` | `cdea4c87bcdf86eee44f2774c7cae0423a82528f` | `f4d99304d7b2aa54c2c1bf585d5dc8eaa09385b7` | `EXACT_BINDING / PORTABLE_RUNTIME_PROOF_PENDING` |
| `technical-seo-specialist` | `technical-seo-specialist-v0.1` | `662730906cb73e39e32795c5d04ebd4d4dedac54` | `a411030f82c464a9893f490bacdc26a7e80ff969` | `EXACT_BINDING / PORTABLE_RUNTIME_PROOF_PENDING` |
| `content-semantic-seo-specialist` | `content-semantic-seo-specialist-v0.1` | `e7a4efbba16d909ee75cc47a270d55f1f5608841` | `ccfa57f0ed2655e8c5def5d43c9168d8d884a29c` | `EXACT_BINDING / PORTABLE_RUNTIME_PROOF_PENDING` |
| `seo-analytics-growth-specialist` | `seo-analytics-growth-specialist-v0.1` | `9411adf4badf948690a46242b61ef18d7d602d06` | `1305139d9776359982adfedf817bff14c578c0f4` | `EXACT_BINDING / PORTABLE_RUNTIME_PROOF_PENDING` |
| `paid-search-sem-specialist` | `paid-search-sem-specialist-v0.1` | `098b55d917014e896144d4727010ff296628e529` | `3cecfe6a4d12a5db748f4b861fd0082f75228a35` | `EXACT_BINDING / PORTABLE_RUNTIME_PROOF_PENDING` |
| `lead-operations-crm-specialist` | `lead-operations-crm-specialist-v0.1` | `37a36c1ff1e97c920246db590aa3ebef0e99f040` | `1da3fbd2809fa820bb9dae71a04fa628963b0033` | `EXACT_BINDING / PORTABLE_RUNTIME_PROOF_PENDING` |
| `software-systems-architect` | current certified fingerprint | `791dc63165518d16713bbaa2d869c12ac09ec2f7` | `09289e4df7e4576d06a70908963a329294569b0b` | `PORTABLE_V0_3_BINDING_RETEST_PASS / FULL_BUILDER_FINGERPRINT_PENDING / CURRENT_CERTIFICATION_PRESERVED` |
| `documentation-auditor` | `documentation-auditor-v1.1` | `5bc10297d9e655cf169d2680f914e446232992e0` | `9864de26d8c2c3de154e0e6804309394efd75237` | `PORTABLE_V1_3_BINDING_RETEST_PASS / FULL_BUILDER_FINGERPRINT_PENDING / CURRENT_CERTIFICATION_PRESERVED` |

## 4. Exact paths

```text
ux-ui-app-specialist
  kernel: runtime/custom-gpt/UX_UI_APP_SPECIALIST_BUILDER_KERNEL_V0_1.md
  package: runtime/custom-gpt/UX_UI_APP_SPECIALIST_BUILDER_PACKAGE_V0_1.md

backend-data-platform-specialist
  kernel: runtime/custom-gpt/BACKEND_DATA_PLATFORM_SPECIALIST_BUILDER_KERNEL_V0_1.md
  package: runtime/custom-gpt/BACKEND_DATA_PLATFORM_SPECIALIST_BUILDER_PACKAGE_V0_1.md

application-security-assurance-specialist
  kernel: runtime/custom-gpt/APPLICATION_SECURITY_ASSURANCE_SPECIALIST_BUILDER_KERNEL_COMPACT_V0_2.md
  package: runtime/custom-gpt/APPLICATION_SECURITY_ASSURANCE_SPECIALIST_BUILDER_PACKAGE_V0_2.md

software-systems-architect
  kernel: runtime/custom-gpt/SOFTWARE_SYSTEMS_ARCHITECT_BUILDER_KERNEL_V0_1.md
  package: runtime/custom-gpt/SOFTWARE_SYSTEMS_ARCHITECT_BUILDER_PACKAGE_V0_1.md

documentation-auditor
  kernel: runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_KERNEL_V1_1.md
  package: runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_PACKAGE_V1_1.md

seo-strategy-governance-specialist
  kernel: runtime/custom-gpt/SEO_STRATEGY_GOVERNANCE_SPECIALIST_BUILDER_KERNEL_V0_3.md
  package: runtime/custom-gpt/SEO_STRATEGY_GOVERNANCE_SPECIALIST_BUILDER_PACKAGE_V0_3.md

technical-seo-specialist
  kernel: runtime/custom-gpt/TECHNICAL_SEO_SPECIALIST_BUILDER_KERNEL_V0_1.md
  package: runtime/custom-gpt/TECHNICAL_SEO_SPECIALIST_BUILDER_PACKAGE_V0_1.md

content-semantic-seo-specialist
  kernel: runtime/custom-gpt/CONTENT_SEMANTIC_SEO_SPECIALIST_BUILDER_KERNEL_V0_1.md
  package: runtime/custom-gpt/CONTENT_SEMANTIC_SEO_SPECIALIST_BUILDER_PACKAGE_V0_1.md

seo-analytics-growth-specialist
  kernel: runtime/custom-gpt/SEO_ANALYTICS_GROWTH_SPECIALIST_BUILDER_KERNEL_V0_1.md
  package: runtime/custom-gpt/SEO_ANALYTICS_GROWTH_SPECIALIST_BUILDER_PACKAGE_V0_1.md

paid-search-sem-specialist
  kernel: runtime/custom-gpt/PAID_SEARCH_SEM_SPECIALIST_BUILDER_KERNEL_V0_1.md
  package: runtime/custom-gpt/PAID_SEARCH_SEM_SPECIALIST_BUILDER_PACKAGE_V0_1.md

lead-operations-crm-specialist
  kernel: runtime/custom-gpt/LEAD_OPERATIONS_CRM_SPECIALIST_BUILDER_KERNEL_V0_1.md
  package: runtime/custom-gpt/LEAD_OPERATIONS_CRM_SPECIALIST_BUILDER_PACKAGE_V0_1.md
```

## 5. vNext-required evidence

### Software Systems Architect

The exact certified kernel contains an explicit central bootstrap sequence including:

- resolve SES `main` live;
- read SES bootstrap and Archetype Registry;
- read Hybrid Specialist Bootstrap;
- resolve SES Project Registry and Project Adapter.

Therefore removing central SES runtime dependency changes the certified instructions.

```text
CURRENT CERTIFICATION = PRESERVED
PORTABLE CURRENT-FINGERPRINT CLAIM = NOT MADE
PORTABLE VNEXT = REQUIRED
FULL RECERTIFICATION = NOT AUTOMATIC
AFFECTED-GATE REVALIDATION = REQUIRED AFTER MATERIAL DELTA
```

### Documentation Auditor

The exact certified v1.1 kernel likewise explicitly requires SES `main` live, SES bootstrap, Archetype Registry and Project Adapter resolution.

The same migration rule applies:

```text
CURRENT CERTIFICATION = PRESERVED
PORTABLE CURRENT-FINGERPRINT CLAIM = NOT MADE
PORTABLE VNEXT = REQUIRED
FULL RECERTIFICATION = NOT AUTOMATIC
AFFECTED-GATE REVALIDATION = REQUIRED AFTER MATERIAL DELTA
```

## 6. Nine no-kernel-mutation candidates

For the other nine bindings above, this migration review did not identify the explicit central SES bootstrap sequence that makes the two vNext cases non-portable.

This is sufficient only to admit those exact bindings into the dedicated portable runtime suite.

It is not portable runtime proof.

```text
EXACT BINDING
-> RUN PORTABLE TESTS
-> PORTABLE PASS ONLY IF RUNTIME EVIDENCE PASSES

ABSENCE OF CURRENT BLOCKER
!= RUNTIME PASS
```

## 7. Publication boundary

No binding in this registry is automatically public.

```text
CERTIFIED_FOR_ANY_PROJECT
+ EXACT PACKAGE BINDING
+ PORTABLE RUNTIME PROOF
!= PUBLICATION AUTHORIZATION
```

Public/private GPT publication is a separate distribution decision.

## 8. Current migration summary

```text
CURRENT CERTIFIED SPECIALISTS: 11
EXACT_BINDING / PORTABLE_RUNTIME_PROOF_PENDING: 9
PORTABLE_BINDING_FIX_CANDIDATE_VERSIONED / BUILDER_NOT_APPLIED: 2

CURRENT SPECIALIST CERTIFICATION INVALIDATED: 0
CURRENT GPT MUTATIONS: 0
CONSUMER PROJECT MUTATIONS: 0
```


## 9. Parallel vNext candidates

```text
software-systems-architect
  candidate kernel:
  runtime/custom-gpt/SOFTWARE_SYSTEMS_ARCHITECT_BUILDER_KERNEL_V0_2_PORTABLE_CANDIDATE.md
  kernel blob: 1b5195362a10f5732dc2f81335c035dc29c46b40
  candidate package:
  runtime/custom-gpt/SOFTWARE_SYSTEMS_ARCHITECT_BUILDER_PACKAGE_V0_2_PORTABLE_CANDIDATE.md

documentation-auditor
  candidate kernel:
  runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_KERNEL_V1_2_PORTABLE_CANDIDATE.md
  kernel blob: 98c6df641e1ffaf6650f4d3075f31e2aba602dc4
  candidate package:
  runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_PACKAGE_V1_2_PORTABLE_CANDIDATE.md
```

Both are repository candidates only. Neither has been applied to the current certified GPT.


## 10. Builder UI evidence update

Product Authority supplied Builder screenshots for both portable vNext candidates.

For each candidate, the visible editor positively matches the expected candidate identity and leading portable-bootstrap semantics.

Current bounded state:

```text
BUILDER_UI_CANDIDATE_PRESENT = YES
VISIBLE_INSTRUCTIONS_IDENTITY = MATCH
VISIBLE_PORTABLE_BOOTSTRAP = MATCH
FULL_INSTRUCTIONS_MATCH = NOT_DETERMINED
MODEL / CAPABILITIES / KNOWLEDGE / ACTIONS = NOT_CAPTURED
PORTABLE_RUNTIME_PROOF = NOT_EXECUTED
PUBLIC_VISIBILITY = NO EVIDENCE; UI SHOWS "APENAS PARA MIM"
```

No current certified parent fingerprint is invalidated by this evidence update.


## 11. Binding-fix candidate supersession

Runtime evidence from Software Systems Architect portable v0.2 exposed a package-binding receipt overclaim. That candidate remains historical.

```text
software-systems-architect
  historical portable candidate:
  v0.2 / kernel blob 1b5195362a10f5732dc2f81335c035dc29c46b40
  A1 binding result: PARTIAL / INITIAL_BINDING_OVERCLAIM

  current binding-fix candidate:
  runtime/custom-gpt/SOFTWARE_SYSTEMS_ARCHITECT_BUILDER_KERNEL_V0_3_PORTABLE_CANDIDATE.md
  kernel blob: d62f8cf750b7965b602ac335050c7c88a5732b5f
  package:
  runtime/custom-gpt/SOFTWARE_SYSTEMS_ARCHITECT_BUILDER_PACKAGE_V0_3_PORTABLE_CANDIDATE.md

documentation-auditor
  historical portable candidate:
  v1.2 / kernel blob 98c6df641e1ffaf6650f4d3075f31e2aba602dc4

  current binding-fix candidate:
  runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_KERNEL_V1_3_PORTABLE_CANDIDATE.md
  kernel blob: 9cfc485c6c69f9724d55d3bcc77509be4dd74492
  package:
  runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_PACKAGE_V1_3_PORTABLE_CANDIDATE.md

SES_BASELINE_REF for both binding-fix candidates:
e25cdf6b9a4f7d7ef4badc1ac3014b6e10d218e4
```

Neither v0.3 nor v1.3 has been applied to Builder at registry-update time.

Only the binding/receipt obligation is invalidated by this correction unless another material Builder/runtime delta is introduced.

```text
USER_CORRECTED / INITIAL_BINDING_OVERCLAIM
!= RETROACTIVE_PASS
```


## 12. Binding retest closure — 2026-09-07

User-supplied runtime receipts for the current binding-fix candidates matched the exact package constants and correctly reported the cryptographic fingerprint as externally provable rather than self-declared.

```text
software-systems-architect portable v0.3
  BINDING_RETEST = PASS
  FULL_BUILDER_FINGERPRINT = PENDING

documentation-auditor portable v1.3
  BINDING_RETEST = PASS
  FULL_BUILDER_FINGERPRINT = PENDING
```

The prior Software Systems Architect v0.2 binding overclaim remains historical and is not rewritten.

The observed repository `ResponseTooLargeError` was bounded to `LIMITED / MISSING_EVIDENCE` and did not produce a false READY claim.

Remaining independent gates:

```text
FULL BUILDER / CONFIGURATION FINGERPRINT CAPTURE
PORTABLE RUNTIME COMPLETENESS FOR ANY STILL-UNEXECUTED REQUIRED CASES
PUBLICATION AUTHORIZATION / VISIBILITY
MENTION (@) TRANSPORT PROOF
```
