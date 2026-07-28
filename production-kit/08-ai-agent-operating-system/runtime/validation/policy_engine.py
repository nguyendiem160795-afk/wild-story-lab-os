"""
Wild Story Lab OS
Module 08 - Validation Runtime
Policy Engine
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class ValidationPolicy:
    name: str
    rule: Callable[[dict[str, Any]], bool]
    description: str = ""


class PolicyEngine:
    """Executes registered validation policies."""

    def __init__(self) -> None:
        self._policies: dict[str, ValidationPolicy] = {}

    def register(self, policy: ValidationPolicy) -> None:
        self._policies[policy.name] = policy

    def validate(self, data: dict[str, Any]) -> dict[str, bool]:
        return {name: policy.rule(data) for name, policy in self._policies.items()}

    def passed(self, data: dict[str, Any]) -> bool:
        return all(self.validate(data).values())

    def clear(self) -> None:
        self._policies.clear()
