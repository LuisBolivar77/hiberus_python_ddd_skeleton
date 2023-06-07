from abc import ABC


class IntObjectValue(ABC):

    def __init__(self, _item: int):
        self._item = _item

    def value(self) -> int:
        return self._item

    def is_bigger_than(self, other) -> bool:
        return self.value() > other.value()
