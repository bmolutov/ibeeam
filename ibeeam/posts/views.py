from rest_framework import viewsets

from posts.models import Post
from posts.serializers import PostSerializer
from posts.permissions import PostAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (PostAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
