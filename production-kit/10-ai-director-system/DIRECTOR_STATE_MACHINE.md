# DIRECTOR_STATE_MACHINE.md

# AI Director State Machine Specification

Version: 1.0.0
Status: Stable

## Purpose

Định nghĩa toàn bộ vòng đời hoạt động của AI Director dưới dạng State Machine nhằm đảm bảo mọi quy trình đều có trạng thái rõ ràng, có thể theo dõi, phục hồi và mở rộng.

---

# State Overview

INIT
↓
LOAD_PROJECT
↓
LOAD_STORY
↓
LOAD_CHARACTER
↓
PLAN_STORY
↓
PLAN_SCENES
↓
PLAN_SHOTS
↓
DIRECT_CAMERA
↓
DIRECT_CHARACTERS
↓
BUILD_PROMPTS
↓
VALIDATE_PROMPTS
↓
QUALITY_GATE
↓
PRODUCTION_PLAN
↓
PACKAGE_BUILD
↓
RELEASE_VALIDATION
↓
RELEASED

---

# State Definitions

## INIT
Entry:
- Khởi tạo AI Director
Exit:
- Chuyển sang LOAD_PROJECT

## LOAD_PROJECT
Entry:
- Đọc metadata dự án
Exit:
- Kiểm tra dữ liệu đầu vào

## LOAD_STORY
Entry:
- Nạp Story Blueprint
Validation:
- Story Goal
- Story Beats

## LOAD_CHARACTER
Entry:
- Nạp Character DNA
Validation:
- Character Bible
- Animation Rules

## PLAN_STORY
Outputs:
- Story Structure
- Scene Count

## PLAN_SCENES
Outputs:
- Scene Blueprint
- Timeline

## PLAN_SHOTS
Outputs:
- Shot List
- Camera Plan

## DIRECT_CAMERA
Outputs:
- Camera Decisions
- Lens
- Lighting

## DIRECT_CHARACTERS
Outputs:
- Blocking
- Acting
- Dialogue

## BUILD_PROMPTS
Outputs:
- Master Prompt
- Scene Prompt
- Platform Prompt

## VALIDATE_PROMPTS
Checks:
- Structure
- Consistency
- Platform Compatibility

## QUALITY_GATE
Checks:
- Story QA
- Visual QA
- Prompt QA
- Continuity QA

## PRODUCTION_PLAN
Outputs:
- Render Queue
- Asset Checklist
- Manifest

## PACKAGE_BUILD
Outputs:
- Production Package

## RELEASE_VALIDATION
Checks:
- Manifest
- Version
- QA
- Release Notes

## RELEASED
Final State

---

# Error States

ERROR_STORY

ERROR_CHARACTER

ERROR_PROMPT

ERROR_QA

ERROR_RELEASE

---

# Recovery Flow

Error
↓
Detect
↓
Retry
↓
Revalidate
↓
Continue

Maximum Retry: 3

---

# Terminal States

SUCCESS

FAILED

CANCELLED

---

Status: Approved
