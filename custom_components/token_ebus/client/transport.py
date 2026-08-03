"""Transport interfaces for Token eBUS."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Transport(ABC):
    """Abstract communication transport."""

    @abstractmethod
    async def connect(self) -> None:
        """Connect to the device."""

    @abstractmethod
    async def disconnect(self) -> None:
        """Disconnect from the device."""

    @abstractmethod
    async def execute(self, command: str) -> str:
        """Execute a command and return the raw response."""

    @property
    @abstractmethod
    def connected(self) -> bool:
        """Return connection state."""
