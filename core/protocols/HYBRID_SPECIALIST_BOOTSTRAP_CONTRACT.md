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

`TASK_SCOPE` is the full material objective requested by the user for which readiness is being evaluated. It must be specific enough to distinguish conceptual/read-only work from current-state, lifecycle or mutation work.

The bootstrap must also classify, and bind into the receipt, the following dimensions even when they are not material:

```text
TARGET_REF_OR_OBJECT
ENVIRONMENT
```

Use `NOT_REQUIRED_FOR_THIS_TASK` when either dimension is genuinely immaterial. A material target/ref/environment must never remain implicit inside a broad task description.

Optional inputs may include mode or additional bounded-scope detail, but they never override project-owned authority or source precedence.

## 3. Proof-ref resolution

SES canonical state and a candidate PR/head are different evidence classes.

Every material bootstrap must first resolve:

```text
SES_CANONICAL_MAIN_REF
```

For ordinary canonical/runtime work:

```text
PROOF_LEVEL: RUNTIME_BEHAVIORAL_PROOF or ordinary task work
SES_EFFECTIVE_REF: SES_CANONICAL_MAIN_REF
SES_CANDIDATE_REF: NOT_APPLICABLE
```

For candidate-head protocol validation:

```text
PROOF_LEVEL: CANDIDATE_HEAD_PROTOCOL_PROOF
SES_CANONICAL_MAIN_REF: <resolved live main>
SES_CANDIDATE_REF: <exact candidate PR/head>
SES_EFFECTIVE_REF: SES_CANDIDATE_REF
```

The candidate ref may be used to read the candidate contract/bootstrap under review, but it must never be mislabeled as canonical SES `main`. Both refs must remain visible in the evidence record when they differ.

`CANDIDATE_HEAD != CANONICAL_MAIN`

## 4. Mandatory resolution flow

For project-specific work, execute the following in order:

```text
RESOLVE SES CANONICAL MAIN LIVE
-> SELECT SES EFFECTIVE REF FOR THE DECLARED PROOF LEVEL
-> READ SES BOOTSTRAP ON SES EFFECTIVE REF
-> READ SES PROJECT REGISTRY ON SES EFFECTIVE REF
-> RESOLVE UNIQUE PROJECT_ID + ADAPTER_PATH
-> READ PROJECT ADAPTER
-> RESOLVE CONSUMER PROJECT CANONICAL SOURCE LIVE
-> READ PROJECT-LOCAL BOOTSTRAP
-> RESOLVE PROJECT-LOCAL SPECIALIST RULES / OVERRIDES
-> READ PROJECT-LOCAL COMMON RULES AND AUTHORITY SOURCES WHEN APPLICABLE
-> READ PROJECT CONTINUITY WHEN CURRENT STATE IS MATERIAL
-> RESOLVE LIVE OBJECTS MATERIAL TO THE TASK/TARGET/ENVIRONMENT
-> EMIT TASK-BOUND CONTEXT READINESS RECEIPT
-> ONLY THEN BEGIN PROJECT-SPECIFIC SUBSTANTIVE WORK
```

The Project Registry remains the SES-side authority for name/ID/alias mapping. The Project Adapter remains a locator, not project truth.

## 5. Project resolver semantics

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

## 6. Task-bound Context Readiness Receipt

Before substantive project-specific work, the specialist must be able to state a receipt equivalent to:

