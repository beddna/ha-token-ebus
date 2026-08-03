"""TCP transport for Token eBUS."""

from __future__ import annotations

import asyncio

from .exceptions import ConnectionError


class TcpTransport:
    """Persistent TCP connection to Token eBUS."""

    def __init__(
        self,
        host: str,
        port: int = 9999,
        timeout: float = 5.0,
    ) -> None:
        self._host = host
        self._port = port
        self._timeout = timeout

        self._reader: asyncio.StreamReader | None = None
        self._writer: asyncio.StreamWriter | None = None

    @property
    def connected(self) -> bool:
        return (
            self._writer is not None
            and not self._writer.is_closing()
        )

    async def connect(self) -> None:
        """Open TCP connection."""

        if self.connected:
            return

        try:
            self._reader, self._writer = await asyncio.wait_for(
                asyncio.open_connection(
                    self._host,
                    self._port,
                ),
                timeout=self._timeout,
            )

        except Exception as err:
            raise ConnectionError(str(err)) from err

    async def disconnect(self) -> None:
        """Close TCP connection."""

        if self._writer is None:
            return

        self._writer.close()
        await self._writer.wait_closed()

        self._reader = None
        self._writer = None

    async def execute(self, command: str) -> str:
        """Execute one command."""

        if not self.connected:
            await self.connect()

        assert self._writer is not None
        assert self._reader is not None

        self._writer.write(f"{command}\n".encode())

        await self._writer.drain()

        data = await asyncio.wait_for(
            self._reader.readuntil(b"\n"),
            timeout=self._timeout,
        )

        return data.decode().strip()
