from loguru import logger

from app.core.browser import Browser
from app.services.auth_service import AuthService



def main():


    logger.info("=" * 60)
    logger.info("Gym Reservation Bot")
    logger.info("=" * 60)

    browser = Browser()

    try:
        driver = browser.create_driver()

        auth_service = AuthService(driver)

        auth_service.login()

        auth_service.logout()

        logger.success("Login and Logout automation completed successfully!")

        input("\nPress ENTER to close the browser...")

    except Exception as e:
        logger.exception(f"Automation failed: {e}")

    finally:
        browser.quit()
        logger.info("Browser closed.")


if __name__ == "__main__":
    main()