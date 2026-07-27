# Example Prompt

> Module 08 — AI Agent Operating System

Version: **1.0.0**

---

# Prompt Metadata

| Field | Value |
|-------|-------|
| Prompt ID | PRM-STORY-PLAN |
| Name | Story Planning Prompt |
| Version | 1.0.0 |
| Status | Production |
| Owner | Wild Story Lab |
| Category | Story Planning |

---

# Purpose

Generate a structured, production-ready story outline from a user request.

---

# Supported Models

- GPT-5.x
- Gemini
- Claude

---

# Input Variables

| Variable | Type | Description |
|----------|------|-------------|
| topic | String | Main story topic |
| audience | String | Target audience |
| duration | Number | Desired duration in seconds |
| style | String | Narrative style |

---

# Prompt

```text
You are an expert Story Planner for Wild Story Lab.

Your task is to transform the user's request into a production-ready story outline.

Requirements:
- Create a compelling hook.
- Divide the story into logical scenes.
- Include conflict, escalation, climax, and resolution.
- Keep the story suitable for the target audience.
- Return the output using Markdown.
```

---

# Expected Output

```text
# Story Outline

Scene 1 — Hook
Scene 2 — Introduction
Scene 3 — Conflict
Scene 4 — Escalation
Scene 5 — Climax
Scene 6 — Resolution
```

---

# Validation Rules

- Required variables provided
- Output contains all required scenes
- Markdown formatting valid
- Story structure complete

---

# Related Assets

- AGT-STORY-PLANNER
- WF-STORY-PIPELINE
- KNW-STORY-RULES

---

# Example Usage

Input:

```text
Topic: Mochi learns teamwork
Audience: Kids
Duration: 60 seconds
Style: Pixar
```

Output:

```text
A six-scene storyboard with a clear hook, escalating challenge, emotional climax, and positive ending.
```

---

# Change Log

| Version | Date | Description |
|---------|------|-------------|
|1.0.0|YYYY-MM-DD|Initial example|
