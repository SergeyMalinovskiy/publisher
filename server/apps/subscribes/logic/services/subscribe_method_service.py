from typing import Any, Dict

from server.apps.subscribes.interfaces.subscribe_method import SubscribeMethod
from server.apps.subscribes.methods import EmailSubscribeMethod
from server.apps.subscribes.models import Subscriber

registered_subscribe_methods: Dict = {
    'email': EmailSubscribeMethod,
    'telegram': None,
    'site': None,
}


class SubscribeMethodService(object):
    """Subscribe method service"""

    def is_method_exists(self, method_name: str) -> bool:
        """Check method exists"""
        # TODO: pass
        return True

    def get_by_subscriber(self, subscriber: Subscriber) -> SubscribeMethod:
        """Resolving for subscribe method"""
        method = subscriber.method
        method_data = subscriber.method_data

        subscribe_method_class: type = self.get_by_name(method)

        return subscribe_method_class(name=method, data=method_data)

    def get_by_name(self, name: str) -> SubscribeMethod:
        """Get subscribe method class from registered methods"""
        return registered_subscribe_methods.get(name)
