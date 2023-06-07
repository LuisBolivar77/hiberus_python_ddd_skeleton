from abc import ABC, abstractmethod
from src.Shared.Domain.Bus.Event.domain_event import DomainEvent


class DomainEventRepository(ABC):

    @abstractmethod
    def save(self, event: DomainEvent) -> None:
        pass
