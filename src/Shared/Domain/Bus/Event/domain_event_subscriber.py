from abc import ABC, abstractmethod
from domain_event import DomainEvent


class DomainEventSubscriber(ABC):
    @abstractmethod
    def __call__(self, event: DomainEvent) -> None:
        pass

    @staticmethod
    @abstractmethod
    def subscribed_to() -> list:
        pass
