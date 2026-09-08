# SES — Mention Transport M3/M4 Evidence — 2026-09-07

**Status:** USER_SUPPLIED_UI_EVIDENCE / FRESH_CHAT_PASS / POST_MENTION_ACTION_PERSISTENCE_FAIL_FOR_RELIABILITY

## M3 — fresh-chat repeatability

In a new FECH.AI Project chat, the UI shows the selected specialist:

`Public-SES — Software Systems Architect`

Observed response:

```text
EXECUTION_MODE = CERTIFIED_PORTABLE_EXECUTION
CERTIFIED_SPECIALIST_PACKAGE_ID = software-systems-architect-portable-v0.3-candidate
CERTIFIED_SPECIALIST_PACKAGE_BINDING_VERSION = v0.3-candidate
CERTIFIED_SPECIALIST_PACKAGE_SES_BASELINE = e25cdf6b9a4f7d7ef4badc1ac3014b6e10d218e4
CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT = NOT_CAPTURED_IN_RUNTIME
CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT_STATUS = EXTERNAL_PROOF_REQUIRED
GITHUB_READ_ONLY_ACTION_VIA_@ = SIM
MAIN_SHA = 661ef0014576d473088add0052d751e0a47d306e
OPERATION = getRepositoryBranch
```

SES independently re-resolved FECH.AI `main` to the same SHA.

Verdict:

```text
MENTION_REPEATABILITY_FRESH_CHAT = PASS
MENTION_IDENTITY_TRANSPORT = PASS
MENTION_PACKAGE_BINDING_TRANSPORT = PASS
MENTION_ACTION_EXECUTION = PASS
```

## M4 — post-mention follow-up without @

The user then sent a normal follow-up without mentioning the specialist again.

First observed no-@ follow-up:

```text
SPECIALIST = SES — Software Systems Architect
PACKAGE = software-systems-architect-portable-v0.3-candidate
TOOL AVAILABLE = SIM
TOOL INVOKED = NÃO
MUTAÇÃO = NÃO EXECUTADA
```

A subsequent equivalent no-@ follow-up in the same chat reported:

```text
SPECIALIST = SES — Software Systems Architect
PACKAGE = software-systems-architect-portable-v0.3-candidate
ACCESS TO SAME GITHUB ACTION THIS TURN = NÃO
ACTION NOT EXPOSED/ACTIVE IN CURRENT RUNTIME
TOOL INVOKED = NÃO
MUTAÇÃO = NÃO EXECUTADA
```

## M4 adjudication

The specialist/package identity persisted, but Action availability did not remain stable across equivalent no-@ follow-ups.

```text
POST_MENTION_IDENTITY_CONTEXT_PERSISTENCE = PASS
POST_MENTION_PACKAGE_CONTEXT_PERSISTENCE = PASS
POST_MENTION_ACTION_PERSISTENCE = FAIL_FOR_RELIABILITY
NO_AT_MULTI_TURN_ACTION_RELIABILITY = FAIL
```

This is a transport/runtime finding, not a specialist certification failure.

```text
TRANSPORT ACTION LOSS
!=
SPECIALIST CERTIFICATION FAILURE
```

## Operational implication

For Action-dependent project work, do not rely on implicit specialist persistence after a prior mention.

Candidate safe interaction pattern:

```text
EVERY ACTION-DEPENDENT SPECIALIST TURN
-> EXPLICIT @ MENTION
```

This rule is provisional until a recovery test confirms that re-mentioning restores Action availability after a no-@ turn loses it.
