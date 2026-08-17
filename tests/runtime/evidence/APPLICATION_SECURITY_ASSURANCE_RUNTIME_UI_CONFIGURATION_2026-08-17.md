# SES — Application Security Assurance Runtime UI Configuration Evidence — 2026-08-17

**Candidate:** `application-security-assurance-specialist-v0.1`  
**Runtime:** `g-6a8311a0836c8191a97bb9f3a39e33a3`  
**Evidence type:** `OPERATOR-PROVIDED BUILDER UI SCREENSHOT / VISUAL CONFIGURATION EVIDENCE`

## Observed configuration

The operator supplied a screenshot of the ChatGPT GPT Builder Configure view for `SES — Application Security Assurance Specialist` on 2026-08-17.

The screenshot visibly supports:

```text
MODEL = GPT-5.6 Sol (gpt-5-6)
WEB_SEARCH = ENABLED
IMAGE_GENERATION = ENABLED
DATA_ANALYSIS / CODE_INTERPRETER = ENABLED
KNOWLEDGE = EMPTY / NO FILES OBSERVED
GITHUB_ACTION = CONFIGURED / api.github.com
VISIBILITY = PRIVATE / APENAS PARA MIM
```

The configured description and four conversation starters are also visible in the Builder UI.

## Integration authority boundary

The screenshot shows the GitHub Action entry but does not by itself prove its permission semantics. READ_ONLY authority is established by the separately recorded Action schema/runtime evidence and R06 execution evidence.

Recorded runtime integration boundary remains:

```text
GITHUB_ACTION_AUTHORITY = READ_ONLY
VERCEL = DISABLED
SUPABASE = DISABLED
```

## Evidence limitations

```text
RAW BUILDER EXPORT = NOT CAPTURED
RAW PRODUCT TELEMETRY = NOT CAPTURED
SCREENSHOT HASH = NOT RECORDED IN REPOSITORY
OPERATOR-PROVIDED VISUAL EVIDENCE = YES
```

Do not infer tool invocation from capability availability.

```text
CAPABILITY ENABLED != TOOL INVOKED
TOOL CAPABILITY != AUTHORIZATION
```

This evidence closes the UI-visible capability/model/knowledge portion of the compact runtime fingerprint. It does not replace the exact Instructions payload capture, Action schema proof, R06 runtime evidence, or operator-attested R01-R08 Instructions continuity.
