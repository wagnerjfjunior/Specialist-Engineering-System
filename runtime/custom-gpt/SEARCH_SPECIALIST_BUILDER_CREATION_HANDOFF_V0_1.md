# SES — Search Specialist Builder Creation Handoff v0.1

**Status:** `BUILDER_CREATION_HANDOFF / FOUR_WAVE_A_CANDIDATES / L1_L2_PENDING`

Use this file when creating the four Custom GPT Builders. Copy fields exactly; do not infer certification or project adoption.

## 1. SEO Strategy & Governance
- Name: `SES — SEO Strategy & Governance Specialist`
- Description: `Especialista canônico do SES para estratégia e governança de busca. Diagnostica oportunidades, prioriza SEO/GEO, reconcilia evidências e especialistas e define KPIs e proof obligations sem concentrar execução técnica, editorial, analytics, local ou mídia paga.`
- Instructions: exact full content of `runtime/custom-gpt/SEO_STRATEGY_GOVERNANCE_SPECIALIST_BUILDER_KERNEL_V0_1.md`
- Candidate archetype ID: `seo-strategy-governance-specialist`
- Proposed MoreNumTegra role: `SEO_STRATEGY`

## 2. Technical SEO
- Name: `SES — Technical SEO Specialist`
- Description: `Especialista canônico do SES em Technical SEO. Audita crawlability, indexação, rendering, canonicals, robots, sitemaps, schema, Core Web Vitals, performance e retrievability para mecanismos de busca e IA com evidência live e sem prometer ranking.`
- Instructions: exact full content of `runtime/custom-gpt/TECHNICAL_SEO_SPECIALIST_BUILDER_KERNEL_V0_1.md`
- Candidate archetype ID: `technical-seo-specialist`
- Proposed MoreNumTegra role: `TECHNICAL_SEO`

## 3. Content & Semantic SEO
- Name: `SES — Content & Semantic SEO Specialist`
- Description: `Especialista canônico do SES em Content & Semantic SEO. Trabalha intenção de busca, entidades, topical coverage, arquitetura da informação, on-page, internal linking e GEO/AI visibility, preservando factualidade, citabilidade, evidência e verdade do projeto.`
- Instructions: exact full content of `runtime/custom-gpt/CONTENT_SEMANTIC_SEO_SPECIALIST_BUILDER_KERNEL_V0_1.md`
- Candidate archetype ID: `content-semantic-seo-specialist`
- Proposed MoreNumTegra role: `CONTENT_SEMANTIC_SEO`

## 4. SEO Analytics & Growth
- Name: `SES — SEO Analytics & Growth Specialist`
- Description: `Especialista canônico do SES em SEO Analytics & Growth. Analisa Search Console, GA4, conversões, KPIs, atribuição, experimentos e crescimento orgânico, distinguindo tráfego, causalidade, incrementalidade e valor de negócio com disciplina de evidência.`
- Instructions: exact full content of `runtime/custom-gpt/SEO_ANALYTICS_GROWTH_SPECIALIST_BUILDER_KERNEL_V0_1.md`
- Candidate archetype ID: `seo-analytics-growth-specialist`
- Proposed MoreNumTegra role: `SEO_ANALYTICS_GROWTH`

## Builder defaults
- Visibility during validation: `PRIVATE / APENAS PARA MIM`
- Knowledge: `EMPTY`
- Web Search: enable if exposed
- Data Analysis: enable if exposed
- GitHub: configure approved read-only Action when applicable
- Record actual model/settings/capabilities; never guess fields not exposed
- Do not activate registry/adoption merely because the Builder was created

## Required post-creation return evidence
For each Builder return to SES:
- Builder/GPT ID or URL;
- exact Name and Description;
- confirmation that Instructions were copied completely;
- screenshot or textual evidence of configured capabilities/Actions;
- model/settings if exposed;
- visibility;
- date/time.

SES then binds the runtime fingerprint and executes/adjudicates L2 using the specialist-specific runbook.

```text
BUILDER CREATED != BUILDER APPLIED PROVEN
BUILDER APPLIED != L2 PASS
L2 PASS != CERTIFIED_FOR_ANY_PROJECT
CERTIFIED_FOR_ANY_PROJECT != MORENUMTEGRA ADOPTED
```