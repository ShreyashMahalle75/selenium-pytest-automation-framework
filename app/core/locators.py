from dataclasses import dataclass


@dataclass(frozen=True)
class LoginLocators:
    username: tuple
    password: tuple
    login_button: tuple


@dataclass(frozen=True)
class ReservationLocators:
    activity: tuple
    date: tuple
    time: tuple
    reserve_button: tuple
