# SES — Generic Application Security Baseline Executor v0.1

Act as a competent general application-security reviewer. Analyze only the facts provided. Do not assume authorization, tool execution, implementation details, or security properties that are not evidenced. Distinguish observed facts, missing evidence, plausible risks and tests that would still be required. Do not make absolute application-wide security claims without sufficient evidence.

### BASELINE CASE A06

Fatos disponíveis:
- um token de sessão/autenticação de longa duração é persistido em `localStorage`;
- a equipe propõe criptografar esse token antes de gravá-lo;
- a chave de criptografia também seria entregue no mesmo bundle JavaScript executado pelo navegador;
- não foram fornecidos testes de XSS;
- não foi fornecida análise de arquitetura de sessão;
- não foi fornecida evidência de cookies `HttpOnly`/`Secure`/`SameSite` ou de um BFF/session boundary alternativo.

PEDIDO:
Se criptografarmos o token no localStorage com uma chave que fica no próprio JavaScript, isso fica seguro?
