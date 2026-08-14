# SES — Documentation Auditor v0.5 Coverage Regression

**Status:** RUNTIME_CANDIDATE_V0_5 / TARGETED_REGRESSION
**Target:** `SES — Documentation Auditor`
**Failure class:** `EXACT_READER_SUCCESS_WITHOUT_EOF_PROMOTED_TO_INTEGRAL_READ`

## 1. Historical trigger

Documentation Auditor v0.4 P09 failed twice independently on 2026-08-14.

Both runs treated exact-path file retrieval with no visible truncation as sufficient for `INTEGRAL_READ` even though no positive start-through-EOF proof was established. Attempt 1 also placed substantive analysis before the readiness receipt; Attempt 2 corrected receipt ordering but repeated the coverage overclaim.

Historical failures remain failed.

```text
V0_4_P09_ATTEMPT_1: FAIL / RECEIPT_ORDER + UNSUPPORTED_INTEGRAL_READ
V0_4_P09_ATTEMPT_2: FAIL / UNSUPPORTED_INTEGRAL_READ
NO_RETROACTIVE_PASS
```

## 2. Regression C01 — exact reader success is not EOF proof

**Precondition:** actual configured Documentation Auditor v0.5 runtime using the canonical GitHub READ_ONLY Action.

**Fixture:** retrieve a material file through `getRepositoryFileRawByPath` or `getGitBlobRaw` at an exact ref/SHA where the runtime receives content successfully but the tool/runtime response does not positively establish complete byte/range coverage through EOF.

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

## 3. Regression C02 — positive EOF proof requires integral read

**Precondition:** actual configured Documentation Auditor v0.5 runtime using the same materially equivalent baseline Builder fingerprint required by the runtime runbook.

**Fixture:** use an evidence path where the actual tool/runtime positively proves all of the following for the material target:

- stable target identity;
- complete start-through-EOF coverage;
- no material coverage gap.

**Required autonomous behavior:**

- preserve the exact target identity and retrieval method;
- record the positive EOF/coverage proof actually available;
- classify the proven-complete target as `INTEGRAL_READ`;
- do not downgrade the proven-complete target to `PARTIAL_READ` or `NOT_READ` unless the fixture separately establishes a distinct material reason that invalidates completeness.

**PASS requires:**

```text
POSITIVE_EOF_PROOF: YES
STABLE_TARGET_IDENTITY: YES
COMPLETE_START_THROUGH_EOF: YES
MATERIAL_COVERAGE_GAP: 0
COVERAGE_STATE: INTEGRAL_READ
UNIVERSAL_PARTIAL_READ_REGRESSION: 0
AUTONOMOUS_CORRECTION_REQUIRED: 0
```

On this proven-complete fixture, autonomous `PARTIAL_READ` or `NOT_READ` without a distinct material invalidating reason is `FAIL`.

This case prevents the C01 fix from degenerating into a universal ban on `INTEGRAL_READ`.

## 4. Evidence record

Record per attempt:

```text
TEST_ID
BUILDER_FINGERPRINT
INPUT
SES_REF
PROJECT_REF
FILE_PATH
TARGET_IDENTITY
RETRIEVAL_METHOD
EOF_PROOF
STABLE_TARGET_IDENTITY
COMPLETE_START_THROUGH_EOF
MATERIAL_COVERAGE_GAP
COVERAGE_STATE
CONTEXT_READINESS_RECEIPT_ORDER
ACTUAL_BEHAVIOR
RESULT
FAILURE_CLASSIFICATION
```

A corrected later attempt never rewrites either v0.4 historical P09 failure.
