# SES — Backend & Data Platform Specialist — Builder Pre-Create Fingerprint — 2026-08-17

**Candidate:** `backend-data-platform-specialist-v0.1`  
**Builder kernel:** `backend-data-platform-specialist-builder-kernel-v0.1`  
**Builder kernel blob SHA:** `0d3c264cc4367ed8671fb7b07c28de24bf821819`  
**Builder package:** `backend-data-platform-specialist-builder-package-v0.1`  
**Builder package blob SHA:** `b5974bbd9e3d16c89f06e50c9be65abe07aeeb49`  
**Evidence class:** operator-supplied Builder screenshots + supplied Action schema  
**State:** `PRE_CREATE / RUNTIME NOT YET CREATED`

## 1. Builder identity observed

Observed in Builder UI:

```text
RUNTIME_NAME = SES — Backend & Data Platform Specialist
BUILDER_STATE = Rascunho / PRE_CREATE
CREATE_BUTTON_VISIBLE = YES
VISIBILITY = NOT YET ESTABLISHED FROM SUPPLIED SCREENSHOTS
GPT_ID_OR_FINAL_URL = NOT YET ESTABLISHED
```

The editor URL is only partially visible in the screenshot and is not recorded as an exact runtime identifier.

## 2. Instructions binding target

Canonical target remains:

```text
KERNEL_BLOB_SHA = 0d3c264cc4367ed8671fb7b07c28de24bf821819
INSTRUCTIONS_CHARACTER_COUNT_TARGET = 7389
INSTRUCTIONS_UTF8_BYTES_TARGET = 7401
INSTRUCTIONS_COMPLETE_COPY = NOT YET DIRECTLY EVIDENCED BY SUPPLIED SCREENSHOTS
BUILDER_ACCEPTED_WITHOUT_TRUNCATION = NOT YET ESTABLISHED
```

No inference is made from package design to actual Builder acceptance.

## 3. GitHub Action fingerprint observed

Supplied schema identifies:

```text
OPENAPI = 3.1.0
ACTION_TITLE = SES GitHub READ_ONLY
ACTION_VERSION = 0.2.1
SERVER = https://api.github.com
MUTATION_ENDPOINTS_EXPOSED = NONE OBSERVED IN SUPPLIED SCHEMA
```

Canonical SES schema artifact remains:

```text
runtime/custom-gpt/GITHUB_READONLY_ACTION.openapi.yaml
CANONICAL_SCHEMA_BLOB_SHA = 1e6237e806fd84716ec13b019e6617ad4110a211
```

Observed available operations in Builder UI / supplied schema:

```text
getAuthenticatedGitHubUser
getRepositoryMetadata
listRepositoryBranches
getRepositoryBranch
getGitCommitObject
getGitTree
getRepositoryFileRawByPath
getGitBlobRaw
getRepositoryCommit
getPullRequest
listPullRequestFiles
listPullRequestReviews
listPullRequestReviewComments
listCommitCheckRuns
listWorkflowRuns
compareRepositoryRefs
```

## 4. Authentication state observed

Builder authentication dialog shows:

```text
AUTHENTICATION_TYPE = API KEY
API_KEY_VALUE = MASKED / NOT RECORDED
AUTH_HEADER_MODE = BEARER
```

No credential value is stored in this evidence artifact.

## 5. Runtime Action test evidence

Observed successful health-check:

```text
OPERATION = getAuthenticatedGitHubUser
RESULT = SUCCESS
AUTHENTICATED_GITHUB_USER = Wagner Fernandes (wagnerjfjunior)
GITHUB_USER_ID = 228261219
```

Observed branch lookup test:

```text
OPERATION = getRepositoryBranch
TARGET_OWNER = wagnerjfjunior
TARGET_REPO = backend-data-platform-specialist-v0.1
TARGET_BRANCH = main
RESULT = 404 NOT FOUND
```

Interpretation boundary:

```text
GITHUB ACTION CONNECTIVITY/AUTHENTICATION = EVIDENCED
ACCESS TO SES REPOSITORY/REF = NOT YET PROVEN BY THIS TEST
404 ON INVENTED/INCORRECT REPOSITORY TARGET != ACTION FAILURE
```

The next bounded Action verification should target the canonical SES repository, e.g. `wagnerjfjunior/Specialist-Engineering-System`, with an explicit branch/ref.

## 6. Other fingerprint fields

Not established by the supplied screenshots and therefore not inferred:

```text
KNOWLEDGE = NOT CAPTURED IN THIS EVIDENCE
WEB_SEARCH = NOT CAPTURED
DATA_ANALYSIS = NOT CAPTURED
IMAGE_GENERATION = NOT CAPTURED
SUPABASE_STATE = NOT CAPTURED DIRECTLY
VERCEL_STATE = NOT CAPTURED DIRECTLY
MODEL = NOT CAPTURED
MODEL_SETTINGS = NOT CAPTURED
FINAL_VISIBILITY = NOT CAPTURED
FINAL_GPT_ID_OR_URL = NOT CAPTURED
```

Package target still requires Knowledge empty, Supabase disabled and Vercel disabled, but target configuration is not treated as observed runtime state until directly captured.

## 7. Proof boundary

```text
BUILDER PACKAGE VERSIONED = YES
BUILDER PRE_CREATE CONFIG EVIDENCE = PARTIAL
GITHUB ACTION AUTHENTICATION = PASS
GITHUB ACTION HEALTH CHECK = PASS
SES REPOSITORY READ PROOF = NOT YET EXECUTED
FINAL BUILDER FINGERPRINT = NOT YET COMPLETE
BUILDER CREATED = NO / NOT YET EVIDENCED
L2 EXECUTION = NOT STARTED
```

This pre-create artifact must be supplemented after Builder creation with the final GPT URL/ID, exact Instructions-fit evidence, final capability states, Knowledge state, visibility and a bounded read of the canonical SES repository/ref.