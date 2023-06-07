from abc import ABC, abstractmethod
from src.Shared.Domain.Bus.Event.domain_event import DomainEvent


class EventBus(ABC):

    @abstractmethod
    def publish(self, *events: DomainEvent) -> None:
        pass
