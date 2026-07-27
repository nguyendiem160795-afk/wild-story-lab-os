# Example Agent

> Module 08 — AI Agent Operating System

Version: **1.0.0**

---

# Agent Metadata

| Field | Value |
|-------|-------|
| Agent ID | AGT-STORY-PLANNER |
| Name | Story Planner Agent |
| Version | 1.0.0 |
| Status | Production |
| Owner | Wild Story Lab |
| Category | Planning |

---

# Purpose

Generate structured story plans for production-ready AI video workflows.

---

# Responsibilities

- Analyze user requirements
- Select appropriate story structure
- Produce scene-by-scene outline
- Recommend supporting assets

---

# Capabilities

- Story Planning
- Outline Generation
- Narrative Structuring
- Production Planning

---

# Inputs

| Name | Type | Description |
|------|------|-------------|
| User Request | Text | Story requirements |
| Constraints | Object | Duration, style, audience |

---

# Outputs

| Name | Type | Description |
|------|------|-------------|
| Story Outline | Markdown | Multi-scene story plan |
| Asset List | Markdown | Required production assets |

---

# Dependencies

- Prompt: PRM-STORY-PLAN
- Workflow: WF-STORY-PIPELINE
- Knowledge: KNW-STORY-RULES

---

# Execution Flow

1. Validate request
2. Load story knowledge
3. Select story structure
4. Generate outline
5. Validate output
6. Return structured result

---

# Example Output

```text
Scene 1: Hook
Scene 2: Conflict
Scene 3: Escalation
Scene 4: Climax
Scene 5: Resolution
```

---

# Validation Checklist

- [x] Metadata complete
- [x] Dependencies defined
- [x] Outputs documented
- [x] Execution flow documented

---

# Change Log

| Version | Date | Description |
|---------|------|-------------|
|1.0.0|YYYY-MM-DD|Initial example|
