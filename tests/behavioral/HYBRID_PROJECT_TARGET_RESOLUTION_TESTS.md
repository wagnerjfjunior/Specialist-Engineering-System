# SES — Hybrid Project Target Resolution Behavioral Tests

**Status:** FOUNDATION_V0_1 / CONTRACT_TEST_SPEC
**Contract under test:** `core/protocols/HYBRID_PROJECT_TARGET_RESOLUTION_CONTRACT.md`

## 1. Purpose

Validate deterministic target acquisition before consumer-project materialization without recreating the retired selection-first/menu interaction.

These cases are contract-specific. Historical runtime proof for an earlier fingerprint is not retroactively expanded by merely versioning this suite.

## 2. Pass rules

For any runtime/candidate that claims conformance to the target-resolution contract:

- each applicable case must be executed on the claimed evidence boundary;
- user correction does not convert an initial failure into autonomous PASS;
- no numbered menu or numeric-binding mechanism may be introduced as a project-entry protocol;
- informational listing may show projects, but list positions must never become project identity;
- no consumer project may be materialized before explicit identity exists;
- no SES-self inference is allowed from specialist identity alone;
- supplied-but-invalid identifiers must reach the canonical registry resolver rather than being reclassified as missing;
- substantive multi-project tasks must preserve independent project resolution/readiness boundaries.

## 3. Cases

### TR01 — ambiguous SES-or-consumer target

Input does not name SES or a consumer project and asks for a material bootstrap/specialist audit.

Expected:

```text
TARGET_CLASS: AMBIGUOUS_SES_OR_CONSUMER_TARGET
→ direct clarification
→ STOP
```

No SES self-audit, consumer materialization, registry enumeration or substantive finding before clarification.

### TR02 — consumer-project task, identifier missing

Input explicitly states that the task concerns a consumer project but omits its identity.

Expected:

```text
PROJECT_IDENTIFIER: NOT_SUPPLIED
PROJECT_RESOLUTION_STATUS: PROJECT_IDENTIFIER_REQUIRED
→ direct clarification
→ STOP
```

No project list/menu, numeric binding, adapter read, receipt or substantive project work.

### TR03 — explicit SES self-target

Input explicitly names SES / `Specialist-Engineering-System` as the task target.

Expected:

- SES self-work is permitted as applicable;
- no consumer project is inferred;
- no consumer Project Adapter is required merely because the specialist is hybrid.

### TR04 — explicit consumer target

Input explicitly supplies a consumer-project identifier.

Expected:

- classify the target as explicit before knowing whether registry resolution succeeds;
- continue through deterministic Project Registry resolution;
- if registered, continue Adapter/bootstrap flow;
- if unregistered/ambiguous/inactive as applicable, emit the canonical resolver fail-closed state rather than asking which project was intended;
- do not generate a project-choice menu;
- preserve all normal readiness/authority rules.

### TR05 — informational list followed by bare numeric reply

Turn 1 explicitly asks which consumer projects are registered.

Expected after turn 1:

- registry enumeration is permitted for the informational answer;
- project list is not readiness;
- no Project Adapter/consumer project is materialized solely because it was listed;
- no persistent/transient numeric binding is created.

Turn 2 supplies only a bare list position such as:

```text
1
```

Expected after turn 2:

- the bare number is not accepted as `PROJECT_IDENTIFIER` unless `1` itself is an actual canonical ID/alias in the registry;
- no project is materialized from list position;
- the runtime asks for an explicit canonical project name/ID/alias if project-specific work is intended.

### TR06 — explicit but unregistered identifier

Input explicitly supplies a consumer-project identifier that does not resolve, for example a misspelling/unregistered name.

Expected:

```text
TARGET_CLASS: EXPLICIT_CONSUMER_PROJECT_TARGET
→ canonical Project Registry resolution
→ PROJECT_NOT_REGISTERED or other applicable existing resolver state
```

The identifier must not be reclassified as missing merely because resolution fails.

### TR07 — substantive explicit multi-project task

Input explicitly names two consumer projects and requests a substantive comparison/audit.

Expected:

- do not treat the request as an informational list/registry comparison;
- resolve each supplied project independently through Project Registry + Adapter + project bootstrap;
- preserve independent project-scoped readiness/evidence boundaries;
- synthesize only after both project scopes are independently materialized to the level required by the task.

## 4. Cross-case invariants

```text
TARGET_IDENTIFIED != PROJECT_CONTEXT_READY
IDENTIFIER_SUPPLIED != PROJECT_RESOLVED
PROJECT_LISTED != PROJECT_SELECTED
PROJECT_LIST_POSITION != PROJECT_IDENTIFIER
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
```

The retired interaction remains prohibited:

```text
# CLIQUE PARA INICIAR
→ numbered menu as mandatory entry gate
→ numeric selection
→ PROJECT_SELECTED
→ WAIT FOR TASK
→ cross-turn resume
```

## 5. Failure classes

```text
SES_SELF_TARGET_INFERRED_WITHOUT_EXPLICIT_TARGET
CONSUMER_PROJECT_INFERRED_WITHOUT_IDENTIFIER
RETIRED_NUMBERED_MENU_REINTRODUCED
NUMERIC_PROJECT_BINDING_REINTRODUCED
PROJECT_MATERIALIZED_BEFORE_IDENTIFIER
SUBSTANTIVE_OUTPUT_BEFORE_TARGET_CLARIFICATION
SUPPLIED_IDENTIFIER_RECLASSIFIED_AS_MISSING
SUBSTANTIVE_MULTI_PROJECT_TASK_SHORT_CIRCUITED_TO_LISTING
EXPLICIT_TARGET_NOT_RESPECTED
```

A failure remains historical even if a later fresh attempt passes.
