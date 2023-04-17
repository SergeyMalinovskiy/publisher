from django.contrib import admin

from server.apps.subscribes.models import Subscriber, Subscribe


admin.site.register(Subscriber)
admin.site.register(Subscribe)
