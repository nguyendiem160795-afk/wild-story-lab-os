"""
Wild Story Lab OS
Module 08 - SDK & CLI
Main Entry Point
"""

from __future__ import annotations

from .bootstrap import Bootstrap
from .cli import CLI


def main(argv: list[str] | None = None) -> int:
    """Application entry point."""
    cli = CLI()
    args = cli.parse(argv)

    bootstrap = Bootstrap(
        config_path=args.config or "config/runtime.json"
    )
    bootstrap.initialize()

    if args.version:
        print("Wild Story Lab OS Module 08 v1.0.0")
        return 0

    print("Wild Story Lab OS Runtime initialized.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
