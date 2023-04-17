from typing import Dict, Any

from server.apps.subscribes.interfaces.subscribe_method import SubscribeMethod


class EmailSubscribeMethod(SubscribeMethod):
    """Email subscribe method"""

    def __init__(self, name: str, data: Any) -> None:
        """Init"""
        self.name = name
        self.data = data

    def name(self) -> str:
        """Get name"""
        return 'email'

    def data(self) -> Dict:
        """Get data"""
        return {'data': self.data}
