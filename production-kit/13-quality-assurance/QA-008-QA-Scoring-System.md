# QA-008 — QA Scoring System

Version: 1.0.0

Status: Production

Owner: Wild Story Lab

Last Updated: 2026-07-23

---

# Purpose

QA Scoring System defines the official scoring methodology used to evaluate every Wild Story Lab production.

The system combines all quality validation modules into a single production score that determines release readiness.

---

# Objectives

- Standardize quality evaluation
- Remove subjective decision-making
- Support automated approval
- Identify production weaknesses
- Improve production consistency
- Enable historical quality analysis

---

# Scoring Architecture

Story

↓

Character

↓

Prompt

↓

Render

↓

Educational

↓

Publishing

↓

Final Score

↓

Release Decision

---

# QA Categories

## Character Consistency

Reference

QA-002

Weight

20%

---

## Story Validation

Reference

QA-003

Weight

20%

---

## Prompt Quality

Reference

QA-004

Weight

15%

---

## Render Validation

Reference

QA-005

Weight

20%

---

## Educational Standards

Reference

QA-006

Weight

15%

---

## Publishing QA

Reference

QA-007

Weight

10%

---

# Scoring Formula

Overall Score

```
Final Score =

(Character × 0.20)

+

(Story × 0.20)

+

(Prompt × 0.15)

+

(Render × 0.20)

+

(Educational × 0.15)

+

(Publishing × 0.10)
```

---

# Rating Scale

| Score | Rating | Status |
|--------|--------|--------|
| 98–100 | Exceptional | Studio Master |
| 95–97 | Excellent | Approved |
| 90–94 | Good | Approved With Notes |
| 85–89 | Acceptable | Review Required |
| Below 85 | Unacceptable | Rejected |

---

# Critical Failure Rules

A production automatically fails if any of the following occur

- Child safety violation
- Copyright violation
- Character identity failure
- Broken story continuity
- Corrupted render
- Missing Production Manifest

Final Score is ignored when a Critical Failure exists.

---

# Severity Multipliers

| Severity | Penalty |
|----------|--------:|
| Critical | Automatic Failure |
| Major | −10 Points |
| Minor | −2 Points |
| Informational | No Penalty |

---

# Approval Workflow

Evaluation

↓

Category Scores

↓

Critical Failure Check

↓

Weighted Score

↓

QA Report

↓

Approval Decision

---

# QA Report

Every evaluation generates

- Final Score
- Category Scores
- Failed Checks
- Warnings
- Recommendations
- Approval Status
- Reviewer
- Timestamp

---

# Example Report

```
Project

ENG-001

Character

99

Story

97

Prompt

98

Render

99

Educational

100

Publishing

97

Final Score

98.4

Status

APPROVED
```

---

# Historical Tracking

Maintain

- Previous Scores
- Trend Analysis
- Common Failures
- Improvement History
- Reviewer Notes

---

# Performance Indicators

Monitor

✓ Average Production Score

✓ Approval Rate

✓ Re-render Rate

✓ Revision Rate

✓ Publishing Success Rate

✓ Educational Accuracy

---

# Best Practices

- Score every production consistently.
- Never bypass Critical Failure rules.
- Archive every QA report.
- Compare current scores with historical averages.
- Use score trends to improve future productions.

---

# Related Documents

- QA-001 Final Video Checklist
- QA-002 Character Consistency
- QA-003 Story Validation
- QA-004 Prompt Quality
- QA-005 Render Validation
- QA-006 Educational Standards
- QA-007 Publishing QA
- RT-006 Production Checklist