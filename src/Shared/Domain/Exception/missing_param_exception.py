class MissingParamException(Exception):

    _MESSAGE = 'Missing param'

    def __init__(self, argument: str):
        self.message = f'{self._MESSAGE} - {argument}'
        super().__init__(self.message)
