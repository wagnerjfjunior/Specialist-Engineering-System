# SES — Hybrid Project Target Resolution Contract

**Status:** FOUNDATION_V0_1 / CONTRACT

## 1. Purpose

Define deterministic behavior before Project Registry resolution when a hybrid SES specialist does not yet have an explicit task target or consumer-project identifier.

This contract exists to prevent two unsafe/ambiguous fallbacks:

1. inferring that SES itself is the task target merely because the specialist belongs to SES;
2. reconstructing the retired numbered-menu / numeric-selection / cross-turn project-entry flow when project identity is missing.

It supplements `core/protocols/HYBRID_SPECIALIST_BOOTSTRAP_CONTRACT.md` and does not replace project-owned bootstrap, authority or continuity.

## 2. Target classes

Classify the requested target before consumer-project materialization:

```text
EXPLICIT_SES_TARGET
EXPLICIT_CONSUMER_PROJECT_TARGET
MISSING_CONSUMER_PROJECT_IDENTIFIER
AMBIGUOUS_SES_OR_CONSUMER_TARGET
```

### `EXPLICIT_SES_TARGET`

Use only when the user explicitly names SES, `Specialist-Engineering-System`, an SES repository path/ref/PR/object, or another unambiguous SES-owned artifact as the task target.

Being inside an SES specialist, mentioning `bootstrap`, `specialist`, `documentation`, `architecture`, or saying `current` does not by itself make SES the target.

### `EXPLICIT_CONSUMER_PROJECT_TARGET`

Use when the user explicitly supplies one or more consumer-project identifiers as the task target, regardless of whether those identifiers ultimately resolve in the canonical Project Registry.

Target classification answers whether the user supplied an identifier; registry resolution separately decides whether each supplied identifier is registered, active, unique and usable.

```text
IDENTIFIER_SUPPLIED != PROJECT_RESOLVED
```

A misspelled, inactive, ambiguous or unregistered supplied identifier must continue to the canonical registry resolver and produce the applicable outcome such as `PROJECT_NOT_REGISTERED`, `PROJECT_ID_AMBIGUOUS` or another existing fail-closed state. Do not reclassify a supplied identifier as missing merely because resolution fails.

### `MISSING_CONSUMER_PROJECT_IDENTIFIER`

Use when the task is substantively about a consumer project but no project identifier was supplied.

### `AMBIGUOUS_SES_OR_CONSUMER_TARGET`

Use when the requested work could reasonably target SES itself or a consumer project and the user did not identify which target is intended.

## 3. Mandatory clarification-only behavior

For `MISSING_CONSUMER_PROJECT_IDENTIFIER`:

```text
PROJECT_IDENTIFIER: NOT_SUPPLIED
PROJECT_RESOLUTION_STATUS: PROJECT_IDENTIFIER_REQUIRED
```

Respond with one direct clarification equivalent to:

`Qual projeto consumidor registrado devo usar?`

Then STOP.

For `AMBIGUOUS_SES_OR_CONSUMER_TARGET`, ask one direct clarification equivalent to:

`Você quer tratar o próprio SES ou qual projeto consumidor registrado?`

Then STOP.

Before the clarification is answered, do not:

- enumerate `projects/REGISTRY.md` merely to offer choices;
- generate a numbered project menu;
- assign transient numeric bindings;
- interpret a bare number as project identity;
- infer SES as the target;
- infer a consumer project from prior chat, memory, sidebar/project context or semantic similarity;
- read a Project Adapter or consumer-project source;
- emit a project Context Readiness Receipt;
- produce project-specific substantive findings, verdicts, risks or recommendations.

This is a clarification-only interaction, not a project-selection state machine.

## 4. Explicit informational listing request

Project enumeration is permitted only when the user explicitly asks which consumer projects are registered/available, requests a project list, or asks to compare **registry metadata/list membership only**.

This exception does **not** apply to a substantive task that explicitly identifies two or more consumer projects for comparison, audit, architecture work or another material analysis. Such a multi-project task must follow the multi-project isolation semantics of `core/protocols/HYBRID_SPECIALIST_BOOTSTRAP_CONTRACT.md`: resolve each supplied project independently and preserve independently identifiable readiness/source boundaries.

Informational enumeration is never project selection:

