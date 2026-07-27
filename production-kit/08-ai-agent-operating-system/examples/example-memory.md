# Example Memory

> Module 08 — AI Agent Operating System

Version: **1.0.0**

---

# Memory Metadata

| Field | Value |
|-------|-------|
| Memory ID | MEM-STORY-SESSION |
| Title | Story Planning Session Context |
| Version | 1.0.0 |
| Status | Production |
| Owner | Wild Story Lab |
| Memory Type | Session |
| Classification | Internal |

---

# Purpose

Provide temporary execution context that enables AI agents to maintain continuity during a single story production workflow.

---

# Memory Summary

Stores the current production request, workflow state, user preferences, and intermediate outputs for the active session.

---

# Memory Content

## Session Context

- Topic: Mochi learns teamwork
- Audience: Children (3–8 years)
- Duration: 60 seconds
- Style: Pixar 3D animation

## Workflow State

- Story outline generated
- Prompt package completed
- Knowledge retrieved
- Waiting for QA validation

## Retrieval Policy

- Available only during the active workflow session.
- Automatically discarded after workflow completion unless promoted to project memory.

---

# Related Assets

- AGT-STORY-PLANNER
- WF-STORY-PIPELINE
- PRM-STORY-PLAN
- KNW-STORY-RULES

---

# Access Control

| Role | Permission |
|------|------------|
| Workflow Engine | Read / Write |
| AI Agents | Read |
| QA Agent | Read |
| Repository | Archive |

---

# Validation Checklist

- [x] Metadata complete
- [x] Session scope defined
- [x] Retention policy documented
- [x] Related assets linked
- [x] Access control defined

---

# Change Log

| Version | Date | Description |
|---------|------|-------------|
|1.0.0|YYYY-MM-DD|Initial example|
