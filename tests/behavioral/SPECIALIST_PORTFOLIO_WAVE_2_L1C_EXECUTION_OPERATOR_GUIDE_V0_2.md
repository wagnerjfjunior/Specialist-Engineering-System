# SES — Specialist Portfolio Wave 2 L1-C Execution Operator Guide v0.2

**Branch:** `feat/specialist-portfolio-wave-2`  
**Supersedes:** `SPECIALIST_PORTFOLIO_WAVE_2_L1C_EXECUTION_OPERATOR_GUIDE_V0_1.md` prospectively only  
**Purpose:** preserve fresh-context execution while permitting neutral packet/fixture identifiers that do not reveal answer keys or adjudication criteria.

## 1. Historical preservation

This v0.2 does not rewrite prior executions or retroactively convert any historical result to PASS.

```text
V0_1_EXECUTION_HISTORY = PRESERVED
RETROACTIVE_CANONICALIZATION = PROHIBITED
```

## 2. Fresh-context rule

Each fixture must run in a fresh isolated context that has not seen the design conversation, behavioral suite, runbook adjudication criteria, expected behaviors, prior fixture outputs, corrective guidance, answer keys or scoring rules.

```text
CURRENT_DESIGN_CONTEXT != EXECUTOR_CONTEXT
FIRST RESPONSE = EVIDENTIARY UNIT
NO COACHING BEFORE CAPTURE
NO RETROACTIVE PASS
```

## 3. Executor-visible packet metadata

A neutral packet or fixture identifier MAY be visible to the executor solely for operational provenance, for example:

```text
### FIXTURE A03
PACKET_ID = APPSEC_L1C_A03_EXACT_PACKET_V0_1
```

This metadata must not disclose:
- proof-obligation identifiers;
- expected critical behavior;
- PASS/FAIL criteria;
- scoring dimensions;
- answer keys;
- prior outputs or adjudications.

Therefore:

```text
NEUTRAL FIXTURE/PACKET ID = PERMITTED
ADJUDICATION OR ANSWER-KEY LEAKAGE = PROHIBITED
```

## 4. Exact packet execution

When a hash-bound execution packet exists, the preferred procedure is:
1. start a fresh isolated context;
2. paste the exact packet unchanged;
3. submit once;
4. capture the first response verbatim before any follow-up;
5. record packet path/blob SHA and kernel ID/blob SHA;
6. record available telemetry; unavailable telemetry is `NOT CAPTURED`;
7. adjudicate only outside the executor context.

The exact packet becomes the input provenance reference. If the interface cannot provide a raw-input hash, record:

```text
RAW_INPUT_HASH = NOT_CAPTURED
PACKET_BLOB_SHA = <known Git blob SHA>
OPERATOR_ATTESTATION = packet pasted wholly and unedited, when available
```

Operator attestation does not prove byte-level UI fidelity, but it is valid provenance metadata and must not be represented as a raw-input hash.

## 5. Raw input/output preservation

Preserve the first response verbatim where technically possible. Export or chat rendering may normalize Markdown; if so, record the limitation explicitly.

```text
RAW_OUTPUT_HASH = NOT_CAPTURED
RENDERING_NORMALIZATION = OBSERVED / NOT_OBSERVED / NOT_DETERMINED
```

Do not fabricate hashes.

## 6. Generic baseline

Generic-baseline executions use fresh isolated contexts and a competent generic security role instruction, the same material facts as the paired Candidate fixture, no Candidate kernel, no Candidate output, and no adjudication criteria.

## 7. Completion boundary

This guide changes only the operational provenance rule regarding neutral packet identifiers and packet-based capture. It does not weaken behavioral proof obligations, stop-loss rules, generic-baseline requirements, prompt invariance, Supabase coverage, or L1/L2 separation.
