## Execution Contract
- ID: PB-092-Classify-AI-Asset
- Version: 1.0
- Status: Executable Draft

## Objective

## Inputs

## Outputs

## Validation

---

# PB-092 --- Classify AI Asset

> **Module:** 11 -- Enterprise Assets
>
> **Playbook ID:** PB-092
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

Classify every registered AI asset into the appropriate category to
improve governance, discoverability, lifecycle management, security, and
automation.

------------------------------------------------------------------------

# Skill Metadata

  Field                Value
  -------------------- ----------------------
  Skill ID             PB-092
  Skill Name           Classify AI Asset
  Capability           AI Asset Management
  Execution Type       Manual / AI / Hybrid
  Automation Ready     Yes
  Complexity           Basic
  Estimated Duration   5--10 minutes

------------------------------------------------------------------------

# Purpose

Assign a standardized classification to every AI asset immediately after
registration.

------------------------------------------------------------------------

# Business Value

-   Improve searchability
-   Enable lifecycle policies
-   Support security controls
-   Simplify reporting
-   Reduce classification errors

------------------------------------------------------------------------

# Prerequisites

-   PB-091 completed
-   Asset registered
-   Metadata available

------------------------------------------------------------------------

# Inputs

-   Asset ID
-   Asset metadata
-   Asset description
-   Business owner
-   Intended use

------------------------------------------------------------------------

# Outputs

-   Classification record
-   Updated asset profile
-   Classification audit log

------------------------------------------------------------------------

# Workflow

1.  Retrieve the registered asset.
2.  Review metadata and purpose.
3.  Select the primary asset category.
4.  Apply secondary tags if required.
5.  Validate classification rules.
6.  Save the classification.
7.  Update the registry.
8.  Record the audit trail.
9.  Notify dependent systems.

------------------------------------------------------------------------

# Decision Rules

  Condition                   Action
  --------------------------- --------------------------------
  Insufficient metadata       Request additional information
  Multiple valid categories   Escalate for review
  Classification validated    Approve and publish

------------------------------------------------------------------------

# Validation Checklist

-   [ ] Asset ID verified
-   [ ] Category assigned
-   [ ] Tags applied
-   [ ] Registry updated
-   [ ] Audit log created

------------------------------------------------------------------------

# Success Criteria

-   Asset has a valid classification.
-   Registry reflects the correct category.
-   Classification supports downstream automation.

------------------------------------------------------------------------

# Deliverables

-   Classification Record
-   Updated Registry Entry
-   Audit Record

------------------------------------------------------------------------

# Best Practices

-   Use standardized taxonomy.
-   Avoid overlapping categories.
-   Review classifications periodically.

------------------------------------------------------------------------

# Common Mistakes

-   Using inconsistent categories.
-   Missing mandatory tags.
-   Skipping validation.

------------------------------------------------------------------------

# Related Playbooks

**Parent**

-   PB-081 AI Asset Management

**Previous Skill**

-   PB-091 Register AI Asset

**Next Skill**

-   PB-093 Update Asset Metadata

------------------------------------------------------------------------

# Version History

  Version   Description
  --------- -----------------
  1.0.0     Initial Release

**End of Playbook**


## Decision Points

## Validation Checklist
- [ ] Inputs verified
- [ ] Outputs validated

## Related Capability

## Related Skill

## Automation Hooks
- Trigger:
- Inputs:
- Outputs:
