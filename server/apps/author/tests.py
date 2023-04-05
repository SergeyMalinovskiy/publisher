from django.test import TestCase
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.test import APITestCase

from server.apps.author.models import Author


# Create your tests here.
class AuthorListAPIViewTestCase(APITestCase):
    url = reverse("authors:list")

    def setUp(self) -> None:
        pass

    def test_create_author(self) -> None:
        response: Response = self.client.post(self.url, {"surname": "Test", "name": "Test"})
        self.assertEqual(201, response.status_code)

    def test_list_author(self) -> None:
        response: Response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)


class AuthorDetailAPIViewTestCase(APITestCase):
    def setUp(self) -> None:
        self.author = Author.objects.create(surname='TestSurname', name='TestName', license_code='1234567890')
        self.url = reverse("authors:detail", kwargs={"pk": self.author.id})

    def test_update_author(self):
        data = [
            ("name",            "TestNewName"),
            ("surname",         "TestNewSurname"),
            ("license_code",    "new_license_code"),
        ]

        for field, new_value in data:
            new_field_value = "TestNewName"

            response: Response = self.client.put(self.url, data={field: new_field_value})

            self.assertEqual(200, response.status_code)
            self.assertEqual(new_field_value, dict(response.data).get(field))

    def test_delete_author(self):
        response: Response = self.client.delete(self.url)
        self.assertEqual(204, response.status_code)

        response: Response = self.client.get(self.url)
        self.assertEqual(404, response.status_code)
