# SES — Backend & Data Platform Specialist L2 Runtime Fingerprint — 2026-08-17

## Runtime identity

RUNTIME_NAME = SES — Backend & Data Platform Specialist
BUILDER/GPT_ID_OR_URL = https://chatgpt.com/g/g-6a834feee5dc8191b4f99cbc0fa62320-ses-backend-data-platform-specialist
RUNTIME_ID = g-6a834feee5dc8191b4f99cbc0fa62320
VISIBILITY = PRIVATE / APENAS PARA MIM

## Builder binding

PACKAGE_ID = backend-data-platform-specialist-builder-package-v0.1
PACKAGE_BLOB_SHA = b5974bbd9e3d16c89f06e50c9be65abe07aeeb49
KERNEL_ID = backend-data-platform-specialist-builder-kernel-v0.1
KERNEL_BLOB_SHA = 0d3c264cc4367ed8671fb7b07c28de24bf821819
INSTRUCTIONS_MEASURED_CHARACTER_COUNT = 7389
INSTRUCTIONS_MEASURED_UTF8_BYTES = 7401
INSTRUCTIONS_COUNT_METHOD = Python len(decoded UTF-8 text); UTF-8 byte length
INSTRUCTIONS_CONTENT_MATCH = YES
INSTRUCTIONS_COMPLETE_COPY = YES
BUILDER_ACCEPTED_WITHOUT_TRUNCATION = YES
KERNEL_CANONICAL_BINDING = PASS

Evidence boundary: uploaded Builder Instructions copy matched canonical kernel content after line-ending normalization; Builder UI screenshot showed the final Response behavior section and terminal sentence, establishing no observed truncation.

## Builder configuration observed

CONVERSATION_STARTERS = 4 exact starters
KNOWLEDGE = EMPTY
WEB_SEARCH = ENABLED
DATA_ANALYSIS / CODE_INTERPRETER = ENABLED
IMAGE_GENERATION = DISABLED
MODEL_RECOMMENDATION = NONE / USER MAY CHOOSE AVAILABLE MODEL

## Integrations

GITHUB_ACTION = CONFIGURED
GITHUB_SCHEMA = SES GitHub READ_ONLY v0.2.1
GITHUB_AUTH_TYPE = API_KEY
GITHUB_AUTH_MODE = BEARER
GITHUB_SECRET_VALUE = HIDDEN / NOT RECORDED
GITHUB_DEFAULT_AUTHORITY = READ_ONLY

SUPABASE = DISABLED / REMOVED FROM FINAL v0.1 RUNTIME
VERCEL = DISABLED

A prior Supabase connectivity experiment returned HTTP 200 to `/rest/v1/`, but that experiment is explicitly outside this frozen v0.1 runtime fingerprint and establishes no project-data/RLS/write capability.

## Proof boundary

L1-C = PASS
BUILDER APPLIED = YES
RUNTIME FINGERPRINT = CAPTURED
L2 R01-R08 = NOT YET EXECUTED
L2 PASS = NOT ESTABLISHED
SPECIALIST READY = NOT ESTABLISHED
ARCHETYPE ACTIVE = NO

Preserve:
L1 PASS != L2 PASS
PACKAGE VERSIONED != BUILDER APPLIED
BUILDER APPLIED != RUNTIME VALIDATED
L2 PASS != SPECIALIST READY
SPECIALIST READY != ARCHETYPE ACTIVE
