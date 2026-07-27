# Repository Standards

> Module 08 — AI Agent Operating System

Version: **0.1.0**

---

# Purpose

This document defines the official repository standards for the AI Agent Operating System.

Every contributor, automation workflow, and AI agent must follow these standards when creating, modifying, or maintaining repository content.

The objective is to ensure that the repository remains organized, maintainable, scalable, and production-ready.

---

# Repository Principles

The repository should always be:

- Clean
- Predictable
- Versioned
- Searchable
- Well documented
- Automation friendly
- Human readable

---

# Repository Philosophy

The repository is the **Single Source of Truth** for the AI Agent Operating System.

Documentation, templates, schemas, workflows, and examples are considered production assets and must be maintained with the same level of discipline as source code.

---

# Root Directory Rules

The repository root should contain only:

- Core documentation
- Configuration files
- License
- Changelog
- Version information
- High-level entry points

Large collections of files should always be placed inside dedicated directories.

---

# Directory Standards

Every directory must have:

- A clearly defined responsibility
- A descriptive name
- A README.md if the directory contains multiple files
- A predictable internal structure

Directories should not overlap in responsibility.

---

# File Standards

Every production file should:

- Have a clear purpose
- Use a descriptive filename
- Be version controlled
- Be referenced by related documentation

Avoid creating temporary or ambiguous files.

---

# Naming Convention

## Directories

Use:

```text
lowercase-kebab-case
```

Examples:

```text
prompt-runtime

knowledge-system

workflow-engine
```

---

## Markdown Files

Core documents:

```text
README.md

ARCHITECTURE.md

SYSTEM_OVERVIEW.md
```

Supporting documents:

```text
design-principles.md

repository-standards.md

release-policy.md
```

---

## Schema Files

```text
<object>.schema.json
```

Examples:

```text
agent.schema.json

workflow.schema.json

prompt.schema.json
```

---

# Documentation Standards

Documentation should:

- Explain one topic
- Avoid duplicated information
- Reference related documents
- Follow consistent formatting
- Use technical English

Each document should contain:

- Purpose
- Scope
- Main Content
- Related Documents
- Summary

---

# Asset Standards

Assets should:

- Be reusable
- Be production quality
- Have meaningful filenames
- Avoid duplication

Large binary files should be minimized whenever possible.

---

# Template Standards

Templates should:

- Be generic
- Avoid project-specific data
- Include placeholders
- Be reusable across workflows

---

# Example Standards

Examples should:

- Be realistic
- Be reproducible
- Demonstrate best practices
- Remain synchronized with documentation

---

# Version Control

Every significant change must include:

- Updated documentation
- Updated version if required
- Changelog entry
- Review before production

---

# Branch Strategy

Recommended branch model:

```text
main

↓

release

↓

feature/*
```

Examples:

```text
feature/workflow-engine

feature/prompt-runtime

feature/knowledge-system
```

---

# Commit Convention

Recommended format:

```text
type(scope): description
```

Examples:

```text
docs(agent): add agent manifest

docs(runtime): improve architecture

feat(workflow): add execution model

fix(schema): correct validation rules
```

Common commit types:

- feat
- fix
- docs
- refactor
- test
- chore

---

# Review Checklist

Before merging changes, verify:

- Documentation updated
- Naming conventions followed
- No duplicated files
- Links verified
- Formatting consistent
- Version information correct
- Changelog updated

---

# Files That Should Never Be Committed

Examples:

```text
node_modules/

.cache/

dist/

build/

coverage/

*.tmp

*.log

.DS_Store

Thumbs.db
```

---

# Files That Must Be Committed

Examples:

- Documentation
- Templates
- Schemas
- Examples
- Standards
- Diagrams
- Configuration files

---

# Repository Maintenance

Repository maintenance should include:

- Removing obsolete references
- Updating documentation
- Verifying links
- Archiving deprecated assets
- Reviewing folder organization

Maintenance should be performed regularly to preserve repository quality.

---

# Related Documents

- README.md
- DIRECTORY_STRUCTURE.md
- VERSION.md
- CHANGELOG.md
- docs/design-principles.md

---

# Summary

The repository standards establish a consistent foundation for organizing, maintaining, and evolving the AI Agent Operating System.

Following these standards ensures that the repository remains reliable, scalable, and easy to navigate for both human contributors and AI agents.