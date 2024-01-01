"""Module Main."""

from contextlib import suppress

from app import app
from routes import *  # noqa: F403
from utilities import read_args_cli

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8080

    if read_args_cli().debug:
        with suppress(KeyboardInterrupt):
            app.run(
                host=host,
                port=port,
                debug=True,
            )
    else:
        from server import Server

        server = Server(
            app=app,
            host=host,
            port=port,
        )

        server.start()
