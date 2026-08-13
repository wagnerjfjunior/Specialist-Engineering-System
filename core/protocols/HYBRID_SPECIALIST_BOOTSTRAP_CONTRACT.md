# SES — Hybrid Specialist Bootstrap Contract

**Status:** FOUNDATION_V0_3 / CANDIDATE_CONTRACT

## 1. Purpose

This contract defines the mandatory pre-work protocol for a hybrid SES specialist that can operate across multiple registered consumer projects.

Primary safety properties:

`NO VERIFIED PROJECT CONTEXT -> NO PROJECT-SPECIFIC SUBSTANTIVE WORK`

`NO SUBSTANTIVE TASK -> NO CONSUMER-PROJECT MATERIALIZATION`

A user-supplied project name, numeric choice, conversation starter, prior chat, memory, copied context, prior receipt or tool capability is never proof that project-specific context is ready for a substantive task.

The hybrid bootstrap is one ordered flow. Different user inputs change stage state; they do not create alternate bootstrap paths or bypass mandatory stages.

`ONE FLOW / DIFFERENT INPUT STATES`

## 2. Inputs and staged completeness

The flow tracks:

```text
PROJECT_IDENTIFIER
SPECIALIST_ID_OR_ARCHETYPE
TASK_CONTEXT
TASK_SCOPE
TARGET_REF_OR_OBJECT
ENVIRONMENT
```

`PROJECT_IDENTIFIER` may initially be `NOT_SUPPLIED`. That state does not authorize project guessing.

`TASK_SCOPE` may initially be `NOT_YET_SUPPLIED` while the user is only starting the specialist or choosing a project. `TASK_SCOPE: NOT_YET_SUPPLIED` is not a material task and must not be converted into an artificial connection/bootstrap task.

Do not invent:

```text
TASK_SCOPE: PROJECT_CONNECTION_BOOTSTRAP
```

merely to justify loading a consumer project before the user has asked for substantive work.

A substantive `TASK_SCOPE` is required before consumer-project materialization, task-bound readiness evaluation or substantive project-specific work.

`TARGET_REF_OR_OBJECT` and `ENVIRONMENT` are classified when a substantive task makes them relevant. Use `NOT_REQUIRED_FOR_THIS_TASK` only when genuinely immaterial.

## 3. Proof-ref resolution

SES canonical state and a candidate PR/head are different evidence classes.

Before a live project menu or material SES/project work, resolve:

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

A candidate ref may be used to read candidate artifacts under review but must never be called canonical `main`.

`CANDIDATE_HEAD != CANONICAL_MAIN`

## 4. One ordered resolution flow

Execute the following state machine in order:

```text
RESOLVE SES CANONICAL MAIN LIVE
-> SELECT SES EFFECTIVE REF
-> READ SES BOOTSTRAP ON SES EFFECTIVE REF
-> RESOLVE SPECIALIST / ARCHETYPE
-> READ SES PROJECT REGISTRY ON SES EFFECTIVE REF
-> RESOLVE PROJECT IDENTIFIER
-> RESOLVE UNIQUE PROJECT_ID + ADAPTER_PATH
-> PROJECT_SELECTED
-> IF TASK_SCOPE = NOT_YET_SUPPLIED: WAIT FOR TASK
-> IF SUBSTANTIVE TASK_SCOPE EXISTS: CLASSIFY TASK MATERIALITY
-> READ PROJECT ADAPTER
-> RESOLVE CONSUMER PROJECT CANONICAL SOURCE LIVE
-> READ PROJECT-LOCAL BOOTSTRAP
-> RESOLVE PROJECT-LOCAL SPECIALIST RULES / OVERRIDES
-> READ ONLY TASK-MATERIAL COMMON / AUTHORITY / GOVERNANCE SOURCES
-> READ PROJECT CONTINUITY ONLY WHEN CURRENT STATE IS MATERIAL
-> RESOLVE LIVE OBJECTS / EVIDENCE MATERIAL TO TASK/TARGET/ENVIRONMENT
-> EMIT TASK-BOUND CONTEXT READINESS RECEIPT
-> ONLY THEN BEGIN PROJECT-SPECIFIC SUBSTANTIVE WORK
```

The `WAIT FOR TASK` state is not a bypass. It is the canonical stopping condition when the next mandatory stage lacks a substantive `TASK_SCOPE`.

A project name supplied directly and a project selected from a numbered menu both enter the same project-resolution stage.

The Project Registry is the SES-side authority for project mapping. A Project Adapter is a locator, not project truth.

## 5. Project-resolution stage

Every hybrid project entry passes through this stage after the applicable SES ref, specialist/archetype and Project Registry are resolved.

### 5.1 Project identifier supplied

When `PROJECT_IDENTIFIER` is supplied, validate it through the current registry using section 7 resolver semantics.

If exactly one active project resolves, preserve:

```text
PROJECT_RESOLUTION_STATUS: RESOLVED
PROJECT_ID
ADAPTER_PATH
PROJECT_SELECTION_STATUS: RESOLVED
```

