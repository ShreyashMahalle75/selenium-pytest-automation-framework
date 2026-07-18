import time
from functools import wraps

from loguru import logger


def retry(max_attempts=3, delay=2):
    """
    Retry decorator for transient failures.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None

            for attempt in range(1, max_attempts + 1):
                try:
                    logger.info(f"Attempt {attempt}/{max_attempts}: {func.__name__}")
                    return func(*args, **kwargs)

                except Exception as e:
                    last_exception = e

                    logger.warning(f"Attempt {attempt} failed: {e}")

                    if attempt < max_attempts:
                        time.sleep(delay)

            raise last_exception

        return wrapper

    return decorator
