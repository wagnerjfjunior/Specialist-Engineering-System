# Paid Search & SEM Specialist — Project Adoption — MoreNumTegra + FECH.AI — 2026-08-25

**Archetype:** `paid-search-sem-specialist`  
**Certified subject:** `paid-search-sem-specialist-v0.1`  
**Certification main SHA:** `e251392fcafb9398af90d3eed5b5b15737dd1c80`

## Authorization
Product Authority explicitly authorized adoption of the certified Paid Search & SEM Specialist in MoreNumTegra and FECH.AI on 2026-08-25.

## Preconditions
- `CERTIFIED_FOR_ANY_PROJECT = YES` verified after PR #78 merge.
- `RESOLUTION_STATUS = ACTIVE` verified through the canonical archetype registry.
- adoption remains a separate project-local lifecycle event.

## MoreNumTegra
```text
ROLE: paid_search_sem
ARCHETYPE_ID: paid-search-sem-specialist
ADOPTION_STATUS: ADOPTED
```

Project-local ad accounts, budgets, billing, conversion definitions, campaign targets, tracking/consent rules and spend/publication authority remain resolved through MoreNumTegra bootstrap/current sources.

## FECH.AI
```text
ROLE: paid_search_sem
ARCHETYPE_ID: paid-search-sem-specialist
ADOPTION_STATUS: ADOPTED
```

FECH.AI ad accounts, budgets, billing, conversion definitions, campaign targets, tracking/consent/privacy/legal rules and spend/publication authority remain resolved through FECH.AI bootstrap/current sources.

## Boundaries
```text
CERTIFIED_FOR_ANY_PROJECT != CONSUMER_PROJECT_ADOPTED
ADOPTED != PROJECT_CONTEXT_READY
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
CAMPAIGN_DESIGNED != CAMPAIGN_PUBLISHED
BUDGET_RECOMMENDED != SPEND_AUTHORIZED
ATTRIBUTED_CONVERSION != INCREMENTAL_CONVERSION
FUTURE_PROJECT != AUTOMATICALLY_ADOPTED
```

No campaign creation/edit, budget or bid change, billing action, publication, tracking/consent change, repository mutation, deployment or production mutation is authorized by these mappings.
