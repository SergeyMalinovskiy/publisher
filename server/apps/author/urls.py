from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from server.apps.author.views import AuthorListView, AuthorDetailView

app_name = 'authors'

urlpatterns = [
    path('', AuthorListView.as_view(), name='list'),
    path('<int:pk>', AuthorDetailView.as_view(), name='detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
