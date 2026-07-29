# RT-006 Runtime Error Recovery

**Module:** 00-runtime-core\
**Version:** 1.0.0\
**Status:** Production Draft

------------------------------------------------------------------------

# Purpose

Runtime Error Recovery định nghĩa cơ chế phát hiện, phân loại và phục
hồi lỗi trong toàn bộ Production Runtime nhằm đảm bảo pipeline có thể
tiếp tục hoạt động an toàn.

------------------------------------------------------------------------

# Objectives

-   Giảm lỗi dừng toàn bộ pipeline.
-   Hỗ trợ Retry có kiểm soát.
-   Ghi đầy đủ Production Log.
-   Cho phép Resume từ Checkpoint.

------------------------------------------------------------------------

# Error Categories

  Code      Category         Action
  --------- ---------------- ---------------
  ERR-001   Configuration    Abort
  ERR-002   Knowledge Load   Retry
  ERR-003   Asset Resolve    Retry
  ERR-004   Story Compile    Retry
  ERR-005   Prompt Compile   Retry
  ERR-006   QA Failed        Stop & Report
  ERR-007   Flow Export      Retry
  ERR-999   Unknown          Manual Review

------------------------------------------------------------------------

# Recovery Strategy

1.  Detect Error
2.  Capture Context
3.  Save Checkpoint
4.  Retry (max 1)
5.  Resume Pipeline
6.  Escalate nếu vẫn thất bại

------------------------------------------------------------------------

# Checkpoint Policy

-   CP-01 Runtime Boot
-   CP-02 Knowledge Loaded
-   CP-03 Story Ready
-   CP-04 Prompt Ready
-   CP-05 QA Passed

------------------------------------------------------------------------

# Production Log

Mỗi lỗi cần ghi:

-   runtime_id
-   error_code
-   module
-   timestamp
-   recovery_action
-   final_status

------------------------------------------------------------------------

# Validation Checklist

-   [ ] Error được phân loại
-   [ ] Context được lưu
-   [ ] Checkpoint hợp lệ
-   [ ] Recovery hoàn tất
-   [ ] Production Log cập nhật
