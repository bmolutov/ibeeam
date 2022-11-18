from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist

from posts.models import Post, PostReaction
from posts.serializers import (
    PostCreateSerializer, PostUpdateSerializer, PostListSerializer, PostReactionCreateSerializer
)
from posts.permissions import PostAuthorOrReadOnly, PostReactionAuthorOrReadOnly


class PostViewSet(viewsets.GenericViewSet):
    lookup_field = 'pk'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            "request": self.request
        })
        return context

    def get_permission_class(self):
        # if self.action == 'like':
        #     return PostReactionAuthorOrReadOnly
        # return PostAuthorOrReadOnly
        pass

    permission_classes = [IsAuthenticated, ]

    def get_queryset(self, *args, **kwargs):
        if self.action == 'like':
            return PostReaction.objects.all()
        return Post.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'like':
            return PostReactionCreateSerializer
        elif self.action == 'edit':
            return PostUpdateSerializer
        elif self.action == 'create':
            return PostCreateSerializer
        elif self.action == 'list':
            return PostListSerializer
        return None

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def edit(self, request, *args, **kwargs):
        pk = kwargs.get('id', None)
        try:
            instance = Post.objects.get(pk=pk, user_id=self.request.user.id)
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

    def delete(self, request, *args, **kwargs):  # noqa
        pk = kwargs.get('id', None)
        if not pk:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            instance = Post.objects.get(pk=pk, user_id=self.request.user.id)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def like(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = PostReaction.objects.filter(
            user_id=serializer.data['user_id'],
            post_id=serializer.data['post_id']
        )
        if not instance:
            post_reaction = PostReaction(**serializer.data)
            post_reaction.save()
        else:
            instance.update(**serializer.data)
        return Response(status=status.HTTP_200_OK)
