# SES — Project Bootstrap Contract

**Status:** FOUNDATION_V0_1 / CONTRACT

## 1. Purpose

Every SES-compatible consumer project must expose a project-owned bootstrap entrypoint that allows a specialist or new conversation to reconstruct enough current context to work safely without relying on memory.

SES standardizes the required semantics, not a mandatory file layout.

## 2. Mandatory semantics

A project bootstrap must make the following resolvable:

1. **Project identity** — what the project is and its current classification.
2. **Canonical source of truth** — repository/system and precedence rules.
3. **Live-ref resolution** — how to determine the current authoritative ref/state before reading project documentation.
4. **Bootstrap order** — the minimum ordered set of project-owned sources to read before substantive work.
5. **Authority model** — who can decide, authorize, accept risk and mutate material state.
6. **Specialist resolution** — how a specialist finds project-local rules, skills or overrides when they exist.
7. **Evidence rules** — how live evidence, versioned documentation, supplied information, inference and memory are ranked, including evidence/provenance admission semantics compatible with `core/protocols/EVIDENCE_PROVENANCE_ADMISSION_CONTRACT.md`.
8. **Environment/boundary model** — material environments and restrictions relevant to safe work.
9. **Continuity entrypoint** — how to recover durable current state when temporal continuity matters.
10. **Fail-closed behavior** — what to do when required context cannot be resolved.

## 3. Bootstrap is not continuity

Bootstrap answers:

`HOW DO I UNDERSTAND THIS PROJECT CORRECTLY?`

Continuity answers:

`WHERE IS THIS PROJECT NOW?`

A bootstrap may point to continuity, but must not silently replace it with a stale snapshot.

## 4. Minimum reconstruction flow

A compliant project should support a flow equivalent to:

```text
RESOLVE CANONICAL LIVE SOURCE
→ READ PROJECT BOOTSTRAP ENTRYPOINT
→ RESOLVE PROJECT-LOCAL SPECIALIST RULES WHEN APPLICABLE
→ READ COMMON PROJECT RULES
→ READ GOVERNANCE/AUTHORITY WHEN APPLICABLE
→ READ CONTINUITY WHEN CURRENT STATE MATTERS
→ RESOLVE MATERIAL LIVE OBJECTS
→ DECLARE GAPS / CONFLICTS / NEXT SAFE ACTION
```

The exact filenames may differ by project.

### 4.1 Evidence/provenance admission inheritance

A SES-compatible project bootstrap must make its evidence handling compatible with:

`core/protocols/EVIDENCE_PROVENANCE_ADMISSION_CONTRACT.md`

The project does not need to copy that contract or use a prescribed evidence directory.

At minimum, project-local bootstrap/evidence rules must preserve:

```text
CONVERSATION != CANONICAL PROJECT EVIDENCE
MATERIAL DECISION -> DURABLE RECONSTRUCTIBLE MEANING
RAW SOURCE -> ADMIT ONLY WHEN BOUNDED / PROBATIVE / NON-DUPLICATIVE
PROJECT OWNS ACTUAL EVIDENCE / RETENTION / SENSITIVE-DATA POLICY
```

For newly registered projects, these semantics are part of SES compatibility. Existing registered projects are reviewed proportionally when materially relevant; SES evolution does not itself authorize project-side mutation.

## 5. Proportionality

A small project may implement the contract with a compact bootstrap. A production, regulated, multi-tenant or high-risk system may require deeper authority, evidence, environment and security sources.

SES must not force every project to copy the complexity of its largest reference implementation.

`STANDARDIZE SEMANTICS != STANDARDIZE DOCUMENT VOLUME`

## 6. Fail-closed states

When material context is missing, use explicit states such as:

- `PROJECT_BOOTSTRAP_UNAVAILABLE`
- `CANONICAL_SOURCE_UNRESOLVED`
- `AUTHORITY_UNRESOLVED`
- `SPECIALIST_RULES_UNRESOLVED`
- `MISSING_EVIDENCE`
- `CONFLICTING_PROJECT_SOURCES`

Missing evidence must not be converted into invented context or a broad PASS.

## 7. Specialist creation dependency

Before SES creates or evolves a project-specific specialist, the project must have a resolvable bootstrap contract or the SES workflow must first prepare one.

Therefore:

`PROJECT-SPECIFIC SPECIALIST DESIGN REQUIRES PROJECT BOOTSTRAP`

This prevents project rules from being embedded ad hoc into individual specialists and becoming divergent copies of project truth.
