from http import HTTPStatus
from typing import Dict

import pytest
from django.test import Client
from django.urls import reverse
from rest_framework.response import Response

from server.apps.publisher.models import Publisher


@pytest.fixture
def get_publisher():
    publisher_data = {
        "name": "Test_Publisher",
        "org_site": "https://test_publisher",
        "email": "test@email.ru"
    }

    publisher = Publisher.objects.create(**publisher_data)

    yield {
        "model": publisher,
        "url": reverse('publishers:detail', kwargs={"pk": publisher.id})
    }

    publisher.delete()


@pytest.mark.django_db
def test_update_publisher(client: Client, get_publisher: Dict, get_auth_header):
    new_name = 'NewPublisherName'

    response: Response = client.put(
        get_publisher.get("url"),
        data={"name": new_name},
        content_type='application/json',
        **get_auth_header
    )

    assert response.status_code == HTTPStatus.OK
    assert response.data.get("name") == new_name


@pytest.mark.django_db
def test_delete_publisher(client: Client, get_publisher: Dict, get_auth_header):
    url = get_publisher.get("url")

    response: Response = client.delete(url, **get_auth_header)
    assert response.status_code == HTTPStatus.NO_CONTENT

    response: Response = client.delete(url, **get_auth_header)
    assert response.status_code == HTTPStatus.NOT_FOUND
