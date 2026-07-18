class AutomationError(Exception):
    """Base exception for automation errors."""


class LoginError(AutomationError):
    """Raised when login fails."""


class ReservationError(AutomationError):
    """Raised when reservation fails."""


class BrowserError(AutomationError):
    """Raised when browser initialization fails."""
