"""
Wild Story Lab OS
Module 08 - Validation Runtime
Quality Gate
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class QualityGateResult:
    """Result of a quality gate evaluation."""
    passed: bool
    score: float
    message: str = ""


class QualityGate:
    """Evaluates quality thresholds before runtime execution."""

    def __init__(self, minimum_score: float = 0.8) -> None:
        self.minimum_score = minimum_score

    def evaluate(self, score: float) -> QualityGateResult:
        passed = score >= self.minimum_score
        return QualityGateResult(
            passed=passed,
            score=score,
            message="Passed" if passed else "Failed",
        )
