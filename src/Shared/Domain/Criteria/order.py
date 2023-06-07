from order_by import _OrderBy
from order_type import OrderType
from src.Shared.Domain.ValueObjects.string_value_object import StringValueObject as StringVO


class Order:
    def __init__(self, _order_by: _OrderBy, _order_type: OrderType):
        self._order_by = _order_by
        self._order_type = _order_type

    def order_by(self) -> _OrderBy:
        return self._order_by

    def order_type(self) -> OrderType:
        return self._order_type

    def create_desc(self) -> "Order":
        return Order(self._order_by, OrderType.DESC)

    @staticmethod
    def from_values(self, order_by: str, order_type: str) -> "Order":
        return Order(_OrderBy(order_by), OrderType(order_type)) if not StringVO.is_empty(order_by) else self.none()

    @staticmethod
    def none() -> "Order":
        return Order(_OrderBy(""), OrderType.NONE)

    def is_none(self) -> bool:
        return self.order_type() == OrderType.NONE
