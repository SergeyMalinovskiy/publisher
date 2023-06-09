from django.http import QueryDict
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from server.apps.author.models import Author
from server.apps.author.serializers import (
    AuthorSerializer,
    AuthorUpdateSerializer,
)
from server.apps.author.repository import AuthorRepository
from server.utils.decorators import TokenAuthenticatedOrReadOnly


@TokenAuthenticatedOrReadOnly()
class AuthorListView(APIView):
    """Handle list of authors"""

    def get(self, request: Request) -> Response:
        """Get authors list"""
        query_params: QueryDict = request.query_params

        authors = Author.objects.filter(
            name=query_params.get('name', None),
        )

        serializer = AuthorSerializer(authors, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@TokenAuthenticatedOrReadOnly()
class AuthorDetailView(APIView):

    def get(self, request: Request, pk, format=None):
        author = self._get_author_by_id(pk)

        return Response((AuthorSerializer(author)).data)

    def put(self, request: Request, pk, format=None):
        print(request.data)
        author = self._get_author_by_id(pk)

        serializer = AuthorUpdateSerializer(author, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk, format=None):
        author = self._get_author_by_id(pk)
        author.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def _get_author_by_id(self, pk) -> Author:
        return AuthorRepository().get_by_id(pk)
