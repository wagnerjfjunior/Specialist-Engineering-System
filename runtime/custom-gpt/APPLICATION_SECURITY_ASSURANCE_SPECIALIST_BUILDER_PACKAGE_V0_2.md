# SES — Application Security Assurance Specialist Builder Configuration Package v0.2

**Package ID:** `application-security-assurance-specialist-builder-package-v0.2`  
**Candidate:** `application-security-assurance-specialist-v0.1`  
**Status:** `BUILDER_FIT_COMPACT_BINDING / RUNTIME_EVIDENCE_IN_PROGRESS / NOT_READY / NOT_ACTIVE`

## 1. Purpose

Bind the actual AppSec Builder/runtime to the compact Builder-fit Instructions payload that was observed in the configured GPT and used for runtime validation.

This package does not rewrite or replace the historical full kernel v0.1. It records a new executable Builder-fit fingerprint derived from that semantic source.

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
Preserve the configured AppSec description unless separately changed and revalidated.

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

The repository compact kernel was created from that exact supplied payload; Git blob identity is recorded separately from SHA-256.

## 4. Semantic-source relation

Historical semantic source:

`runtime/custom-gpt/APPLICATION_SECURITY_ASSURANCE_SPECIALIST_BUILDER_KERNEL_V0_1.md`

Full kernel blob SHA:

`6c44ce208425402aa4a89adfc5cd4e4ed8571ed3`

The compact kernel is not byte-identical to the full kernel. A separate semantic-equivalence review records preserved material safeguards and noncritical compression deltas.

Canonical comparison evidence:

`tests/runtime/evidence/APPLICATION_SECURITY_ASSURANCE_COMPACT_KERNEL_SEMANTIC_REVIEW_2026-08-17.md`

## 5. Conversation starters

Preserve the four configured v0.1 starters unless a separately versioned Builder change is authorized. Starter wording is not part of the compact-kernel text itself.

## 6. Knowledge and capabilities

Target/effective binding for the currently tested private runtime must be captured from the Builder UI and runtime evidence. Preserve known constraints:

```text
KNOWLEDGE = EMPTY
GITHUB_ACTION = ENABLED / READ_ONLY
VERCEL = DISABLED
SUPABASE = DISABLED
VISIBILITY = PRIVATE / APENAS PARA MIM
MODEL / MODEL SETTINGS = NOT EXPOSED unless observed
```

Web Search / Data Analysis / Image Generation must be recorded as actually configured when final fingerprint evidence is closed. Capability availability is not proof of invocation.

## 7. GitHub Action

Use the approved SES GitHub read-only Action only.

Historical schema source:

`runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`

Schema blob:

`1e6237e806fd84716ec13b019e6617ad4110a211`

R06 on the compact runtime returned read-only repository evidence successfully and made no mutation. Final L2 adjudication must preserve the exact R06 evidence event rather than rewriting the earlier blocked event.

## 8. Runtime proof boundary

```text
R06_INITIAL = BLOCKED / EXTERNAL RUNTIME-ACTION SERVICE
R06_RETEST_2026-08-17 = PASS
INITIAL BLOCKED HISTORY = PRESERVED
RETROACTIVE PASS = NO
```

The compact Instructions were the effective runtime Instructions used for the current R06 retest. The v0.1 full-kernel exact-copy requirement was not met and is not claimed as met.

## 9. L2 binding

Use:

- `tests/runtime/APPLICATION_SECURITY_ASSURANCE_SPECIALIST_L2_RUNBOOK_V0_1.md` for preserved fixture/proof-obligation definitions;
- `tests/runtime/APPLICATION_SECURITY_ASSURANCE_SPECIALIST_L2_COMPACT_BINDING_V0_2.md` for the executable compact-fingerprint binding and affected-gate adjudication rules.

Do not replay unaffected L1/L2 gates merely to create confidence. Revalidate only claims affected by the compact-kernel binding or contradictory evidence.

## 10. Invalidation

Material changes to compact Instructions, Knowledge, model/settings, capabilities, Action schema/authentication scope, integration set, permissions or runtime behavior invalidate only affected fingerprint claims and require proportional retest.

```text
L1 PASS != L2 PASS
L2 PASS != READY
READY != ARCHETYPE ACTIVE
TOOL CAPABILITY != AUTHORIZATION
```
