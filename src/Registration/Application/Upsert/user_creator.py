from src.Registration.Domain.User import User
from src.Registration.Domain.user_repository import UserRepository
from src.Shared.Domain.ValueObjects.uuid_value_object import Uuid
from src.Shared.Domain.ValueObjects.name import Name
from src.Shared.Domain.ValueObjects.email import Email
from src.Shared.Domain.ValueObjects.password import Password
from injector import inject


class UserCreator:

    @inject
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def creator(
            self,
            uuid: str,
            name: str,
            email: str,
            password: str
    ) -> None:
        user = User.build(
            Uuid(uuid),
            Name(name),
            Email(email),
            Password(password)
        )
        self.repository.save(user)
