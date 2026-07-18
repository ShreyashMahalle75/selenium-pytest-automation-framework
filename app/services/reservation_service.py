from loguru import logger

from app.models.reservation import Reservation
from app.pages.reservation_page import ReservationPage
from app.utils.retry import retry


class ReservationService:

    def __init__(self, driver):
        self.driver = driver
        self.page = ReservationPage(driver)

    @retry(max_attempts=3, delay=2)
    def reserve_slot(self, reservation: Reservation):
        logger.info("Starting reservation workflow...")

        self.page.reserve(reservation)

        logger.success("Reservation workflow completed.")
