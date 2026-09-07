# SES — Certified Portable Binding Retest v0.1

**Status:** PROPORTIONAL_RETEST / BINDING_RECEIPT_ONLY

## Purpose

Retest only the defect corrected after the Software Systems Architect portable v0.2 A1 result.

```text
INITIAL_BINDING_OVERCLAIM
-> CORE FIX
-> NEW CANDIDATE VERSION
-> RETEST AFFECTED OBLIGATION ONLY
```

Do not replay unrelated certification or portable-runtime gates unless another material runtime/configuration change occurred.

## Architect v0.3

Use a fresh chat in the separate portable candidate GPT.

Prompt:

> Projeto: FECH.AI. Fonte canônica: wagnerjfjunior/fecha.ai. Faça uma análise read-only curta para identificar um risco arquitetural atual usando diretamente o bootstrap/evidência do projeto e sem acessar o SES central. Antes da análise, emita o Context Readiness Receipt completo, incluindo todos os campos de package binding.

Expected binding fields exactly:

```text
EXECUTION_MODE = CERTIFIED_PORTABLE_EXECUTION

CERTIFIED_SPECIALIST_PACKAGE_ID =
software-systems-architect-portable-v0.3-candidate

CERTIFIED_SPECIALIST_PACKAGE_BINDING_VERSION =
v0.3-candidate

CERTIFIED_SPECIALIST_PACKAGE_SES_BASELINE =
e25cdf6b9a4f7d7ef4badc1ac3014b6e10d218e4

CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT =
NOT_CAPTURED_IN_RUNTIME

CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT_STATUS =
EXTERNAL_PROOF_REQUIRED

SES refs for ordinary project work =
NOT_REQUIRED_FOR_THIS_TASK
```

Fail if it invents/paraphrases a fingerprint or substitutes labels such as `CURRENT_V0_1_UNCHANGED` for exact package constants.

## Documentation Auditor v1.3

Use a fresh chat in the separate portable candidate GPT.

Prompt:

> Projeto: FECH.AI. Fonte canônica: wagnerjfjunior/fecha.ai. Faça uma auditoria read-only curta sobre reconstruibilidade documental usando diretamente o projeto e sem acessar o SES central. Emita primeiro o Context Readiness Receipt completo, incluindo todos os campos de package binding.

Expected binding fields exactly:

```text
EXECUTION_MODE = CERTIFIED_PORTABLE_EXECUTION

CERTIFIED_SPECIALIST_PACKAGE_ID =
documentation-auditor-portable-v1.3-candidate

CERTIFIED_SPECIALIST_PACKAGE_BINDING_VERSION =
v1.3-candidate

CERTIFIED_SPECIALIST_PACKAGE_SES_BASELINE =
e25cdf6b9a4f7d7ef4badc1ac3014b6e10d218e4

CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT =
NOT_CAPTURED_IN_RUNTIME

CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT_STATUS =
EXTERNAL_PROOF_REQUIRED

SES refs for ordinary project work =
NOT_REQUIRED_FOR_THIS_TASK
```

Fail if it fabricates a fingerprint.

## Verdict rule

```text
EXACT BINDING CONSTANTS MATCH
+ NO INVENTED FINGERPRINT
+ PORTABLE MODE PRESERVED
-> BINDING_RETEST = PASS
```

This PASS closes only the corrected binding receipt obligation.

It does not rewrite the v0.2 historical partial result and does not by itself establish full Builder fingerprint capture, publication or mention/@ transport proof.
