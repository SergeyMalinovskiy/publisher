from http import HTTPStatus

import pytest
from django.test import TestCase
from django.urls import reverse
from rest_framework.response import Response

from server.apps.author.models import Author
from django.test import Client


@pytest.fixture()
def get_author():
    author = Author.objects.create(surname="TestSurname", name="TestName")

    yield author

    author.delete()


@pytest.fixture()
def get_author_url(get_author):
    return reverse("books:list")


@pytest.mark.django_db
def test_create_books_with_not_exists_author(client: Client, get_author_url, get_auth_header):
    not_exists_author_id: int = Author.objects.latest('id').id+1

    data = {
        "name": "TestBook",
        "registration_code": "TEST_CODE12345",
        "main_author": not_exists_author_id
    }

    response: Response = client.post(get_author_url, data, **get_auth_header)

    assert HTTPStatus.BAD_REQUEST == response.status_code


@pytest.mark.django_db
def test_list_books(client: Client, get_author_url):
    response: Response = client.get(get_author_url)

    assert HTTPStatus.OK == response.status_code

