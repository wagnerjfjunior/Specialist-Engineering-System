# SES — Software Systems Architect Builder Fingerprint — 2026-08-19

**Certification subject:** `software-systems-architect / builder-fit-v0.1`
**Evidence class:** `EXTERNAL_BUILDER_CONFIGURATION / OPERATOR_SCREENSHOTS + SUPPLIED_SCHEMA_TEXT`
**Runtime proof:** `NOT_YET_EXECUTED`

## 1. Evidence boundary

This record is based on operator-supplied screenshots of the actual Custom GPT Builder and supplied text for the configured GitHub Action schema/kernel display. It records only fields visibly established by that evidence. Missing/non-visible fields remain `NOT_CAPTURED`.

`BUILDER_APPLIED != L2_RUNTIME_PASS`
`FINGERPRINT_CAPTURED != TOOL_INVOCATION_PROOF`

## 2. Captured identity/configuration

```text
RUNTIME_NAME = SES — Software Systems Architect
ARCHETYPE_ID = software-systems-architect
VISIBILITY = PRIVATE / APENAS PARA MIM
MODEL = GPT-5.6 Sol (gpt-5-6) / recommended model shown
DESCRIPTION_COMPLETE_COPY = YES / visually consistent with versioned 286-character Builder-fit description
DESCRIPTION_CHARACTER_COUNT = 286 / versioned source count
INSTRUCTIONS_COMPLETE_COPY = YES / beginning and ending of exact compact kernel visibly captured; supplied complete text matches versioned kernel
KERNEL_PATH = runtime/custom-gpt/SOFTWARE_SYSTEMS_ARCHITECT_BUILDER_KERNEL_V0_1.md
KERNEL_BLOB_SHA = 5aa37be41e83e7f3c83019a5b29e1a8583364d2f
INSTRUCTIONS_CHARACTER_COUNT = 7710 / versioned source count
INSTRUCTIONS_UTF8_BYTES = 7752 / versioned source count
CONVERSATION_STARTERS = 4 / visually captured
KNOWLEDGE = EMPTY / no uploaded files visible
WEB_SEARCH = ENABLED
IMAGE_GENERATION = DISABLED
DATA_ANALYSIS / CODE_INTERPRETER = ENABLED
CUSTOM_ACTION_HOST = api.github.com
CUSTOM_ACTION_TITLE = SES GitHub READ_ONLY
ACTION_AUTH_TYPE = API KEY
ACTION_AUTH_MODE = BEARER
ACTION_SECRET = PRESENT BUT HIDDEN / NOT RECORDED
ACTION_METHOD_SURFACE = GET-only in supplied schema
ACTION_SCHEMA_PATH = runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml
ACTION_SCHEMA_EXPECTED_BLOB = 1e6237e806fd84716ec13b019e6617ad4110a211
APPS = NOT_CAPTURED
BUILDER/GPT_FULL_ID = NOT_CAPTURED
MODEL_SETTINGS_BEYOND_RECOMMENDED_MODEL = NOT_CAPTURED
```

The Builder UI shows the GPT as live/private and an `Atualizar` control. This record does not infer publication beyond `APENAS PARA MIM`.

## 3. Action evidence

The supplied Action schema is OpenAPI `3.1.0`, title `SES GitHub READ_ONLY`, version `0.2.1`, server `https://api.github.com`, and exposes GET operations only, including `/user`, repository metadata/branches/files/blobs/commits/PR read operations, checks/workflows and compare. No mutation endpoint is present in the supplied schema text.

This establishes configured read-only action surface at the configuration-evidence level. It does **not** establish successful authentication, repository access or tool correctness in runtime. Those remain C10/L2 proof obligations.

## 4. Builder application adjudication

The screenshots show the current Builder-fit package fields applied without the previously observed Description/Instructions fit blocker.

```text
C07 ACTUAL BUILDER APPLIED = PASS
C08 RUNTIME FINGERPRINT CAPTURED = PASS / SUFFICIENT FOR L2 ENTRY
C09 L2 RUNTIME PASS = NOT_ESTABLISHED
C10 TOOL HONESTY / INTEGRATION PROOF = NOT_ESTABLISHED
```

`C08 PASS` means the current configuration is sufficiently fingerprinted to define the runtime test subject. It does not mean every non-material UI field was captured.

## 5. Next gate

Execute `tests/runtime/SOFTWARE_SYSTEMS_ARCHITECT_L2_CURRENT_FINGERPRINT_RUNBOOK_V0_1.md` against this exact configured GPT. Any material Builder change before/during L2 invalidates affected runtime evidence and requires fingerprint reconciliation.
