from celery import shared_task

from server.apps.subscribes.models import Subscriber, Event

@shared_task()
def send_subscribe_notification(event_id: int, subscriber_id: int):
    """Send subscribe notification"""
    # TODO: отправлять тем же методом, которым подписался
    subscriber = Subscriber.objects.get(pk=subscriber_id)
    event = Event.objects.get(pk=event_id)

    print('{subscriber} : {event}'.format(subscriber=subscriber, event='event'))


