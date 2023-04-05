import pytest
from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse
from rest_framework.response import Response

from server.apps.author.models import Author


class AuthorListViewTest(TestCase):
    url = reverse('authors:list')

    @pytest.mark.django_db()
    def test_create_author(self):
        data = {
            "surname": "Test",
            "name": "Test"
        }

        response: Response = self.client.post(self.url, data=data)

        assert response.status_code == HTTPStatus.CREATED

    @pytest.mark.django_db()
    def test_get_authors(self):
        response: Response = self.client.get(self.url)

        assert response.status_code == HTTPStatus.OK
