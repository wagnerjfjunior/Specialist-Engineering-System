# SES — Specialist Capability / Proof Preflight Contract v0.1

**Status:** `CANDIDATE / UNIVERSAL CONTRACT`

## Purpose

Prevent a specialist from silently changing a materially requested proof level because a required tool, integration, credential or evidence source is unavailable.

This contract governs task admission. It does not grant tool access or mutation authority.

## Core invariants

```text
REQUESTED_PROOF_LEVEL != AVAILABLE_PROOF_LEVEL
TOOL_CONFIGURED != TOOL_AVAILABLE
TOOL_AVAILABLE != TOOL_INVOKED
TOOL_INVOKED != RESULT_VERIFIED
STATIC_AUDIT != LIVE_AUDIT
FALLBACK_AVAILABLE != FALLBACK_AUTHORIZED
```

A specialist must not silently downgrade a task such as `LIVE_DATABASE_AUDIT` into a repository/static audit.

## Mandatory preflight

Before substantive work when the user's requested outcome materially depends on connected-system evidence:

1. identify `REQUESTED_PROOF_LEVEL`;
2. identify the minimum `REQUIRED_CAPABILITIES`;
3. resolve whether each required capability is configured and usable for the bounded target;
4. perform a minimal read-only capability probe when safe and proportionate;
5. record `CAPABILITY_STATUS`;
6. decide task admission before producing the substantive audit.

Suggested receipt:

```text
REQUESTED_PROOF_LEVEL:
REQUIRED_CAPABILITIES:
CAPABILITY_STATUS:
TARGET:
TASK_ADMISSION:
AVAILABLE_FALLBACK:
FALLBACK_AUTHORIZATION:
```

## Admission states

```text
ADMITTED
BLOCKED_REQUIRED_CAPABILITY_UNAVAILABLE
BLOCKED_REQUIRED_EVIDENCE_UNAVAILABLE
FALLBACK_OFFERED_NOT_AUTHORIZED
FALLBACK_AUTHORIZED
```

If the requested proof level cannot be satisfied, the specialist must stop the requested audit and state the blocker before any lower-proof substantive result.

## Fallback rule

A lower-proof mode may be offered, but not silently executed when it materially changes the claim/proof boundary.

Example:

```text
REQUESTED: LIVE_DATABASE_AUDIT
AVAILABLE: STATIC_REPOSITORY_DATABASE_AUDIT

→ report blocker
→ offer static fallback
→ require explicit user acceptance before treating fallback as task fulfillment
```

The specialist may still provide a very short explanation of what static evidence is available, but must not deliver a full static audit under the original live-audit label without explicit fallback authorization.

## Capability classes

Examples of material capabilities:
- live database/catalog introspection;
- connected repository exact-ref access;
- deployment/runtime logs;
- analytics/account data;
- ad-platform state;
- browser/runtime inspection;
- external evidence source required by the requested proof level.

The exact capability set is SPECIALIST-SPECIFIC and PROJECT-LOCAL.

## Authority

Capability does not imply authorization.

```text
READ_CAPABILITY != WRITE_AUTHORIZATION
LIVE_ACCESS != PRODUCTION_MUTATION_AUTHORIZATION
```

Read-only evidence retrieval may be permitted by the applicable project/task contract. Mutations still require explicit authorization.

## Failure behavior

When a required capability is absent, inaccessible, unauthorized, erroring or returns insufficient evidence:

```text
DO NOT INFER LIVE STATE
DO NOT CLAIM TASK COMPLETION
DO NOT SUBSTITUTE MEMORY/HISTORICAL EVIDENCE
DO NOT SILENTLY DOWNGRADE PROOF LEVEL
```

Use `NOT DETERMINED`, `MISSING EVIDENCE` or a bounded blocker.

## Generalization boundary

This is a candidate universal contract because the failure mode applies across specialist domains: proof-level preservation and fallback authorization are independent of any one project or technology.

Project-specific tool names, credentials, endpoints and source-of-truth locations remain PROJECT-LOCAL. Specialist-specific required capability sets remain SPECIALIST-SPECIFIC.

## Invalidation

A specialist runtime that materially changes task-admission behavior requires proportional behavioral revalidation. Existing runtime PASS evidence does not transfer automatically.
