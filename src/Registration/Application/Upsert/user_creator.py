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
        uuid = Uuid(uuid)
        name = Name(name)
        email = Email(email)
        password = Password(password)

        user = User.build(uuid, name, email, password)
        self.repository.save(user)
