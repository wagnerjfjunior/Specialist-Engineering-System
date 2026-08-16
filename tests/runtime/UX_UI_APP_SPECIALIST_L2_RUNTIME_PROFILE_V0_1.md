# SES — UX/UI APP Specialist L2 Runtime Profile v0.1

**Candidate ID:** `ux-ui-app-specialist-v0.1`  
**Prerequisite:** `CANONICAL_L1-C = PASS`  
**Status:** `L2_RUNTIME_CANDIDATE / NOT_APPLIED / NOT_EXECUTED`

## 1. Purpose

L2 validates the actual deployed specialist runtime under an exact fingerprint. It is not another prompt-only behavioral exercise.

```text
L1 PASS != L2 PASS
PROFILE VERSIONED != BUILDER APPLIED
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

## 3. L2 fingerprint fields

Before execution, capture exactly:

```text
RUNTIME_ID
BUILDER/GPT_ID_OR_URL
RUNTIME_NAME
PROFILE_VERSION
PROFILE_BLOB_SHA
INSTRUCTION_BLOB_SHA_OR_EXACT_EXPORT
KNOWLEDGE_FILE_LIST
KNOWLEDGE_FILE_HASHES
ACTIONS/TOOLS_ENABLED
ACTION/TOOL_CONFIG_VERSION
MODEL
MODEL_MODE/SETTINGS
CAPABILITIES
CONVERSATION_START_MODE
DATE/TIME
EXECUTION_ID
```

If a field cannot be obtained from the product UI/API, record `NOT EXPOSED`, not an invented value.

## 4. Required configuration boundary

The runtime must not silently inherit:
- FECH.AI-specific rules;
- Blogs/SEO-specific rules;
- Supabase-specific implementation requirements;
- project-local business rules;
- hidden test answer keys or adjudication rubrics.

Consumer-project knowledge may be added only under a separately versioned adoption/configuration event.

## 5. Tools/actions

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

## 6. Runtime proof scope

L2 should establish whether the exact deployed fingerprint preserves the material L1 behavior. It must not claim universal behavior across future model/runtime changes.

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

## 7. Invalidation

Material change to instructions, knowledge, model, actions/tools, permissions, system/runtime settings or relevant product capability invalidates only affected L2 claims and requires proportional retest.
