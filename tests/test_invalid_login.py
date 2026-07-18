import pytest

from app.config.settings import get_settings
from app.pages.login_page import LoginPage


@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        ("student", "WrongPassword123", "Your password is invalid!"),
        ("wronguser", "Password123", "Your username is invalid!"),
        ("", "Password123", "Your username is invalid!"),
        ("student", "", "Your password is invalid!"),
    ],
)
def test_invalid_login(driver, username, password, expected_error):
    settings = get_settings()

    login_page = LoginPage(driver)

    login_page.open(settings.BASE_URL)

    if username == "student":
        username = settings.GYM_USERNAME

    if password == "Password123":
        password = settings.GYM_PASSWORD

    login_page.login(username, password)

    