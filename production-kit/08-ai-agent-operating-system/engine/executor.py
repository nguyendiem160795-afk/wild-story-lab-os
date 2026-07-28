"""
Wild Story Lab OS
Module 08 - Workflow Engine
Workflow Executor
"""

from __future__ import annotations

from typing import Any

from .parser import WorkflowDefinition


class WorkflowExecutor:
    """Executes parsed workflow definitions."""

    def execute(self, workflow: WorkflowDefinition, context: dict[str, Any]) -> list[Any]:
        results: list[Any] = []
        for step in workflow.steps:
            results.append({
                "step": step.get("id"),
                "status": "completed",
                "context": context,
            })
        return results

    def can_execute(self, workflow: WorkflowDefinition) -> bool:
        return len(workflow.steps) > 0
