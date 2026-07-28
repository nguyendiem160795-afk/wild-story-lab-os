"""
Wild Story Lab OS
Module 08 - Runtime Lifecycle
"""

from __future__ import annotations

from enum import Enum
from typing import Callable


class LifecycleState(str, Enum):
    INITIALIZED = "initialized"
    READY = "ready"
    RUNNING = "running"
    PAUSED = "paused"
    STOPPED = "stopped"
    FAILED = "failed"


class LifecycleManager:
    """Manages runtime lifecycle transitions."""

    def __init__(self) -> None:
        self.state = LifecycleState.INITIALIZED
        self._callbacks: dict[LifecycleState, list[Callable[[], None]]] = {}

    def transition(self, state: LifecycleState) -> None:
        self.state = state
        for callback in self._callbacks.get(state, []):
            callback()

    def on(self, state: LifecycleState, callback: Callable[[], None]) -> None:
        self._callbacks.setdefault(state, []).append(callback)

    @property
    def is_running(self) -> bool:
        return self.state == LifecycleState.RUNNING

    @property
    def is_ready(self) -> bool:
        return self.state == LifecycleState.READY
