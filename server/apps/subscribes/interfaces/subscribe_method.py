from abc import ABC, abstractmethod
from typing import Any


class SubscribeMethod(ABC):
    """Subscribe method interface"""

    @abstractmethod
    def __init__(self, name: str, data: Any) -> None:
        """Init stub"""
        raise NotImplementedError

    @property
    @abstractmethod
    def name(self) -> str:
        """Return method name"""
        raise NotImplementedError

    @property
    @abstractmethod
    def data(self) -> Any:
        """Return method data"""
        raise NotImplementedError
