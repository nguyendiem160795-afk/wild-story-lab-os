# Agent Registry

> Wild Story Lab OS
> Module 08 — AI Agent Operating System

Version: **1.0.0**

---

# Purpose

The Agent Registry is the authoritative catalog of all AI Agents available within Module 08.

Every production agent must be registered before it can participate in workflows.

---

# Registry Fields

| Field | Description |
|------|-------------|
| Agent ID | Unique identifier |
| Name | Agent name |
| Version | Semantic version |
| Status | Draft / Production / Deprecated |
| Owner | Responsible maintainer |
| Category | Functional domain |
| Capabilities | Primary responsibilities |
| Related Workflow | Linked workflows |

---

# Registered Agents

| Agent ID | Name | Version | Status | Category |
|----------|------|---------|--------|----------|
| AGT-STORY-PLANNER | Story Planner Agent | 1.0.0 | Production | Planning |

---

# Registration Rules

- Every Agent ID must be unique.
- Every agent must reference an approved schema.
- Every production agent requires documentation.
- Every version change must update this registry.

---

# Lifecycle

```text
Create
   ↓
Review
   ↓
Approve
   ↓
Register
   ↓
Deploy
   ↓
Maintain
   ↓
Archive
```

---

# Governance Checklist

- [ ] Unique ID assigned
- [ ] Metadata complete
- [ ] Schema validated
- [ ] Documentation linked
- [ ] Template compliant
- [ ] Example available
- [ ] Registry updated

---

# Related Documents

- agent.schema.json
- agent-template.md
- example-agent.md
- AGENT_MANIFEST.md
