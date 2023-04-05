import json
from http import HTTPStatus

import pytest
from django.test import TestCase
from django.urls import reverse
from rest_framework.response import Response

from server.apps.author.models import Author


@pytest.mark.django_db()
class AuthorDetailViewTest(TestCase):
    def setup_class(self) -> None:
        self.author = Author.objects.create(surname='TestSurname', name='TestName', license_code='1234567890')
        self.url = reverse("authors:detail", kwargs={"pk": self.author.id})


    def test_update_author(self):
        data = [
            ("name", "TestNewName"),
            ("surname", "TestNewSurname"),
            ("license_code", "new_license_code"),
        ]

        for field, new_value in data:
            new_field_value = "TestNewName"

            response: Response = self.client.put(
                                    self.url,
                                    data=json.dumps({field: new_field_value}),
                                    content_type='application/json'
                                )

            assert response.status_code == HTTPStatus.OK
            assert new_field_value == dict(response.data).get(field)

    def test_delete_author(self):
        response: Response = self.client.delete(self.url)
        assert response.status_code == HTTPStatus.NO_CONTENT

        response: Response = self.client.get(self.url)
        assert response.status_code == HTTPStatus.NOT_FOUND
