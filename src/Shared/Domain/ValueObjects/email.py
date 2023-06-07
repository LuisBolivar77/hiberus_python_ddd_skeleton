from string_value_object import StringValueObject as StringOV
from validate_email_address import validate_email


class Email(StringOV):

    def __init__(self, _val: str):
        super().__init__(_val)
        self.validate()

    def is_equals(self, val) -> bool:
        return self.value == val.value()

    def validate(self):
        if not validate_email(self.value):
            raise ValueError(f"email {self.value} not valid")
