# SES — Direct Specialist Attachment Access Finding — 2026-09-07

**Status:** USER_SUPPLIED_UI/RUNTIME_EVIDENCE / ATTACHMENT_ACCESS_NOT_DETERMINED

## Scope

Direct execution of:

`Public-SES — Software Systems Architect`

outside the FECH.AI Project, without `@`, using the full 13-block architect test prompt.

The intended test object was the same 2000-word attachment previously read successfully through FECH.AI Project + `@`.

## Observed direct-specialist response

The specialist reported:

```text
documento anexo não está disponível no contexto que recebi nesta conversa

PROOF_LEVEL = DOCUMENT_ONLY
EXECUTION_MODE = CERTIFIED_PORTABLE_EXECUTION
PACKAGE_ID = software-systems-architect-portable-v0.3-candidate
BINDING_VERSION = v0.3-candidate
SES_BASELINE = e25cdf6b9a4f7d7ef4badc1ac3014b6e10d218e4
PACKAGE_FINGERPRINT = NOT_CAPTURED_IN_RUNTIME
FINGERPRINT_STATUS = EXTERNAL_PROOF_REQUIRED
EVIDENCE_STATUS = MISSING_EVIDENCE
CONTEXT_STATUS = BLOCKED
MUTATION_AUTHORIZATION = NONE / READ_ONLY
```

The runtime refused to execute BLOCO 1–13 by assumption and did not use external sources to fabricate the missing specification.

## Behavioral adjudication

```text
EVIDENCE_DISCIPLINE = PASS
FAIL_CLOSED = PASS
NO_HALLUCINATED_DOCUMENT_CONTENT = PASS
READ_ONLY_BOUNDARY = PASS
PACKAGE_BINDING_DISCIPLINE = PASS
```

## Attachment-access adjudication

The currently supplied screenshot does not independently prove that the attachment chip/file object was present in the direct Custom GPT message at send time.

Therefore:

```text
DIRECT_SPECIALIST_ATTACHMENT_VISIBLE = NOT_DETERMINED
DIRECT_SPECIALIST_ATTACHMENT_CONTENT_ACCESS = BLOCKED_OBSERVED
ROOT_CAUSE = NOT_DETERMINED
```

Do not yet classify this as a direct-Custom-GPT attachment transport defect.

Possible explanations still open:
1. file was not actually attached to that direct message;
2. file was attached but not transported into the Custom GPT runtime;
3. transient attachment-ingestion/UI issue.

## Comparison boundary

The prior FECH.AI Project + @ run successfully recovered controlled anchors from beginning/middle/end of the same source fixture.

Therefore the currently observed states are:

```text
@ SPECIALIST SAMPLED ATTACHMENT ACCESS = PASS
DIRECT SPECIALIST ATTACHMENT ACCESS = NOT_DETERMINED / BLOCKED_OBSERVED
```

Cognitive-quality equivalence for the 13-block test remains unexecuted because the direct specialist did not receive the document content.

## Next safe action

Run one minimal direct-Custom-GPT attachment diagnostic:

- new direct chat with Public-SES — Software Systems Architect;
- attach the exact same fixture;
- visibly confirm the attachment chip/file before send;
- ask only for ATTACHMENT_VISIBLE + filename + ANCHOR_A/B/C.

If that passes, proceed to full 13-block direct-specialist baseline.

If it fails while attachment presence is visibly proven, classify:

`DIRECT_CUSTOM_GPT_ATTACHMENT_TRANSPORT = FAIL_FOR_OBSERVED_RUNTIME`.
