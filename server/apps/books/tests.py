from django.urls import reverse
from rest_framework.response import Response
from rest_framework.test import APITestCase

from ..author.models import Author
from .models import Book


# Create your tests here.
class BooksListAPIViewTestCase(APITestCase):
    url = reverse("books:list")

    def setUp(self) -> None:
        self.author = Author.objects.create(surname="TestSurname", name="TestName")

    def test_create_books(self):
        data = {
            "name": "TestBook",
            "registration_code": "TEST_CODE12345",
            "main_author": self.author.id
        }
        response: Response = self.client.post(self.url, data)

        self.assertEqual(201, response.status_code)

        del response.data['id']
        self.assertDictEqual(data, response.data)

    def test_create_books_with_not_exists_author(self):
        not_exists_author_id: int = Author.objects.latest('id').id+1

        data = {
            "name": "TestBook",
            "registration_code": "TEST_CODE12345",
            "main_author": not_exists_author_id
        }

        response: Response = self.client.post(self.url, data)

        self.assertEqual(400, response.status_code)

    def test_list_books(self):
        response: Response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)


class BooksDetailAPIViewTestCase(APITestCase):
    def setUp(self) -> None:
        self.author = Author.objects.create(surname="TestSurname", name="TestName")

        self.book_initial_data = {
            "name": "TestBook",
            "registration_code": "102N81298-12745",
            "main_author": self.author
        }

        self.book = Book.objects.create(**self.book_initial_data)
        self.url = reverse("books:detail", kwargs={"pk": self.book.id})

    def test_get_book(self):
        response: Response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)
        self.assertDictEqual(
            {
                **self.book_initial_data,
                "id": self.book.id,
                "main_author": self.book_initial_data.get('main_author').id
            },
            response.data
        )

    def test_update_book(self):
        new_book_data = {
            "registration_code": "NEW_REGISTRATION_CODE_120312931"
        }

        response: Response = self.client.put(self.url, data=new_book_data)
        self.assertEqual(response.data.get('registration_code'), new_book_data.get('registration_code'))

    def test_delete_book(self):
        response: Response = self.client.delete(self.url)
        self.assertEqual(204, response.status_code)

        response: Response = self.client.get(self.url)
        self.assertEqual(404, response.status_code)

