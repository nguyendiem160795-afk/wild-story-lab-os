# Directory Structure

> Module 08 — AI Agent Operating System

Version: **0.1.0**

---

# Purpose

This document defines the official directory structure of the AI Agent Operating System.

Every file, document, template, schema, and future component must follow this structure.

The directory hierarchy is considered part of the system architecture and should remain stable over time.

---

# Design Objectives

The directory structure is designed to achieve the following goals:

- Predictability
- Discoverability
- Scalability
- Separation of Concerns
- Reusability
- Version Control
- Long-Term Maintainability

---

# Root Structure

```text
08-ai-agent-operating-system/
│
├── README.md
├── SYSTEM_OVERVIEW.md
├── ARCHITECTURE.md
├── AGENT_MANIFEST.md
├── DIRECTORY_STRUCTURE.md
├── VERSION.md
├── CHANGELOG.md
├── LICENSE.md
│
├── docs/
├── assets/
├── examples/
├── schemas/
├── templates/
├── workflows/
├── registry/
├── runtime/
├── memory/
├── knowledge/
├── automation/
├── qa/
└── tools/
```

---

# Root Files

## README.md

Repository entry point.

Contains:

- Overview
- Goals
- Components
- Quick Navigation

---

## SYSTEM_OVERVIEW.md

High-level explanation of the operating system.

---

## ARCHITECTURE.md

Complete architectural specification.

---

## AGENT_MANIFEST.md

Universal contract for every AI agent.

---

## DIRECTORY_STRUCTURE.md

Defines repository organization.

---

## VERSION.md

Current release information.

---

## CHANGELOG.md

History of all changes.

---

## LICENSE.md

Repository license.

---

# docs/

Purpose:

Store long-form technical documentation.

Recommended structure:

```text
docs/

architecture/

design/

guides/

standards/

references/

governance/
```

Examples:

```
Design Principles

Coding Standards

Architecture Decision Records

Developer Guide

System Rules
```

---

# assets/

Purpose:

Store reusable visual resources.

Examples:

```
Architecture Diagrams

Icons

Logos

Illustrations

Reference Images
```

Recommended structure:

```text
assets/

diagrams/

icons/

branding/

images/
```

---

# examples/

Purpose:

Provide implementation examples.

Examples:

```
Sample Agent

Sample Workflow

Sample Prompt

Sample Memory Record

Sample QA Report
```

Recommended structure:

```text
examples/

agents/

prompts/

workflows/

memory/

knowledge/
```

---

# schemas/

Purpose:

Store JSON Schema definitions.

Examples:

```
agent.schema.json

workflow.schema.json

prompt.schema.json

memory.schema.json

knowledge.schema.json
```

Schemas define validation rules across the operating system.

---

# templates/

Purpose:

Reusable document templates.

Examples:

```
Agent Template

Workflow Template

Prompt Template

Knowledge Card

QA Report

ADR Template
```

---

# workflows/

Purpose:

Store reusable workflow definitions.

Examples:

```
Video Production

Image Generation

Publishing

Documentation

Asset Review
```

Every workflow must have:

- Metadata
- Inputs
- Outputs
- Dependencies
- Validation Rules

---

# registry/

Purpose:

Maintain system registries.

Examples:

```
Agent Registry

Workflow Registry

Capability Registry

Tool Registry

Plugin Registry
```

Registry files should be machine-readable whenever possible.

---

# runtime/

Purpose:

Store runtime specifications.

Examples:

```
Prompt Runtime

Execution Runtime

Context Runtime

Variable Runtime
```

Runtime documentation should describe execution behavior rather than implementation.

---

# memory/

Purpose:

Define memory models.

Examples:

```
Conversation Memory

Project Memory

Long-Term Memory

Execution Memory
```

---

# knowledge/

Purpose:

Store knowledge system documentation.

Examples:

```
Knowledge Graph

Knowledge Cards

Metadata Standards

Retrieval Rules
```

---

# automation/

Purpose:

Document automation services.

Examples:

```
Task Automation

Scheduled Jobs

Build Pipelines

Publishing Automation
```

---

# qa/

Purpose:

Quality Assurance documentation.

Examples:

```
Validation Rules

QA Checklist

Review Process

Compliance Reports
```

---

# tools/

Purpose:

Store tool integration specifications.

Examples:

```
GitHub

Google Flow

Runway

Sora

Veo

CapCut

OpenAI
```

---

# Naming Convention

Directories should use:

```
lowercase

kebab-case
```

Examples:

```
prompt-runtime

knowledge-system

workflow-engine
```

Avoid:

```
PromptRuntime

Prompt_Runtime

Prompt Runtime
```

---

# File Naming Convention

Documentation:

```
UPPER_CASE.md
```

Examples:

```
README.md

ARCHITECTURE.md

SYSTEM_OVERVIEW.md
```

Templates:

```
kebab-case.md
```

Examples:

```
workflow-template.md

prompt-template.md
```

Schemas:

```
*.schema.json
```

Examples:

```
agent.schema.json

workflow.schema.json
```

---

# Future Expansion

The directory structure is intentionally extensible.

Future modules may introduce:

```text
integrations/

plugins/

monitoring/

analytics/

security/

cost-management/

api/

cli/
```

No existing directory should require renaming when these additions are introduced.

---

# Repository Rules

The following files must never be committed:

```
node_modules/

.cache/

.temp/

dist/

build/

coverage/

*.log
```

The following files must always be committed:

```
Documentation

Templates

Schemas

Examples

Standards

Guides
```

---

# Maintenance Rules

When adding a new directory:

1. Define its purpose.
2. Update this document.
3. Add a README if the directory is non-trivial.
4. Follow existing naming conventions.
5. Avoid duplicate responsibilities.

---

# Related Documents

- README.md
- SYSTEM_OVERVIEW.md
- ARCHITECTURE.md
- AGENT_MANIFEST.md
- VERSION.md
- CHANGELOG.md

---

# Summary

A predictable directory structure is essential for a scalable AI operating system.

Every folder should have a single responsibility, clear ownership, and documented conventions to ensure long-term maintainability across the Wild Story Lab ecosystem.