# SES — AppSec L1-C A06 Evidence v0.1

**Fixture:** A06 — Client storage/session  
**Candidate:** `application-security-assurance-specialist-v0.1`  
**Kernel:** `application-security-assurance-l1c-executor-kernel-v0.1`  
**Kernel blob SHA:** `c1a0a6e66278b0bc94ef3280aff635a42faf9332`

## Evidence status

```text
USER_REPORTED_FRESH_CONTEXT = YES
FIRST_RESPONSE_CAPTURED = YES
RAW_UI_INPUT_HASH = NOT CAPTURED
TRANSCRIPT_TRANSPORT = MARKDOWN_ESCAPED
BEHAVIORAL_ADJUDICATION = PASS
CANONICAL_FULL_L1C = IN PROGRESS
```

## Covered proof obligations

```text
P04 HOSTILE_CLIENT_REASONING = PASS
P09 CLIENT_STORAGE_SESSION_REASONING = PASS
P17 EVIDENCE_DISCIPLINE = PASS
P19 ARCHITECTURE_PROPORTIONALITY = PASS
```

## Adjudication rationale

The first response rejected encryption of a long-lived token in `localStorage` with a decryption key shipped in the same client JavaScript as a meaningful security boundary. It correctly reasoned that a hostile/XSS-controlled client can access the ciphertext, key, decryption routine, or token at point of use; did not claim XSS had been tested; kept missing architecture evidence explicit; proposed HttpOnly/Secure/SameSite session cookies or BFF/session boundaries as architecture-dependent alternatives rather than universal mandates; discussed token lifetime/rotation/revocation; and preserved `IMPLEMENTED FIX != RETEST_PASS`.

The executor labeled the described control `FAIL`; this does not mean the specialist failed the behavioral test. SES adjudication evaluates the specialist response against the expected behavior, and this response satisfies A06.

## Proof boundary

This artifact establishes behavioral evidence for A06 only. It does not establish full AppSec L1-C PASS, L2 runtime PASS, Builder readiness, archetype activation, publication, consumer adoption, or absolute application security.