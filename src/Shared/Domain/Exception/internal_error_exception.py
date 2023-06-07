class InternalErrorException(Exception):

    _MESSAGE = 'Internal error'

    def __init__(
            self,
            message: str = _MESSAGE,
            previous_exception: Exception = None
    ):
        super().__init__(message, 0, previous_exception)
