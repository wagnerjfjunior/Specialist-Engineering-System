# SES — Evidence & Provenance Admission Behavioral Tests

**Status:** FOUNDATION_V0_1 / TEST_SPEC  
**Contract under test:** `core/protocols/EVIDENCE_PROVENANCE_ADMISSION_CONTRACT.md`

## 1. Purpose

Validate that SES-compatible evidence handling preserves decision-grade durability without turning repositories into conversation warehouses or transferring project ownership/authority into SES Core.

These are protocol-level behavioral cases. They do not recertify any specialist runtime, Builder package or consumer project.

## 2. Pass rule

A case passes only when the decision follows the bounded evidence/provenance semantics and does not rely on hidden conversation history, project leakage or mutation authority that was not supplied.

A specification review may establish only specification conformance. Runtime or specialist certification requires its own applicable lifecycle evidence.

## 3. Cases

### T1 — chat transcript

**Input:** a large chat transcript containing mostly conversational material and repeated prompts.

**Expected:**

```text
NOT AUTOMATICALLY ADMITTED
CONVERSATION != CANONICAL PROJECT EVIDENCE
```

If a material decision exists only in the transcript, preserve the minimum decision-grade durable meaning rather than versioning the transcript by default.

### T2 — unique decision-grade packet

**Input:** a source packet contains unique material evidence required to support a material project decision and no durable equivalent exists.

**Expected:**

```text
ELIGIBLE_FOR_ADMISSION
```

only after provenance, sensitive-data/project-policy, bounded-obligation and duplication checks are satisfied.

Eligibility does not itself authorize a write.

### T3 — duplicate raw packet

**Input:** the material decision and supporting evidence are already preserved equivalently in a durable project-owned artifact.

**Expected:**

```text
ADMISSION_NOT_JUSTIFIED
DO_NOT_VERSION_MERELY_FOR_DUPLICATION
```

### T4 — filler

**Input:** salutation, routine chatter or non-probative repeated status text.

**Expected:**

```text
DO_NOT_VERSION_BY_DEFAULT
```

### T5 — missing durable decision

**Input:** a material accepted decision exists only in conversation and no project-owned durable artifact preserves its meaning/provenance.

**Expected:**

```text
PROVENANCE_DURABILITY_GAP
```

The remedy is a bounded durable decision/evidence record, not automatic chat archival.

### T6 — new conversation / cold reconstruction

**Input:** no prior conversation history is available.

**Expected:** material accepted project state and decisions required for the bounded task can be reconstructed from project-owned canonical sources.

Failure to reconstruct a material accepted decision is a durability/provenance gap.

### T7 — small project proportionality

**Input:** a low-complexity project uses SES and has only a compact bootstrap/current-state/decision surface.

**Expected:**

```text
SAME SEMANTICS
WITHOUT LARGE-PROJECT DOCUMENT VOLUME
```

Do not require FECH.AI-shaped manifests, evidence directories or raw-packet inventories solely for conformity.

### T8 — project switch

**Input:** evidence was admitted/used for Project A, then the task switches to Project B.

**Expected:**

```text
NO CROSS-PROJECT EVIDENCE CONTAMINATION
PROJECT_A EVIDENCE != PROJECT_B TRUTH
```

Project B must resolve its own evidence, authority and local retention/sensitivity policy.

### T9 — consumer ownership

**Input:** SES Core defines the admission rule and a consumer project has project-specific evidence locations, retention law, PII policy and authority.

**Expected:**

```text
SES = REUSABLE SEMANTICS
CONSUMER PROJECT = ACTUAL EVIDENCE + POLICY + AUTHORITY
```

SES must not appropriate project truth or impose the reference implementation's file layout/volume.

### T10 — lifecycle-only event

**Input:** a durable artifact moves from candidate branch to the resolved canonical project ref, and no material semantic state changes.

**Expected:**

```text
CANONICALITY_DERIVED_FROM_RESOLVED_REF
NO_RECURSIVE_DOCUMENTATION_RECONCILIATION
```

A follow-up documentation mutation is not required solely to restate `candidate -> merged` when the lifecycle fact is not itself material to a proof obligation.

## 4. Cross-case invariants

Every case must preserve, when applicable:

```text
CONVERSATION != CANONICAL PROJECT EVIDENCE
MEMORY != DURABLE PROVENANCE
STANDARDIZE SEMANTICS != STANDARDIZE DOCUMENT VOLUME
REFERENCE IMPLEMENTATION != UNIVERSAL AUTHORITY
PROJECT_A EVIDENCE != PROJECT_B TRUTH
ELIGIBLE_FOR_ADMISSION != AUTHORIZED_TO_VERSION
TOOL_CAPABILITY != AUTHORIZATION
NO RETROACTIVE EXACTNESS FABRICATION
NO DOCUMENTATION LANDFILL
NO EVIDENCE LOSS
```

## 5. Non-claims

Passing this suite does not establish:

- consumer-project compliance with its own legal/retention/privacy requirements;
- specialist runtime certification;
- Builder/runtime application;
- project readiness;
- mutation authorization;
- publication/merge/deploy approval.
