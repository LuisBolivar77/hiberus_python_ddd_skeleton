class AlreadyStoredException(Exception):
    _MESSAGE = 'The entity is already stored'

    def __init__(
            self,
            message: str = _MESSAGE,
            code: str = 500,
            previous: Exception = None
    ) -> None:
        super().__init__(message, code, previous)
