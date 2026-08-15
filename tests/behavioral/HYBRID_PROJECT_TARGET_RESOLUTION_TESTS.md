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
- no numbered menu or numeric-binding mechanism may be introduced unless the case is an explicit informational-list request, and even then list positions must not become project identity;
- no consumer project may be materialized before explicit identity exists;
- no SES-self inference is allowed from specialist identity alone.

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

Input explicitly names a registered consumer project.

Expected:

- continue through deterministic Project Registry/Adapter/bootstrap flow;
- do not ask missing-target clarification;
- do not generate a project-choice menu;
- preserve all normal readiness/authority rules.

### TR05 — explicit informational project-list request

Input explicitly asks which consumer projects are registered.

Expected:

- registry enumeration is permitted for the informational answer;
- project list is not readiness;
- no Project Adapter/consumer project is materialized solely because it was listed;
- no persistent/transient numeric binding is created;
- a later bare number is not accepted as project identity unless the number is an actual canonical ID/alias.

## 4. Cross-case invariants

```text
TARGET_IDENTIFIED != PROJECT_CONTEXT_READY
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
EXPLICIT_TARGET_NOT_RESPECTED
```

A failure remains historical even if a later fresh attempt passes.
