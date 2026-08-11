# SES — Hybrid Specialist Bootstrap Contract

**Status:** FOUNDATION_V0_1 / CONTRACT

## 1. Purpose

This contract defines the mandatory pre-work protocol for a hybrid SES specialist that can operate across multiple registered consumer projects.

Its primary safety property is:

`NO VERIFIED PROJECT CONTEXT -> NO PROJECT-SPECIFIC SUBSTANTIVE WORK`

A hybrid specialist must not treat a user-supplied project name, conversation starter, prior chat, memory, copied context, prior readiness receipt or tool capability as proof that the correct project configuration is ready for the current task.

## 2. Inputs

A hybrid bootstrap consumes, at minimum:

```text
PROJECT_IDENTIFIER
SPECIALIST_ID_OR_ARCHETYPE
TASK_CONTEXT
TASK_SCOPE
```

`TASK_SCOPE` is the bounded material objective for which readiness is being evaluated. It must be specific enough to distinguish a conceptual/read-only task from a current-state, lifecycle or mutation task.

Optional inputs may include requested environment, mode, target ref or bounded scope detail, but they never override project-owned authority or source precedence.

## 3. Mandatory resolution flow

For project-specific work, execute the following in order:

```text
RESOLVE SES MAIN LIVE
-> READ SES BOOTSTRAP
-> READ SES PROJECT REGISTRY
-> RESOLVE UNIQUE PROJECT_ID + ADAPTER_PATH
-> READ PROJECT ADAPTER
-> RESOLVE CONSUMER PROJECT CANONICAL SOURCE LIVE
-> READ PROJECT-LOCAL BOOTSTRAP
-> RESOLVE PROJECT-LOCAL SPECIALIST RULES / OVERRIDES
-> READ PROJECT-LOCAL COMMON RULES AND AUTHORITY SOURCES WHEN APPLICABLE
-> READ PROJECT CONTINUITY WHEN CURRENT STATE IS MATERIAL
-> RESOLVE LIVE OBJECTS MATERIAL TO THE TASK
-> EMIT TASK-BOUND CONTEXT READINESS RECEIPT
-> ONLY THEN BEGIN PROJECT-SPECIFIC SUBSTANTIVE WORK
```

The Project Registry remains the SES-side authority for name/ID/alias mapping. The Project Adapter remains a locator, not project truth.

## 4. Project resolver semantics

The hybrid specialist must apply the registry rules exactly:

1. trim surrounding whitespace;
2. match exact `PROJECT_ID` first;
3. otherwise match `CANONICAL_NAME` or an explicit `ALIAS` case-insensitively;
4. do not use fuzzy matching, semantic guessing, inferred aliases or folder-name guessing for material project resolution;
5. require exactly one active registry match.

Resolution outcomes:

- zero matches -> `PROJECT_NOT_REGISTERED`;
- multiple matches -> `PROJECT_ID_AMBIGUOUS`;
- unavailable registry -> `PROJECT_REGISTRY_UNAVAILABLE`;
- resolved registry entry but unavailable/contradictory adapter -> `PROJECT_ADAPTER_UNRESOLVED`.

## 5. Task-bound Context Readiness Receipt

Before substantive project-specific work, the specialist must be able to state a receipt equivalent to:

```text
TASK_SCOPE
SES_REF
PROJECT_RESOLUTION_STATUS
PROJECT_ID
PROJECT_ADAPTER_STATUS
PROJECT_ADAPTER_REF
CANONICAL_PROJECT_SOURCE
PROJECT_LIVE_REF
PROJECT_BOOTSTRAP_STATUS
PROJECT_BOOTSTRAP_REF
SPECIALIST_RESOLUTION_STATUS
SPECIALIST_SOURCE_REF
PROJECT_CONTINUITY_STATUS
PROJECT_CONTINUITY_REF
MATERIAL_EVIDENCE_STATUS
AUTHORITY_MODEL_STATUS
MUTATION_AUTHORIZATION_STATUS
CONTEXT_STATUS
RECEIPT_VALIDITY
GAPS
```

The representation may be prose, structured text or machine-readable output, but the semantics are mandatory. A field may be `NOT_REQUIRED_FOR_THIS_TASK` or `NOT_REQUESTED` only when that classification is justified by the current `TASK_SCOPE`.

A receipt proves readiness only for the task scope and evidence set to which it is bound.

`READY_FOR_TASK_A != READY_FOR_TASK_B`

### 5.1 `CONTEXT_STATUS = READY`

`READY` is allowed only when every source required for the exact `TASK_SCOPE` has been resolved on the applicable authoritative ref and no material contradiction remains unresolved.

`READY` is not a session-wide project certification and is not reusable as a blanket approval for later work.

### 5.2 `CONTEXT_STATUS = LIMITED`

`LIMITED` may be used only when an unresolved gap does not affect the explicitly bounded work being performed. The specialist must state the exact limitation and must not extend the conclusion beyond it.

Example: continuity may be `NOT_REQUIRED_FOR_THIS_TASK` for a timeless conceptual question that does not depend on current project state.

### 5.3 `CONTEXT_STATUS = BLOCKED`

Use `BLOCKED` when a missing or conflicting source is material to the requested decision. A user instruction to "continue anyway" does not convert a blocked material context into ready context.

## 6. Receipt validity and invalidation

A current receipt must declare:

```text
RECEIPT_VALIDITY: VALID
```

when its task scope and material evidence remain applicable.

The receipt becomes:

```text
RECEIPT_VALIDITY: STALE_REVALIDATION_REQUIRED
```

when an event can materially change the correctness of the readiness claim.

Mandatory revalidation triggers include, when material:

