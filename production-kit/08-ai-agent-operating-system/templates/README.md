# Templates

> Module 08 — AI Agent Operating System

Version: **0.1.0**

---

# Purpose

The `templates` directory contains reusable document templates used throughout the AI Agent Operating System.

Templates provide standardized structures for creating new assets, ensuring consistency across documentation, workflows, AI agents, prompts, schemas, and operational processes.

Rather than starting from scratch, contributors should begin with an approved template.

---

# Objectives

The template library is designed to:

- Standardize documentation
- Accelerate development
- Reduce duplication
- Improve maintainability
- Ensure structural consistency
- Simplify onboarding
- Support automation

---

# Template Categories

## Agent Templates

Templates for defining AI agents.

Examples:

- Agent Specification
- Agent Card
- Capability Definition
- Permission Profile

---

## Workflow Templates

Templates describing reusable workflows.

Examples:

- Workflow Specification
- Task Definition
- Execution Plan
- Retry Strategy

---

## Prompt Templates

Templates for prompt engineering.

Examples:

- System Prompt
- User Prompt
- Runtime Prompt
- Review Prompt
- Validation Prompt

---

## Documentation Templates

Templates for repository documentation.

Examples:

- Technical Specification
- Architecture Document
- User Guide
- Reference Manual

---

## Knowledge Templates

Templates used by the Knowledge System.

Examples:

- Knowledge Card
- Rule Definition
- Character Profile
- Story Card

---

## QA Templates

Templates supporting validation.

Examples:

- QA Report
- Validation Checklist
- Review Report
- Compliance Report

---

# Recommended Structure

```text
templates/
│
├── README.md
├── agents/
├── workflows/
├── prompts/
├── documentation/
├── knowledge/
├── qa/
└── reports/
```

---

# Naming Convention

Template files should use lowercase kebab-case.

Examples:

```
agent-template.md

workflow-template.md

prompt-template.md

qa-report-template.md
```

Avoid:

```
AgentTemplate.md

Workflow Template.md

template1.md
```

---

# Template Standards

Every template should contain:

- Title
- Purpose
- Scope
- Required Fields
- Optional Fields
- Example
- Related Documents

Templates should contain placeholders rather than project-specific content.

---

# Placeholder Convention

Use descriptive placeholders enclosed in double braces.

Examples:

```text
{{agent_name}}

{{workflow_id}}

{{prompt_version}}

{{author}}

{{created_date}}
```

Avoid ambiguous placeholders such as:

```text
{{text}}

{{value}}

{{item}}
```

---

# Versioning

Templates follow Semantic Versioning.

Major updates indicate structural changes.

Minor updates introduce optional sections.

Patch updates fix formatting or documentation issues.

---

# Review Process

Every new template should follow this lifecycle:

```text
Draft

↓

Review

↓

Approval

↓

Production

↓

Deprecated

↓

Archived
```

---

# Best Practices

When creating templates:

- Keep them generic.
- Avoid project-specific examples.
- Document every required field.
- Minimize optional complexity.
- Design for reuse.

---

# Future Templates

Future releases may introduce templates for:

- Plugin Development
- API Specifications
- Event Definitions
- Monitoring Reports
- Analytics Dashboards
- Cost Reports
- Release Notes
- Migration Guides

---

# Related Documents

- DIRECTORY_STRUCTURE.md
- docs/README.md
- docs/design-principles.md
- docs/glossary.md

---

# Summary

The `templates` directory provides the reusable blueprints that standardize development across the AI Agent Operating System.

Consistent templates reduce ambiguity, improve collaboration, and make automation significantly easier as the Wild Story Lab ecosystem continues to grow.