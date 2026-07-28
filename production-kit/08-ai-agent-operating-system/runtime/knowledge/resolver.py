"""
Wild Story Lab OS
Module 08 - Prompt Runtime
Variable Resolver
"""

from __future__ import annotations

from typing import Any


class VariableResolver:
    """Resolves runtime variables for prompt rendering."""

    def __init__(self) -> None:
        self._variables: dict[str, Any] = {}

    def register(self, name: str, value: Any) -> None:
        self._variables[name] = value

    def resolve(self, name: str, default: Any = None) -> Any:
        return self._variables.get(name, default)

    def resolve_all(self) -> dict[str, Any]:
        return dict(self._variables)

    def clear(self) -> None:
        self._variables.clear()
