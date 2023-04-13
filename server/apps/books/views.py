from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from server.apps.books.serializers import BookSerializer, BookUpdateSerializer
from server.apps.books.models import Book
from server.apps.books.repository import BookRepository
from server.utils.decorators import TokenAuthenticatedOrReadOnly


@TokenAuthenticatedOrReadOnly()
class BookListView(APIView):
    """
    Responses for list of books.
    """

    def get(self, request: Request) -> Response:
        """
        Get lists of books.
        """
        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        """
        Create new book.
        """
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@TokenAuthenticatedOrReadOnly()
class BookDetailView(APIView):
    """
    Responses for detail view of book.
    """

    def get(self, request: Request, pk: int) -> Response:
        """
        Get book by ID.
        """
        book = BookRepository().get_by_id(pk)

        return Response(BookSerializer(book).data)

    def put(self, request: Request, pk: int) -> Response:
        """
        Update book.
        """
        book = BookRepository().get_by_id(pk)

        serializer = BookUpdateSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int) -> Response:
        """
        Delete book.
        """
        book = BookRepository().get_by_id(pk)
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
