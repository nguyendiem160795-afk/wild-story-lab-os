# PB-093 --- Update Asset Metadata

> **Module:** 11 -- Enterprise Assets
>
> **Playbook ID:** PB-093
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

Maintain accurate, complete, and current metadata for AI assets
throughout their lifecycle to ensure discoverability, governance,
compliance, and reliable automation.

------------------------------------------------------------------------

# Skill Metadata

  Field                Value
  -------------------- -----------------------
  Skill ID             PB-093
  Skill Name           Update Asset Metadata
  Capability           AI Asset Management
  Execution Type       Manual / AI / Hybrid
  Automation Ready     Yes
  Complexity           Basic
  Estimated Duration   5--10 minutes

------------------------------------------------------------------------

# Purpose

Update metadata whenever an AI asset changes ownership, purpose,
version, location, status, or other business attributes.

------------------------------------------------------------------------

# Business Value

-   Improve asset discoverability
-   Preserve data quality
-   Support compliance
-   Reduce operational errors
-   Enable AI-driven workflows

------------------------------------------------------------------------

# Prerequisites

-   PB-091 completed
-   PB-092 completed
-   Valid Asset ID
-   Change request approved (if required)

------------------------------------------------------------------------

# Inputs

-   Asset ID
-   Current metadata
-   Updated metadata
-   Change reason
-   Requester information

------------------------------------------------------------------------

# Outputs

-   Updated metadata record
-   Metadata version history
-   Audit log
-   Change confirmation

------------------------------------------------------------------------

# Workflow

1.  Locate the asset record.
2.  Verify authorization.
3.  Review requested changes.
4.  Validate mandatory fields.
5.  Apply metadata updates.
6.  Increment metadata version.
7.  Save changes to the registry.
8.  Record the audit trail.
9.  Notify dependent systems.

------------------------------------------------------------------------

# Decision Rules

  Condition                 Action
  ------------------------- --------------------------
  Unauthorized request      Reject update
  Mandatory field missing   Request correction
  Validation successful     Publish updated metadata

------------------------------------------------------------------------

# Validation Checklist

-   [ ] Asset ID verified
-   [ ] Request authorized
-   [ ] Metadata validated
-   [ ] Registry updated
-   [ ] Version history created
-   [ ] Audit log completed

------------------------------------------------------------------------

# Success Criteria

-   Metadata is accurate and current.
-   Changes are traceable.
-   Dependent systems receive updated information.

------------------------------------------------------------------------

# Deliverables

-   Updated Metadata Record
-   Version History
-   Audit Record
-   Update Confirmation

------------------------------------------------------------------------

# Best Practices

-   Update metadata immediately after significant changes.
-   Use standardized naming conventions.
-   Record every modification.

------------------------------------------------------------------------

# Common Mistakes

-   Leaving outdated metadata.
-   Skipping audit logging.
-   Editing without authorization.

------------------------------------------------------------------------

# Related Playbooks

**Parent**

-   PB-081 AI Asset Management

**Previous Skill**

-   PB-092 Classify AI Asset

**Next Skill**

-   PB-094 Assign Asset Owner

------------------------------------------------------------------------

# Version History

  Version   Description
  --------- -----------------
  1.0.0     Initial Release

**End of Playbook**
