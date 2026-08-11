# SES — Architecture Boundary

**Status:** FOUNDATION_V0_1 / PROPOSED_CANONICAL_BOUNDARY

## 1. Core thesis

SES centralizes the engineering control plane for reusable specialist design while consumer projects retain their own state and authority.

```text
CENTRALIZE:
reusable specialist engineering contracts
methods
archetypes
cognitive modes
templates
validation patterns
versioning/adoption rules

DECENTRALIZE:
project truth
operational state
runtime
production
tenants/users/data
project authority
current incidents/PRs/deployments
project-local decisions
```

`CENTRAL EVOLUTION != AUTOMATIC PROJECT MUTATION`

## 2. Layer model

```text
SES CORE
  +
SPECIALIST ARCHETYPE
  +
PROJECT ADAPTER
  -> PROJECT BOOTSTRAP
  -> PROJECT CONTINUITY
  +
TASK CONTEXT
  =
CURRENT SPECIALIST CONTEXT
```

The roles are distinct:

- **Project Adapter locates.**
- **Project Bootstrap contextualizes.**
- **Project Continuity positions the project in time.**
- **Specialist Archetype supplies domain method and competence model.**
- **Task Context scopes the current request.**

## 3. Project registration

A registered project receives a small SES-side adapter under:

`projects/<project-id>/PROJECT_ADAPTER.md`

The adapter must not become a second source of project truth. It is a locator/manifest for canonical project-owned sources.

Therefore:

`FOLDER PER REGISTERED PROJECT = YES`

but:

`GPT PER PROJECT = NOT REQUIRED BY DEFAULT`

## 4. Hybrid and project-bound specialists

SES supports two architectural classes.

### 4.1 Hybrid specialist

A functional specialist can work across multiple registered projects when it can deterministically resolve the correct adapter and project bootstrap before substantive project-specific work.

Typical candidates include documentation audit, architecture, UX/product analysis, research and strategy.

### 4.2 Project-bound specialist

A project-specific instance may be preferable when isolation, authority, sensitive data, privileged mutation, production access or blast radius materially require fixed project boundaries.

Typical candidates include privileged production operators, high-risk security mutation, deployment authority or sensitive-data operations.

Hybrid is therefore the scalability default; project-bound is an isolation/risk option, not a failure of the architecture.

## 5. Conversation starters are UX, not control

A starter such as "Which project are we working on?" can initiate project resolution, but it must not be treated as evidence that the correct project configuration was loaded.

Substantive project work requires:

`PROJECT RESOLUTION + ADAPTER RESOLUTION + PROJECT BOOTSTRAP`

When continuity is material, also require:

`PROJECT CONTINUITY RESOLUTION`

## 6. Runtime loading is not yet implemented

This foundation defines the contract, not the final loading mechanism.

Potential future implementations include:

- external API/Action loading from versioned sources;
- generated project-bound specialist instances;
- other deterministic loaders.

Knowledge-file retrieval alone must not be assumed equivalent to deterministic project configuration for material authority or safety boundaries.

## 7. Non-goals of this foundation

This change does not create:

- specialist archetypes;
- Custom GPTs;
- Actions/API loaders;
- RBAC;
- deployment automation;
- project runtime control;
- universal SFJM state;
- automatic project upgrades.

The immediate purpose is to establish a stable multi-project entry model before specialist proliferation.
