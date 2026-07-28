# CONTEXT_MANAGEMENT_SPEC.md

# Context Management Specification

Version: 2.0 Vision
Status: Draft

## Purpose

Định nghĩa hệ thống quản lý Context của AI Director và toàn bộ AI Agent trong Wild Story Lab OS nhằm duy trì ngữ cảnh nhất quán trong suốt vòng đời dự án.

---

# Context Architecture

User Request
↓
Project Context
↓
Story Context
↓
Scene Context
↓
Shot Context
↓
Prompt Context
↓
QA Context
↓
Release Context

---

# Context Types

## Global Context

Phạm vi:
- Toàn bộ Project

Bao gồm:
- Project Metadata
- World Rules
- Character Registry
- Director Policies

---

## Story Context

Bao gồm:

- Story Goal
- Story Beats
- Emotional Arc
- Conflict
- Ending

---

## Scene Context

Bao gồm:

- Scene ID
- Location
- Characters
- Timeline
- Camera Plan

---

## Shot Context

Bao gồm:

- Shot ID
- Camera
- Lens
- Motion
- Lighting
- Composition

---

## Prompt Context

Bao gồm:

- Master Prompt
- Scene Prompt
- Platform Prompt
- Prompt History

---

## QA Context

Bao gồm:

- Story QA
- Visual QA
- Prompt QA
- Continuity QA
- Release QA

---

# Context Lifecycle

Create
↓
Load
↓
Merge
↓
Validate
↓
Update
↓
Archive

---

# Context Prioritization

Priority 1
Story Context

Priority 2
Character Context

Priority 3
Scene Context

Priority 4
Shot Context

Priority 5
Prompt Context

Priority 6
QA Context

---

# Context Recovery

If Context Lost

↓

Reload Project

↓

Reload Story

↓

Reload Character

↓

Reload Scene

↓

Continue

---

# Synchronization Rules

- AI Director quản lý Context chính.
- Agent chỉ đọc Context đã được phê duyệt.
- Mọi cập nhật đều ghi vào Context Log.
- Không ghi đè Context khi chưa xác thực.

---

# Outputs

- Context Snapshot
- Context Log
- Synchronization Report
- Recovery Report

Status: Draft
