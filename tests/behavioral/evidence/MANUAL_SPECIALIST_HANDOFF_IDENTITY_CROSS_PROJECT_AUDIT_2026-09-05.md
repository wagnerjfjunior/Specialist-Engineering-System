# SES — Manual Specialist Handoff Canonical Identity Cross-Project Audit — 2026-09-05

**Status:** `CROSS_PROJECT_STATIC_AUDIT / H16-H20_SPEC_PASS / FECHAI_RUNTIME_FAILURE_PRESERVED`  
**Subject:** `core/protocols/MANUAL_SPECIALIST_HANDOFF_CONTRACT.md` v0.2 candidate

## Trigger

A FECH.AI project conversation generated a manual handoff destination:

```text
Envie ao GPT1.5 — FECH.AI Arquiteto SaaS
```

while current FECH.AI routing resolves:

```text
ROLE = architecture
ARCHETYPE_ID = software-systems-architect
CANONICAL SES IDENTITY = SES — Software Systems Architect
GPT1 / GPT1.5 = legacy/project-local continuity
```

Classification:

```text
OBSERVED_FAILURE = SPECIALIST_ROUTING_DRIFT / HANDOFF_RENDERING_IDENTITY
RETROACTIVE_ERASURE = NO
```

## Historical origin

Two independent changes created the gap:

```text
2026-08-20
FECH.AI adopted SES role routing:
architecture -> software-systems-architect
legacy GPT identities became continuity/project-local references.

2026-08-24
SES adopted MANUAL_COPY_PASTE as the current specialist transport.
The v0.1 packet had SPECIALIST_RUNTIME_NAME but did not normatively require
the human-facing target to equal the Archetype Registry CANONICAL_NAME.
```

The defect is therefore a universal handoff-rendering contract gap first observed in FECH.AI, not a FECH.AI-only specialist-design defect.

## Live consumer-project audit anchors

```text
FECH.AI main = 6da025abef73744dbb0ea971c8a0519f693c1677
Blogs/Sites/Portais/SEO main = 3433607b6d68d3b7cfc31d888375b469b707ab63
MoreNumTegra main = 27711b9644bf1ce35231bb0d1d871f10ce1d44d3
SFJM Workspace main = 06a174648426713bb45589b8606700e63bbc284e
SES base = 285b08206d334971b182e2d46646ba0b6938bdfe
```

## Cross-project findings

| Project | Static state before v0.2 | Finding |
|---|---|---|
| FECH.AI | Exact SES role map exists and says current SES identity outranks GPT legacy identity | Runtime/manual handoff failure observed: legacy GPT1.5 was rendered as destination. Requires universal contract fix plus local bootstrap/routing consumption. |
| Blogs/Sites/Portais/SEO | `config/specialists.yaml` already declares canonical name/archetype primary and legacy labels continuity-only; adapter says `LEGACY_GPT_LABEL != CURRENT_SES_IDENTITY` | No conflicting destination rendering found in static search. Runtime absence is not proven. |
| MoreNumTegra | Uses exact `ROLE -> ARCHETYPE_ID`; no legacy GPT destination pattern found | Static routing is compatible, but v0.1 had no universal target-rendering obligation. Susceptible in principle until v0.2 is consumed. |
| SFJM Workspace | Only Documentation Auditor adopted; exact role map; no legacy GPT destination pattern found | Static routing is compatible, but v0.1 had no universal target-rendering obligation. Susceptible in principle until v0.2 is consumed. |

```text
NO_STATIC_CONFLICT_FOUND != RUNTIME_ABSENCE_PROVEN
```

## v0.2 correction

Universal rule:

```text
SES SELECTED ARCHETYPE
-> archetypes/REGISTRY.md
-> CANONICAL_NAME
-> SPECIALIST_TARGET_NAME

SPECIALIST_TARGET_NAME = ARCHETYPE_REGISTRY.CANONICAL_NAME
LEGACY_ALIAS != SPECIALIST_TARGET_NAME
PROJECT_LOCAL_RULES != SPECIALIST_TARGET_NAME
SPECIALIST_RUNTIME_NAME != ROUTING_AUTHORITY
```

An unmapped project-local role remains project-local. The new rule does not fabricate SES adoption or replace a local specialist when no SES archetype is selected.

## H16-H20 static adjudication

```text
H16 CANONICAL_TARGET_IDENTITY = PASS
H17 LEGACY_ALIAS_NON_AUTHORITY = PASS
H18 CROSS_PROJECT_CANONICAL_NAME_CONSISTENCY = PASS
H19 UNMAPPED_PROJECT_LOCAL_ROLE_REMAINS_LOCAL = PASS
H20 MANUAL_HANDOFF_RENDERING = PASS

H16-H20 = PASS / SPEC_CONFORMANCE
```

The four registered consumer Project Adapters are updated in this candidate to bind manual handoff rendering to the same universal contract.

## Scope boundary

This audit proves static contract/adaptor consistency for the v0.2 candidate. It does not prove that every external ChatGPT project conversation has already consumed the new merged ref.

Required completion work:

1. merge the SES v0.2 contract;
2. update consumer-project bootstrap/routing pointers where needed so project conversations explicitly consume the current manual handoff contract;
3. perform bounded post-merge static verification on all registered consumer projects;
4. preserve FECH.AI's observed failure as historical evidence; do not rewrite it as a PASS.
