# GRAPH_VALIDATION_SPEC.md

# AI Director Graph Validation Specification

Version: 2.0 Vision
Status: Draft

## Purpose

Graph Validation chịu trách nhiệm kiểm tra tính hợp lệ của Dependency Graph trước khi Execution Engine bắt đầu thực thi. Mục tiêu là đảm bảo toàn bộ Node và Edge đều đúng, không tồn tại vòng lặp, không thiếu phụ thuộc và thứ tự thực thi luôn chính xác.

---

# Validation Pipeline

Load Graph
↓
Validate Nodes
↓
Validate Edges
↓
Detect Cycles
↓
Check Reachability
↓
Validate Critical Path
↓
Calculate Health Score
↓
Generate Report
↓
Approval Decision

---

# Node Validation

## Rules

- Node ID phải duy nhất.
- Node Type phải hợp lệ.
- Node Metadata đầy đủ.
- Node Status hợp lệ.
- Node phải thuộc một Project.

Nếu vi phạm:
- Reject Graph

---

# Edge Validation

## Rules

- Source Node tồn tại.
- Target Node tồn tại.
- Edge Type hợp lệ.
- Không có Edge trùng lặp.
- Không tạo Self Loop.

Nếu vi phạm:
- Reject Graph

---

# Cycle Detection

Các vòng lặp không được phép:

Story → Scene → Story

Prompt → QA → Prompt

Release → QA → Release

Nếu phát hiện:
- Graph Status = INVALID

---

# Reachability Analysis

Kiểm tra:

- Mọi Node đều có đường đi từ Project Node.
- Release Node phải luôn reachable.
- Không tồn tại Orphan Node.

---

# Critical Path Validation

Critical Path chuẩn:

Project
↓
Story
↓
Scene
↓
Shot
↓
Prompt
↓
QA
↓
Production
↓
Release

Không được phép bỏ qua bất kỳ bước nào.

---

# Graph Health Score

Điểm đánh giá:

- Node Integrity: 25%
- Edge Integrity: 20%
- Cycle Detection: 20%
- Reachability: 15%
- Critical Path: 20%

Health Score ≥ 95

Status:
PASS

---

# Auto Repair Strategy

Nếu lỗi có thể sửa:

1. Remove Duplicate Edge
2. Remove Orphan Node
3. Rebuild Missing Edge
4. Recalculate Execution Order
5. Revalidate Graph

Maximum Auto Repair Attempts: 3

---

# Outputs

- Graph Validation Report
- Health Score
- Critical Path Report
- Repair Report
- Approval Status

Status: Draft
