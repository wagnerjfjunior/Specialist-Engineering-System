# SES — Attachment Transport Fixture — Arquiteto 2000 palavras v0.1

**Status:** CONTROLLED_TEST_FIXTURE
**Source:** user-supplied attachment

## Exact object

```text
FILENAME = SES_Arquiteto_Teste_Progressivo_2000_palavras.txt
WORD_COUNT = 2000
SHA256 = 8c9815eff29a8d8a7c0458a9e11cb5a39d92cd3537f92bac2b4ae5703d833670
```

Do not rename, edit, resave or regenerate the file between arms.

## Phase 1 — attachment reading anchors

The runtime must use only the attached file. No GitHub, SES central, web or memory substitution.

### ANCHOR_A — beginning region

Question:

```text
No BLOCO 2, quais são as cinco tecnologias/capacidades explicitamente listadas para identidade/backend e quais são os três tipos de usuário citados?
```

Expected:

```text
Supabase Auth
PostgreSQL
RLS
RPCs
Edge Functions

administradores
gestores
corretores
```

### ANCHOR_B — middle region

Question:

```text
No BLOCO 6, quais são os seis tipos de mudança contidos na PR e qual é a regra textual usada para avaliar seu escopo?
```

Expected six items:

```text
uma RPC crítica
uma policy RLS
um componente React
uma GitHub Action
um documento SFJM
uma configuração de Vercel
```

Expected rule:

```text
uma PR = um risco principal = um rollback simples
```

### ANCHOR_C — end region

Question:

```text
No FORMATO FINAL OBRIGATÓRIO, quais são os cinco campos imediatamente posteriores a SECURITY_BOUNDARIES? E quais são as dez palavras finais do documento após a frase de encerramento do BLOCO 13?
```

Expected five fields:

```text
BLOCKING
REQUIRED
RESIDUAL_RISK
PLANNED_FUTURE
NOT_RELEVANT
```

Expected final ten tokens:

```text
contratos invariantes evidências dependências isolamento autorização ownership tenant rollback observabilidade
```

## Phase 1 prompt — use identically

```text
Este é um teste controlado de transporte/leitura de anexo. Use SOMENTE o arquivo anexo. Não use GitHub, SES central, web, memória de outro chat nem conhecimento externo para preencher lacunas. Não execute o teste arquitetural completo ainda.

Responda somente:
1. ATTACHMENT_VISIBLE = SIM/NÃO
2. FILENAME = nome visível ou NOT_EXPOSED
3. ANCHOR_A = resposta
4. ANCHOR_B = resposta
5. ANCHOR_C = resposta
6. COVERAGE = BEGINNING / MIDDLE / END, cada um como PASS/FAIL/NOT_DETERMINED
7. LIMITATIONS = qualquer truncamento, erro, ausência de acesso ou NOT_OBSERVED

Não invente conteúdo ausente.
```

## Arms

### Arm A
FECH.AI Project + exact attachment + explicit `@Public-SES — Software Systems Architect`.

### Arm C
SES Project fresh chat + exact attachment + no `@`.

### Arm B
Direct Software Systems Architect Custom GPT + exact attachment, only if A and C materially diverge or if an additional control is desired.

## Phase 1 verdict

```text
A anchors all PASS + C anchors all PASS
-> observed attachment transport equivalence supported

A FAIL + C PASS
-> run B to isolate @ transport vs specialist runtime

A PASS + C FAIL
-> SES-host/runtime difference; not @ failure

A/C partial
-> do not claim integral attachment visibility
```

## Phase 2 — full capability comparison

Only after Phase 1 closes.

Use the exact same file and ask the runtime to execute the entire test contained in the document, preserving READ_ONLY and the mandatory final format.

Compare:
- block completeness;
- fact/inference/hypothesis separation;
- architecture depth;
- evidence discipline;
- overclaim resistance;
- authority boundaries;
- final mandatory fields;
- whether beginning/middle/end instructions were all honored.

Phase 2 is a reasoning-equivalence study, not merely a file-visibility test.
