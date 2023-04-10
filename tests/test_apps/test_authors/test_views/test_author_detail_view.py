import json
from http import HTTPStatus

import pytest
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.response import Response

from server.apps.author.models import Author


@pytest.mark.django_db()
def test_update_author(client: Client, get_author_url, get_auth_header):
    data = [
        ("name", "TestNewName"),
        ("surname", "TestNewSurname"),
        ("license_code", "new_license_code"),
    ]

    for field, new_value in data:
        new_field_value = "TestNewName"

        response: Response = client.put(
                                get_author_url,
                                data=json.dumps({field: new_field_value}),
                                content_type='application/json',
                                **get_auth_header
                            )

        assert response.status_code == HTTPStatus.OK
        assert new_field_value == dict(response.data).get(field)


@pytest.mark.django_db()
def test_delete_author(client: Client, get_author_url, get_auth_header):
    response: Response = client.delete(get_author_url, **get_auth_header)
    assert response.status_code == HTTPStatus.NO_CONTENT

    response: Response = client.get(get_author_url)
    assert response.status_code == HTTPStatus.NOT_FOUND


@pytest.fixture()
def get_author():
    author = Author.objects.create(surname='TestSurname', name='TestName', license_code='1234567890')

    yield author

    author.delete()


@pytest.fixture()
def get_author_url(get_author):
    return reverse("authors:detail", kwargs={"pk": get_author.id})
