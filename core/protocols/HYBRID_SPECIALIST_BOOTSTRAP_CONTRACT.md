# SES — Hybrid Specialist Bootstrap Contract

**Status:** FOUNDATION_V0_1 / CONTRACT

## 1. Purpose

This contract defines the mandatory pre-work protocol for a hybrid SES specialist that can operate across multiple registered consumer projects.

Its primary safety property is:

`NO VERIFIED PROJECT CONTEXT -> NO PROJECT-SPECIFIC SUBSTANTIVE WORK`

A hybrid specialist must not treat a user-supplied project name, conversation starter, prior chat, memory, copied context or tool capability as proof that the correct project configuration has been loaded.

## 2. Inputs

A hybrid bootstrap consumes, at minimum:

```text
PROJECT_IDENTIFIER
SPECIALIST_ID_OR_ARCHETYPE
TASK_CONTEXT
```

Optional inputs may include requested environment, mode, target ref or bounded scope, but they never override project-owned authority or source precedence.

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
-> EMIT CONTEXT READINESS RECEIPT
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

## 5. Context Readiness Receipt

Before substantive project-specific work, the specialist must be able to state a receipt equivalent to:

```text
SES_REF
PROJECT_RESOLUTION_STATUS
PROJECT_ID
PROJECT_ADAPTER_REF
CANONICAL_PROJECT_SOURCE
PROJECT_LIVE_REF
PROJECT_BOOTSTRAP_STATUS
SPECIALIST_RESOLUTION_STATUS
SPECIALIST_SOURCE_REF
PROJECT_CONTINUITY_STATUS
MATERIAL_EVIDENCE_STATUS
AUTHORITY_STATUS
CONTEXT_STATUS
GAPS
```

The representation may be prose, structured text or machine-readable output, but the semantics are mandatory.

### 5.1 `CONTEXT_STATUS = READY`

`READY` is allowed only when every source required for the requested task has been resolved on the applicable authoritative ref and no material contradiction remains unresolved.

### 5.2 `CONTEXT_STATUS = LIMITED`

`LIMITED` may be used only when the unresolved gap does not affect the bounded work being performed. The specialist must state the exact limitation and must not extend the conclusion beyond it.

Example: continuity may be `NOT_REQUIRED_FOR_THIS_TASK` for a timeless conceptual question that does not depend on current project state.

### 5.3 `CONTEXT_STATUS = BLOCKED`

Use `BLOCKED` when a missing or conflicting source is material to the requested decision. A user instruction to "continue anyway" does not convert a blocked material context into ready context.

## 6. Mandatory fail-closed states

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
- `AUTHORITY_UNRESOLVED`
- `MISSING_EVIDENCE`
- `CONFLICTING_PROJECT_SOURCES`

Missing evidence must never be converted into an inferred project fact or broad PASS.

## 7. Project-switch isolation

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

For an explicitly multi-project task, each project must be resolved independently and conclusions must preserve source boundaries.

## 8. Evidence binding

A readiness claim must be bound to concrete evidence sufficient for the task. At minimum, material work should preserve the exact SES ref and exact consumer-project live ref used.

When the consumer project uses versioned specialist skills or bootstrap documents, the receipt should identify the exact file/ref or equivalent immutable locator when available.

A search result, snippet, prior summary or user-supplied assertion is not by itself proof that a required canonical source was read.

## 9. Authority boundary

Hybrid context resolution grants context, not authority.

`CONTEXT_READY != AUTHORIZED_TO_MUTATE`

`TOOL_CAPABILITY != AUTHORIZATION`

Mutation authority must still be resolved from the consumer project's own authority/governance sources and the current task authorization.

## 10. Runtime mechanism boundary

This contract defines required behavior, not the final loading technology.

Potential implementations may include external API/Action loading, generated project-bound instances or another deterministic loader. Knowledge retrieval alone must not be assumed equivalent to fixed project authority or safety configuration.

The runtime mechanism must eventually prove that it can satisfy this contract in a fresh conversation without relying on hidden prior state.

## 11. Acceptance criteria

A hybrid specialist bootstrap is behaviorally acceptable only if it can demonstrate all of the following:

1. deterministic project resolution from registered identifiers;
2. no fuzzy project inference for material work;
3. fail-closed behavior when registry, adapter, canonical source, bootstrap, specialist rules, authority or required continuity are unavailable;
4. exact separation between project context and mutation authority;
5. no cross-project context contamination after a project switch;
6. explicit readiness receipt before substantive project-specific work;
7. no retroactive `READY` after a failed bootstrap unless the missing evidence is actually resolved;
8. fresh-conversation repeatability.

The canonical behavioral cases are defined in `tests/behavioral/HYBRID_SPECIALIST_BOOTSTRAP_TESTS.md`.
