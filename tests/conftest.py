"""
This module is used to provide configuration, fixtures, and plugins for pytest.

It may be also used for extending doctest's context:
1. https://docs.python.org/3/library/doctest.html
2. https://docs.pytest.org/en/latest/doctest.html
"""
from typing import Dict

import pytest
from django.contrib.auth import get_user_model
from faker import Faker
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture(autouse=True)
def _media_root(settings, tmpdir_factory) -> None:
    """Forces django to save media files into temp folder."""
    settings.MEDIA_ROOT = tmpdir_factory.mktemp('media', numbered=True)


@pytest.fixture(autouse=True)
def _password_hashers(settings) -> None:
    """Forces django to use fast password hashers for tests."""
    settings.PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.MD5PasswordHasher',
    ]


@pytest.fixture(autouse=True)
def _auth_backends(settings) -> None:
    """Deactivates security backend from Axes app."""
    settings.AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
    )


@pytest.fixture(autouse=True)
def _debug(settings) -> None:
    """Sets proper DEBUG and TEMPLATE debug mode for coverage."""
    settings.DEBUG = False
    for template in settings.TEMPLATES:
        template['OPTIONS']['debug'] = True


@pytest.fixture()
def main_heading() -> str:
    """An example fixture containing some html fragment."""
    return '<h1>wemake-django-template</h1>'


@pytest.fixture()
def get_django_user():
    user = get_user_model().objects.create(username='username')

    user.set_password('12345678')
    user.save()

    yield user

    user.delete()


@pytest.fixture()
def get_auth_token(get_django_user):
    refresh = RefreshToken.for_user(get_django_user)

    return refresh.access_token


@pytest.fixture()
def get_auth_header(get_auth_token) -> Dict:
    return {"HTTP_AUTHORIZATION": f'Bearer {get_auth_token}'}


@pytest.fixture()
def faker() -> Faker:
    """Init faker"""
    return Faker()
