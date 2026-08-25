# SES — Search Specialist Builder Creation Handoff v0.2

**Status:** `BUILDER_CREATION_HANDOFF / SEVEN_CANDIDATES / L1_L2_PENDING`  
**Supersedes for new Builder creation:** `SEARCH_SPECIALIST_BUILDER_CREATION_HANDOFF_V0_1.md` without rewriting it.

Create all Builders as `PRIVATE / APENAS PARA MIM`. Default Knowledge is `EMPTY`. Copy the exact kernel named below; do not summarize it. Web Search/Data Analysis may be enabled if exposed. Configure only explicitly approved integrations and record actual states.

## 1. SEO Strategy & Governance
- Name: `SES — SEO Strategy & Governance Specialist`
- Description: `Especialista canônico do SES para estratégia e governança de busca. Diagnostica oportunidades, prioriza SEO/GEO, reconcilia evidências e especialistas e define KPIs e proof obligations sem concentrar execução técnica, editorial, analytics, local ou mídia paga.`
- Instructions: `runtime/custom-gpt/SEO_STRATEGY_GOVERNANCE_SPECIALIST_BUILDER_KERNEL_V0_1.md`
- Archetype candidate: `seo-strategy-governance-specialist`
- MoreNumTegra candidate role: `SEO_STRATEGY`

## 2. Technical SEO
- Name: `SES — Technical SEO Specialist`
- Description: `Especialista canônico do SES em Technical SEO. Audita crawlability, indexação, rendering, canonicals, robots, sitemaps, schema, Core Web Vitals, performance e retrievability para mecanismos de busca e IA com evidência live e sem prometer ranking.`
- Instructions: `runtime/custom-gpt/TECHNICAL_SEO_SPECIALIST_BUILDER_KERNEL_V0_1.md`
- Archetype candidate: `technical-seo-specialist`
- MoreNumTegra candidate role: `TECHNICAL_SEO`

## 3. Content & Semantic SEO
- Name: `SES — Content & Semantic SEO Specialist`
- Description: `Especialista canônico do SES em Content & Semantic SEO. Trabalha intenção de busca, entidades, topical coverage, arquitetura da informação, on-page, internal linking e GEO/AI visibility, preservando factualidade, citabilidade, evidência e verdade do projeto.`
- Instructions: `runtime/custom-gpt/CONTENT_SEMANTIC_SEO_SPECIALIST_BUILDER_KERNEL_V0_1.md`
- Archetype candidate: `content-semantic-seo-specialist`
- MoreNumTegra candidate role: `CONTENT_SEMANTIC_SEO`

## 4. SEO Analytics & Growth
- Name: `SES — SEO Analytics & Growth Specialist`
- Description: `Especialista canônico do SES em SEO Analytics & Growth. Analisa Search Console, GA4, conversões, KPIs, atribuição, experimentos e crescimento orgânico, distinguindo tráfego, causalidade, incrementalidade e valor de negócio com disciplina de evidência.`
- Instructions: `runtime/custom-gpt/SEO_ANALYTICS_GROWTH_SPECIALIST_BUILDER_KERNEL_V0_1.md`
- Archetype candidate: `seo-analytics-growth-specialist`
- MoreNumTegra candidate role: `SEO_ANALYTICS_GROWTH`

## 5. Local SEO
- Name: `SES — Local SEO Specialist`
- Description: `Especialista canônico do SES em Local SEO. Audita Google Business Profile, Maps, elegibilidade, NAP, reviews, citações, páginas locais e consistência de entidade geográfica, sem inventar presença física, perfis, avaliações ou autoridade operacional.`
- Instructions: `runtime/custom-gpt/LOCAL_SEO_SPECIALIST_BUILDER_KERNEL_V0_1.md`
- Archetype candidate: `local-seo-specialist`
- MoreNumTegra candidate role: `LOCAL_SEO` — adoption only if eligible local business/location target exists.

## 6. Authority & Digital PR
- Name: `SES — Authority & Digital PR Specialist`
- Description: `Especialista canônico do SES em Authority & Digital PR. Analisa backlinks, referring domains, brand mentions, link gaps, risco de spam e oportunidades de PR digital, separando autoridade, correlação e causalidade e sem autorizar outreach ou aquisição de links.`
- Instructions: `runtime/custom-gpt/AUTHORITY_DIGITAL_PR_SPECIALIST_BUILDER_KERNEL_V0_1.md`
- Archetype candidate: `authority-digital-pr-specialist`
- MoreNumTegra candidate role: `AUTHORITY_DIGITAL_PR` — adoption based on demonstrated demand.

## 7. Paid Search & SEM
- Name: `SES — Paid Search & SEM Specialist`
- Description: `Especialista canônico do SES em Paid Search & SEM. Estrutura e audita campanhas de busca paga, keywords, match types, negativas, bidding, orçamento, Quality Score, search terms e conversões, sem autorizar spend/publicação e sem confundir atribuição com incrementalidade.`
- Instructions: `runtime/custom-gpt/PAID_SEARCH_SEM_SPECIALIST_BUILDER_KERNEL_V0_1.md`
- Archetype candidate: `paid-search-sem-specialist`
- MoreNumTegra candidate role: `PAID_SEARCH_SEM` — operational adoption only after tracking/conversion and spend/campaign gates.

## Builder constraints
All descriptions are authored below the user's 300-character maximum. All exact kernels are deliberately materially below the 8000-character Instructions maximum. Do not paste package documents into Instructions; paste only the kernel content.

## Required return evidence per Builder
- Builder/GPT ID or URL;
- exact Name + Description;
- confirmation of complete exact kernel copy;
- actual Knowledge/capabilities/Actions/connectors;
- model/settings if exposed;
- visibility;
- date/time;
- screenshots/text evidence sufficient to bind the configuration fingerprint.

SES then executes/adjudicates the applicable L1/L2 runbooks and certification obligations. Do not add any candidate to `archetypes/REGISTRY.md` or a consumer `SPECIALIST_ROLE_MAP` merely because its Builder exists.

```text
BUILDER_CREATED != BUILDER_APPLIED_PROVEN
BUILDER_APPLIED != L1_PASS
BUILDER_APPLIED != L2_PASS
L1_L2_PASS != AUTOMATIC_CERTIFICATION
CERTIFIED_FOR_ANY_PROJECT != PROJECT_ADOPTED
```