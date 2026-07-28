# Branch Strategy

> Wild Story Lab OS
> Module 08 — AI Agent Operating System

Version: **1.0.0**

---

# Purpose

This document defines the Git branching model for Module 08 to ensure predictable development, stable releases, and efficient collaboration.

---

# Branch Model

| Branch | Purpose |
|--------|---------|
| main | Production-ready code and documentation |
| develop | Integration branch for ongoing work |
| feature/* | New features and enhancements |
| hotfix/* | Critical fixes for released versions |
| release/* | Release preparation and stabilization |

---

# Workflow

1. Create a `feature/*` branch from `develop`.
2. Submit a Pull Request to `develop`.
3. Validate documentation, schemas, templates, and registries.
4. Merge `develop` into `release/*` when preparing a release.
5. Merge `release/*` into `main` after approval.
6. Apply urgent fixes through `hotfix/*` and merge back into both `main` and `develop`.

---

# Naming Convention

Examples:

```text
feature/agent-runtime
feature/prompt-engine
release/v1.1.0
hotfix/schema-validation
```

---

# Protection Rules

- Protect `main` from direct commits.
- Require Pull Request reviews.
- Keep `develop` synchronized with `main`.
- Delete merged feature branches when appropriate.

---

# Related Documents

- CONTRIBUTING.md
- pull_request_template.md
- CHANGELOG.md
