# RT-004 Runtime Events

**Module:** 00-runtime-core\
**Version:** 1.0.0\
**Status:** Production Draft

------------------------------------------------------------------------

# Purpose

Runtime Events định nghĩa cơ chế giao tiếp giữa các Runtime Module. Mỗi
sự kiện (Event) đại diện cho một thay đổi trạng thái hoặc một hành động
cần được xử lý trong Pipeline.

------------------------------------------------------------------------

# Event Principles

-   Event chỉ truyền dữ liệu cần thiết.
-   Event không chứa Business Logic.
-   Event có ID duy nhất.
-   Event được ghi vào Production Log khi cần.

------------------------------------------------------------------------

# Standard Event Flow

Request Received

↓

Knowledge Loaded

↓

Assets Resolved

↓

Story Compiled

↓

Director Planned

↓

Prompt Compiled

↓

QA Completed

↓

Ready for Flow

------------------------------------------------------------------------

# Event Catalog

  Event ID   Description
  ---------- --------------------
  EVT-001    Runtime Started
  EVT-002    Knowledge Loaded
  EVT-003    Assets Resolved
  EVT-004    Story Compiled
  EVT-005    Director Completed
  EVT-006    Prompt Generated
  EVT-007    QA Passed
  EVT-008    Flow Ready
  EVT-009    Runtime Completed
  EVT-010    Runtime Failed

------------------------------------------------------------------------

# Event Payload

Required fields:

-   runtime_id
-   project_id
-   episode_id
-   event_id
-   timestamp
-   status

------------------------------------------------------------------------

# Integration

Events được sử dụng bởi:

-   Runtime Core
-   Production Manager
-   QA Runtime
-   Production Log
-   Feedback Engine

------------------------------------------------------------------------

# Validation Checklist

-   [ ] Event ID hợp lệ
-   [ ] Payload đầy đủ
-   [ ] Timestamp hợp lệ
-   [ ] Event được xử lý
-   [ ] Event được ghi log nếu cần
