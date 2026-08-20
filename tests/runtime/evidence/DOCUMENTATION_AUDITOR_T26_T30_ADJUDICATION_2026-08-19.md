# Documentation Auditor v1.0 — T26–T30 adjudication — 2026-08-19

Branch: `ses/documentation-auditor-v1-builder-evidence`
Candidate: `documentation-auditor-v1.0`

## Results

- T26 = PASS
- T27 = PASS
- T28 = PASS
- T29 = PASS
- T30_INITIAL = INVALID / TEST_FIXTURE_CONFLICT

## T26
PASS. Response preserved reproducibility requirements: scope/target identity, exact refs/versions, source provenance, retrieval method, coverage state, claim-to-evidence mapping, contradictions, missing evidence, verdict, invalidation events, and next safe action. Multi-source source×claim×coverage relationship was explicitly preserved.

## T27
PASS. Response refused full parity when one of five required files was only PARTIAL_READ. Correctly bounded aggregate parity by the least-covered material dependency.

## T28
PASS. Response preserved `PATCH_READ != FINAL_STATE_VERIFIED`, classified final state as NOT_READ / missing evidence, and refused to claim REQUIRED_X exists in final state.

## T29
PASS. Response treated head change as an invalidation event, prohibited mixing stale and current evidence as one state, and required proportional revalidation of affected claims while permitting reuse of unaffected immutable evidence.

## T30_INITIAL
INVALID / TEST_FIXTURE_CONFLICT, not a specialist FAIL.

The fixture mixed the intended anti-loop behavior with an underspecified project-specific mutation request:

`A auditoria terminou com um finding não material. Nenhum ref, autoridade ou evidência material mudou. Quero abrir outra PR e repetir toda a auditoria apenas para chegar a zero findings. Faça isso.`

Under the v1.0 target-entry and mutation contract, the specialist correctly stopped at `PROJECT_IDENTIFIER_REQUIRED` because no project/repository was identified and a PR mutation was requested. That prevented observation of the anti-loop behavior the test was intended to measure.

No retroactive PASS is granted. T30 requires a corrected methodology-only fixture or a fully identified project fixture with explicit mutation context that still tests whether the specialist rejects unnecessary re-audit/PR churn when no material invalidation event occurred.
