# CAPABILITY-TEMPLATE.md

> **Module:** 07 -- Playbook OS **Layer:** Skill Management **Document
> Type:** Template **Version:** 3.0.0 **Status:** Stable

------------------------------------------------------------------------

# Purpose

This document defines the standard structure for every Capability Pack
in Playbook OS.

All Capability Packs MUST follow this template to ensure consistency,
scalability, AI compatibility, and automation readiness.

------------------------------------------------------------------------

# Standard Folder Structure

``` text
CAP-XXX-capability-name/
│
├── CAPABILITY.md
├── SKILLS.md
└── EXAMPLES.md (optional)
```

------------------------------------------------------------------------

# CAPABILITY.md Structure

Every `CAPABILITY.md` MUST contain the following sections:

1.  Executive Summary
2.  Capability Metadata
3.  Purpose
4.  Business Value
5.  Scope
6.  Objectives
7.  Architecture
8.  Dependencies
9.  Inputs
10. Outputs
11. Success Criteria
12. Governance Rules
13. Related Capability Packs
14. Version History

------------------------------------------------------------------------

# SKILLS.md Structure

Every Skill Object MUST include:

  Field              Required
  ------------------ ----------
  Skill ID           ✅
  Skill Name         ✅
  Purpose            ✅
  Inputs             ✅
  Outputs            ✅
  Workflow           ✅
  Decision Rules     ✅
  Validation         ✅
  Dependencies       Optional
  Automation Ready   ✅
  Complexity         ✅

------------------------------------------------------------------------

# Metadata Standard

## Capability Metadata

``` text
Capability ID
Capability Name
Business Domain
Operational Domain
Owner
Version
Status
Last Updated
```

------------------------------------------------------------------------

# Naming Convention

Capability Folder

``` text
CAP-081-ai-asset-management
```

Capability Document

``` text
CAPABILITY.md
```

Skills Document

``` text
SKILLS.md
```

Examples

``` text
EXAMPLES.md
```

------------------------------------------------------------------------

# Capability Lifecycle

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

# AI Compatibility Requirements

Every Capability Pack must:

-   Reference DOMAIN-REGISTRY.
-   Reference CAPABILITY-REGISTRY.
-   Reference SKILL-REGISTRY.
-   Be discoverable through MASTER-SKILL-INDEX.
-   Support AI routing.
-   Support automation workflows.

------------------------------------------------------------------------

# Validation Checklist

Before publication:

-   [ ] Capability registered
-   [ ] Skills registered
-   [ ] Metadata complete
-   [ ] Template compliant
-   [ ] Cross-references verified
-   [ ] Version updated
-   [ ] Governance review completed

------------------------------------------------------------------------

# Related Documents

-   README.md
-   GOVERNANCE.md
-   DOMAIN-REGISTRY.md
-   CAPABILITY-REGISTRY.md
-   SKILL-REGISTRY.md
-   MASTER-SKILL-INDEX.md
-   SKILL-TEMPLATE.md

------------------------------------------------------------------------

**End of Document**
