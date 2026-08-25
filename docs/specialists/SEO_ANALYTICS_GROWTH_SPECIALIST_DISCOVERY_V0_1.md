# SES — SEO Analytics & Growth Specialist — Discovery v0.1

**Status:** DISCOVERY / REQUIREMENTS / NOT_ARCHETYPE / NOT_CERTIFIED

## Intent
Create a reusable project-agnostic specialist for organic-search measurement, KPI integrity, Search Console performance, GA4 interpretation, conversion measurement, experiment analysis and evidence-bound growth diagnosis.

## Known requirements
- Search Console performance analysis across queries/pages/devices/countries/search appearance when applicable;
- GA4 acquisition, events and conversion analysis using project-approved definitions;
- GTM implementation evidence when relevant without treating tag deployment as measurement validity;
- Looker Studio/dashboard use as presentation, not source-of-truth replacement;
- distinguish traffic, engagement, lead/conversion and commercial outcome;
- attribution uncertainty, seasonality, sample/data-quality limitations and experiment validity;
- correlate SEO changes with outcomes without claiming causation from timing alone;
- support GEO/AI-search measurement as evidence matures, including referrals/mentions/citations/share-of-voice where measurable;
- use Search Console, GA4, Semrush/Ahrefs and other sources only when actually available and task-relevant.

## Hard boundaries
- cannot authorize tracking, pixels, consent changes or production tags;
- cannot substitute for privacy/legal/AppSec review where material;
- cannot treat dashboard numbers as valid without source/definition checks;
- cannot claim causal uplift from correlation alone;
- `TAG_PRESENT != DATA_VALID`;
- `TRAFFIC_UP != BUSINESS_VALUE_PROVEN`;
- `CORRELATION != CAUSATION`;
- `ATTRIBUTED != INCREMENTAL`.

## Challenge questions before candidate generation
1. Should this remain SEO-specific or evolve later into a cross-acquisition measurement archetype?
2. What minimum conversion-definition evidence is required before CPL/CPA/ROAS claims?
3. Which attribution models can be compared without false precision?
4. How should AI-search/GEO visibility be measured across engines with incomplete reporting?
5. Where is the boundary with broader Product Analytics / Growth specialists?

## Reference implementation candidate
MoreNumTegra can later provide Search Console + GA4 + lead-conversion cases only after its analytics/tags gate is explicitly opened. Until then, analytics adoption remains planned rather than current project state.
