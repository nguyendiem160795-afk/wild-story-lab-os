# DIRECTOR_WORKFLOW_SPEC.md

# AI Director Workflow Specification

Version: 1.0.0
Status: Stable

## Purpose

Tài liệu này đặc tả toàn bộ Workflow của AI Director System, bao gồm State Machine, Decision Logic, Quality Gates và Release Gates.

---

# Workflow Overview

Story Request
↓
Story Analysis
↓
Scene Planning
↓
Shot Planning
↓
Cinematic Directing
↓
Character Directing
↓
Prompt Composition
↓
Prompt Validation
↓
Prompt Optimization
↓
Platform Adaptation
↓
Quality Intelligence
↓
Production Planning
↓
Export
↓
Release Validation
↓
Stable Release

---

# Director State Machine

INIT
↓
LOAD_STORY
↓
PLAN_SCENES
↓
DIRECT_SCENES
↓
GENERATE_PROMPTS
↓
VALIDATE_PROMPTS
↓
QUALITY_CHECK
↓
PACKAGE_BUILD
↓
RELEASE_READY
↓
FINISHED

---

# Decision Gates

## Gate 1 — Story Validation
Requirements:
- Story Goal defined
- Story Beats complete
- Hook available

Result:
PASS / FAIL

---

## Gate 2 — Character Validation

Requirements:
- Character DNA loaded
- Character Bible valid
- Animation Rules available

Result:
PASS / FAIL

---

## Gate 3 — Prompt Validation

Requirements:
- Prompt complete
- No conflicting instructions
- Platform compatible

Result:
PASS / FAIL

---

## Gate 4 — Quality Gate

Required Scores:

- Story QA ≥ 90
- Visual QA ≥ 90
- Prompt QA ≥ 90
- Continuity QA ≥ 95

Result:
PASS / RETRY

---

## Gate 5 — Release Gate

Requirements:
- Production Package complete
- Manifest valid
- Release Validator PASS

Result:
APPROVED / REJECTED

---

# Retry Strategy

If any gate fails:

Detect Error
↓
Classify Error
↓
Select Retry Level
↓
Regenerate Output
↓
Re-Validate
↓
Continue Workflow

Maximum Retry: 3

---

# Outputs

- Workflow Report
- Decision Log
- QA Report
- Production Package
- Release Package

Status: Approved
