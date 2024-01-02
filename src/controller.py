"""Module Controller."""

from __future__ import annotations

from typing import TYPE_CHECKING

from utilities import PATH_DRIVERS, Drivers

if TYPE_CHECKING:
    from pathlib import Path

    from selenium.webdriver.chrome.webdriver import WebDriver


class Controller:
    """Interface representing the controller."""

    def __init__(self: Controller, path_drivers: Path) -> None:
        self.browsers = {}
        self.drivers = Drivers(path_drivers=path_drivers)

    def driver(
        self: Controller,
        browser: str,
    ) -> WebDriver:
        if browser not in self.browsers:
            driver = self.drivers[browser]
            self.browsers[browser] = driver()

        return self.browsers.get(browser)


controller = Controller(path_drivers=PATH_DRIVERS)
