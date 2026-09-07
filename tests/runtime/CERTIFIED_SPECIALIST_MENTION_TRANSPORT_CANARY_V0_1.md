# SES — Certified Specialist Mention Transport Canary v0.1

**Status:** RUNTIME_TRANSPORT_TEST_SPEC / MANUAL_EXECUTION_REQUIRED
**Primary canary:** Software Systems Architect portable v0.3 candidate
**Consumer project:** FECH.AI

## 1. Purpose

Determine whether ChatGPT project-level mention invocation (`@`) preserves enough of the specialist runtime to support:

1. specialist identity/package binding;
2. project-scoped context behavior;
3. specialist Action/tool availability;
4. repeatable invocation in the same and a fresh conversation.

This is a transport/runtime test, not specialist recertification.

```text
PACKAGE PORTABILITY
!=
MENTION TRANSPORT
!=
ACTION AVAILABILITY THROUGH MENTION
```

## 2. Preconditions

Use the FECH.AI ChatGPT Project.

Target specialist:

```text
Public-SES — Software Systems Architect
PACKAGE_ID = software-systems-architect-portable-v0.3-candidate
BINDING_VERSION = v0.3-candidate
```

Do not modify the current certified parent GPT.

Capture screenshots whenever ChatGPT shows:
- permission prompts;
- inability to invoke the GPT;
- blocked tools/Actions;
- transport errors;
- model/runtime substitution warnings;
- any UI state materially different from direct-GPT execution.

## 3. Canary M1 — first mention in fresh project chat

Create a new conversation **inside the FECH.AI Project**.

Invoke the candidate using ChatGPT mention UI (`@`) and send:

> @Public-SES — Software Systems Architect  
> Projeto: FECH.AI. Fonte canônica: wagnerjfjunior/fecha.ai. Este é um teste de transporte via @ dentro do projeto. Não faça análise arquitetural. Responda somente com: (1) EXECUTION_MODE; (2) CERTIFIED_SPECIALIST_PACKAGE_ID; (3) CERTIFIED_SPECIALIST_PACKAGE_BINDING_VERSION; (4) CERTIFIED_SPECIALIST_PACKAGE_SES_BASELINE; (5) CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT; (6) CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT_STATUS; (7) se consegue usar sua Action GitHub read-only neste runtime via @. Em seguida, se a Action estiver disponível, resolva live apenas o SHA atual de main de wagnerjfjunior/fecha.ai e informe a operação realmente executada. Não acesse o SES central.

Expected identity/binding:

```text
EXECUTION_MODE = CERTIFIED_PORTABLE_EXECUTION
CERTIFIED_SPECIALIST_PACKAGE_ID = software-systems-architect-portable-v0.3-candidate
CERTIFIED_SPECIALIST_PACKAGE_BINDING_VERSION = v0.3-candidate
CERTIFIED_SPECIALIST_PACKAGE_SES_BASELINE = e25cdf6b9a4f7d7ef4badc1ac3014b6e10d218e4
CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT = NOT_CAPTURED_IN_RUNTIME
CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT_STATUS = EXTERNAL_PROOF_REQUIRED
```

Action result classification:

```text
ACTION_AVAILABLE_AND_INVOKED
ACTION_AVAILABLE_BUT_PERMISSION_REQUIRED
ACTION_NOT_EXPOSED_THROUGH_MENTION
ACTION_INVOCATION_BLOCKED
ACTION_STATE_NOT_DETERMINED
```

Never convert missing Action UI into proof that the Action does not exist in the standalone GPT.

## 4. Canary M2 — second mention in the same chat

In the same conversation, invoke the same specialist again through `@`:

> @Public-SES — Software Systems Architect  
> Repita somente a resolução read-only do SHA atual de main de wagnerjfjunior/fecha.ai usando sua Action GitHub. Não reutilize o SHA anterior como prova. Informe se a Action foi realmente invocada nesta segunda chamada e qualquer bloqueio/permission prompt observado.

Purpose:

- detect first-call-only permission behavior;
- detect whether subsequent mention invocation loses Action availability;
- detect stale-result reuse.

Expected:

```text
SECOND_MENTION_SPECIALIST_IDENTITY = PRESERVED
SECOND_MENTION_ACTION_STATE = OBSERVED
NO_STALE_SHA_AS_LIVE_PROOF
```

## 5. Canary M3 — fresh-chat repeatability

Create another **new conversation inside the FECH.AI Project** and repeat M1 exactly.

Purpose:

- prove the result is not dependent on hidden prior chat state;
- distinguish deterministic platform limitation from one-chat anomaly.

## 6. Canary M4 — no-mention follow-up

Only if M1 succeeds, in that same chat send a normal follow-up **without `@`**:

> Sem usar @ novamente, diga qual especialista/package está conduzindo esta conversa e se você ainda possui acesso à mesma Action GitHub neste turno. Não execute nenhuma mutação.

This does not assume persistence. Record actual behavior.

Possible states:

```text
SPECIALIST_CONTEXT_PERSISTS
HOST_CHAT_CONTEXT_RESUMED
IDENTITY_NOT_DETERMINED
ACTION_STATE_CHANGED
```

## 7. Verdict dimensions

Do not collapse into one PASS.

Report independently:

```text
MENTION_IDENTITY_TRANSPORT
MENTION_PACKAGE_BINDING_TRANSPORT
MENTION_PROJECT_CONTEXT
MENTION_ACTION_AVAILABILITY
MENTION_ACTION_EXECUTION
MENTION_REPEATABILITY_SAME_CHAT
MENTION_REPEATABILITY_FRESH_CHAT
POST_MENTION_CONTEXT_PERSISTENCE
```

Each dimension may be:

```text
PASS
FAIL
BLOCKED
NOT_DETERMINED
NOT_EXECUTED
```

## 8. Main adjudication

The transport is operationally viable for SES project use only if, at minimum:

```text
MENTION_IDENTITY_TRANSPORT = PASS
MENTION_PACKAGE_BINDING_TRANSPORT = PASS
MENTION_PROJECT_CONTEXT = PASS
MENTION_ACTION_EXECUTION = PASS
MENTION_REPEATABILITY_FRESH_CHAT = PASS
```

If identity works but Action is unavailable through `@`:

```text
SPECIALIST_MENTION_TRANSPORT = PARTIAL
ACTION_TRANSPORT = FAIL/BLOCKED
PROJECT_WORK_REQUIRING_ACTIONS_THROUGH_MENTION = NOT_VIABLE
```

If the first call works but the second same-chat call blocks:

```text
REPEATABILITY_SAME_CHAT = FAIL
KNOWN OPERATIONAL LIMITATION
```

Do not alter specialist certification because of a platform transport limitation unless the exact specialist runtime/fingerprint itself changed.

```text
TRANSPORT FAILURE
!=
SPECIALIST CERTIFICATION FAILURE
```

## 9. Evidence to return

For each canary:
- exact prompt;
- full response;
- screenshot of any permission/error UI;
- whether `@` resolved the intended GPT;
- whether Action invocation was visible;
- exact operation name only if exposed;
- exact live SHA returned;
- any platform error text.

