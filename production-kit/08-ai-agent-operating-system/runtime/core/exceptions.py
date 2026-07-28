"""
Wild Story Lab OS
Module 08 - Runtime Exceptions
"""

from __future__ import annotations


class RuntimeErrorBase(Exception):
    """Base exception for the Wild Story Lab runtime."""


class AgentRegistrationError(RuntimeErrorBase):
    """Raised when agent registration fails."""


class WorkflowExecutionError(RuntimeErrorBase):
    """Raised when workflow execution fails."""


class ValidationError(RuntimeErrorBase):
    """Raised when validation fails."""


class RegistryError(RuntimeErrorBase):
    """Raised when registry operations fail."""


class ContextError(RuntimeErrorBase):
    """Raised when runtime context is invalid."""


class SessionError(RuntimeErrorBase):
    """Raised when session management fails."""


class ConfigurationError(RuntimeErrorBase):
    """Raised when runtime configuration is invalid."""


class PluginError(RuntimeErrorBase):
    """Raised when a plugin cannot be loaded or executed."""
