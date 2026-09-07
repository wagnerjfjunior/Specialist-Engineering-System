# SES — Mention Transport Canary M1 PASS — 2026-09-07

**Status:** USER_SUPPLIED_RUNTIME_OUTPUT / M1_PASS
**SES main at evidence capture:** `bf11e0974c0922d9096c386929ba40856712e222`

## Scope

Primary canary:
- ChatGPT Project: FECH.AI
- specialist: Public-SES — Software Systems Architect portable v0.3 candidate
- transport: project-level `@` mention
- task: identity/package binding + GitHub read-only Action invocation

## User-supplied runtime result

```text
EXECUTION_MODE =
CERTIFIED_PORTABLE_EXECUTION

CERTIFIED_SPECIALIST_PACKAGE_ID =
software-systems-architect-portable-v0.3-candidate

CERTIFIED_SPECIALIST_PACKAGE_BINDING_VERSION =
v0.3-candidate

CERTIFIED_SPECIALIST_PACKAGE_SES_BASELINE =
e25cdf6b9a4f7d7ef4badc1ac3014b6e10d218e4

CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT =
NOT_CAPTURED_IN_RUNTIME

CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT_STATUS =
EXTERNAL_PROOF_REQUIRED

GITHUB_READ_ONLY_ACTION_VIA_@ =
SIM

MAIN_SHA =
661ef0014576d473088add0052d751e0a47d306e

OPERAÇÃO_EXECUTADA =
getRepositoryBranch
```

## Independent revalidation

SES independently re-resolved:

`wagnerjfjunior/fecha.ai / main`

and observed:

`661ef0014576d473088add0052d751e0a47d306e`

matching the runtime-returned SHA.

The operation name `getRepositoryBranch` is recorded as runtime/user-supplied evidence. SES does not infer that name beyond the observed output.

## M1 adjudication

```text
MENTION_IDENTITY_TRANSPORT = PASS
MENTION_PACKAGE_BINDING_TRANSPORT = PASS
MENTION_PROJECT_CONTEXT = PASS
MENTION_ACTION_AVAILABILITY = PASS
MENTION_ACTION_EXECUTION = PASS

LIVE_SHA_RESULT_MATCH = PASS
CENTRAL_SES_REQUIRED_FOR_ORDINARY_PROJECT_TASK = NO

MENTION_REPEATABILITY_SAME_CHAT = NOT_EXECUTED
MENTION_REPEATABILITY_FRESH_CHAT = NOT_EXECUTED
POST_MENTION_CONTEXT_PERSISTENCE = NOT_EXECUTED
```

## Non-claims

M1 alone does not establish:
- second-mention repeatability in the same chat;
- fresh-chat repeatability;
- post-mention host/specialist context persistence;
- Documentation Auditor mention transport;
- general platform-wide mention reliability.

```text
M1 PASS
!=
FULL MENTION TRANSPORT PASS
```
