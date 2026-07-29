# RT-005 Runtime Interfaces

**Module:** 00-runtime-core\
**Version:** 1.0.0\
**Status:** Production Draft

------------------------------------------------------------------------

# Purpose

Runtime Interfaces định nghĩa hợp đồng (Contract) giữa các Runtime
Module nhằm đảm bảo mọi thành phần có thể giao tiếp thống nhất và dễ mở
rộng.

------------------------------------------------------------------------

# Interface Design Rules

-   Một Interface chỉ có một trách nhiệm.
-   Input và Output phải được chuẩn hóa.
-   Không phụ thuộc vào implementation cụ thể.
-   Mọi Runtime Module phải công bố Interface.

------------------------------------------------------------------------

# Core Interfaces

## IKnowledgeLoader

### Input

-   project_id
-   series_id
-   episode_id

### Output

-   Knowledge Package

------------------------------------------------------------------------

## IAssetResolver

### Input

-   Knowledge Package

### Output

-   Asset Package

------------------------------------------------------------------------

## IStoryCompiler

### Input

-   Asset Package

### Output

-   Story Package

------------------------------------------------------------------------

## IDirectorEngine

### Input

-   Story Package

### Output

-   Director Plan

------------------------------------------------------------------------

## IPromptCompiler

### Input

-   Director Plan

### Output

-   Prompt Package

------------------------------------------------------------------------

## IQARuntime

### Input

-   Prompt Package

### Output

-   QA Report

------------------------------------------------------------------------

# Interface Contract

Mỗi Interface phải xác định:

-   Input Schema
-   Output Schema
-   Validation Rules
-   Error Codes
-   Version

------------------------------------------------------------------------

# Versioning

-   v1.0 Initial
-   Backward Compatible
-   Semantic Versioning

------------------------------------------------------------------------

# Validation Checklist

-   [ ] Interface Name hợp lệ
-   [ ] Input đầy đủ
-   [ ] Output đầy đủ
-   [ ] Version xác định
-   [ ] Contract được kiểm thử
