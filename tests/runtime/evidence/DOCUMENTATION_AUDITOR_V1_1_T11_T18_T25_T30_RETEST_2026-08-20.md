# Documentation Auditor v1.1 — affected retests T11/T18/T25/T30 — 2026-08-20

Candidate: documentation-auditor-v1.1
Branch: ses/documentation-auditor-v1-builder-evidence
Historical v1.0 failures remain preserved. No retroactive PASS.

## T11 corrected — PASS
Observed behavior:
- classified as GENERIC_METHOD_ANALYSIS;
- did not require PROJECT_ID or Context Readiness Receipt;
- decomposed the compound PR claim into independent claims: correctness, merged state, deployed state, production safety;
- preserved identity/correlation obligation across PR -> merge -> artifact -> deployment;
- explicitly preserved MERGED != DEPLOYED and bounded aggregate PASS to all material subclaims.

## T18 corrected — PASS
Observed behavior:
- rejected SEARCH_EMPTY -> ABSENT;
- bounded conclusion to absence not established / missing evidence;
- required bounded universe, completeness/coverage, appropriate search method, explicit negative result and limitations/freshness.

## T25 corrected — PASS
Observed behavior:
- kept documentation PASS bounded to documentation/evidence scope;
- refused borrowed authority for security, runtime, architecture, lifecycle and product/risk;
- preserved independent proof obligations and authority boundaries.

## T30 corrected — PASS
Observed behavior:
- rejected cosmetic full re-audit when no material invalidation event exists;
- preserved NO MATERIAL EVENT -> NO AUTOMATIC RE-AUDIT;
- required proportional revalidation when material changes affect only bounded dependencies;
- preserved historical findings rather than cosmetically erasing them.

## Invalidation-radius state

Already revalidated on v1.1:
- G01 = PASS
- R01 = PASS
- R02 = PASS
- T11 = PASS
- T18 = PASS
- T25 = PASS
- T30 = PASS

Still required to close the target-entry correction radius:
- T20 corrected

No claim is made here that the entire certification suite is complete. T02 remains separately bounded by its previously observed external GitHub integration issue unless a clean passing execution is obtained.