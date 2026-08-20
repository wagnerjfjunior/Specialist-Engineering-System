# SES — Next Safe Action

> Registro autoritativo da próxima ação segura do SES quando este arquivo estiver em `main`.

**Next action ID:** `runtime-enforcement-gateway-consumer-action-adoption`  
**Primary target:** `SES Runtime Enforcement Gateway consumer integration`  
**Current phase:** `RUNTIME_ENFORCEMENT_GATEWAY_OPERATIONALIZATION / CONSUMER_ADOPTION`

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
OPENAPI_BOUND_SCHEMA = runtime/specialist_gateway/RUNTIME_ENFORCEMENT_GATEWAY.openapi.yaml
GPT_ACTION_SCHEMA_COMPATIBILITY = PASS
GPT_ACTION_PREVIEW_INVOCATION = PASS
GPT_ACTION_PREVIEW_POSITIVE_ROUTE = PASS
GPT_ACTION_PREVIEW_FAIL_CLOSED_ROUTE = PASS
GPT_ACTION_PROOF_SES_REF = 7234219a4859f7c31571371030aaad459886c0ad
MINIMUM_OPERATIONAL_GATEWAY_RUNTIME = PASS
ACTION_PERSISTED_OR_PUBLISHED_CONFIGURATION = NOT PROVEN
SFJM_ACTION_ADOPTION = NOT PROVEN
```

Evidence:

```text
tests/runtime/evidence/RUNTIME_ENFORCEMENT_GATEWAY_DEPLOYMENT_ATTEMPT_2026-08-20.md
tests/runtime/evidence/RUNTIME_ENFORCEMENT_GATEWAY_EXTERNAL_HEALTH_2026-08-20.md
tests/runtime/evidence/RUNTIME_ENFORCEMENT_GATEWAY_EXTERNAL_ROUTE_2026-08-20.md
tests/runtime/evidence/RUNTIME_ENFORCEMENT_GATEWAY_GPT_ACTION_PREVIEW_2026-08-20.md
```

## Next safe action

Do not redesign the Gateway. The minimum operational runtime and GPT Action preview compatibility are proven. Continue only with explicit consumer adoption:

```text
1. identify the operational Custom GPT that must own the Gateway Action;
2. if SFJM is the intended consumer, configure the existing host-bound OpenAPI schema directly in SFJM rather than creating another routing layer;
3. use the existing SES_GATEWAY_API_KEY as a hidden custom-header credential named X-SES-Gateway-Key;
4. add bounded consumer instructions defining when routeSpecialistRole must be called and forbidding invented project identifiers, semantic role translation and mutation-authority inference;
5. persist/update the operational GPT configuration;
6. open a fresh conversation in that operational GPT;
7. observe one exact adopted-role invocation and verify ROUTABLE + mutation_authorized=false;
8. observe one fail-closed case if proportionate;
9. record the operational consumer identity and proof without exposing secrets;
10. only then set that consumer's ACTION_ADOPTION = PASS.
```

The Custom GPT named `SES -Runtime-Enforcement-Gateway` used for the current Preview proof is a test harness unless explicitly authorized as the operational broker. Do not publish or elevate it solely because Preview tests passed.

No controller, loader, HTTP or deployment revalidation is required solely for consumer adoption unless runtime source changes materially.

Do not request, store, commit or expose `SES_GATEWAY_API_KEY` or `SES_GITHUB_TOKEN` as evidence.

```text
MINIMUM_OPERATIONAL_GATEWAY_RUNTIME = PASS
ACTION_PREVIEW_INVOKED != ACTION_PUBLISHED
TEST_HARNESS != CONSUMER_ADOPTION
ROUTABLE != EXECUTED
TOOL_CAPABILITY != AUTHORIZATION
CERTIFIED_FOR_ANY_PROJECT != CONSUMER_PROJECT_ADOPTED
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
RETROACTIVE_PASS = NO
```
