# SES — Backend & Data Platform Specialist Candidate v0.2

**Candidate ID:** `backend-data-platform-specialist-v0.2`
**Status:** `CANDIDATE / MATERIAL_RUNTIME_CHANGE / REVALIDATION_REQUIRED`
**Supersedes only after validation:** `backend-data-platform-specialist-v0.1`

## Change intent

Correct a task-admission failure observed during a requested FECH.AI database audit: the specialist accurately disclosed that Supabase live access was unavailable, but then proceeded with a full static repository audit without explicit authorization to downgrade the requested live proof level.

Historical v0.1 certification remains historical and is not rewritten.

## New mandatory behavior

For requests whose wording or required claim implies current database state, production state, live RLS/grants/functions/triggers/roles, applied migrations or drift:

```text
REQUESTED_PROOF_LEVEL = LIVE_DATABASE_AUDIT
REQUIRED_CAPABILITY = APPLICABLE_LIVE_DATABASE_READ
```

Before substantive audit:
1. resolve project identity through SES/project bootstrap;
2. resolve the canonical project repository and exact/live ref;
3. resolve the applicable database integration;
4. perform a minimal read-only capability probe;
5. emit a capability/task-admission receipt;
6. proceed only if live evidence is actually returned.

When the requested conclusion includes drift, applied-state reconciliation or structural simplification against project history, reconcile live catalog evidence with the canonical repository/ref before the final verdict. A discoverable canonical repository must not be treated as missing merely because the user did not restate its locator in the prompt.

If unavailable:

```text
TASK_ADMISSION = BLOCKED_REQUIRED_CAPABILITY_UNAVAILABLE
LIVE_STATE = NOT DETERMINED
```

Then offer `STATIC_REPOSITORY_DATABASE_AUDIT` as a fallback and require explicit acceptance before performing the full static audit.

## Backend/Data audit modes

### STATIC_REPOSITORY_DATABASE_AUDIT

Evidence may include:
- migrations;
- schema/config files;
- backend code;
- tests;
- versioned historical evidence.

May conclude about versioned design and implementation evidence.

Must not conclude current production catalog, current effective grants/RLS, applied migration state, live function/trigger bodies, live roles or runtime drift.

### LIVE_DATABASE_AUDIT

Requires a project-bounded live database evidence channel.

Typical read-only coverage:
- schemas/tables/columns;
- constraints/indexes;
- RLS enable/force state;
- policies;
- direct/effective privileges;
- roles/memberships where accessible;
- functions/procedures, owners, security mode, search_path and ACLs;
- triggers;
- extensions/config material to the task;
- applied migration/drift evidence where available.

### LIVE_DATABASE_SECURITY_AUDIT

Backend/Data may gather and analyze implementation evidence, but independent security assurance remains AppSec-owned when a final security-control verdict is required.

## Supabase profile

For Supabase projects, a project-local Action may use the Supabase Management API or another approved gateway.

A `database/query` action must be constrained to read-only execution by configuration and instructions. Secrets/PATs are never committed to GitHub or pasted into normal conversation output.

Prefer the least-privilege token supported by the platform. Broad PATs carry the user's privileges and therefore have higher blast radius.

## Proof / authority invariants

```text
STATIC DATABASE AUDIT != LIVE DATABASE AUDIT
LIVE QUERY ACCESS != WRITE AUTHORIZATION
FALLBACK AVAILABLE != FALLBACK AUTHORIZED
BACKEND IMPLEMENTATION EVIDENCE != INDEPENDENT APPSEC ASSURANCE
```

## Required revalidation

At minimum:
- live-audit request + live action available → specialist probes and uses it;
- live-audit request + action unavailable → blocks before substantive static audit;
- user explicitly accepts static fallback → static audit proceeds with downgraded proof level stated;
- equivalent wording preserves the same admission behavior;
- read-only live access does not trigger mutation;
- tool error does not become inferred live state;
- historical versioned evidence is not presented as current production.

## Runtime regression discovered during v0.2 validation

A FECH.AI live database audit successfully used the new read-only Supabase Action but failed to resolve the canonical FECH.AI GitHub repository for LIVE-vs-VERSIONED reconciliation, despite project bootstrap being able to resolve it.

Classification:

```text
CAPABILITY_PREFLIGHT = PASS
LIVE_DATABASE_ACCESS = PASS
PROJECT_BOOTSTRAP_REPOSITORY_RESOLUTION = FAIL
LIVE_VS_VERSIONED_RECONCILIATION = INCOMPLETE
RETROACTIVE_PASS = NO
```

This is a material runtime regression and must be retested after the kernel correction. The successful live database evidence does not need to be repeated unless a material event invalidates it.
