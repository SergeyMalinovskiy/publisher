from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(unique=True, null=False, max_length=255)
    org_site = models.URLField(null=False, max_length=255)
    email = models.EmailField(unique=True, null=False, max_length=255)
    is_confirmed = models.BooleanField(null=False, default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
