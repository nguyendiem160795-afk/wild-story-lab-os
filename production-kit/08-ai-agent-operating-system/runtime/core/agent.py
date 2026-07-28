"""
Wild Story Lab OS
Module 08 - Runtime Core
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass
class ExecutionContext:
    """Shared runtime context passed between agents."""
    session_id: str
    workflow_id: str
    state: dict[str, Any] = field(default_factory=dict)


class Agent(ABC):
    """Base class for all executable runtime agents."""

    def __init__(self, agent_id: str, name: str):
        self.agent_id = agent_id
        self.name = name

    @abstractmethod
    def execute(self, context: ExecutionContext) -> Any:
        """Execute the agent."""
        raise NotImplementedError
