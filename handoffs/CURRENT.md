# SES — Current Handoff

**Status:** `MANUAL_SPECIALIST_HANDOFF / CURRENT_OPERATIONAL_PATH`  
**Canonical source:** `wagnerjfjunior/Specialist-Engineering-System`  
**Canonical ref rule:** resolve `main` live before material work  
**Authoritative next action:** `docs/NEXT_SAFE_ACTION.md`

## Mandatory reading order

1. resolve SES `main` live and read `docs/bootstrap/INDEX.md`;
2. read `handoffs/CURRENT.md`;
3. read `docs/PROJECT_STATUS.md`;
4. read `docs/NEXT_SAFE_ACTION.md`;
5. read `docs/BLOCKED_ACTIONS.md`;
6. for SES-mediated specialist consultation, read `core/protocols/MANUAL_SPECIALIST_HANDOFF_CONTRACT.md` and `tests/behavioral/MANUAL_SPECIALIST_HANDOFF_TESTS.md`;
7. for historical or deliberately reopened Gateway work, read `core/protocols/RUNTIME_ENFORCEMENT_GATEWAY_CONTRACT.md`, `runtime/specialist_gateway/CUSTOM_GPT_PROFILE.md` and the applicable runtime/deployment evidence before making any Gateway operational claim.

## Current certified portfolio

```text
UX/UI APP Specialist = CERTIFIED_FOR_ANY_PROJECT YES
Backend & Data Platform Specialist = YES
Application Security Assurance Specialist = YES
Software Systems Architect = YES
Documentation Auditor = YES / v1.1
```

All certification remains fingerprint-bound. Historical FAIL/BLOCKED/INVALID/overclaim events remain preserved.

```text
RETROACTIVE_PASS = NO
RETROACTIVE_ERASURE = NO
```

## Current specialist consultation model

The accepted current operational transport is manual human-mediated copy/paste.

```text
SES
-> resolve explicit project / task / specialist
-> generate Specialist Consultation Packet
-> HUMAN COPY
-> target specialist Custom GPT
-> HUMAN PASTE
-> specialist resolves live context and performs bounded work
-> HUMAN COPY result
-> SES
-> SES adjudication / next decision
```

Normative contract:

`core/protocols/MANUAL_SPECIALIST_HANDOFF_CONTRACT.md`

Behavioral specification:

`tests/behavioral/MANUAL_SPECIALIST_HANDOFF_TESTS.md`

Preserve:

```text
CONSULTED != ADOPTED
ADOPTED != EXECUTED
EXECUTED != AUTHORIZED_TO_MUTATE
SPECIALIST_OUTPUT != SES_APPROVAL
COPIED_CONTEXT != LIVE_EVIDENCE
```

An explicit ad-hoc consultation with a certified specialist may occur without project adoption only when clearly labeled `EXPLICIT_AD_HOC_CONSULTATION`. It must not create or imply a project role mapping.

## Runtime Enforcement Gateway / Specialist Router

Gateway and Router remain versioned historical/runtime-candidate assets. Their prior bounded test evidence is preserved, including controller/loader/HTTP/external route/GPT Action/Custom GPT observations recorded on 2026-08-20.

A later material usability event withdrew their acceptance as the current end-to-end specialist-consultation workflow in the ChatGPT project context.

```text
HISTORICAL_GATEWAY_TEST_EVIDENCE = PRESERVED
HISTORICAL_ROUTER_TEST_EVIDENCE = PRESERVED
SPECIALIST_ROUTER_CURRENT_STATUS = NOT_CURRENT_OPERATIONAL_PATH
RUNTIME_ENFORCEMENT_GATEWAY_CURRENT_STATUS = NOT_CURRENT_OPERATIONAL_PATH_FOR_SPECIALIST_CONSULTATION
CURRENT_SPECIALIST_TRANSPORT = MANUAL_COPY_PASTE
RETROACTIVE_ERASURE = NO
```

Correction evidence:

`tests/runtime/evidence/RUNTIME_ENFORCEMENT_GATEWAY_OPERATIONAL_MODEL_CORRECTION_2026-08-23.md`

Historical Gateway evidence remains available at:

```text
tests/runtime/evidence/RUNTIME_ENFORCEMENT_GATEWAY_DEPLOYMENT_ATTEMPT_2026-08-20.md
tests/runtime/evidence/RUNTIME_ENFORCEMENT_GATEWAY_EXTERNAL_HEALTH_2026-08-20.md
tests/runtime/evidence/RUNTIME_ENFORCEMENT_GATEWAY_EXTERNAL_ROUTE_2026-08-20.md
tests/runtime/evidence/RUNTIME_ENFORCEMENT_GATEWAY_GPT_ACTION_PREVIEW_2026-08-20.md
tests/runtime/evidence/RUNTIME_ENFORCEMENT_GATEWAY_OPERATIONAL_CUSTOM_GPT_ADOPTION_2026-08-20.md
```

```text
ENDPOINT_TEST_PASS != END_TO_END_WORKFLOW_USABLE
RUNTIME_COMPONENT_AVAILABLE != OPERATIONAL_PATH_ACCEPTED
```

Do not delete or rewrite those historical proofs. Do not use them to claim current Router/Gateway operational acceptance.

## Authority boundary

Manual transport does not change project authority. Consumer projects remain authoritative for project truth, current state, environments, project-local specialist rules, adoption and mutation permissions.

```text
AS_IS != TARGET_STATE
TOOL_CAPABILITY != AUTHORIZATION
CERTIFIED_FOR_ANY_PROJECT != CONSUMER_PROJECT_ADOPTED
CENTRAL_EVOLUTION != AUTOMATIC_PROJECT_MUTATION
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
```

Required secrets remain external and must not be requested, copied between GPTs or committed:

```text
SES_GITHUB_TOKEN
SES_GATEWAY_API_KEY
```

## Next objective

For ordinary specialist consultation, use the manual handoff path. Do not reopen Gateway work automatically.

A future Router/Gateway transport may be reconsidered only after a deliberate SES objective, new end-to-end evidence in the intended user workflow and explicit adoption.

The authoritative next-action semantics are in `docs/NEXT_SAFE_ACTION.md`.