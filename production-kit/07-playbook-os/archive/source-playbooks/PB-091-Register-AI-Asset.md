# PB-091 --- Register AI Asset

> **Module:** 11 -- Enterprise Assets
>
> **Playbook ID:** PB-091
>
> **Parent Capability:** PB-081 -- AI Asset Management
>
> **Playbook Type:** Executable Skill
>
> **Version:** 1.0.0
>
> **Status:** Stable

------------------------------------------------------------------------

# Executive Summary

Register a newly created AI asset into the Enterprise Asset Registry
using standardized metadata so it becomes discoverable, governed,
traceable, and reusable.

------------------------------------------------------------------------

# Skill Metadata

  Field                Value
  -------------------- ----------------------
  Skill ID             PB-091
  Skill Name           Register AI Asset
  Capability           AI Asset Management
  Execution Type       Manual / AI / Hybrid
  Automation Ready     Yes
  Complexity           Basic
  Estimated Duration   5--10 minutes

------------------------------------------------------------------------

# Purpose

Create a single, authoritative registration record for every new AI
asset.

------------------------------------------------------------------------

# Business Value

-   Prevent unmanaged assets
-   Improve governance
-   Enable reuse
-   Support audits
-   Maintain traceability

------------------------------------------------------------------------

# Prerequisites

-   PB-081 completed
-   Asset created
-   Owner identified

------------------------------------------------------------------------

# Inputs

-   Asset name
-   Asset type
-   Owner
-   Business purpose
-   Metadata
-   Repository location

------------------------------------------------------------------------

# Outputs

-   Registered Asset ID
-   Asset Registry Record
-   Metadata Record
-   Audit Log Entry

------------------------------------------------------------------------

# Workflow

1.  Verify the asset exists.
2.  Identify the asset owner.
3.  Select the asset category.
4.  Complete mandatory metadata.
5.  Validate metadata quality.
6.  Submit the registration.
7.  Generate the unique Asset ID.
8.  Record the audit trail.
9.  Notify stakeholders.

------------------------------------------------------------------------

# Decision Rules

  Condition                   Action
  --------------------------- ----------------------------
  Required metadata missing   Reject registration
  Duplicate asset detected    Escalate for review
  Owner missing               Assign before registration
  Validation successful       Approve registration

------------------------------------------------------------------------

# Validation Checklist

-   [ ] Asset exists
-   [ ] Owner assigned
-   [ ] Metadata complete
-   [ ] Category selected
-   [ ] Asset ID generated
-   [ ] Audit log recorded

------------------------------------------------------------------------

# Success Criteria

-   Asset is searchable.
-   Metadata is complete.
-   Ownership is clear.
-   Asset is ready for lifecycle management.

------------------------------------------------------------------------

# Deliverables

-   Asset Registry Entry
-   Metadata Record
-   Registration Confirmation
-   Audit Record

------------------------------------------------------------------------

# Best Practices

-   Register assets immediately after creation.
-   Use standardized metadata.
-   Avoid duplicate registrations.
-   Keep ownership current.

------------------------------------------------------------------------

# Common Mistakes

-   Missing metadata.
-   Duplicate registrations.
-   Undefined ownership.
-   Incorrect classification.

------------------------------------------------------------------------

# Related Playbooks

**Parent**

-   PB-081 AI Asset Management

**Next Skill**

-   PB-092 Classify AI Asset

------------------------------------------------------------------------

# Version History

  Version   Description
  --------- -----------------
  1.0.0     Initial Release

**End of Playbook**
