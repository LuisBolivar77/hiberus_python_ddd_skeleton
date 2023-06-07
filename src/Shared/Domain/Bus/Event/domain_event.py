from abc import ABC, abstractmethod
import uuid
from datetime import datetime, timezone


class DomainEvent(ABC):
    _aggregate_id: str
    _play_head: int

    def __init__(
            self,
            _aggregate_id: str,
            _play_head: int = -1,
            event_id: str = None,
            occurred_on: str = None,
    ):
        self._event_id = event_id if event_id else str(uuid.uuid4())
        self._occurred_on = occurred_on if occurred_on else str(datetime.now(timezone.utc))

    @staticmethod
    @abstractmethod
    def from_primitives(
            aggregate_id: str,
            body: dict,
            event_id: str,
            occurred_on: str
    ) -> 'DomainEvent':
        pass

    @staticmethod
    @abstractmethod
    def event_name(self) -> str:
        pass

    @abstractmethod
    def to_primitives(self) -> dict:
        pass

    def aggregate_id(self) -> str:
        return self._aggregate_id

    def event_id(self) -> str:
        return self._event_id

    def occurred_on(self) -> str:
        return self._occurred_on

    def play_head(self) -> int:
        return self._play_head

    def set_play_head(self, play_head: int) -> None:
        self._play_head = play_head
