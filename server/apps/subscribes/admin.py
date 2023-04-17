from django.contrib import admin

from server.apps.subscribes.models import Subscriber, Subscribe, Event

admin.site.register(Subscriber)
admin.site.register(Subscribe)
admin.site.register(Event)
