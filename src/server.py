"""Module Server Prod."""

from __future__ import annotations

from signal import SIGINT, signal
from typing import TYPE_CHECKING

from gevent.pywsgi import WSGIServer

from tools import logger

if TYPE_CHECKING:
    from types import Any, FrameType

    from flask import Flask


class Server:
    """Interface representing the server."""

    def __init__(
        self: Server,
        app: Flask,
        host: str,
        port: int,
        **options: dict[str, Any],
    ) -> None:
        self.server = WSGIServer(
            application=app,
            listener=(host, port),
            **options,
        )

    def stop_handler(
        self: Server,
        code: int,
        frame: FrameType,
    ) -> None:
        """Handle signal to stop server.

        Parameters
        ----------
        code : int
            The signal code.
        frame : FrameType
            The signal frame.
        """
        logger.debug_(msg=f"CODE {code} - FRAME {frame}.")

        self.stop()

    def stop(self: Server) -> None:
        """Stop the server."""
        logger.trace_(msg="Stop Server!")

        self.server.stop()
        self.server.close()

    def start(self: Server) -> None:
        """Start the server."""
        logger.trace_(msg="Start Server!")

        signal(
            signalnum=SIGINT,
            handler=self.stop_handler,
        )

        self.server.serve_forever()
