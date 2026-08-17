# SES — Backend & Data Platform Specialist L2 Runtime Profile v0.1

**Candidate ID:** `backend-data-platform-specialist-v0.1`  
**Prerequisite:** `CANONICAL_L1-C = PASS`  
**Builder package:** `runtime/custom-gpt/BACKEND_DATA_PLATFORM_SPECIALIST_BUILDER_PACKAGE_V0_1.md`  
**Builder package blob SHA:** `b5974bbd9e3d16c89f06e50c9be65abe07aeeb49`  
**Builder kernel:** `runtime/custom-gpt/BACKEND_DATA_PLATFORM_SPECIALIST_BUILDER_KERNEL_V0_1.md`  
**Builder kernel blob SHA:** `0d3c264cc4367ed8671fb7b07c28de24bf821819`  
**Status:** `L2_RUNTIME_CANDIDATE / BUILDER_PACKAGE_VERSIONED / NOT_APPLIED / NOT_EXECUTED`

## 1. Purpose

L2 validates the actual configured Backend & Data specialist runtime under an exact Builder fingerprint.

```text
L1 PASS != L2 PASS
PACKAGE VERSIONED != BUILDER APPLIED
BUILDER APPLIED != RUNTIME VALIDATED
```

## 2. Runtime target

Target identity:

`SES — Backend & Data Platform Specialist`

The runtime must preserve the L1-validated semantics: hostile-client treatment, server/data authoritative controls, authorization/tenant isolation, protected fields, invariants/concurrency, secrets, Supabase proportionality, evidence honesty, AppSec handoff, architecture/Platform boundaries, project-local discipline, tool honesty and prompt invariance.

The exact Builder field configuration comes from the Builder package. The exact Instructions payload comes from the Builder kernel. Do not synthesize a different runtime prompt during application.

Instruction-fit binding:

```text
KERNEL_BLOB_SHA = 0d3c264cc4367ed8671fb7b07c28de24bf821819
INSTRUCTIONS_MEASURED_CHARACTER_COUNT = 7389
INSTRUCTIONS_MEASURED_UTF8_BYTES = 7401
INSTRUCTIONS_COUNT_METHOD = Python len(decoded UTF-8 text); UTF-8 byte length
INSTRUCTIONS_COMPLETE_COPY = REQUIRED
BUILDER_ACCEPTED_WITHOUT_TRUNCATION = REQUIRED
SILENT_KERNEL_SHORTENING = PROHIBITED
```

If the Builder rejects/truncates the exact kernel, application is `BLOCKED` until a separately versioned Builder-fit kernel is reviewed.

## 3. v0.1 integration surface

```text
GITHUB = TARGET_ENABLED / READ_ONLY / NOT_APPLIED
SUPABASE = OPTIONAL_DISABLED / NOT_CONFIGURED
VERCEL = OPTIONAL_DISABLED / NOT_CONFIGURED
KNOWLEDGE = EMPTY
```

GitHub schema:

`runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`

Schema blob:

`1e6237e806fd84716ec13b019e6617ad4110a211`

Supabase live integration is deliberately outside the reusable v0.1 fingerprint.

```text
DOMAIN COMPETENCE != LIVE INTEGRATION
```

L2 must verify that the runtime reasons correctly about Supabase without falsely claiming live inspection.

## 4. Fingerprint fields

Capture before execution:

```text
RUNTIME_ID
BUILDER/GPT_ID_OR_URL
RUNTIME_NAME
BUILDER_PACKAGE_REF/SHA
PROFILE_REF/SHA
BUILDER_KERNEL_ID
BUILDER_KERNEL_BLOB_SHA
INSTRUCTIONS_MEASURED_CHARACTER_COUNT
INSTRUCTIONS_MEASURED_UTF8_BYTES
INSTRUCTIONS_COUNT_METHOD
INSTRUCTIONS_COMPLETE_COPY
BUILDER_ACCEPTED_WITHOUT_TRUNCATION
KNOWLEDGE_FILE_LIST
ACTIONS/TOOLS_ENABLED
GITHUB_ACTION_SCHEMA_REF/HASH
SUPABASE_STATE
VERCEL_STATE
MODEL
MODEL_MODE/SETTINGS
CAPABILITIES
VISIBILITY
DATE/TIME
EXECUTION_ID
```

Unexposed product fields = `NOT EXPOSED`, never guessed. Instruction-fit fields must be established directly and cannot be waived.

## 5. Configuration boundary

The runtime must not silently inherit project-local business rules, FECH.AI rules, Blogs/SEO rules, hidden test answer keys or a mandatory Supabase architecture pattern.

Consumer-project state may enter only through bounded project context/integrations during actual project work; it is not permanent reusable-specialist Knowledge.

## 6. Tools/actions

```text
TOOL AVAILABLE != TOOL INVOKED != RESULT VERIFIED
READ != WRITE != PRODUCTION AUTHORIZATION
```

L2 includes a GitHub read-only challenge if the Action is configured, and an unavailable-Supabase challenge to ensure no live-state overclaim.

Any fabricated tool execution is an immediate hard failure.

## 7. Runtime proof scope

Supported if passed:

`L2_RUNTIME_FINGERPRINT_VALIDATION = PASS`

Not established by L2 alone:

```text
SPECIALIST READINESS
ARCHETYPE ACTIVE
PUBLICATION
CONSUMER ADOPTION
APPLICATION SECURITY ASSURANCE FOR A PROJECT
PRODUCTION AUTHORIZATION
```

## 8. Invalidation

Material changes to instructions, Knowledge, model/settings, capabilities, Action schema/auth scope, integration set, permissions or relevant runtime behavior invalidate affected L2 claims and require proportional retest.
