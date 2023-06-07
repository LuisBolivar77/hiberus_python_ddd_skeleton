from abc import ABC, abstractmethod

from src.Shared.Domain.Aggregate.aggregate_root import AggregateRoot


class AggregateFactory(ABC):

    @abstractmethod
    def create(
            self,
            aggregate_class: str,
            domain_events: list,
    ) -> AggregateRoot:
        pass
