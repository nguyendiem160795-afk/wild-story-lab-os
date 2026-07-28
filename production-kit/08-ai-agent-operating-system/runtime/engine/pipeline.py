"""
Wild Story Lab OS
Module 08 - Workflow Engine
Pipeline
"""

from __future__ import annotations

from typing import Any


class Pipeline:
    """Sequential workflow execution pipeline."""

    def __init__(self) -> None:
        self._steps: list[dict[str, Any]] = []

    def add_step(self, step: dict[str, Any]) -> None:
        self._steps.append(step)

    def steps(self) -> list[dict[str, Any]]:
        return list(self._steps)

    def execute(self) -> list[dict[str, Any]]:
        results = []
        for step in self._steps:
            results.append(
                {
                    "step": step.get("id"),
                    "status": "completed",
                }
            )
        return results

    def clear(self) -> None:
        self._steps.clear()
