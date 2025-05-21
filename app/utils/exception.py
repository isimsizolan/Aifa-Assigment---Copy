from functools import wraps
from app.utils.errors import AppError

# This code defines two decorators, `catch` and `catchsync`, which are used to handle exceptions in asynchronous and synchronous functions, respectively.

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
