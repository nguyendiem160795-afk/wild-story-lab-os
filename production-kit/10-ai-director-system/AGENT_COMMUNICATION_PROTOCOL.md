# AGENT_COMMUNICATION_PROTOCOL.md

# AI Agent Communication Protocol

Version: 1.0.0
Status: Draft

## Purpose

Định nghĩa giao thức giao tiếp chuẩn giữa các AI Agent trong Wild Story Lab OS nhằm đảm bảo truyền dữ liệu nhất quán, có khả năng mở rộng và hỗ trợ tự động hóa.

---

# Communication Architecture

Story Agent
      │
Character Agent
      │
Camera Agent
      │
Prompt Agent
      │
QA Agent
      │
Release Agent
      │
AI Director (Coordinator)

---

# Message Lifecycle

Create Request
↓
Validate Message
↓
Dispatch
↓
Process
↓
Return Response
↓
Log Result

---

# Message Format

Header
- message_id
- sender
- receiver
- timestamp
- priority

Body
- task
- payload
- metadata

Footer
- status
- checksum

---

# Request Types

- STORY_REQUEST
- CHARACTER_REQUEST
- CAMERA_REQUEST
- PROMPT_REQUEST
- QA_REQUEST
- RELEASE_REQUEST

---

# Response Types

- SUCCESS
- WARNING
- FAILED
- RETRY_REQUIRED

---

# Priority Levels

P1 Critical
P2 High
P3 Normal
P4 Low

---

# Retry Protocol

Retry Level 1
Retry Level 2
Retry Level 3

Maximum Retry: 3

---

# Error Codes

ACP-001 Invalid Message
ACP-002 Missing Payload
ACP-003 Invalid Receiver
ACP-004 Timeout
ACP-005 Validation Failed

---

# Shared Context

Agents share:

- Story Context
- Character Context
- Scene Context
- Prompt Context
- QA Context

AI Director controls synchronization.

---

# Outputs

- Communication Log
- Request Log
- Response Log
- Retry Report

Status: Draft
