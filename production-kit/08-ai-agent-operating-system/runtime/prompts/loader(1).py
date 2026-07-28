"""
Wild Story Lab OS
Module 08 - Registry Engine
Component Loader
"""

from __future__ import annotations

import importlib
from types import ModuleType


class ComponentLoader:
    """Loads runtime components dynamically."""

    def __init__(self) -> None:
        self._modules: dict[str, ModuleType] = {}

    def load(self, module_name: str) -> ModuleType:
        """Load a Python module by name."""
        module = importlib.import_module(module_name)
        self._modules[module_name] = module
        return module

    def is_loaded(self, module_name: str) -> bool:
        return module_name in self._modules

    def unload(self, module_name: str) -> None:
        self._modules.pop(module_name, None)

    def loaded_modules(self) -> list[str]:
        return sorted(self._modules.keys())

    def clear(self) -> None:
        self._modules.clear()
