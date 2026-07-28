# DECISION_ENGINE_SPEC.md

# AI Director Decision Engine Specification

Version: 1.0.0
Status: Stable

## Purpose

Decision Engine là lõi ra quyết định của AI Director System. Thành phần này chịu trách nhiệm đánh giá dữ liệu đầu vào, lựa chọn phương án đạo diễn tối ưu và đảm bảo mọi quyết định đều tuân thủ Story Goal, Character DNA và Production Rules.

---

# Objectives

- Phân tích Story Blueprint
- Đánh giá Scene Context
- Lựa chọn Camera Strategy
- Điều phối Character
- Sinh Prompt Strategy
- Kiểm soát Quality Gates
- Quyết định Release

---

# Decision Pipeline

Story Input
↓
Context Analysis
↓
Rule Evaluation
↓
Priority Resolution
↓
Director Decision
↓
Quality Validation
↓
Production Output

---

# Decision Layers

## Layer 1 — Story

Priority:
1. Story Goal
2. Story Beats
3. Emotional Arc
4. Conflict
5. Ending

---

## Layer 2 — Character

Priority:
1. Character DNA
2. Personality
3. Emotion
4. Acting
5. Dialogue

---

## Layer 3 — Cinematic

Priority:
1. Camera
2. Lens
3. Lighting
4. Composition
5. Motion
6. FX

---

## Layer 4 — Prompt

Priority:
1. Story Accuracy
2. Character Consistency
3. Platform Compatibility
4. Prompt Clarity

---

# Conflict Resolution Rules

If multiple decisions conflict:

1. Preserve Story Goal
2. Preserve Character DNA
3. Prefer Visual Clarity
4. Optimize for Target Platform
5. Reject contradictory instructions

---

# Fallback Strategy

Level 1
- Retry current decision

Level 2
- Rebuild prompt section

Level 3
- Re-plan scene

Level 4
- Escalate to manual review

Maximum automatic retries: 3

---

# Decision Outputs

- Story Decision
- Camera Decision
- Character Decision
- Prompt Decision
- QA Decision
- Release Decision

---

# Validation Rules

- Story Goal must remain unchanged
- Character DNA is immutable
- Quality Gate must PASS
- Platform Adapter must succeed
- Release Validator must approve

---

# Status

Approved
