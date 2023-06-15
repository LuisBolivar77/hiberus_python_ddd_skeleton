from src.Registration.Domain.User import User
from src.Registration.Domain.user_repository import UserRepository
from src.Shared.Infrastructure.mongo_db_client import MongoDBClient


class MongoUserRepository(UserRepository):
    COLLECTION = 'User'

    def __init__(self):
        self.db = MongoDBClient.db_client()

    def save(self, user: User) -> None:
        self.db[self.COLLECTION].insert_one({
            '_id': user.id[0].item,
            'name': user.name[0].value,
            'email': user.email[0].value,
            'password': user.password.value()
        })

    def search(self, uuid: str) -> User:
        pass

    def delete(self, uuid: str) -> None:
        pass
