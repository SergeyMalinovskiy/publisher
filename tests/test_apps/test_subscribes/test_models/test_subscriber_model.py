import json

import pytest

from server.apps.subscribes.interfaces.subscribe_method import SubscribeMethod
from server.apps.subscribes.models import Subscriber


@pytest.fixture()
def subscriber() -> Subscriber:
    """Create subscriber"""
    subscriber = Subscriber.objects.create(
        method='email',
        method_data=json.dumps({'email': 'test@email.ru'}),
        is_active=True,
    )

    yield subscriber

    subscriber.delete()


@pytest.mark.django_db()
def test_subscriber_email_method(subscriber: Subscriber) -> None:
    """Test subscribe email method"""
    subscribe_method: SubscribeMethod = subscriber.subscribe_method

    assert json.loads(subscribe_method.data).get('email') == 'test@email.ru'
