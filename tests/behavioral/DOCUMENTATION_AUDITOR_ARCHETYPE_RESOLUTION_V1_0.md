# SES — Documentation Auditor Archetype Resolution v1.0

**Target:** `documentation-auditor`  
**Status:** `CERTIFICATION_TEST / STATIC_DETERMINISTIC_RESOLUTION`

## Inputs

Resolve against canonical `archetypes/REGISTRY.md` using the registry's exact deterministic rules.

Required cases:

```text
A01 exact ID: documentation-auditor
A02 canonical name: SES — Documentation Auditor
A03 alias: Documentation Auditor
A04 alias case variation: ses documentation auditor
A05 unknown: documentation-auditor-unknown
A06 collision check: exactly one ACTIVE match for every accepted identity
```

## Expected

A01-A04 resolve uniquely to:

```text
ARCHETYPE_ID = documentation-auditor
CONTRACT_PATH = archetypes/documentation-auditor/ARCHETYPE.md
RESOLUTION_STATUS = ACTIVE
```

A05 fails closed with zero match. A06 finds no identity collision among ACTIVE registry entries.

## Pass rule

```text
A01-A06 = PASS
→ C14 ARCHETYPE_RESOLUTION = PASS
```

This test establishes only archetype resolution. It does not establish Builder application, runtime behavior, project readiness, mutation authority or certification by itself.
