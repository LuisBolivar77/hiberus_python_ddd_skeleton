from src.Shared.Domain.Aggregate.aggregate_root import AggregateRoot
from src.Shared.Domain.ValueObjects.email import Email
from src.Shared.Domain.ValueObjects.name import Name
from src.Shared.Domain.ValueObjects.password import Password
from src.Shared.Domain.ValueObjects.uuid_value_object import Uuid


class User(AggregateRoot):

    def __init__(
            self,
            uuid: Uuid,
            name: Name,
            email: Email,
            password: Password,
    ):
        self.id = uuid,
        self.name = name,
        self.email = email,
        self.password = password

    @staticmethod
    def build(
            uuid: Uuid,
            name: Name,
            email: Email,
            password: Password,
    ) -> 'User':
        return User(uuid, name, email, password)

    @staticmethod
    def from_primitives(
            uuid: str,
            name: str,
            email: str,
            password: str,
    ) -> 'User':
        return User(
            Uuid(uuid),
            Name(name),
            Email(email),
            Password(password)
        )

    def uuid(self) -> Uuid:
        return self.id

    def name(self) -> Name:
        return self.name

    def email(self) -> Email:
        return self.email

    def password(self) -> Password:
        return self.password
