from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait

from app.config.settings import get_settings


class Browser:
    """
    Browser Factory.
    Supports Chrome, Edge and Headless mode.
    """

    def __init__(self, browser_name="chrome", headless=False):
        self.settings = get_settings()
        self.browser_name = browser_name.lower()
        self.headless = headless
        self.driver = None

    def create_driver(self):
        """
        Create a Selenium WebDriver instance.
        """

        if self.browser_name == "edge":

            options = EdgeOptions()

            if self.headless:
                options.add_argument("--headless=new")

            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_argument("--window-size=1920,1080")

            self.driver = webdriver.Edge(options=options)

        else:

            options = ChromeOptions()

            if self.headless:
                options.add_argument("--headless=new")

            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")

            self.driver = webdriver.Chrome(options=options)

        self.driver.implicitly_wait(self.settings.IMPLICIT_WAIT)

        return self.driver

    def wait(self):
        """
        Return explicit wait instance.
        """
        return WebDriverWait(
            self.driver,
            self.settings.EXPLICIT_WAIT,
        )

    def maximize(self):
        """
        Maximize browser window.
        """
        self.driver.maximize_window()

    def close(self):
        """
        Close current browser window.
        """
        if self.driver:
            self.driver.close()

    def quit(self):
        """
        Quit browser session.
        """
        if self.driver:
            self.driver.quit()