import pytest

from app.config.settings import get_settings
from app.pages.login_page import LoginPage
from app.pages.dashboard_page import DashboardPage
from app.utils.data_provider import DataProvider

test_data = DataProvider.login_data()


@pytest.mark.parametrize("data", test_data)
def test_login_using_csv(driver, data):
    settings = get_settings()

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    login_page.open(settings.BASE_URL)

    username = data["username"]
    password = data["password"]
    expected_result = data["expected_result"]

    login_page.login(username, password)

    if expected_result == "Success":
     assert dashboard_page.is_logged_in()
    else:
        assert login_page.get_error_message() == expected_result