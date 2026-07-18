import allure

from app.config.settings import get_settings
from app.pages.dashboard_page import DashboardPage
from app.pages.login_page import LoginPage


@allure.epic("Gym Reservation Bot")
@allure.feature("Authentication")
@allure.story("Valid Login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify user can login with valid credentials")
@allure.description(
    "Verify that a registered user can successfully log into the application "
    "using valid credentials."
)
def test_valid_login(driver):
    settings = get_settings()

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    with allure.step("Open login page"):
        login_page.open(settings.BASE_URL)

    with allure.step("Enter valid username"):
        login_page.enter_username(settings.GYM_USERNAME)

    with allure.step("Enter valid password"):
        login_page.enter_password(settings.GYM_PASSWORD)

    with allure.step("Click Login button"):
        login_page.click_login()

    with allure.step("Verify dashboard is displayed"):
       assert dashboard_page.is_logged_in()
    with allure.step("Verify welcome message"):
        assert "Logged In Successfully" in dashboard_page.get_success_message()