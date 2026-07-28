"""
Wild Story Lab OS
Module 08 - SDK & CLI
CLI
"""

from __future__ import annotations

import argparse


class CLI:
    """Command-line interface."""

    def build(self) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(prog="wsl")
        parser.add_argument("--version", action="store_true", help="Show version")
        parser.add_argument("--config", type=str, default=None, help="Config file")
        return parser

    def parse(self, args: list[str] | None = None):
        return self.build().parse_args(args)
