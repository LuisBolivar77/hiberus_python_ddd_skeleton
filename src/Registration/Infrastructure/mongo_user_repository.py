from src.Registration.Domain.User import User
from src.Registration.Domain.user_repository import UserRepository
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import os


class MongoUserRepository(UserRepository):

    COLLECTION = 'users'

    def __init__(self):
        load_dotenv(find_dotenv())
        mongo_pwd = os.environ.get('MONGO_PWD')
        mongo_string = os.environ.get('MONGO_STRING').replace('<password>', mongo_pwd)
        mongo_db = os.environ.get('MONGO_DB')
        self.client = MongoClient(mongo_string)
        self.db = self.client[mongo_db]

    def save(self, user: User) -> None:
        self.db[self.COLLECTION].insert_one({
            '_id': user.uuid().value(),
            'name': user.name().value(),
            'email': user.email().value(),
            'password': user.password.value()
        })

    def search(self, uuid: str) -> User:
        pass

    def delete(self, uuid: str) -> None:
        pass
