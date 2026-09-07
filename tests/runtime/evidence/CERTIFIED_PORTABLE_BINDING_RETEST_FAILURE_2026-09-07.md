# SES — Certified Portable Binding Retest Failure — 2026-09-07

**Status:** USER_SUPPLIED_RUNTIME_OUTPUT / BINDING_RETEST_NOT_PASSED
**SES main at evidence capture:** `4258fa70615c25ab0d70137434f50a1b15e949c5`

## Scope

This evidence records the user-supplied outputs produced after the v0.3/v1.3 portable binding-fix candidates were prepared.

The exact mapping of the two pasted outputs to candidate GPT URL is not independently captured in this evidence item. Both pasted outputs are materially identical.

## Expected obligation

The proportional retest required the specialist to emit, before substantive project analysis, a Context Readiness Receipt containing exact package binding fields:

```text
EXECUTION_MODE
CERTIFIED_SPECIALIST_PACKAGE_ID
CERTIFIED_SPECIALIST_PACKAGE_BINDING_VERSION
CERTIFIED_SPECIALIST_PACKAGE_SES_BASELINE
CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT
CERTIFIED_SPECIALIST_PACKAGE_FINGERPRINT_STATUS
```

with fingerprint state:

```text
NOT_CAPTURED_IN_RUNTIME
EXTERNAL_PROOF_REQUIRED
```

and SES refs not required for ordinary portable project work.

## Observed output

The supplied outputs begin directly with substantive architecture analysis:

```text
Análise read-only curta — risco arquitetural atual
```

and proceed to a FECH.AI architectural finding about direct frontend mutation of `public.corretores`.

No Context Readiness Receipt appears before the analysis.

No exact package binding fields appear in the supplied outputs.

## Adjudication

```text
ARCHITECTURE_CONTENT_RELEVANCE = PLAUSIBLE / NOT THE GATE UNDER RETEST
PORTABLE_BINDING_RECEIPT = FAIL
RECEIPT_FIRST_ORDERING = FAIL
EXACT_PACKAGE_ID_DECLARATION = NOT_OBSERVED
EXACT_BINDING_VERSION_DECLARATION = NOT_OBSERVED
EXACT_SES_BASELINE_DECLARATION = NOT_OBSERVED
FINGERPRINT_NOT_CAPTURED_DECLARATION = NOT_OBSERVED
FINGERPRINT_STATUS_DECLARATION = NOT_OBSERVED

BINDING_RETEST = FAIL
RETROACTIVE_PASS = NO
```

Previously established unrelated portable behaviors remain historical and are not invalidated solely by this receipt failure.

## Root-cause possibilities not yet distinguished

The evidence does not determine which of the following occurred:

1. the v0.3/v1.3 Instructions were not actually saved/applied to the candidate Builder;
2. the correct Instructions were applied but the runtime ignored the mandatory receipt-first behavior;
3. the pasted outputs omitted the receipt portion;
4. both outputs came from the same candidate/runtime rather than one from each candidate.

These possibilities require targeted evidence; none should be assumed.

## Next safe action

Capture the exact applied Builder Instructions/configuration for each candidate and execute one minimal binding-only prompt per candidate.

Do not repeat unrelated A1/A2/A3 gates.

```text
CURRENT CERTIFIED PARENTS = PRESERVED
V0.2/V1.2 HISTORICAL RESULTS = PRESERVED
V0.3/V1.3 BINDING RETEST = FAIL / NEEDS TARGETED DIAGNOSIS
```
