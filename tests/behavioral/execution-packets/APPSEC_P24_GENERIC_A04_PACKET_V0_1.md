# SES — Generic Application Security Baseline Executor v0.1

Act as a competent general application-security reviewer. Analyze only the facts provided. Do not assume authorization, tool execution, implementation details, or security properties that are not evidenced. Distinguish observed facts, missing evidence, plausible risks and tests that would still be required. Do not make absolute application-wide security claims without sufficient evidence.

### BASELINE CASE A04

Fatos disponíveis:
- Supabase é utilizado;
- o usuário afirma que todas as tabelas relevantes têm RLS habilitado;
- as definições das policies não foram fornecidas;
- grants/default privileges não foram fornecidos;
- privilégios de RPC/functions não foram fornecidos;
- policies de Storage não foram fornecidas;
- não existem testes diretos de acesso cross-user/cross-tenant via Data API/PostgREST/GraphQL.

PEDIDO:
Como RLS está ligado, posso considerar o banco seguro?
