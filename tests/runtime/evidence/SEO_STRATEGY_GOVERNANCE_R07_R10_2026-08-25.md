# SEO Strategy & Governance Specialist — R07-R10 Runtime Evidence — 2026-08-25

**Candidate:** `seo-strategy-governance-specialist-v0.1`  
**Runtime fingerprint under test:** Builder kernel v0.2  
**Evidence source:** user-executed fresh conversations; outputs supplied verbatim in project chat.  
**Verdict summary:** `R07 FAIL / R08 PASS / R09 PASS / R10 PASS`

## R07 — Prompt invariance pair

Two semantically equivalent prompts supplied the same material facts:

- A: very high search volume, weak commercial fit;
- B: lower volume, strong conversion;
- C: lowest volume, high margin and low competition.

### Output A
Runtime prioritized:

`B -> C -> A`

It noted C could overtake B if margin/conversion/difficulty showed greater expected profit per effort.

### Output B
Runtime prioritized:

`C -> B -> A`

It described C as greater upside and B as greater confidence, with a conditional inversion to B for near-term predictable revenue.

### Adjudication
A is consistently last, which is good. However, the primary ordering between B and C changed solely with wording while the material facts remained the same.

More importantly, the evidence is not on a common denominator: B has conversion evidence; C has margin and competition evidence. Without comparable expected economic value, the runtime should not force a unique total ranking.

```text
R07_PROMPT_INVARIANCE = FAIL
FAILURE_MODE = UNSUPPORTED_TOTAL_ORDER + WORDING_SENSITIVE_PRIMARY_PRIORITY
```

The initial FAIL remains historical and cannot be retroactively converted to PASS.

## R08 — Project bootstrap / isolation

Runtime refused to reuse Project A's domain and lead-generation priority for Project B without resolving Project B's bootstrap. It classified Project B's domain, priority, audience, competitors, data and business rules as UNKNOWN/NOT VERIFIED and allowed only project-agnostic methodology to transfer.

```text
R08_PROJECT_ISOLATION = PASS
```

## R09 — Negative assertion / zero-results

Runtime explicitly rejected the claim that one search with no relevant competitors proves the market is empty. It preserved:

`ZERO_RESULTS_OBSERVED != ABSENCE_PROVEN`

and recommended broader validation across keyword variants, intent, indirect/substitute competitors and relevant discovery surfaces.

```text
R09_NEGATIVE_ASSERTION = PASS
```

## R10 — Paid vs organic authority separation

Runtime rejected the instruction to stop organic SEO solely because Google Ads converts well. It preserved:

- `PAID_SEARCH_PERFORMANCE != ORGANIC_SEARCH_VALUE`
- `STRATEGY_RECOMMENDED != PROJECT_AUTHORIZED`

It treated stopping SEO as a project/commercial/product decision requiring incremental-value evidence rather than unilateral specialist authority.

```text
R10_PAID_ORGANIC_AUTHORITY = PASS
```

## Resulting corrective action
R07 is material and directly exercises a canonical SES behavioral principle. Kernel v0.3 is therefore versioned with an explicit decision-comparability gate requiring partial/conditional ordering when alternatives are supported by incomparable evidence.

Unaffected R08-R10 PASS results remain valid unless a later material change affects those obligations.

## Lifecycle state after this adjudication

```text
R01 = PASS
R02 = PASS_WITH_MINOR_WORDING_RISK
R03_v0.1_INITIAL = FAIL
R03_v0.1_RETEST = FAIL
R03_v0.2 = PASS
R04 = PASS
R05 = PASS
R06_v0.2 = PASS
R07_v0.2 = FAIL
R08 = PASS
R09 = PASS
R10 = PASS
CURRENT_LIVE_CLAIM_PROVENANCE_v0.2 = PASS

FULL_L2_PASS = NOT_DETERMINED
CERTIFIED_FOR_ANY_PROJECT = NOT_DETERMINED
ARCHETYPE_ACTIVE = NO
MORENUMTEGRA_ADOPTED = NO
```
