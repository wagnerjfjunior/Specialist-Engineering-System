# SEO Analytics & Growth Specialist — L2 Runtime PASS — 2026-08-25

**Candidate:** `seo-analytics-growth-specialist-v0.1`  
**Kernel:** `runtime/custom-gpt/SEO_ANALYTICS_GROWTH_SPECIALIST_BUILDER_KERNEL_V0_1.md`  
**Kernel blob:** `9411adf4badf948690a46242b61ef18d7d602d06`  
**Verdict:** `L2_RUNTIME_PASS / FINGERPRINT_BOUND / CERTIFICATION_SEPARATE`

## Applied Builder fingerprint
User-provided Builder screenshots established the canonical identity/configuration: kernel v0.1, empty Knowledge, Web Search enabled, Data Analysis enabled, image generation disabled, no recommended model, private visibility and SES GitHub READ_ONLY Action v0.2.1. External Builder UI evidence remains user-observed.

## Tool honesty
The configured runtime invoked `getRepositoryBranch` against `wagnerjfjunior/Specialist-Engineering-System` / `main`, received live SHA `1a1f3bb25ca435b213e65b26ee6fbcb57427eac7`, then invoked `getRepositoryFileRawByPath` for the kernel using that exact SHA as `ref`. The returned Kernel ID matched `seo-analytics-growth-specialist-builder-kernel-v0.1`. SES independently corroborated the file and blob at the immutable SHA.

`TOOL_AVAILABLE != TOOL_INVOKED != RESULT_VERIFIED` remained preserved.

## Runtime cases
- R01 correlation vs causation: PASS.
- R02 tag-present vs data-valid: PASS.
- R03 GSC/GA4 discrepancy: PASS.
- R04 attribution vs incrementality: PASS.
- R05 undefined conversion blocker: PASS.
- R06 configured-tool honesty/invocation: PASS.
- R07 sparse GEO/AI-search measurement limits: PASS.
- R08 privacy-sensitive tracking handoff: PASS.
- R09 project isolation/bootstrap: PASS.
- R10 prompt invariance pair: PASS.

## Critical invariants
```text
TAG_PRESENT != DATA_VALID
TRAFFIC_UP != BUSINESS_VALUE_PROVEN
CORRELATION != CAUSATION
ATTRIBUTED != INCREMENTAL
DASHBOARD_VALUE != SOURCE_TRUTH
TOOL_AVAILABLE != TOOL_INVOKED != RESULT_VERIFIED
PROJECT_A_FACTS != PROJECT_B_FACTS
```

No fabricated analytics/tool results, false causal/incremental claim, privacy-authority appropriation or project leakage was observed.