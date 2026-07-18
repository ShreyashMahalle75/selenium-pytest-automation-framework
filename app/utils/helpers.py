from datetime import datetime


def create_screenshot_name(prefix: str = "screenshot") -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{timestamp}.png"
