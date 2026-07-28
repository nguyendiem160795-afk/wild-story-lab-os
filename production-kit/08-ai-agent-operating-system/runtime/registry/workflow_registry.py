"""
Wild Story Lab OS
Module 08 - Registry Engine
Workflow Registry
"""

from __future__ import annotations

from typing import Any


class WorkflowRegistry:
    """Registry responsible for executable runtime workflows."""

    def __init__(self) -> None:
        self._workflows: dict[str, Any] = {}

    def register(self, workflow_id: str, workflow: Any) -> None:
        if workflow_id in self._workflows:
            raise ValueError(f"Workflow '{workflow_id}' is already registered.")
        self._workflows[workflow_id] = workflow

    def unregister(self, workflow_id: str) -> None:
        self._workflows.pop(workflow_id, None)

    def resolve(self, workflow_id: str) -> Any:
        return self._workflows.get(workflow_id)

    def exists(self, workflow_id: str) -> bool:
        return workflow_id in self._workflows

    def all(self) -> dict[str, Any]:
        return dict(self._workflows)

    def clear(self) -> None:
        self._workflows.clear()
