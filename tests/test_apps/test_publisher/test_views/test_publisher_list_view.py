from http import HTTPStatus
from typing import Dict

import pytest
from django.test import Client
from rest_framework.response import Response

from server.apps.publisher.models import Publisher


@pytest.fixture()
def get_publisher_data() -> Dict:
    return {
        'name': 'test_publisher',
        'org_site': 'https://test-publisher123.com',
        'email': 'test_publisher@mail.ru'
    }


@pytest.fixture()
def get_publisher(get_publisher_data):

    publisher = Publisher.objects.create(**get_publisher_data)

    yield publisher

    publisher.delete()


@pytest.mark.django_db()
def test_create_publisher(client: Client, get_publisher_data, get_auth_header):
    response: Response = client.post('/publishers/', data=get_publisher_data, **get_auth_header)

    assert response.status_code == HTTPStatus.CREATED


@pytest.mark.django_db()
def test_list_publishers(client: Client, get_publisher):
    response: Response = client.get('/publishers/')

    assert response.status_code == HTTPStatus.OK
    assert response.data.pop().get('id') == get_publisher.id
