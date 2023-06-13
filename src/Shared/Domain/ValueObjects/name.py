from src.Shared.Domain.ValueObjects.string_value_object import StringValueObject as StringVO


class Name(StringVO):

    def __init__(self, _val: str):
        super().__init__(_val)
        self.validate()

    def validate(self):
        if StringVO.is_empty(self.value):
            raise ValueError(self.value)

    def is_equals(self, val) -> bool:
        return self.value == val.value()
