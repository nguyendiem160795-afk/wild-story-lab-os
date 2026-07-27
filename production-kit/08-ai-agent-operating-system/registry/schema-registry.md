# Schema Registry

> Wild Story Lab OS
> Module 08 — AI Agent Operating System

Version: **1.0.0**

---

# Purpose

The Schema Registry is the canonical inventory of every approved JSON Schema used by Module 08.

---

# Registered Schemas

| Schema ID | File | Version | Status | Purpose |
|-----------|------|---------|--------|---------|
| SCH-AGENT | agent.schema.json | 1.0.0 | Production | Agent definition |
| SCH-WORKFLOW | workflow.schema.json | 1.0.0 | Production | Workflow definition |
| SCH-PROMPT | prompt.schema.json | 1.0.0 | Production | Prompt definition |
| SCH-KNOWLEDGE | knowledge.schema.json | 1.0.0 | Production | Knowledge definition |
| SCH-MEMORY | memory.schema.json | 1.0.0 | Production | Memory definition |
| SCH-ASSET | asset.schema.json | 1.0.0 | Production | Asset definition |
| SCH-METADATA | metadata.schema.json | 1.0.0 | Production | Metadata definition |
| SCH-TEMPLATE | template.schema.json | 1.0.0 | Production | Template definition |
| SCH-REGISTRY | registry.schema.json | 1.0.0 | Production | Registry definition |
| SCH-VALIDATION | validation-report.schema.json | 1.0.0 | Production | Validation report |

---

# Governance Rules

- Every schema must have semantic versioning.
- Breaking changes require a major version increment.
- All production schemas must be documented and validated.

---

# Related Documents

- schemas/
- templates/
- examples/
- MANIFEST.md
