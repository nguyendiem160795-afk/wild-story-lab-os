"""
Wild Story Lab OS
Module 08 - Prompt Runtime
Template Engine
"""

from __future__ import annotations

from typing import Any

from .renderer import PromptRenderer
from .resolver import VariableResolver
from .validator import PromptValidator


class TemplateEngine:
    """High-level engine for validating and rendering prompt templates."""

    def __init__(self) -> None:
        self.renderer = PromptRenderer()
        self.resolver = VariableResolver()
        self.validator = PromptValidator()

    def render(self, template: str, variables: dict[str, Any]) -> str:
        if not self.validator.validate(template):
            raise ValueError("Invalid prompt template.")
        for key, value in variables.items():
            self.resolver.register(key, value)
        return self.renderer.render(template, self.resolver.resolve_all())
