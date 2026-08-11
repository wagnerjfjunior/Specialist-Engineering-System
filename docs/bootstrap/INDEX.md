# Specialist Engineering System — Bootstrap Index

**Status:** FOUNDATION_V0_1 / DOCUMENTATION_ONLY
**Repository:** `wagnerjfjunior/Specialist-Engineering-System`

This index defines the minimum reconstruction order for material work on SES itself and for SES-mediated work on a registered consumer project.

## 1. Resolve SES live state

Before material architecture, protocol, specialist, validation, project-adapter or release decisions:

1. resolve the live SHA of SES `main` as `SES_CANONICAL_MAIN_REF`;
2. determine the declared proof level;
3. for ordinary/canonical work, use `SES_EFFECTIVE_REF = SES_CANONICAL_MAIN_REF`;
4. for candidate-head validation, preserve the exact candidate head separately as `SES_CANDIDATE_REF` and use it as `SES_EFFECTIVE_REF` without calling it canonical `main`;
5. read this file and the material SES contracts on the exact `SES_EFFECTIVE_REF`;
6. do not substitute memory, prior conversation, screenshots or copied project state for repository evidence;
7. keep SES state distinct from consumer-project state.

If the required SES bootstrap cannot be resolved on the applicable effective ref, declare `SES_BOOTSTRAP_UNAVAILABLE` and do not make a material canonical/readiness claim.

`CANDIDATE_HEAD != CANONICAL_MAIN`

## 2. Material SES foundation sources

Read when applicable:

- `docs/architecture/ARCHITECTURE_BOUNDARY.md`
- `projects/REGISTRY.md`
- `core/protocols/PROJECT_ADAPTER_CONTRACT.md`
- `core/protocols/PROJECT_BOOTSTRAP_CONTRACT.md`
- `core/protocols/PROJECT_CONTINUITY_CONTRACT.md`
- `core/protocols/HYBRID_SPECIALIST_BOOTSTRAP_CONTRACT.md` for hybrid/multi-project specialist work

Behavioral validation of the hybrid bootstrap contract is defined in:

- `tests/behavioral/HYBRID_SPECIALIST_BOOTSTRAP_TESTS.md`

Future archetype, specialist, validation and versioning contracts must be reached from this bootstrap rather than becoming independent entrypoints.

## 3. Consumer-project resolution

Before project-specific specialist work:

1. collect or identify the project name/ID explicitly;
2. define the full requested `TASK_SCOPE`;
3. classify `TARGET_REF_OR_OBJECT` and `ENVIRONMENT`, using `NOT_REQUIRED_FOR_THIS_TASK` only when genuinely immaterial;
4. resolve the project identifier through `projects/REGISTRY.md`;
5. obtain one unique `PROJECT_ID` and `ADAPTER_PATH` from the registry;
6. read the registered Project Adapter at that exact path;
7. use the adapter only to locate the consumer project's canonical source and entrypoints;
8. resolve the consumer project's live canonical ref;
9. execute the project-local bootstrap protocol;
10. resolve the applicable specialist/project-local rules and overrides;
11. read project-local common rules and authority/governance sources when applicable;
12. execute the project-local continuity protocol when current-state continuity is material;
13. resolve live evidence material to the exact task/target/environment;
14. for hybrid specialists, emit the task-bound Context Readiness Receipt required by `core/protocols/HYBRID_SPECIALIST_BOOTSTRAP_CONTRACT.md`;
15. only then perform project-specific substantive work within the receipt's effective scope.

This order is normative for hybrid SES-mediated work and aligns with `core/protocols/PROJECT_BOOTSTRAP_CONTRACT.md`:

```text
PROJECT BOOTSTRAP
-> SPECIALIST / PROJECT-LOCAL RULES
-> COMMON RULES / AUTHORITY WHEN APPLICABLE
-> CONTINUITY WHEN CURRENT STATE MATTERS
-> MATERIAL LIVE OBJECTS
```

Do not use fuzzy project-name guessing for material resolution. Zero matches = `PROJECT_NOT_REGISTERED`; multiple matches = `PROJECT_ID_AMBIGUOUS`.

A conversation starter such as "Which project are we working on?" is UX only. It is not a security boundary and does not replace registry/adapter/bootstrap resolution.

