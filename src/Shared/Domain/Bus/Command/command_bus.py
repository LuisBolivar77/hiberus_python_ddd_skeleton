from abc import abstractmethod
from command import Command


class CommandBus:

    @abstractmethod
    def dispatch(self, command: Command) -> None:
        pass
