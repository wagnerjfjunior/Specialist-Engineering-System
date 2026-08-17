# SES — Application Security Assurance Specialist Builder Configuration Package v0.2

**Package ID:** `application-security-assurance-specialist-builder-package-v0.2`  
**Candidate:** `application-security-assurance-specialist-v0.1`  
**Status:** `BUILDER_FIT_COMPACT_BINDING / L2_PASS_COMPACT_FINGERPRINT_BOUND / READY_USER_AUTHORIZED / ARCHETYPE_ACTIVE_ON_CANDIDATE_BRANCH`

## 1. Purpose

Bind the actual AppSec Builder/runtime to the compact Builder-fit Instructions payload that was observed in the configured GPT and used for runtime validation.

This package does not rewrite or replace the historical full kernel v0.1. It records the executable Builder-fit fingerprint derived from that semantic source and the validated runtime configuration evidence used for L2 closure.

```text
FULL KERNEL v0.1 = CANONICAL SEMANTIC SOURCE / HISTORICAL
COMPACT KERNEL v0.2 = EFFECTIVE BUILDER-FIT EXECUTABLE PAYLOAD
SEMANTIC EQUIVALENCE != BYTE IDENTITY
V0.1 EXACT-COPY REQUIREMENT != RETROACTIVELY SATISFIED
```

## 2. Builder identity

### Name
`SES — Application Security Assurance Specialist`

### Description
Configured description observed in Builder UI and preserved unless separately changed and revalidated.

### Visibility
`PRIVATE / APENAS PARA MIM`

## 3. Instructions — exact Builder-fit binding

Use the complete exact content of:

`runtime/custom-gpt/APPLICATION_SECURITY_ASSURANCE_SPECIALIST_BUILDER_KERNEL_COMPACT_V0_2.md`

Compact kernel Git blob SHA:

`bb4a776b8d67f16e89b30961a37c212ef2605c9f`

Observed effective Instructions capture supplied by the operator on 2026-08-17:

```text
filename = AppSec_Instructions.txt
characters = 7977
UTF-8 bytes = 7979
lines = 113
SHA-256 = cc0b28b453d4ed64ceac1c5dc7214f596d8bbc71e4130917fe24a47c3b2881a6
trailing_newline = NO
```

Count method:

```text
characters = Python len(decoded UTF-8 text)
UTF-8 bytes = len(text.encode("utf-8"))
lines = newline_count + 1
SHA-256 = SHA-256 of exact UTF-8 bytes supplied by the operator
```

The repository compact kernel was created from that supplied payload; Git blob identity is recorded separately from SHA-256.

## 4. Semantic-source relation

Historical semantic source:

`runtime/custom-gpt/APPLICATION_SECURITY_ASSURANCE_SPECIALIST_BUILDER_KERNEL_V0_1.md`

Full kernel blob SHA:

`6c44ce208425402aa4a89adfc5cd4e4ed8571ed3`

The compact kernel is not byte-identical to the full kernel. The semantic-equivalence review records preserved material safeguards and noncritical compression deltas:

`tests/runtime/evidence/APPLICATION_SECURITY_ASSURANCE_COMPACT_KERNEL_SEMANTIC_REVIEW_2026-08-17.md`

## 5. Conversation starters

The configured Builder UI shows the four AppSec starters used by this specialist. Starter wording is not part of the compact-kernel text itself. Material starter changes that affect behavior require proportional review.

## 6. Effective runtime configuration

Operator-provided Builder screenshots on 2026-08-17 established the following UI-visible runtime configuration:

```text
MODEL = GPT-5.6 Sol (gpt-5-6)
WEB_SEARCH = ENABLED
IMAGE_GENERATION = ENABLED
DATA_ANALYSIS / CODE_INTERPRETER = ENABLED
KNOWLEDGE = EMPTY / NO FILES OBSERVED
GITHUB_ACTION = CONFIGURED / api.github.com
VISIBILITY = PRIVATE / APENAS PARA MIM
```

Additional integration constraints preserved from the recorded AppSec runtime configuration evidence:

```text
GITHUB_ACTION_AUTHORITY = READ_ONLY
VERCEL = DISABLED
SUPABASE = DISABLED
```

Capability availability is not proof of invocation. Tool-execution claims require returned evidence from the applicable tool.

Canonical UI/config evidence record:

`tests/runtime/evidence/APPLICATION_SECURITY_ASSURANCE_RUNTIME_UI_CONFIGURATION_2026-08-17.md`

## 7. GitHub Action

Use the approved SES GitHub read-only Action only.

Historical schema source:

`runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`

Schema blob:

`1e6237e806fd84716ec13b019e6617ad4110a211`

R06 on the compact runtime returned read-only repository evidence successfully and made no mutation. Final L2 adjudication preserves the exact R06 evidence event rather than rewriting the earlier blocked event.

## 8. Runtime proof boundary

```text
R06_INITIAL = BLOCKED / EXTERNAL RUNTIME-ACTION SERVICE
R06_RETEST_2026-08-17 = PASS
INITIAL BLOCKED HISTORY = PRESERVED
RETROACTIVE PASS = NO
```

The operator explicitly attested that the same compact Instructions payload remained effective during the already-recorded R01-R08 executions.

```text
R01_R08_EFFECTIVE_INSTRUCTIONS_CONTINUITY = OPERATOR_ATTESTED / YES
RAW_RUNTIME_TELEMETRY = NOT CAPTURED
CONTRADICTORY_RUNTIME_EVIDENCE = NONE OBSERVED
```

## 9. L2 and readiness binding

Use:

- `tests/runtime/APPLICATION_SECURITY_ASSURANCE_SPECIALIST_L2_RUNBOOK_V0_1.md` for preserved fixture/proof-obligation definitions;
- `tests/runtime/APPLICATION_SECURITY_ASSURANCE_SPECIALIST_L2_COMPACT_BINDING_V0_2.md` for the executable compact-fingerprint binding;
- `tests/runtime/evidence/APPLICATION_SECURITY_ASSURANCE_L2_FINAL_VERDICT_COMPACT_V0_2_2026-08-17.md` for final L2 adjudication;
- `tests/runtime/evidence/APPLICATION_SECURITY_ASSURANCE_SPECIALIST_READINESS_DECISION_2026-08-17.md` for readiness authorization.

Current candidate-branch lifecycle state:

```text
L1-C = PASS
L2_RUNTIME_FINGERPRINT_VALIDATION = PASS / COMPACT_FINGERPRINT_BOUND
SPECIALIST_READINESS = READY / USER_AUTHORIZED
ARCHETYPE_RESOLUTION_STATUS = ACTIVE ON CANDIDATE BRANCH
```

Canonical `main` archetype activation requires merge of the candidate branch.

## 10. Invalidation

Material changes to compact Instructions, Knowledge, model/settings, capabilities, Action schema/authentication scope, integration set, permissions or runtime behavior invalidate only affected fingerprint claims and require proportional retest.

```text
L1 PASS != L2 PASS
L2 PASS != READY
READY != ARCHETYPE ACTIVE
ARCHETYPE ACTIVE != CONSUMER ADOPTION
TOOL CAPABILITY != AUTHORIZATION
```
