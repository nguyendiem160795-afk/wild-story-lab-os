# 03 - Core Systems

# AI Director Core Systems

> Wild Story Lab OS / Production Kit

---

# Purpose

Tài liệu này mô tả các hệ thống lõi (Core Systems) tạo nên AI Director System. Đây là những thành phần chịu trách nhiệm phân tích, lập kế hoạch, điều phối và kiểm soát toàn bộ quy trình sản xuất.

---

# Core Architecture

```text
                AI Director
                     │
 ┌───────────────────┼───────────────────┐
 │                   │                   │
Story          Decision Engine     Workflow Engine
 │                   │                   │
 ├──────────────┬────┴────┬──────────────┤
 │              │         │              │
Character   Prompt     Quality     Production
Intelligence Intelligence Intelligence Intelligence
```

---

# Story Intelligence

## Responsibilities

- Story Analysis
- Story Goal
- Story Structure
- Story Beats
- Emotional Arc
- Scene Breakdown

### Inputs

- Story Blueprint
- World Rules
- Character Registry

### Outputs

- Production Story Plan

---

# Character Intelligence

## Responsibilities

- Character DNA Validation
- Acting Direction
- Emotion Planning
- Character Consistency
- Dialogue Planning

### Outputs

- Character Direction Plan

---

# Cinematic Intelligence

## Responsibilities

- Camera Planning
- Lens Selection
- Lighting Design
- Composition
- Camera Motion

### Outputs

- Cinematic Blueprint

---

# Prompt Intelligence

## Responsibilities

- Master Prompt
- Scene Prompt
- Platform Prompt
- Prompt Optimization
- Prompt Validation

### Supported Platforms

- Google Flow
- Veo
- Runway
- Sora
- Luma

### Outputs

- Prompt Package

---

# Decision Engine

## Responsibilities

- Evaluate Options
- Apply Director Policies
- Resolve Conflicts
- Select Production Strategy

### Outputs

- Director Decisions

---

# Workflow Engine

## Responsibilities

- Workflow Planning
- Task Scheduling
- Dependency Resolution
- Agent Coordination
- Progress Tracking

### Outputs

- Execution Workflow

---

# Quality Intelligence

## Responsibilities

- Story QA
- Visual QA
- Prompt QA
- Continuity QA
- Release QA

### Outputs

- QA Reports
- Quality Score

---

# Production Intelligence

## Responsibilities

- Production Planning
- Asset Management
- Package Generation
- Release Preparation

### Outputs

- Production Package
- Release Package

---

# System Interaction

```text
Story Intelligence
        ↓
Character Intelligence
        ↓
Cinematic Intelligence
        ↓
Prompt Intelligence
        ↓
Decision Engine
        ↓
Workflow Engine
        ↓
Quality Intelligence
        ↓
Production Intelligence
```

---

# Design Principles

- Story First
- Quality by Default
- Modular Components
- Reusable Architecture
- Multi-Agent Collaboration
- Documentation Driven

---

# Related Documents

- DIRECTOR_SPEC.md
- DECISION_ENGINE_SPEC.md
- WORKFLOW_EXECUTOR_SPEC.md
- EXECUTION_ENGINE_SPEC.md
- QUALITY_GATE_SPEC.md

---

# Next Document

Tiếp tục đọc:

**docs/04-workflow.md**

---

Version: 1.0.0

Status: Complete
