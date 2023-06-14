from flask import g
from injector import Module
from src.Registration.Application.Upsert.user_creator import UserCreator
from src.Registration.Domain.user_repository import UserRepository
from src.Registration.Infrastructure.mongo_user_repository import MongoUserRepository


class AppModule(Module):
    def configure(self, binder):
        binder.bind(UserRepository, to=MongoUserRepository)
        binder.bind(UserCreator, to=UserCreator)
