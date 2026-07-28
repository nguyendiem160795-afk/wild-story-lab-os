# DIR-003 Director Decision Engine

## Metadata

ID: DIR-003
Module: 10 AI Director System
Category: Director Core
Version: 1.0.0
Status: Active

## Purpose

Định nghĩa cơ chế ra quyết định của AI Director. Đây là thành phần lựa chọn phương án đạo diễn tối ưu dựa trên Story, Character và Production Components.

## Decision Inputs

- Story Goal
- Story Beat
- Character State
- Emotional Target
- Target Platform
- Production Constraints

## Decision Pipeline

Story Analysis
→ Context Evaluation
→ Rule Matching
→ Component Selection
→ Conflict Resolution
→ Quality Scoring
→ Decision Output

## Decision Domains

### Story
- Hook
- WOW
- Climax
- Ending

### Cinematic
- Shot
- Lens
- Camera Movement
- Lighting
- Composition

### Character
- Acting
- Emotion
- Motion
- Eye Contact

### Production
- FX
- Audio
- Prompt Strategy
- Style Preset

## Decision Rules

- Story luôn ưu tiên hơn hiệu ứng.
- Character phải nhất quán.
- Chỉ một trọng tâm thị giác mỗi cảnh.
- Mọi quyết định phải hỗ trợ Story Goal.
- Ưu tiên thành phần đã được chuẩn hóa trong Module 09.

## Outputs

- Scene Decision
- Shot Decision
- Prompt Decision
- QA Score

## Dependencies

- DIR-002 Director Workflow
- Module 05 Story Engine
- Module 09 Production Components

Status: Approved
