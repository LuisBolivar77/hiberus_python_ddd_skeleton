from filters import Filters
from order import Order


class Criteria:

    def __init__(
            self,
            _filters: Filters,
            _order: Order = None,
            _offset: int = None,
            _limit: int = None
    ):
        self.filters = _filters
        self.order = _order
        self.offset = _offset
        self.limit = _limit

    def has_filters(self):
        return self.filters.count() > 0

    def has_order(self):
        return not self.order.is_none() if self.order else False

    def has_offset(self):
        return self.offset is not None

    def has_limit(self):
        return self.limit is not None

    def filters(self):
        return self.filters

    def order(self):
        return self.order

    def offset(self):
        return self.offset

    def limit(self):
        return self.limit
