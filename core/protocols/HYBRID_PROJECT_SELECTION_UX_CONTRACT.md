# SES — Hybrid Project Selection UX Contract

**Status:** `CANDIDATE_V0_1 / CORE_PROTOCOL`

## Purpose

Define deterministic project selection for SES hybrid specialists when no valid registered project identifier has been supplied. Selection is UX and resolution only; it does not establish project readiness or mutation authority.

`PROJECT_SELECTED != PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE`

## Triggers

Apply when:
- the conversation starts through `# CLIQUE PARA INICIAR`;
- the user asks to start/connect/work without identifying a project;
- a supplied project identifier is unknown or ambiguous under the SES Project Registry.

A valid explicit project identifier may resolve directly through the canonical Project Registry without displaying the menu.

## No project supplied

1. Resolve SES `main` live and select the applicable `SES_EFFECTIVE_REF`.
2. Read `projects/REGISTRY.md` on that exact ref.
3. Enumerate only entries whose `STATUS` is `ACTIVE`.
4. Display each active project once using `CANONICAL_NAME` in a numbered list.
5. Retain the exact `PROJECT_ID` associated with each displayed number.
6. Ask the user to choose one displayed number.
7. Do not begin consumer-project bootstrap or project-specific substantive work before a valid selection.

The numeric mapping is transient and bound to the exact list displayed. Never hard-code a permanent mapping such as `1 = fechai`.

Recommended rendering:

```text
Selecione o projeto em que deseja trabalhar:

1. <CANONICAL_NAME A>
2. <CANONICAL_NAME B>

Digite o número do projeto.
```

## Numeric selection

Resolve a numeric reply only against the most recently displayed canonical registry menu. Map it to that entry's `PROJECT_ID`. An out-of-range choice must not be guessed; report invalid selection and re-present the current active list. If the applicable SES ref/registry materially changed before selection, regenerate the list.

A numeric answer has no project meaning outside the menu instance that created it.

## Explicit identifier

Apply canonical registry rules: exact `PROJECT_ID`, otherwise exact `CANONICAL_NAME` or explicit `ALIAS` case-insensitively; never fuzzy-match. Exactly one active match may continue directly to hybrid bootstrap.

## Unknown or ambiguous identifier

Preserve `PROJECT_NOT_REGISTERED` or `PROJECT_ID_AMBIGUOUS`; do not guess. If the registry is available, show the current numbered active-project list as a recovery path and wait for valid selection. Showing the menu does not rewrite the original failed resolution as PASS.

## Selection is not readiness

After valid selection continue:

`PROJECT_ID → Project Adapter → consumer live canonical source → project bootstrap → project-local specialist rules → authority/governance/continuity when material → task-material evidence → task-bound Context Readiness Receipt`.

If the user requested only connection/bootstrap and no substantive task, readiness may be assessed only for that bounded connection/bootstrap scope. Do not emit blanket readiness for future unspecified work.

`READY_FOR_PROJECT_CONNECTION != READY_FOR_UNSPECIFIED_FUTURE_TASKS`

A later substantive task requires a task-specific `TASK_SCOPE`, material dependency classification and a new or revalidated task-bound receipt.

## Registry unavailable

If the registry cannot be resolved, emit `PROJECT_REGISTRY_UNAVAILABLE`. Do not invent a list from memory, prior conversation, Knowledge, screenshots or hard-coded names.

## Project switch and authority

A project switch invalidates prior project-scoped authority, continuity, environment, verdict vocabulary, specialist overrides and readiness as required by the hybrid bootstrap contract. Bootstrap the new project independently.

`CONVERSATION_STARTER != CONFIGURATION_AUTHORITY`
`PROJECT_SELECTION != POLICY_AUTHORITY`
`PROJECT_SELECTION != MUTATION_AUTHORIZATION`

Consumer projects remain authoritative for their own truth, local rules, continuity and authorization model.
