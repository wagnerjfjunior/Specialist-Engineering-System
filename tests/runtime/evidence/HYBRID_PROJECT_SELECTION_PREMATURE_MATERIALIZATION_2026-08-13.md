# SES — Hybrid Project Selection Premature Materialization Finding — 2026-08-13

**Evidence class:** USER_OBSERVED_RUNTIME / ARCHITECTURAL_FINDING
**Canonicalization status:** evidence record only; does not itself establish runtime PASS
**Affected specialists:** `SES — Documentation Auditor`, `SES — SaaS Architect`
**SES canonical main during observations:** `b8886501b0bd4ea7a8d2b39c605241a60e381701`

## 1. Purpose

Preserve the runtime observations that caused the deferred-project-materialization correction without rewriting them after the fix.

## 2. Builder state independently shown by user screenshots

### Documentation Auditor

Observed Builder Instructions header:

```text
SES — Documentation Auditor Builder Kernel
Status: RUNTIME_CANDIDATE_V0_2 / COMPACT_BUILDER_INSTRUCTIONS
Target archetype: documentation-auditor
```

Observed starter:

`# CLIQUE PARA INICIAR`

### SaaS Architect

Observed Builder Instructions header:

```text
SES — Universal Hybrid Specialist Builder Kernel
Status: RUNTIME_CANDIDATE_V0_1 / BUILDER_INSTRUCTIONS_SOURCE
Target archetype: saas-architect
```

Observed starter:

`# CLIQUE PARA INICIAR`

Therefore:

```text
STARTER_CHANGE_APPLIED: YES
DOCUMENTATION_AUDITOR_NEW_TARGET_KERNEL_APPLIED: NO
SAAS_ARCHITECT_NEW_TARGET_KERNEL_APPLIED: NO
```

## 3. Documentation Auditor observations

### Project option 1 — FECH.AI

Observed:
- project menu displayed;
- numeric selection `1` resolved FECH.AI;
- SES ref reported `b8886501b0bd4ea7a8d2b39c605241a60e381701`;
- FECH.AI main reported `5c36ded26a0d675fd080a72ecde50f407566b309`;
- project-local Documentation Auditor resolved;
- project bootstrap/current-state material was loaded;
- response bounded readiness to connection/bootstrap only.

User reported the interaction took roughly two minutes before the next prompt became available.

### Project option 2 — Blogs/Sites/Portais/SEO

Observed:
- numeric selection `2` resolved `blogs-sites-portais-seo`;
- project main reported `8c7f3380582b9c2f2997600c746e9054978ff64d`;
- project-local Documentation Auditor resolved;
- response bounded readiness to connection/bootstrap.

User reported roughly two minutes of processing.

The Blogs/SEO SHA was independently rechecked through GitHub during the SES analysis and matched the live project main at that time.

## 4. SaaS Architect observations

### Initial starter attempt

Input:

`# CLIQUE PARA INICIAR`

Actual response was generic onboarding asking the user to provide a project/repository/problem rather than the required live numbered project menu.

Classification:

```text
P01 ATTEMPT 1: FAIL
FAILURE_CLASS: BUILDER_KERNEL_DRIFT / V0_1_INSTRUCTIONS_STILL_APPLIED
RETROACTIVE_PASS: NO
```

### Later FECH.AI selection

Observed:
- project menu displayed;
- option `1` resolved FECH.AI;
- FECH.AI main and project-local SaaS Architect were resolved before a substantive task;
- readiness was bounded to connection/bootstrap.

### Later Blogs/SEO selection

Observed:
- option `2` resolved Blogs/SEO;
- runtime processed project bootstrap, lifecycle/authority and specialist material before a substantive task;
- final response reported project main `8c7f3380582b9c2f2997600c746e9054978ff64d`;
- project-local architect `gpt1` was resolved.

User-observed wall time:

`4 minutes 10 seconds`

This wall time is not independently instrumented by SES and must be treated as user-observed timing.

## 5. Finding

The material issue is not the exact wall-clock duration. The deterministic behavioral defect is:

```text
PROJECT_SELECTED
+ TASK_SCOPE_NOT_SUPPLIED
-> CONSUMER_PROJECT_MAIN / BOOTSTRAP / LOCAL_SPECIALIST / AUTHORITY-CONTINUITY RETRIEVAL
```

The system performed project materialization before it had a substantive task whose proof obligations could determine which project sources were material.

Consequences:
- avoidable latency;
- unnecessary GitHub/API calls;
- unnecessary context consumption;
- authority/lifecycle retrieval unrelated to any current decision;
- risk of ceremonial bulk loading.

## 6. Corrective invariant

```text
NO SUBSTANTIVE TASK
-> NO CONSUMER-PROJECT MATERIALIZATION
```

After project selection:

```text
PROJECT_SELECTION_STATUS: RESOLVED
PROJECT_ID: selected project
TASK_SCOPE: NOT_YET_SUPPLIED
NEXT_REQUIRED_INPUT: TASK
```

No Project Adapter, consumer-project ref, project bootstrap, local specialist, continuity, authority/governance, project evidence or Context Readiness Receipt is required until a substantive task exists.

## 7. Regression proof obligation

Wall-clock latency is supplementary evidence only.

Deterministic regression criterion:

```text
P02 / P03:
CONSUMER_PROJECT_ACTION_CALLS_BEFORE_TASK = 0
RECEIPT_EMITTED = NO
```

When a substantive task arrives:
- the same flow resumes;
- project materialization begins;
- retrieval is proportional to task proof obligations;
- a task-bound receipt precedes substantive work.

## 8. Historical preservation

A later corrected PASS does not rewrite:
- SaaS Architect P01 attempt 1 FAIL;
- older Builder-version observations;
- premature-materialization observations;
- user-observed timing.

The corrected runtime must append new evidence.
