# Specialist Engineering System — Bootstrap Index

**Status:** RUNTIME_CANDIDATE_V0_1 / BOOTSTRAP_INDEX
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

## 2. Material SES sources

Read when applicable:

- `docs/architecture/ARCHITECTURE_BOUNDARY.md`
- `projects/REGISTRY.md`
- `archetypes/REGISTRY.md` for specialist/archetype resolution
- the exact archetype contract resolved by `archetypes/REGISTRY.md`
- `core/protocols/PROJECT_ADAPTER_CONTRACT.md`
- `core/protocols/PROJECT_BOOTSTRAP_CONTRACT.md`
- `core/protocols/PROJECT_CONTINUITY_CONTRACT.md`
- `core/protocols/HYBRID_SPECIALIST_BOOTSTRAP_CONTRACT.md` for hybrid/multi-project specialist work
- `core/protocols/HYBRID_PROJECT_TARGET_RESOLUTION_CONTRACT.md` when target/project identity is missing, ambiguous, or project enumeration is requested
- `core/protocols/EVIDENCE_RETRIEVAL_RESILIENCE_CONTRACT.md` when large-file, large-tree, truncation, incomplete transport or context-budget risk is material

Behavioral validation of hybrid bootstrap/target resolution is defined in:

- `tests/behavioral/HYBRID_SPECIALIST_BOOTSTRAP_TESTS.md`
- `tests/behavioral/HYBRID_PROJECT_TARGET_RESOLUTION_TESTS.md`

For the `saas-architect` Custom GPT runtime candidate, also read when validating/applying/testing that candidate:

- `runtime/custom-gpt/SAAS_ARCHITECT_BUILDER_PROFILE.md`
- `runtime/custom-gpt/SAAS_ARCHITECT_BUILDER_KERNEL.md`
- `runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`
- `tests/runtime/HYBRID_SAAS_ARCHITECT_RUNTIME_RUNBOOK.md`
- `tests/runtime/HYBRID_SAAS_ARCHITECT_FIXTURES.md`

For the `documentation-auditor` Custom GPT runtime candidate, also read when validating/applying/testing that candidate:

- `runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_PROFILE.md`
- `runtime/custom-gpt/DOCUMENTATION_AUDITOR_BUILDER_KERNEL.md`
- `runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml`
- `tests/runtime/DOCUMENTATION_AUDITOR_RUNTIME_RUNBOOK.md`
- `tests/runtime/DOCUMENTATION_AUDITOR_PROJECT_TARGET_REGRESSION.md`
- `tests/behavioral/DOCUMENTATION_AUDITOR_TESTS.md`
- `core/protocols/EVIDENCE_RETRIEVAL_RESILIENCE_CONTRACT.md` when the task or runtime case exercises retrieval resilience

For `ux-ui-app-specialist`, first resolve the active archetype through `archetypes/REGISTRY.md` and read:

- `archetypes/ux-ui-app-specialist/ARCHETYPE.md`

For its validated v0.1 runtime fingerprint, also read when configuring/applying/testing or auditing that runtime:

- `runtime/custom-gpt/UX_UI_APP_SPECIALIST_BUILDER_PACKAGE_V0_1.md`
- `runtime/custom-gpt/UX_UI_APP_SPECIALIST_BUILDER_KERNEL_V0_1.md`
- `runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml` when GitHub is applied
- `tests/runtime/UX_UI_APP_SPECIALIST_L2_RUNTIME_PROFILE_V0_1.md`
- `tests/runtime/UX_UI_APP_SPECIALIST_L2_RUNBOOK_V0_1.md`
- `tests/behavioral/UX_UI_APP_SPECIALIST_L1C_VALIDATION_V0_1.md`
- `tests/runtime/evidence/UX_UI_APP_SPECIALIST_L2_RUNTIME_PROOF_2026-08-16.md`
- `tests/behavioral/UX_UI_APP_SPECIALIST_ARCHETYPE_RESOLUTION_V0_1.md`

The UX/UI APP Specialist is an active reusable archetype when the live `archetypes/REGISTRY.md` resolves `ux-ui-app-specialist` with `RESOLUTION_STATUS: ACTIVE`. Its Builder/runtime PASS remains fingerprint-bound and its activation does not imply automatic consumer-project adoption or mutation authority.

Future archetype, specialist, validation and versioning contracts must be reached from this bootstrap rather than becoming independent entrypoints.

## 3. Archetype resolution

Before a reusable SES specialist performs material specialist work:

1. read `archetypes/REGISTRY.md` on `SES_EFFECTIVE_REF`;
2. resolve the requested `ARCHETYPE_ID` deterministically;
3. read the exact `CONTRACT_PATH` returned by the registry;
4. fail closed if no unique active archetype resolves;
5. for project-specific work, continue to project resolution rather than treating archetype resolution as project readiness.

```text
ARCHETYPE_RESOLVED
!=
PROJECT_CONTEXT_READY
```

A project-local specialist identity/override must be resolved from the consumer project's canonical sources after project bootstrap. Do not freeze consumer-project specialist identities into the universal archetype registry.

## 4. Target and consumer-project resolution

Before consumer-project materialization, establish whether the user explicitly targeted SES itself, explicitly identified a consumer project, omitted a required consumer-project identifier, or left the target ambiguous between SES and a consumer project.

