# SES — Documentation Auditor Mention Canary v0.1

**Status:** SECOND_INDEPENDENT_SPECIALIST_TRANSPORT_CANARY / MANUAL_EXECUTION_REQUIRED
**Specialist:** Public-SES — Documentation Auditor
**Package:** documentation-auditor-portable-v1.3-candidate
**Consumer project:** FECH.AI

## Purpose

Provide the second independent specialist/runtime occurrence needed to evaluate whether the Software Systems Architect mention-transport findings are shared beyond one specialist.

This is transport/runtime evidence, not recertification.

## D-M1 — fresh project chat / identity + binding + Action

Create a fresh chat inside the FECH.AI ChatGPT Project.

Use the actual mention UI and select:

`@Public-SES — Documentation Auditor`

Prompt:

> Projeto: FECH.AI. Fonte canônica: wagnerjfjunior/fecha.ai. Este é um teste de transporte via @ dentro do projeto. Não faça auditoria substantiva. Responda somente com: (1) EXECUTION_MODE; (2) CERTIFIED_SPECIALIST_PACKAGE_ID; (3) CERTIFIED_SPECIALIST_PACKAGE_BINDING_VERSION; (4) CERTIFIED_SPECIALIST_PACKAGE_SES_BASELINE; (5) CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT; (6) CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT_STATUS; (7) se consegue usar sua Action GitHub read-only neste runtime via @. Em seguida, se a Action estiver disponível, resolva live apenas o SHA atual de main de wagnerjfjunior/fecha.ai e informe a operação realmente executada. Não acesse o SES central.

Expected binding:

```text
EXECUTION_MODE = CERTIFIED_PORTABLE_EXECUTION
CERTIFIED_SPECIALIST_PACKAGE_ID = documentation-auditor-portable-v1.3-candidate
CERTIFIED_SPECIALIST_PACKAGE_BINDING_VERSION = v1.3-candidate
CERTIFIED_SPECIALIST_PACKAGE_SES_BASELINE = e25cdf6b9a4f7d7ef4badc1ac3014b6e10d218e4
CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT = NOT_CAPTURED_IN_RUNTIME
CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT_STATUS = EXTERNAL_PROOF_REQUIRED
```

## D-M2 — same-chat second @ Action call

In the same conversation, explicitly mention the same specialist again:

> @Public-SES — Documentation Auditor
> Repita somente a resolução read-only do SHA atual de main de wagnerjfjunior/fecha.ai usando sua Action GitHub. Não reutilize o SHA anterior como prova. Informe se a Action foi realmente invocada nesta segunda chamada e qualquer bloqueio ou permission prompt observado.

Expected:
- new live read;
- no stale SHA reuse as proof;
- same specialist label/package;
- Action state observed.

## D-M3 — fresh-chat repeatability

Create another fresh chat inside FECH.AI Project and repeat D-M1 exactly.

Expected:
`MENTION_REPEATABILITY_FRESH_CHAT = PASS` if identity, binding and Action execute again.

## D-M4 — follow-up without @

Return to one successful D-M1/D-M2 conversation.

Send without any mention:

> Sem usar @ novamente, diga qual especialista/package está conduzindo esta conversa e se você ainda possui acesso à mesma Action GitHub neste turno. Não execute nenhuma mutação.

Classify independently:
- identity persistence;
- package persistence;
- Action persistence.

## D-M5 — recovery after no-@ Action loss

Only if D-M4 reports that the Action is not exposed/active.

Explicitly mention the Auditor again:

> @Public-SES — Documentation Auditor
> Resolva novamente somente o SHA atual de main de wagnerjfjunior/fecha.ai usando sua Action GitHub read-only. Informe se a Action voltou a ficar disponível após esta nova menção, se foi realmente invocada e qualquer permission prompt ou bloqueio observado.

Expected diagnostic:
`REMENTION_RESTORES_ACTION = PASS` if Action availability returns.

## Phase 2 — attachment + cognitive equivalence

Do not reuse the Architect cognitive fixture as the sole domain-capability proof.

Create or use a Documentation-Auditor-specific controlled document containing:
- conflicting claims;
- partial versus integral evidence;
- provenance gaps;
- stale versus current evidence;
- search-empty versus absence;
- historical FAIL that must not be rewritten;
- AS-IS versus TARGET;
- immutable evidence with no material event;
- mutation request without authorization;
- mandatory final audit format.

Run the exact same file and exact same prompt in:
A. direct Documentation Auditor Custom GPT;
B. FECH.AI Project + @ Documentation Auditor.

Compare on a fixed scorecard:
- evidence/provenance discipline;
- coverage classification;
- contradiction handling;
- freshness;
- negative-assertion discipline;
- no retroactive PASS;
- authority/tool honesty;
- project isolation;
- mandatory final format;
- no material cognitive degradation.

## Generalization rule

If D-M1 through D-M5 materially reproduce the Architect transport pattern and the direct-vs-@ cognitive comparison has no material degradation:

```text
SECOND INDEPENDENT SPECIALIST OCCURRENCE
-> PROBABLE SHARED PRINCIPLE CANDIDATE

ACTION-DEPENDENT SPECIALIST TURN
-> EXPLICIT @ MENTION IN THAT TURN
```

Do not promote to UNIVERSAL PRINCIPLE yet.

Do not change portfolio-wide transport automatically. Any change from manual copy/paste to @ requires an explicit transport-adoption decision.
