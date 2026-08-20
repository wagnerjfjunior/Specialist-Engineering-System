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

`github_loader.py` is the minimal canonical-source loader for an operational runtime. On each snapshot load it:

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

If canonical materialization fails, callers must fail closed and must not reuse an unproven stale snapshot as current state.

Non-goals: semantic intent classification, automatic adoption, project mutation, Builder configuration, database-backed policy storage or consumer-project truth storage.

`ROUTABLE` means eligible to enter project bootstrap; it is not execution proof and never grants mutation authority.

```text
CONTROLLER_IMPLEMENTED != DEPLOYED_SERVICE
CANONICAL_SNAPSHOT_LOADED != SPECIALIST_EXECUTED
ROUTABLE != EXECUTED
TOOL_CAPABILITY != AUTHORIZATION
```
