# SES — Next Safe Action

> Este é o registro atual autoritativo da única próxima ação segura do SES.

**Next action ID:** `apply-deferred-project-materialization-runtime-targets-v1`
**Primary target:** `SES — Documentation Auditor` v0.4
**Affected target:** `SES — SaaS Architect` v0.3
**Canonical source:** `wagnerjfjunior/Specialist-Engineering-System` / `main` resolved live

## Why this supersedes the prior action

Runtime exploration of the standardized project-entry flow exposed a material interaction defect: after project selection and before any substantive task, both specialists could materialize consumer projects, including project live ref, bootstrap and local specialist/authority sources.

User-observed waits were approximately two minutes for Documentation Auditor selections and 4m10s for SaaS Architect Blogs/SEO. Those wall times are user observations, not independently instrumented platform timings.

The deterministic architectural defect is independent of timing:

`PROJECT_SELECTED + NO SUBSTANTIVE TASK -> CONSUMER-PROJECT MATERIALIZATION OCCURRED`

The corrected contract requires:

`NO SUBSTANTIVE TASK -> NO CONSUMER-PROJECT MATERIALIZATION`

Therefore:
- Documentation Auditor target advances from v0.3 to v0.4;
- SaaS Architect target advances from v0.2 to v0.3;
- shared project-entry runtime cases advance from P01–P08 to P01–P10;
- SaaS Architect v0.1 historical runtime PASS remains preserved;
- SaaS v0.2 P01 failure and the premature-materialization observations remain historical evidence.

## Action

After this change is canonical on SES `main`, apply the exact new compact kernels to the two external Builders in this order:

1. `SES — Documentation Auditor` v0.4;
2. `SES — SaaS Architect` v0.3.

For each target:

1. resolve SES `main` live;
2. read the exact current Builder profile/kernel;
3. verify the kernel character count and complete-copy requirement;
4. obtain explicit Product Authority authorization for the exact external Builder mutation if not already granted;
5. change only the fields authorized and required by the target;
6. capture a fresh non-secret Builder fingerprint;
7. execute fresh P01, P02, P03, P09 and P10 before broader behavioral proof;
8. preserve every prior FAIL/observation without retroactive PASS.

## Critical expected behavior

```text
# CLIQUE PARA INICIAR
-> live SES menu
-> user selects project
-> PROJECT_SELECTED
-> zero consumer-project materialization calls
-> ask for task

task arrives
-> same ordered flow resumes
-> task-proportional project materialization
-> Context Readiness Receipt
-> substantive work
```

Direct project identifier without task must reach the same `PROJECT_SELECTED / WAIT_FOR_TASK` state.

## Version-bound evidence

```text
SAAS_V0_1_RUNTIME_BEHAVIORAL_PROOF: PASS / HISTORICAL / PRESERVED
SAAS_V0_2_RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
SAAS_V0_2_P01_ATTEMPT_1: FAIL / BUILDER_KERNEL_DRIFT
SAAS_V0_3_RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED

DOCUMENTATION_AUDITOR_V0_4_RUNTIME_BEHAVIORAL_PROOF: NOT_ESTABLISHED
```

## Done condition

This semantic action is complete when both external Builders:
- are materially equivalent to their new target profiles;
- have fresh fingerprints;
- pass the targeted selection-deferral regression cases P01/P02/P03/P09/P10 without erasing prior failures.

This does not itself establish full runtime behavioral certification.

## Limits

This record does not itself authorize:
- external Builder mutation without explicit Product Authority authorization;
- publication/sharing changes;
- consumer-project mutation;
- write-capable production Actions;
- runtime behavioral certification;
- project-local equivalence promotion;
- legacy specialist retirement.

## Anti-loop

Do not reopen/downgrade SaaS v0.1 historical PASS.

Do not rerun unrelated gates merely because the project-entry target version changed.

Replace this record only after this semantic action completes, is materially invalidated or is explicitly superseded.
