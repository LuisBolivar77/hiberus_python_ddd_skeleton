class DomainError(Exception):
    def __init__(self):
        super().__init__(self.error_message())

    def error_code(self):
        raise NotImplementedError

    def error_message(self):
        raise NotImplementedError
