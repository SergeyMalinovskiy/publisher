import pytest
from http import HTTPStatus

from django.test import Client
from django.urls import reverse
from rest_framework.response import Response


@pytest.mark.django_db()
def test_create_author(client: Client, get_author_url, get_auth_header):
    data = {
        "surname": "Test",
        "name": "Test"
    }

    response: Response = client.post(get_author_url, data=data, **get_auth_header)

    assert response.status_code == HTTPStatus.CREATED


@pytest.mark.django_db()
def test_get_authors(client: Client, get_author_url):
    response: Response = client.get(get_author_url)

    assert response.status_code == HTTPStatus.OK


@pytest.fixture()
def get_author_url():
    return reverse('authors:list')
