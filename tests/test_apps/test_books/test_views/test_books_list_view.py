from http import HTTPStatus

import pytest
from django.test import TestCase
from django.urls import reverse
from rest_framework.response import Response

from server.apps.author.models import Author


@pytest.mark.django_db()
class BooksListViewTest(TestCase):
    url = reverse("books:list")

    def setup_class(self) -> None:
        self.author = Author.objects.create(surname="TestSurname", name="TestName")

    def teardown_class(self):
        self.author.delete()

    def test_create_books(self):
        data = {
            "name": "TestBook",
            "registration_code": "TEST_CODE12345",
            "main_author": self.author.id
        }
        response: Response = self.client.post(self.url, data)

        assert HTTPStatus.CREATED == response.status_code

        del response.data['id']
        assert data == response.data

    def test_create_books_with_not_exists_author(self):
        not_exists_author_id: int = Author.objects.latest('id').id+1

        data = {
            "name": "TestBook",
            "registration_code": "TEST_CODE12345",
            "main_author": not_exists_author_id
        }

        response: Response = self.client.post(self.url, data)

        assert HTTPStatus.BAD_REQUEST == response.status_code

    def test_list_books(self):
        response: Response = self.client.get(self.url)

        assert HTTPStatus.OK == response.status_code