```text
PROJECT_LISTED != PROJECT_SELECTED
PROJECT_LIST_POSITION != PROJECT_IDENTIFIER
```

Do not persist number-to-project bindings. A later bare numeric reply is not a valid `PROJECT_IDENTIFIER` unless that number is itself an explicit canonical ID/alias in the registry.

If a project-specific task follows an informational list, require the user to identify the project by canonical name, `PROJECT_ID`, or explicit alias before materialization.

## 5. Consumer-project materialization

Only after one or more explicit consumer-project identifiers exist may the hybrid specialist continue to canonical registry resolution.

For a single-project task:

```text
projects/REGISTRY.md
→ deterministic unique active project resolution
→ Project Adapter
→ consumer live canonical source
→ project bootstrap/local specialist
→ material authority/continuity/evidence
→ task-bound Context Readiness Receipt
→ project-specific substantive work
```

For an explicitly multi-project substantive task, resolve each supplied project independently through the same chain and preserve separate project-scoped receipt/evidence boundaries before synthesis.

Registry resolution remains exact-ID / exact canonical-name / explicit-alias only. No fuzzy or inferred project resolution is added by this contract.

## 6. SES self-work

When `EXPLICIT_SES_TARGET` is established, perform SES-owned bootstrap/self-continuity as applicable without pretending SES is a registered consumer project.

Do not route SES self-work through a consumer Project Adapter unless the task separately and explicitly includes a consumer project.

## 7. Stop-loss precedence

The following interaction remains retired:

```text
# CLIQUE PARA INICIAR
→ live numbered project menu
→ numeric selection
→ PROJECT_SELECTED
→ WAIT FOR TASK
→ cross-turn resume
```

Any older reference to `selection-only interaction`, menu selection, transient numeric mapping or cross-turn project selection must not be interpreted as authority to recreate that flow.

For current targets, the only permitted no-project pre-materialization behavior is direct clarification under section 3, except for an explicit informational listing request under section 4.

## 8. Evidence and authority boundary

Target clarification establishes only task identity.

```text
TARGET_IDENTIFIED != PROJECT_CONTEXT_READY
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
```

A conversation starter, clarification answer, project list or prior receipt does not prove adapter/bootstrap/readiness and does not grant mutation authority.

## 9. Required regression behavior

A runtime target satisfies this contract only if behavioral tests demonstrate all of:

```text
GENERIC_OR_AMBIGUOUS_BOOTSTRAP_TASK_WITHOUT_TARGET
→ DIRECT CLARIFICATION
→ NO SES SELF-INFERENCE
→ NO PROJECT ENUMERATION
→ NO NUMERIC BINDING
→ NO PROJECT MATERIALIZATION
→ NO SUBSTANTIVE AUDIT

CONSUMER_PROJECT_TASK_WITHOUT_IDENTIFIER
→ PROJECT_IDENTIFIER_REQUIRED
→ DIRECT CLARIFICATION
→ STOP

EXPLICIT_INFORMATIONAL_PROJECT_LIST
→ LIST MAY BE RETURNED
→ BARE NUMERIC FOLLOW-UP MUST NOT BECOME PROJECT_IDENTIFIER
→ NO NUMERIC BINDING
→ NO PROJECT MATERIALIZATION FROM LIST POSITION

EXPLICIT_BUT_UNREGISTERED_IDENTIFIER
→ EXPLICIT_CONSUMER_PROJECT_TARGET
→ CANONICAL REGISTRY RESOLUTION
→ PROJECT_NOT_REGISTERED or other applicable fail-closed resolver state

EXPLICIT_MULTI_PROJECT_SUBSTANTIVE_TASK
→ EACH PROJECT RESOLVED INDEPENDENTLY
→ NO INFORMATIONAL-LIST SHORT-CIRCUIT
→ PROJECT-SCOPED RECEIPT/EVIDENCE BOUNDARIES PRESERVED
```

Any autonomous numbered-menu response used as a required project-entry mechanism or any numeric list-position binding is a behavioral failure even if no mutation occurs.

Canonical contract-level cases are defined in:

`tests/behavioral/HYBRID_PROJECT_TARGET_RESOLUTION_TESTS.md`

Runtime candidates may add stricter archetype-specific regressions, but they may not weaken this contract.
