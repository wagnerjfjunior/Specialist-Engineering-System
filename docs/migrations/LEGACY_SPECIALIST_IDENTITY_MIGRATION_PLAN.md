# SES — Legacy Specialist Identity Migration Plan v0.1

**Status:** `CANONICAL_MIGRATION_PLAN_V0_1 / NO_AUTOMATIC_RENAME`  
**Purpose:** normalize legacy GPT-number and obsolete specialist labels without rewriting history, breaking project continuity or creating retroactive PASS.

## 1. Problem

Several consumer-project sources still use historical identities such as:

- `GPT0`, `GPT1`, `GPT2`, ...;
- `SES SaaS Architect` / `SaaS Architect`;
- project-specific specialist names whose current SES equivalent is an archetype identity.

The current SES model resolves specialists by canonical name and `ARCHETYPE_ID`. Legacy labels are continuity/history pointers only.

## 2. Migration invariants

```text
LEGACY_LABEL != CANONICAL_IDENTITY
MIGRATION != HISTORY_REWRITE
ADOPTION != LEGACY_BUILDER_RETIREMENT
RENAME != BEHAVIORAL_EQUIVALENCE
CURRENT_CERTIFICATION != HISTORICAL_GPT_PASS
USER_CORRECTED / INITIAL_OVERCLAIM remains preserved
RETROACTIVE_PASS = NO
```

No legacy Builder, skill, test or evidence may be deleted or reclassified solely because a new SES archetype exists.

## 3. Migration units

Migration must occur per consumer project and per role.

For each legacy identity:

1. resolve the project live;
2. resolve the current legacy artifact and its authority;
3. identify the intended SES `ROLE -> ARCHETYPE_ID`;
4. classify equivalence as `EXACT`, `PARTIAL`, `OVERLAPPING`, `NO_EQUIVALENT` or `NOT_DETERMINED`;
5. preserve historical Builder IDs, URLs, tests and evidence;
6. add canonical mapping without deleting history;
7. execute any required project-local compatibility tests;
8. obtain explicit retirement authorization before retiring a legacy Builder;
9. record migration evidence and final state.

## 4. Current known legacy surfaces

### FECH.AI

The SES Project Adapter already maps canonical roles while preserving legacy aliases such as `GPT0`, `GPT1`, `GPT1.5`, `GPT2` and `GPT3`.

Target direction:
- keep legacy aliases only as continuity pointers;
- use canonical SES role/archetype names in new SES-mediated work;
- do not retire FECH.AI-local Builder/contracts until project-local equivalence and retirement gates are satisfied.

### Blogs-sites-portais-seo

The consumer repository currently maintains a project-local registry organized as `gpt0` through `gpt8`.

This is a project-local legacy registry and must not be treated as the canonical SES portfolio taxonomy.

Target direction:
- preserve `config/gpts.yaml` until an explicit migration is executed;
- map project-local functions to adopted SES archetypes where equivalence exists;
- retain local-only functions when no canonical SES archetype exists;
- do not rename or retire Builders solely from archetype adoption;
- require explicit project migration/retirement decisions.

### MoreNumTegra

Use current SES role mappings in the Project Adapter. Historical labels, if encountered, remain continuity-only unless project sources declare otherwise.

## 5. Identity precedence

For SES-mediated material work:

```text
1. ARCHETYPE_ID
2. CANONICAL_NAME
3. explicit ROLE -> ARCHETYPE_ID mapping
4. explicit registered alias
5. project-local legacy label only after project bootstrap
```

Never use fuzzy matching from `GPT<number>` to an archetype.

## 6. Required migration evidence

A completed migration should record:

- project and immutable refs;
- legacy identity;
- canonical role/archetype;
- equivalence classification;
- artifacts preserved;
- tests executed;
- Builder/runtime fingerprint if affected;
- adoption status;
- retirement status;
- explicit user/project authorization;
- post-merge verification.

## 7. Retirement gate

A legacy specialist may be marked retired only when all applicable conditions are satisfied:

- canonical replacement is explicit;
- project adoption is explicit;
- project-local compatibility/equivalence is demonstrated when material;
- no required local capability is lost;
- affected runtime tests pass;
- historical evidence remains addressable;
- explicit retirement authorization exists.

`CANONICAL_REPLACEMENT_EXISTS != LEGACY_SPECIALIST_RETIRED`.

## 8. Non-goals

This plan does not:
- rename consumer-project files automatically;
- mutate Custom GPT Builders automatically;
- delete project-local registries;
- infer that every legacy GPT has a one-to-one SES replacement;
- convert project-specific rules into universal SES rules;
- force immediate migration.

## 9. Completion condition

The migration program is complete only when active consumer projects use canonical SES identities for new routing while all retained legacy identities are explicitly classified as continuity-only, project-local-only or intentionally active exceptions.

Until then, mixed nomenclature is a known migration state, not evidence that the canonical SES registry is obsolete.
