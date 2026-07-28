# MULTI_AGENT_COORDINATION.md

# Multi-Agent Coordination Specification

Version: 2.0 Vision
Status: Draft

## Purpose

Định nghĩa cơ chế phối hợp giữa các AI Agent trong Wild Story Lab OS dưới sự điều phối của AI Director.

---

# Architecture

                AI Director
                     │
 ┌──────────┬─────────┼─────────┬──────────┐
 │          │         │         │          │
Story   Character   Camera   Prompt      QA
Agent     Agent      Agent     Agent     Agent
                     │
               Release Agent

---

# Agent Responsibilities

## Story Agent
- Story Analysis
- Story Beats
- Hook
- Conflict
- Ending

Outputs
- Story Blueprint

---

## Character Agent

Responsibilities

- Character DNA
- Acting
- Emotion
- Dialogue

Outputs

- Character Plan

---

## Camera Agent

Responsibilities

- Camera
- Lens
- Lighting
- Composition
- Motion

Outputs

- Cinematic Plan

---

## Prompt Agent

Responsibilities

- Prompt Compose
- Prompt Optimize
- Platform Adapter

Outputs

- Prompt Package

---

## QA Agent

Responsibilities

- Story QA
- Visual QA
- Prompt QA
- Continuity QA

Outputs

- QA Report

---

## Release Agent

Responsibilities

- Package Build
- Manifest
- Release Validation

Outputs

- Release Package

---

# Coordination Workflow

Story Agent
↓
Character Agent
↓
Camera Agent
↓
Prompt Agent
↓
QA Agent
↓
Release Agent

AI Director giám sát toàn bộ quá trình.

---

# Communication Rules

- Agent chỉ giao tiếp qua dữ liệu chuẩn.
- Không sửa dữ liệu của Agent khác.
- Mọi thay đổi phải được AI Director phê duyệt.
- QA Agent có quyền yêu cầu Retry.
- Release Agent chỉ hoạt động sau khi QA PASS.

---

# Failure Recovery

Nếu một Agent thất bại:

Detect Failure
↓
Retry
↓
Escalate to Director
↓
Continue Workflow

Maximum Retry: 3

---

# Outputs

- Agent Logs
- Decision Logs
- QA Reports
- Production Package
- Release Package

Status: Draft
