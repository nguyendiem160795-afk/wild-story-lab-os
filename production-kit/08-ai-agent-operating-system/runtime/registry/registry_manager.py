"""
Wild Story Lab OS
Module 08 - Registry Engine
Registry Manager
"""

from __future__ import annotations

from .agent_registry import AgentRegistry
from .workflow_registry import WorkflowRegistry
from .prompt_registry import PromptRegistry
from .knowledge_registry import KnowledgeRegistry
from .memory_registry import MemoryRegistry


class RegistryManager:
    """Coordinates all runtime registries."""

    def __init__(self) -> None:
        self.agents = AgentRegistry()
        self.workflows = WorkflowRegistry()
        self.prompts = PromptRegistry()
        self.knowledge = KnowledgeRegistry()
        self.memory = MemoryRegistry()

    def clear_all(self) -> None:
        self.agents.clear()
        self.workflows.clear()
        self.prompts.clear()
        self.knowledge.clear()
        self.memory.clear()

    def summary(self) -> dict[str, int]:
        return {
            "agents": len(self.agents.all()),
            "workflows": len(self.workflows.all()),
            "prompts": len(self.prompts.all()),
            "knowledge": len(self.knowledge.all()),
            "memory": len(self.memory.all()),
        }
