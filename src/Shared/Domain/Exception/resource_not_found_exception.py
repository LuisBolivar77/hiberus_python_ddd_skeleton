class ResourceNotFoundException(Exception):

    _MESSAGE = "{} identified by {} not found"

    def __init__(
            self,
            object_type: str,
            search_criteria: str,
    ) -> None:
        super().__init__(format(self._MESSAGE, object_type, search_criteria))
