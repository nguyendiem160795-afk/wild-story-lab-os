"""
Wild Story Lab OS
Module 08 - Workflow Engine
Retry Manager
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RetryPolicy:
    """Configuration for workflow retry behavior."""
    max_attempts: int = 3
    current_attempt: int = 0

    @property
    def remaining(self) -> int:
        return max(0, self.max_attempts - self.current_attempt)


class RetryManager:
    """Controls retry attempts for workflow steps."""

    def __init__(self, policy: RetryPolicy | None = None) -> None:
        self.policy = policy or RetryPolicy()

    def should_retry(self) -> bool:
        return self.policy.current_attempt < self.policy.max_attempts

    def record_failure(self) -> bool:
        self.policy.current_attempt += 1
        return self.should_retry()

    def reset(self) -> None:
        self.policy.current_attempt = 0
