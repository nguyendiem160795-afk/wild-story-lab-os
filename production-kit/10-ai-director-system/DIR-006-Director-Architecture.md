# DIR-006 Director Architecture

## Metadata

ID: DIR-006
Module: 10 AI Director System
Category: Director Core
Version: 1.0.0
Status: Active

## Purpose

Định nghĩa kiến trúc tổng thể của AI Director và cách các thành phần phối hợp để chuyển Story thành Prompt Package hoàn chỉnh.

## High-Level Architecture

Story Engine
        │
        ▼
Story Analyzer
        │
        ▼
Decision Engine
        │
 ┌──────┼────────┬──────────┬──────────┐
 ▼      ▼        ▼          ▼
Scene  Camera  Character   Audio
Planner Director Director Director
        │
        └──────────────┐
                       ▼
              Prompt Orchestrator
                       │
                       ▼
               Quality Intelligence
                       │
                       ▼
                 Export Manager

## Core Components

- Story Analyzer
- Scene Planner
- Decision Engine
- Camera Director
- Character Director
- Prompt Orchestrator
- Quality Intelligence
- Export Manager

## Data Flow

Input Story
→ Story Analysis
→ Scene Blueprint
→ Directing Decisions
→ Prompt Assembly
→ QA Validation
→ Export Package

## Integration

- Module 05 Story Engine
- Module 06 Character System
- Module 08 AI Agent OS
- Module 09 Production Components

## Outputs

- Scene Plan
- Shot List
- Prompt Package
- QA Report
- Production Report

Status: Approved
