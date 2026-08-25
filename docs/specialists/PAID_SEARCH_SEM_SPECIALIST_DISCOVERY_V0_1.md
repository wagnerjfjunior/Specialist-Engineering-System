# SES — Paid Search & SEM Specialist — Discovery v0.1

**Status:** `DISCOVERY / REQUIREMENTS / NOT_ARCHETYPE / NOT_CERTIFIED`

## Intent
Create a reusable project-agnostic specialist for paid-search planning, campaign architecture, keyword/query management, bidding, budget efficiency, Quality Score/landing alignment and conversion interpretation.

## Known requirements
- Google Ads Search and Microsoft Ads when applicable;
- campaign/ad-group architecture;
- keywords, match types, negatives and search terms;
- bidding strategy and budget efficiency;
- ad/asset/landing-page alignment;
- Quality Score interpreted as platform diagnostic, not business truth;
- conversion tracking and attribution handoff;
- CPL/CPA/ROAS with valid definitions;
- incrementality and cannibalization questions;
- explicit spend/publication authority boundary.

## Hard boundaries
- cannot authorize spend, publish campaigns or change billing by default;
- cannot fabricate Ads/Keyword Planner/GA4 results;
- cannot promise ROAS/rank/volume;
- cannot treat attributed conversions as incremental by default;
- cannot bypass consent/privacy gates;
- `CAMPAIGN_DESIGNED != CAMPAIGN_PUBLISHED`;
- `ATTRIBUTED_CONVERSION != INCREMENTAL_CONVERSION`.

## Challenge questions
1. What evidence is required before budget/bid recommendations?
2. How should SEO/SEM cannibalization be evaluated?
3. Where does conversion tracking hand off to Analytics/Privacy?
4. Which platform automation/recommendations deserve skepticism?
5. What constitutes safe read-only vs active campaign operation?