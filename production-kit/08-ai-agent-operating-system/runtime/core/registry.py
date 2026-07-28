"""
Wild Story Lab OS
Module 08 - Runtime Registry
"""

from __future__ import annotations

from typing import Any


class RuntimeRegistry:
    """Central registry for runtime components."""

    def __init__(self) -> None:
        self._components: dict[str, Any] = {}

    def register(self, component_id: str, component: Any) -> None:
        if component_id in self._components:
            raise ValueError(f"Component '{component_id}' is already registered.")
        self._components[component_id] = component

    def unregister(self, component_id: str) -> None:
        self._components.pop(component_id, None)

    def resolve(self, component_id: str) -> Any:
        return self._components.get(component_id)

    def exists(self, component_id: str) -> bool:
        return component_id in self._components

    def list(self) -> list[str]:
        return sorted(self._components.keys())

    def clear(self) -> None:
        self._components.clear()
