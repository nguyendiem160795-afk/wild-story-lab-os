# RT-001 Runtime Core Overview

**Module:** 00-runtime-core\
**Version:** 1.0.0\
**Status:** Draft for Production

------------------------------------------------------------------------

# 1. Purpose

Runtime Core là hạt nhân điều phối toàn bộ `production-runtime`. Nhiệm
vụ của Runtime Core là thực thi (Execution), không lưu trữ tri thức.
Toàn bộ tri thức được lấy từ `production-kit`.

------------------------------------------------------------------------

# 2. Design Principles

1.  Knowledge và Runtime tách biệt.
2.  Runtime chỉ điều phối.
3.  Mọi module đều có Input → Process → Output.
4.  Không sao chép dữ liệu từ production-kit.
5.  Mọi bước đều có thể kiểm tra (QA).

------------------------------------------------------------------------

# 3. Architecture

``` text
production-kit
      ↓
Knowledge Loader
      ↓
Runtime Core
      ↓
Story Compiler
      ↓
Director Engine
      ↓
Prompt Compiler
      ↓
Flow Runtime
      ↓
QA Runtime
```

------------------------------------------------------------------------

# 4. Runtime Responsibilities

-   Khởi động Runtime.
-   Quản lý Context.
-   Điều phối Event.
-   Điều phối Pipeline.
-   Quản lý lỗi.
-   Ghi Checkpoint.

------------------------------------------------------------------------

# 5. Boot Sequence

1.  Load Configuration
2.  Validate Repository
3.  Initialize Runtime Context
4.  Load Knowledge
5.  Verify Dependencies
6.  Start Execution

------------------------------------------------------------------------

# 6. Runtime Context

-   Global Context
-   Project Context
-   Series Context
-   Episode Context
-   Scene Context

------------------------------------------------------------------------

# 7. Interfaces

-   IKnowledgeLoader
-   IStoryCompiler
-   IDirectorEngine
-   IPromptCompiler
-   IFlowRuntime
-   IQARuntime

------------------------------------------------------------------------

# 8. Error Handling

-   Detect
-   Classify
-   Recover
-   Log
-   Resume

------------------------------------------------------------------------

# 9. Validation Checklist

-   [ ] Repository hợp lệ
-   [ ] Runtime Context hợp lệ
-   [ ] Knowledge Loader sẵn sàng
-   [ ] Dependency đầy đủ
-   [ ] Runtime Boot thành công

------------------------------------------------------------------------

# 10. Next Documents

-   RT-002 Runtime Execution Engine
-   RT-003 Runtime Context
