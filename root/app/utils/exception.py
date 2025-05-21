from functools import wraps
from app.utils.errors import AppError

def catch(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except AppError as e:
            return f"[Error] {e.message}"
        except Exception as e:
            return f"[Unexpected error] {str(e)}"
    return wrapper

def catchsync(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AppError as e:
            return f"[Error] {e.message}"
        except Exception as e:
            return f"[Unexpected error] {str(e)}"
    return wrapper
