from django.http import Http404

from .models import Book


class BookRepository:
    def get_by_id(self, pk: int) -> Book:
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404
