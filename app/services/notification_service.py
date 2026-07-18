from loguru import logger


class NotificationService:
    """
    Placeholder for email/Slack/Telegram notifications.
    """

    def send_success(self, message: str):
        logger.success(message)

    def send_failure(self, message: str):
        logger.error(message)
