---
document_id: GL-008
module: 01-foundation
category: glossary
title: Quality Terms
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
created_date: 2026-07-23
last_updated: 2026-07-23
---

# Quality Terms

> Official quality terminology dictionary for the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose

This glossary defines quality-related terminology used throughout EAOSS.

The purpose is to establish a common language for:

- Quality management.
- Quality evaluation.
- Validation processes.
- Continuous improvement.
- Artifact governance.

---

# 2. Quality

## Definition

Quality represents the degree to which an artifact, system, process, or output satisfies defined requirements and expectations.

Quality characteristics include:

- Correctness.
- Completeness.
- Consistency.
- Reliability.
- Maintainability.

---

# 3. Quality Management

## Definition

Quality Management is the coordinated process of planning, controlling, and improving quality across the organization.

Quality Management includes:

- Standards definition.
- Quality evaluation.
- Review processes.
- Improvement activities.

---

# 4. Quality Assurance (QA)

## Definition

Quality Assurance is a preventive approach that ensures processes are designed and followed correctly to produce expected outcomes.

QA focuses on:

- Process compliance.
- Standard adoption.
- Prevention of defects.

---

# 5. Quality Control (QC)

## Definition

Quality Control is an inspection-based approach used to identify defects or deviations in completed outputs.

QC activities include:

- Artifact inspection.
- Compliance checking.
- Error detection.

---

# 6. Validation

## Definition

Validation confirms that an artifact, system, or process satisfies the intended business or user requirements.

Validation answers:

"Are we building the right thing?"

---

# 7. Verification

## Definition

Verification confirms that an artifact has been created according to defined specifications and standards.

Verification answers:

"Are we building it correctly?"

---

# 8. Accuracy

## Definition

Accuracy measures how closely information represents the actual intended state.

Examples:

- Correct information.
- Correct metadata.
- Correct references.

---

# 9. Completeness

## Definition

Completeness measures whether all required information and components are present.

A complete artifact should contain:

- Required sections.
- Required metadata.
- Required references.

---

# 10. Consistency

## Definition

Consistency ensures that information, structures, and processes remain uniform across the system.

Examples:

- Naming consistency.
- Version consistency.
- Terminology consistency.

---

# 11. Reliability

## Definition

Reliability represents the ability of a system or artifact to perform consistently and produce dependable results.

---

# 12. Maintainability

## Definition

Maintainability measures how easily an artifact can be updated, modified, and managed throughout its lifecycle.

Maintainable artifacts have:

- Clear structure.
- Proper documentation.
- Version tracking.

---

# 13. Traceability

## Definition

Traceability is the ability to track relationships between requirements, decisions, changes, and implementations.

Example:

```
Requirement
      ↓
Standard
      ↓
Implementation
      ↓
Review
```

---

# 14. Defect

## Definition

A defect is a deviation between the expected requirement and the actual result.

Examples:

- Missing information.
- Incorrect structure.
- Invalid reference.

---

# 15. Quality Metric

## Definition

A Quality Metric is a measurable indicator used to evaluate quality performance.

Examples:

| Metric | Description |
|---|---|
| Completeness Score | Level of information completeness |
| Compliance Rate | Percentage of requirement compliance |
| Defect Count | Number of identified defects |
| Review Pass Rate | Successful review percentage |

---

# 16. Quality Gate

## Definition

A Quality Gate is a mandatory checkpoint that must be passed before an artifact moves to the next lifecycle stage.

Example:

```
Draft
 ↓
Quality Gate
 ↓
Approved
```

---

# 17. Quality Review

## Definition

Quality Review is a structured evaluation process to determine whether an artifact meets defined standards.

A Quality Review evaluates:

- Accuracy.
- Completeness.
- Compliance.
- Usability.

---

# 18. Continuous Improvement

## Definition

Continuous Improvement is an ongoing process of evaluating and enhancing systems, processes, and artifacts.

Common cycle:

```
Plan
 ↓
Execute
 ↓
Review
 ↓
Improve
 ↓
Repeat
```

---

# 19. Quality Checklist

A quality-approved artifact should have:

| Requirement | Mandatory |
|---|---|
| Defined owner | Yes |
| Version identifier | Yes |
| Metadata | Yes |
| Review completed | Yes |
| References included | Yes |
| Lifecycle defined | Yes |

---

# 20. References

- GL-001 Core Terms
- GL-004 Documentation Terms
- GL-007 Lifecycle Terms
- POL-009 Audit Policy
- TMP-006 Review Template

---

# 21. Revision History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-07-23 | Initial Quality Terms Glossary |

---

# End of Document