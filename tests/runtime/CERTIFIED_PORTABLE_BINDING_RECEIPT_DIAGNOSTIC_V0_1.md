# SES — Certified Portable Binding Receipt Diagnostic v0.1

**Status:** TARGETED_RUNTIME_DIAGNOSTIC / NO_RECERTIFICATION

## Purpose

Distinguish whether the v0.3/v1.3 binding-fix candidate is actually applied and whether the runtime obeys mandatory receipt-first package binding behavior.

This diagnostic does not re-run architecture/audit gates.

## Preconditions

Before running, verify in Builder that the candidate Instructions visibly identify:

### Architect

```text
Software Systems Architect Builder Kernel v0.3 Portable Candidate
Package ID: software-systems-architect-portable-v0.3-candidate
Binding version: v0.3-candidate
SES baseline: e25cdf6b9a4f7d7ef4badc1ac3014b6e10d218e4
Runtime fingerprint: NOT_CAPTURED_IN_RUNTIME / EXTERNAL_PROOF_REQUIRED
```

### Documentation Auditor

```text
Documentation Auditor Builder Kernel v1.3 Portable Candidate
Portable binding:
ID=documentation-auditor-portable-v1.3-candidate
VERSION=v1.3-candidate
SES_BASELINE=e25cdf6b9a4f7d7ef4badc1ac3014b6e10d218e4
FINGERPRINT=NOT_CAPTURED_IN_RUNTIME
STATUS=EXTERNAL_PROOF_REQUIRED
```

If Builder does not show the matching candidate identity, do not execute runtime diagnosis. Apply/save the intended Instructions first.

## Architect diagnostic

Fresh chat.

Prompt:

> Projeto: FECH.AI. Fonte canônica: wagnerjfjunior/fecha.ai. Não faça análise arquitetural ainda. Responda SOMENTE com o Context Readiness Receipt para esta tarefa ordinária read-only. Inclua explicitamente EXECUTION_MODE, CERTIFIED_SPECIALIST_PACKAGE_ID, CERTIFIED_SPECIALIST_PACKAGE_BINDING_VERSION, CERTIFIED_SPECIALIST_PACKAGE_SES_BASELINE, CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT, CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT_STATUS e SES_REFS. Não invente nenhum valor.

Expected exact binding:

```text
EXECUTION_MODE = CERTIFIED_PORTABLE_EXECUTION
CERTIFIED_SPECIALIST_PACKAGE_ID = software-systems-architect-portable-v0.3-candidate
CERTIFIED_SPECIALIST_PACKAGE_BINDING_VERSION = v0.3-candidate
CERTIFIED_SPECIALIST_PACKAGE_SES_BASELINE = e25cdf6b9a4f7d7ef4badc1ac3014b6e10d218e4
CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT = NOT_CAPTURED_IN_RUNTIME
CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT_STATUS = EXTERNAL_PROOF_REQUIRED
SES_REFS = NOT_REQUIRED_FOR_THIS_TASK
```

## Documentation Auditor diagnostic

Fresh chat.

Prompt:

> Projeto: FECH.AI. Fonte canônica: wagnerjfjunior/fecha.ai. Não faça auditoria ainda. Responda SOMENTE com o Context Readiness Receipt para esta tarefa ordinária read-only. Inclua explicitamente EXECUTION_MODE, CERTIFIED_SPECIALIST_PACKAGE_ID, CERTIFIED_SPECIALIST_PACKAGE_BINDING_VERSION, CERTIFIED_SPECIALIST_PACKAGE_SES_BASELINE, CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT, CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT_STATUS e SES_REFS. Não invente nenhum valor.

Expected exact binding:

```text
EXECUTION_MODE = CERTIFIED_PORTABLE_EXECUTION
CERTIFIED_SPECIALIST_PACKAGE_ID = documentation-auditor-portable-v1.3-candidate
CERTIFIED_SPECIALIST_PACKAGE_BINDING_VERSION = v1.3-candidate
CERTIFIED_SPECIALIST_PACKAGE_SES_BASELINE = e25cdf6b9a4f7d7ef4badc1ac3014b6e10d218e4
CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT = NOT_CAPTURED_IN_RUNTIME
CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT_STATUS = EXTERNAL_PROOF_REQUIRED
SES_REFS = NOT_REQUIRED_FOR_THIS_TASK
```

## Diagnosis

```text
BUILDER SHOWS v0.3/v1.3
+ RECEIPT EXACT
-> BINDING_FIX_BEHAVIOR = PASS

BUILDER SHOWS v0.3/v1.3
+ RECEIPT MISSING/WRONG
-> RUNTIME_INSTRUCTION_ADHERENCE_DEFECT

BUILDER DOES NOT SHOW v0.3/v1.3
-> CANDIDATE_NOT_APPLIED / NO RUNTIME VERDICT
```

Do not create another candidate version until this distinction is established.
