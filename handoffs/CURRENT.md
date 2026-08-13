# SES — Current Handoff

**Status:** `SFJM_OPERATIONAL_CONTINUITY_V0_1 / MATERIAL_RECORDED_STATE`  
**Canonical source:** `wagnerjfjunior/Specialist-Engineering-System`  
**Canonical ref rule:** resolve `main` live before material work  
**SFJM method source:** `wagnerjfjunior/StopJuniorMode@d03d477c3b329aa973a38ec4e949c249fa017929`  
**Continuity contract:** `core/protocols/PROJECT_CONTINUITY_CONTRACT.md`  
**Authoritative next action:** `docs/NEXT_SAFE_ACTION.md`  
**Next action ID:** `apply-deferred-project-materialization-runtime-targets-v1`

## 1. Purpose

Preserve minimum durable operational meaning for SES without making conversation history authoritative or duplicating volatile consumer-project state.

Consumer-project truth, continuity and authority remain project-owned.

## 2. Reading order

1. resolve SES `main` live and read `docs/bootstrap/INDEX.md`;
2. read `handoffs/CURRENT.md`;
3. read `docs/PROJECT_STATUS.md`;
4. read `docs/NEXT_SAFE_ACTION.md`;
5. read `docs/BLOCKED_ACTIONS.md`;
6. then read task-material contracts/runtime evidence.

## 3. Confirmed durable state

1. SES remains project-agnostic.
2. Active archetypes: `saas-architect`, `documentation-auditor`.
3. SaaS Architect v0.1 historical runtime PASS remains preserved at T01–T29 = 29/29.
4. SaaS Architect v0.2 was a target version but was not fully applied; user evidence shows external Builder Instructions remained v0.1 and the first new-starter P01 attempt failed.
5. SaaS Architect v0.3 is the new target.
6. Documentation Auditor external Builder was observed with v0.2 Instructions while later Core behavior enabled the new menu; v0.4 is the new target.
7. Both external Builders use `# CLIQUE PARA INICIAR`.
8. Runtime exploration showed project selection could trigger consumer-project materialization before a substantive task, creating avoidable latency.
9. New canonical intent: selection resolves only `PROJECT_ID`; no Project Adapter/project main/bootstrap/local specialist/continuity/authority/evidence or readiness receipt until a substantive task exists.
10. Shared runtime-required project-entry cases are P01–P10 for the new targets.
11. External Builder application, runtime proof, publication, consumer equivalence and retirement remain separate lifecycle states.

## 4. Core interaction invariant

```text
# CLIQUE PARA INICIAR
-> SES live/bootstrap/archetype
-> Project Registry
-> numbered menu
-> user selects
-> PROJECT_SELECTED
-> WAIT FOR TASK

TASK ARRIVES
-> same flow resumes
-> task-proportional project materialization
-> task-bound Context Readiness Receipt
-> work
```

Direct project identifier without task reaches the same `PROJECT_SELECTED / WAIT FOR TASK` state.

`NO SUBSTANTIVE TASK -> NO CONSUMER-PROJECT MATERIALIZATION`

## 5. Historical runtime evidence preserved

User observations on 2026-08-13:
- Documentation Auditor menu/selection worked with older Builder Instructions after Core v0.2 was canonical;
- SaaS Architect first starter attempt with v0.1 Instructions failed to present the project menu;
- later selections that materialized projects before task showed user-observed waits around two minutes (Documentation Auditor) and 4m10s (SaaS Architect Blogs/SEO).

These timings are not independently instrumented. They are preserved as user-observed evidence; P02/P03 use zero pre-task consumer-project calls as the deterministic regression criterion.

## 6. Live state versus recorded state

`LIVE_RESOLVED_STATE != MATERIAL_RECORDED_STATE`

Resolve live when material: SES refs, PR state, external Builder config, model, access boundary, publication state and consumer-project refs.

Do not rewrite historical proof because a new target version exists.

## 7. Current next action

Authoritative source: `docs/NEXT_SAFE_ACTION.md`.

Derived summary: after this change is canonical, apply/reconcile Documentation Auditor v0.4 then SaaS Architect v0.3, with explicit Product Authority required for external Builder mutation, then run targeted P01/P02/P03/P09/P10 regressions before broader proof.

This handoff does not authorize publication, consumer-project mutation, runtime certification or legacy retirement.

## 8. Short resume prompt

```text
SES -> resolve main live -> bootstrap -> continuity -> preserve SaaS v0.1 PASS + v0.2 FAIL history -> new targets DA v0.4 / SaaS v0.3 -> no task means no consumer-project materialization -> apply Builders only with explicit authorization -> run P01/P02/P03/P09/P10 -> no automatic runtime PASS.
```
