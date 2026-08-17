# SES — Application Security Assurance Specialist L2 Runtime Profile v0.1

**Candidate ID:** `application-security-assurance-specialist-v0.1`  
**Prerequisite:** `APPSEC_L1C_RESULT = PASS`  
**Builder package:** `runtime/custom-gpt/APPLICATION_SECURITY_ASSURANCE_SPECIALIST_BUILDER_PACKAGE_V0_1.md`  
**Builder kernel:** `runtime/custom-gpt/APPLICATION_SECURITY_ASSURANCE_SPECIALIST_BUILDER_KERNEL_V0_1.md`  
**Builder kernel blob SHA:** `6c44ce208425402aa4a89adfc5cd4e4ed8571ed3`  
**Status:** `L2_RUNTIME_CANDIDATE / BUILDER_PACKAGE_VERSIONED / NOT_APPLIED / NOT_EXECUTED`

## 1. Purpose

L2 validates the actual configured specialist runtime under an exact fingerprint. It is not another prompt-only L1 exercise.

```text
L1 PASS != L2 PASS
PACKAGE VERSIONED != BUILDER APPLIED
BUILDER APPLIED != RUNTIME VALIDATED
```

## 2. Runtime target

Target runtime identity:
`SES — Application Security Assurance Specialist`

The runtime must preserve material L1 semantics including:
- independent-assurance vs implementation separation;
- explicit active-test authorization boundary;
- hostile-client posture;
- server/data authorization reasoning;
- cross-user/cross-tenant discovery;
- Supabase semantic security profile;
- secrets/client-storage discipline;
- injection and adjacent-risk discovery;
- CVE applicability and current-primary-source freshness discipline;
- bounded findings/severity;
- unsupported-PASS resistance;
- independent retest;
- architecture non-dogmatism;
- production safety;
- tool honesty;
- prompt invariance;
- project isolation and handoffs.

The exact Builder field configuration comes from the package; the exact Instructions payload comes from the Builder kernel. Do not synthesize a different runtime prompt during application.

## 3. v0.1 integration surface

```text
GITHUB = TARGET_ENABLED / READ_ONLY / NOT_APPLIED
WEB_SEARCH = TARGET_ENABLED IF EXPOSED
DATA_ANALYSIS = TARGET_ENABLED IF EXPOSED
VERCEL = OPTIONAL_DISABLED / NOT_CONFIGURED
SUPABASE = OPTIONAL_DISABLED / NOT_CONFIGURED
KNOWLEDGE = EMPTY
```

GitHub uses:
`runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`

Schema blob:
`1e6237e806fd84716ec13b019e6617ad4110a211`

Supabase being a tested security domain does not imply direct Supabase connection in this fingerprint.

## 4. L2 fingerprint fields

Capture before execution:

```text
RUNTIME_ID
BUILDER/GPT_ID_OR_URL
RUNTIME_NAME
BUILDER_PACKAGE_REF/SHA
PROFILE_VERSION
PROFILE_BLOB_SHA
BUILDER_KERNEL_ID
BUILDER_KERNEL_BLOB_SHA
INSTRUCTIONS_MEASURED_CHARACTER_COUNT
INSTRUCTIONS_COUNT_METHOD
INSTRUCTIONS_COMPLETE_COPY
BUILDER_ACCEPTED_WITHOUT_TRUNCATION
INSTRUCTION_BLOB_SHA_OR_EXACT_EXPORT
CONVERSATION_STARTERS
KNOWLEDGE_FILE_LIST
KNOWLEDGE_FILE_HASHES
WEB_SEARCH
DATA_ANALYSIS
IMAGE_GENERATION
ACTIONS/TOOLS_ENABLED
ACTION/TOOL_CONFIG_VERSION
GITHUB_ACTION_SCHEMA_REF/HASH
VERCEL_STATE
SUPABASE_STATE
MODEL
MODEL_MODE/SETTINGS
CAPABILITIES
VISIBILITY
DATE/TIME
EXECUTION_ID
```

Unexposed product fields = `NOT EXPOSED`. The four instruction-fit fields are mandatory and cannot be waived.

## 5. Required configuration boundary

The runtime must not silently inherit:
- FECH.AI-specific rules;
- Blogs/SEO-specific rules;
- consumer-project business rules;
- project secrets/data;
- hidden test answer keys or adjudication rubrics;
- Backend/Data implementation authority;
- risk acceptance/release authority.

## 6. Tool/action discipline

```text
TOOL AVAILABLE != TOOL INVOKED != RESULT VERIFIED
TOOL CAPABILITY != AUTHORIZATION
```

L2 must include runtime-specific challenges for:
- read-only GitHub evidence when Action is configured;
- current advisory/freshness verification using web capability when available;
- explicit non-execution claims when tools are unavailable or not invoked.

Any fabricated tool/advisory/repository execution is an immediate hard blocker.

## 7. Runtime proof scope

Supported if passed:
`L2_RUNTIME_FINGERPRINT_VALIDATION = PASS`

Not automatically established:

```text
SPECIALIST_READINESS = AUTHORIZED
ARCHETYPE ACTIVE
CONSUMER ADOPTION
PUBLICATION
PRODUCTION SECURITY CERTIFICATION
RISK ACCEPTANCE
```

## 8. Invalidation

Material change to instructions, Knowledge, model, actions/tools, permissions, integration set, system/runtime settings or relevant product capability invalidates only affected L2 claims and requires proportional retest.