## 4. Task-bound readiness semantics

A readiness receipt applies only to the exact task, effective scope, target, environment and material evidence to which it was bound.

`READY_FOR_TASK_A != READY_FOR_TASK_B`

For hybrid specialists:

```text
CONTEXT_STATUS: READY
```

means the entire requested `TASK_SCOPE` can be completed safely and `EFFECTIVE_SCOPE` is materially equivalent to it.

```text
CONTEXT_STATUS: LIMITED
```

means the full requested scope cannot be completed, but an explicit strict subset recorded as `EFFECTIVE_SCOPE` can be completed safely and the excluded portion is identified in `GAPS`.

```text
CONTEXT_STATUS: BLOCKED
```

means a material gap/conflict prevents the requested decision and no safe reduced scope has been established.

An irrelevant source classified `NOT_REQUIRED_FOR_THIS_TASK` does not by itself make a task `LIMITED`.

## 5. Receipt invalidation and proportional revalidation

Do not reuse a prior `READY` as session-wide project certification.

When any of the following becomes material, re-evaluate the receipt and revalidate the affected dependencies:

- project switch;
- material task/effective-scope change;
- target ref/object change;
- environment change;
- SES canonical/effective contract/ref change affecting the task;
- consumer-project live-ref change affecting current-state work;
- specialist source/ref change;
- continuity invalidation event;
- authority model or mutation-scope change;
- new contradictory or superseding evidence.

Use:

```text
RECEIPT_VALIDITY: STALE_REVALIDATION_REQUIRED
```

until the newly material/invalidated evidence has been resolved and a new receipt is emitted.

Revalidation must be proportional. Do not replay unrelated gates or reread immutable evidence solely because an unrelated ref changed.

## 6. Fail-closed project entry

Project-specific work must not proceed as established project context when any of the following is unresolved and material to the task:

- SES bootstrap on the applicable effective ref;
- project identity;
- project registry mapping;
- project adapter;
- canonical source;
- project bootstrap entrypoint;
- specialist/project-local rules;
- required authority model/boundary source;
- material current-state source when continuity is required;
- live evidence required for the requested decision;
- unresolved conflict between material project sources;
- applicable mutation authorization when a mutation is requested.

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

For hybrid specialists:

`NO VERIFIED PROJECT CONTEXT -> NO PROJECT-SPECIFIC SUBSTANTIVE WORK`

## 7. Source-of-truth and authority boundary

SES owns reusable engineering contracts and project registration metadata.

The consumer project owns its own:

- product/project truth;
- live operational state;
- authority;
- environments;
- current decisions;
- runtime evidence;
- project-local specialist rules.

The Project Registry maps identifiers to adapters. A Project Adapter points to project-owned sources. Neither may duplicate consumer-project truth.

A successful bootstrap establishes context only. It does not grant mutation authority.

```text
AUTHORITY_MODEL_STATUS
!=
MUTATION_AUTHORIZATION_STATUS
```

`CONTEXT_READY != AUTHORIZED_TO_MUTATE`

A write-capable tool does not authorize a mutation. A requested mutation without explicit applicable authorization must not execute.

## 8. Proof-level integrity

Keep these conclusions separate:

```text
SPEC_CONFORMANCE
CANDIDATE_HEAD_PROTOCOL_PROOF
RUNTIME_BEHAVIORAL_PROOF
```

For candidate-head proof, preserve both:

```text
SES_CANONICAL_MAIN_REF
SES_CANDIDATE_REF
```

and identify `SES_EFFECTIVE_REF` explicitly.

A coherent specification or successful read-only resolution chain on a candidate PR head does not prove that a future Custom GPT, Action/API loader or other runtime mechanism satisfies the behavior.

`RUNTIME_BEHAVIORAL_PROOF = PASS` requires the actual specialist/loading mechanism to execute every runtime-required canonical case in `tests/behavioral/HYBRID_SPECIALIST_BOOTSTRAP_TESTS.md`. Any required `NOT_EXECUTED`, `SKIPPED`, `INDETERMINATE` or failed case prevents runtime PASS.

## 9. Change discipline

For material SES changes:

`one PR = one primary risk = one simple rollback`

Creating or updating SES documentation does not authorize mutation in any consumer project. Central evolution does not automatically mutate or upgrade registered projects.
