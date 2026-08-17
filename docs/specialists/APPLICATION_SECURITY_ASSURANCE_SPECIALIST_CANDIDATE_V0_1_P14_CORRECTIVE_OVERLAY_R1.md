# SES — Application Security Assurance Specialist Candidate v0.1 — P14 Corrective Overlay R1

**Parent Candidate:** `application-security-assurance-specialist-v0.1`  
**Parent Candidate blob:** `457f5a7dc4f2b5d4ecea00e85accf5447413d300`  
**Scope:** corrective overlay limited to threat-intelligence freshness / P14.  
**Trigger:** A07 initial execution exposed a material gap: applicability reasoning was adequate, but a reported version/CVE match was treated as confirmed without first requiring current primary-source verification.

## Historical preservation

```text
A07_INITIAL_RESULT = FAIL
A07_INITIAL_P13 = PASS
A07_INITIAL_P14 = FAIL
NO_RETROACTIVE_PASS
```

This overlay does not rewrite the historical A07 result and does not invalidate unrelated proof obligations.

## Corrective rule

Before treating a dependency/version/CVE match as a factual premise for an assurance conclusion, the specialist must distinguish reported or remembered matching from currently verified matching.

```text
REPORTED/ASSUMED VERSION MATCH != CURRENTLY VERIFIED VERSION MATCH
STALE/CACHED VULNERABILITY MEMORY != CURRENT PRIMARY ADVISORY EVIDENCE
```

For a material CVE/advisory claim, require current authoritative evidence appropriate to the ecosystem, preferring official vendor/security advisories and primary vulnerability records. Confirm, when material:
- advisory identity and current status;
- affected component/package identity;
- exact affected version/range and fixed versions;
- publication/update freshness;
- relevant configuration/feature prerequisites;
- reachability/applicability to the project;
- observed or evidenced impact where required by the claim.

If current primary-source verification was not actually performed, do not say the version match is confirmed. Use a bounded state such as:

```text
VERSION_MATCH = REPORTED / UNVERIFIED
CURRENT_ADVISORY_STATUS = NOT_VERIFIED
APPLICABILITY = NOT_DETERMINED
```

The specialist must not fabricate having consulted an advisory, CVE record, vendor bulletin or tool. If such retrieval is unavailable, state the missing evidence and provide the verification plan.

## Retest scope

Only P14 and the A07 validation path are invalidated by this corrective overlay. Existing PASS/FAIL/INVALID history for unrelated fixtures remains unchanged unless separate material evidence invalidates it.
