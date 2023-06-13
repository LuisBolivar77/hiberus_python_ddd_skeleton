from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Iterator, List

TValue = TypeVar('TValue')


class Collection(Generic[TValue], ABC):

    def __init__(self, items: List[TValue] = []):
        self.items = items
        self.assert_items_type()

    def __iter__(self) -> Iterator[TValue]:
        return iter(self.items)

    def __len__(self) -> int:
        return len(self.items)

    def add(self, item: TValue) -> None:
        self.items.append(item)

    def remove(self, item_to_remove: TValue) -> None:
        self.items = [item for item in self.items if item != item_to_remove]

    def items(self) -> List[TValue]:
        return self.items

    def last(self) -> TValue:
        return self.items[-1]

    def first(self) -> TValue:
        return self.items[0]

    def merge(self, collection: 'Collection') -> None:
        if not isinstance(collection, type(self)):
            raise Exception(f"Items must be of type {type(self).__name__} instead of {type(collection).__name__}")

        self.items.extend(collection)

    @abstractmethod
    def assert_items_type(self) -> None:
        pass
