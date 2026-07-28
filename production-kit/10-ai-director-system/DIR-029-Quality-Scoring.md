# DIR-029 Quality Scoring

## Metadata

ID: DIR-029
Module: 10 AI Director System
Category: Prompt Orchestrator
Version: 1.0.0
Status: Active

## Purpose

Quality Scoring đánh giá chất lượng tổng thể của Prompt và kế hoạch đạo diễn trước khi xuất sang nền tảng AI Video.

## Responsibilities

- Chấm điểm Story
- Chấm điểm Character Consistency
- Chấm điểm Cinematic Quality
- Chấm điểm Prompt Completeness
- Chấm điểm Platform Compatibility
- Đưa ra Production Readiness Score

## Scoring Categories

| Category | Weight |
|----------|-------:|
| Story Quality | 25% |
| Character Consistency | 20% |
| Cinematic Language | 20% |
| Prompt Completeness | 15% |
| Platform Compatibility | 10% |
| Technical Validation | 10% |

## Scoring Pipeline

Load Prompt
→ Evaluate Story
→ Evaluate Character
→ Evaluate Cinematic Decisions
→ Evaluate Platform Compatibility
→ Calculate Final Score

## Score Levels

- 95–100: Production Ready
- 85–94: Minor Optimization
- 70–84: Revision Required
- Below 70: Retry Required

## Outputs

- Quality Report
- Final Score
- Improvement Suggestions
- Production Readiness Flag

## Validation Rules

- Không xuất Prompt dưới ngưỡng 85.
- Mọi lỗi nghiêm trọng phải được sửa trước khi xuất.
- Điểm Story và Character không được dưới 80.

## Dependencies

- DIR-026 Prompt Validator
- DIR-027 Prompt Optimizer
- DIR-028 Platform Adapter

Status: Approved
