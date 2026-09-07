# SES — Evidence & Provenance Admission Contract

**Status:** FOUNDATION_V0_1 / CORE_PROTOCOL

## 1. Purpose

Define reusable SES Core semantics for deciding what project evidence and provenance must become durable, what raw/source material is merely eligible for repository admission, and what conversational or duplicative material should not be versioned by default.

The contract protects both failure modes:

```text
EVIDENCE LOSS
!=
DOCUMENTATION LANDFILL
```

Its primary invariant is:

```text
A SES-compatible project must preserve enough durable,
decision-grade evidence to reconstruct material state and decisions
without depending on conversation history,

AND

raw conversational/source material must not be versioned
merely because it existed.
```

SES standardizes evidence/provenance semantics. The consumer project owns its actual project truth, evidence, retention decisions, locations, authority and sensitive-data policy.

## 2. Architectural boundary

```text
SES CORE
= reusable admission / provenance / durability semantics

CONSUMER PROJECT
= project truth + project evidence + authority
  + retention/legal/privacy/security rules
  + concrete storage/layout
```

Preserve:

```text
PROJECT OWNS PROJECT TRUTH
SES OWNS REUSABLE SEMANTICS

STANDARDIZE SEMANTICS
!=
STANDARDIZE DOCUMENT VOLUME

REFERENCE IMPLEMENTATION
!=
UNIVERSAL AUTHORITY
```

This contract does not require a specific evidence directory, manifest shape, number of files, retention period, hash algorithm or project-specific verdict taxonomy.

## 3. Conversation and memory boundary

```text
CONVERSATION != CANONICAL PROJECT EVIDENCE
MEMORY != DURABLE PROVENANCE
COPIED CONTEXT != LIVE EVIDENCE
```

Conversation content may contain material source information, decisions or evidence. Its existence in a chat is not itself a reason to version the conversation.

When a material accepted decision exists only in conversation or another non-durable surface, the project has a durability/provenance gap until the material meaning is preserved in a project-owned durable source.

The correction is to preserve the decision-grade meaning and necessary provenance, not to archive the entire conversation by default.

## 4. Decision reconstructibility

When applicable, durable project-owned sources must preserve enough information for a later conversation or specialist to reconstruct:

```text
WHAT WAS DECIDED
WHY IT WAS ACCEPTED
MATERIAL SOURCE / EVIDENCE BOUNDARY
AUTHORITY / AUTHORIZATION PROVENANCE
RESIDUAL RISK / LIMITATIONS
SUPERSEDED STATE WHEN MATERIAL
INVALIDATION CONDITIONS
SEMANTIC NEXT MATERIAL ACTION
```

Not every project or decision requires every field. The proof obligation is proportional to decision materiality, risk and project complexity.

A project may satisfy reconstructibility with one compact artifact or multiple ledgers. Reconstructibility does not require raw-source forensic reproduction when the accepted material decision can be independently reconstructed from durable evidence and the raw source adds no unique decision-grade value.

```text
CURRENT DECISION RECONSTRUCTIBILITY
!=
RAW SOURCE FORENSIC REPRODUCIBILITY
```

## 5. Evidence admission decision

Before versioning raw/source material, evaluate whether repository admission is justified.

Raw/source material is **eligible for admission** only when the applicable conditions are satisfied:

1. **DECISION-GRADE** — it contains material evidence needed for a real claim, decision, audit, lifecycle or continuity obligation.
2. **UNIQUE VALUE** — the material evidence is not already preserved equivalently by a durable project-owned artifact.
3. **PROVENANCE-BOUND** — source/object/ref/version/time/fingerprint is bound strongly enough for the actual proof obligation, or any historical limitation is explicitly recorded.
4. **SANITIZED / POLICY-COMPLIANT** — project-local secret, PII, legal, privacy, security and retention requirements are satisfied before admission.
5. **BOUNDED** — the material maps to an identified evidence or decision obligation rather than an undefined archival desire.
6. **NON-DUPLICATIVE** — admission does not create a redundant competing authority.
7. **PROJECT-OWNED** — the consumer project remains the owner of its evidence and decides the concrete durable surface under its own authority.

Eligibility does not itself authorize a mutation.

```text
ELIGIBLE_FOR_ADMISSION
!=
AUTHORIZED_TO_VERSION

TOOL_CAPABILITY
!=
AUTHORIZATION
```

## 6. Do not version by default

The following classes are normally non-probative or duplicative and therefore should not be versioned merely because they exist:

- greetings, salutations and conversational filler;
- duplicate prompts or restatements of an already durable contract;
- assistant chain-of-thought/reasoning or conversational explanation that is not itself an authoritative project record;
- tool chatter or routine transport logs with no unique proof value;
- duplicate handoffs or repeated status messages;
- superseded intermediate drafts whose material final state is durably preserved;
- redundant screenshots when equivalent exact textual/object evidence is durably preserved;
- raw specialist packets whose material decision-grade evidence is already preserved equivalently.

This list is illustrative, not exhaustive.

A project may retain otherwise noncanonical raw material for a concrete legal, regulatory, forensic, contractual or operational requirement. That is a project-local policy decision and must not silently convert the material into canonical project truth.

## 7. Durable summary versus raw source

Prefer the smallest durable artifact that satisfies the proof obligation.

```text
UNIQUE MATERIAL SOURCE NEEDED FOR PROOF
→ RAW/SOURCE ADMISSION MAY BE JUSTIFIED

MATERIAL MEANING FULLY PRESERVED EQUIVALENTLY
→ RAW DUPLICATE IS NOT REQUIRED

NO DECISION-GRADE VALUE
→ DO_NOT_VERSION_BY_DEFAULT
```

