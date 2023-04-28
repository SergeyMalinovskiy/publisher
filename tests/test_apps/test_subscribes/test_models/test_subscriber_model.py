import json

import pytest

from server.apps.subscribes.logic.services.subscribe_method_service import (
    SubscribeMethodService,
)
from server.apps.subscribes.models import Subscriber


@pytest.fixture()
def subscribe_method_service() -> SubscribeMethodService:
    """Returns subscribe method service fixture"""
    return SubscribeMethodService()


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
def test_subscriber_email_method(
    subscriber: Subscriber,
    subscribe_method_service: SubscribeMethodService,
) -> None:
    """Test subscribe email method"""
    subscribe_method = subscribe_method_service.get_by_subscriber(subscriber)

    assert json.loads(subscribe_method.data).get('email') == 'test@email.ru'
