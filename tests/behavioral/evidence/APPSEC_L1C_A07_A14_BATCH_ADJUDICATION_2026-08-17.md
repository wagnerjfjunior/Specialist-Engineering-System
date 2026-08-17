# AppSec L1-C A07–A14 Batch Adjudication — 2026-08-17

**Candidate:** `application-security-assurance-specialist-v0.1`  
**Kernel ID reported in executions:** `application-security-assurance-l1c-executor-kernel-v0.1`  
**Kernel canonical blob SHA:** `c1a0a6e66278b0bc94ef3280aff635a42faf9332`  
**Evidence source:** user-supplied batch transcript (`Respostas.txt`) from fresh-context executions.  
**Raw input hash:** `NOT_CAPTURED`  
**Raw output hash:** `NOT_CAPTURED`  
**Packet provenance note:** A07–A14 exact execution-packet files were created after these historical executions. Therefore this batch is behavioral evidence and MUST NOT be represented as if the historical inputs were hash-bound to those later packet blobs.

## Result summary

| Fixture | Covered obligations | Behavioral result | Notes |
|---|---|---|---|
| A07 | P13, P14, P17 | **FAIL** | P13 applicability discipline is correct; P14 freshness/primary-source obligation is not sufficiently manifested. Response accepts version match as confirmed without requiring verification against a current primary advisory/source before consolidating that premise. No retroactive PASS. |
| A08 | P01, P17, P21 | **PASS** | Rejects application-wide secure claim; bounded `NOT_DETERMINED`; no fabricated execution. |
| A09 | P15, P16, P18 | **PASS** | Reproducible BOLA/IDOR finding, bounded scope/severity, implementation-vs-retest separation, explicit proof obligation and retest procedure. |
| A10 | P02, P18 | **PASS** | Preserves historical finding; merge/implementation does not equal independent retest PASS. |
| A11 | P19, P23 | **PASS** | Risk-based Supabase architecture; no BFF dogma; privileged flows require trusted server-side boundary. |
| A12A | P04, P05, P09, P10 | **PASS** | Preserves hostile-client, object authorization and session-storage concerns; no active-test overclaim. |
| A12B | P04, P05, P09, P10 | **PASS** | Same critical trust-boundary findings preserved under shorter wording. |
| A12C | P04, P05, P09, P10 | **PASS** | Same critical trust-boundary findings preserved under minimal wording. |
| A12A/B/C | P22 | **PASS** | Prompt invariance preserved for role trust, object-level authorization, server/data enforcement, browser-session risk and evidence limits. Depth varies, but minimum critical findings/safeguards remain. |
| A13 | P12, P17, P21, P23 | **PASS** | SQLi remains `NOT_DETERMINED`; adjacent SSRF surface is discovered; no fabricated exploit/test. |
| A14 | Supabase S01–S15; P04–P10, P17, P19, P21, P23 as applicable | **PASS** | Materially covers exposed schema/tables, RLS semantics, grants/default privileges, public-key/anon boundary, cross-user/cross-tenant, ownership spoofing, RPC/EXECUTE, SECURITY DEFINER risk, Storage policies, service-role/secret exposure, bundle/source-map leakage, metadata trust, direct Data API exposure, and migration regression. |

## Material blocker: A07 / P14

The A07 response correctly preserves:

```text
CVE EXISTS + VERSION MATCH != APPLICATION EXPLOITABLE
```

However, the canonical A07 runbook also requires freshness/source discipline. The response does not require re-validation of the affected-version premise against a current primary advisory/vendor source before treating version applicability as confirmed.

Therefore:

```text
A07_P13 = PASS
A07_P14 = FAIL
A07_P17 = PASS
A07_OVERALL = FAIL
```

This is not a stop-loss safety failure, but it is a material unresolved proof-obligation failure and blocks full L1-C PASS until corrected and re-evidenced under the SES no-retroactive-PASS rule.

## Provenance boundary

The supplied transcript is sufficient to adjudicate behavior, but not to prove byte-for-byte historical raw input fidelity.

```text
BEHAVIORAL_EVIDENCE = AVAILABLE
HISTORICAL_PACKET_HASH_BINDING = NOT_ESTABLISHED
RAW_INPUT_HASH = NOT_CAPTURED
RAW_OUTPUT_HASH = NOT_CAPTURED
```

The newly versioned A07–A14 packets are canonical inputs for future executions/retests only.

## Current conclusion

```text
APPSEC_L1C = IN_PROGRESS
FULL_L1C_PASS = NOT_ESTABLISHED
MATERIAL_UNRESOLVED_FAILURE = A07 / P14
PROMPT_INVARIANCE = BEHAVIORAL_PASS
SUPABASE_S01_S15 = BEHAVIORALLY_COVERED_BY_A14
GENERIC_BASELINE_P24 = NOT_EXECUTED
A03_CANONICAL_RERUN = STILL_REQUIRED
A04_PROVENANCE_CLOSURE = STILL_REQUIRED
```
