from uuid import UUID, uuid4
from enum import Enum


class Uuid:

    def __init__(self, item: str):
        self.item = item

    def value(self) -> str:
        return self.item

    def equals(self, other) -> bool:
        return self.value() == other.value()

    @staticmethod
    def random(self):
        return self(uuid4())

    @staticmethod
    def is_valid(self, value: str) -> bool:
        try:
            UUID(str(value))
            return True
        except ValueError:
            return False

    def _validate(self, value: str) -> None:
        if not self.is_valid(value):
            raise ValueError(f"{value} is not a valid UUID")

    def __str__(self):
        Enum
        return str(self.item)
