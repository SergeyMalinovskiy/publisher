from django.db import models

from server.apps.books.models import Book
from server.apps.publisher.models import Publisher


# Create your models here.
class Post(models.Model):
    title = models.CharField(null=False, max_length=255)
    cover_image = models.FileField(upload_to="uploads/%Y/%m/%d/")
    is_active = models.BooleanField(default=False)

    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
    books = models.ManyToManyField(Book, null=True)

    publication_datetime = models.DateTimeField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
