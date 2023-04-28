from typing import List

from server.apps.subscribes.models import Subscribe
from server.common.interfaces.serializer import HasFilterData


class SubscribeService(object):
    """Subscribe service"""

    def create_subscribe(self):
        raise NotImplementedError

    def get_subscribes(self, filter_object: HasFilterData) -> List[Subscribe]:
        """Returns list of subscribes"""
        return Subscribe.objects.filter(filter_object.get_filter_data())

    def get_subscribes_by_method(self, method: str):
        raise NotImplementedError
