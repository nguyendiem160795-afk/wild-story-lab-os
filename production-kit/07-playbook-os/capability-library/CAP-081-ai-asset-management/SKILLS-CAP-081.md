# SKILLS.md

> **Capability ID:** CAP-081\
> **Capability:** AI Asset Management\
> **Version:** 1.0.0\
> **Status:** Stable

------------------------------------------------------------------------

# Purpose

This document defines the executable Skill Objects contained within
CAP-081.

Each Skill represents a reusable operational capability that can be
executed by humans or AI Agents.

------------------------------------------------------------------------

# Skill Catalog

  -----------------------------------------------------------------------
  ID                Skill             Purpose           Status
  ----------------- ----------------- ----------------- -----------------
  PB-091            Register AI Asset Register a new AI Stable
                                      asset into the    
                                      repository        

  PB-092            Classify AI Asset Assign            Stable
                                      categories, tags  
                                      and metadata      

  PB-093            Update Asset      Maintain metadata Stable
                    Metadata          accuracy          

  PB-094            Assign Asset      Record ownership  Stable
                    Owner             and               
                                      accountability    

  PB-095            Validate Asset    Verify            Stable
                    Quality           completeness and  
                                      quality           

  PB-096            Audit AI Asset    Review compliance Stable
                                      and lifecycle     
                                      status            

  PB-097            Archive AI Asset  Archive inactive  Stable
                                      assets            

  PB-098            Restore Archived  Restore archived  Stable
                    Asset             assets when       
                                      required          

  PB-099            Calculate Asset   Evaluate business Stable
                    Value             value of an asset 

  PB-100            Retire AI Asset   Permanently       Stable
                                      retire an asset   
                                      from active use   
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Skill Execution Order

``` text
PB-091 Register
      ↓
PB-092 Classify
      ↓
PB-093 Update Metadata
      ↓
PB-094 Assign Owner
      ↓
PB-095 Validate
      ↓
PB-096 Audit
      ↓
PB-097 Archive
      ↓
PB-098 Restore (Optional)
      ↓
PB-099 Calculate Value
      ↓
PB-100 Retire
```

------------------------------------------------------------------------

# Skill Object Template

Each Skill follows the standard schema:

``` yaml
id:
name:
purpose:
inputs:
outputs:
workflow:
validation:
dependencies:
automation_ready:
version:
status:
```

------------------------------------------------------------------------

# Dependencies

-   CAPABILITY.md
-   EXAMPLES.md
-   SKILL-REGISTRY.md
-   MASTER-SKILL-INDEX.md

------------------------------------------------------------------------

# Notes

This document serves as the authoritative index of executable Skills
within CAP-081. Detailed execution logic can evolve independently while
preserving the Skill IDs.

------------------------------------------------------------------------

**End of Document**