If no substantive task exists, stop at `PROJECT_SELECTED` and ask for the task.

### 5.2 Project identifier not supplied

When `PROJECT_IDENTIFIER: NOT_SUPPLIED`, including `# CLIQUE PARA INICIAR`:

1. use `projects/REGISTRY.md` on current `SES_EFFECTIVE_REF`;
2. enumerate only `STATUS: ACTIVE`;
3. display each project once using `CANONICAL_NAME`;
4. number the displayed list;
5. bind each displayed number to that exact `PROJECT_ID`;
6. ask the user to choose one displayed number;
7. wait for a valid selection;
8. never hard-code a permanent number-to-project mapping.

Recommended rendering:

```text
Selecione o projeto em que deseja trabalhar:

1. <CANONICAL_NAME A>
2. <CANONICAL_NAME B>

Digite o número do projeto.
```

Menu presence proves only current SES registration for hybrid resolution.

`PROJECT_LISTED != PROJECT_SPECIALIST_READY`

### 5.3 Numeric selection

A numeric reply has project meaning only against the exact menu instance previously displayed.

Invalid/out-of-range numbers are not guessed. Re-present or regenerate the list.

If the applicable SES ref or registry materially changes between menu display and selection, invalidate the old numeric mapping and regenerate the menu.

### 5.4 Unknown or ambiguous identifier

Zero active matches -> `PROJECT_NOT_REGISTERED`.

Multiple active matches -> `PROJECT_ID_AMBIGUOUS`.

When registry evidence is available, the same stage may present the current active list as recovery. A later successful recovery does not rewrite the failed attempt as PASS.

## 6. Project selection versus project materialization

A successful selection establishes project identity only.

```text
PROJECT_SELECTED != PROJECT_BOOTSTRAPPED
PROJECT_SELECTED != PROJECT_SPECIALIST_READY
PROJECT_SELECTED != PROJECT_CONTEXT_READY
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
```

When `TASK_SCOPE: NOT_YET_SUPPLIED`, the specialist must not:

- read the Project Adapter;
- resolve the consumer project's live ref;
- read project bootstrap;
- resolve project-local specialist rules;
- read continuity;
- read authority/governance;
- read project evidence;
- emit a Context Readiness Receipt.

Expected interaction after selection is bounded:

```text
PROJECT_SELECTION_STATUS: RESOLVED
PROJECT_ID: <selected>
TASK_SCOPE: NOT_YET_SUPPLIED
NEXT_REQUIRED_INPUT: TASK
```

The specialist may render this naturally, e.g. `Projeto selecionado. Envie a tarefa.`

### 6.1 Task activation

When a substantive task is later supplied, continue the same flow from the selected project. Before materialization, revalidate the selected `PROJECT_ID` against the applicable live registry when the registry/ref may have changed materially.

Then classify material dependencies before retrieval.

`TASK -> MATERIAL DEPENDENCIES -> TARGETED PROJECT BOOTSTRAP`

Do not perform ceremonial bulk loading. Project-local bootstrap instructions define authority and source ordering, but only task-material downstream sources need to be resolved unless the project bootstrap explicitly makes a source universally mandatory for every substantive task.

### 6.2 Project and task supplied together

If the initial user request already contains both a resolvable project identifier and a substantive task, the same flow continues through materialization without stopping at `WAIT FOR TASK`.

This is not a bypass: all stages are still executed in order with the required inputs already present.

## 7. Project resolver semantics

Apply registry rules exactly:

1. trim surrounding whitespace;
2. exact `PROJECT_ID` first;
3. otherwise exact `CANONICAL_NAME` or explicit `ALIAS` case-insensitively;
4. no fuzzy matching, semantic guessing, inferred alias or folder-name guessing;
5. require exactly one active match.

Outcomes:

- zero matches -> `PROJECT_NOT_REGISTERED`;
- multiple matches -> `PROJECT_ID_AMIGUOUS`;
- unavailable registry -> `PROJECT_REGISTRY_UNAVAILABLE`;
- adapter problems are evaluated only after task activation, when adapter resolution becomes material.

A conversation starter is interaction input only. It is not configuration authority, readiness or mutation authority.

## 8. Task-bound Context Readiness Receipt

A Context Readiness Receipt exists only for a substantive task.

Before substantive project-specific work, preserve semantics equivalent to:

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

Fields may be `NOT_REQUIRED_FOR_THIS_TASK`, `NOT_REQUESTED` or `NOT_APPLICABLE` only when justified by the exact task/proof level.

A receipt proves readiness only for the task, effective scope, target, environment and evidence set to which it is bound.

`READY_FOR_TASK_A != READY_FOR_TASK_B`

### 8.1 `CONTEXT_STATUS = READY`

Allowed only when:

- the entire requested `TASK_SCOPE` can be completed safely;
- `EFFECTIVE_SCOPE` is materially equivalent to `TASK_SCOPE`;
- every source material to that task/target/environment is resolved;
- no material contradiction remains unresolved.

