"""
Wild Story Lab OS
Module 08 - Runtime Core Context
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class RuntimeContext:
    """Shared runtime context for workflow execution."""

    session_id: str
    workflow_id: str
    agent_id: str | None = None
    variables: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)
    artifacts: dict[str, Any] = field(default_factory=dict)

    def set(self, key: str, value: Any) -> None:
        self.variables[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self.variables.get(key, default)

    def has(self, key: str) -> bool:
        return key in self.variables

    def update(self, values: dict[str, Any]) -> None:
        self.variables.update(values)

    def snapshot(self) -> dict[str, Any]:
        return {
            "session_id": self.session_id,
            "workflow_id": self.workflow_id,
            "agent_id": self.agent_id,
            "variables": self.variables.copy(),
            "metadata": self.metadata.copy(),
            "artifacts": self.artifacts.copy(),
        }
