# WORKFLOW_EXECUTOR_SPEC.md

# AI Director Workflow Executor Specification

Version: 2.0 Vision
Status: Draft

## Purpose

Workflow Executor là thành phần chịu trách nhiệm thực thi từng Workflow trong AI Director System theo đúng thứ tự, điều kiện và trạng thái đã được AI Director phê duyệt.

---

# Architecture

AI Director
↓
Workflow Executor
├── Workflow Loader
├── Node Scheduler
├── Branch Engine
├── Event Dispatcher
├── State Manager
├── Retry Manager
└── Execution Logger

---

# Workflow Lifecycle

Load Workflow
↓
Validate Workflow
↓
Build Execution Graph
↓
Resolve Dependencies
↓
Execute Nodes
↓
Evaluate Conditions
↓
Update State
↓
Finish Workflow
↓
Archive Execution

---

# Workflow Components

## Workflow Definition

Mỗi Workflow gồm:

- Workflow ID
- Name
- Version
- Input
- Output
- Node List
- Dependency Graph
- Success Criteria

---

## Node Types

### Start Node
- Khởi tạo Workflow

### Action Node
- Thực thi một tác vụ

### Decision Node
- Đánh giá điều kiện

### Parallel Node
- Chạy nhiều nhánh đồng thời

### Merge Node
- Hợp nhất các nhánh

### End Node
- Kết thúc Workflow

---

# Execution Rules

- Start Node luôn chạy đầu tiên.
- Mỗi Node chỉ thực thi khi Dependencies đã hoàn thành.
- Decision Node quyết định nhánh tiếp theo.
- Parallel Node chỉ hợp nhất khi tất cả nhánh hoàn tất.
- End Node chỉ chạy sau khi mọi Node PASS.

---

# State Management

Workflow States

- CREATED
- READY
- RUNNING
- WAITING
- RETRYING
- FAILED
- COMPLETED
- ARCHIVED

---

# Event Handling

Supported Events

- Workflow Started
- Node Started
- Node Completed
- Node Failed
- Retry Triggered
- Workflow Completed

---

# Retry Strategy

Retry Level 1
- Re-execute Node

Retry Level 2
- Rebuild Node Context

Retry Level 3
- Restart Workflow Section

Maximum Retry: 3

---

# Monitoring Metrics

- Workflow Duration
- Active Nodes
- Completed Nodes
- Failed Nodes
- Retry Count
- Success Rate

---

# Outputs

- Execution Graph
- Workflow Log
- State History
- Retry Report
- Audit Log

Status: Draft
