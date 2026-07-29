# RT-003 Runtime Context

**Module:** 00-runtime-core\
**Version:** 1.0.0\
**Status:** Draft

------------------------------------------------------------------------

# Purpose

Runtime Context là vùng dữ liệu tạm thời được chia sẻ giữa các Runtime
Module trong quá trình thực thi. Context không lưu tri thức; nó chỉ giữ
trạng thái và dữ liệu đang xử lý.

------------------------------------------------------------------------

# Context Hierarchy

1.  Global Context
2.  Project Context
3.  Series Context
4.  Episode Context
5.  Scene Context
6.  Task Context

------------------------------------------------------------------------

# Context Rules

-   Chỉ Runtime mới được ghi Context.
-   Knowledge Loader chỉ đọc dữ liệu từ production-kit.
-   Mỗi Episode có Context riêng.
-   Scene không được ghi đè Global Context.
-   Context bị hủy sau khi hoàn thành Pipeline.

------------------------------------------------------------------------

# Standard Fields

  Field             Description
  ----------------- --------------------
  project_id        Project hiện hành
  series_id         Series đang xử lý
  episode_id        Episode hiện hành
  scene_id          Scene hiện hành
  runtime_id        Phiên Runtime
  execution_state   Trạng thái Runtime
  assets            Asset đã resolve
  prompts           Prompt đã compile
  qa_status         Kết quả QA

------------------------------------------------------------------------

# Context Lifecycle

Initialize

↓

Populate

↓

Update

↓

Validate

↓

Release

------------------------------------------------------------------------

# Integration

Runtime Context được sử dụng bởi:

-   Knowledge Loader
-   Asset Resolver
-   Story Compiler
-   Director Engine
-   Prompt Compiler
-   Flow Runtime
-   QA Runtime

------------------------------------------------------------------------

# Validation Checklist

-   [ ] Runtime ID hợp lệ
-   [ ] Episode ID hợp lệ
-   [ ] Asset đã Inject
-   [ ] Prompt đã Inject
-   [ ] QA Status hợp lệ
-   [ ] Context Release thành công
