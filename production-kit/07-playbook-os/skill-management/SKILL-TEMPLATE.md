# SKILL-TEMPLATE.md

> **Module:** 07 -- Playbook OS **Layer:** Skill Management **Document
> Type:** Canonical Skill Specification **Version:** 3.0.0 **Status:**
> Stable

------------------------------------------------------------------------

# Purpose

This document defines the canonical specification for every Executable
Skill in Playbook OS.

A Skill is the smallest executable unit of work within the system.

Every Skill Object MUST conform to this specification.

------------------------------------------------------------------------

# Skill Object Architecture

``` text
Business Domain
        │
        ▼
Operational Domain
        │
        ▼
Capability
        │
        ▼
Executable Skill
```

------------------------------------------------------------------------

# Canonical Skill Schema

  Field                Type      Required   Description
  -------------------- --------- ---------- ---------------------------------------
  id                   String    ✅         Permanent Skill Identifier
  name                 String    ✅         Skill Name
  capability           String    ✅         Parent Capability
  business_domain      String    ✅         Business Domain ID
  operational_domain   String    ✅         Operational Domain ID
  version              String    ✅         Semantic Version
  status               Enum      ✅         Draft / Stable / Deprecated / Retired
  complexity           Enum      ✅         Basic / Intermediate / Advanced
  automation_ready     Boolean   ✅         AI Execution Ready
  owner                String    Optional   Skill Owner

------------------------------------------------------------------------

# Execution Schema

Every Skill MUST contain:

  Section            Required
  ------------------ ----------
  Purpose            ✅
  Business Value     ✅
  Inputs             ✅
  Outputs            ✅
  Workflow           ✅
  Decision Rules     ✅
  Validation         ✅
  Success Criteria   ✅
  Dependencies       Optional
  Related Skills     Optional

------------------------------------------------------------------------

# Canonical YAML Example

``` yaml
id: PB-091

name: Register AI Asset

capability: CAP-081

business_domain: BD-001

operational_domain: OD-001

version: 1.0.0

status: Stable

complexity: Basic

automation_ready: true

purpose:

business_value:

inputs:

outputs:

workflow:

decision_rules:

validation:

success_criteria:

dependencies:

related_skills:
```

------------------------------------------------------------------------

# Skill Lifecycle

``` text
Draft
    ↓
Review
    ↓
Approved
    ↓
Stable
    ↓
Deprecated
    ↓
Retired
```

------------------------------------------------------------------------

# AI Execution Requirements

Every Skill must:

-   Be uniquely identifiable.
-   Be executable independently.
-   Support deterministic execution.
-   Produce measurable outputs.
-   Be machine-readable.
-   Be automation-ready.

------------------------------------------------------------------------

# Validation Checklist

Before a Skill is published:

-   [ ] Registered in SKILL-REGISTRY
-   [ ] Parent Capability exists
-   [ ] Metadata complete
-   [ ] Workflow documented
-   [ ] Validation defined
-   [ ] Version assigned
-   [ ] Governance approved

------------------------------------------------------------------------

# Related Documents

-   DOMAIN-REGISTRY.md
-   CAPABILITY-REGISTRY.md
-   SKILL-REGISTRY.md
-   MASTER-SKILL-INDEX.md
-   CAPABILITY-TEMPLATE.md
-   GOVERNANCE.md

------------------------------------------------------------------------

**End of Document**
