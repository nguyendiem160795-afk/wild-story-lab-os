"""
Wild Story Lab OS
Module 08 - Validation Runtime
Security Validator
"""

from __future__ import annotations

from typing import Any


class SecurityValidator:
    """Performs basic runtime security validation."""

    def validate(self, data: dict[str, Any]) -> bool:
        return not self.find_unsafe_keys(data)

    def find_unsafe_keys(self, data: dict[str, Any]) -> list[str]:
        blocked = {"password", "secret", "token", "private_key"}
        return [k for k in data.keys() if k.lower() in blocked]

    def assert_secure(self, data: dict[str, Any]) -> None:
        unsafe = self.find_unsafe_keys(data)
        if unsafe:
            raise ValueError(f"Unsafe keys detected: {', '.join(unsafe)}")
