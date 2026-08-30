# SES — Integrated Marketing Strategist — Builder Creation Handoff v0.1

**Status:** `BUILDER_CREATION_HANDOFF / CANDIDATE_ONLY`

## Objective
Create one private Custom GPT runtime candidate for `integrated-marketing-strategist-v0.1` without claiming readiness, registry activation, certification or consumer-project adoption.

## Builder fields
- **Name:** `SES — Integrated Marketing Strategist`
- **Description:** copy exactly from `runtime/custom-gpt/INTEGRATED_MARKETING_STRATEGIST_BUILDER_PACKAGE_V0_1.md`
- **Instructions:** copy the complete exact content of `runtime/custom-gpt/INTEGRATED_MARKETING_STRATEGIST_BUILDER_KERNEL_V0_1.md`
- **Knowledge:** empty
- **Visibility:** private / only me
- **Capabilities:** Web Search and Data Analysis when available
- **Actions/connectors:** none required for initial application; if any are configured, record exact surface and permissions before testing

## Required return evidence
After application, return enough UI/configuration evidence to bind:
1. Builder/GPT identity;
2. exact Instructions version;
3. capabilities;
4. Knowledge state;
5. Actions/connectors;
6. model/material settings if exposed;
7. visibility;
8. timestamp.

Do not infer application from repository versioning.

```text
BUILDER_PACKAGE_EXISTS != BUILDER_APPLIED
BUILDER_APPLIED != RUNTIME_FINGERPRINT_CAPTURED
RUNTIME_FINGERPRINT_CAPTURED != L2_PASS
```

## Next gate
Freeze the applied fingerprint, execute the canonical L1/L2 suites, record failures/retests without retroactive erasure, perform readiness adjudication, obtain explicit user READY authorization, then separately evaluate registry activation and terminal certification.
