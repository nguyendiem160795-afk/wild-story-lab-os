"""
Wild Story Lab OS
Module 08 - SDK & CLI
Client
"""

from __future__ import annotations

from typing import Any

from .sdk import SDKClient


class Client:
    """Convenience wrapper around SDKClient."""

    def __init__(self) -> None:
        self.sdk = SDKClient()

    def connect(self, name: str, service: Any) -> None:
        self.sdk.register(name, service)

    def service(self, name: str) -> Any:
        return self.sdk.get(name)

    def available(self) -> list[str]:
        return self.sdk.services()
