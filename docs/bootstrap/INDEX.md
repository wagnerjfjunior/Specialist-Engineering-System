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
- `core/protocols/PROJECT_ADAPTER_CONTRACT.md`
- `core/protocols/PROJECT_BOOTSTRAP_CONTRACT.md`
- `core/protocols/PROJECT_CONTINUITY_CONTRACT.md`

Future archetype, specialist, validation and versioning contracts must be reached from this bootstrap rather than becoming independent entrypoints.

## 3. Consumer-project resolution

Before project-specific specialist work:

1. identify the project explicitly;
2. resolve its registered adapter under `projects/<project-id>/PROJECT_ADAPTER.md`;
3. use the adapter only to locate the consumer project's canonical source and entrypoints;
4. resolve the consumer project's live canonical ref;
5. execute the project-local bootstrap protocol;
6. execute the project-local continuity protocol when current-state continuity is material;
7. resolve the applicable specialist/project-local rules;
8. only then perform project-specific substantive work.

A conversation starter such as "Which project are we working on?" is UX only. It is not a security boundary and does not replace adapter/bootstrap resolution.

## 4. Fail-closed project entry

Project-specific work must not proceed as established project context when any of the following is unresolved:

- project identity;
- canonical source;
- project bootstrap entrypoint;
- required authority/boundary source;
- material current-state source when continuity is required.

Use explicit states such as:

- `PROJECT_NOT_REGISTERED`
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

A project adapter must point to these sources, not duplicate them.

## 6. Change discipline

For material SES changes:

`one PR = one primary risk = one simple rollback`

Creating or updating SES documentation does not authorize mutation in any consumer project. Central evolution does not automatically mutate or upgrade registered projects.
