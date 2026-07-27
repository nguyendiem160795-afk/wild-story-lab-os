# Metadata Standards

> Module 08 — AI Agent Operating System

Version: **0.1.0**

---

# Purpose

This document defines the official metadata standards for every production asset within the AI Agent Operating System.

Metadata provides structured information that enables discovery, validation, governance, automation, traceability, indexing, and lifecycle management.

Every production asset should include standardized metadata.

---

# Objectives

The Metadata Standards framework aims to:

- Standardize asset descriptions
- Improve searchability
- Support automation
- Enable version tracking
- Improve traceability
- Simplify validation
- Increase interoperability

---

# Scope

These standards apply to:

- Documentation
- AI Agents
- Workflows
- Prompt Templates
- Knowledge Objects
- Memory Records
- JSON Schemas
- Examples
- Assets
- Configuration Files

---

# Metadata Principles

## Consistency

Metadata fields should use consistent names and formats across the repository.

---

## Completeness

Required metadata should always be present before an asset is approved.

---

## Machine Readability

Metadata should be structured so that automation tools can process it reliably.

---

## Human Readability

Metadata should remain understandable without specialized tooling.

---

# Required Metadata Fields

Every production asset should include:

- Asset ID
- Title
- Version
- Owner
- Status
- Category
- Created Date
- Last Updated
- Description

These fields establish the minimum metadata baseline.

---

# Optional Metadata Fields

Additional fields may include:

- Tags
- Keywords
- Dependencies
- Related Assets
- Review Date
- Reviewer
- Approval Status
- Source
- License

Optional metadata improves discovery and governance.

---

# Metadata Naming Rules

Field names should use:

```text
snake_case
```

Examples:

```text
asset_id

created_at

last_updated

approval_status

related_assets
```

Avoid inconsistent naming styles.

---

# Status Values

Recommended values include:

- Draft
- Review
- Approved
- Production
- Deprecated
- Archived

Status should accurately reflect the lifecycle stage.

---

# Version Metadata

Every asset should declare its version using Semantic Versioning.

Example:

```text
version: 1.2.0
```

Version history should be synchronized with CHANGELOG entries.

---

# Ownership Metadata

Ownership metadata should identify the responsible maintainer.

Typical fields:

- owner
- maintainer
- reviewer

Ownership improves accountability and maintenance planning.

---

# Cross References

Metadata may reference related assets.

Examples:

- Related Documents
- Related Workflows
- Related Prompts
- Related Agents
- Related ADRs

Cross references improve repository navigation.

---

# Validation Rules

Before publication verify:

- Required fields present
- Field names valid
- Version assigned
- Status assigned
- Owner defined
- Dates formatted correctly
- References valid

---

# Best Practices

- Keep metadata current.
- Avoid duplicate values.
- Use standardized terminology.
- Update metadata together with content.
- Review metadata during every release.

---

# Related Documents

- naming-conventions.md
- versioning-policy.md
- validation-framework.md
- repository-standards.md
- documentation-standards.md

---

# Summary

Metadata Standards establish a common language for describing production assets across the AI Agent Operating System. Consistent metadata improves discoverability, governance, automation, validation, and long-term maintainability throughout the Wild Story Lab ecosystem.
