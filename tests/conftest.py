import os
from datetime import datetime

import allure
import pytest

from app.core.browser import Browser


def pytest_addoption(parser):
    """
    Add custom command-line options.
    """

    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "edge"],
        help="Browser to run tests on",
    )

    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode",
    )


@pytest.fixture(scope="function")
def driver(request):
    """
    Create a new browser instance for each test.
    Capture screenshots on failure and attach them to Allure.
    """

    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    browser = Browser(
        browser_name=browser_name,
        headless=headless,
    )

    driver = browser.create_driver()

    yield driver

    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:

        os.makedirs("screenshots", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        screenshot_name = (
            f"{request.node.name}_{timestamp}.png"
        )

        screenshot_path = os.path.join(
            "screenshots",
            screenshot_name,
        )

        driver.save_screenshot(screenshot_path)

        allure.attach.file(
            screenshot_path,
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG,
        )

        print(f"\nScreenshot saved: {screenshot_path}")

    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Store test execution result.
    """

    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)