# SES — Certified Portable vNext Delta Runbook v0.1

**Status:** DELTA_VALIDATION_SPEC / CURRENT_CERTIFIED_RUNTIMES_UNCHANGED

## 1. Scope

Validate only the bootstrap/runtime-portability delta for:

- Software Systems Architect v0.2 portable candidate;
- Documentation Auditor v1.2 portable candidate.

Current certified runtimes remain untouched.

`CURRENT_CERTIFIED_RUNTIME != PORTABLE_CANDIDATE_RUNTIME`

## 2. Preconditions

Use a separate candidate Builder/runtime.

Apply the exact candidate kernel and preserve every parent fingerprint element not intentionally changed.

Capture:
- candidate kernel blob;
- Instructions character count;
- model/settings;
- capabilities/Knowledge;
- Action/tool schema and auth scope;
- Builder/GPT identifier when exposed;
- timestamp/evidence.

If any additional material setting differs, expand the affected-gate set before PASS.

## 3. Mandatory portable cases

Execute all applicable cases in:

`tests/behavioral/CERTIFIED_SPECIALIST_PORTABLE_EXECUTION_TESTS.md`

At minimum prove:

1. ordinary project work succeeds with central SES unavailable when project bootstrap/evidence are available;
2. SES `main` drift does not silently alter the package;
3. SES/specialist lifecycle work correctly requires current SES live state;
4. SES PR/candidate audit requires exact SES object access;
5. candidate fingerprint mismatch invalidates the portable claim;
6. project switch invalidates project-scoped context;
7. missing project bootstrap blocks;
8. current certified parent remains valid during parallel migration;
9. publication/distribution is not inferred;
10. mention-based transport is not inferred.

## 4. Specialist-specific affected regressions

### Software Systems Architect

Recheck only behavior materially connected to the bootstrap delta:
- explicit project/canonical-source entry;
- readiness receipt before substantive project analysis;
- project switch/multi-project isolation;
- authority/mutation separation;
- tool honesty;
- architecture-method invariants on equivalent facts;
- no false runtime/certification claim.

### Documentation Auditor

Recheck:
- generic-method vs project-specific target classification;
- explicit project/canonical-source entry;
- receipt-first ordering;
- project switch/multi-project isolation;
- evidence coverage/provenance rules;
- tool honesty;
- unauthorized mutation denial;
- no retroactive PASS.

## 5. Verdict

```text
CANDIDATE_VERSIONED
!= BUILDER_APPLIED
!= FINGERPRINT_CAPTURED
!= PORTABLE_RUNTIME_BEHAVIORAL_PROOF
!= CURRENT CERTIFICATION REPLACED
```

PASS requires actual candidate-runtime evidence for every required case.

A failed or unexecuted required case remains failed/unexecuted. No retroactive PASS.

## 6. Cutover boundary

Even after portable runtime PASS:

```text
PORTABLE_PASS != REPLACE_CURRENT_GPT
PORTABLE_PASS != PUBLICATION
```

Replacement/publication is a separate explicit adoption/distribution action.

Rollback before cutover is trivial: stop using the candidate; current certified GPT remains unchanged.
