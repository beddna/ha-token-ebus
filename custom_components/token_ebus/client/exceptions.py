"""Exceptions for Token eBUS client."""


class TokenEBusError(Exception):
    """Base exception for Token eBUS."""


class ConnectionError(TokenEBusError):
    """Connection to Token device failed."""


class ProtocolError(TokenEBusError):
    """Unexpected protocol response."""


class ParseError(TokenEBusError):
    """Parser failed to decode response."""


class AuthenticationError(TokenEBusError):
    """Authentication failed."""


class TimeoutError(TokenEBusError):
    """Command timeout."""
