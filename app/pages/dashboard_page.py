from selenium.webdriver.common.by import By

from app.pages.base_page import BasePage


class DashboardPage(BasePage):
    """Page Object for the dashboard after successful login."""

    SUCCESS_MESSAGE = (By.CLASS_NAME, "post-title")
    LOGOUT_BUTTON = (By.LINK_TEXT, "Log out")

    def get_success_message(self):
        """Return the welcome message."""
        return self.get_text(self.SUCCESS_MESSAGE)

    def logout(self):
        """Click the logout button."""
        self.click(self.LOGOUT_BUTTON)

    def is_logged_in(self):
        """Return True if the dashboard is displayed."""
        return "Logged In Successfully" in self.get_success_message()