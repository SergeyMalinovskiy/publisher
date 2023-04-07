from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from server.apps.books.serializers import BookSerializer, BookUpdateSerializer
from server.apps.books.models import Book
from server.apps.books.repository import BookRepository
from server.utils.decorators import TokenAuthenticatedOrReadOnly


@TokenAuthenticatedOrReadOnly()
class BookListView(APIView):
    def get(self, request: Request, format=None) -> Response:
        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)

        return Response(serializer.data)

    def post(self, request: Request, format=None) -> Response:
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@TokenAuthenticatedOrReadOnly()
class BookDetailView(APIView):
    def get(self, request: Request, pk, format=None):
        book = BookRepository().get_by_id(pk)

        return Response(BookSerializer(book).data)

    def put(self, request: Request, pk, format=None):
        book = BookRepository().get_by_id(pk)

        serializer = BookUpdateSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk, format=None):
        book = BookRepository().get_by_id(pk)
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
