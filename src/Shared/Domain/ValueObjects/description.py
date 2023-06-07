from string_value_object import StringValueObject as StringVO


class Description(StringVO):

    MAX_LENGTH = 255

    def __init__(self, value: str):
        super().__init__(value)

    def validate(self):
        if StringVO.is_empty(self.value):
            raise ValueError("empty description")

        if len(self.value) > self.MAX_LENGTH:
            exceeded_amount = len(self.value) - self.MAX_LENGTH
            raise ValueError(f"the description exceeds the max length by {exceeded_amount} characters")

