from django.db import models
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey

from mixins.models import TimestampMixin
from posts.models import Post


class Comment(MPTTModel, TimestampMixin):
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
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    content = models.CharField(
        max_length=2048,
        verbose_name='content'
    )

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    class MPTTMeta:
        order_insertion_by = ['created_at']


class CommentReaction(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='own_comment_reactions'
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='comment_reactions'
    )
    is_liked = models.BooleanField(
        default=False
    )

    class Meta:
        verbose_name = 'Reaction'
        verbose_name_plural = 'Reactions'
