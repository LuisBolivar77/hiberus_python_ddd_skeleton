"""Containers module."""

from dependency_injector import containers, providers

from app.Controller.Registration.user_put_controller import UserPutController
from src.Registration.Application.Upsert.user_creator import UserCreator
from src.Registration.Domain.user_repository import UserRepository


class Container(containers.DeclarativeContainer):
    pass
    # user_repository = providers.Singleton(UserRepository)
    # user_creator = providers.Factory(UserCreator, repository=user_repository)
    # user_put_controller = providers.Factory(UserPutController, user_creator=user_creator)
    # config = providers.Configuration(yaml_files=["config.yml"])
    #
    # user_repository = providers.Factory(
    #     UserRepository
    # )
    #
    # user_creator = providers.Factory(
    #     UserCreator,
    #     repository=user_repository
    # )
