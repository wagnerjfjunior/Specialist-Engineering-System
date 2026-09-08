# SES — Attachment Transport Equivalence Evidence — 2026-09-07

**Status:** USER_SUPPLIED_RUNTIME_OUTPUT / SAMPLED_COVERAGE_PASS
**SES main at evidence capture:** `f1531753530c2c19dc13d8943013f8be9627db4e`

## Fixture

Expected source fixture:

```text
FILENAME = SES_Arquiteto_Teste_Progressivo_2000_palavras.txt
WORD_COUNT = 2000
SHA256 = 8c9815eff29a8d8a7c0458a9e11cb5a39d92cd3537f92bac2b4ae5703d833670
```

The @ runtime visibly reported:

`SES_Arquiteto_Teste_Progressivo_2000_palavras(1).txt`

The suffix `(1)` is treated as a UI/local filename variation only. Exact attachment hash identity was not exposed by the @ runtime.

## SES direct control

The same source document was uploaded directly in the SES conversation.

SES successfully recovered the controlled anchors from:
- beginning;
- middle;
- end.

```text
SES_DIRECT_BEGINNING = PASS
SES_DIRECT_MIDDLE = PASS
SES_DIRECT_END = PASS
```

## @ transport result

User-supplied runtime output from FECH.AI Project + explicit @ Software Systems Architect:

```text
ATTACHMENT_VISIBLE = SIM

FILENAME =
SES_Arquiteto_Teste_Progressivo_2000_palavras(1).txt

ANCHOR_A =
Supabase Auth; PostgreSQL; RLS; RPCs; Edge Functions.
Users: administradores; gestores; corretores.

ANCHOR_B =
uma RPC crítica; uma policy RLS; um componente React;
uma GitHub Action; um documento SFJM; uma configuração de Vercel.

Rule =
uma PR = um risco principal = um rollback simples

ANCHOR_C =
BLOCKING; REQUIRED; RESIDUAL_RISK; PLANNED_FUTURE; NOT_RELEVANT

Final ten words =
contratos invariantes evidências dependências isolamento autorização ownership tenant rollback observabilidade

COVERAGE =
BEGINNING PASS / MIDDLE PASS / END PASS
```

The runtime also reported a sandbox `FileNotFoundError` during one direct-path attempt, but stated that attachment content remained accessible through another attachment-reading path.

## Adjudication

```text
MENTION_ATTACHMENT_VISIBILITY = PASS
MENTION_ATTACHMENT_CONTENT_ACCESS = PASS
MENTION_ATTACHMENT_BEGINNING_COVERAGE = PASS
MENTION_ATTACHMENT_MIDDLE_COVERAGE = PASS
MENTION_ATTACHMENT_END_COVERAGE = PASS

SES_ATTACHMENT_BEGINNING_COVERAGE = PASS
SES_ATTACHMENT_MIDDLE_COVERAGE = PASS
SES_ATTACHMENT_END_COVERAGE = PASS

ATTACHMENT_TRANSPORT_EQUIVALENCE =
PASS_FOR_SAMPLED_BEGINNING_MIDDLE_END_COVERAGE
```

## Important non-claim

Three correct anchors distributed across the document do not prove byte-complete or semantically integral reading of the entire attachment.

Therefore:

```text
INTEGRAL_READ = NOT_PROVEN
FULL_ATTACHMENT_HASH_MATCH_IN_@_RUNTIME = NOT_PROVEN
```

The runtime phrase equivalent to "conteúdo integral do anexo disponível" is stronger than the evidence established by this test and must not be used as an integral-coverage PASS.

## Failure handling observation

The observed sandbox `FileNotFoundError` did not cause fabricated content. The runtime still produced the correct three anchors through the available attachment content path.

```text
ONE FILE ACCESS PATH FAILED
!=
ATTACHMENT CONTENT UNAVAILABLE
```

## Current conclusion

For this exact fixture and observed ChatGPT runtime:

```text
DIRECT SES SAMPLED COVERAGE = PASS
@ SPECIALIST SAMPLED COVERAGE = PASS
BEGINNING/MIDDLE/END EQUIVALENCE = PASS

ATTACHMENT TRANSPORT DEFECT VIA @ = NOT OBSERVED
```

Next separate study: compare full 13-block reasoning quality via @ specialist versus direct SES runtime.
