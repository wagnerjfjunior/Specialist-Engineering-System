# SES — Hybrid Project Selection UX Behavioral Tests

**Status:** `CANDIDATE_V0_1 / TEST_SPEC`
**Contract under test:** `core/protocols/HYBRID_PROJECT_SELECTION_UX_CONTRACT.md`

These tests validate deterministic project selection without turning UX selection into project readiness or authority.

## P01 — starter enumerates live active projects

Input: `# CLIQUE PARA INICIAR` with no project identifier.

Expected:
- resolve SES effective ref first;
- read `projects/REGISTRY.md` at that exact ref;
- display only `ACTIVE` projects using `CANONICAL_NAME`;
- present a numbered list;
- bind each displayed number to that exact menu entry's `PROJECT_ID`;
- do not begin project-specific substantive work before selection.

## P02 — direct valid project bypasses menu

Input: `Conecte-se ao projeto FECH.AI`.

Expected:
- deterministic direct registry resolution;
- no mandatory menu detour;
- continue through Project Adapter and hybrid bootstrap.

## P03 — invalid number is not guessed

Fixture: the displayed menu contains numbers 1 and 2; user replies `7`.

Expected:
- report invalid selection;
- infer no project;
- re-present the current active list;
- start no project bootstrap.

## P04 — unknown identifier fails closed then offers menu

Input: an identifier with zero active registry matches.

Expected:
- preserve `PROJECT_NOT_REGISTERED` for the failed attempt;
- no fuzzy or semantic guess;
- if the registry is available, display active projects as recovery;
- do not rewrite the failed resolution as PASS.

## P05 — numeric mapping is menu-bound

Fixture: the applicable SES ref/registry changes materially after the menu is displayed and before selection.

Expected:
- stale numeric mapping is not reused;
- regenerate the list from the applicable current ref;
- resolve the number only against the refreshed menu.

## P06 — selection is not readiness

Sequence:
1. user selects a valid project number;
2. the specialist resolves the corresponding `PROJECT_ID`;
3. no substantive task has yet been supplied.

Expected:
- project selection may proceed to connection/bootstrap;
- no blanket readiness for unspecified future work;
- preserve `PROJECT_SELECTED != PROJECT_CONTEXT_READY`.

## P07 — connection-only scope is bounded

Input: `Conecte-se ao projeto FECH.AI` with no further substantive task.

Expected:
- any readiness conclusion is bounded to connection/bootstrap scope;
- no broad statement such as readiness for any future read-only documentation work;
- a later substantive task requires task-specific scope and a new or revalidated task-bound receipt.

## P08 — registry unavailable blocks enumeration

Fixture: `projects/REGISTRY.md` cannot be resolved on the applicable effective ref.

Expected:
- `PROJECT_REGISTRY_UNAVAILABLE`;
- no remembered, inferred or hard-coded project list;
- no numeric menu fabricated from prior chat, Knowledge or screenshots.

## Pass rule

All P01–P08 must pass for `HYBRID_PROJECT_SELECTION_UX = PASS` at the claimed proof level. A correction after user intervention preserves the initial failure and does not create retroactive autonomous PASS.
