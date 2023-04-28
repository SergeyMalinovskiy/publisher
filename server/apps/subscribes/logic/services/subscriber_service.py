from typing import Any, Dict, List

from server.apps.subscribes.interfaces.subscribe_method import SubscribeMethod
from server.apps.subscribes.logic.services.subscribe_method_service import SubscribeMethodService
from server.apps.subscribes.models import Subscriber


class SubscriberService(object):
    """Subscriber service"""


    def create_subscriber(
        self,
        method: str,
        method_data: str,
        is_active: bool = True,
    ) -> Subscriber:
        """Create and returning subscriber"""
        subscribe_method_service = SubscribeMethodService

        subscribe_method = subscribe_method_service.get_by_name(method)

        subscriber = Subscriber(
            method=subscribe_method.name,
            method_data=method_data,
            is_active=is_active,
        )

        subscriber.save()

        return subscriber

    def get_subscribers(self, filter_data: Dict) -> List[Subscriber]:
        pass

    def delete_subscriber(self, id: int) -> bool:
        pass

    def get_by_id(self, id: int) -> Subscriber:
        pass
