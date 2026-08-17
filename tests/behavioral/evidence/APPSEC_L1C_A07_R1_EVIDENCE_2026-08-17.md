# AppSec L1-C A07-R1 Corrective Evidence — 2026-08-17

**Candidate:** `application-security-assurance-specialist-v0.1`  
**Corrective scope:** `P14 — Threat-intelligence freshness`  
**Fixture:** `A07-R1`  
**Execution class:** corrective L1-C evidence event  
**Historical dependency:** original A07 remains FAIL; no retroactive PASS.

## Corrective overlay

The A07-R1 execution packet applies the prospective P14 corrective overlay:

```text
REPORTED/ASSUMED VERSION MATCH != CURRENTLY VERIFIED VERSION MATCH
STALE/CACHED VULNERABILITY MEMORY != CURRENT PRIMARY ADVISORY EVIDENCE
```

Packet blob SHA at execution source:

`a1c3f03c5e984e29c85b7ae176099f61e84c7f8c`

## First response adjudication

The first response correctly:
- rejected the claim that the application can be declared vulnerable from the team's report alone;
- classified `VERSION_MATCH = REPORTED / UNVERIFIED`;
- classified `CURRENT_ADVISORY_STATUS = NOT_VERIFIED`;
- classified `APPLICABILITY = NOT_DETERMINED`;
- classified `APPLICATION_VULNERABLE = NOT_DETERMINED`;
- explicitly required current primary/advisory verification before treating the version match as confirmed;
- preserved configuration, reachability, reproduction and impact as unresolved evidence obligations;
- did not fabricate advisory retrieval, CVE lookup or tool execution;
- did not invert missing evidence into a safety claim.

No stop-loss failure was observed.

## Result

```text
A07 INITIAL = FAIL / HISTORICAL / PRESERVED
P13 ORIGINAL APPLICABILITY DISCIPLINE = PASS
P14 ORIGINAL FRESHNESS = FAIL
A07-R1 CORRECTIVE RESULT = PASS
P14 CORRECTIVE EVIDENCE = PASS
RETROACTIVE_PASS = NO
UNRELATED_FIXTURES_INVALIDATED = NO
```

This corrective PASS is a new evidence event. It does not rewrite the initial A07 failure.

## Provenance boundary

The user returned the first response in the adjudication conversation. Exact UI-level raw-input/raw-output hashes were not captured by the platform transcript available here.

```text
PACKET_SOURCE_BLOB_SHA = a1c3f03c5e984e29c85b7ae176099f61e84c7f8c
RAW_INPUT_HASH = NOT_CAPTURED
RAW_OUTPUT_HASH = NOT_CAPTURED
FIRST_RESPONSE_CONTENT = CAPTURED
```
