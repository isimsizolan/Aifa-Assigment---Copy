import logging
from functools import wraps

# This code sets up a logger for an application, defining two decorators `log` and `logsync` to log function calls and results.

logger = logging.getLogger("agentic")
logger.setLevel(logging.INFO)

if not logger.hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def log(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        logger.info(f"[TOOL CALL] {func.__name__} | args: {args}, kwargs: {kwargs}")
        try:
            result = await func(*args, **kwargs)
            logger.info(f"[TOOL RESULT] {func.__name__} | result: {result}")
            return result
        except Exception as e:
            logger.error(f"[TOOL ERROR] {func.__name__} | error: {e}")
            raise
    return wrapper


def logsync(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"[TOOL CALL] {func.__name__} | args: {args}, kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"[TOOL RESULT] {func.__name__} | result: {result}")
            return result
        except Exception as e:
            logger.error(f"[TOOL ERROR] {func.__name__} | error: {e}")
            raise
    return wrapper