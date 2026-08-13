# Specialist Engineering System — Bootstrap Index

**Status:** RUNTIME_CANDIDATE_V0_3 / BOOTSTRAP_INDEX
**Repository:** `wagnerjfjunior/Specialist-Engineering-System`

This index defines the minimum reconstruction order for material SES work and SES-mediated work on registered consumer projects.

## 1. Resolve SES live state

Before material architecture, protocol, specialist, validation, project-adapter or release decisions, and before a hybrid specialist presents a live project menu:

1. resolve live SES `main` as `SES_CANONICAL_MAIN_REF`;
2. determine proof level;
3. ordinary/canonical work -> `SES_EFFECTIVE_REF = SES_CANONICAL_MAIN_REF`;
4. candidate-head validation -> preserve `SES_CANDIDATE_REF` separately and use it as `SES_EFFECTIVE_REF` without calling it canonical `main`;
5. read this index and task-material SES contracts on that exact ref;
6. do not substitute memory, prior chat, screenshots or copied project state for repository evidence;
7. keep SES state distinct from consumer-project state.

If required SES bootstrap cannot be resolved, use `SES_BOOTSTRAP_UNAVAILABLE`; do not fabricate a project menu or material readiness.

`CANDIDATE_HEAD != CANONICAL_MAIN`

## 2. Material SES sources

Read when applicable:

- `docs/architecture/ARCHITECTURE_BOUNDARY.md`
- `projects/REGISTRY.md`
- `archetypes/REGISTRY.md`
- exact archetype contract resolved by the registry
- `core/protocols/PROJECT_ADAPTER_CONTRACT.md`
- `core/protocols/PROJECT_BOOTSTRAP_CONTRACT.md`
- `core/protocols/PROJECT_CONTINUITY_CONTRACT.md`
- `core/protocols/HYBRID_SPECIALIST_BOOTSTRAP_CONTRACT.md`
- `core/protocols/EVIDENCE_RETRIEVAL_RESILIENCE_CONTRACT.md` when retrieval risk is material

Hybrid behavioral validation:
- `tests/behavioral/HYBRID_SPECIALIST_BOOTSTRAP_TESTS.md`

SaaS Architect runtime:
- `runtime/custom-gpt/SAAS_ARCHITECT_BUILDER_PROFILE.md`
- `runtime/custom-gpt/UNIVERSAL_BUILDER_KERNEL.md`
- `runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`
- `tests/runtime/HYBRID_SAAS_ARCHITECT_RUNTIME_RUNBOOK.md`
- `tests/runtime/HYBRID_SAAS_ARCHITECT_FIXTURES.md`

Documentation Auditor runtime:
- `runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_PROFILE.md`
- `runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_KERNEL.md`
- `runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`
- `tests/runtime/DOCUMENTATION_AUDITOR_RUNTIME_RUNBOOK.md`
- `tests/behavioral/DOCUMENTATION_AUDITOR_TESTS.md`
- `tests/behavioral/HYBRID_SPECIALIST_BOOTSTRAP_TESTS.md`

Future contracts must remain reachable from this bootstrap rather than become competing entrypoints.

## 3. Archetype resolution

Before a reusable SES specialist performs material work or presents its project menu:

1. read `archetypes/REGISTRY.md` on `SES_EFFECTIVE_REF`;
2. resolve requested `ARCHETYPE_ID` deterministically;
3. read the exact `CONTRACT_PATH`;
4. fail closed if no unique active archetype resolves.

`ARCHETYPE_RESOLVED != PROJECT_CONTEXT_READY`

Project-local specialist identity/overrides remain consumer-project owned and are resolved only after a substantive task activates project materialization.

## 4. Consumer-project entry: selection first, materialization only for a task

Every hybrid specialist uses one ordered project-entry flow.

### 4.1 Resolve project identity

