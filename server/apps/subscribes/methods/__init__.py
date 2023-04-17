from typing import Any, Dict

from server.apps.subscribes.interfaces.subscribe_method import SubscribeMethod
from server.apps.subscribes.methods.email_subscribe_method import EmailSubscribeMethod


registered_subscribe_methods: Dict = {
    'email': EmailSubscribeMethod,
}


def resolve_subscribe_method(method_name: str, data: Any) -> SubscribeMethod:
    """Resolving for subscribe method"""
    subscribe_method_class: type = registered_subscribe_methods.get(method_name)

    return subscribe_method_class(name=method_name, data=data)
