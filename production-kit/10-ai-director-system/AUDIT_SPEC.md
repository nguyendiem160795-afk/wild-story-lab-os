# AUDIT_SPEC.md

# AI Director Audit Specification

Version: 2.0 Vision
Status: Draft

## Purpose

Định nghĩa hệ thống Audit của AI Director nhằm ghi nhận, truy vết và kiểm chứng toàn bộ hoạt động của hệ thống trong suốt vòng đời sản xuất.

---

# Audit Objectives

- Truy vết mọi quyết định của AI Director
- Ghi nhận lịch sử Workflow
- Kiểm tra thay đổi dữ liệu
- Theo dõi hoạt động của AI Agent
- Hỗ trợ điều tra sự cố
- Đảm bảo tính minh bạch

---

# Audit Architecture

AI Director
↓
Audit Manager
├── Event Logger
├── Decision Logger
├── Workflow Logger
├── QA Logger
├── Security Logger
└── Archive Manager

---

# Audit Categories

## Decision Audit

Ghi nhận:

- Story Decisions
- Camera Decisions
- Character Decisions
- Prompt Decisions
- Release Decisions

---

## Workflow Audit

Theo dõi:

- Workflow Start
- Workflow End
- Node Execution
- Retry Events
- Failures

---

## QA Audit

Lưu trữ:

- Story QA
- Visual QA
- Prompt QA
- Continuity QA
- Release QA

---

## Security Audit

Ghi nhận:

- User Actions
- Permission Changes
- Configuration Updates
- Access Violations

---

# Audit Record Structure

Header

- audit_id
- timestamp
- actor
- component

Body

- action
- input
- output
- result

Footer

- status
- checksum

---

# Retention Policy

- Workflow Logs: 90 ngày
- QA Reports: 1 năm
- Release Logs: Không giới hạn
- Critical Security Events: Không giới hạn

---

# Outputs

- Audit Log
- Audit Report
- Compliance Report
- Traceability Report

Status: Draft
