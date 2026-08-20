# SES — Next Safe Action

> Registro autoritativo da próxima ação segura do SES quando este arquivo estiver em `main`.

**Next action ID:** `runtime-enforcement-gateway-operational-custom-gpt-adoption`  
**Primary target:** `SES — Specialist Router`  
**Current phase:** `RUNTIME_ENFORCEMENT_GATEWAY_OPERATIONALIZATION / CUSTOM_GPT_ADOPTION`

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
CUSTOM_GPT_OPERATIONAL_PROFILE = runtime/specialist_gateway/CUSTOM_GPT_PROFILE.md
RECOMMENDED_CUSTOM_GPT_NAME = SES — Specialist Router
ACTION_PERSISTED_OR_PUBLISHED_CONFIGURATION = NOT PROVEN
OPERATIONAL_CUSTOM_GPT_ADOPTION = NOT PROVEN
SFJM_CUSTOM_GPT_ASSUMPTION = USER_CORRECTED / INITIAL_OVERCLAIM
```

Evidence:

```text
tests/runtime/evidence/RUNTIME_ENFORCEMENT_GATEWAY_DEPLOYMENT_ATTEMPT_2026-08-20.md
tests/runtime/evidence/RUNTIME_ENFORCEMENT_GATEWAY_EXTERNAL_HEALTH_2026-08-20.md
tests/runtime/evidence/RUNTIME_ENFORCEMENT_GATEWAY_EXTERNAL_ROUTE_2026-08-20.md
tests/runtime/evidence/RUNTIME_ENFORCEMENT_GATEWAY_GPT_ACTION_PREVIEW_2026-08-20.md
```

## User-corrected consumer model

There is no separate `SFJM Custom GPT` in the current design. The existing Custom GPT name `SES -Runtime-Enforcement-Gateway` was a provisional alias chosen during setup because the editor required a name. The prior assumption that a different SFJM Custom GPT must receive the Action is preserved as an initial overclaim corrected by the user.

The minimum design is now:

```text
Human / project workflow
→ SES — Specialist Router (Custom GPT)
→ routeSpecialistRole Action
→ SES Runtime Enforcement Gateway
→ deterministic routing receipt
```

The Custom GPT is a routing client. The backend Gateway remains the enforcement service.

## Next safe action

Do not redesign or redeploy the Gateway. Adopt the versioned Custom GPT profile already defined in `runtime/specialist_gateway/CUSTOM_GPT_PROFILE.md`:

```text
1. rename the existing Custom GPT from the provisional alias to `SES — Specialist Router`;
2. replace its description with the versioned Description from CUSTOM_GPT_PROFILE.md;
3. paste the exact versioned Instructions from CUSTOM_GPT_PROFILE.md into the Builder Instructions field;
4. keep the already proven host-bound OpenAPI Action and hidden X-SES-Gateway-Key credential;
5. persist/update the Custom GPT configuration;
6. open a fresh conversation in that updated GPT;
7. request one exact adopted FECH.AI role and verify routeSpecialistRole is actually invoked, decision = ROUTABLE and mutation_authorized = false;
8. request one exact legacy/non-adopted role and verify no semantic translation occurs;
9. record the returned SES_REF and operational GPT identity without exposing secrets;
10. only then set OPERATIONAL_CUSTOM_GPT_ADOPTION = PASS.
```

Do not add a second broker GPT merely to represent SFJM. Do not embed consumer-project role maps in the GPT Instructions. If project_identifier or role is missing, the GPT must ask rather than guess.

No controller, loader, HTTP or deployment revalidation is required solely for this consumer-profile adoption unless runtime source changes materially.

Do not request, store, commit or expose `SES_GATEWAY_API_KEY` or `SES_GITHUB_TOKEN` as evidence.

```text
MINIMUM_OPERATIONAL_GATEWAY_RUNTIME = PASS
CUSTOM_GPT_PROFILE_DEFINED != CUSTOM_GPT_PROFILE_ADOPTED
ACTION_PREVIEW_INVOKED != ACTION_PUBLISHED
ROUTABLE != EXECUTED
TOOL_CAPABILITY != AUTHORIZATION
CERTIFIED_FOR_ANY_PROJECT != CONSUMER_PROJECT_ADOPTED
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
USER_CORRECTED_INITIAL_OVERCLAIM != RETROACTIVE_ERASURE
RETROACTIVE_PASS = NO
```
