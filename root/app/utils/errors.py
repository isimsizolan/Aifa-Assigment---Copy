class APIError(Exception):
    """Raised when an external API call fails."""

    def __init__(self, message: str):
        super().__init__(message)