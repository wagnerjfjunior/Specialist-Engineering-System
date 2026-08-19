# SES — Software Systems Architect Custom GPT Builder Profile v0.1

**Status:** `BUILDER_FIT / RUNTIME_CORRECTION_CANDIDATE / REAPPLY_REQUIRED / L1C_PASS / L2_R04_OPEN`  
**ARCHETYPE_ID:** `software-systems-architect`

## Purpose

Version the intended Builder configuration while preserving historical SaaS evidence and all current L2 failures on their original fingerprints.

`PROFILE_VERSIONED != BUILDER_APPLIED != RUNTIME_FINGERPRINT != RUNTIME_PROOF`

## Builder fields

**Name:** `SES — Software Systems Architect`

**Description:**

`Arquiteto de sistemas de software do SES. Audita AS-IS, domínios, dependências, trust boundaries, multi-tenancy, dados, eventos, concorrência, confiabilidade e observabilidade; define target architecture, migração, rollback e proof obligations com evidência e isolamento entre projetos.`

Measured: `286 Unicode code points / 292 UTF-8 bytes`.

**Instructions exact source:** `runtime/custom-gpt/SOFTWARE_SYSTEMS_ARCHITECT_BUILDER_KERNEL_V0_1.md`

```text
EXPECTED_KERNEL_BLOB = 791dc63165518d16713bbaa2d869c12ac09ec2f7
INSTRUCTIONS_UNICODE_CODE_POINTS = 7436
INSTRUCTIONS_UTF8_BYTES = 7478
OPERATOR_OBSERVED_UI_LIMIT = 8000 characters / 2026-08-19
```

**Conversation starters:** same four exact starters versioned in the Builder package.

```text
KNOWLEDGE = EMPTY
Web Search = ENABLED
Code Interpreter / Data Analysis = ENABLED
Image Generation = DISABLED
Actions = ENABLED
ACTION = SES GitHub READ_ONLY
EXPECTED_ACTION_SCHEMA_BLOB = 1e6237e806fd84716ec13b019e6617ad4110a211
VISIBILITY = PRIVATE / APENAS PARA MIM
```

## Runtime behavior corrections bound to this fingerprint

```text
MISSING PROJECT ID → ASK DIRECTLY → STOP
TOOL OPERATION NAME NOT OBSERVABLE → TOOL_OPERATION=NOT_CAPTURED
PROJECT-SPECIFIC WORK → COMPLETE CONTEXT READINESS RECEIPT FIRST
REQUIRED RECEIPT FIELDS → EXPLICIT NONBLANK VALUE OR EXPLICIT UNKNOWN/MISSING STATUS
INCOMPLETE RECEIPT → NO SUBSTANTIVE WORK
```

Required receipt fields:
`PROOF_LEVEL`, `TASK_SCOPE`, `EFFECTIVE_SCOPE`, `TARGET_REF_OR_OBJECT`, `ENVIRONMENT`, `SES_CANONICAL_MAIN_REF`, `PROJECT_ID/PROJECT_RESOLUTION`, `PROJECT_LIVE_REF`, `SPECIALIST_RESOLUTION`, `CONTINUITY_STATUS`, `AUTHORITY_STATE`, `MUTATION_AUTHORIZATION`, `EVIDENCE_STATUS`, `CONTEXT_STATUS`, `RECEIPT_VALIDITY`, `GAPS`.

## Reconciliation gate

```text
RUNTIME_NAME = SES — Software Systems Architect
ARCHETYPE_ID = software-systems-architect
DESCRIPTION_COMPLETE_COPY = YES
DESCRIPTION_CHARACTER_COUNT = 286
INSTRUCTIONS_COMPLETE_COPY = YES
KERNEL_BLOB = 791dc63165518d16713bbaa2d869c12ac09ec2f7
INSTRUCTIONS_CHARACTER_COUNT = 7436
INSTRUCTIONS_UTF8_BYTES = 7478
CONVERSATION_STARTERS = exactly 4
KNOWLEDGE = EMPTY
ACTION_SURFACE = READ_ONLY / GET-only
MODEL = actual
APPS = actual / NOT EXPOSED
VISIBILITY = PRIVATE / APENAS PARA MIM
```

## Current lifecycle

```text
L1-C = PASS
R01_RETEST_1 = PASS
R03_RETEST_1 = PASS
R09_RETEST_1 = PASS
R04_RETEST_1 = FAIL / PRESERVED
R04_RETEST_2 = FAIL / PRESERVED
R04_RETEST_3 = FAIL / RECEIPT_INCOMPLETE / PRESERVED
CURRENT_BUILDER_APPLIED = STALE_REVALIDATION_REQUIRED
CURRENT_RUNTIME_FINGERPRINT = STALE_REVALIDATION_REQUIRED
C09 = NOT_SATISFIED
C10 = PASS / PRESERVED
C11 = NOT_ELIGIBLE
C12 = NOT_APPLICABLE_YET
CERTIFIED_FOR_ANY_PROJECT = NO
```

After reapply, capture a fresh fingerprint and retest only `R04_RETEST_4` unless another material configuration change invalidates more evidence.
