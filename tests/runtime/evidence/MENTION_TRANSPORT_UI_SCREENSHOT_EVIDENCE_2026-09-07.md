# SES — Mention Transport UI Screenshot Evidence — 2026-09-07

**Status:** USER_SUPPLIED_UI_EVIDENCE / TRANSPORT_PARTIAL_REFINEMENT
**SES main at evidence capture:** `a8c89665af4f9a3e708a3ed1a57a1ae8b60f662a`

## Scope

Two screenshots from a FECH.AI project chat were supplied as UI evidence for project-level `@` mention transport of the Software Systems Architect candidate.

The screenshots are treated as stronger evidence for visible tool invocation than plain runtime prose, but they do not expose hidden transport internals or complete GPT configuration.

## Screenshot A — first visible invocation

Observed visible response fields include:

```text
EXECUTION_MODE =
LIVE READ ONLY / PROJECT-LOCAL / NO SES CENTRAL

CERTIFIED_SPECIALIST_PACKAGE_ID =
NOT_EXPOSED_IN_THIS_RUNTIME

CERTIFIED_SPECIALIST_PACKAGE_BINDING_VERSION =
NOT_EXPOSED_IN_THIS_RUNTIME

CERTIFIED_SPECIALIST_PACKAGE_SES_BASELINE =
NOT_EXPOSED_IN_THIS_RUNTIME

CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT =
NOT_EXPOSED_IN_THIS_RUNTIME

CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT_STATUS =
UNVERIFIABLE — package metadata not exposed; no value invented

GitHub read-only via @ neste runtime =
YES — read-only GitHub access was actually invoked successfully

MAIN LIVE SHA =
661ef0014576d473088add0052d751e0a47d306e

OPERAÇÃO REALMENTE EXECUTADA =
READ-ONLY GET /repos/wagnerjfjunior/fecha.ai/branches/main

SES CENTRAL ACCESSED =
NO
```

The ChatGPT UI visibly shows `Ferramenta chamada`.

## Screenshot B — second visible invocation in the same chat

Observed:

```text
SHA atual de main =
661ef0014576d473088add0052d751e0a47d306e

Action GitHub realmente invocada nesta segunda chamada =
SIM

Operação executada =
leitura read-only de GET /repos/wagnerjfjunior/fecha.ai/branches/main

Bloqueio observado =
NENHUM

Permission prompt observado =
NENHUM

runtime statement =
O SHA acima foi obtido por nova leitura live nesta chamada,
não reutilizado da resposta anterior.
```

The ChatGPT UI again visibly shows `Ferramenta chamada`.

## Evidence refinement

The screenshots materially strengthen:

```text
MENTION_ACTION_AVAILABILITY = PASS
MENTION_ACTION_EXECUTION = PASS
MENTION_REPEATABILITY_SAME_CHAT = PASS
SECOND_CALL_BLOCKING = NONE_OBSERVED
SECOND_CALL_PERMISSION_PROMPT = NONE_OBSERVED
```

They also reveal that package metadata is not necessarily exposed in every observed mention runtime response.

Therefore the current transport state must not be collapsed into a single global PASS.

```text
ACTION TRANSPORT THROUGH @ = PASS_FOR_OBSERVED_CHAT
PACKAGE METADATA EXPOSURE THROUGH @ = INCONSISTENT / NOT_YET_PROVEN_REPEATABLE
```

## Relationship to prior M1/M2 evidence

Prior user-supplied M1 text reported exact package binding constants.

This UI evidence shows another observed response in which those fields are `NOT_EXPOSED_IN_THIS_RUNTIME`.

Without evidence proving these are the exact same invocation/result object, SES must preserve both observations rather than overwrite either one.

```text
PRIOR EXACT-BINDING OBSERVATION = PRESERVED
UI NOT-EXPOSED OBSERVATION = PRESERVED
CONTRADICTION / RUNTIME VARIABILITY = OPEN
```

## Current dimensional adjudication

```text
MENTION_ACTION_AVAILABILITY = PASS
MENTION_ACTION_EXECUTION = PASS
MENTION_REPEATABILITY_SAME_CHAT = PASS
MENTION_PROJECT_REPOSITORY_ACCESS = PASS
MENTION_NO_CENTRAL_SES_FOR_ORDINARY_TASK = PASS_FOR_OBSERVED_UI

MENTION_IDENTITY_TRANSPORT = NOT_DETERMINED_AS_REPEATABLE
MENTION_PACKAGE_BINDING_TRANSPORT = NOT_DETERMINED_AS_REPEATABLE

MENTION_REPEATABILITY_FRESH_CHAT = NOT_EXECUTED / NOT_CLOSED_BY_THESE_SCREENSHOTS
POST_MENTION_CONTEXT_PERSISTENCE = NOT_EXECUTED
```

## Next safe action

Use a fresh FECH.AI project chat and invoke the same specialist through the mention UI.

The next test must determine whether exact package identity/binding is exposed consistently in a fresh chat while GitHub Action execution remains available.

Do not modify specialist certification because of this transport-layer variability.

```text
TRANSPORT VARIABILITY
!=
SPECIALIST CERTIFICATION FAILURE
```