1. classify `PROJECT_IDENTIFIER` as user-supplied or `NOT_SUPPLIED`;
2. classify `TASK_SCOPE` as substantive or `NOT_YET_SUPPLIED`;
3. read `projects/REGISTRY.md` on exact `SES_EFFECTIVE_REF`;
4. execute project-resolution semantics from `core/protocols/HYBRID_SPECIALIST_BOOTSTRAP_CONTRACT.md`;
5. if project is absent, including `# CLIQUE PARA INICIAR`, display current `ACTIVE` projects by `CANONICAL_NAME` as a numbered list and wait for a valid selection;
6. if project was supplied directly, validate it through the same resolution stage;
7. obtain one unique `PROJECT_ID` and `ADAPTER_PATH`.

The menu is UX over the live registry. Never hard-code numbers.

```text
PROJECT_LISTED != PROJECT_SPECIALIST_READY
PROJECT_SELECTED != PROJECT_BOOTSTRAPPED
PROJECT_SELECTED != PROJECT_CONTEXT_READY
```

### 4.2 Stop when the task is absent

When:

```text
PROJECT_SELECTION_STATUS: RESOLVED
TASK_SCOPE: NOT_YET_SUPPLIED
```

stop before consumer-project materialization.

Do not yet:

- read the Project Adapter;
- resolve consumer-project `main`;
- read project bootstrap;
- resolve project-local specialist rules;
- read continuity;
- read authority/governance;
- retrieve project evidence;
- emit a Context Readiness Receipt.

Ask the user for the task.

`NO SUBSTANTIVE TASK -> NO CONSUMER-PROJECT MATERIALIZATION`

This stop is a state-machine gate, not a bypass.

### 4.3 Continue when a substantive task exists

Once a substantive `TASK_SCOPE` exists:

1. revalidate selected `PROJECT_ID` against the applicable live registry when material;
2. classify `TARGET_REF_OR_OBJECT` and `ENVIRONMENT`;
3. read the registered Project Adapter;
4. use it only to locate consumer canonical sources/entrypoints;
5. resolve consumer-project live canonical ref;
6. execute project-local bootstrap;
7. resolve applicable project-local specialist rules/overrides;
8. classify which downstream sources are material to the task;
9. read project-local common/authority/governance sources only when task-material or explicitly mandatory for every substantive task;
10. execute project continuity only when current state is material;
11. resolve live evidence material to exact task/target/environment;
12. emit the task-bound Context Readiness Receipt;
13. only then perform project-specific substantive work within `EFFECTIVE_SCOPE`.

Project bootstrap establishes source ordering and mandatory policy. It does not justify ceremonial retrieval of every referenced document when the task does not depend on it.

Use progressive disclosure:

`TASK -> CLAIMS -> PROOF OBLIGATIONS -> MATERIAL SURFACES -> TARGETED RETRIEVAL`

### 4.4 Project and task supplied together

If the user supplies both a resolvable project and substantive task in one request, traverse the same stages in order and continue directly into materialization. No alternate path is created.

Do not use fuzzy project guessing. Zero matches = `PROJECT_NOT_REGISTERED`; multiple matches = `PROJECT_ID_AMBIGUOUS`.

A starter such as `# CLIQUE PARA INICIAR` is UX input only; it is not project configuration, readiness or authority.

## 5. Task-bound readiness semantics

A Context Readiness Receipt exists only for substantive work.

`READY_FOR_TASK_A != READY_FOR_TASK_B`

`CONTEXT_STATUS: READY` means full requested `TASK_SCOPE` can be completed safely and `EFFECTIVE_SCOPE` is materially equivalent.

`CONTEXT_STATUS: LIMITED` means only an explicit strict safe subset can be completed and excluded scope is identified in `GAPS`.

`CONTEXT_STATUS: BLOCKED` means a material gap/conflict prevents the requested conclusion and no safe reduced scope exists.

An irrelevant source classified `NOT_REQUIRED_FOR_THIS_TASK` does not itself make a task `LIMITED`.

Project selection alone does not produce a readiness receipt.

## 6. Receipt invalidation and proportional revalidation

Do not reuse prior `READY` as session-wide project certification.

Re-evaluate when material:

