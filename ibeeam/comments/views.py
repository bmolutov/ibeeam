from rest_framework import viewsets

from comments.serializers import PostCommentSerializer
from comments.models import Comment
from comments.permissions import CommentAuthorOrReadOnly


class PostCommentViewSet(viewsets.ModelViewSet):
    permission_classes = (CommentAuthorOrReadOnly,)
    queryset = Comment.objects.all()
    serializer_class = PostCommentSerializer
