# SES — Runtime Enforcement Gateway Deployment Attempt — 2026-08-20

**Runtime source ref before this evidence-only update:** `c8e99a587a9ae1a515352477798514a641e3aeeb`  
**Runtime:** `runtime/specialist_gateway/`  
**HTTP handlers:** `api/health.py`, `api/route.py`  
**Deployment config:** `vercel.json`  
**Target platform attempted:** Vercel preview deployment

## Purpose

Attempt the external deployment proof required after PR #47 without changing the Gateway architecture or embedding secrets in SES.

Required runtime secrets remain external:

```text
SES_GITHUB_TOKEN
SES_GATEWAY_API_KEY
```

The available Vercel tool surface did not expose an environment-secret mutation operation. No secret was inserted into repository or deployment source files.

## Attempt 1 — packaging provenance rejected

The deployment operation initially returned:

```text
STATE = INITIALIZING
DEPLOYMENT_ID = dpl_GpyJd9j8T5YGwNgNBnWGxnHYXZai
URL = https://ses-runtime-enforcement-gateway-cdwi6s1zs.vercel.app
```

During self-audit, the submitted inline deployment package was found to contain reformatted copies of some runtime files rather than preserving the exact retrieved file texts from the canonical ref.

Therefore:

```text
ATTEMPT_1_PROOF_ELIGIBILITY = REJECTED
CAUSE = DEPLOYMENT_PACKAGE_PROVENANCE_NOT_BYTE_BOUND_TO_CANONICAL_SOURCE
RETROACTIVE_PASS = NO
```

The deployment ID was also not retrievable afterward, but Attempt 1 is excluded from deployment proof regardless of that platform behavior.

## Attempt 2 — canonical-source package, platform persistence failure

A second preview deployment request was made using the runtime file texts retrieved from SES ref `c8e99a587a9ae1a515352477798514a641e3aeeb` for the minimum executable bundle:

```text
api/health.py
api/route.py
runtime/specialist_gateway/__init__.py
runtime/specialist_gateway/controller.py
runtime/specialist_gateway/github_loader.py
runtime/specialist_gateway/http_api.py
vercel.json
```

The deploy operation returned:

```text
STATE = INITIALIZING
DEPLOYMENT_ID = dpl_5bWPHeznmQ9m8N2ph3jiSZGBr14s
URL = https://ses-runtime-enforcement-gateway-v01-o39hr86zp.vercel.app
INSPECTOR = https://vercel.com/wagnerjfjunior-3025s-projects/ses-runtime-enforcement-gateway-v01/5bWPHeznmQ9m8N2ph3jiSZGBr14s
```

Follow-up observations against the same connected Vercel account/team:

```text
get_deployment(team_id) = 404 / Deployment not found
get_deployment(team_slug) = 404 / Deployment not found
get_deployment_build_logs = 404 / Deployment not found
list_projects = []
web_fetch_vercel_url(/health) = unable to create shareable URL
```

The same `list_projects = []` condition was observed before deployment and remained after both deployment responses.

## Adjudication

A creation response containing an ID and URL is insufficient when the returned object cannot subsequently be resolved, inspected, listed or reached through the available platform tooling.

```text
DEPLOY_REQUEST_RESPONSE = OBSERVED
PERSISTED_DEPLOYMENT = NOT_PROVEN
BUILD_COMPLETION = NOT_PROVEN
EXTERNAL_HEALTH = NOT_PROVEN
EXTERNAL_ROUTE = NOT_PROVEN
DEPLOYED_RUNTIME = NOT_CLAIMED
ACTION_TOOL_INTEGRATION = NOT_CLAIMED
```

Current bounded state:

```text
GATEWAY_CODE = DEPLOY_READY
LOCAL_HTTP_TESTS = H01-H08 PASS 8/8
VERCEL_CONNECTOR_DEPLOYMENT_PERSISTENCE = BLOCKED / INCONSISTENT TOOL BEHAVIOR
VERCEL_ENV_SECRET_CONFIGURATION = UNAVAILABLE IN OBSERVED TOOL SURFACE
EXTERNAL_CONFIGURATION_OR_WORKING_DEPLOYMENT_SURFACE_REQUIRED = YES
```

This does not invalidate controller, canonical-loader or HTTP unit evidence because no runtime source behavior changed. It blocks only deployment/invocation gates.

## Next proof obligation

Using a working authorized Vercel project/deployment surface:

```text
1. create or associate a persistent Vercel project;
2. configure SES_GITHUB_TOKEN read-only;
3. configure SES_GATEWAY_API_KEY;
4. deploy the current Gateway runtime;
5. observe GET /health;
6. observe authenticated POST /route for one ROUTABLE FECH.AI role;
7. observe one fail-closed route;
8. bind the verified host into the OpenAPI schema;
9. configure and externally invoke the Action/tool before claiming integration.
```

No architecture redesign is required by this failure alone.
