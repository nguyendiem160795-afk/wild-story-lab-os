"""
Wild Story Lab OS
Module 08 - Memory Runtime
Project Memory
"""

from __future__ import annotations

from typing import Any


class ProjectMemory:
    """Persistent in-memory store shared across workflows in a project."""

    def __init__(self) -> None:
        self._projects: dict[str, dict[str, Any]] = {}

    def set(self, project_id: str, key: str, value: Any) -> None:
        self._projects.setdefault(project_id, {})[key] = value

    def get(self, project_id: str, key: str, default: Any = None) -> Any:
        return self._projects.get(project_id, {}).get(key, default)

    def snapshot(self, project_id: str) -> dict[str, Any]:
        return dict(self._projects.get(project_id, {}))

    def clear(self, project_id: str | None = None) -> None:
        if project_id is None:
            self._projects.clear()
        else:
            self._projects.pop(project_id, None)
