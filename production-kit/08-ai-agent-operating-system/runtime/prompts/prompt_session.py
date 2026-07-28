"""
Wild Story Lab OS
Module 08 - Prompt Runtime
Prompt Session
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from uuid import uuid4


@dataclass
class PromptSession:
    """Represents a prompt execution session."""

    prompt_id: str
    session_id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=datetime.utcnow)
    variables: dict[str, Any] = field(default_factory=dict)
    rendered_prompt: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def set_variable(self, key: str, value: Any) -> None:
        self.variables[key] = value

    def render(self, content: str) -> None:
        self.rendered_prompt = content

    def snapshot(self) -> dict[str, Any]:
        return {
            "session_id": self.session_id,
            "prompt_id": self.prompt_id,
            "created_at": self.created_at.isoformat(),
            "variables": dict(self.variables),
            "rendered_prompt": self.rendered_prompt,
            "metadata": dict(self.metadata),
        }
