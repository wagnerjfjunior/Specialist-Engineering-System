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

## 2. Material SES foundation sources

Read when applicable:

- `docs/architecture/ARCHITECTURE_BOUNDARY.md`
- `projects/REGISTRY.md`
- `core/protocols/PROJECT_ADAPTER_CONTRACT.md`
- `core/protocols/PROJECT_BOOTSTRAP_CONTRACT.md`
- `core/protocols/PROJECT_CONTINUITY_CONTRACT.md`

Future archetype, specialist, validation and versioning contracts must be reached from this bootstrap rather than becoming independent entrypoints.

## 3. Consumer-project resolution

Before project-specific specialist work:

1. collect or identify the project name/ID explicitly;
2. resolve that identifier through `projects/REGISTRY.md`;
3. obtain one unique `PROJECT_ID` and `ADAPTER_PATH` from the registry;
4. read the registered Project Adapter at that exact path;
5. use the adapter only to locate the consumer project's canonical source and entrypoints;
6. resolve the consumer project's live canonical ref;
7. execute the project-local bootstrap protocol;
8. execute the project-local continuity protocol when current-state continuity is material;
9. resolve the applicable specialist/project-local rules;
10. only then perform project-specific substantive work.

Do not use fuzzy project-name guessing for material resolution. Zero matches = `PROJECT_NOT_REGISTERED`; multiple matches = `PROJECT_ID_AMBIGUOUS`.

A conversation starter such as "Which project are we working on?" is UX only. It is not a security boundary and does not replace registry/adapter/bootstrap resolution.

## 4. Fail-closed project entry

Project-specific work must not proceed as established project context when any of the following is unresolved:

- project identity;
- project registry mapping;
- project adapter;
- canonical source;
- project bootstrap entrypoint;
- required authority/boundary source;
- material current-state source when continuity is required.

Use explicit states such as:

- `PROJECT_REGISTRY_UNAVAILABLE`
- `PROJECT_NOT_REGISTERED`
- `PROJECT_ID_AMBIGUOUS`
- `PROJECT_ADAPTER_UNRESOLVED`
- `PROJECT_BOOTSTRAP_UNAVAILABLE`
- `PROJECT_CONTINUITY_UNAVAILABLE`
- `MISSING_EVIDENCE`

Do not invent missing project context.

## 5. Source-of-truth boundary

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

## 6. Change discipline

For material SES changes:

`one PR = one primary risk = one simple rollback`

Creating or updating SES documentation does not authorize mutation in any consumer project. Central evolution does not automatically mutate or upgrade registered projects.
