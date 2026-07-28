"""
Wild Story Lab OS
Module 08 - Validation Runtime
Validation Report
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ValidationReport:
    """Represents the result of a validation run."""

    passed: bool
    timestamp: datetime = field(default_factory=datetime.utcnow)
    checks: dict[str, bool] = field(default_factory=dict)
    messages: list[str] = field(default_factory=list)

    def add_check(self, name: str, result: bool) -> None:
        self.checks[name] = result

    def add_message(self, message: str) -> None:
        self.messages.append(message)

    @property
    def score(self) -> float:
        if not self.checks:
            return 0.0
        return sum(self.checks.values()) / len(self.checks)
