---
document_id: GL-005
module: 01
category: Glossary
title: AI Terms (Thuật ngữ Trí tuệ Nhân tạo)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# AI Terms (Thuật ngữ Trí tuệ Nhân tạo)

> Official artificial intelligence terminology dictionary for the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This glossary defines artificial intelligence terminology used throughout EAOSS.

The purpose is to establish a shared language for:

- AI architecture.
- AI systems.
- AI agents.
- Knowledge management.
- AI-assisted workflows.

---

# 2. Artificial Intelligence (AI)

## Vietnamese:
Trí tuệ nhân tạo

## Definition:

Artificial Intelligence is the capability of computer systems to perform tasks that normally require human intelligence.

Examples:

- Reasoning.
- Learning.
- Understanding language.
- Generating content.
- Decision support.

---

# 3. AI System

## Vietnamese:
Hệ thống AI

## Definition:

An AI System is a system that uses artificial intelligence capabilities to perform specific tasks or provide intelligent services.

Components may include:

- Models.
- Data.
- Agents.
- Tools.
- Evaluation systems.

---

# 4. AI Model

## Vietnamese:
Mô hình AI

## Definition:

An AI Model is a computational model trained to recognize patterns, generate outputs, or perform intelligent tasks.

Examples:

- Language models.
- Vision models.
- Embedding models.

---

# 5. Large Language Model (LLM)

## Vietnamese:
Mô hình ngôn ngữ lớn

## Definition:

An LLM is an AI model trained on large amounts of text data to understand and generate natural language.

Capabilities:

- Text generation.
- Summarization.
- Reasoning assistance.
- Language understanding.

---

# 6. AI Agent

## Vietnamese:
Tác nhân AI

## Definition:

An AI Agent is an autonomous or semi-autonomous AI system that can:

- Receive goals.
- Reason about tasks.
- Use tools.
- Execute actions.
- Produce results.

Basic structure:

```text
Goal
 ↓
Reasoning
 ↓
Action
 ↓
Feedback
```

---

# 7. Agent Framework

## Vietnamese:
Khung tác nhân AI

## Definition:

An Agent Framework provides the architecture and mechanisms for building, managing, and operating AI Agents.

Includes:

- Agent logic.
- Tool usage.
- Memory.
- Planning.
- Evaluation.

---

# 8. Prompt

## Vietnamese:
Câu lệnh / yêu cầu cho AI

## Definition:

A Prompt is an instruction or input provided to an AI model to guide its response.

A prompt may contain:

- Goal.
- Context.
- Constraints.
- Expected output format.

---

# 9. Prompt Engineering

## Vietnamese:
Kỹ thuật thiết kế Prompt

## Definition:

Prompt Engineering is the practice of designing effective instructions to achieve reliable AI outputs.

Includes:

- Role definition.
- Context design.
- Constraint setting.
- Output formatting.

---

# 10. Context

## Vietnamese:
Ngữ cảnh

## Definition:

Context is information provided to an AI system to help it understand the situation and generate relevant outputs.

Examples:

- Previous messages.
- Documents.
- Knowledge sources.
- Instructions.

---

# 11. Context Window

## Vietnamese:
Cửa sổ ngữ cảnh

## Definition:

Context Window is the amount of information an AI model can process at one time.

---

# 12. Memory

## Vietnamese:
Bộ nhớ AI

## Definition:

Memory allows AI systems to retain and use information across interactions.

Types:

- Short-term memory.
- Long-term memory.
- External knowledge memory.

---

# 13. Knowledge Base

## Vietnamese:
Cơ sở tri thức AI

## Definition:

A Knowledge Base is an organized collection of information used by AI systems for retrieval and reasoning.

Examples:

- Documents.
- Rules.
- Metadata.
- Structured knowledge.

---

# 14. Retrieval-Augmented Generation (RAG)

## Vietnamese:
Sinh tăng cường truy xuất

## Definition:

RAG is an AI architecture pattern that combines retrieval systems with generation models.

Process:

```text
User Query
    ↓
Retrieve Knowledge
    ↓
Generate Response
```

Benefits:

- Better accuracy.
- Updated knowledge.
- Reduced hallucination.

---

# 15. Embedding

## Vietnamese:
Biểu diễn vector

## Definition:

Embedding converts information into numerical representations that capture semantic meaning.

Used for:

- Similarity search.
- Knowledge retrieval.
- AI memory.

---

# 16. Vector Database

## Vietnamese:
Cơ sở dữ liệu vector

## Definition:

A Vector Database stores and retrieves embedding representations.

Purpose:

- Semantic search.
- Knowledge retrieval.
- AI applications.

---

# 17. AI Workflow

## Vietnamese:
Luồng làm việc AI

## Definition:

An AI Workflow defines the sequence of steps performed by AI systems and supporting processes.

Example:

```text
Input
 ↓
Processing
 ↓
AI Reasoning
 ↓
Validation
 ↓
Output
```

---

# 18. Tool Calling

## Vietnamese:
Gọi công cụ

## Definition:

Tool Calling allows AI systems to interact with external capabilities.

Examples:

- APIs.
- Databases.
- Automation tools.

---

# 19. Human-in-the-loop (HITL)

## Vietnamese:
Con người trong vòng kiểm soát

## Definition:

A design approach where humans review, approve, or guide AI decisions.

Purpose:

- Quality control.
- Safety.
- Accountability.

---

# 20. AI Evaluation

## Vietnamese:
Đánh giá AI

## Definition:

AI Evaluation measures the quality, reliability, safety, and performance of AI systems.

Evaluation areas:

- Accuracy.
- Consistency.
- Safety.
- Usefulness.

---

# 21. Hallucination

## Vietnamese:
Ảo giác AI

## Definition:

Hallucination occurs when an AI system generates information that is incorrect, unsupported, or invented.

Prevention:

- Better context.
- Knowledge retrieval.
- Validation.

---

# 22. AI Governance

## Vietnamese:
Quản trị AI

## Definition:

AI Governance defines rules, responsibilities, and controls for developing and operating AI systems.

Includes:

- Safety.
- Ethics.
- Security.
- Accountability.

---

# 23. AI Quality Checklist

| Requirement | Mandatory |
|---|---|
| Term defined | Yes |
| Vietnamese meaning included | Yes |
| AI context explained | Yes |
| Related concepts mapped | Yes |

---

# 24. References

- GL-001 Core Terms
- POL-006 Security Policy
- POL-007 Access Control Policy
- POL-008 Data Management Policy
- TMP-007 ADR Template

---

# 25. Revision History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-07-23 | Initial AI Terms Glossary |

---

# End of Document