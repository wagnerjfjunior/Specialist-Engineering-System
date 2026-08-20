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

## Manual unblock checkpoint — Git connection and runtime secrets

After the persistence blocker above, the Vercel project UI was manually reconciled with the SES repository.

Observed from user-supplied Vercel UI evidence:

```text
CONNECTED_GIT_REPOSITORY = wagnerjfjunior/Specialist-Engineering-System
GIT_CONNECTION_STATUS = OBSERVED / CONNECTED
PREVIOUS_PRODUCTION_SOURCE = vercel deploy / NOT GIT-BOUND
```

The user then confirmed that the required runtime variables were created in Vercel:

```text
SES_GITHUB_TOKEN = USER_CONFIRMED CONFIGURED / SECRET VALUE NOT OBSERVED
SES_GATEWAY_API_KEY = USER_CONFIRMED CONFIGURED / SECRET VALUE NOT OBSERVED
```

Secret values were not requested, read, stored or committed. Final Vercel secret scopes are not independently tool-verified in this evidence event.

This evidence-only commit is intentionally used to create a new `main` commit after Git connection so Vercel can produce the first deployment attributable to the connected SES repository rather than replaying a historical `vercel deploy` artifact.

```text
RUNTIME_SOURCE_CHANGE = NO
CONTROLLER_LOADER_HTTP_RETEST_REQUIRED = NO
NEXT_AFFECTED_GATE = GIT_BOUND_DEPLOYMENT_OBSERVATION
```

## Next proof obligation

Using the connected Vercel project/deployment surface:

```text
1. merge this evidence-only trigger into SES main;
2. observe a new Vercel deployment sourced from the connected Git repository/main commit;
3. observe GET /health;
4. observe authenticated POST /route for one ROUTABLE FECH.AI role;
5. observe one fail-closed route;
6. bind the verified host into the OpenAPI schema;
7. configure and externally invoke the Action/tool before claiming integration.
```

No architecture redesign is required by the earlier deployment-tool failure alone.