```text
PROOF_LEVEL
TASK_SCOPE
EFFECTIVE_SCOPE
TARGET_REF_OR_OBJECT
ENVIRONMENT
SES_CANONICAL_MAIN_REF
SES_CANDIDATE_REF
SES_EFFECTIVE_REF
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

The representation may be prose, structured text or machine-readable output, but the semantics are mandatory. A field may be `NOT_REQUIRED_FOR_THIS_TASK`, `NOT_REQUESTED` or `NOT_APPLICABLE` only when that classification is justified by the exact task/proof level.

A receipt proves readiness only for the task, effective scope, target, environment and evidence set to which it is bound.

`READY_FOR_TASK_A != READY_FOR_TASK_B`

### 6.1 `CONTEXT_STATUS = READY`

`READY` is allowed only when:

- the entire requested `TASK_SCOPE` can be completed safely;
- `EFFECTIVE_SCOPE` is materially equivalent to `TASK_SCOPE`;
- every source required for that task/target/environment has been resolved on the applicable authoritative ref;
- no material contradiction remains unresolved.

`READY` is not a session-wide project certification and is not reusable as a blanket approval for later work.

### 6.2 `CONTEXT_STATUS = LIMITED`

`LIMITED` is allowed only when the full requested `TASK_SCOPE` cannot be safely completed, but an explicitly reduced `EFFECTIVE_SCOPE` can be completed without relying on the unresolved material dependency.

For `LIMITED`:

```text
EFFECTIVE_SCOPE must be a strict subset of TASK_SCOPE
GAPS must identify what prevents the full scope
```

The specialist must state the excluded portion and must not silently answer beyond `EFFECTIVE_SCOPE`.

A source that is genuinely irrelevant to the requested task does not by itself make the result `LIMITED`; it may be `NOT_REQUIRED_FOR_THIS_TASK` while the task remains `READY`.

### 6.3 `CONTEXT_STATUS = BLOCKED`

Use `BLOCKED` when a missing or conflicting source is material to the requested decision and no safe reduced scope has been explicitly established. A user instruction to "continue anyway" does not convert a blocked material context into ready context.

## 7. Receipt validity and invalidation

A current receipt must declare:

```text
RECEIPT_VALIDITY: VALID
```

when its task, effective scope, target, environment and material evidence remain applicable.

The receipt becomes:

```text
RECEIPT_VALIDITY: STALE_REVALIDATION_REQUIRED
```

when an event can materially change the correctness of the readiness claim.

Mandatory revalidation triggers include, when material:

- project switch;
- material change in `TASK_SCOPE` or `EFFECTIVE_SCOPE`;
- material change in `TARGET_REF_OR_OBJECT`;
- material change in `ENVIRONMENT`;
- SES canonical/effective ref change affecting a contract used by the task;
- consumer-project live ref change when the task depends on current state or changed content;
- specialist source/ref change;
- continuity invalidation event;
- authority model change;
- new mutation request or changed mutation scope;
- new evidence that contradicts or supersedes a material premise.

A stale receipt must not be silently reused. Revalidate only the sources invalidated or made newly material by the new task/event; do not replay unrelated gates.

`STALE_RECEIPT -> REVALIDATE MATERIAL DEPENDENCIES -> NEW RECEIPT`

## 8. Mandatory fail-closed states

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

## 9. Project-switch isolation

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

## 10. Evidence binding

A readiness claim must be bound to concrete evidence sufficient for the task. Material work must preserve the exact SES canonical/effective refs and exact consumer-project live ref used.

When target or environment is material, the receipt must bind the exact target/ref/object and environment. A change to either is an invalidation event unless the evidence establishes that the change is immaterial to the task.

When the consumer project uses versioned bootstrap, specialist or continuity documents, the receipt should identify the exact file/ref or equivalent immutable locator when available.

A search result, snippet, prior summary, prior receipt or user-supplied assertion is not by itself proof that a required canonical source was read.

## 11. Authority boundary

Hybrid context resolution grants context, not authority.

Two states must remain distinct:

```text
AUTHORITY_MODEL_STATUS
MUTATION_AUTHORIZATION_STATUS
```

`AUTHORITY_MODEL_STATUS` answers whether the project-owned authority model required for the task was resolved.

`MUTATION_AUTHORIZATION_STATUS` answers whether the current requested mutation, if any, has explicit and applicable authorization for the exact mutation scope, target and environment.

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

When a mutation is requested without applicable authorization, the specialist must not mutate and must emit `MUTATION_AUTHORIZATION_STATUS: NOT_AUTHORIZED` (or the project-specific equivalent) for that mutation attempt.

Mutation authority must still be resolved from the consumer project's own authority/governance sources and the current task authorization. A new mutation request or changed mutation scope/target/environment requires authorization re-evaluation even if contextual evidence otherwise remains valid.

## 12. Proof levels and runtime mechanism boundary

This contract defines required behavior, not the final loading technology.

Potential implementations may include external API/Action loading, generated project-bound instances or another deterministic loader. Knowledge retrieval alone must not be assumed equivalent to fixed project authority or safety configuration.

Evidence must distinguish:

```text
SPEC_CONFORMANCE
CANDIDATE_HEAD_PROTOCOL_PROOF
RUNTIME_BEHAVIORAL_PROOF
```

- `SPEC_CONFORMANCE` means the contract, bootstrap and tests are internally coherent.
- `CANDIDATE_HEAD_PROTOCOL_PROOF` means an exact candidate PR/head can demonstrate the resolution chain against real read-only sources while preserving both canonical-main and candidate refs.
- `RUNTIME_BEHAVIORAL_PROOF` means the actual specialist/loading mechanism executes every runtime-required canonical case and demonstrates the required behavior, including fresh-conversation execution, without relying on hidden prior state.

A runtime-required case that is `NOT_EXECUTED`, `SKIPPED`, `INDETERMINATE` or otherwise lacks expected behavioral evidence prevents `RUNTIME_BEHAVIORAL_PROOF = PASS`.

Neither specification quality nor candidate-head feasibility may be relabeled as runtime behavioral PASS.

## 13. Acceptance criteria

A hybrid specialist bootstrap is behaviorally acceptable only if it can demonstrate all of the following:

1. deterministic project resolution from registered identifiers;
2. no fuzzy project inference for material work;
3. fail-closed behavior for every mandatory state in section 8;
4. exact separation between project context and mutation authorization, including a denied unauthorized-mutation path;
5. no cross-project context contamination after a project switch;
6. explicit task/target/environment-bound readiness receipt before substantive project-specific work;
7. deterministic and mutually distinguishable `READY`, `LIMITED` and `BLOCKED` semantics;
8. receipt invalidation/revalidation after material task/ref/target/environment/authority/evidence changes;
9. no retroactive `READY` after a failed bootstrap unless the missing evidence is actually resolved in a new attempt;
10. explicit dual-ref treatment for candidate-head proof;
11. fresh-conversation repeatability;
12. explicit separation between spec/candidate-head proof and runtime behavioral proof;
13. no runtime PASS while any runtime-required canonical case remains unexecuted or failed.

The canonical behavioral cases are defined in `tests/behavioral/HYBRID_SPECIALIST_BOOTSTRAP_TESTS.md`.
