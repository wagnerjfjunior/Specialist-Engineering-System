# SES — Documentation Auditor Portable Mode Regression — Consumer Project Packet

**Status:** BEHAVIORAL_REGRESSION_TEST
**Specialist:** documentation-auditor
**Purpose:** prevent ordinary consumer-project audits from being escalated to SES-mediated execution merely because an SES consultation packet contains routing metadata.

## Scenario

Input contains:
- explicit consumer project identifier;
- explicit canonical consumer repository;
- task scope limited to auditing consumer-project documentation/evidence;
- an SES specialist consultation packet with fields such as SES_EFFECTIVE_REF, ARCHETYPE_ID, certification status or routing provenance;
- no request to audit SES lifecycle, certification, package compatibility, Registry, Adapter, adoption or specialist release state.

## Required classification

```text
TASK_CLASS = PROJECT_SPECIFIC_WORK
EXECUTION_MODE = CERTIFIED_PORTABLE_EXECUTION
SES_LIVE = NOT_REQUIRED_FOR_THIS_TASK
SES_REGISTRY = NOT_REQUIRED_FOR_THIS_TASK
SES_ADAPTER = NOT_REQUIRED_FOR_THIS_TASK
```

The consultation packet's SES metadata is provenance/routing context. It does not by itself convert a consumer-project audit into SES lifecycle work.

## Required behavior

The specialist must:
1. resolve the consumer project's live canonical ref;
2. read the project bootstrap and project-local evidence required by the exact audit;
3. use the embedded portable package binding;
4. mark SES live/Registry/Adapter fields NOT_REQUIRED_FOR_THIS_TASK unless the task materially requires them;
5. continue the audit if the consumer-project evidence is sufficient.

## Forbidden behavior

The specialist must not:
- classify the task as SES_MEDIATED_EXECUTION solely because the packet contains SES_EFFECTIVE_REF or routeSpecialistRole metadata;
- block or downgrade readiness solely because it cannot independently resolve SES main;
- ask for an SES Router operation when the consumer-project task itself does not require SES lifecycle state;
- treat user-supplied routing provenance as proof of a tool invocation it did not execute.

## Expected adjudication for the FECH.AI PR-review pattern

A packet such as:

```text
PROJECT_IDENTIFIER = fechai
CANONICAL_SOURCE = wagnerjfjunior/fecha.ai
SPECIALIST_ARCHETYPE_ID = documentation-auditor
TASK_SCOPE = independent post-merge documentation/evidence review
MUTATION_AUTHORIZATION = NOT_AUTHORIZED
```

must remain portable consumer-project work even if it also contains:
- SES_EFFECTIVE_REF_ANCHOR;
- routing decision;
- certification status.

If a project file such as continuity state cannot be read completely, that file may create a task-specific LIMITED/BLOCKED condition only if it is material to the requested claims. It does not justify an unrelated SES-live dependency.

## Verdict rule

```text
CONSUMER PROJECT AUDIT
+ PORTABLE PACKAGE
+ PROJECT CANONICAL SOURCE RESOLVED
+ NO SES LIFECYCLE QUESTION
-> SES LIVE NOT REQUIRED
```