Apply `core/protocols/HYBRID_PROJECT_TARGET_RESOLUTION_CONTRACT.md` before reading `projects/REGISTRY.md` when target/project identity is missing or ambiguous.

Mandatory pre-registry rule:

```text
MISSING CONSUMER PROJECT IDENTIFIER
→ DIRECT CLARIFICATION
→ STOP

AMBIGUOUS SES OR CONSUMER TARGET
→ DIRECT CLARIFICATION
→ STOP
```

Do not infer SES as the target merely because the specialist belongs to SES. Do not enumerate the Project Registry merely to offer choices. Project enumeration is permitted only when the user explicitly asks which projects are available; list position never becomes project identity.

Once a consumer project is explicit, continue:

1. record the explicit project name/ID;
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

A conversation starter is UX only. It is not a security boundary and does not replace explicit target identity, registry/adapter/bootstrap resolution or readiness.

## 5. Task-bound readiness semantics

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

## 6. Receipt invalidation and proportional revalidation

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
- Builder/kernel/action/model change affecting a runtime behavioral claim;
- new contradictory or superseding evidence.

Use:

```text
RECEIPT_VALIDITY: STALE_REVALIDATION_REQUIRED
```

until the newly material/invalidated evidence has been resolved and a new receipt is emitted.

Revalidation must be proportional. Do not replay unrelated gates or reread immutable evidence solely because an unrelated ref changed.

## 7. Fail-closed project entry

Project-specific work must not proceed as established project context when any of the following is unresolved and material to the task:

- SES bootstrap on the applicable effective ref;
- requested archetype when archetype behavior is required;
- explicit target/project identity;
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
- `PROJECT_IDENTIFIER_REQUIRED`
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

Do not invent missing project context or target identity.

For hybrid specialists:

`NO VERIFIED PROJECT CONTEXT -> NO PROJECT-SPECIFIC SUBSTANTIVE WORK`

## 8. Source-of-truth and authority boundary

SES owns reusable engineering contracts, archetype contracts, runtime-candidate configuration specifications and project registration metadata.

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

The first `SES — SaaS Architect` runtime candidate intentionally uses a GitHub READ_ONLY Action; its schema contains no write operations.

## 9. Runtime-candidate integrity

Keep these lifecycle states separate:

```text
VERSIONED_PROFILE
BUILDER_APPLIED
PREVIEW_TESTED
RUNTIME_BEHAVIORAL_PROOF
PUBLISHED
```

Versioning a Builder profile/kernel/action schema in SES does not prove it has been applied externally.

Before runtime testing of any SES Custom GPT candidate:

1. resolve the applicable runtime candidate sources from this bootstrap and, when active, its archetype registry entry;
2. read the exact versioned Builder package/profile and kernel;
3. capture the Builder fingerprint required by that package/profile;
4. resolve the Action schema actually applied;
5. execute the runtime runbook and canonical behavioral suite applicable to that candidate/archetype;
6. keep any candidate-specific resilience/fixture requirements separate and explicit.

No Builder secret/token may be committed to SES.

## 10. Proof-level integrity

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

`RUNTIME_BEHAVIORAL_PROOF = PASS` requires the actual configured specialist/loading mechanism to execute every runtime-required canonical case in the behavioral suite applicable to the resolved candidate/archetype, plus any additional runtime/resilience cases that the applicable runbook marks mandatory for the claimed readiness scope. Any required `NOT_EXECUTED`, `SKIPPED`, `INDETERMINATE` or failed case prevents the corresponding runtime/readiness PASS.

Do not substitute one archetype's behavioral suite for another archetype's runtime proof.

## 11. Change discipline

For material SES changes:

`one PR = one primary risk = one simple rollback`

Creating or updating SES documentation/runtime specifications does not authorize mutation in any consumer project or external GPT Builder. Central evolution does not automatically mutate or upgrade registered projects.

## 12. SES self-continuity / SFJM operational layer

For material work on **SES itself** when current operational continuity is relevant, this bootstrap also resolves the SES-owned SFJM continuity layer:

1. `handoffs/CURRENT.md`;
2. `docs/PROJECT_STATUS.md`;
3. `docs/NEXT_SAFE_ACTION.md`;
4. `docs/BLOCKED_ACTIONS.md`.

`docs/NEXT_SAFE_ACTION.md` is the sole authoritative record of the current semantic next safe action for SES. Bootstrap, handoff and project status may contain only derived summaries of that action.

If a derived summary conflicts materially with the authoritative next-action record or with a newer live authoritative source, stop and reconcile before execution.

The continuity model follows:

```text
LIVE_RESOLVED_STATE
!=
MATERIAL_RECORDED_STATE
```

Volatile repository, review, Builder, environment and consumer-project facts must be resolved live when material. Continuity is updated only when a material objective, decision, blocker, proof state, authority boundary or semantic next action changes; ordinary commits and conversation changes do not force a continuity rewrite.

This SES self-continuity layer does **not** replace consumer-project continuity. Registered projects remain authoritative for their own state and are still resolved through `projects/REGISTRY.md`, the applicable Project Adapter and project-owned bootstrap/continuity sources.

The operational method was adopted from the SFJM canonical bootstrap protocol in `wagnerjfjunior/StopJuniorMode` at baseline `d03d477c3b329aa973a38ec4e949c249fa017929`. That repository is a method/reference source for this adoption, not the authority for SES project state. Future SFJM evolution does not automatically mutate SES; changes require a deliberate versioned SES change.
