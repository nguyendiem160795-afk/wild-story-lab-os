"""
Wild Story Lab OS
Module 08 - Memory Runtime
Retention Policy
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class RetentionPolicy:
    """Retention policy for runtime memory artifacts."""

    max_age_days: int = 30

    def is_expired(self, created_at: datetime) -> bool:
        return datetime.utcnow() > created_at + timedelta(days=self.max_age_days)

    def expires_at(self, created_at: datetime) -> datetime:
        return created_at + timedelta(days=self.max_age_days)


class RetentionManager:
    """Evaluates retention rules for stored memory."""

    def __init__(self, policy: RetentionPolicy | None = None) -> None:
        self.policy = policy or RetentionPolicy()

    def should_delete(self, created_at: datetime) -> bool:
        return self.policy.is_expired(created_at)
