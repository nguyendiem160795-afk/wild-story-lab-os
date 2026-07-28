"""
Wild Story Lab OS
Module 08 - SDK & CLI
Bootstrap
"""

from __future__ import annotations

from .client import Client
from .config import Config


class Bootstrap:
    """Initializes the SDK runtime."""

    def __init__(self, config_path: str):
        self.config = Config(config_path)
        self.client = Client()

    def initialize(self) -> Client:
        self.config.load()
        return self.client

    def shutdown(self) -> None:
        pass
