# Frequently Asked Questions (FAQ)

> Module 08 — AI Agent Operating System

Version: **0.1.0**

---

# Purpose

This document answers the most common questions about the AI Agent Operating System.

It serves as a quick reference for contributors, AI engineers, documentation writers, and repository maintainers.

---

# General Questions

## What is Module 08?

Module 08 defines the AI Agent Operating System that coordinates AI agents, workflows, knowledge, memory, documentation, and governance within the Wild Story Lab ecosystem.

---

## Why does this module exist?

Its goal is to transform AI from isolated prompt execution into a structured production platform with reusable standards and repeatable workflows.

---

## Is Module 08 source code?

No.

BUILD-001 focuses on engineering documentation.

Implementation artifacts such as schemas, runtimes, APIs, and automation are introduced in later builds.

---

# Architecture

## Why is documentation created first?

Documentation establishes architecture before implementation.

This reduces ambiguity and prevents inconsistent development.

---

## What is the Single Source of Truth?

The Git repository.

Every reusable production asset should exist in the repository and be version controlled.

---

## Why are standards separated into multiple documents?

Each document has one responsibility.

Smaller focused documents are easier to maintain, review, and reference.

---

# AI Agents

## What is an AI Agent?

An AI Agent is a specialized component responsible for performing a defined production task.

Examples include:

- Story Planner
- Prompt Engineer
- QA Reviewer
- Publishing Manager

---

## Can agents communicate directly?

The preferred model is collaboration through standardized workflows rather than tightly coupled agent-to-agent communication.

---

# Knowledge

## Where should project knowledge be stored?

Knowledge belongs in the Knowledge System rather than inside prompts.

Centralized knowledge improves consistency and reuse.

---

## Why avoid duplicated knowledge?

Duplicate information creates conflicting updates and increases maintenance effort.

---

# Workflows

## Why standardize workflows?

Standard workflows make execution predictable, automatable, and easier to validate.

---

## Should every workflow be documented?

Yes.

Every production workflow should describe:

- Inputs
- Outputs
- Dependencies
- Validation
- Error handling

---

# Documentation

## Why are there many documentation files?

Each document addresses a single engineering topic.

This improves navigation and long-term maintainability.

---

## When should documentation be updated?

Whenever implementation changes.

Documentation should evolve together with the repository.

---

# Versioning

## Which versioning system is used?

Semantic Versioning (SemVer):

MAJOR.MINOR.PATCH

---

## When is a major version required?

Major versions indicate breaking architectural or compatibility changes.

---

# Governance

## Who approves architectural changes?

Major architectural decisions should be approved according to the Governance policy.

---

## What is an Architecture Decision Record (ADR)?

An ADR permanently records the reasoning behind significant architectural decisions.

Historical ADRs should never be deleted.

---

# Repository

## What belongs in the repository?

Production assets including:

- Documentation
- Templates
- Schemas
- Examples
- Standards
- Configuration

Temporary files should not be committed.

---

# Future Development

## What comes after BUILD-001?

Future builds introduce:

- JSON Schemas
- Templates
- Runtime Components
- Knowledge System
- Memory Engine
- Workflow Engine
- Automation Services

---

# Related Documents

- README.md
- philosophy.md
- architecture-decisions.md
- governance.md
- versioning-policy.md

---

# Summary

This FAQ provides quick answers to the most common questions about the AI Agent Operating System and serves as an entry point for new contributors joining the Wild Story Lab project.
