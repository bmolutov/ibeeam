from rest_framework import viewsets

from comments.serializers import PostCommentSerializer
from comments.models import PostComment
from comments.permissions import CommentAuthorOrReadOnly


class PostCommentViewSet(viewsets.ModelViewSet):
    permission_classes = (CommentAuthorOrReadOnly,)
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
