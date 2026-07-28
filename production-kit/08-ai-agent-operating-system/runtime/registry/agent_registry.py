"""
Wild Story Lab OS
Module 08 - Registry Engine
Agent Registry
"""

from __future__ import annotations

from typing import Any


class AgentRegistry:
    """Registry responsible for executable runtime agents."""

    def __init__(self) -> None:
        self._agents: dict[str, Any] = {}

    def register(self, agent_id: str, agent: Any) -> None:
        if agent_id in self._agents:
            raise ValueError(f"Agent '{agent_id}' is already registered.")
        self._agents[agent_id] = agent

    def unregister(self, agent_id: str) -> None:
        self._agents.pop(agent_id, None)

    def resolve(self, agent_id: str) -> Any:
        return self._agents.get(agent_id)

    def exists(self, agent_id: str) -> bool:
        return agent_id in self._agents

    def all(self) -> dict[str, Any]:
        return dict(self._agents)

    def clear(self) -> None:
        self._agents.clear()
