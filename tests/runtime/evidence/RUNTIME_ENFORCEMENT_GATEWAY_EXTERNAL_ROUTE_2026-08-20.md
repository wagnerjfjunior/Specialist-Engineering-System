# SES — Runtime Enforcement Gateway External Route Proof — 2026-08-20

**Canonical host:** `https://ses-runtime-enforcement-gateway.vercel.app`  
**SES ref returned by both external receipts:** `ea0e7a189be72261992249bcc357bc51dad5a4f7`  
**Evidence source:** user-supplied terminal output from authenticated `curl` requests  
**Secret handling:** `SES_GATEWAY_API_KEY` value was not requested, displayed, stored or committed.

## Purpose

Prove the deployed `POST /route` behavior for one exact adopted FECH.AI role and one legacy/non-adopted role, without semantic guessing and without mutation authority.

## R01 — exact adopted role

Request characteristics:

```text
METHOD = POST
PATH = /route
AUTH = X-SES-Gateway-Key supplied through local environment variable
PROJECT_IDENTIFIER = fechai
ROLE = documentation_audit
TASK_SCOPE = external runtime route proof
```

Observed response:

```text
HTTP = 200
STATUS = ok
SES_REF = ea0e7a189be72261992249bcc357bc51dad5a4f7
PROJECT_ID = fechai
PROJECT_ADAPTER_PATH = projects/fechai/PROJECT_ADAPTER.md
ROLE = documentation_audit
ADOPTION_STATUS = ADOPTED
ARCHETYPE_ID = documentation-auditor
ARCHETYPE_CONTRACT_PATH = archetypes/documentation-auditor/ARCHETYPE.md
ARCHETYPE_RESOLUTION_STATUS = ACTIVE
CERTIFICATION_STATUS = YES
CERTIFIED_SUBJECT = CURRENT_KERNEL_BLOB=5bc10297d9e655cf169d2680f914e446232992e0
PROJECT_BOOTSTRAP_ENTRYPOINT = docs/bootstrap/INDEX.md
DECISION = ROUTABLE
BLOCKER = NONE
MUTATION_AUTHORIZED = false
```

Adjudication:

```text
R01 = PASS
ROUTABLE != EXECUTED
MUTATION_AUTHORIZED = false
```

## R02 — legacy role fail-closed

Request characteristics:

```text
METHOD = POST
PATH = /route
AUTH = X-SES-Gateway-Key supplied through local environment variable
PROJECT_IDENTIFIER = fechai
ROLE = GPT0
TASK_SCOPE = external fail-closed routing proof
```

Observed response:

```text
HTTP = 200
STATUS = ok
SES_REF = ea0e7a189be72261992249bcc357bc51dad5a4f7
PROJECT_ID = fechai
PROJECT_ADAPTER_PATH = projects/fechai/PROJECT_ADAPTER.md
ROLE = GPT0
ADOPTION_STATUS = NOT_RESOLVED
ARCHETYPE_ID = NOT_RESOLVED
CERTIFICATION_STATUS = NOT_RESOLVED
PROJECT_BOOTSTRAP_ENTRYPOINT = docs/bootstrap/INDEX.md
DECISION = SPECIALIST_ROLE_NOT_ADOPTED
BLOCKER = SPECIALIST_ROLE_NOT_ADOPTED
MUTATION_AUTHORIZED = false
```

Adjudication:

```text
R02 = PASS
SEMANTIC_OR_FUZZY_ROLE_GUESSING = NOT OBSERVED
LEGACY_ALIAS_AUTO_ADOPTION = NO
FAIL_CLOSED = YES
```

## Result

```text
EXTERNAL_POST_ROUTE = PASS
EXACT_ADOPTED_ROLE = PASS
LEGACY_ROLE_FAIL_CLOSED = PASS
MUTATION_AUTHORITY = false
ACTION_TOOL_INVOCATION = NOT PROVEN
SPECIALIST_EXECUTION = NOT PROVEN
```

This proof establishes external routing behavior only. It does not prove Action/tool configuration, autonomous specialist execution, project-context readiness or mutation authorization.
