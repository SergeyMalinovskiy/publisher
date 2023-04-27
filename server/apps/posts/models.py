from django.db import models

from server.apps.books.models import Book
from server.apps.publisher.models import Publisher
from server.common.base_model import BaseModel


# Create your models here.
class Post(BaseModel):
    """Post model"""

    title = models.CharField(null=False, max_length=255)
    cover_image = models.FileField(upload_to="uploads/%Y/%m/%d/")
    is_active = models.BooleanField(default=False)

    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
    books = models.ManyToManyField(Book, null=True)

    publication_datetime = models.DateTimeField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """Returns stringify model"""
        return '{title}'.format(title=self.title)
