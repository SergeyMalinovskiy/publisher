from http import HTTPStatus

import pytest
from django.test import TestCase
from django.urls import reverse
from rest_framework.response import Response

from server.apps.author.models import Author
from server.apps.books.models import Book


@pytest.mark.django_db()
class BooksDetailViewTest(TestCase):
    def setup_class(self) -> None:
        self.author = Author.objects.create(surname="TestSurname", name="TestName")

        self.book_initial_data = {
            "name": "TestBook",
            "registration_code": "102N81298-12745",
            "main_author": self.author
        }

        self.book = Book.objects.create(**self.book_initial_data)
        self.url = reverse("books:detail", kwargs={"pk": self.book.id})

    def teardown_class(self):
        self.author.delete()

    def test_get_book(self):
        response: Response = self.client.get(self.url)

        assert response.status_code == HTTPStatus.OK
        assert {
                **self.book_initial_data,
                "id": self.book.id,
                "main_author": self.book_initial_data.get('main_author').id
            } == response.data

    def test_update_book(self):
        new_book_data = {
            "registration_code": "NEW_REGISTRATION_CODE_120312931"
        }

        response: Response = self.client.put(self.url, data=new_book_data, content_type='application/json')
        print({'data': response.data})
        assert response.data.get('registration_code') == new_book_data.get('registration_code')

    def test_delete_book(self):
        response: Response = self.client.delete(self.url)
        assert response.status_code == HTTPStatus.NO_CONTENT

        response: Response = self.client.get(self.url)
        assert response.status_code == HTTPStatus.NOT_FOUND