- project switch;
- task/effective-scope change;
- target/object/ref change;
- environment change;
- SES contract/ref change affecting task;
- consumer live-ref change affecting task;
- specialist source/ref change;
- continuity invalidation;
- authority or mutation-scope change;
- Builder/kernel/action/model change affecting runtime proof;
- new contradictory/superseding evidence.

Use `RECEIPT_VALIDITY: STALE_REVALIDATION_REQUIRED` until affected dependencies are revalidated.

Do not replay unrelated gates or reread immutable evidence solely because an unrelated ref changed.

A selection-only state has no Context Readiness Receipt to reuse.

## 7. Fail-closed project entry

For substantive project-specific work, fail closed when material dependencies are unresolved, including:

- SES bootstrap;
- archetype;
- project registry mapping;
- Project Adapter;
- canonical source;
- project bootstrap;
- project-local specialist rules;
- authority model when material;
- continuity/current-state source when material;
- evidence required for decision;
- unresolved project-source conflict;
- mutation authorization when mutation is requested.

Use explicit states such as:

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

Do not invent missing project context.

`NO VERIFIED PROJECT CONTEXT -> NO PROJECT-SPECIFIC SUBSTANTIVE WORK`

## 8. Source-of-truth and authority boundary

SES owns reusable engineering contracts, archetypes, runtime-candidate specifications and project registration metadata.

Consumer projects own project truth, live state, authority, environments, decisions, runtime evidence and project-local specialist rules.

Project Registry maps identifiers to adapters. Adapters point to project-owned sources. Neither duplicates consumer truth.

Context does not grant mutation authority.

```text
AUTHORITY_MODEL_STATUS != MUTATION_AUTHORIZATION_STATUS
CONTEXT_READY != AUTHORIZED_TO_MUTATE
TOOL_CAPABILITY != AUTHORIZATION
```

## 9. Runtime-candidate integrity

Keep separate:

```text
VERSIONED_PROFILE
BUILDER_APPLIED
PREVIEW_TESTED
RUNTIME_BEHAVIORAL_PROOF
PUBLISHED
```

Before runtime testing:

1. resolve applicable archetype;
2. read exact Builder profile/kernel;
3. capture required Builder fingerprint;
4. resolve actual Action schema;
5. execute applicable runtime runbook and canonical suites;
6. preserve archetype-specific resilience/fixture obligations.

No Builder secret/token may be committed.

## 10. Proof-level integrity

Keep separate:

```text
SPEC_CONFORMANCE
CANDIDATE_HEAD_PROTOCOL_PROOF
RUNTIME_BEHAVIORAL_PROOF
```

For candidate-head proof preserve `SES_CANONICAL_MAIN_REF`, `SES_CANDIDATE_REF` and explicit `SES_EFFECTIVE_REF`.

Runtime PASS requires the actual configured specialist/loading mechanism to execute every runtime-required canonical case applicable to the target version. Any required `NOT_EXECUTED`, `SKIPPED`, `INDETERMINATE` or failed case prevents PASS.

Do not substitute one archetype's proof for another.

## 11. Change discipline

For material SES changes:

`one PR = one primary risk = one simple rollback`

Repository changes do not authorize mutation in consumer projects or external GPT Builders.

`CENTRAL EVOLUTION != AUTOMATIC RUNTIME MUTATION`

## 12. SES self-continuity

For material work on SES itself when operational continuity is relevant:

1. `handoffs/CURRENT.md`
2. `docs/PROJECT_STATUS.md`
3. `docs/NEXT_SAFE_ACTION.md`
4. `docs/BLOCKED_ACTIONS.md`

`docs/NEXT_SAFE_ACTION.md` is the sole authoritative semantic next action. Other continuity files are derived summaries.

`LIVE_RESOLVED_STATE != MATERIAL_RECORDED_STATE`

Resolve volatile repository, review, Builder, environment and consumer-project facts live when material.

This SES continuity layer does not replace consumer-project continuity.

The operational method was adopted from `wagnerjfjunior/StopJuniorMode` baseline `d03d477c3b329aa973a38ec4e949c249fa017929` as a reference method, not as authority for SES state. Future SFJM evolution does not automatically mutate SES.
