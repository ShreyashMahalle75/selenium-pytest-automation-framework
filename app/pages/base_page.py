from pathlib import Path

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from app.config.settings import get_settings
from app.utils.helpers import create_screenshot_name


class BasePage:
    """
    Base class for all page objects.
    Provides common Selenium operations.
    """

    def __init__(self, driver):
        self.driver = driver
        self.settings = get_settings()
        self.wait = WebDriverWait(
            driver,
            self.settings.EXPLICIT_WAIT,
        )

    def open(self, url: str):
        """Open a URL."""
        self.driver.get(url)

    def find(self, locator):
        """Find an element after waiting for it."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """Click an element when it becomes clickable."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator, text: str):
        """Clear and type into an input field."""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Get text from an element."""
        return self.find(locator).text

    def is_visible(self, locator):
        """Check whether an element is visible."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def current_url(self):
        """Return current page URL."""
        return self.driver.current_url

    def title(self):
        """Return current page title."""
        return self.driver.title

    def refresh(self):
        """Refresh the page."""
        self.driver.refresh()

    def wait_for_page(self):
        """Wait until the page has completely loaded."""
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def scroll_to(self, element):
        """Scroll the page until the element is visible."""
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element,
        )

    def js_click(self, element):
        """Click an element using JavaScript."""
        self.driver.execute_script(
            "arguments[0].click();",
            element,
        )

    def take_screenshot(self, folder="screenshots"):
        """Capture a screenshot."""
        Path(folder).mkdir(parents=True, exist_ok=True)

        filename = create_screenshot_name()

        path = Path(folder) / filename

        self.driver.save_screenshot(str(path))

        return path
