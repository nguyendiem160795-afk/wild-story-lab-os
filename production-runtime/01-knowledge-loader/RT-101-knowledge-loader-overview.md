# RT-101 Knowledge Loader Overview

**Module:** 01-knowledge-loader **Version:** 1.0.0

## Purpose

Knowledge Loader là cầu nối giữa `production-kit` và
`production-runtime`.

## Responsibilities

-   Load Character
-   Load World
-   Load Story
-   Load Production Rules
-   Validate Dependencies
-   Build Knowledge Package

## Inputs

-   production-kit repository
-   project_id
-   series_id
-   episode_id

## Outputs

Knowledge Package gồm: - Character Data - World Data - Story Rules -
Prompt Rules

## Validation

-   Repository reachable
-   Required modules exist
-   Version compatible
