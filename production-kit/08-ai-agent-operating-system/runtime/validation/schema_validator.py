"""
Wild Story Lab OS
Module 08 - Validation Runtime
Schema Validator
"""

from __future__ import annotations

from typing import Any


class SchemaValidator:
    """Validates dictionaries against a minimal required-field schema."""

    def validate(self, data: dict[str, Any], required: list[str]) -> bool:
        return all(field in data for field in required)

    def missing_fields(self, data: dict[str, Any], required: list[str]) -> list[str]:
        return [field for field in required if field not in data]

    def assert_valid(self, data: dict[str, Any], required: list[str]) -> None:
        missing = self.missing_fields(data, required)
        if missing:
            raise ValueError(f"Missing required fields: {', '.join(missing)}")
