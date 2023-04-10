from rest_framework.viewsets import ModelViewSet

from server.apps.posts.models import Post
from server.apps.posts.serializers import PostSerializer
from server.utils.decorators import TokenAuthenticatedOrReadOnly


@TokenAuthenticatedOrReadOnly()
class PostsViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
