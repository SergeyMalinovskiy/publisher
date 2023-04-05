from django.db import models

from server.apps.author.models import Author


# Create your models here.
class Book(models.Model):
    class BookAuthorType:
        MAIN_AUTHOR = 'main_author'
        OTHER_AUTHOR = 'other_author'

    name = models.CharField(max_length=255)
    registration_code = models.CharField(max_length=255, unique=True)

    main_author = models.ForeignKey(Author, on_delete=models.CASCADE, name=BookAuthorType.MAIN_AUTHOR)

    other_authors = models.ManyToManyField(Author, related_name=BookAuthorType.OTHER_AUTHOR)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.main_author, self.name)
