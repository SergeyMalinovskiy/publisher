from rest_framework.serializers import ModelSerializer

from server.apps.books.models import Book
from server.apps.posts.models import Post


# class PostBooksSerializer(ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ["id"]
#

class PostSerializer(ModelSerializer):
    # books = PostBooksSerializer(many=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "is_active",
            "publisher",
            "created_at",
            "updated_at"
        ]


