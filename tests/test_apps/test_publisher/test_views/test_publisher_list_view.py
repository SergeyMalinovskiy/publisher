from http import HTTPStatus

import pytest
from django.test import Client
from django.urls import reverse
from rest_framework.response import Response


@pytest.fixture
def get_publisher_url():
    return reverse('publishers:list')


@pytest.mark.skip(reason='Not implemented')
def test_create_publisher(client: Client, get_publisher_url):
    publisher_data = {
        "name": "test_publisher",
        "org_site": "https://test_publisher.test",
        "email": "test_publisher@mail.ru"
    }
    response: Response = client.post(get_publisher_url, data=publisher_data)

    assert response.status_code == HTTPStatus.CREATED
