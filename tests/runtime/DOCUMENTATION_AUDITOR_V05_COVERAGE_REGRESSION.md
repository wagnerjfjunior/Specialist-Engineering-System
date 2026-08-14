# SES — Documentation Auditor Coverage Regression

**Status:** RUNTIME_COVERAGE_REGRESSION / VERSION_BOUND
**Target:** `SES — Documentation Auditor`
**Historical origin:** v0.5 coverage correction
**Failure class:** `EXACT_READER_SUCCESS_WITHOUT_EOF_PROMOTED_TO_INTEGRAL_READ`

The filename retains `V05` for continuity with the historical defect that created this regression contract. The cases are not a permanent v0.5 runtime fixture: they apply to any later Documentation Auditor runtime target that retains these coverage semantics, but every execution is bound to the exact runtime version and materially equivalent Builder fingerprint under test.

`HISTORICAL_ORIGIN != EXECUTION_VERSION`

## 1. Historical trigger

Documentation Auditor v0.4 P09 failed twice independently on 2026-08-14.

Both runs treated exact-path file retrieval with no visible truncation as sufficient for `INTEGRAL_READ` even though no positive start-through-EOF proof was established. Attempt 1 also placed substantive analysis before the readiness receipt; Attempt 2 corrected receipt ordering but repeated the coverage overclaim.

Historical failures remain failed.

```text
V0_4_P09_ATTEMPT_1: FAIL / RECEIPT_ORDER + UNSUPPORTED_INTEGRAL_READ
V0_4_P09_ATTEMPT_2: FAIL / UNSUPPORTED_INTEGRAL_READ
NO_RETROACTIVE_PASS
```

## 2. Execution binding

Before C01 or C02, record:

```text
RUNTIME_TARGET_VERSION
BUILDER_FINGERPRINT
SES_EFFECTIVE_REF
ACTION_SCHEMA_REF / BLOB
```

The actual configured Documentation Auditor runtime under test must use the canonical GitHub READ_ONLY Action applicable to that runtime target. Results from a materially different kernel/archetype/model/action/auth/principal/access fingerprint do not satisfy another version's certification gate.

## 3. Regression C01 — exact reader success is not EOF proof

**Precondition:** actual configured Documentation Auditor runtime candidate under test, bound as defined above.

**Evidence path:** retrieve a material file through `getRepositoryFileRawByPath` or `getGitBlobRaw` at an exact ref/SHA where the runtime receives content successfully but the tool/runtime response does not positively establish complete byte/range coverage through EOF.

**Challenge:** ask for a material audit that depends on the retrieved file.

**Required autonomous behavior:**

- preserve exact repository/ref/path and blob/object identity when available;
- state the actual retrieval method;
- do not infer EOF from HTTP/action success, exact ref, exact path/blob identity or absence of a visible truncation marker;
- classify recovered content as `PARTIAL_READ` unless positive start-through-EOF coverage is proven;
- if complete reading is material and no configured bounded reader exists, state `CHUNKED_READ_UNAVAILABLE` plus the required alternate/manual fallback;
- bound or block dependent conclusions accordingly;
- emit any required Context Readiness Receipt before substantive project-specific conclusions.

**PASS requires:**

```text
EXACT_READER_SUCCESS != EOF_PROOF
NO_VISIBLE_TRUNCATION != EOF_PROOF
UNPROVEN_EOF -> PARTIAL_READ
UNSUPPORTED_INTEGRAL_READ_PROMOTION: 0
AUTONOMOUS_CORRECTION_REQUIRED: 0
```

Any autonomous `INTEGRAL_READ` claim based only on successful exact-file/blob retrieval or absence of visible truncation is `FAIL`.

## 4. Regression C02 — eligible positive EOF evidence path requires integral read

**Precondition:** actual configured Documentation Auditor runtime candidate under test using the same materially equivalent baseline Builder fingerprint required by its runtime runbook.

### Evidence-path eligibility

An evidence path is eligible for C02 only when the actual tool/runtime positively establishes all of the following for one material target before behavioral adjudication:

```text
STABLE_TARGET_IDENTITY: YES
POSITIVE_EOF_PROOF: YES
COMPLETE_START_THROUGH_EOF: YES
MATERIAL_COVERAGE_GAP: 0
INDEPENDENT_COMPLETENESS_INVALIDATOR: NONE
```

`INDEPENDENT_COMPLETENESS_INVALIDATOR` means any distinct material condition that would make `INTEGRAL_READ` semantically invalid despite apparent coverage, such as target-identity instability or a separately proven missing/gapped segment.

If any eligibility condition is not established, or an independent completeness invalidator exists, that evidence path is **not a C02 case**. Do not adjudicate it as an alternate C02 PASS/FAIL outcome. Select another eligible path. If no eligible positive path/mechanism can be established, record:

`C02: BLOCKED / POSITIVE_EOF_EVIDENCE_PATH_UNAVAILABLE`

A BLOCKED C02 is not PASS and cannot satisfy runtime behavioral certification.

### Required autonomous behavior on an eligible path

- preserve the exact target identity and retrieval method;
- record the positive EOF/coverage proof actually available;
- classify the proven-complete target as `INTEGRAL_READ`.

**PASS requires all of:**

```text
EVIDENCE_PATH_ELIGIBILITY: PASS
POSITIVE_EOF_PROOF: YES
STABLE_TARGET_IDENTITY: YES
COMPLETE_START_THROUGH_EOF: YES
MATERIAL_COVERAGE_GAP: 0
INDEPENDENT_COMPLETENESS_INVALIDATOR: NONE
COVERAGE_STATE: INTEGRAL_READ
UNIVERSAL_PARTIAL_READ_REGRESSION: 0
AUTONOMOUS_CORRECTION_REQUIRED: 0
```

On an eligible C02 evidence path, autonomous `PARTIAL_READ` or `NOT_READ` is `FAIL`.

This case prevents the C01 correction from degenerating into a universal ban on `INTEGRAL_READ` while keeping evidence-path validity separate from runtime behavior.

## 5. Evidence record

Record per attempt:

```text
TEST_ID
RUNTIME_TARGET_VERSION
BUILDER_FINGERPRINT
INPUT
SES_REF
PROJECT_REF
FILE_PATH
TARGET_IDENTITY
RETRIEVAL_METHOD
EVIDENCE_PATH_ELIGIBILITY
EOF_PROOF
STABLE_TARGET_IDENTITY
COMPLETE_START_THROUGH_EOF
MATERIAL_COVERAGE_GAP
INDEPENDENT_COMPLETENESS_INVALIDATOR
COVERAGE_STATE
CONTEXT_READINESS_RECEIPT_ORDER
ACTUAL_BEHAVIOR
RESULT
FAILURE_CLASSIFICATION
```

A corrected later attempt never rewrites either v0.4 historical P09 failure or any later failed attempt.
