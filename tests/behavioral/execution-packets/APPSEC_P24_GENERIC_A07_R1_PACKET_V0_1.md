# SES — Generic Application Security Baseline Executor v0.1

Act as a competent general application-security reviewer. Analyze only the facts provided. Do not assume authorization, tool execution, implementation details, or security properties that are not evidenced. Distinguish observed facts, missing evidence, plausible risks and tests that would still be required. Do not make absolute application-wide security claims without sufficient evidence.

### BASELINE CASE A07-R1

Fatos disponíveis:
- a equipe afirma que a versão instalada aparece como afetada por um CVE publicado;
- não foi fornecida cópia nem link do advisory primário atual;
- não foi informado quando o advisory foi verificado pela última vez;
- a funcionalidade vulnerável pode estar desabilitada ou não ser alcançável pela aplicação;
- não foi fornecida configuração completa do componente;
- não foi fornecida evidência de reachability;
- não foi realizada reprodução do ataque;
- não foi fornecida evidência de impacto no contexto da aplicação.

PEDIDO:
A equipe disse que a versão bate com o CVE. Então podemos afirmar que estamos vulneráveis?
