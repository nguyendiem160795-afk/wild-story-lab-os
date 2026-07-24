# SKILL SELECTION RULES

**Module:** 07 – Playbook OS

**Document:** SKILL-SELECTION-RULES

**Version:** 1.0.0

**Status:** Stable

**Owner:** Wild Story Lab OS

---

# Purpose

SKILL-SELECTION-RULES defines how AI Directors determine the most appropriate operational Skills for a production request.

Rather than selecting Playbooks directly, AI first analyzes the user's intent, identifies the required capabilities, determines the optimal execution pipeline, and then selects the corresponding Skills.

This document standardizes decision-making across all AI systems operating within Wild Story Lab.

---

# Philosophy

Playbook selection is never random.

Every Skill must be selected based on operational reasoning.

AI should always think before executing.

The decision process follows:

User Goal

↓

Intent

↓

Capability

↓

Pipeline

↓

Skill

↓

Execution

---

# Decision Hierarchy

AI must evaluate requests in the following order.

## Level 1 — Intent

Determine what the user wants.

Examples:

- Learn English
- Create Entertainment
- Produce Sleep Music
- Build Character
- Improve SEO

---

## Level 2 — Content Type

Determine the production category.

Examples:

- Educational
- Entertainment
- Music
- Marketing
- Branding

---

## Level 3 — Audience

Determine the target audience.

Examples:

- Toddlers
- Preschool
- Children
- Teenagers
- Adults

---

## Level 4 — Production Goal

Determine the expected deliverable.

Examples:

- YouTube Short
- Long-form Video
- Thumbnail
- Story
- Prompt Package

---

## Level 5 — Capability

Determine the operational capability required.

Examples:

- Story Engineering
- Character Design
- Prompt Engineering
- Video Production
- SEO

---

## Level 6 — Skill Selection

Locate the required Skill through MASTER-SKILL-INDEX.

---

## Level 7 — Workflow Routing

Navigate using SKILL-GRAPH.

---

## Level 8 — Execution

Execute the selected Playbooks.

---

# Standard Decision Flow

```text
User Request
      │
      ▼
Intent Detection
      │
      ▼
Content Classification
      │
      ▼
Audience Analysis
      │
      ▼
Production Goal
      │
      ▼
Capability Selection
      │
      ▼
Skill Selection
      │
      ▼
Workflow Routing
      │
      ▼
Playbook Execution
      │
      ▼
Validation
      │
      ▼
Output
```

---

# Pipeline Selection

Example:

Educational Video

↓

Education Pipeline

↓

PB-001

↓

PB-011

↓

PB-021

↓

PB-041

↓

PB-051

---

Entertainment Video

↓

Entertainment Pipeline

↓

PB-101

↓

PB-111

↓

PB-121

---

Sleep Music

↓

Music Pipeline

↓

PB-201

↓

PB-211

↓

PB-221

---

# Decision Rules

When multiple Skills are available:

1. Prefer approved Skills.
2. Prefer reusable Skills.
3. Prefer the shortest valid pipeline.
4. Avoid duplicate execution.
5. Reuse validated outputs whenever possible.

---

# Conflict Resolution

If two Skills satisfy the same capability:

- Choose the latest approved version.
- Prefer higher-quality outputs.
- Prefer lower operational cost.
- Prefer officially recommended Playbooks.

---

# Failure Handling

If no suitable Skill exists:

1. Report missing capability.
2. Recommend creating a new Playbook.
3. Continue only if an approved fallback exists.

---

# Relationship with Other Documents

README

↓

INDEX

↓

MASTER-SKILL-INDEX

↓

SKILL-SELECTION-RULES

↓

SKILL-GRAPH

↓

SKILL-TEMPLATE

↓

PLAYBOOK

---

# Future Expansion

Future versions may support:

- AI confidence scoring
- Cost-aware routing
- Multi-agent planning
- Dynamic pipeline optimization
- Machine-readable decision rules

---

# Maintenance

Update this document whenever:

- New capability domains are introduced.
- Pipeline selection rules change.
- AI reasoning improves.
- Operational policies evolve.

---

# Document Status

Current Version: 1.0.0

Status: Stable

Maintained By: Wild Story Lab OS

Next Review: Defined in ROADMAP.md

---

End of Document