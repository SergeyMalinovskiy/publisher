from django.db import models

from server.apps.subscribes.interfaces.subscribe_method import SubscribeMethod
from server.apps.subscribes.methods import resolve_subscribe_method
from server.common.base_model import BaseModel


class Subscriber(BaseModel):
    """Subscriber model"""

    method = models.CharField(max_length=255)
    method_data = models.JSONField(null=True)
    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(type):
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

    def __str__(self) -> str:
        """Returns stringify model"""
        return '({id}): {method} | {data}'.format(
            id=self.pk,
            method=self.method,
            data=self.method_data,
        )

    @property
    def subscribe_method(self) -> SubscribeMethod:
        """Returns subscribe method"""
        return resolve_subscribe_method(self.method, self.method_data)


class Event(BaseModel):
    """Event model"""

    name = models.CharField(unique=True, max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(type):
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self) -> str:
        """Returns stringify model"""
        return '{name}'.format(name=self.name)


class Subscribe(BaseModel):
    """Subscribe model"""

    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)

    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    valid_until_date = models.DateTimeField(null=True, blank=True)

    class Meta(type):
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self) -> str:
        """Returns stringify model"""
        return '{id}: {event}'.format(id=self.id, event=self.event)


