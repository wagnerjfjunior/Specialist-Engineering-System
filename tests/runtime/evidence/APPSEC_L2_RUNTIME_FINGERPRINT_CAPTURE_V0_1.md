# AppSec L2 Runtime Fingerprint Capture v0.1

**Specialist:** SES — Application Security Assurance Specialist  
**Candidate:** `application-security-assurance-specialist-v0.1`  
**L1-C:** `PASS`  
**Builder package:** `runtime/custom-gpt/APPLICATION_SECURITY_ASSURANCE_SPECIALIST_BUILDER_PACKAGE_V0_1.md`  
**Builder kernel:** `runtime/custom-gpt/APPLICATION_SECURITY_ASSURANCE_SPECIALIST_BUILDER_KERNEL_V0_1.md`  
**Builder kernel blob SHA:** `6c44ce208425402aa4a89adfc5cd4e4ed8571ed3`  
**Status:** `PRE_APPLICATION / FINGERPRINT_NOT_CAPTURED / L2_NOT_EXECUTED`

## 1. Builder application fingerprint

Fill only from actual Builder/runtime evidence. Do not infer unavailable fields.

```text
RUNTIME_ID =
BUILDER/GPT_ID_OR_URL =
RUNTIME_NAME =
BUILDER_PACKAGE_REF/SHA =
PROFILE_REF/SHA =
BUILDER_KERNEL_ID = application-security-assurance-specialist-builder-kernel-v0.1
BUILDER_KERNEL_BLOB_SHA = 6c44ce208425402aa4a89adfc5cd4e4ed8571ed3
INSTRUCTIONS_MEASURED_CHARACTER_COUNT =
INSTRUCTIONS_COUNT_METHOD =
INSTRUCTIONS_COMPLETE_COPY =
BUILDER_ACCEPTED_WITHOUT_TRUNCATION =
INSTRUCTION_BLOB_SHA_OR_EXACT_EXPORT =
CONVERSATION_STARTERS =
KNOWLEDGE_FILE_LIST = EMPTY target
KNOWLEDGE_FILE_HASHES = NOT_APPLICABLE if empty
WEB_SEARCH =
DATA_ANALYSIS =
IMAGE_GENERATION =
ACTIONS/TOOLS_ENABLED =
ACTION/TOOL_CONFIG_VERSION =
GITHUB_ACTION_STATE =
GITHUB_ACTION_SCHEMA_REF/HASH = 1e6237e806fd84716ec13b019e6617ad4110a211 if applied
VERCEL_STATE = DISABLED target
SUPABASE_STATE = DISABLED target
MODEL =
MODEL_MODE/SETTINGS =
CAPABILITIES =
VISIBILITY = PRIVATE / APENAS PARA MIM target
DATE/TIME =
EXECUTION_ID =
```

## 2. Mandatory instruction-fit gate

L2 execution is blocked unless all are established:

```text
INSTRUCTIONS_MEASURED_CHARACTER_COUNT = numeric value
INSTRUCTIONS_COUNT_METHOD = explicit reproducible method
INSTRUCTIONS_COMPLETE_COPY = YES
BUILDER_ACCEPTED_WITHOUT_TRUNCATION = YES
```

`NOT EXPOSED` is not accepted for these four fields.

## 3. Configuration drift check

Before R01 and before final adjudication verify:

```text
KERNEL_CHANGED = NO
KNOWLEDGE_CHANGED = NO
MODEL/SETTINGS_CHANGED = NO or recorded material change
TOOLS/ACTIONS_CHANGED = NO
GITHUB_SCHEMA_CHANGED = NO
VERCEL_ENABLED = NO
SUPABASE_ENABLED = NO
VISIBILITY_BROADENED = NO
```

Any material change requires re-fingerprinting and proportional retest.

## 4. Runtime execution ledger

| Fixture | Fresh context | First output captured | Tools/result captured | Result |
|---|---|---|---|---|
| R01 unauthorized production attack | PENDING | PENDING | PENDING | NOT_EXECUTED |
| R02 hostile browser + cross-tenant | PENDING | PENDING | PENDING | NOT_EXECUTED |
| R03 Supabase semantic security | PENDING | PENDING | PENDING | NOT_EXECUTED |
| R04 CVE freshness/current-source | PENDING | PENDING | PENDING | NOT_EXECUTED |
| R05 finding closure/retest | PENDING | PENDING | PENDING | NOT_EXECUTED |
| R06 GitHub read-only runtime challenge | PENDING | PENDING | PENDING | NOT_EXECUTED |
| R07A prompt invariance | PENDING | PENDING | PENDING | NOT_EXECUTED |
| R07B prompt invariance | PENDING | PENDING | PENDING | NOT_EXECUTED |
| R08 SQLi + adjacent SSRF | PENDING | PENDING | PENDING | NOT_EXECUTED |

## 5. Proof boundary

```text
BUILDER_PACKAGE_VERSIONED = YES
BUILDER_KERNEL_VERSIONED = YES
L1_C_PASS = YES
BUILDER_APPLIED = NOT_ESTABLISHED
FINGERPRINT_CAPTURED = NO
L2_RUNTIME_FINGERPRINT_VALIDATION = NOT_ESTABLISHED
ARCHETYPE_ACTIVE = NO / NOT ESTABLISHED BY THIS ARTIFACT
PUBLICATION = NOT AUTHORIZED BY THIS ARTIFACT
```
