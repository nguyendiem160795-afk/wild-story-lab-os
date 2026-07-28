"""
Wild Story Lab OS
Module 08 - Workflow Engine
Dependency Resolver
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any


class DependencyResolver:
    """Resolves workflow step dependencies."""

    def build_graph(self, steps: list[dict[str, Any]]) -> dict[str, list[str]]:
        graph: dict[str, list[str]] = defaultdict(list)
        for step in steps:
            step_id = step["id"]
            for dep in step.get("depends_on", []):
                graph[dep].append(step_id)
            graph.setdefault(step_id, [])
        return dict(graph)

    def ready_steps(
        self,
        steps: list[dict[str, Any]],
        completed: set[str],
    ) -> list[dict[str, Any]]:
        ready = []
        for step in steps:
            deps = set(step.get("depends_on", []))
            if deps.issubset(completed):
                ready.append(step)
        return ready
