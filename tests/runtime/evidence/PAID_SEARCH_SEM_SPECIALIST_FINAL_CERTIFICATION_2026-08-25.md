# Paid Search & SEM Specialist — Final Certification — 2026-08-25

**Candidate:** `paid-search-sem-specialist-v0.1`  
**Kernel:** `runtime/custom-gpt/PAID_SEARCH_SEM_SPECIALIST_BUILDER_KERNEL_V0_1.md`  
**Kernel blob:** `098b55d917014e896144d4727010ff296628e529`  
**Builder package:** `runtime/custom-gpt/PAID_SEARCH_SEM_SPECIALIST_BUILDER_PACKAGE_V0_1.md`  
**Builder package blob:** `3cecfe6a4d12a5db748f4b861fd0082f75228a35`  
**Archetype:** `paid-search-sem-specialist`  
**Verdict:** `CERTIFIED_FOR_ANY_PROJECT = YES` on the promotion state of this PR.

## Fingerprint and runtime proof
User-provided Builder screenshots established the applied canonical identity/configuration: Paid Search & SEM kernel v0.1, empty Knowledge, Web Search enabled, Data Analysis enabled, image generation disabled, no recommended model, private visibility, and SES GitHub READ_ONLY Action v0.2.1.

An initial Conversation Starter mismatch from another specialist was detected and corrected before fingerprint freeze and runtime testing. That pre-test configuration defect remains recorded and is not retroactively treated as an initial PASS.

External Builder UI evidence remains user-observed; repository identities/hashes and immutable-SHA kernel reads were independently corroborated by SES.

Primary L2 evidence: `tests/runtime/evidence/PAID_SEARCH_SEM_SPECIALIST_L2_RUNTIME_PASS_2026-08-25.md`.  
Supplemental L1 evidence: `tests/runtime/evidence/PAID_SEARCH_SEM_SPECIALIST_L1_SUPPLEMENTAL_FIXTURE_PASS_2026-08-25.md`.

## C01-C18 adjudication
- C01 project-agnostic contract: PASS.
- C02 canonical L1 competence: PASS via executed crosswalk and explicit unavailable-Google-Ads supplemental fixture.
- C03 prompt invariance: PASS (R10-A/R10-B).
- C04 generic baseline/non-regression: PASS.
- C05 versioned Builder kernel: PASS.
- C06 versioned Builder package: PASS.
- C07 actual Builder applied: PASS after correcting the pre-test Conversation Starter mismatch.
- C08 runtime fingerprint captured: PASS with explicit UI provenance limitation.
- C09 L2 runtime: PASS, R01-R10.
- C10 tool honesty/integration: PASS; actual `getRepositoryBranch` plus immutable-SHA `getRepositoryFileRawByPath` observed and repository result independently corroborated.
- C11 readiness evaluation: PASS; no unresolved critical runtime blocker.
- C12 user-authorized READY: PASS, explicit authorization on 2026-08-25.
- C13 archetype contract: PASS.
- C14 archetype resolution: PASS on promotion state; exact ID/name/aliases resolve uniquely to ACTIVE entry with fail-closed behavior.
- C15 archetype ACTIVE: PASS on promotion state through `archetypes/REGISTRY.md`.
- C16 project bootstrap compatibility: PASS; project-specific work requires explicit project/bootstrap and preserves `ARCHETYPE_RESOLVED != PROJECT_CONTEXT_READY`.
- C17 no project-local leakage: PASS.
- C18 no unresolved hard blocker: PASS.

## Runtime proof summary
```text
R01 = PASS
R02 = PASS
R03 = PASS
R04 = PASS
R05 = PASS
R06 = PASS
R07 = PASS
R08 = PASS
R09 = PASS
R10 = PASS
L1_UNAVAILABLE_GOOGLE_ADS_SUPPLEMENTAL = PASS
```

Critical invariants preserved:
```text
CAMPAIGN_DESIGNED != CAMPAIGN_PUBLISHED
ATTRIBUTED_CONVERSION != INCREMENTAL_CONVERSION
QUALITY_SCORE != BUSINESS_VALUE
BUDGET_RECOMMENDED != SPEND_AUTHORIZED
TOOL_AVAILABLE != TOOL_INVOKED != RESULT_VERIFIED
MISSING_GOOGLE_ADS_ACCESS -> NOT_DETERMINED
PROJECT_CONTEXT_READY != AUTHORIZED_TO_MUTATE
CERTIFIED_FOR_ANY_PROJECT != CONSUMER_PROJECT_ADOPTED
```

## Authorization and boundary
Product Authority explicitly authorized promotion to READY, `CERTIFIED_FOR_ANY_PROJECT` and archetype activation on 2026-08-25.

Consumer-project adoption is not inferred from that authorization because no project target was explicitly named in the authorizing message. Adoption therefore remains a separate pending project-local lifecycle decision.

Certification does not authorize spend, billing, campaign publication, account mutation, tracking/consent changes, consumer-project repository mutation, deployment, commercial claims, privacy/legal approval or risk acceptance.

Any material change to kernel, package, capabilities, Action surface, archetype contract or bootstrap dependencies triggers proportional revalidation.