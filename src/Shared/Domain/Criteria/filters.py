from filter import Filter


class Filters:
    def __init__(self, filters: list[Filter]):
        self.filters = filters

    def add(self, filter_item: Filter):
        return self.__class__(self.filters + [filter_item])

    def filters(self) -> list[Filter]:
        return self.filters

    def count(self) -> int:
        return len(self.filters)
