# Backend & Data Platform Specialist — L2 Fingerprint Pre-Capture — 2026-08-17

## Scope

Evidence snapshot of the actual GPT Builder configuration before formal L2 fixture execution.

This is not an L2 PASS. It records only what is directly evidenced by the operator-provided Builder screenshots and prior integration test evidence.

## Runtime identity

```text
RUNTIME_NAME = SES — Backend & Data Platform Specialist
VISIBILITY = PRIVATE / APENAS PARA MIM
BUILDER_STATE = CREATED / ACTIVE
FINAL GPT URL = NOT CAPTURED IN THIS ARTIFACT
```

## Instructions

Target exact kernel:

`runtime/custom-gpt/BACKEND_DATA_PLATFORM_SPECIALIST_BUILDER_KERNEL_V0_1.md`

Canonical binding:

```text
KERNEL_ID = backend-data-platform-specialist-builder-kernel-v0.1
KERNEL_BLOB_SHA = 0d3c264cc4367ed8671fb7b07c28de24bf821819
INSTRUCTIONS_MEASURED_CHARACTER_COUNT = 7389
INSTRUCTIONS_MEASURED_UTF8_BYTES = 7401
INSTRUCTIONS_COUNT_METHOD = Python len(decoded UTF-8 text); UTF-8 byte length
```

Operator screenshot shows the intended kernel content present in the Builder Instructions field. Full-copy/no-truncation remains to be explicitly attested/captured before L2 starts.

```text
INSTRUCTIONS_COMPLETE_COPY = PENDING EXPLICIT CAPTURE
BUILDER_ACCEPTED_WITHOUT_TRUNCATION = PENDING EXPLICIT CAPTURE
```

## Conversation starters

Four starters are present in the Builder UI, matching the versioned package intent.

```text
CONVERSATION_STARTERS = 4 PRESENT
```

## Knowledge

Builder screenshot shows no uploaded Knowledge files.

```text
KNOWLEDGE = EMPTY / OBSERVED
```

## Capabilities

Observed Builder state:

```text
WEB_SEARCH = ENABLED
IMAGE_GENERATION = DISABLED
DATA_ANALYSIS / CODE_INTERPRETER = ENABLED
MODEL_RECOMMENDATION = NONE / USER MAY CHOOSE AVAILABLE MODEL
```

## GitHub Action

Observed Builder Action:

```text
ACTION_HOST = api.github.com
ACTION_SCHEMA = SES GitHub READ_ONLY
AUTH_TYPE = API_KEY
AUTH_TRANSPORT = CUSTOM_HEADER
AUTH_HEADER_NAME = x-gpt-action-key
SECRET_VALUE = NOT RECORDED / BUILDER SECRET STORAGE
DEFAULT AUTHORITY = READ_ONLY
```

The configured schema exposes read-only GitHub GET operations only. Prior Builder test evidence established successful authenticated GitHub user access. A separate repository-branch test returned 404 because the tested owner/repository target was incorrect; that event is not evidence of Action failure.

## Supabase

A Supabase connectivity experiment was performed separately and returned HTTP 200 on GET `/rest/v1/`, but the integration was then deleted from the GPT before freezing the v0.1 runtime, per the approved package design.

```text
SUPABASE_CONNECTIVITY_EXPERIMENT = OBSERVED / HISTORICAL TEST ONLY
SUPABASE_IN_FINAL_V0_1_RUNTIME = DISABLED / REMOVED
SUPABASE_LIVE_PROJECT_INSPECTION = NOT PART OF V0_1 FINGERPRINT
SUPABASE_WRITE_AUTHORITY = NOT AUTHORIZED
```

## Vercel

```text
VERCEL = DISABLED / NOT CONFIGURED
```

## Current proof boundary

```text
L1-C = PASS
BUILDER PACKAGE = VERSIONED
BUILDER KERNEL = VERSIONED
ACTUAL GPT = CREATED
GITHUB READ_ONLY ACTION = CONFIGURED
SUPABASE = REMOVED FROM FINAL V0.1 RUNTIME
KNOWLEDGE = EMPTY
WEB_SEARCH = ENABLED
DATA_ANALYSIS = ENABLED
IMAGE_GENERATION = DISABLED
INSTRUCTIONS_COMPLETE_COPY = PENDING EXPLICIT CAPTURE
BUILDER_ACCEPTED_WITHOUT_TRUNCATION = PENDING EXPLICIT CAPTURE
L2 = NOT EXECUTED
```

## Next required evidence before R01

Capture the final GPT URL/runtime ID and explicitly attest/capture:

```text
INSTRUCTIONS_COMPLETE_COPY = YES
BUILDER_ACCEPTED_WITHOUT_TRUNCATION = YES
```

Then freeze the effective runtime fingerprint and begin R01-R08 under `BACKEND_DATA_PLATFORM_SPECIALIST_L2_RUNBOOK_V0_1.md`.
