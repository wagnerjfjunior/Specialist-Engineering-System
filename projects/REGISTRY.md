# SES — Project Registry

**Status:** FOUNDATION_V0_1 / PROJECT_RESOLUTION_AUTHORITY

## 1. Purpose

This registry is the SES authority for resolving a project identifier supplied by a user or specialist into one registered SES Project Adapter.

It owns project-registration metadata only. It does not own consumer-project truth, current state, authority, runtime, data or specialist rules.

## 2. Resolution contract

Project resolution must be deterministic.

```text
USER-SUPPLIED PROJECT IDENTIFIER
→ PROJECT REGISTRY
→ UNIQUE PROJECT_ID
→ UNIQUE ADAPTER PATH
→ PROJECT ADAPTER
```

Resolution rules:

1. trim surrounding whitespace;
2. match exact `PROJECT_ID` first;
3. otherwise match `CANONICAL_NAME` or an explicit `ALIAS` case-insensitively;
4. do not use fuzzy matching, semantic guessing or inferred aliases for material project resolution;
5. exactly one active registry entry must resolve;
6. zero matches = `PROJECT_NOT_REGISTERED`;
7. more than one match = `PROJECT_ID_AMBIGUOUS`;
8. unavailable registry = `PROJECT_REGISTRY_UNAVAILABLE`.

A conversation starter such as "Which project are we working on?" can collect the identifier, but the registry performs the authoritative SES-side mapping.

## 3. Required registration fields

Each active entry must define:

```text
PROJECT_ID
CANONICAL_NAME
ALIASES
ADAPTER_PATH
STATUS
```

Aliases must be explicit and unique across active entries. An alias must never silently redirect to a different project.

## 4. Source-of-truth boundary

The registry may store stable locator metadata such as names, aliases and adapter paths.

It must not store or freeze:

- current main/head SHA;
- current PR/check/deployment state;
- current blockers or next action;
- production/runtime state;
- project authority decisions;
- credentials, secrets, tenant/user data;
- copied bootstrap, continuity or specialist content.

Those remain owned by the consumer project's canonical sources reached through its adapter.

## 5. Registered projects

### FECH.AI

```text
PROJECT_ID: fechai
CANONICAL_NAME: FECH.AI
ALIASES:
- FECHAI
- FECH.AI — Projeto Principal / Master Project
- fecha.ai
ADAPTER_PATH: projects/fechai/PROJECT_ADAPTER.md
STATUS: ACTIVE
```

This registration establishes only SES-side project discovery. FECH.AI remains authoritative for its own state and rules.

### Ecossistema de Blogs, Sites, Portais e SEO

```text
PROJECT_ID: blogs-sites-portais-seo
CANONICAL_NAME: Ecossistema de Blogs, Sites, Portais e SEO
ALIASES:
- Blogs-sites-portais-seo
- Blogs Sites Portais SEO
- Blogs, Sites, Portais e SEO
- blog-sites-portais-seo
ADAPTER_PATH: projects/blogs-sites-portais-seo/PROJECT_ADAPTER.md
STATUS: ACTIVE
```

This registration establishes only SES-side project discovery. `wagnerjfjunior/Blogs-sites-portais-seo` remains authoritative for its own state, specialist contracts, lifecycle, authority and runtime evidence.

## 6. Change discipline

Adding, removing, renaming or aliasing a project changes SES project-resolution behavior and must be reviewed as a versioned SES change.

`REGISTERED != AUTHORIZED`

Registration does not grant SES or any specialist authority to mutate the consumer project.
