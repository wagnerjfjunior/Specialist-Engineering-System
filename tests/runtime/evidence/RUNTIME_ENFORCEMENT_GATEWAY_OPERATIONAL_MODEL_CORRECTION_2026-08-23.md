# SES — Runtime Enforcement Gateway Operational Model Correction — 2026-08-23

**Evidence type:** current-state correction / operational usability finding  
**Subject:** `SES — Specialist Router` + Runtime Enforcement Gateway as the execution path for specialist consultation

## 1. Prior recorded state

SES previously recorded successful bounded Gateway/Router tests, including external health, route cases, GPT Action preview cases and user-reported operational Custom GPT invocation. Those historical records remain preserved under their original fingerprints and evidence boundaries.

No historical PASS is rewritten by this correction.

## 2. New material event

The project owner reported that the Router/Enforcement Gateway is not usable as the real SES specialist-consultation workflow in the ChatGPT project context.

Operationally observed/reported limitations include:

- specialist invocation through the intended Router/@ workflow is not a reliable execution path;
- permission/inter-GPT behavior prevents the intended specialist orchestration from functioning as required;
- external Action behavior of the target specialist is not exposed/usable through that composition path as needed;
- the practical working method is to prepare the consultation in SES, manually copy it, paste it into the target specialist Custom GPT, then copy the specialist result back to SES.

This is a material usability event because the previous project status promoted bounded runtime proofs into `OPERATIONAL_MINIMUM_SCOPE_COMPLETE` for the intended workflow.

## 3. Adjudication

```text
HISTORICAL_GATEWAY_TEST_EVIDENCE = PRESERVED
HISTORICAL_ROUTER_TEST_EVIDENCE = PRESERVED
RETROACTIVE_PASS = NO
RETROACTIVE_ERASURE = NO

CURRENT_ROUTER_OPERATIONAL_ACCEPTANCE = WITHDRAWN
CURRENT_GATEWAY_OPERATIONAL_ACCEPTANCE = WITHDRAWN_FOR_SPECIALIST_CONSULTATION_PATH
CURRENT_ACCEPTED_SPECIALIST_TRANSPORT = MANUAL_COPY_PASTE
```

The correction does not assert that every Gateway endpoint or historical test is technically broken. It asserts the narrower and operationally material fact that the Router/Gateway composition is not the accepted current end-to-end specialist consultation path.

```text
ENDPOINT_TEST_PASS != END_TO_END_WORKFLOW_USABLE
RUNTIME_COMPONENT_AVAILABLE != OPERATIONAL_PATH_ACCEPTED
```

## 4. Replacement operational path

```text
SES
-> resolve project / task / specialist
-> generate Specialist Consultation Packet
-> human copy/paste to target specialist
-> specialist resolves live project context and performs bounded work
-> human copy/paste Specialist Result Packet back to SES
-> SES adjudicates / integrates / selects next action
```

The normative candidate contract for this path is:

`core/protocols/MANUAL_SPECIALIST_HANDOFF_CONTRACT.md`

Behavioral specification:

`tests/behavioral/MANUAL_SPECIALIST_HANDOFF_TESTS.md`

## 5. Boundaries

This correction does not:

- delete Gateway/Router code or historical evidence;
- automatically deprecate their contracts for future experimentation;
- prove the manual workflow has executed for every specialist;
- create specialist adoption in any consumer project;
- authorize mutation in SES or consumer projects beyond the separately authorized correction branch/PR;
- authorize a future Router/Gateway re-adoption.

A future operational Router/Gateway status requires new end-to-end evidence in the intended usage context and an explicit SES adoption decision.