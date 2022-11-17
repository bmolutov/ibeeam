from rest_framework import serializers

from comments.models import Comment


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'user', 'post', 'content')
