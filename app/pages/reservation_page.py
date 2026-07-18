from loguru import logger

from app.models.reservation import Reservation
from app.pages.base_page import BasePage


class ReservationPage(BasePage):
    """
    Generic reservation page.

    Website-specific locators will be added later.
    """

    def reserve(self, reservation: Reservation):
        logger.info(
            f"Preparing reservation for "
            f"{reservation.gym_name} "
            f"on {reservation.reservation_date} "
            f"at {reservation.reservation_time}"
        )

        # TODO:
        # 1. Open reservation page
        # 2. Select activity
        # 3. Select date
        # 4. Select time
        # 5. Click Reserve
