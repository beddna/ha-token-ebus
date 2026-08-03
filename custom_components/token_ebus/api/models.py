"""Data models for Token eBUS."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class Register:
    """Definition of one eBUS register."""

    circuit: str
    name: str
    readable: bool = False
    writable: bool = False

    @property
    def key(self) -> str:
        """Return unique register identifier."""
        return f"{self.circuit}/{self.name}"


@dataclass(slots=True)
class RegisterValue:
    """Current register value."""

    register: Register
    value: Any
    timestamp: datetime


@dataclass(slots=True)
class CacheEntry:
    """One entry returned by 'cache -v'."""

    register: Register
    raw_request: str
    raw_response: str
    hits: int
    age_seconds: int
    timestamp: datetime


@dataclass(slots=True)
class DeviceInfo:
    """Basic information about connected Token device."""

    host: str
    port: int
    firmware: str | None = None
    hardware: str | None = None
