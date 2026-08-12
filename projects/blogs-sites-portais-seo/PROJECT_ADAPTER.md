# SES Project Adapter — Ecossistema de Blogs, Sites, Portais e SEO

**Status:** FOUNDATION_V0_1 / REGISTERED_CONSUMER_PROJECT

This adapter describes the `blogs-sites-portais-seo` consumer project registered in the SES Project Registry and points to project-owned canonical sources. It intentionally contains stable locators only; it does not copy or freeze project operational truth.

```text
PROJECT_ID: blogs-sites-portais-seo
PROJECT_NAME: Ecossistema de Blogs, Sites, Portais e SEO
CANONICAL_SOURCE: GitHub repository wagnerjfjunior/Blogs-sites-portais-seo
DEFAULT_REF_OR_RESOLUTION_RULE: resolve live main before material work
BOOTSTRAP_ENTRYPOINT: bootstrap/BOOTSTRAP_CANONICO.md
CONTINUITY_ENTRYPOINT: handoffs/CURRENT.md
SPECIALIST_ENTRYPOINT_OR_RESOLUTION_RULE: config/gpts.yaml
GOVERNANCE_ENTRYPOINT: resolve through bootstrap/BOOTSTRAP_CANONICO.md and applicable docs/governance sources
AUTHORITY_ENTRYPOINT: bootstrap/BOOTSTRAP_CANONICO.md plus docs/NEXT_SAFE_ACTION.md and docs/BLOCKED_ACTIONS.md when mutation/lifecycle authority is material
ENVIRONMENT_ENTRYPOINT: config/project.yaml plus docs/PROJECT_STATUS.md when environment/project-state evidence is material
```

## Resolution flow

For project-specific specialist work:

```text
resolve wagnerjfjunior/Blogs-sites-portais-seo main live
→ read bootstrap/BOOTSTRAP_CANONICO.md
→ follow its mandatory reading order
→ read handoffs/CURRENT.md
→ read docs/PROJECT_STATUS.md
→ read docs/NEXT_SAFE_ACTION.md
→ read docs/BLOCKED_ACTIONS.md
→ read config/project.yaml
→ resolve the applicable local specialist through config/gpts.yaml
→ for a specific GPT, read its canonical document, skill, Builder instructions/manifest and tests as required by the project bootstrap
→ resolve live GitHub/environment evidence material to the requested decision
→ perform only bounded work permitted by project-local authority
```

## Project-owned boundaries

The project currently defines its own specialist registry (`config/gpts.yaml`), project manifest (`config/project.yaml`), bootstrap, lifecycle/SFJM continuity and authorization semantics. SES must consume those sources through this adapter rather than duplicate them.

The project-local registry currently includes `gpt0` through `gpt8`. Their external Builder identities and project-specific contracts remain project-owned until an explicitly validated SES migration retires a legacy Builder.

## Boundary

This adapter does not own or freeze:

- the consumer project's current `main` SHA;
- PR/head/base/check/review/thread state;
- current next lifecycle transition;
- current Builder field values or behavioral parity;
- current assets, domains, metrics, traffic, revenue or production state;
- project-local GPT skills or acceptance tests;
- Product Authority decisions;
- credentials, secrets or user data.

Those remain owned by `wagnerjfjunior/Blogs-sites-portais-seo` and its authoritative project-local/live sources.

## Authority rule

Registration enables deterministic SES project resolution only.

```text
REGISTERED != AUTHORIZED
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
```

The consumer project's current policy is READ_ONLY by default for the GitHub specialist Action. Corrections, Ready, merge, Builder changes, deploy, publication, domain/DNS changes, campaigns and other mutations remain governed by project-owned authorization sources.

## Migration rule

Registration does not retire any existing project-bound GPT. A legacy Builder may be retired only after the relevant SES archetype is independently validated for this project and the retirement gate is explicitly authorized.
