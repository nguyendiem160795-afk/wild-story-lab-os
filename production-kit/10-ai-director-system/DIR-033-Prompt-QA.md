# DIR-033 Prompt QA

## Metadata

ID: DIR-033
Module: 10 AI Director System
Category: Quality Intelligence
Version: 1.0.0
Status: Active

## Purpose

Prompt QA chịu trách nhiệm kiểm định Prompt cuối cùng trước khi xuất sang Google Flow, Veo, Runway, Sora hoặc Luma, đảm bảo Prompt đầy đủ, nhất quán và sẵn sàng sử dụng.

## Responsibilities

- Kiểm tra Prompt Structure
- Kiểm tra Prompt Completeness
- Kiểm tra Character Consistency
- Kiểm tra Story Consistency
- Kiểm tra Cinematic Language
- Kiểm tra Platform Compatibility

## Inputs

- Master Prompt
- Platform Prompt
- Validation Report
- Optimization Report
- Quality Score

## QA Pipeline

Load Prompt
→ Structure QA
→ Semantic QA
→ Cinematic QA
→ Platform QA
→ Final Approval

## Validation Checklist

### Structure
- Required Prompt Blocks
- Correct Ordering
- No Redundant Instructions

### Story
- Story Goal Preserved
- Story Beat Alignment
- Ending Integrity

### Character
- Character DNA
- Emotion
- Acting
- Dialogue

### Cinematic
- Camera
- Lens
- Lighting
- Composition
- Motion
- FX

### Platform
- Google Flow Ready
- Veo Ready
- Runway Ready
- Sora Ready
- Luma Ready

## Outputs

- Prompt QA Report
- Final QA Score
- Critical Issues
- Approval Status

## Acceptance Criteria

- QA Score ≥ 90
- No Critical Errors
- Platform Compatibility PASS
- Ready for Production

## Dependencies

- DIR-026 Prompt Validator
- DIR-027 Prompt Optimizer
- DIR-028 Platform Adapter
- DIR-029 Quality Scoring

Status: Approved
