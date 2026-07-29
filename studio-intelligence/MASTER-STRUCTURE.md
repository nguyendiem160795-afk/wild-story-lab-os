
# MASTER-STRUCTURE.md
Version: 1.0.0
Status: Draft (Architecture Freeze Candidate)

# Purpose

This document defines the canonical information architecture of the
`studio-intelligence` repository. No new folders or documentation
domains should be introduced until this document is updated.

---

# Top Level Structure

```text
studio-intelligence/
│
├── README.md
├── ARCHITECTURE.md
├── ROADMAP.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SPECIFICATION-STANDARD.md
├── FOLDER-STANDARD.md
│
├── architecture/
├── standards/
├── specifications/
├── governance/
├── glossary/
├── decisions/
└── templates/
```

---

# Directory Responsibilities

## architecture/

Contains the architectural knowledge of Wild Story Lab OS.

Recommended structure:

```text
architecture/
├── README.md
├── SUMMARY.md
├── 00-overview.md
├── 01-design-philosophy.md
├── 02-core-principles.md
├── 03-system-layers.md
├── 04-repository-architecture.md
├── 05-module-architecture.md
├── 06-runtime-architecture.md
├── 07-knowledge-architecture.md
├── 08-ai-workflow.md
├── 09-human-workflow.md
├── 10-data-flow.md
├── 11-governance.md
├── 12-versioning.md
├── 13-security.md
├── 14-scalability.md
├── 15-adr.md
└── 16-future.md
```

## standards/

Global engineering, documentation and naming standards.

## specifications/

Formal specifications for every subsystem.

## governance/

Policies, contribution workflow and review process.

## glossary/

Canonical terminology and definitions.

## decisions/

Architecture Decision Records (ADR).

## templates/

Reusable templates for documents.

---

# Naming Convention

- lower-case
- kebab-case
- numbered sequence for ordered documents
- README.md is always the entry point
- SUMMARY.md is the navigation file

---

# Documentation Principles

1. Documentation First
2. Specification Driven
3. AI Native
4. Git Friendly
5. Reusable
6. Version Controlled

---

# Cross Reference Rules

Every document should include:

- Related Documents
- Previous Document
- Next Document
- Version

---

# Future Expansion

Additional domains must be added only through
an update to MASTER-STRUCTURE.md.

---

# Status

Architecture Freeze Pending Approval
