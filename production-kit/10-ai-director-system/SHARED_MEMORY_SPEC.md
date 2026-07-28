# SHARED_MEMORY_SPEC.md

# Shared Memory Specification

Version: 2.0 Vision
Status: Draft

## Purpose

Định nghĩa kiến trúc Shared Memory dùng chung cho toàn bộ AI Agent trong Wild Story Lab OS nhằm đảm bảo các Agent luôn làm việc trên cùng một ngữ cảnh và dữ liệu nhất quán.

---

# Memory Architecture

AI Director
    │
    ├── Global Memory
    ├── Working Memory
    ├── Episodic Memory
    ├── Semantic Memory
    ├── Cache Layer
    └── Archive Layer

---

# Memory Types

## Global Memory

Purpose

Lưu trữ thông tin dùng chung cho toàn bộ hệ thống.

Examples

- Project Metadata
- Story Universe
- Character Registry
- World Rules
- Global Policies

---

## Working Memory

Purpose

Lưu trạng thái của phiên làm việc hiện tại.

Examples

- Active Story
- Active Scene
- Active Shot
- Current Prompt
- Current QA

Lifecycle

Session-based

---

## Episodic Memory

Purpose

Lưu lịch sử các lần chạy.

Contents

- Previous Decisions
- Retry History
- QA History
- Release History

---

## Semantic Memory

Purpose

Lưu tri thức lâu dài.

Examples

- Prompt Patterns
- Cinematic Rules
- Director Policies
- Best Practices

---

## Cache Layer

Purpose

Tăng tốc truy xuất dữ liệu.

Stores

- Recent Stories
- Character Cache
- Prompt Cache
- QA Cache

---

## Archive Layer

Purpose

Lưu trữ dữ liệu lịch sử.

Retention

- Releases
- Production Packages
- QA Reports
- Decision Logs

---

# Synchronization Rules

- AI Director là nguồn đồng bộ duy nhất.
- Mọi Agent đọc từ Shared Memory.
- Chỉ AI Director được ghi vào Global Memory.
- Working Memory được làm mới sau mỗi Project.

---

# Memory Lifecycle

Create
↓
Load
↓
Read
↓
Update
↓
Validate
↓
Archive

---

# Security Rules

- Character DNA chỉ đọc.
- Story Goal không được sửa.
- Release Data chỉ đọc sau khi phát hành.
- Mọi thay đổi phải được ghi log.

---

# Outputs

- Shared Context
- Memory Snapshot
- Synchronization Report
- Memory Audit Log

Status: Draft
