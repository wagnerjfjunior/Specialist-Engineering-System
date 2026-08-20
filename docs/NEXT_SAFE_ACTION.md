# SES — Next Safe Action

> Registro autoritativo da próxima ação segura do SES quando este arquivo estiver em `main`.

**Next action ID:** `runtime-enforcement-gateway-action-tool-integration`  
**Primary target:** `SES Runtime Enforcement Gateway`  
**Current phase:** `RUNTIME_ENFORCEMENT_GATEWAY_OPERATIONALIZATION / ACTION_INTEGRATION`

## Current certified portfolio

```text
UX/UI APP = CERTIFIED_FOR_ANY_PROJECT YES
BACKEND & DATA PLATFORM = YES
APPLICATION SECURITY ASSURANCE = YES
SOFTWARE SYSTEMS ARCHITECT = YES
DOCUMENTATION AUDITOR = YES / v1.1
```

Historical failures remain preserved; `RETROACTIVE_PASS = NO`.

## Gateway current state

```text
CONTRACT = IMPLEMENTED / MERGED
CONTROLLER = IMPLEMENTED / G01-G12 PASS 12/12
G12_INITIAL = FAIL / PRESERVED
FECHAI_REFERENCE_ROUTING = PASS 7/7
FECHAI_PROJECT_ROUTING_RECONCILIATION = IMPLEMENTED
CANONICAL_GITHUB_LOADER = IMPLEMENTED / L01-L08 PASS 8/8
HTTP_SERVICE_CODE = MERGED / H01-H08 PASS 8/8
GIT_BOUND_MAIN_DEPLOYMENT_STATUS = VERCEL SUCCESS
CANONICAL_HOST = https://ses-runtime-enforcement-gateway.vercel.app
EXTERNAL_HEALTH = PASS
EXTERNAL_ROUTE_ADOPTED_ROLE = PASS
EXTERNAL_ROUTE_LEGACY_FAIL_CLOSED = PASS
ROUTE_MUTATION_AUTHORIZED = false
OPENAPI_BOUND_SCHEMA = runtime/specialist_gateway/RUNTIME_ENFORCEMENT_GATEWAY.openapi.yaml
ACTION_TOOL_CONFIGURATION = NOT PROVEN
ACTION_TOOL_INVOCATION = NOT PROVEN
```

The route proof is pinned to SES ref `ea0e7a189be72261992249bcc357bc51dad5a4f7`. A later documentation/OpenAPI commit does not retroactively rewrite that receipt. The Vercel deployment-object lookup limitation remains preserved separately.

Evidence:

```text
tests/runtime/evidence/RUNTIME_ENFORCEMENT_GATEWAY_DEPLOYMENT_ATTEMPT_2026-08-20.md
tests/runtime/evidence/RUNTIME_ENFORCEMENT_GATEWAY_EXTERNAL_HEALTH_2026-08-20.md
tests/runtime/evidence/RUNTIME_ENFORCEMENT_GATEWAY_EXTERNAL_ROUTE_2026-08-20.md
```

## Next safe action

Do not redesign or redeploy the Gateway merely because Action/tool integration remains open. Continue only through an authorized Action/tool configuration surface:

```text
1. configure an Action/tool using runtime/specialist_gateway/RUNTIME_ENFORCEMENT_GATEWAY.openapi.yaml;
2. configure the Action credential as the existing SES_GATEWAY_API_KEY without committing or exposing the secret;
3. verify the configured tool exposes routeSpecialistRole and, where supported, getGatewayHealth;
4. invoke routeSpecialistRole externally for an exact adopted FECH.AI role;
5. verify the returned receipt remains ROUTABLE and mutation_authorized = false;
6. invoke or otherwise verify one fail-closed case when the Action surface permits it;
7. record the actual Action/tool operation invoked, target host, returned SES_REF and result;
8. only after observed invocation set ACTION_TOOL_INTEGRATION = PASS.
```

If no authorized Action/tool configuration surface is available, stop at `OPENAPI_BOUND / ACTION_CONFIGURATION_REQUIRED`. Do not substitute manual curl proof for Action invocation proof.

Do not request, store, commit or expose `SES_GATEWAY_API_KEY` or `SES_GITHUB_TOKEN` as evidence.

Controller, loader and HTTP local gates remain valid because this increment changes evidence/documentation/OpenAPI binding, not routing behavior.

Do not add database, dashboard, Supabase dependency, semantic/fuzzy free-text routing, automatic specialist adoption, autonomous Builder creation or automatic project mutation.

```text
OPENAPI_BOUND != ACTION_CONFIGURED
ACTION_CONFIGURED != ACTION_INVOKED
ROUTABLE != EXECUTED
TOOL_CAPABILITY != AUTHORIZATION
CERTIFIED_FOR_ANY_PROJECT != CONSUMER_PROJECT_ADOPTED
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
RETROACTIVE_PASS = NO
```
