# SES — UX/UI APP Specialist L2 Runtime Profile v0.1

**Candidate ID:** `ux-ui-app-specialist-v0.1`  
**Prerequisite:** `CANONICAL_L1-C = PASS`  
**Builder package:** `runtime/custom-gpt/UX_UI_APP_SPECIALIST_BUILDER_PACKAGE_V0_1.md`  
**Builder kernel:** `runtime/custom-gpt/UX_UI_APP_SPECIALIST_BUILDER_KERNEL_V0_1.md`  
**Builder kernel blob SHA:** `8e988dceca962f608141cbef663fd4baea4cf86f`  
**Status:** `L2_RUNTIME_CANDIDATE / BUILDER_PACKAGE_VERSIONED / NOT_APPLIED / NOT_EXECUTED`

## 1. Purpose

L2 validates the actual configured specialist runtime under an exact fingerprint. It is not another prompt-only behavioral exercise.

```text
L1 PASS != L2 PASS
PACKAGE VERSIONED != BUILDER APPLIED
BUILDER APPLIED != RUNTIME VALIDATED
```

## 2. Runtime target

Target runtime identity:

`SES — UX/UI APP Specialist`

Target behavior must preserve the L1-validated Candidate/kernel semantics, including:
- evidence and assumption discipline;
- UX/product-experience depth beyond visual styling;
- research/greenfield/hybrid boundaries;
- state/recovery coverage;
- accessibility and responsive/mobile proof discipline;
- security, architecture, backend/data, privacy/compliance and project-local authority handoffs;
- tool-execution honesty;
- prompt invariance;
- non-regression against a competent generic baseline.

The exact Builder field configuration comes from the Builder package. The exact Instructions payload comes from the Builder kernel. Do not synthesize a different runtime prompt during application.

## 3. v0.1 integration surface

Target package configuration:

```text
GITHUB = TARGET_ENABLED / READ_ONLY / NOT_APPLIED
VERCEL = OPTIONAL_DISABLED / NOT_CONFIGURED
SUPABASE = OPTIONAL_DISABLED / NOT_CONFIGURED
KNOWLEDGE = EMPTY
```

GitHub uses the existing SES read-only Action schema when actually configured:

`runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`

Schema blob at package-design time:

`1e6237e806fd84716ec13b019e6617ad4110a211`

Vercel and Supabase are explicitly outside the v0.1 L2 fingerprint unless a future versioned package changes that decision. Their mere availability must not be treated as connected capability.

## 4. L2 fingerprint fields

Before execution, capture exactly:

```text
RUNTIME_ID
BUILDER/GPT_ID_OR_URL
RUNTIME_NAME
BUILDER_PACKAGE_REF/SHA
PROFILE_VERSION
PROFILE_BLOB_SHA
BUILDER_KERNEL_ID
BUILDER_KERNEL_BLOB_SHA
INSTRUCTION_BLOB_SHA_OR_EXACT_EXPORT
KNOWLEDGE_FILE_LIST
KNOWLEDGE_FILE_HASHES
ACTIONS/TOOLS_ENABLED
ACTION/TOOL_CONFIG_VERSION
GITHUB_ACTION_SCHEMA_REF/HASH
VERCEL_STATE
SUPABASE_STATE
MODEL
MODEL_MODE/SETTINGS
CAPABILITIES
CONVERSATION_START_MODE
DATE/TIME
EXECUTION_ID
```

If a field cannot be obtained from the product UI/API, record `NOT EXPOSED`, not an invented value.

## 5. Required configuration boundary

The runtime must not silently inherit:
- FECH.AI-specific rules;
- Blogs/SEO-specific rules;
- Supabase-specific implementation requirements;
- project-local business rules;
- hidden test answer keys or adjudication rubrics.

Consumer-project knowledge may be added only under a separately versioned adoption/configuration event.

## 6. Tools/actions

Tool availability does not prove execution.

```text
TOOL AVAILABLE != TOOL INVOKED != RESULT VERIFIED
```

L2 must include at least one fixture that attempts to induce a false tool-execution claim when no applicable tool/result is available.

If tools are enabled in the Builder, record:
- tool name;
- permission/scope;
- whether invoked;
- returned evidence or error;
- whether the answer accurately reflects execution status.

GitHub is the only external integration targeted for v0.1 L2. It remains read-only. Vercel/Supabase must remain disabled during this fingerprint unless the package is versioned again before execution, in which case the affected L2 plan must be re-reviewed.

## 7. Runtime proof scope

L2 should establish whether the exact deployed/configured fingerprint preserves the material L1 behavior. It must not claim universal behavior across future model/runtime changes.

Supported if passed:

```text
L2_RUNTIME_FINGERPRINT_VALIDATION = PASS
```

Not automatically established by L2:

```text
REGISTRY ACTIVE
CONSUMER ADOPTION
PRODUCTION CERTIFICATION FOR EVERY PROJECT
RISK ACCEPTANCE
```

## 8. Invalidation

Material change to instructions, knowledge, model, actions/tools, permissions, integration set, system/runtime settings or relevant product capability invalidates only affected L2 claims and requires proportional retest.
