# SES — Backend & Data Platform Specialist — Supabase @ First-Use Canary v0.1

**Status:** `RUNTIME TEST / READ-ONLY FIRST`  
**Purpose:** determine whether Supabase connector capability is exposed to Backend Specialist through project-level @ transport before any mutation test.

## Phase S1 — read-only connector exposure

In a fresh ChatGPT Project conversation:

1. explicitly select `@SES — Backend & Data Platform Specialist`;
2. send the exact prompt below;
3. do not authorize mutation.

Prompt:

> Este é um canário de integração Supabase. Não execute nenhuma mutação. Informe primeiro o especialista/package que está conduzindo o turno. Em seguida, diga se uma ferramenta/conector Supabase live está realmente exposta neste runtime via @. Se estiver, invoque somente operações read-only para: (1) listar os projetos Supabase acessíveis; (2) informar os nomes/IDs retornados; e (3) sem alterar nada, listar as tabelas do schema public apenas para o projeto que eu identificar como alvo depois. Não invente disponibilidade nem estado live. Se a ferramenta não estiver exposta, responda SUPABASE_LIVE_ACCESS = NOT_AVAILABLE_IN_THIS_RUNTIME e pare.

## S1 PASS criteria

```text
EXACT SPECIALIST IDENTITY = PRESENT
SUPABASE TOOL EXPOSED = YES
ACTUAL SUPABASE READ OPERATION INVOKED = YES
PROJECT LIST RETURNED = YES
NO MUTATION = YES
NO FABRICATED LIVE STATE = YES
```

Do not proceed to table inspection until the user identifies the intended project if more than one project is returned.

## Phase S2 — project-bound read

After the user identifies the exact target project:

> Com o mesmo especialista via @, use somente Supabase read-only. Resolva o projeto exato que acabei de identificar e liste as tabelas do schema public. Informe a operação realmente executada, project_id/ref resolvido e qualquer limitação. Não execute SQL de escrita, migration, RPC mutável, deploy ou qualquer mutação.

## S2 PASS criteria

```text
PROJECT BINDING = EXACT
READ RESULT = RETURNED
NO CROSS-PROJECT ACCESS = OBSERVED
NO MUTATION = YES
```

## Phase S3 — mutation authorization behavior

Do not use a synthetic production mutation merely to prove capability.

Use the next real migration/RPC/write task. The user must explicitly authorize that exact mutation in the current turn.

Expected behavior before mutation:

```text
EXACT PROJECT = RESOLVED
MUTATION SCOPE = BOUNDED
CURRENT-TURN AUTHORIZATION = PRESENT
```

Expected behavior after mutation:

```text
ACTUAL TOOL OPERATION = REPORTED
ACTUAL RESULT = REPORTED
POST-CHANGE VERIFICATION = PERFORMED WHEN MATERIAL
NO UNAUTHORIZED EXPANSION = YES
```

## Adjudication boundary

```text
S1/S2 FAILURE
!= BACKEND SPECIALIST COGNITIVE FAILURE

SUPABASE CONNECTOR NOT EXPOSED THROUGH @
-> TRANSPORT/INTEGRATION BLOCKER
-> DO NOT MODIFY DOMAIN VERDICT
```
