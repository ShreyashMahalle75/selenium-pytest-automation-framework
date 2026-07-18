from loguru import logger

from app.config.settings import get_settings
from app.pages.dashboard_page import DashboardPage
from app.pages.login_page import LoginPage


class AuthService:
    """Handles authentication workflow."""

    def __init__(self, driver):
        self.driver = driver
        self.settings = get_settings()
        self.login_page = LoginPage(driver)
        self.dashboard_page = DashboardPage(driver)

    def login(self):
        logger.info("Opening login page...")

        if not self.settings.BASE_URL:
            raise ValueError("BASE_URL is not configured in the .env file.")

        self.login_page.open(self.settings.BASE_URL)

        logger.info("Entering credentials...")

        self.login_page.login(
            self.settings.GYM_USERNAME,
            self.settings.GYM_PASSWORD,
        )

        logger.info("Verifying login...")

        if not self.dashboard_page.is_logged_in():
            raise Exception("Login failed!")

        logger.success("Login successful.")
        return True

    def logout(self):
        logger.info("Logging out...")

        self.dashboard_page.logout()

        if not self.login_page.is_login_page_displayed():
            raise Exception("Logout failed!")

        logger.success("Logout successful.")
        return True