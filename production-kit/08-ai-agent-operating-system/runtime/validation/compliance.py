"""
Wild Story Lab OS
Module 08 - Validation Runtime
Compliance Checker
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ComplianceResult:
    """Compliance evaluation result."""
    compliant: bool
    violations: list[str] = field(default_factory=list)


class ComplianceChecker:
    """Checks runtime compliance against configured rules."""

    def evaluate(self, violations: list[str]) -> ComplianceResult:
        return ComplianceResult(
            compliant=len(violations) == 0,
            violations=list(violations),
        )

    def is_compliant(self, violations: list[str]) -> bool:
        return len(violations) == 0
