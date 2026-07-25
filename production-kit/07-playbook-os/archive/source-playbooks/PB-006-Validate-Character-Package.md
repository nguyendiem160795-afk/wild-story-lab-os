## Execution Contract
- ID: PB-006-Validate-Character-Package
- Version: 1.0
- Status: Executable Draft

## Objective

## Inputs

## Outputs

## Validation

---

# PB-006 --- Validate Character Package

> **Module:** Module 07 -- Playbook OS\
> **Playbook ID:** PB-006\
> **Version:** 1.0.0\
> **Status:** Stable

------------------------------------------------------------------------

## Document Information

  Field     Value
  --------- ----------------------------
  ID        PB-006
  Title     Validate Character Package
  Domain    Character Development
  Owner     Wild Story Lab
  Version   1.0.0
  Status    Stable

------------------------------------------------------------------------

## Overview

This Playbook validates a Character Package before prompt engineering
and visual production begin.

## 1. Purpose

Ensure every Character Package is complete, consistent, reusable, and
aligned with the approved Story Package.

## 2. Business Value

-   Prevent character inconsistency.
-   Protect brand identity.
-   Reduce redesign iterations.
-   Improve production quality.

## 3. Scope

### Included

-   Validate character profile.
-   Validate visual consistency.
-   Validate personality.
-   Validate production readiness.
-   Approve or reject Character Package.

### Excluded

-   Creating new characters.
-   Prompt generation.
-   Image or video production.

## 4. Inputs

Required: - Character Package (PB-005)

Optional: - Story Package - Brand Bible - Character Bible

## 5. Outputs

One of the following:

-   Approved Character Package
-   Revision Request
-   Rejected Character Package

## 6. Workflow

1.  Review Character Package
2.  Validate Character Profile
3.  Validate Visual Identity
4.  Validate Personality
5.  Validate Consistency Rules
6.  Record Validation Results
7.  Approve or Return for Revision

## 7. Validation Checklist

-   [ ] Character Name
-   [ ] Role
-   [ ] Appearance
-   [ ] Costume
-   [ ] Personality
-   [ ] Voice Style
-   [ ] Expressions
-   [ ] Consistency Rules
-   [ ] Production Notes

## 8. Decision Matrix

  Result            Action
  ----------------- ---------------------------
  Pass              Approve Character Package
  Minor Issues      Return for Revision
  Critical Issues   Reject Character Package

## 9. Deliverables

``` text
Character Validation Report
├── Validation Status
├── Missing Items
├── Consistency Issues
├── Recommendations
└── Approval Decision
```

## 10. Quality Standards

A validated Character Package must be:

-   Complete
-   Consistent
-   Reusable
-   Production Ready
-   Brand Aligned

## 11. Best Practices

-   Keep one visual identity.
-   Maintain consistent costume.
-   Use clear personality traits.
-   Validate every production asset against the package.

## 12. Common Mistakes

-   Different appearance between scenes.
-   Undefined personality.
-   Costume changes without reason.
-   Missing expressions.

## 13. Related Playbooks

Previous: - PB-005 Create Character Package

Next: - PB-007 Create Prompt Package

## 14. References

-   PB-003 Create Story Package
-   PB-004 Validate Story Package
-   PB-005 Create Character Package

## 15. Changelog

  Version   Date         Description
  --------- ------------ -----------------
  1.0.0     YYYY-MM-DD   Initial Release

------------------------------------------------------------------------

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
