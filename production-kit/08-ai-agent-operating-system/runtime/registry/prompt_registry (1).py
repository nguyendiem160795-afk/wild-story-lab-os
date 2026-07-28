"""
Wild Story Lab OS
Module 08 - Registry Engine
Prompt Registry
"""

from __future__ import annotations

from typing import Any


class PromptRegistry:
    """Registry responsible for runtime prompt templates."""

    def __init__(self) -> None:
        self._prompts: dict[str, Any] = {}

    def register(self, prompt_id: str, prompt: Any) -> None:
        if prompt_id in self._prompts:
            raise ValueError(f"Prompt '{prompt_id}' is already registered.")
        self._prompts[prompt_id] = prompt

    def unregister(self, prompt_id: str) -> None:
        self._prompts.pop(prompt_id, None)

    def resolve(self, prompt_id: str) -> Any:
        return self._prompts.get(prompt_id)

    def exists(self, prompt_id: str) -> bool:
        return prompt_id in self._prompts

    def all(self) -> dict[str, Any]:
        return dict(self._prompts)

    def clear(self) -> None:
        self._prompts.clear()
