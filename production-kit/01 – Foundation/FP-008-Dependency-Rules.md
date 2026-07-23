---
document_id: FP-008
module: 01
category: Principles
title: Dependency Rules (Quy tắc Phụ thuộc)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# Dependency Rules (Quy tắc Phụ thuộc)

> Canonical dependency rules for the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This document defines the dependency rules governing relationships between modules, documents, standards, and other artifacts within EAOSS.

The objective is to maintain a modular, predictable, and maintainable architecture by preventing unnecessary coupling and dependency cycles.

---

# 2. Objectives (Mục tiêu)

The objectives are to:

- Prevent circular dependencies.
- Promote loose coupling.
- Encourage modular architecture.
- Improve maintainability.
- Enable independent evolution.
- Simplify impact analysis.

---

# 3. Scope (Phạm vi)

These rules apply to:

- Modules
- Documents
- Standards
- Policies
- Principles
- Templates
- Future EAOSS artifacts

---

# 4. Rule 1 — Directed Dependencies

Dependencies shall always have a clear direction.

A dependent artifact may reference another artifact, but the reverse dependency shall not be introduced without architectural review.

---

# 5. Rule 2 — No Circular Dependencies

Circular dependencies are prohibited.

The following pattern is not allowed:

```text
Module A
    ↓
Module B
    ↓
Module C
    ↓
Module A
```

Any identified cycle shall be resolved before approval.

---

# 6. Rule 3 — Depend on Stable Artifacts

Whenever possible, dependencies should target stable artifacts such as:

- Approved standards
- Published principles
- Official baselines
- Canonical specifications

Avoid depending on draft or experimental artifacts.

---

# 7. Rule 4 — Minimize Dependencies

Each artifact should depend on the smallest possible set of external artifacts.

Reducing dependency count improves maintainability and reduces change impact.

---

# 8. Rule 5 — Explicit Dependencies

Every dependency shall be documented.

Dependencies should identify:

- Target artifact
- Purpose
- Dependency type
- Impact if changed

Hidden dependencies are not permitted.

---

# 9. Rule 6 — Layer Respect

Dependencies shall follow the approved architectural layers.

Higher-level modules may depend on lower-level modules.

Lower-level modules shall not depend on higher-level modules.

---

# 10. Rule 7 — Reference Instead of Duplication

Artifacts should reference canonical sources rather than duplicate content.

This minimizes maintenance effort and prevents inconsistent updates.

---

# 11. Rule 8 — Dependency Review

New dependencies shall be evaluated for:

- Architectural impact
- Coupling
- Stability
- Long-term maintenance
- Alternative designs

Dependency Review is required for significant architectural changes.

---

# 12. Rule 9 — Dependency Documentation

Each module should maintain a documented dependency section that identifies:

- Upstream dependencies
- Downstream consumers
- External references
- Dependency constraints

---

# 13. Rule 10 — Evolution Without Cascade Failure

Dependencies should be designed to minimize ripple effects.

Changes in one artifact should require minimal modifications to dependent artifacts.

---

# 14. Dependency Checklist

Every dependency should satisfy the following checklist:

| Requirement | Mandatory |
|-------------|-----------|
| Clearly documented | Yes |
| No circular dependency | Yes |
| Stable target | Yes |
| Minimal coupling | Yes |
| Layer compliant | Yes |
| Architecture reviewed (if significant) | Yes |

---

# 15. Compliance

All EAOSS artifacts shall comply with these dependency rules.

Compliance shall be verified during Architecture Review and Compliance Review.

---

# 16. References

- FP-001 Architecture Principles
- FP-002 Engineering Principles
- FP-004 Documentation Principles
- FP-005 Governance Principles
- FP-007 Versioning Policy
- 01-foundation/ARCHITECTURE.md

---

# 17. Revision History

| Version | Date | Description |
|----------|------|-------------|
| 1.0.0 | 2026-07-23 | Initial Dependency Rules |

---

# End of Document