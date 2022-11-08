from mixins.models import TimestampMixin
from posts.models import Post
from django.db import models
from django.conf import settings


class PostComment(TimestampMixin):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.CharField(
        max_length=2048,
        verbose_name='content'
    )

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class CommentReaction(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reactions'
    )
    comment = models.ForeignKey(
        PostComment,
        on_delete=models.CASCADE,
        related_name='reactions'
    )
    emoji_url = models.CharField(
        max_length=512,
        verbose_name='url'
    )

    class Meta:
        verbose_name = 'Reaction'
        verbose_name_plural = 'Reactions'
