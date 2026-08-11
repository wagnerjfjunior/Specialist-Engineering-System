# SES Project Adapter — FECH.AI

**Status:** REFERENCE_IMPLEMENTATION / FOUNDATION_V0_1

This adapter describes the FECH.AI project registered in the SES Project Registry and points to its project-owned canonical sources. It intentionally contains pointers, not copied FECH.AI operational truth.

```text
PROJECT_ID: fechai
PROJECT_NAME: FECH.AI — Projeto Principal / Master Project
CANONICAL_SOURCE: GitHub repository wagnerjfjunior/fecha.ai
DEFAULT_REF_OR_RESOLUTION_RULE: resolve live main before material work
BOOTSTRAP_ENTRYPOINT: docs/bootstrap/INDEX.md
CONTINUITY_ENTRYPOINT: docs/sfjm/INDEX.md
SPECIALIST_ENTRYPOINT_OR_RESOLUTION_RULE: docs/skills/fechai-gpt-registry.md
GOVERNANCE_ENTRYPOINT: docs/governance/INDEX.md when applicable
AUTHORITY_ENTRYPOINT: resolve through the FECH.AI bootstrap and applicable canonical governance/continuity sources
ENVIRONMENT_ENTRYPOINT: docs/bootstrap/2026-06-10-fechai-saas-current-state-index.md
```

## Resolution flow

For FECH.AI project-specific specialist work:

```text
resolve wagnerjfjunior/fecha.ai main live
→ read docs/bootstrap/INDEX.md
→ resolve applicable specialist through docs/skills/fechai-gpt-registry.md
→ read the canonical specialist skill on the exact ref
→ read common project operating rules required by bootstrap
→ read governance when applicable
→ read docs/sfjm/INDEX.md and required continuity views when current-state continuity is material
→ resolve live GitHub/environment evidence material to the decision
→ perform bounded work
```

## Boundary

This file does not own or freeze:

- FECH.AI current main SHA;
- current PR/head/check state;
- current production/deployment state;
- current blockers or next action;
- FECH.AI specialist skill contents;
- project authority decisions;
- security state;
- tenants, users or data.

Those remain owned by FECH.AI and its authoritative live/project-local sources.

## Reference-implementation rule

FECH.AI may provide evidence for reusable SES patterns, but a FECH.AI rule does not become universal merely because this is the first registered project.

`REFERENCE IMPLEMENTATION != UNIVERSAL AUTHORITY`
