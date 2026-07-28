"""
Wild Story Lab OS
Module 08 - Prompt Runtime
Prompt Renderer
"""

from __future__ import annotations

from typing import Any


class PromptRenderer:
    """Renders prompt templates using runtime variables."""

    def render(self, template: str, variables: dict[str, Any]) -> str:
        result = template
        for key, value in variables.items():
            result = result.replace(f"{{{{{key}}}}}", str(value))
        return result

    def validate(self, template: str) -> bool:
        return isinstance(template, str) and len(template) > 0
