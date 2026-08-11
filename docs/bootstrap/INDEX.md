# Specialist Engineering System — Bootstrap Index

**Status:** FOUNDATION_V0_1 / DOCUMENTATION_ONLY
**Repository:** `wagnerjfjunior/Specialist-Engineering-System`

This index defines the minimum reconstruction order for material work on SES itself and for SES-mediated work on a registered consumer project.

## 1. Resolve SES live state

Before material architecture, protocol, specialist, validation, project-adapter or release decisions:

1. resolve the live SHA of SES `main`;
2. read this file on the exact resolved ref;
3. read the material SES contracts on that same ref;
4. do not substitute memory, prior conversation, screenshots or copied project state for the repository source;
5. keep SES state distinct from consumer-project state.

If the required repository state cannot be resolved, declare `SES_BOOTSTRAP_UNAVAILABLE` and do not make a material canonical claim.

When validating a contract that exists only on a PR head, identify that explicitly as candidate-head evidence. Do not call the candidate canonical on SES `main` until merged.

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
2. define the current bounded `TASK_SCOPE`;
3. resolve the project identifier through `projects/REGISTRY.md`;
4. obtain one unique `PROJECT_ID` and `ADAPTER_PATH` from the registry;
5. read the registered Project Adapter at that exact path;
6. use the adapter only to locate the consumer project's canonical source and entrypoints;
7. resolve the consumer project's live canonical ref;
8. execute the project-local bootstrap protocol;
9. execute the project-local continuity protocol when current-state continuity is material;
10. resolve the applicable specialist/project-local rules;
11. resolve project authority sources material to the task;
12. resolve live evidence material to the task;
13. for hybrid specialists, emit the task-bound Context Readiness Receipt required by `core/protocols/HYBRID_SPECIALIST_BOOTSTRAP_CONTRACT.md`;
14. only then perform project-specific substantive work within that receipt's scope.

Do not use fuzzy project-name guessing for material resolution. Zero matches = `PROJECT_NOT_REGISTERED`; multiple matches = `PROJECT_ID_AMBIGUOUS`.

A conversation starter such as "Which project are we working on?" is UX only. It is not a security boundary and does not replace registry/adapter/bootstrap resolution.

## 4. Task-bound readiness and revalidation

A readiness receipt applies only to the exact task and material evidence to which it was bound.

`READY_FOR_TASK_A != READY_FOR_TASK_B`

Do not reuse a prior `READY` as session-wide project certification.

When any of the following becomes material, re-evaluate the receipt and revalidate the affected dependencies:

- project switch;
- material task/scope change;
- SES contract/ref change affecting the task;
- consumer-project live-ref change affecting current-state work;
- specialist source/ref change;
- continuity invalidation event;
- authority model or mutation-scope change;
- material environment/target-ref change;
- new contradictory or superseding evidence.

Use:

```text
RECEIPT_VALIDITY: STALE_REVALIDATION_REQUIRED
```

until the newly material/invalidated evidence has been resolved and a new receipt is emitted.

Revalidation must be proportional. Do not replay unrelated gates or reread immutable evidence solely because an unrelated ref changed.

## 5. Fail-closed project entry

Project-specific work must not proceed as established project context when any of the following is unresolved and material to the task:

- project identity;
- project registry mapping;
- project adapter;
- canonical source;
- project bootstrap entrypoint;
- specialist/project-local rules;
- required authority model/boundary source;
- material current-state source when continuity is required;
- live evidence required for the requested decision.

Use explicit states such as:

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

## 6. Source-of-truth and authority boundary

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

## 7. Proof-level integrity

Keep these conclusions separate:

```text
SPEC_CONFORMANCE
CANDIDATE_HEAD_PROTOCOL_PROOF
RUNTIME_BEHAVIORAL_PROOF
```

A coherent specification or successful read-only resolution chain on a candidate PR head does not prove that a future Custom GPT, Action/API loader or other runtime mechanism actually satisfies the behavior.

Runtime behavioral PASS requires execution by the actual specialist/loading mechanism under the test conditions, including fresh-conversation proof where required.

## 8. Change discipline

For material SES changes:

`one PR = one primary risk = one simple rollback`

Creating or updating SES documentation does not authorize mutation in any consumer project. Central evolution does not automatically mutate or upgrade registered projects.
