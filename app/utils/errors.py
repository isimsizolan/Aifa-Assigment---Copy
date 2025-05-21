from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.responses import Response
from starlette.requests import Request as StarletteRequest

class AppError(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code

class ExternalAPIException(AppError):
    def __init__(self, message: str):
        super().__init__(message, status_code=502)

class DatabaseException(AppError):
    def __init__(self, message: str):
        super().__init__(message, status_code=500)

async def app_error_handler(request: StarletteRequest, exc: AppError) -> Response:
    return JSONResponse(
        status_code=exc.status_code,
        content={"status": "error", "message": exc.message},
    )