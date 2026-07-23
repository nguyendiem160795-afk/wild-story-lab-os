# AG-003 — Agent Communication

Version: 1.0.0

Status: Production

Owner: Wild Story Lab

Last Updated: 2026-07-23

---

# Purpose

Agent Communication defines the messaging protocols, interaction patterns, data exchange standards, and collaboration mechanisms used by AI Agents throughout Wild Story Lab OS.

Reliable communication ensures that agents cooperate efficiently, avoid duplicated work, preserve context, and maintain production consistency.

---

# Objectives

- Standardize communication
- Reduce misunderstandings
- Improve collaboration
- Preserve execution context
- Enable scalable multi-agent workflows
- Support distributed execution

---

# Communication Philosophy

Agents never assume.

Agents communicate through structured messages.

Every important decision is traceable.

Every request has a response.

---

# Communication Architecture

Agent

↓

Message Bus

↓

Routing Engine

↓

Receiving Agent

↓

Execution

↓

Response

↓

Shared Knowledge

---

# Message Types

## Task Request

Sent when requesting work.

Contains

- Task ID
- Objective
- Priority
- Deadline
- Constraints

---

## Task Response

Sent after task completion.

Contains

- Result
- Confidence
- Execution Time
- Recommendations

---

## Information Request

Used when an agent needs additional knowledge.

Examples

- Retrieve Character Bible
- Search Prompt Recipe
- Find Classroom Assets

---

## Information Response

Returns

- Requested Knowledge Objects
- Related References
- Confidence Score

---

## Status Update

Reports

- Started
- In Progress
- Waiting
- Completed
- Failed

---

## Warning

Reports

- Risk
- Missing Dependencies
- QA Issues
- Policy Violations

---

## Approval Request

Requests

- Human Approval
- Governance Approval
- QA Approval

---

# Message Structure

Every message contains

- Message ID
- Sender
- Receiver
- Timestamp
- Correlation ID
- Task ID
- Message Type
- Payload
- Priority
- Status

---

# Priority Levels

Critical

High

Normal

Low

Background

---

# Communication Modes

## Direct

One agent

↓

One agent

---

## Broadcast

One

↓

Many

---

## Request / Response

Agent A

↓

Agent B

↓

Response

---

## Publish / Subscribe

Agent

↓

Event Bus

↓

Subscribers

---

## Workflow Chain

Story

↓

Prompt

↓

Asset

↓

Runtime

↓

QA

↓

Publisher

---

# Context Sharing

Agents share

- Task Context
- Knowledge References
- Dependency Information
- QA Results
- Execution Reports

Agents never duplicate large datasets.

---

# Event Types

Examples

Task Created

Task Started

Task Completed

Knowledge Updated

QA Passed

QA Failed

Render Finished

Publishing Completed

---

# Failure Handling

Communication failure

↓

Retry

↓

Alternative Route

↓

Escalation

↓

Human Notification

---

# Security

Messages must

✓ Preserve integrity

✓ Respect permissions

✓ Record sender identity

✓ Maintain audit logs

✓ Validate payload

---

# Performance Targets

Average message latency

<100 ms

Task routing

<250 ms

Retry success

>99%

---

# Best Practices

- Keep messages concise.
- Share references instead of raw data.
- Correlate related messages.
- Log every critical exchange.
- Use events for asynchronous workflows.

---

# Related Documents

- AG-001 Agent Architecture
- AG-002 Agent Roles
- AG-004 Agent Memory
- KS-001 Knowledge Graph
- RT-001 Production Orchestrator