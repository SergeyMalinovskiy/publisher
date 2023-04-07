from django.urls import path, include
from rest_framework.routers import SimpleRouter

from server.apps.publisher.views import PublisherViewSet

app_name = 'publishers'

router = SimpleRouter()
router.register("", PublisherViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("<int:pk>/", PublisherViewSet.as_view, name='detail')
]
