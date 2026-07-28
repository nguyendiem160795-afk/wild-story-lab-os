# QUALITY_GATE_SPEC.md

# AI Director Quality Gate Specification

Version: 1.0.0
Status: Stable

## Purpose

Đặc tả toàn bộ hệ thống Quality Gates của AI Director System nhằm đảm bảo mọi Story, Prompt và Production Package đều đạt chuẩn trước khi phát hành.

---

# Quality Gate Architecture

Story QA
↓
Visual QA
↓
Prompt QA
↓
Continuity QA
↓
Production QA
↓
Release QA

Mỗi Gate phải PASS trước khi chuyển sang Gate tiếp theo.

---

# Gate 01 — Story QA

## Validation

- Story Goal rõ ràng
- Hook hấp dẫn
- Story Beats đầy đủ
- Conflict tăng dần
- Climax hợp lý
- Ending hoàn chỉnh

Minimum Score

90 / 100

PASS
↓

Visual QA

---

# Gate 02 — Visual QA

Validation

- Character DNA
- Camera
- Lens
- Lighting
- Composition
- Motion
- FX

Minimum Score

90 / 100

---

# Gate 03 — Prompt QA

Validation

- Prompt Structure
- Subject
- Action
- Environment
- Camera
- Lighting
- Style
- Platform Compatibility

Minimum Score

90 / 100

---

# Gate 04 — Continuity QA

Validation

- Character Continuity
- Costume
- Props
- Timeline
- Environment
- Camera Direction

Minimum Score

95 / 100

---

# Gate 05 — Production QA

Validation

- Asset Manifest
- Scene Blueprint
- Shot List
- Prompt Package
- Render Queue

Minimum Score

95 / 100

---

# Gate 06 — Release QA

Validation

- README
- CHANGELOG
- Manifest
- Release Notes
- Version
- QA Reports

Result

APPROVED

or

REJECTED

---

# Retry Policy

If Gate FAILS

↓

Classify Error

↓

Retry Level 1

↓

Retry Level 2

↓

Retry Level 3

↓

Manual Review

Maximum Retry

3

---

# Severity Levels

Critical
Release blocked

Major
Retry required

Minor
Warning only

Info
No action required

---

# Outputs

- Quality Gate Report
- QA Summary
- Retry Report
- Approval Decision

Status: Approved
