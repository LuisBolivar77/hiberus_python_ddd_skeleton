from abc import ABC, abstractmethod
from query import Query


class QueryBus(ABC):

    @abstractmethod
    def ask(self, query: Query):
        pass