A durable summary must not overclaim what the omitted raw material proved. If omitting the raw source prevents reproduction of a material claim, either admit sufficient source evidence or classify the remaining proof limitation explicitly.

## 8. Historical integrity

Missing historical provenance must remain missing unless independently established.

```text
MISSING HISTORICAL PROVENANCE
!=
AUTOMATIC HISTORICAL GATE FAILURE

MISSING HISTORICAL PROVENANCE
!=
PERMISSION TO FABRICATE RETROACTIVE EXACTNESS
```

Later-recovered material may be recorded with its actual provenance class, but must not be relabeled as the exact historical source unless exact equivalence is independently proven.

Do not rewrite prior accepted/failed states solely to make provenance look cleaner.

## 9. Publication and anti-loop semantics

Prefer self-resolving publication semantics when canonicality can be derived objectively.

If an artifact's authority rule is equivalent to:

```text
artifact exists on the resolved canonical project ref
→ artifact is canonical
```

then a follow-up documentation mutation must not be required solely to replace a lifecycle label such as `candidate` with `merged` when no material semantic state changed.

```text
LIFECYCLE-ONLY EVENT
+ NO MATERIAL SEMANTIC CHANGE
→ NO RECURSIVE DOCUMENTATION RECONCILIATION
```

A lifecycle update remains justified when the lifecycle fact itself is material to a decision, proof obligation, authorization, compliance record or continuity state.

## 10. Project isolation

Evidence is project-scoped unless an explicit cross-project evidence contract says otherwise.

```text
PROJECT_A EVIDENCE
!=
PROJECT_B TRUTH
```

A project switch invalidates any assumption that prior project-scoped evidence, authority, retention rules, privacy rules, continuity or verdict semantics carry forward.

Reference implementations may inform SES design, but their project-specific facts and document volume do not transfer into other projects.

## 11. Proportionality

A low-complexity project must satisfy the same semantic obligations without copying the documentation volume of a large or regulated project.

Examples:

```text
SMALL PROJECT
→ compact bootstrap + compact decisions/current-state artifact
  may be sufficient

HIGH-RISK PROJECT
→ richer evidence, authority, freshness and provenance surfaces
  may be required
```

The obligation is decision-grade durability and bounded provenance, not ceremony.

## 12. Inheritance and adoption

### 12.1 New SES-compatible projects

A newly registered SES-compatible project must implement project-owned bootstrap/continuity/evidence behavior compatible with this contract.

It does not need to copy this file. Inheritance occurs through SES Core bootstrap semantics and the Project Bootstrap Contract.

### 12.2 Existing registered projects

```text
SES MAIN ADVANCES
!=
AUTOMATIC CONSUMER PROJECT MUTATION
```

Existing projects are not automatically rewritten when this contract evolves.

When an existing project next performs materially relevant bootstrap/continuity/evidence work, review compatibility proportionally. Mutate the consumer project only when a real gap is found and separate project-local authority authorizes that mutation.

A compatible existing project may require no project-side change.

## 13. Relationship to other SES contracts

- `PROJECT_BOOTSTRAP_CONTRACT.md` requires projects to expose compatible evidence rules and reconstructible entrypoints.
- `PROJECT_CONTINUITY_CONTRACT.md` preserves durable operational meaning and must not become a conversation archive.
- `EVIDENCE_RETRIEVAL_RESILIENCE_CONTRACT.md` governs how evidence is retrieved and how coverage is classified; retrieval does not decide admission.
- `HYBRID_SPECIALIST_BOOTSTRAP_CONTRACT.md` governs project/context resolution and exact evidence binding; readiness does not authorize admission.
- `Documentation Auditor` applies SES Core evidence primitives to provenance, coverage, contradiction and reconstructibility, but does not become the owner or automatic scribe of project evidence.

```text
RETRIEVED
!=
ADMITTED

AUDITED
!=
OWNED_BY_AUDITOR

ELIGIBLE
!=
AUTHORIZED
```

## 14. Fail-closed outcomes

When material, use bounded states such as:

- `PROVENANCE_DURABILITY_GAP` — required material meaning is not durably reconstructible;
- `ADMISSION_NOT_JUSTIFIED` — proposed raw/versioned material lacks a bounded decision-grade reason;
- `PROVENANCE_LIMITATION` — exact source provenance is incomplete and must remain qualified;
- `PROJECT_POLICY_REQUIRED` — project-local sensitive-data/retention policy is required before admission.

These states do not create a universal project verdict taxonomy. Consumer-project canonical vocabulary remains authoritative where defined.

## 15. Acceptance criteria

A conforming use of this contract must preserve all of the following:

1. material accepted decisions are reconstructible without hidden conversation history;
2. conversation existence alone never justifies repository admission;
3. unique decision-grade raw evidence can be admitted when provenance, sensitivity, boundary and duplication checks are satisfied;
4. duplicate/non-probative raw material is not versioned by default;
5. historical provenance gaps are not fabricated away;
6. small projects satisfy semantics without large-project documentation volume;
7. evidence never silently crosses project ownership boundaries;
8. lifecycle-only canonicalization does not create recursive documentation churn;
9. SES defines semantics while consumer projects own their actual evidence and authority;
10. admission eligibility never grants mutation authority.

Normative behavioral cases are defined in:

`tests/behavioral/EVIDENCE_PROVENANCE_ADMISSION_TESTS.md`
