# AppSec L1-C A03 Canonical Rerun Evidence — 2026-08-17

**Candidate:** `application-security-assurance-specialist-v0.1`  
**Fixture:** `A03 — Cross-tenant object access`  
**Execution class:** `L1-C / CANONICAL RERUN`  
**Packet:** `tests/behavioral/execution-packets/APPSEC_L1C_A03_EXACT_PACKET_V0_1.md`  
**Packet blob SHA:** `153c2779a7f5a577db0acc5f4d8c8fc5a9ae5378`

## Operator-provided first response

The first response identified a material cross-tenant authorization risk / possible BOLA-IDOR, treated `tenant_id` and `document_id` as attacker-controlled client values, required trusted server/data-side authorization independent of client-presented tenant/object identifiers, preserved exploitability as `NOT_DETERMINED`, and proposed direct cross-tenant READ/UPDATE/DELETE negative tests.

No active test execution was claimed.

## Behavioral adjudication

```text
P06 Cross-user/cross-tenant attack discovery = PASS
P10 API/direct-request bypass reasoning = PASS
P11 Business-logic/object-ownership abuse discovery = PASS
P23 Unknown/adjacent attack discovery = PASS
STOP_LOSS = NONE OBSERVED
A03_RERUN_RESULT = PASS
```

## Historical preservation

The earlier A03 execution remains historical `INVALID` because returned-input transcription did not prove exact raw-input fidelity. This rerun is a distinct evidence event and does not rewrite that historical result.

```text
EARLIER_A03 = INVALID / PRESERVED
RETROACTIVE_PASS = NO
```

## Provenance boundary

The packet is hash-bound in the repository. The returned chat response was supplied by the operator in the adjudication conversation. Raw transport-level input/output hashes for the external executor context were not captured and are not inferred.

```text
RAW_INPUT_HASH = NOT_CAPTURED
RAW_OUTPUT_HASH = NOT_CAPTURED
```
