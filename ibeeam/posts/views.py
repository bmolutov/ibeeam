from rest_framework import viewsets, generics, filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from django.core.exceptions import ObjectDoesNotExist

from posts.models import Post, PostReaction
from posts.serializers import (
    PostCreateSerializer, PostUpdateSerializer, PostListSerializer, PostReactionCreateSerializer,
    FavoritePostsListSerializer
)
from custom_auth.integration import get_favorite_posts_ids
from custom_auth.models import User
from posts.permissions import PostAuthorOrReadOnly, PostReactionAuthorOrReadOnly


class PostViewSet(viewsets.GenericViewSet):
    lookup_field = 'pk'
    parser_classes = [MultiPartParser, ]

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

    def list_favorites(self, request, *args, **kwargs): # noqa
        user_id = kwargs.get('user_id', None)
        # trying to get profile_id using user_id
        try:
            profile_id = User.objects.get(id=user_id).profile_id
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # validating list of ids
        result = get_favorite_posts_ids(profile_id)

        ids_serializer = FavoritePostsListSerializer(data=result)
        ids_serializer.is_valid(raise_exception=True)

        # getting list of favorite posts
        serializer = PostListSerializer(
            data=list(Post.objects.filter(id__in=ids_serializer.data['ids']).values()),
            many=True
        )
        serializer.is_valid(raise_exception=True)

        # returning result
        return Response(serializer.data, status=status.HTTP_200_OK)

class SearchPostView(generics.ListAPIView):
    pagination_class = None
    serializer_class = PostListSerializer
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    permission_classes = [IsAuthenticated, ]
    def get_queryset(self):
        queryset = Post.objects.all()
        pattern = self.request.query_params.get('pattern')
        if pattern is not None:
            queryset = queryset.filter(title__contains=pattern)
        return queryset.order_by('-updated_at')