# DIRECTOR_SEQUENCE.md

# AI Director Sequence Specification

Version: 1.0.0
Status: Stable

## Purpose

Định nghĩa luồng thực thi (Execution Sequence) của AI Director System từ lúc nhận yêu cầu đến khi phát hành Production Package.

---

# High-Level Sequence

User Request
    ↓
AI Agent OS
    ↓
Story Engine
    ↓
Character System
    ↓
AI Director
    ↓
Prompt Engine
    ↓
QA Engine
    ↓
Production Planner
    ↓
Release Manager
    ↓
Production Package

---

# Detailed Execution Flow

## Phase 1 — Story Initialization

1. Receive Story Request
2. Load Story Blueprint
3. Validate Story Goal
4. Load Story Beats
5. Build Story Context

Output:
- Story Context

---

## Phase 2 — Character Initialization

1. Load Character Bible
2. Load Character DNA
3. Validate Character Consistency
4. Load Animation Rules

Output:
- Character Context

---

## Phase 3 — Directing

Sequence

Story Analysis
↓
Scene Planning
↓
Shot Planning
↓
Camera Direction
↓
Character Direction
↓
Prompt Composition

Output:
- Director Decisions

---

## Phase 4 — Prompt Pipeline

Compose Prompt
↓
Validate Prompt
↓
Optimize Prompt
↓
Platform Adapter

Output:
- Platform Prompt

---

## Phase 5 — QA Pipeline

Story QA
↓
Visual QA
↓
Prompt QA
↓
Continuity QA
↓
Release QA

Output:
- QA Report

---

## Phase 6 — Production

Generate Production Manifest
↓
Build Render Queue
↓
Package Assets
↓
Export Production Package

---

## Phase 7 — Release

Validate Release
↓
Generate Release Notes
↓
Publish Release Package

---

# Sequence Rules

- Story luôn thực thi trước.
- Character luôn được khóa trước Prompt.
- QA bắt buộc trước Production.
- Release chỉ diễn ra sau khi toàn bộ QA PASS.

---

# Outputs

- Story Context
- Character Context
- Prompt Package
- QA Reports
- Production Package
- Release Package

Status: Approved
