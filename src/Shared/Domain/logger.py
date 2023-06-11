from abc import ABC, abstractmethod


class Logger(ABC):

        @abstractmethod
        def info(
                self,
                message: str,
                context: dict = None
        ) -> None:
            pass

        @abstractmethod
        def warning(
                self,
                message: str,
                context: dict = None
        ) -> None:
            pass

        @abstractmethod
        def error(
                self,
                message: str,
                context: dict = None
        ) -> None:
            pass
