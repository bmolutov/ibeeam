from rest_framework import serializers

from comments.models import PostComment


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = ('id', 'user', 'post', 'content')
