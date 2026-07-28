"""
Wild Story Lab OS
Module 08 - SDK & CLI
SDK Client
"""

from __future__ import annotations

from typing import Any


class SDKClient:
    """High-level SDK entry point."""

    def __init__(self) -> None:
        self._services: dict[str, Any] = {}

    def register(self, name: str, service: Any) -> None:
        self._services[name] = service

    def get(self, name: str) -> Any:
        return self._services[name]

    def services(self) -> list[str]:
        return sorted(self._services.keys())
