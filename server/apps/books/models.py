from dataclasses import dataclass

from django.db import models

from server.apps.author.models import Author
from server.common.base_model import BaseModel


@dataclass(frozen=True)
class BookAuthorType(object):
    """Book author type"""

    main_author: str = 'main_author'
    other_author: str = 'other_author'


class Book(BaseModel):
    """Book model"""

    name = models.CharField(max_length=255)
    registration_code = models.CharField(max_length=255, unique=True)

    main_author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        name=BookAuthorType.main_author,
    )

    other_authors = models.ManyToManyField(
        Author,
        related_name=BookAuthorType.other_author,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """Returns stringify model"""
        return '{name}'.format(name=self.name)
