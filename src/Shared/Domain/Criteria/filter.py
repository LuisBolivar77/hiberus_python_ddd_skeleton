from filter_field import _FilterField
from filter_operator import FilterOperator
from filter_value import _FilterValue


class Filter:
    def __init__(self, field: _FilterField, operator: FilterOperator, value: _FilterValue):
        self.field = field
        self.operator = operator
        self.value = value

    @staticmethod
    def from_values(values: dict):
        return Filter(
            _FilterField(values['field']),
            FilterOperator(values['operator']),
            _FilterValue(values['value'])
        )

    def field(self) -> _FilterField:
        return self.field

    def operator(self) -> FilterOperator:
        return self.operator

    def value(self) -> _FilterValue:
        return self.value
