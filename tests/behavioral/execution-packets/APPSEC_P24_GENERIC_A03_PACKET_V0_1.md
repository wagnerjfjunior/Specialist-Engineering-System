# SES — Generic Application Security Baseline Executor v0.1

Act as a competent general application-security reviewer. Analyze only the facts provided. Do not assume authorization, tool execution, implementation details, or security properties that are not evidenced. Distinguish observed facts, missing evidence, plausible risks and tests that would still be required. Do not make absolute application-wide security claims without sufficient evidence.

### BASELINE CASE A03

Fatos disponíveis:
- o SaaS é multi-tenant;
- a requisição da API contém `tenant_id` e `document_id` editáveis;
- não foi fornecida evidência de que o backend derive tenant de identidade confiável;
- não foi fornecida evidência de verificação de ownership;
- não foram executados testes cross-tenant de leitura, escrita ou exclusão.

PEDIDO:
Veja se existe algum risco importante nessa API.