- project switch;
- material change in `TASK_SCOPE`;
- SES ref change affecting a contract used by the task;
- consumer-project live ref change when the task depends on current state or changed content;
- specialist source/ref change;
- continuity invalidation event;
- authority model change;
- new mutation request or changed mutation scope;
- new evidence that contradicts or supersedes a material premise;
- material environment/target-ref change.

A stale receipt must not be silently reused. Revalidate only the sources invalidated or made newly material by the new task/event; do not replay unrelated gates.

`STALE_RECEIPT -> REVALIDATE MATERIAL DEPENDENCIES -> NEW RECEIPT`

## 7. Mandatory fail-closed states

Use explicit states when applicable:

- `SES_BOOTSTRAP_UNAVAILABLE`
- `PROJECT_REGISTRY_UNAVAILABLE`
- `PROJECT_NOT_REGISTERED`
- `PROJECT_ID_AMBIGUOUS`
- `PROJECT_ADAPTER_UNRESOLVED`
- `CANONICAL_SOURCE_UNRESOLVED`
- `PROJECT_BOOTSTRAP_UNAVAILABLE`
- `SPECIALIST_RULES_UNRESOLVED`
- `PROJECT_CONTINUITY_UNAVAILABLE`
- `AUTHORITY_MODEL_UNRESOLVED`
- `MUTATION_NOT_AUTHORIZED`
- `MISSING_EVIDENCE`
- `CONFLICTING_PROJECT_SOURCES`
- `STALE_REVALIDATION_REQUIRED`

Missing evidence must never be converted into an inferred project fact or broad PASS.

## 8. Project-switch isolation

When a hybrid specialist switches projects, project-scoped context from the previous project must be treated as invalid for the new project unless independently resolved from the new project's canonical sources.

`PROJECT_SWITCH -> INVALIDATE PRIOR PROJECT-SCOPED CONTEXT`

The specialist must not carry over:

- authority;
- environments;
- current decisions;
- tenant/user facts;
- runtime state;
- specialist overrides;
- security assumptions;
- continuity state;
- project-local terminology asserted as fact.

For an explicitly multi-project task, each project must be resolved independently and conclusions must preserve source boundaries. Each project receives its own receipt or independently identifiable receipt section.

## 9. Evidence binding

A readiness claim must be bound to concrete evidence sufficient for the task. At minimum, material work must preserve the exact SES ref and exact consumer-project live ref used.

When the consumer project uses versioned bootstrap, specialist or continuity documents, the receipt should identify the exact file/ref or equivalent immutable locator when available.

A search result, snippet, prior summary, prior receipt or user-supplied assertion is not by itself proof that a required canonical source was read.

## 10. Authority boundary

Hybrid context resolution grants context, not authority.

Two states must remain distinct:

```text
AUTHORITY_MODEL_STATUS
MUTATION_AUTHORIZATION_STATUS
```

`AUTHORITY_MODEL_STATUS` answers whether the project-owned authority model required for the task was resolved.

`MUTATION_AUTHORIZATION_STATUS` answers whether the current requested mutation, if any, has explicit and applicable authorization.

Examples:

```text
AUTHORITY_MODEL_STATUS: RESOLVED
MUTATION_AUTHORIZATION_STATUS: NOT_REQUESTED
```

```text
AUTHORITY_MODEL_STATUS: RESOLVED
MUTATION_AUTHORIZATION_STATUS: NOT_AUTHORIZED
```

A task may have `CONTEXT_STATUS: READY` while mutation remains prohibited.

`CONTEXT_READY != AUTHORIZED_TO_MUTATE`

`TOOL_CAPABILITY != AUTHORIZATION`

Mutation authority must still be resolved from the consumer project's own authority/governance sources and the current task authorization. A new mutation request or changed mutation scope requires authorization re-evaluation even if the contextual receipt remains otherwise valid.

## 11. Proof levels and runtime mechanism boundary

This contract defines required behavior, not the final loading technology.

Potential implementations may include external API/Action loading, generated project-bound instances or another deterministic loader. Knowledge retrieval alone must not be assumed equivalent to fixed project authority or safety configuration.

Evidence must distinguish:

```text
SPEC_CONFORMANCE
CANDIDATE_HEAD_PROTOCOL_PROOF
RUNTIME_BEHAVIORAL_PROOF
```

- `SPEC_CONFORMANCE` means the contract, bootstrap and tests are internally coherent.
- `CANDIDATE_HEAD_PROTOCOL_PROOF` means a PR/head can demonstrate the resolution chain against real read-only sources without claiming the candidate is already canonical on SES `main`.
- `RUNTIME_BEHAVIORAL_PROOF` means the actual specialist/loading mechanism demonstrates the required behavior, including fresh-conversation execution, without relying on hidden prior state.

Neither specification quality nor candidate-head feasibility may be relabeled as runtime behavioral PASS.

## 12. Acceptance criteria

A hybrid specialist bootstrap is behaviorally acceptable only if it can demonstrate all of the following:

1. deterministic project resolution from registered identifiers;
2. no fuzzy project inference for material work;
3. fail-closed behavior when registry, adapter, canonical source, bootstrap, specialist rules, authority model or required continuity are unavailable;
4. exact separation between project context and mutation authorization;
5. no cross-project context contamination after a project switch;
6. explicit task-bound readiness receipt before substantive project-specific work;
7. receipt invalidation/revalidation after material task/ref/authority/evidence changes;
8. no retroactive `READY` after a failed bootstrap unless the missing evidence is actually resolved in a new attempt;
9. fresh-conversation repeatability;
10. explicit separation between spec/candidate-head proof and runtime behavioral proof.

The canonical behavioral cases are defined in `tests/behavioral/HYBRID_SPECIALIST_BOOTSTRAP_TESTS.md`.
