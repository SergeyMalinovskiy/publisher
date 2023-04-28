from typing import List, Any

from server.apps.subscribes.models import Event


class EventService(object):
    """Event service"""

    @classmethod
    def create_event(cls: Any, name: str) -> Event:
        """Create event"""
        return Event.objects.create(name=name)

    @classmethod
    def enable_event(cls: Any, event_id: int) -> bool:
        """Activate event"""
        return True

    @classmethod
    def disable_event(cls: Any, event_id: int) -> bool:
        """Disable event activity"""
        return True

    @classmethod
    def get_events(cls: Any, *args: Any, **kwargs: Any) -> List[Event]:
        """Returns list of events"""
        return Event.objects.all()

