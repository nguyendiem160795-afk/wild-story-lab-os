"""
Wild Story Lab OS
Module 08 - Workflow Engine
Execution Plan
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ExecutionStep:
    """Represents a single executable workflow step."""
    step_id: str
    agent: str
    depends_on: list[str] = field(default_factory=list)
    parameters: dict[str, Any] = field(default_factory=dict)


@dataclass
class ExecutionPlan:
    """Execution plan generated before workflow execution."""
    workflow_id: str
    steps: list[ExecutionStep] = field(default_factory=list)

    def add_step(self, step: ExecutionStep) -> None:
        self.steps.append(step)

    def ordered_steps(self) -> list[ExecutionStep]:
        return list(self.steps)

    def total_steps(self) -> int:
        return len(self.steps)
