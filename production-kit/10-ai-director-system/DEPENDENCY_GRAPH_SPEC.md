# DEPENDENCY_GRAPH_SPEC.md

# AI Director Dependency Graph Specification

Version: 2.0 Vision
Status: Draft

## Purpose

Định nghĩa hệ thống Dependency Graph giúp AI Director xác định thứ tự thực thi của Story, Scene, Shot, Prompt, QA và Release dựa trên quan hệ phụ thuộc.

---

# Architecture

Project
↓
Dependency Graph
├── Node Registry
├── Edge Registry
├── Dependency Resolver
├── Cycle Detector
├── Graph Optimizer
└── Execution Planner

---

# Node Types

## Project Node
- Đại diện cho toàn bộ Project

## Story Node
- Story Blueprint
- Story Beats

## Scene Node
- Scene Blueprint
- Scene Timeline

## Shot Node
- Camera Plan
- Shot Definition

## Prompt Node
- Master Prompt
- Platform Prompt

## QA Node
- Story QA
- Visual QA
- Prompt QA
- Continuity QA

## Release Node
- Production Package
- Release Package

---

# Edge Rules

Story → Scene

Scene → Shot

Shot → Prompt

Prompt → QA

QA → Production

Production → Release

Không được phép tạo cạnh ngược gây vòng lặp.

---

# Dependency Resolution

1. Register Nodes
2. Register Edges
3. Validate Graph
4. Detect Cycles
5. Topological Sort
6. Generate Execution Order

---

# Cycle Detection

Nếu phát hiện:

Scene → Prompt → Scene

hoặc

QA → Prompt → QA

Kết quả:

REJECT GRAPH

---

# Topological Sorting

Execution Order

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

---

# Critical Path

Đường đi quan trọng:

Story
↓

Scene
↓

Prompt
↓

QA
↓

Release

Đây là chuỗi không được phép gián đoạn.

---

# Validation Rules

- Node ID duy nhất.
- Edge hợp lệ.
- Không có Circular Dependency.
- Mọi Node phải kết nối với Project.
- Release Node luôn là Node cuối.

---

# Outputs

- Dependency Graph
- Execution Order
- Validation Report
- Critical Path Report

Status: Draft
