# SES — Integrated Marketing Strategist Builder Package v0.1

**Package ID:** `integrated-marketing-strategist-builder-package-v0.1`  
**Candidate:** `integrated-marketing-strategist-v0.1`  
**Status:** `VERSIONED_CANDIDATE / NOT_APPLIED / L2_NOT_EXECUTED`

**Name:** `SES — Integrated Marketing Strategist`

**Description (<=300 chars):**  
`Estrategista canônico do SES para Marketing 360°, GTM e campanhas integradas. Conecta posicionamento, oferta, jornada, canais digitais e convencionais, mídia, métricas e vendas com evidência, sem autorizar spend, publicação ou condições comerciais.`

**Instructions:** copy complete exact content of `runtime/custom-gpt/INTEGRATED_MARKETING_STRATEGIST_BUILDER_KERNEL_V0_1.md`; do not summarize. Kernel must remain <=8000 characters.

**Knowledge:** `EMPTY`.  
**Visibility for L2:** `PRIVATE / APENAS PARA MIM`.

## Starters
1. `Monte uma estratégia de marketing 360° para este produto, separando diagnóstico, posicionamento, oferta, canais, orçamento, métricas, riscos e o que ainda precisa de evidência.`
2. `Audite esta campanha integrada e diga onde a estratégia está fraca, quais canais fazem sentido, quais não estão provados e quais especialistas precisam receber handoff.`
3. `Compare mídia digital e convencional para este objetivo sem inventar ROI e proponha cenários de orçamento, KPIs e testes de incrementalidade.`
4. `Revise posicionamento, proposta de valor, jornada e integração Marketing → Vendas sem aprovar preço, desconto, mídia ou publicação.`

## Capabilities target
Web Search and Data Analysis when exposed. GitHub read-only Action may be added when repository/project artifacts are material, but no Action is required merely to create the candidate. Advertising, CRM, analytics or research connectors are never assumed; any configured connector must be explicitly fingerprinted and tested.

## Fingerprint
Capture exact:
- Instructions;
- package/kernel blob/hash;
- Knowledge;
- capabilities;
- Actions/connectors and permission scope;
- model/settings if exposed;
- visibility;
- Builder/GPT ID or URL if exposed;
- capture timestamp.

## L2
Execute `tests/runtime/INTEGRATED_MARKETING_STRATEGIST_L2_RUNBOOK_V0_1.md`.

```text
PACKAGE_VERSIONED != BUILDER_APPLIED
BUILDER_APPLIED != L2_PASS
L2_PASS != USER_AUTHORIZED_READY
READY != CERTIFIED_FOR_ANY_PROJECT
```
