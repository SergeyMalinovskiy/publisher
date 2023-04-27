from django.db import models
from django.db.models import Manager
from django.utils import timezone


class BaseModel(models.Model):
    """Base Django model"""

    objects: Manager

    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(type):
        abstract = True
