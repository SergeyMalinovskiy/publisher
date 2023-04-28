from abc import ABC, abstractmethod
from typing import Dict


class HasFilterData(ABC):
    """Has filter data method interface"""

    @abstractmethod
    def get_filter_data(self) -> Dict:
        """Returns filter data"""
        raise NotImplementedError()
