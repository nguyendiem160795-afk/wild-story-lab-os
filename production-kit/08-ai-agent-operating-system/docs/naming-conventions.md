# Naming Conventions

> Module 08 — AI Agent Operating System

Version: **0.1.0**

---

# Purpose

This document defines the official naming conventions used throughout the AI Agent Operating System.

Consistent naming improves readability, discoverability, automation, and long-term maintainability.

Every contributor, AI agent, and automation workflow must follow these conventions.

---

# Design Goals

The naming system is designed to achieve the following objectives:

- Consistency
- Predictability
- Readability
- Searchability
- Automation Compatibility
- Scalability

---

# General Rules

Names should always be:

- Short
- Descriptive
- Consistent
- Human readable
- Machine friendly

Avoid abbreviations unless they are industry standards.

---

# Directory Names

Directories use:

```text
lowercase-kebab-case
```

Examples

```text
workflow-engine

prompt-runtime

knowledge-system

memory-engine

qa-framework
```

Avoid

```text
WorkflowEngine

Workflow_Engine

Workflow Engine
```

---

# Markdown Files

Repository entry documents use uppercase.

Examples

```text
README.md

ARCHITECTURE.md

CHANGELOG.md

VERSION.md

LICENSE.md
```

Supporting documents use lowercase kebab-case.

Examples

```text
design-principles.md

repository-standards.md

naming-conventions.md

documentation-standards.md
```

---

# JSON Schemas

Schema files use:

```text
<object>.schema.json
```

Examples

```text
agent.schema.json

workflow.schema.json

prompt.schema.json

memory.schema.json
```

---

# Agent IDs

Every AI agent must have a unique identifier.

Format

```text
AGT-###
```

Examples

```text
AGT-001

AGT-002

AGT-010

AGT-125
```

Reserved prefixes:

| Prefix | Meaning |
|---------|---------|
| AGT | AI Agent |
| SYS | System Agent |
| QA | Quality Agent |

---

# Workflow IDs

Workflow identifiers use:

```text
WF-###
```

Examples

```text
WF-001

WF-014

WF-102
```

---

# Task IDs

Task identifiers use:

```text
TSK-###
```

Examples

```text
TSK-001

TSK-015

TSK-999
```

---

# Prompt IDs

Prompt identifiers use:

```text
PRM-###
```

Examples

```text
PRM-001

PRM-021

PRM-300
```

---

# Knowledge IDs

Knowledge objects use:

```text
KNW-###
```

Examples

```text
KNW-001

KNW-045
```

---

# Memory IDs

Memory records use:

```text
MEM-###
```

Examples

```text
MEM-001

MEM-240
```

---

# Asset IDs

Reusable production assets use:

```text
AST-###
```

Examples

```text
AST-001

AST-520
```

---

# Template IDs

Templates use:

```text
TPL-###
```

Examples

```text
TPL-001

TPL-120
```

---

# Version Format

Every version follows Semantic Versioning.

```text
MAJOR.MINOR.PATCH
```

Examples

```text
0.1.0

1.0.0

2.3.5
```

---

# Variable Naming

Variables use:

```text
snake_case
```

Examples

```text
agent_id

workflow_name

execution_status

created_at
```

Avoid

```text
AgentID

workflowName

Workflow_Name
```

---

# Environment Variables

Environment variables use:

```text
UPPER_SNAKE_CASE
```

Examples

```text
OPENAI_API_KEY

PROJECT_ROOT

WORKFLOW_TIMEOUT
```

---

# Boolean Values

Boolean names should clearly express a true/false condition.

Examples

```text
is_enabled

is_active

has_permission

requires_review
```

---

# Date and Time

Use ISO 8601 whenever possible.

Example

```text
2026-07-27T09:30:00Z
```

Date only

```text
2026-07-27
```

---

# Status Values

Use Pascal Case for status enumerations.

Examples

```text
Draft

Review

Approved

Production

Deprecated

Archived
```

---

# Tags

Tags use lowercase.

Examples

```text
workflow

agent

knowledge

prompt

documentation
```

---

# Reserved Words

Avoid using reserved generic names such as:

```text
new

temp

test

final

copy

backup

misc

data
```

Use descriptive names instead.

---

# Naming Checklist

Before creating a new object, verify:

- Name is descriptive
- Name follows project conventions
- No duplicate exists
- Identifier is unique
- Version is assigned
- Documentation is updated

---

# Related Documents

- repository-standards.md
- documentation-standards.md
- glossary.md
- VERSION.md

---

# Summary

Consistent naming is one of the foundations of a maintainable operating system.

A predictable naming convention improves collaboration, automation, validation, repository navigation, and long-term scalability across the Wild Story Lab AI Agent Operating System.