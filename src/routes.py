"""Module Routes."""

from __future__ import annotations

from app import app
from controller import controller
from flask import jsonify, render_template, request
from utilities import (
    BREAKPOINTS,
    BROWSERS,
    DEIVCES,
    SYSTEMS,
)


@app.route("/")
def route_index() -> str:
    """Render the application index page."""
    return render_template(
        "index.jinja",
        context={
            "breakpoints": BREAKPOINTS,
            "browsers": BROWSERS,
            "devices": DEIVCES,
            "systems": SYSTEMS,
        },
    )


@app.route("/api/browser/start", methods=["POST"])
def start_browser() -> str:
    """Start the web browser."""
    controller.setup(**request.form.to_dict())
    controller.start()

    return jsonify("api_driver_start!")


@app.route("/api/browser/stop")
def stop_browser() -> str:
    """Stop the web browser."""
    controller.stop()

    return jsonify("api_driver_stop!")
