# SES — Current Handoff

**Status:** `SFJM_OPERATIONAL_CONTINUITY_V0_1 / STOP_LOSS_ROLLBACK_STATE`
**Canonical source:** `wagnerjfjunior/Specialist-Engineering-System`
**Canonical ref rule:** resolve `main` live before material work
**Continuity contract:** `core/protocols/PROJECT_CONTINUITY_CONTRACT.md`
**Authoritative next action:** `docs/NEXT_SAFE_ACTION.md`
**Next action ID:** `reconcile-ses-builders-to-multi-starter-baselines-v1`

## 1. Purpose

Preserve the durable decision and safe continuation after stopping the single-starter project-selection feature.

Consumer-project truth, continuity and authority remain project-owned.

## 2. Reading order

1. resolve SES `main` live and read `docs/bootstrap/INDEX.md`;
2. read `handoffs/CURRENT.md`;
3. read `docs/PROJECT_STATUS.md`;
4. read `docs/NEXT_SAFE_ACTION.md`;
5. read `docs/BLOCKED_ACTIONS.md`;
6. then read task-material contracts/runtime evidence.

## 3. Durable state

1. SES remains project-agnostic.
2. SFJM continuity remains operational; `LIVE_RESOLVED_STATE != MATERIAL_RECORDED_STATE`.
3. SaaS Architect v0.1 historical runtime PASS T01–T29 = 29/29 remains preserved.
4. PRs #14/#15 introduced the single-starter / selection-first / deferred cross-turn project-entry experiment.
5. PR #16 fixed EOF/`INTEGRAL_READ` overclaim behavior; preserve it.
6. PR #17 fixed the Documentation Auditor receipt-order specification contradiction; preserve receipt-before-substantive-output.
7. PR #18 bounded mechanical-enforcement claims; preserve that learning without treating it as a mandate for more prompt hardening.
8. PR #19 is closed without merge as `ABANDONED / STOP-LOSS` and must remain historical.
9. Product decision: retire `# CLIQUE PARA INICIAR → menu → number → PROJECT_SELECTED → WAIT FOR TASK → resume`.
10. Restore direct project + substantive-task bootstrap semantics and multi-starter UX.
11. Historical v0.4/v0.5/v0.6 failures remain failures; no retroactive PASS.
12. Documentation Auditor v0.8 is the post-stop-loss repository target and is not proof of external Builder application.
13. SaaS Architect repository target returns to the certified v0.1 kernel/four-starter baseline; current external Builder equivalence must be re-established separately.
14. No consumer project is automatically mutated by this rollback.

## 4. Current required behavior

For project-specific substantive work:

```text
TASK_SCOPE + EXPLICIT PROJECT_IDENTIFIER
→ SES live/bootstrap/archetype
→ projects/REGISTRY.md
→ unique Project Adapter
→ consumer project live/bootstrap/local specialist
→ task-material/mandatory sources
→ task-bound Context Readiness Receipt
→ project-specific substantive work
```

If project identity is missing for a project-specific task, ask for it directly. Do not require a generated numbered menu or numeric cross-turn selection state.

Preserve:

```text
CONTEXT_READINESS_RECEIPT
→ PROJECT-SPECIFIC VERDICT / FINDINGS / RISKS / RECOMMENDATIONS

EXACT_READER_SUCCESS != EOF_PROOF
NO_VISIBLE_TRUNCATION != EOF_PROOF
UNPROVEN_EOF -> PARTIAL_READ
INTEGRAL_READ -> POSITIVE START-THROUGH-EOF PROOF + STABLE TARGET IDENTITY
```

Keep separate:

```text
NORMATIVE_REQUIREMENT
BEHAVIORAL_COMPLIANCE
MECHANICALLY_ENFORCED_INVARIANT
```

## 5. Preserved evidence

```text
SAAS_V0_1_RUNTIME_BEHAVIORAL_PROOF: PASS / HISTORICAL / PRESERVED
SAAS_V0_2_V0_3_SELECTION_FIRST_TARGETS: SUPERSEDED_BY_STOP_LOSS

DA_V0_4_P09_ATTEMPT_1: FAIL / PRESERVED
DA_V0_4_P09_ATTEMPT_2: FAIL / PRESERVED
DA_V0_5_C01: PASS / HISTORICAL / PRESERVED
DA_V0_5_P09_ATTEMPT_1: FAIL / PRESERVED
DA_V0_6_P09_ATTEMPT_1: FAIL / PRESERVED
DA_V0_6_UNSUPPORTED_INTEGRAL_READ_PROMOTION: 0 / PRESERVED
DA_V0_6_RECEIPT_MECHANICAL_ENFORCEMENT: NOT_ESTABLISHED / PRESERVED
DA_V0_7: ABANDONED / STOP_LOSS / PR #19 NOT_MERGED
DA_V0_8: ROLLBACK_TARGET / BUILDER_NOT_YET_RECONCILED
```

## 6. Next action

Authoritative source: `docs/NEXT_SAFE_ACTION.md`.

Derived summary after this rollback becomes canonical: reconcile **both external private SES Builders** to their multi-starter post-stop-loss repository baselines, capture fresh non-secret fingerprints, execute proportional smoke only, then return to ordinary SES development.

Do not reopen the retired interaction or require its historical P01–P10 selection-first suite.

## 7. Short resume prompt

```text
SES -> resolve main live -> single-starter/menu/cross-turn selection retired by stop loss -> PR #19 remains abandoned -> direct project+task bootstrap restored -> SaaS v0.1 certified kernel + four starters restored -> DA v0.8 rollback target preserves EOF + receipt-first + evidence/authority hardening -> next: reconcile both external SES Builders to multi-starter baselines -> proportional smoke -> continue SES; do not reopen starter-menu experiment.
```
