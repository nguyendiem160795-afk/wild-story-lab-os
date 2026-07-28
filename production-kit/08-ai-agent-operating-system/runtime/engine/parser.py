"""
Wild Story Lab OS
Module 08 - Workflow Engine
Workflow Parser
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class WorkflowDefinition:
    """Represents a parsed workflow definition."""

    workflow_id: str
    name: str
    steps: list[dict[str, Any]] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


class WorkflowParser:
    """Parses workflow specifications into runtime objects."""

    def parse(self, data: dict[str, Any]) -> WorkflowDefinition:
        return WorkflowDefinition(
            workflow_id=data["workflow_id"],
            name=data.get("name", data["workflow_id"]),
            steps=data.get("steps", []),
            metadata=data.get("metadata", {}),
        )

    def validate(self, workflow: WorkflowDefinition) -> bool:
        return bool(workflow.workflow_id and workflow.steps)
