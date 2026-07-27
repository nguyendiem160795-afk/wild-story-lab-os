# Prompt Registry

> Wild Story Lab OS
> Module 08 — AI Agent Operating System

Version: **1.0.0**

---

# Purpose

The Prompt Registry is the authoritative catalog of all approved prompt assets used by AI agents and workflows.

---

# Registry Fields

| Field | Description |
|------|-------------|
| Prompt ID | Unique identifier |
| Name | Prompt name |
| Version | Semantic version |
| Status | Draft / Production / Deprecated |
| Owner | Responsible maintainer |
| Category | Prompt domain |
| Related Workflow | Associated workflow |

---

# Registered Prompts

| Prompt ID | Name | Version | Status | Workflow |
|-----------|------|---------|--------|----------|
| PRM-STORY-PLAN | Story Planning Prompt | 1.0.0 | Production | WF-STORY-PIPELINE |

---

# Registration Rules

- Prompt IDs must be unique.
- Prompts must follow `prompt.schema.json`.
- Production prompts require documentation and validation.
- Version updates must be reflected in this registry.

---

# Lifecycle

Create → Review → Approve → Register → Use → Maintain → Archive

---

# Governance Checklist

- [ ] Unique ID assigned
- [ ] Schema validated
- [ ] Variables documented
- [ ] Example available
- [ ] Documentation linked
- [ ] Registry updated

---

# Related Documents

- prompt.schema.json
- prompt-template.md
- example-prompt.md
