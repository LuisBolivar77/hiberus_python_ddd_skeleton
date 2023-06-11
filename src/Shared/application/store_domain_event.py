from src.Shared.Domain.Bus.Event.domain_event import DomainEvent
from src.Shared.Domain.Bus.Event.domain_event_repository import DomainEventRepository
from src.Shared.Domain.Bus.Event.domain_event_subscriber import DomainEventSubscriber


class StoreDomainEvent(DomainEventSubscriber):

    def __init__(self, _repository: DomainEventRepository) -> None:
        self.repository = _repository

    def __call__(self, domain_event: DomainEvent) -> None:
        self.repository.save(domain_event)

    def subscribed_to(self) -> list:
        return [self.__class__.__name__]
