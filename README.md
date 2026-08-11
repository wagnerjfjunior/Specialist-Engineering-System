# Specialist Engineering System (SES)

SES is a project-agnostic system for designing, challenging, generating, testing, validating, versioning and evolving AI specialists across different projects and domains. SES is not itself a specialist for any particular product or project.

## Canonical entrypoints

- SES bootstrap: `docs/bootstrap/INDEX.md`
- Registered-project resolution: `projects/REGISTRY.md`

Material SES work should begin from the bootstrap. Project-specific work must resolve the project through the registry and its adapter before loading project-owned bootstrap, continuity or specialist sources.

## Core boundary

SES owns reusable specialist-engineering contracts and project-registration metadata. Consumer projects retain authority over their own truth, live operational state, environments, runtime, data and project-local decisions.

`CENTRAL EVOLUTION != AUTOMATIC PROJECT MUTATION`
