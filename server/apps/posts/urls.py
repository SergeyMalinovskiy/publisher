from django.urls import path, include
from rest_framework.routers import DefaultRouter

from server.apps.posts.views import PostsViewSet

app_name = 'posts'

router = DefaultRouter()
router.register('', PostsViewSet)

urlpatterns = [
    path('', include(router.urls))
]

