# Registry

> Wild Story Lab OS  
> Module 08 — AI Agent Operating System

Version: **1.0.0**

---

# Purpose

The `registry/` directory is the authoritative catalog of all production artifacts managed by Module 08.

Unlike JSON schemas, registry files record the **actual inventory** of assets that exist in the repository.

---

# Registry Structure

```text
registry/
├── README.md
├── agent-registry.md
├── workflow-registry.md
├── prompt-registry.md
├── knowledge-registry.md
├── schema-registry.md
└── asset-registry.md
```

---

# Registry Responsibilities

- Maintain the canonical list of AI Agents
- Track approved Workflows
- Register Prompt assets
- Register Knowledge Objects
- Register Schemas
- Register Production Assets

---

# Registry Lifecycle

```text
Create
   ↓
Review
   ↓
Approve
   ↓
Register
   ↓
Maintain
   ↓
Archive
```

---

# Naming Convention

| Registry | ID Prefix |
|----------|-----------|
| Agent | AGT |
| Workflow | WF |
| Prompt | PRM |
| Knowledge | KNW |
| Asset | AST |
| Schema | SCH |

---

# Governance

Every production artifact must:

- Have a unique identifier
- Exist in exactly one registry
- Be versioned
- Be traceable
- Reference supporting documentation

---

# Maintenance

Registry files should be updated whenever:

- A new artifact is added
- An artifact is deprecated
- A version changes
- Ownership changes
