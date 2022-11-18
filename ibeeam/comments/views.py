from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated

from comments.serializers import (
    CommentReactionSerializer, CommentCreateSerializer, CommentUpdateSerializer, CommentListSerializer
)
from comments.models import Comment, CommentReaction
from comments.permissions import CommentAuthorOrReadOnly, CommentReactionAuthorOrReadOnly


class CommentViewSet(viewsets.GenericViewSet):
    lookup_field = 'pk'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            "request": self.request
        })
        return context

    # def get_permission_class(self):
    #     if self.action == 'like':
    #         return CommentReactionAuthorOrReadOnly
    #     return CommentAuthorOrReadOnly

    permission_classes = [IsAuthenticated, ]

    def get_queryset(self, *args, **kwargs):
        if self.action == 'like':
            return CommentReaction.objects.all()
        return Comment.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'like':
            return CommentReactionSerializer
        elif self.action == 'update':
            return CommentUpdateSerializer
        elif self.action == 'leave':
            return CommentCreateSerializer
        elif self.action == 'list':
            return CommentListSerializer
        return None

    def leave(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('id', None)
        try:
            instance = Comment.objects.get(pk=pk, user_id=self.request.user.id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs): # noqa
        pk = kwargs.get('id', None)
        if not pk:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            instance = Comment.objects.get(pk=pk, user_id=self.request.user.id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def like(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = CommentReaction.objects.filter(
            user_id=serializer.data['user_id'],
            comment_id=serializer.data['comment_id']
        )
        if not instance:
            comment_reaction = CommentReaction(**serializer.data)
            comment_reaction.save()
        else:
            instance.update(**serializer.data)
        return Response(status=status.HTTP_200_OK)
