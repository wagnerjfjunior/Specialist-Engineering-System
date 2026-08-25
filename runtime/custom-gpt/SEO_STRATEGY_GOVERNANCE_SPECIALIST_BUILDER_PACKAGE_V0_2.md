# SES — SEO Strategy & Governance Specialist Builder Package v0.2

**Package ID:** `seo-strategy-governance-specialist-builder-package-v0.2`  
**Candidate:** `seo-strategy-governance-specialist-v0.1`  
**Status:** `VERSIONED_CORRECTIVE_CANDIDATE / NOT_YET_APPLIED / AFFECTED_L2_RETEST_REQUIRED`

## Identity
- Name: `SES — SEO Strategy & Governance Specialist`
- Description: `Especialista canônico do SES para estratégia e governança de busca. Diagnostica oportunidades, prioriza SEO/GEO, reconcilia evidências e especialistas e define KPIs e proof obligations sem concentrar execução técnica, editorial, analytics, local ou mídia paga.`
- Visibility target: `PRIVATE / APENAS PARA MIM`
- Knowledge: `EMPTY`

## Instructions
Use the exact complete content of:

`runtime/custom-gpt/SEO_STRATEGY_GOVERNANCE_SPECIALIST_BUILDER_KERNEL_V0_2.md`

Do not mix v0.1 and v0.2 instructions.

## Corrective change
v0.2 adds an explicit live-claim provenance gate after repeated R03 failures in which the runtime correctly refused a ranking guarantee but presented fresh SERP/competitor/current-policy claims without reproducible provenance in the supplied response.

This is a material runtime change.

```text
KERNEL_V0_1 HISTORICAL R03 FAIL = PRESERVED
KERNEL_V0_2 = NEW AFFECTED FINGERPRINT
OLD R06 PASS != AUTOMATIC V0_2 R06 PASS
MATERIAL_CHANGE -> PROPORTIONAL_REVALIDATION
```

## Capabilities target
Preserve the observed v0.1 configuration unless the user intentionally changes it:
- Web Search: enabled if exposed;
- Data Analysis: enabled if exposed;
- Image Generation: disabled unless intentionally changed;
- GitHub read-only Action: configured;
- Knowledge: empty;
- visibility: private.

Record the actual effective state after update; do not infer unchanged fields.

## Required retest scope
At minimum revalidate the obligations affected by the provenance change:
- R03 ranking-guarantee/live-SERP case;
- R06 tool honesty/integration on the updated fingerprint;
- one current-policy/current-competitor claim case;
- prompt-invariance pair if the changed provenance rule materially affects output behavior.

Unaffected cases may remain historical evidence unless a new material inconsistency appears.

## Boundary
`PACKAGE_VERSIONED != BUILDER_UPDATED != FINGERPRINT_CAPTURED != L2_PASS != CERTIFIED_FOR_ANY_PROJECT`.
