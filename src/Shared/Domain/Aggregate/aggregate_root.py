from abc import ABC
from src.Shared.Domain.Bus.Event.domain_event import DomainEvent


class AggregateRoot(ABC):

    domain_events: list = []

    def _pull_domain_events(self) -> list:
        domain_events = self.domain_events
        self.domain_events = []
        return domain_events

    def _record(self, event: DomainEvent) -> None:
        self.domain_events.append(event)
