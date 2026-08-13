# SES — Blocked Actions

**Status:** `SFJM_OPERATIONAL_CONTINUITY_V0_1 / BLOCKED_ACTIONS`
**Canonical source:** `wagnerjfjunior/Specialist-Engineering-System`

Absence from this document does not create authorization. Capability, prior approval for another action, conversation history or a derived summary do not substitute for current applicable authority.

## 1. Blocked without explicit applicable authorization

- direct or unreviewed mutation of canonical SES state outside the normal change process;
- merge or publication decisions not explicitly authorized for the exact scope;
- external Builder configuration changes;
- changes to runtime candidate configuration merely because a versioned profile exists;
- consumer-project mutation performed from SES central evolution alone;
- automatic propagation of SES changes into FECH.AI, Blogs/Sites/Portais/SEO or any other registered project;
- retirement or deletion of any legacy project-bound specialist without the required project-local equivalence/observation/retirement gate;
- declaration of Documentation Auditor runtime certification without the required runtime evidence;
- promotion of static documentation, merged code or a versioned profile into proof of external application or runtime behavior;
- storing secrets or sensitive access material in SES continuity files;
- rewriting historical proof results merely because a later run or project decision differs.

## 2. Read-only work normally allowed within scope

When the task and tool surface permit it, the following are non-mutating activities:

- resolve live repository refs and metadata;
- read canonical SES contracts, registries, adapters and runtime evidence;
- inspect current PR/check/review state;
- compare live observations with versioned SES sources;
- synthesize bounded project status;
- identify missing evidence, drift and proof invalidation events.

Read-only capability does not authorize subsequent mutation.

## 3. Consumer-project boundary

SES continuity never becomes the authority for a consumer project's live state.

For project-specific work:

```text
SES BOOTSTRAP
→ PROJECT REGISTRY
→ PROJECT ADAPTER
→ CONSUMER PROJECT LIVE CANONICAL SOURCE
→ PROJECT BOOTSTRAP / CONTINUITY / AUTHORITY
```

If project-local continuity or authority is material and unavailable, fail closed for the affected conclusion.

## 4. Conflict rule

If `docs/NEXT_SAFE_ACTION.md` conflicts materially with bootstrap, handoff, project status, a live authoritative source or an applicable authority boundary:

1. stop execution;
2. resolve the live source and exact conflict;
3. preserve the authoritative next-action record only as the intended semantic action, not as permission to ignore the conflict;
4. reconcile the material recorded state before continuing.

## 5. Anti-loop rule

Do not create a new reconciliation cycle for an ordinary conversation change, metadata-only event or unrelated commit.

Revalidate only the evidence and continuity meaning invalidated by the material event.
