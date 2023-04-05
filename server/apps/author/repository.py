from django.http import Http404

from .models import Author


class AuthorRepository:
    def get_by_id(self, pk: int) -> Author:
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404
