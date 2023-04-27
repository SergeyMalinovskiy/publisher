from factory import Factory, Faker, SubFactory, RelatedFactoryList
from factory.fuzzy import FuzzyText

from server.apps.author.factories import AuthorFactory
from server.apps.books.models import Book


class BookFactory(Factory):
    """Book factory"""

    class Meta(type):
        model = Book

    name = Faker('sentence', nb_words=4)
    registration_code = FuzzyText(
        length=10,
        chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',
    )

    main_author = SubFactory(AuthorFactory)
    other_authors = RelatedFactoryList(
        AuthorFactory,
        size=3,
    )

