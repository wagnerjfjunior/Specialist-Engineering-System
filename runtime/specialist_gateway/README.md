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

Non-goals: semantic intent classification, automatic adoption, project mutation, Builder configuration, deployment, database-backed policy storage or consumer-project truth storage.

`ROUTABLE` means eligible to enter project bootstrap; it is not execution proof and never grants mutation authority.
