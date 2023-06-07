from abc import ABC


class FloatValueObject(ABC):

    def __init__(self, _item: float):
        self._item = _item

    def value(self) -> float:
        return self._item
