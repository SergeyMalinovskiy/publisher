from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from server.apps.books.views import BookListView, BookDetailView

app_name = "books"

urlpatterns = [
    path("", BookListView.as_view(), name="list"),
    path("<int:pk>", BookDetailView.as_view(), name="detail")
]

urlpatterns = format_suffix_patterns(urlpatterns)
