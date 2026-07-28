"""
Wild Story Lab OS
Module 08 - Telemetry
Tracer
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass(slots=True)
class Trace:
    """Represents a traced runtime operation."""

    operation: str
    trace_id: str = field(default_factory=lambda: str(uuid4()))
    started_at: datetime = field(default_factory=datetime.utcnow)
    finished_at: datetime | None = None

    def finish(self) -> None:
        self.finished_at = datetime.utcnow()


class Tracer:
    """Creates and manages runtime traces."""

    def __init__(self) -> None:
        self._traces: dict[str, Trace] = {}

    def start(self, operation: str) -> Trace:
        trace = Trace(operation=operation)
        self._traces[trace.trace_id] = trace
        return trace

    def finish(self, trace_id: str) -> None:
        if trace_id in self._traces:
            self._traces[trace_id].finish()

    def traces(self) -> list[Trace]:
        return list(self._traces.values())
