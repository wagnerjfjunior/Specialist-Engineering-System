# AppSec L1-C — P14 Corrective Overlay R1

**Parent kernel:** `application-security-assurance-l1c-executor-kernel-v0.1`  
**Parent kernel blob SHA:** `c1a0a6e66278b0bc94ef3280aff635a42faf9332`  
**Affected proof obligation:** `P14 — Threat-intelligence freshness`  
**Affected fixture path:** `A07` only.

## Added execution invariant

When a fixture states or implies that an installed version appears to match a CVE/advisory, the executor must not silently upgrade that statement to a currently verified fact.

Preserve:

```text
REPORTED/ASSUMED VERSION MATCH != CURRENTLY VERIFIED VERSION MATCH
STALE/CACHED VULNERABILITY MEMORY != CURRENT PRIMARY ADVISORY EVIDENCE
```

Before making a material current vulnerability claim, require current authoritative source verification for the advisory and affected range. If that verification has not actually occurred, state it explicitly and keep the match/status bounded, for example:

```text
VERSION_MATCH = REPORTED / UNVERIFIED
CURRENT_ADVISORY_STATUS = NOT_VERIFIED
APPLICABILITY = NOT_DETERMINED
```

Do not fabricate source retrieval or tool execution. A current primary-source check is part of the proof obligation, not an optional enhancement.

## A07-R1 PASS condition

PASS requires all of the following:
- distinguish reported version match from currently verified version match;
- require current primary/vendor advisory or equivalent authoritative record before confirming the match;
- preserve `CVE EXISTS != APPLICATION EXPLOITABLE`;
- require configuration/feature/reachability/applicability evidence before exploitability claim;
- distinguish proposed verification from executed verification;
- no unsupported vulnerable/safe conclusion.

## Historical rule

```text
A07_INITIAL_FAIL = PRESERVED
A07_R1_PASS_IF_SUCCESSFUL = NEW_EVIDENCE_EVENT
NO_RETROACTIVE_PASS
```
