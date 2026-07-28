"""
Wild Story Lab OS
Module 08 - Workflow Engine
Execution Result
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class ExecutionResult:
    """Represents the outcome of a workflow execution."""

    workflow_id: str
    success: bool
    started_at: datetime
    finished_at: datetime
    outputs: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)

    @property
    def duration_seconds(self) -> float:
        return (self.finished_at - self.started_at).total_seconds()

    def add_output(self, key: str, value: Any) -> None:
        self.outputs[key] = value

    def add_error(self, message: str) -> None:
        self.errors.append(message)
