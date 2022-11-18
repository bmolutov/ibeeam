from rest_framework import serializers

from comments.models import Comment


class CommentCreateSerializer(serializers.Serializer): # noqa
    user_id = serializers.SerializerMethodField()
    post_id = serializers.IntegerField()
    parent_comment_id = serializers.IntegerField(
        required=False
    )
    content = serializers.CharField(
        max_length=2048
    )

    def create(self, validated_data):
        validated_data.update({
            'user_id': self.context.get('request').user.id
        })
        return Comment.objects.create(**validated_data)

    def get_user_id(self, obj):
        return self.context.get('request').user.id


class CommentUpdateSerializer(serializers.Serializer): # noqa
    content = serializers.CharField(
        max_length=2048
    )

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance


class CommentListSerializer(serializers.Serializer): # noqa
    id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    post_id = serializers.IntegerField()
    parent_comment_id = serializers.IntegerField(
        required=False
    )
    content = serializers.CharField(
        max_length=2048
    )
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class CommentReactionSerializer(serializers.Serializer): # noqa
    user_id = serializers.SerializerMethodField()
    comment_id = serializers.IntegerField()
    is_liked = serializers.BooleanField(
        default=False
    )

    def get_user_id(self, obj):
        return self.context.get('request').user.id
