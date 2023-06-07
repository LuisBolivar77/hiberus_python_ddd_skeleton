from abc import ABC


class StringValueObject(ABC):

    def __init__(self, value: str):
        self.value = value

    def value(self):
        return self.value

    def __str__(self):
        return str(self.value)

    @staticmethod
    def is_empty(val: str) -> bool:
        return val == "" or val is None

