"""
Wild Story Lab OS
Module 08 - Memory Runtime
Serializer
"""

from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from typing import Any


class MemorySerializer:
    """Serializes and deserializes runtime memory objects."""

    def serialize(self, obj: Any) -> str:
        if is_dataclass(obj):
            obj = asdict(obj)
        return json.dumps(obj, ensure_ascii=False, indent=2)

    def deserialize(self, payload: str) -> Any:
        return json.loads(payload)

    def to_bytes(self, obj: Any) -> bytes:
        return self.serialize(obj).encode("utf-8")

    def from_bytes(self, payload: bytes) -> Any:
        return self.deserialize(payload.decode("utf-8"))