### 8.2 `CONTEXT_STATUS = LIMITED`

Allowed only when a strict, explicit safe subset can be completed independently.

```text
EFFECTIVE_SCOPE must be a strict subset of TASK_SCOPE
GAPS must identify what prevents the full scope
```

### 8.3 `CONTEXT_STATUS = BLOCKED`

Use when a missing/conflicting material dependency prevents the requested conclusion and no safe reduced scope exists.

A user instruction to `continue anyway` does not convert material blockage into readiness.

## 9. Receipt validity and proportional revalidation

A valid receipt becomes:

```text
RECEIPT_VALIDITY: STALE_REVALIDATION_REQUIRED
```

when a material event can change its correctness, including:

- project switch;
- material task/effective-scope change;
- target/object/ref change;
- environment change;
- SES contract/ref change affecting the task;
- consumer-project live-ref change affecting the task;
- specialist source/ref change;
- continuity invalidation;
- authority or mutation-scope change;
- new contradictory/superseding evidence.

Revalidate only invalidated or newly material dependencies.

`STALE_RECEIPT -> REVALIDATE MATERIAL DEPENDENCIES -> NEW RECEIPT`

A mere project selection has no readiness receipt to invalidate.

## 10. Mandatory fail-closed states

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

Adapter/project/bootstrap/specialist/continuity/authority states become applicable only after a substantive task activates project materialization.

Missing evidence must never become inferred project fact or broad PASS.

## 11. Project-switch isolation

A project switch invalidates prior project-scoped context for the new project.

`PROJECT_SWITCH -> INVALIDATE PRIOR PROJECT-SCOPED CONTEXT`

Do not carry over authority, environments, decisions, runtime state, specialist overrides, security assumptions, continuity or project-local facts.

For multi-project substantive tasks, resolve each project independently and preserve source boundaries. Each materialized project receives its own receipt or independently identifiable receipt section.

## 12. Evidence binding and retrieval proportionality

Material claims bind to evidence sufficient for the task.

Preserve exact SES refs and, after project materialization, exact consumer-project refs used for material evidence.

Search results, snippets, prior summaries, prior receipts and user assertions do not prove canonical source reading.

Use progressive disclosure:

`TASK -> CLAIMS -> PROOF OBLIGATIONS -> MATERIAL SURFACES -> TARGETED RETRIEVAL`

Do not ingest an entire repository merely because a project was selected.

## 13. Authority boundary

Context grants context only.

```text
AUTHORITY_MODEL_STATUS != MUTATION_AUTHORIZATION_STATUS
CONTEXT_READY != AUTHORIZED_TO_MUTATE
TOOL_CAPABILITY != AUTHORIZATION
```

Resolve project-owned authority only when material to the substantive task. A mutation request always requires explicit applicable authorization for exact scope/target/environment.

A write-capable tool never grants authority by itself.

## 14. Proof levels and runtime mechanism boundary

Keep separate:

```text
SPEC_CONFORMANCE
CANDIDATE_HEAD_PROTOCOL_PROOF
RUNTIME_BEHAVIORAL_PROOF
```

- `SPEC_CONFORMANCE`: contract/bootstrap/tests are internally coherent.
- `CANDIDATE_HEAD_PROTOCOL_PROOF`: exact candidate head demonstrates the required read-only resolution behavior while preserving canonical and candidate refs.
- `RUNTIME_BEHAVIORAL_PROOF`: actual specialist/loading mechanism executes every runtime-required canonical case, including fresh conversation behavior.

Required cases that are `NOT_EXECUTED`, `SKIPPED`, `INDETERMINATE` or failed prevent runtime PASS.

Specification quality or candidate-head feasibility is not runtime PASS.

## 15. Acceptance criteria

A hybrid specialist is acceptable only if it demonstrates:

1. one ordered flow regardless of how project identity/task are supplied;
2. deterministic project resolution;
3. live numbered enumeration when project is absent;
4. transient menu-bound numeric mapping;
5. project selection stops before consumer-project materialization when task is absent;
6. no Context Readiness Receipt for selection-only interaction;
7. task arrival resumes the same flow and triggers only task-material project loading;
8. project+task supplied together traverses the same stages without an artificial wait;
9. explicit separation among project listing, selection, bootstrap, specialist readiness, context readiness and authority;
10. no fuzzy project inference;
11. fail-closed behavior for material unresolved states;
12. cross-project isolation;
13. task/target/environment-bound receipts only for substantive work;
14. deterministic `READY`, `LIMITED`, `BLOCKED`;
15. proportional revalidation after material changes;
16. historical failures preserved without retroactive PASS;
17. candidate/canonical refs preserved when applicable;
18. fresh-conversation repeatability;
19. proof-level separation;
20. no runtime PASS while any runtime-required case remains unexecuted or failed.

Canonical behavioral cases are defined in `tests/behavioral/HYBRID_SPECIALIST_BOOTSTRAP_TESTS.md`.
