# SES — Certified Specialist Attachment Transport Equivalence v0.1

**Status:** RUNTIME_TRANSPORT_TEST_SPEC / MANUAL_EXECUTION_REQUIRED

## Purpose

Determine whether an attached document remains visible and materially equivalent when used through project-level @ mention transport versus direct specialist runtime versus direct SES runtime.

This is a transport/ingestion test, not specialist recertification.

```text
ATTACHMENT AVAILABLE TO HOST CHAT
!=
ATTACHMENT AVAILABLE TO @ SPECIALIST
!=
ATTACHMENT AVAILABLE TO DIRECT CUSTOM GPT
```

## Test object

Use the exact same uploaded file in all arms.

Do not edit, rename, resave or regenerate the file between runs.

Record:
- exact filename;
- file type;
- approximate size if UI exposes it;
- upload timestamp/session;
- screenshots of attachment chips/UI.

Before execution, SES should inspect the file once and define three content anchors from different parts of the document:
- ANCHOR_A: near beginning;
- ANCHOR_B: middle;
- ANCHOR_C: near end.

The anchors must be based on actual document content, not model memory.

## Arm A — FECH.AI Project + @ specialist

Create a fresh chat inside FECH.AI Project.

Attach the file first.

Then explicitly mention:

`@Public-SES — Software Systems Architect`

Prompt:

> Este é um teste de transporte de documento anexo via @. Não use GitHub, não use SES central e não faça análise arquitetural. Use somente o documento anexo desta mensagem. Informe: (1) ATTACHMENT_VISIBLE; (2) nome do arquivo que você consegue acessar, se exposto; (3) se consegue ler conteúdo material do documento; (4) o conteúdo solicitado para ANCHOR_A, ANCHOR_B e ANCHOR_C; (5) qualquer limitação, truncamento, erro ou ausência de acesso. Não invente conteúdo ausente.

Expected classification:

```text
MENTION_ATTACHMENT_VISIBILITY
MENTION_ATTACHMENT_CONTENT_ACCESS
MENTION_ATTACHMENT_BEGINNING_COVERAGE
MENTION_ATTACHMENT_MIDDLE_COVERAGE
MENTION_ATTACHMENT_END_COVERAGE
```

## Arm B — direct Custom GPT

Open the same Software Systems Architect Custom GPT directly, not through a Project @ mention.

Start a fresh chat.

Attach the exact same file.

Send the same prompt, replacing only the first sentence with:

> Este é um teste de leitura direta do mesmo documento no Custom GPT. Não use GitHub, não use SES central e não faça análise arquitetural.

Use the same ANCHOR_A/B/C requests.

Expected classification:

```text
DIRECT_SPECIALIST_ATTACHMENT_VISIBILITY
DIRECT_SPECIALIST_ATTACHMENT_CONTENT_ACCESS
DIRECT_SPECIALIST_BEGINNING_COVERAGE
DIRECT_SPECIALIST_MIDDLE_COVERAGE
DIRECT_SPECIALIST_END_COVERAGE
```

## Arm C — direct SES runtime

In the SES Project, start a fresh chat.

Attach the exact same file.

Do not use @.

Prompt:

> Este é o controle de leitura direta do mesmo documento no SES. Use somente o documento anexo. Informe: (1) ATTACHMENT_VISIBLE; (2) nome do arquivo que você consegue acessar, se exposto; (3) se consegue ler conteúdo material do documento; (4) o conteúdo solicitado para ANCHOR_A, ANCHOR_B e ANCHOR_C; (5) qualquer limitação, truncamento, erro ou ausência de acesso. Não invente conteúdo ausente.

Expected classification:

```text
SES_ATTACHMENT_VISIBILITY
SES_ATTACHMENT_CONTENT_ACCESS
SES_BEGINNING_COVERAGE
SES_MIDDLE_COVERAGE
SES_END_COVERAGE
```

## Adjudication matrix

```text
A PASS + B PASS + C PASS
-> attachment transport equivalence supported for observed file/runtime

A FAIL + B PASS
-> @ attachment transport defect/limitation

A FAIL + B FAIL + C PASS
-> specialist runtime attachment handling defect/limitation

A PASS + B PASS + C FAIL
-> SES-host-specific difference; not @ transport failure

ALL FAIL
-> attachment/document ingestion problem or unsupported file case

PARTIAL BEGIN/MIDDLE/END COVERAGE
-> coverage limitation; no integral-read claim
```

## Evidence rules

Do not accept vague statements such as "I can read the file" as integral proof.

For each arm preserve:
- full prompt;
- full response;
- screenshots showing file attachment and runtime target;
- exact anchor outputs;
- explicit limitations/errors;
- any visible file-reading/tool UI state.

```text
FILE CHIP VISIBLE
!=
CONTENT READ
!=
INTEGRAL COVERAGE
```

## Current target

First file should be a real project-relevant document large/structured enough to exercise attachment transport, but small enough that all three arms can reasonably attempt complete material reading.

SES should define the anchor queries only after the exact document is supplied.
