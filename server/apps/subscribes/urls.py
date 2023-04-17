from django.urls import path

from server.apps.subscribes.views import SubscribesAPIView

app_name = 'subscribes'

urlpatterns = [
    path('', SubscribesAPIView.as_view()),
    path('<slug:event>/', SubscribesAPIView.as_view()),
]
