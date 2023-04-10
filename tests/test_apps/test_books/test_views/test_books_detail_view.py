from http import HTTPStatus

import pytest
from django.test import Client
from django.urls import reverse
from rest_framework.response import Response

from server.apps.author.models import Author
from server.apps.books.models import Book


@pytest.mark.django_db()
def test_get_book(client: Client, get_book_url, get_book_initial_data, get_book):
    response: Response = client.get(get_book_url)

    assert response.status_code == HTTPStatus.OK
    assert {
            **get_book_initial_data,
            "id": get_book.id,
            "main_author": get_book_initial_data.get('main_author').id
        } == response.data


@pytest.mark.django_db()
def test_update_book(client: Client, get_auth_header, get_book_url):
    new_book_data = {
        "registration_code": "NEW_REGISTRATION_CODE_120312931"
    }

    response: Response = client.put(get_book_url, data=new_book_data, content_type='application/json', **get_auth_header)

    print(response)
    assert response.data.get('registration_code') == new_book_data.get('registration_code')


@pytest.mark.django_db()
def test_delete_book(client: Client, get_auth_header, get_book_url):
    response: Response = client.delete(get_book_url, **get_auth_header)
    assert response.status_code == HTTPStatus.NO_CONTENT

    response: Response = client.get(get_book_url, **get_auth_header)
    assert response.status_code == HTTPStatus.NOT_FOUND


@pytest.fixture()
def get_author():
    author = Author.objects.create(surname="TestSurname", name="TestName")

    yield author

    author.delete()


@pytest.fixture()
def get_author_url(get_author):
    return reverse("books:list")


@pytest.fixture()
def get_book_initial_data(get_author):
    return {
        "name": "TestBook",
        "registration_code": "102N81298-12745",
        "main_author": get_author
    }


@pytest.fixture()
def get_book(get_author, get_book_initial_data):
    book_initial_data = get_book_initial_data
    book = Book.objects.create(**book_initial_data)

    yield book

    book.delete()


@pytest.fixture()
def get_book_url(get_book):
    return reverse("books:detail", kwargs={"pk": get_book.id})

