class ValidationError(Exception):
    """Raised when validation of input data fails."""

    def __init__(self, message="Validation error occurred"):
        super().__init__(message)
        self.message = message


class FileError(Exception):
    """Raised when there are issues with file operations."""

    def __init__(self, message="File handling error occurred"):
        super().__init__(message)
        self.message = message


class NotFoundError(Exception):
    """Raised when a required user or task is not found."""

    def __init__(self, message="Requested resource not found"):
        super().__init__(message)
        self.message = message
