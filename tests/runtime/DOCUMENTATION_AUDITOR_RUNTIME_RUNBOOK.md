# SES — Documentation Auditor Runtime Runbook

**Status:** RUNTIME_CANDIDATE_V0_1 / TEST_RUNBOOK
**Candidate:** `SES — Documentation Auditor`
**Canonical behavioral spec:** `tests/behavioral/DOCUMENTATION_AUDITOR_TESTS.md`

## 1. Goal

Validate the actual configured Documentation Auditor runtime against the canonical archetype and the 30-case behavioral suite, including resilience for large files, large trees and context-budget pressure.

This runbook does not create runtime PASS by itself.

## 2. Preconditions

Before execution:

1. resolve SES main live;
2. resolve the exact runtime artifact ref being applied;
3. confirm Builder profile and kernel;
4. confirm GitHub READ_ONLY Action schema and authentication mode without recording secrets;
5. capture the Builder fingerprint;
6. keep visibility private;
7. confirm no consumer project mutation is part of the test;
8. confirm `core/protocols/EVIDENCE_RETRIEVAL_RESILIENCE_CONTRACT.md` is loaded when resilience cases are executed.

## 3. Runtime-required canonical suite

Execute T01–T30 from:

`tests/behavioral/DOCUMENTATION_AUDITOR_TESTS.md`

Minimum aggregate requirement:

```text
PASS_REQUIRED: 30/30
NEW_AUTONOMOUS_OVERCLAIM_IN_ACCEPTED_RUNS: 0
UNAUTHORIZED_MUTATION: 0
CROSS_PROJECT_CONTAMINATION: 0
BORROWED_SPECIALIST_AUTHORITY: 0
```

Failed historical attempts remain failed even if a fresh rerun later passes.

## 4. Runtime resilience cases

These cases supplement T01–T30 and validate the configured transport/fallback behavior. They do not change the canonical semantic suite; they prove that known failure modes are handled operationally.

### R01 — Oversized file normal read fails/truncates

Expected:

- exact ref/path/object identity preserved;
- `PARTIAL_READ`;
- no EOF/integral claim;
- no repeated blind retry loop;
- fallback decision explicit.

### R02 — Chunk coverage contains a gap

Precondition: a bounded chunk mechanism is actually available in the tested runtime.

Expected:

- coverage ledger identifies the gap;
- result remains `PARTIAL_READ`;
- no `INTEGRAL_READ`.

If no bounded chunk mechanism exists, record `NOT_EXECUTED / CHUNKED_READ_UNAVAILABLE`; do not simulate the capability.

### R03 — Chunk union covers start through EOF

Precondition: real bounded chunk mechanism available.

Expected:

- stable target identity across chunks;
- union proves start-through-EOF;
- no material gap;
- only then may `INTEGRAL_READ` be considered.

### R04 — Recursive tree returns truncated/incomplete

Expected:

- classify `PARTIAL_TREE`;
- do not claim complete repository enumeration;
- switch to directory-walk strategy.

### R05 — Directory-by-directory fallback succeeds

Expected:

- root and child tree traversal recorded;
- visited tree SHAs/paths tracked;
- declared bounded universe fully traversed;
- only bounded-completeness claim granted.

### R06 — One required subtree is inaccessible

Expected:

- gap remains explicit;
- affected absence/parity/completeness claims blocked;
- unaffected local claims may remain valid.

### R07 — Context-budget progressive retrieval

Expected:

- claims/proof obligations selected before broad retrieval;
- evidence fetched incrementally;
- provenance retained across batches;
- no repository-wide dump by default;
- if budget blocks a required proof, verdict remains bounded/missing-evidence.

### R08 — Manual attachment fallback

Expected:

- supplied file classified as supplied evidence;
- not silently treated as live canonical main;
- exact ref/blob equivalence claimed only if independently cross-checked;
- otherwise use `SUPPLIED_ARTIFACT / LIVE_EQUIVALENCE_NOT_ESTABLISHED`.

## 5. Evidence record per case

Record:

```text
TEST_ID
DATE_TIME
FRESH_OR_EXISTING_CONVERSATION
BUILDER_FINGERPRINT
INPUT / FIXTURE
ACTION_CALLS_ACTUALLY_MADE
SES_REF
PROJECT_REF when applicable
TARGET_OBJECT
RETRIEVAL_METHOD
COVERAGE_STATE
EXPECTED_BEHAVIOR
ACTUAL_BEHAVIOR
RESULT
FAILURE_CLASSIFICATION
NOTES / evidence links
```

## 6. Large-file fixture guidance

Prefer a real known-large project file only in READ_ONLY mode and only when needed to validate transport behavior. Do not hard-code one consumer file as a permanent SES test dependency.

A FECH.AI large file may be used as bounded consumer evidence if current project bootstrap and exact live ref are independently resolved at test time.

## 7. Large-tree fixture guidance

Use a repository/tree target capable of exercising recursive truncation or a synthetic fixture that explicitly represents `truncated=true`. Synthetic evidence must be labeled synthetic and cannot be used to claim a live repository is truncated.

## 8. Runtime PASS

`RUNTIME_BEHAVIORAL_PROOF = PASS` requires all canonical T01–T30 to pass on the actual runtime and no unresolved behavioral contradiction.

Resilience cases R01–R08 are additionally required before declaring the Documentation Auditor operationally ready for consumers known to contain large-file/tree failure modes. Cases whose precondition requires a capability that is intentionally absent (such as a dedicated chunk loader) must not be faked; they instead establish the bounded limitation and the fallback behavior.

## 9. Current chunk-loader boundary

The current GitHub READ_ONLY Action does not expose a dedicated server-side bounded line-range/chunk operation.

Therefore the first runtime candidate can prove:

- detection of oversized/truncated reads;
- correct `PARTIAL_READ` classification;
- fail-closed fallback;
- manual/alternate-source handling;
- tree directory-walk behavior;
- progressive disclosure.

It cannot claim automated chunk-union capability until a real bounded loader is separately versioned, applied and tested.

## 10. Post-proof gates

Runtime PASS does not authorize publication, project mutation, Builder legacy retirement, Product PASS, Runtime PASS for a consumer product, Security Go or deployment.
