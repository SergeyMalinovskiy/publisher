import json
from http import HTTPStatus
from typing import List, Dict, OrderedDict

import pytest
from django.test import Client
from faker import Faker
from rest_framework.response import Response

from server.apps.subscribes.models import Subscribe, Event, Subscriber


@pytest.fixture()
def uri() -> str:
    """Returns subscribes uri"""
    return '/subscribes/'

@pytest.fixture()
def subscriber(faker: Faker) -> Subscriber:
    """Generate one subscriber"""
    model = Subscriber.objects.create(
        method='email',
        method_data=json.dumps({'email': faker.email()}),
        is_active=True,
    )

    yield model

    model.delete()


@pytest.fixture()
def event() -> Event:
    """Generate one event"""
    model = Event.objects.create()

    yield model

    model.delete()


@pytest.fixture()
def subscribe(event: Event, subscriber: Subscriber) -> Subscribe:
    """Generate on subscribe"""
    models = Subscribe.objects.create(
        event=event,
        subscriber=subscriber,
    )

    yield models

    models.delete()


@pytest.fixture()
def subscribes(event: Event, subscriber: Subscriber) -> List[Subscribe]:
    """Generate subscribes list"""
    models: List[Subscribe] = []

    for _ in range(10):
        models.append(Subscribe(
            subscriber=subscriber,
            event=event,
        ))

    saved_models = Subscribe.objects.bulk_create(models)

    yield saved_models

    ids = [model.id for model in saved_models]
    Subscribe.objects.filter(pk__in=ids).delete()


@pytest.mark.django_db()
def test_subscribes_list(
    get_auth_header: Dict,
    client: Client,
    subscribes: List[Subscribe],
    uri: str,
) -> None:
    response: Response = client.get(uri, **get_auth_header)

    assert response.status_code == HTTPStatus.OK
    assert len(response.data) == len(subscribes)
