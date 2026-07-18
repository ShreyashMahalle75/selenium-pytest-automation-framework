from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger

from app.pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object for the Practice Test Automation login page."""

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "submit")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "post-title")
    LOGIN_HEADER = (By.TAG_NAME, "h2")
    ERROR_MESSAGE = (By.ID, "error")

    def open(self, url: str):
        """Open the login page."""
        self.driver.get(url)
        self.wait_for_page()

    def enter_username(self, username: str):
        logger.info(f"Entering username: {username}")
        self.type(self.USERNAME, username)

    def enter_password(self, password: str):
        logger.info("Entering password")
        self.type(self.PASSWORD, password)

    def click_login(self):
        logger.info("Clicking Login button")
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str):
        """Perform login."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_success_message(self):
        """Return success message after login."""
        return self.get_text(self.SUCCESS_MESSAGE)

    def is_login_page_displayed(self):
        """Verify login page is displayed."""
        return "Test login" in self.get_text(self.LOGIN_HEADER)

    def get_error_message(self):
        """
        Wait until the login error message is visible
        and contains text.
        """
        error = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )

        self.wait.until(
            lambda driver: error.text.strip() != ""
        )

        return error.text.strip()

    def get_username_validation_message(self):
        """Return browser validation message for username field."""
        username_field = self.find(self.USERNAME)
        return username_field.get_attribute("validationMessage")