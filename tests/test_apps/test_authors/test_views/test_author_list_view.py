import random
from typing import List

import pytest
from http import HTTPStatus

from django.db.models import Model
from django.test import Client
from django.urls import reverse
from faker import Faker
from rest_framework.response import Response

from server.apps.author.models import Author


@pytest.mark.django_db()
def test_create_author(client: Client, get_author_url, get_auth_header):
    data = {
        "surname": "Test",
        "name": "Test"
    }

    response: Response = client.post(get_author_url, data=data, **get_auth_header)

    assert response.status_code == HTTPStatus.CREATED


@pytest.mark.django_db()
def test_get_authors(client: Client, get_author_url: List[Model]) -> None:
    """Testing authors list"""
    response: Response = client.get(get_author_url)

    assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db()
def test_filtering_authors(
    client: Client,
    get_author_url: str,
    get_faked_authors: List[Author],
) -> None:
    """Test filters"""
    authors = get_faked_authors

    rand_author: Author = random.choice(authors)
    authors_count = len(list(filter(
        lambda author: author.name == rand_author.name,
        authors,
    )))

    query_params = {'name': rand_author.name}
    response: Response = client.get(get_author_url, query_params)

    assert len(list(response.data)) == authors_count


@pytest.fixture()
def get_author_url() -> str:
    """Returns authors list URI"""
    return reverse('authors:list')


@pytest.fixture()
def faker() -> Faker:
    """Initialize faker"""
    return Faker()


@pytest.fixture()
def get_faked_authors(faker: Faker) -> List[Author]:
    """Returns mocked authors list"""
    authors = []

    for _ in range(10):
        authors.append(Author.objects.create(
            surname=faker.first_name(),
            name=faker.last_name(),
            license_code=faker.unique.random_number(digits=11),
        ))

    ids = [author.id for author in authors]

    yield authors

    Author.objects.filter(pk__in=ids).delete()

