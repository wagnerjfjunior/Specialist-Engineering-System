# SEO Strategy & Governance Specialist — R07 Prompt Invariance — v0.3

**Candidate:** `seo-strategy-governance-specialist-v0.1`  
**Builder kernel:** `seo-strategy-governance-specialist-builder-kernel-v0.3`  
**Case:** `R07 — prompt invariance / decision comparability`  
**Verdict:** `PASS / USER-EXECUTED_RUNTIME_RESULT`

## Runtime pair

Two semantically equivalent prompts supplied the same material facts with wording changes only.

### R07-A result

The runtime concluded:

```text
B and C > A
B vs C remains conditional / unresolved
```

It explicitly stated that no total order between B and C was proven because they were supported by different dimensions and lacked a common economic denominator. It requested comparable expected-value inputs such as capturable traffic, conversion rate, margin and effort/cost.

### R07-B result

The runtime concluded:

```text
{B, C} > A
B ? C remains unresolved
```

It again stated that imposing either `B > C` or `C > B` would invent comparability not supported by the supplied evidence.

## Adjudication

The two outputs preserve the same material state:

```text
A = lower commercial priority under current evidence
B and C = both superior to A
B vs C = not determined without a common denominator
```

This satisfies the v0.3 decision-comparability rules:

- `INCOMPARABLE_EVIDENCE != TOTAL_ORDER_PROVEN`
- `SAME_FACTS + EQUIVALENT_TASK -> SAME_MATERIAL_PRIORITY_STATE`
- `MISSING_COMMON_DENOMINATOR -> CONDITIONAL_OR_PARTIAL_PRIORITY`
- `WORDING_CHANGE != EVIDENCE_CHANGE`

## Historical integrity

Preserve:

```text
R07_V0_2 = FAIL / HISTORICAL
R07_V0_3 = PASS
NO_RETROACTIVE_PASS = TRUE
```

This PASS does not itself establish full L2, terminal certification, archetype activation or project adoption.

## Remaining proportional proof

One additional independent comparability case with different labels/numbers is required to show the correction is not coupled only to the original A/B/C fixture.
