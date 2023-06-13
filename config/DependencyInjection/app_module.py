from flask import g
from injector import Module, provider
from src.Registration.Application.Upsert.user_creator import UserCreator
from src.Registration.Domain.user_repository import UserRepository


class AppModule(Module):

    @provider
    def provider_user_creator(self) -> UserCreator:
        # Access request-specific data from Flask's `g` object
        if hasattr(g, 'user_creator'):
            return g.user_creator

        # If the dependency doesn't exist in `g`, create a new instance
        user_creator = UserCreator()

        # Store the dependency in `g` for future requests
        g.user_creator = user_creator

        return user_creator

    @provider
    def provider_user_repository(self) -> UserRepository:
        if hasattr(g, 'user_repository'):
            return g.user_repository
        user_repository = UserRepository()
        g.user_repository = user_repository
        return user_repository
