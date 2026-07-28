# DIRECTOR_DECISION_TREE.md

# AI Director Decision Tree

Version: 1.0.0
Status: Stable

## Purpose

Định nghĩa toàn bộ cây quyết định (Decision Tree) của AI Director System, mô tả cách hệ thống lựa chọn phương án tối ưu trong từng giai đoạn sản xuất.

---

# Global Decision Flow

Receive Story
↓
Analyze Context
↓
Evaluate Rules
↓
Select Best Strategy
↓
Validate
↓
Execute
↓
QA
↓
Release

---

# Story Decision Tree

Story Request
│
├── Story Goal Exists?
│      ├── YES → Continue
│      └── NO → Reject
│
├── Story Beats Complete?
│      ├── YES
│      └── NO → Retry
│
└── Emotional Arc Valid?
       ├── YES
       └── NO → Rebuild Story

---

# Character Decision Tree

Character Loaded?
│
├── YES
│
├── DNA Valid?
│      ├── YES
│      └── NO → Reject
│
└── Character Consistent?
       ├── YES
       └── NO → Retry

---

# Cinematic Decision Tree

Scene Ready?
│
├── Camera Selected?
├── Lens Selected?
├── Lighting Selected?
├── Composition Valid?
└── Motion Planned?

If any answer = NO
→ Retry Planning

---

# Prompt Decision Tree

Prompt Built?
│
├── Structure Valid?
├── Story Accurate?
├── Character Consistent?
├── Platform Compatible?
└── Prompt QA PASS?

If FAIL
→ Prompt Optimizer

---

# QA Decision Tree

Story QA PASS?
│
├── YES
│
├── Visual QA PASS?
│
├── Prompt QA PASS?
│
├── Continuity PASS?
│
└── Release QA PASS?

All PASS
→ Production

Otherwise
→ Retry Strategy

---

# Release Decision Tree

Package Complete?
│
├── Manifest Valid?
├── Version Valid?
├── Documentation Complete?
├── QA Reports Complete?
└── Deployment Ready?

If YES
→ RELEASE

If NO
→ Reject Release

---

# Priority Rules

1. Story
2. Character
3. Cinematic
4. Prompt
5. QA
6. Release

---

# Outputs

- Decision Log
- Retry Report
- QA Report
- Release Decision

Status: Approved
