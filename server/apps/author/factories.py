import abc

from factory import Factory, Faker
from factory.fuzzy import FuzzyText

from server.apps.author.models import Author


class AuthorFactory(Factory):
    """Author model"""

    class Meta(type):
        model = Author

    surname = Faker('last_name')
    name = Faker('first_name')

    license_code = FuzzyText(
        length=10,
        chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',
    )
