from rest_framework.serializers import ModelSerializer

from server.apps.posts.models import Post


class PostSerializer(ModelSerializer):
    """Post in/out model serializer"""

    class Meta(type):
        model = Post
        fields = [
            'id',
            'title',
            'is_active',
            'publisher',
            'created_at',
            'updated_at',
        ]
