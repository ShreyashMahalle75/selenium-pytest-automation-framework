from app.services.auth_service import AuthService


def test_logout(driver):
    auth = AuthService(driver)

    assert auth.login() is True
    auth.logout()