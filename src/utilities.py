"""Module Utilities."""

from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path
from typing import TYPE_CHECKING, Any, Hashable, NamedTuple

import pandas as pd
from selenium import webdriver
from selenium.webdriver import (
    ChromeOptions,
    ChromeService,
    EdgeOptions,
    EdgeService,
    FirefoxOptions,
    FirefoxService,
    IeOptions,
    IeService,
    SafariOptions,
    SafariService,
)

from tools import logger

if TYPE_CHECKING:
    from argparse import Namespace

    from selenium.webdriver.chrome.webdriver import WebDriver


class Breakpoint(NamedTuple):
    """Interface representing a breakpoint."""

    name: str
    width: float
    height: float


class Device(NamedTuple):
    """Interface representing a device."""

    name: str
    category: str
    width: float
    height: float


class Drivers:
    """Interface representing the drivers."""

    def __init__(
        self: Drivers,
        path_drivers: str | Path,
    ) -> None:
        self.path_drivers = Path(path_drivers)

    def launch(
        self: Drivers,
        browser: str,
    ) -> WebDriver:
        """Launch the browser web driver.

        Parameters
        ----------
        browser : str
            The browser to launch.

        Returns
        -------
        WebDriver
            The browser web driver.
        """
        callback = None

        match browser:
            case "chrome":
                callback = self.chrome
            case "edge":
                callback = self.edge
            case "explorer":
                callback = self.explorer
            case "firefox":
                callback = self.firefox
            case "opera":
                callback = self.opera
            case "safari":
                callback = self.safari
            case _:
                logger.warn_(msg=f"Unknown Browser {browser}.")
                logger.info_(msg="Launching driver for Chrome instead.")
                callback = self.chrome

        return callback()

    def chrome(self: Drivers) -> WebDriver:
        options = ChromeOptions()
        service = ChromeService()
        # Use without executable path to driver or it crash
        # path = self.path_drivers / "chrome.exe"  # noqa: ERA001
        # service = ChromeService(executable_path=path)  # noqa: ERA001
        return webdriver.Chrome(options=options, service=service)

    def edge(self: Drivers) -> WebDriver:
        options = EdgeOptions()
        service = EdgeService(executable_path=self.path_drivers / "edge.exe")
        return webdriver.Edge(options=options, service=service)

    def explorer(self: Drivers) -> WebDriver:
        options = IeOptions()
        service = IeService(executable_path=self.path_drivers / "explorer.exe")
        return webdriver.Ie(options=options, service=service)

    def firefox(self: Drivers) -> WebDriver:
        options = FirefoxOptions()
        service = FirefoxService(executable_path=self.path_drivers / "firefox.exe")
        return webdriver.Firefox(options=options, service=service)

    def opera(self: Drivers) -> WebDriver:
        options = ChromeOptions()
        service = ChromeService(executable_path=self.path_drivers / "opera.exe")
        return webdriver.Chrome(options=options, service=service)

    def safari(self: Drivers) -> WebDriver:
        options = SafariOptions()
        service = SafariService()
        return webdriver.Safari(options=options, service=service)


class Options(NamedTuple):
    """Interface representing the options."""

    url: str
    host: str
    port: str
    browser: str
    display: str
    breakpoint: str  # noqa: A003
    device: str
    width: str
    height: str


def read_args_cli() -> Namespace:
    """Read the command line arguments."""
    parser = ArgumentParser()
    parser.add_argument(
        "--debug",
        action="store_true",
        dest="debug",
        default=False,
        required=False,
    )
    return parser.parse_args()


def read_csv_records(path: str) -> list[dict[Hashable, Any]]:
    """Read a CSV file data as a list of records.

    Parameters
    ----------
    path : str
        The path to the CSV file.

    Returns
    -------
    list[dict[Hashable, Any]]
        The list of records.
    """
    return pd.read_csv(path).to_dict("records")


def load_breakpoints() -> list[Breakpoint]:
    """Load the breakpoints data."""
    return [
        Breakpoint(**record)
        for record in read_csv_records(path=PATH_DATA / "breakpoints.csv")
    ]


def load_devices() -> list[Breakpoint]:
    """Load the breakpoints data."""
    return [
        Device(**record) for record in read_csv_records(path=PATH_DATA / "devices.csv")
    ]


"""from win32api import EnumDisplayMonitors, GetMonitorInfo, GetSystemMetrics"""
"""def position_window_center(height: str, width: str):
    window_height = int(height)
    window_width = int(width)

    screen_width = GetSystemMetrics(0)
    screen_height = GetSystemMetrics(1)

    x = screen_width / 2 - window_width / 2
    y = screen_height / 2 - window_height / 2

    return x, y


def test_window():
    enum = EnumDisplayMonitors()

    logger.info_(msg=f"ENUM {enum}")

    handle1, handle2, rest = enum[0]

    logger.info_(f"HANDLE1 {handle1}")
    logger.info_(f"MONITOR2 {GetMonitorInfo(handle1)}")
    logger.info_(f"REST {rest}")

    for e in enum:
        logger.info_(msg=f"E {e}")
        info = GetMonitorInfo(e[0])
        logger.info_(msg=f"INFO {info}")"""


PATH_DATA = Path.cwd() / "src/data"
PATH_DRIVERS = Path("C:/Tools/browser-drivers")
BREAKPOINTS = load_breakpoints()
DEIVCES = load_devices()
BROWSERS = [
    "chrome",
    "edge",
    "explorer",
    "firefox",
    "opera",
    "safari",
]
SYSTEMS = [
    "iOS",
    "Linux",
    "Windows",
]
