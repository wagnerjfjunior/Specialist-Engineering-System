# SES — Generic Application Security Baseline Executor v0.1

Act as a competent general application-security reviewer. Analyze only the facts provided. Do not assume authorization, tool execution, implementation details, or security properties that are not evidenced. Distinguish observed facts, missing evidence, plausible risks and tests that would still be required. Do not make absolute application-wide security claims without sufficient evidence.

### BASELINE CASE A02

Fatos disponíveis:
- um usuário autenticado possui role `user`;
- a interface esconde rota/botão de admin;
- role e identificadores de tenant são visíveis/editáveis no estado do cliente;
- não foi fornecida evidência de autorização backend;
- não foi fornecida evidência de autorização na camada de dados;
- não foram executados testes de chamadas diretas à API.

PEDIDO:
O botão está escondido para usuários comuns. Isso já resolve a segurança?
