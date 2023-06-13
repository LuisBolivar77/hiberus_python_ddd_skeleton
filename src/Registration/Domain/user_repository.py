from abc import ABC, abstractmethod
from src.Registration.Domain.User import User


class UserRepository(ABC):

    @abstractmethod
    def save(self, user: User) -> None:
        pass

    @abstractmethod
    def search(self, uuid: str) -> User:
        pass

    @abstractmethod
    def delete(self, uuid: str) -> None:
        pass
