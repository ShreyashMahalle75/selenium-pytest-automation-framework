from dataclasses import dataclass


@dataclass
class Reservation:
    """
    Reservation request details.
    """

    gym_name: str
    reservation_date: str
    reservation_time: str
    activity: str = ""
