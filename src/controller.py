"""Module Controller."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from utilities import PATH_DRIVERS, Drivers, Options

from tools import logger

if TYPE_CHECKING:
    from pathlib import Path

    from selenium.webdriver.chrome.webdriver import WebDriver


class Controller:
    """Interface representing the controller."""

    def __init__(self: Controller, path_drivers: Path) -> None:
        self.host = "127.0.0.1"
        self.port = "8080"
        self.url: str = None
        self.browser: str = None

        self.driver: WebDriver = None
        self.drivers = Drivers(path_drivers=path_drivers)

    def navigate(self: Controller) -> None:
        logger.trace_(msg=f"CURRENT URL {self.driver.current_url}")

        if self.driver.current_url == self.options.url:
            return

        if self.options.url == "":
            host = self.options.host or self.host
            port = self.options.port or self.port
            url = f"http://{host}:{port}/"

            if self.driver.current_url == url:
                return

        self.driver.get(url=self.url)
        self.url = self.options.url or url

    def launch(self: Controller) -> None:
        logger.trace_()

        if self.options.browser != self.browser:
            logger.info_(msg="START DRIVER")

            if self.driver is not None:
                self.stop()

            self.driver = self.drivers.launch(browser=self.browser)
            self.browser = self.options.browser

    def resize(self: Controller) -> None:
        logger.trace_()

        height = self.options.height
        width = self.options.width

        if height == "" or width == "":
            self.driver.maximize_window()
        else:
            self.driver.set_window_size(width=width, height=height)

    def setup(self: Controller, **options: dict[str, Any]) -> None:
        logger.trace_(msg=f"OPTIONS {options}")

        self.options = Options(**options)

    # INVESTIGATE ERROR ON RACE CONDITION BETWEEN DRIVER INITIATION
    # AND TRYING TO ACCESS E.G. THE WINDOW HANDLE OR THE DRIVER NAME
    def start(self: Controller) -> None:
        logger.trace_()

        self.launch()

        self.resize()

        self.navigate()

    def stop(self: Controller) -> None:
        logger.trace_()

        if self.driver is not None:
            logger.info_(msg=f"DRIVER {self.driver.name}")

            self.driver.quit()
            self.driver = None
            self.browser = None


controller = Controller(path_drivers=PATH_DRIVERS)
