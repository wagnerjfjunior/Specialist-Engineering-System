# SES Specialist Runtime Enforcement Gateway v0.1

Minimal deterministic runtime implementation of `core/protocols/RUNTIME_ENFORCEMENT_GATEWAY_CONTRACT.md`.

It resolves:

```text
PROJECT_IDENTIFIER
→ Project Registry record
→ Project Adapter
→ exact adopted ROLE
→ ARCHETYPE_ID
→ ACTIVE archetype
→ current certification eligibility
→ bootstrap pointer
→ ROUTABLE / fail-closed decision
```

## Runtime materialization

`controller.py` remains a pure deterministic decision engine. It does not perform network I/O.

`github_loader.py` is the canonical-source loader. On each snapshot load it:

```text
resolve SES main live
→ pin SES_REF
→ read projects/REGISTRY.md at SES_REF
→ read every registered Project Adapter at SES_REF
→ read archetypes/REGISTRY.md at SES_REF
→ read docs/SPECIALIST_CERTIFICATION_STATUS.md at SES_REF
→ materialize RuntimeEnforcementGateway
```

The GitHub client is read-only and uses only Python standard-library HTTP. Private-repository access must be supplied at runtime through `SES_GITHUB_TOKEN` (preferred) or `GITHUB_TOKEN`. No secret belongs in this repository.

If canonical materialization fails, callers fail closed. The runtime does not reuse an unproven stale snapshot as current state.

## Minimum HTTP surface

`http_api.py` exposes the provider-independent service semantics. `api/health.py` and `api/route.py` are thin Python/Vercel adapters using only the standard library.

```text
GET /health
→ verify Gateway auth configuration exists
→ verify current canonical SES snapshot can be materialized
→ 200 ready / bounded 5xx unavailable

POST /route
→ require X-SES-Gateway-Key
→ validate exact PROJECT_IDENTIFIER + ROLE + TASK_SCOPE payload
→ materialize current SES snapshot
→ execute existing deterministic controller
→ return routing receipt
```

Required runtime configuration:

```text
SES_GITHUB_TOKEN = read-only GitHub access for the private SES repository
SES_GATEWAY_API_KEY = shared API secret for X-SES-Gateway-Key
```

`/health` is intentionally unauthenticated but does not expose `SES_REF`, certification subjects or project details. Authenticated `/route` includes `SES_REF` in the receipt for reproducibility.

A domain routing blocker such as `SPECIALIST_NOT_CERTIFIED` remains a successful HTTP exchange with that explicit decision in the receipt. Transport/dependency failures use bounded HTTP error states instead of masquerading as routing decisions.

The versioned OpenAPI file is a deployment template. Its server host must be replaced only after an actual deployment is observed; template existence is not Action/tool integration proof.

## Non-goals

Gateway v0.1 does not provide semantic intent classification, automatic adoption, project mutation, Builder configuration, database-backed policy storage, consumer-project truth storage or autonomous specialist execution.

`ROUTABLE` means eligible to enter project bootstrap; it is not execution proof and never grants mutation authority.

```text
CONTROLLER_IMPLEMENTED != DEPLOYED_SERVICE
HTTP_CODE_VERSIONED != DEPLOYED_SERVICE
OPENAPI_TEMPLATE != ACTION_CONFIGURED
DEPLOYED != INVOKED
CANONICAL_SNAPSHOT_LOADED != SPECIALIST_EXECUTED
ROUTABLE != EXECUTED
TOOL_CAPABILITY != AUTHORIZATION
```
