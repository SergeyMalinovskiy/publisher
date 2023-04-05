from django.db import models


# Create your models here.
class Author(models.Model):
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    license_code = models.CharField(max_length=255, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.surname, self.name)
