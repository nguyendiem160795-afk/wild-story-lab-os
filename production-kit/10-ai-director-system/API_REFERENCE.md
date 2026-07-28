# API_REFERENCE.md

# AI Director System API Reference

Version: 1.0.0
Status: Stable

## Purpose

Tài liệu này mô tả chuẩn giao tiếp (Interface Contract) giữa Module 10 AI Director System với các module khác trong Wild Story Lab OS và các nền tảng AI Video.

---

# System Interfaces

Module 05 Story Engine
        │
        ▼
Module 06 Character System
        │
        ▼
Module 08 AI Agent OS
        │
        ▼
Module 09 Production Components
        │
        ▼
Module 10 AI Director

---

# Input Contracts

## Story Interface

Input:
- Story Blueprint
- Story Beats
- World Rules
- Episode Metadata

Output:
- Story Analysis
- Scene Blueprint

---

## Character Interface

Input:
- Character Bible
- Character DNA
- Pose Library
- Animation Rules

Output:
- Character Blocking
- Acting Plan
- Facial Plan

---

## Production Interface

Input:
- Camera Library
- Lens Library
- Lighting Library
- FX Library
- Prompt Components

Output:
- Cinematic Plan
- Prompt Package

---

# Output Contracts

## Prompt Package

Contains:
- Master Prompt
- Scene Prompts
- Platform Prompts

---

## Production Package

Contains:
- Scene Blueprint
- Shot List
- Asset Manifest
- Render Queue
- QA Reports

---

## Release Package

Contains:
- Release Manifest
- Version Metadata
- Documentation
- Production Bundle

---

# Platform Targets

Supported:

- Google Flow
- Veo
- Runway
- Sora
- Luma

---

# Validation Rules

✓ Required fields must exist

✓ Character DNA immutable

✓ Story Goal preserved

✓ Prompt QA PASS

✓ Platform compatibility PASS

---

# Error Codes

API-001 Missing Story Blueprint

API-002 Missing Character DNA

API-003 Invalid Prompt Package

API-004 QA Failed

API-005 Release Validation Failed

---

# Version

API Version: 1.0.0

Status: Approved
