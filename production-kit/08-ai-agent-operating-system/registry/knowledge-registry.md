# Knowledge Registry

> Wild Story Lab OS
> Module 08 — AI Agent Operating System

Version: **1.0.0**

---

# Purpose

The Knowledge Registry is the authoritative catalog of all approved Knowledge Objects used throughout the AI Agent Operating System.

Every production knowledge asset must be registered to ensure discoverability, governance, and traceability.

---

# Registry Fields

| Field | Description |
|------|-------------|
| Knowledge ID | Unique identifier |
| Title | Knowledge title |
| Version | Semantic version |
| Status | Draft / Production / Deprecated |
| Owner | Responsible maintainer |
| Category | Knowledge domain |
| Classification | Public / Internal / Restricted / Confidential |

---

# Registered Knowledge

| Knowledge ID | Title | Version | Status | Category |
|--------------|-------|---------|--------|----------|
| KNW-STORY-RULES | Story Planning Rules | 1.0.0 | Production | Story Design |

---

# Registration Rules

- Knowledge IDs must be unique.
- Knowledge must conform to `knowledge.schema.json`.
- Production knowledge requires review and approval.
- Changes must be reflected in this registry.

---

# Lifecycle

Create → Review → Approve → Register → Maintain → Archive

---

# Governance Checklist

- [ ] Unique ID assigned
- [ ] Classification defined
- [ ] Metadata complete
- [ ] References verified
- [ ] Documentation linked
- [ ] Registry updated

---

# Related Documents

- knowledge.schema.json
- knowledge-template.md
- example-knowledge.md
