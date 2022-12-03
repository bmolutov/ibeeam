from rest_framework import serializers

from posts.models import Post
from utils.serializers import Base64ImageField


class PostCreateSerializer(serializers.Serializer): # noqa
    user_id = serializers.SerializerMethodField()
    image = serializers.ImageField(
        required=False
    )
    title = serializers.CharField(
        max_length=256
    )
    content = serializers.CharField(
        max_length=2048
    )

    def create(self, validated_data):
        validated_data.update({
            'user_id': self.context.get('request').user.id
        })
        return Post.objects.create(**validated_data)

    def get_user_id(self, obj):
        return self.context.get('request').user.id


class PostUpdateSerializer(serializers.Serializer): # noqa
    image = serializers.ImageField(
        required=False
    )
    title = serializers.CharField(
        max_length=256
    )
    content = serializers.CharField(
        max_length=2048
    )

    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance


class PostListSerializer(serializers.Serializer): # noqa
    id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    # TODO: what to do with this field?
    # image = serializers.ImageField(
    #     required=False
    # )
    # image = Base64ImageField(
    #     max_length=None,
    #     use_url=True,
    #     required=False,
    #     allow_empty_file=True,
    #     allow_null=True
    # )
    # ???
    # image = serializers.CharField(
    #     max_length=1024,
    #     required=False
    # )
    title = serializers.CharField(
        max_length=256
    )
    content = serializers.CharField(
        max_length=2048
    )
    views_count = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class PostReactionCreateSerializer(serializers.Serializer): # noqa
    user_id = serializers.SerializerMethodField()
    post_id = serializers.IntegerField()
    is_liked = serializers.BooleanField(
        default=False
    )

    def get_user_id(self, obj):
        return self.context.get('request').user.id


class FavoritePostsListSerializer(serializers.Serializer): # noqa
    ids = serializers.ListField(
        child=serializers.IntegerField(
            min_value=1
        )
    )
