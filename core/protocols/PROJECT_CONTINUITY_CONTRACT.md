# SES — Project Continuity Contract

**Status:** FOUNDATION_V0_1 / CONTRACT

## 1. Purpose

A Project Continuity Protocol preserves durable operational meaning between conversations, specialists and work cycles without becoming a substitute for live project sources.

Continuity is required conceptually for SES-compatible project work that depends on current state. Its implementation complexity is proportional to project risk and operational maturity.

## 2. Core separation

A compliant continuity model must distinguish:

```text
LIVE_RESOLVED_STATE
!=
MATERIAL_RECORDED_STATE
```

### Live resolved state

Facts that can change independently and must be resolved from the authoritative runtime/source when material, such as current branch/head, deployment status, active environment state, current checks or other volatile lifecycle facts.

### Material recorded state

Durable meaning that should survive ordinary lifecycle churn, such as objectives, material decisions, unresolved risks, blockers, accepted constraints, semantic next action and handoff meaning.

A recorded snapshot must not override a newer authoritative live state.

## 3. Minimum continuity capabilities

A project continuity implementation must make the following recoverable when applicable:

- current material objective/state;
- material decisions and constraints;
- unresolved blockers/risks;
- semantic next safe action;
- authority/authorization provenance material to continuation;
- evidence validity or freshness when material;
- handoff/ownership meaning;
- invalidation events that require revalidation.

The project may implement these in one compact document or multiple specialized ledgers.

## 4. Proportional implementation

Small project example:

```text
CURRENT_STATE.md
DECISIONS.md
NEXT_ACTION.md
```

Higher-risk project example may add:

```text
AUTHORIZATIONS
EVIDENCE_FRESHNESS
BLOCKED_ACTIONS
HANDOFFS
```

SES standardizes continuity semantics, not a mandatory SFJM-shaped directory.

## 5. Reference implementation: SFJM

FECH.AI SFJM is a reference implementation of this contract, not the universal storage format for all projects.

Lessons that may be reused include:

- separate live-resolved from durable recorded state;
- avoid duplicating volatile lifecycle facts across multiple authorities;
- update continuity only for material semantic changes;
- avoid recursive reconciliation loops;
- do not replay historical gates automatically when no present safety decision depends on them.

These are reference-derived patterns and remain subject to SES validation before promotion to broader universal principles.

## 6. Anti-loop rule

A new conversation, ordinary commit, documentation-only closure or lifecycle transition must not automatically force a continuity rewrite.

Update continuity when evidence or a decision materially changes the meaning required for safe continuation.

`NEW EVENT != AUTOMATIC CONTINUITY MUTATION`

## 7. Historical integrity

Continuity must preserve material historical observations without silently rewriting them into a different past state.

Later reassessment may invalidate, supersede or reinterpret a prior conclusion, but should link the new assessment to the prior record rather than erase provenance.

## 8. Fail-closed behavior

If continuity is material to the requested decision and the project continuity entrypoint cannot be resolved, declare `PROJECT_CONTINUITY_UNAVAILABLE` and limit or block conclusions that depend on current recorded state.

Absence of continuity evidence is not evidence that no blocker, authorization or prior decision exists.
