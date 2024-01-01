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

from tools import logger


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
    options = request.form.to_dict()

    logger.info_(msg=f"OPTIONS {options}")

    controller.start(**options)

    return jsonify("api_driver_start!")


@app.route("/api/browser/stop")
def stop_browser() -> str:
    """Stop the web browser."""
    controller.stop()

    logger.info_(msg=f"DRIVER {controller.driver}")

    return jsonify("api_driver_stop!")
