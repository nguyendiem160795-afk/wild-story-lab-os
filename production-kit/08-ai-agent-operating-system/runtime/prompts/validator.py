"""
Wild Story Lab OS
Module 08 - Prompt Runtime
Prompt Validator
"""

from __future__ import annotations

import re


class PromptValidator:
    """Validates prompt templates before execution."""

    REQUIRED_PLACEHOLDER = re.compile(r"\{\{([a-zA-Z0-9_]+)\}\}")

    def validate(self, template: str) -> bool:
        if not template or not template.strip():
            return False
        return True

    def placeholders(self, template: str) -> list[str]:
        return self.REQUIRED_PLACEHOLDER.findall(template)

    def has_placeholders(self, template: str) -> bool:
        return len(self.placeholders(template)) > 0
