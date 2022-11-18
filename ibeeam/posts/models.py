from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

from mixins.models import TimestampMixin
from utils.upload import get_post_image_path


class Post(TimestampMixin):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    image = models.ImageField(
        upload_to=get_post_image_path,
        blank=True,
        null=True
    )
    title = models.CharField(
        max_length=256,
        verbose_name='title',
    )
    content = models.CharField(
        max_length=2048,
        verbose_name='content',
        blank=True,
        null=True
    )
    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name="views count",
        validators=[MinValueValidator(1)]
    )

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class PostReaction(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='own_post_reactions'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='post_reactions'
    )
    is_liked = models.BooleanField(
        default=False
    )

    class Meta:
        verbose_name = 'Reaction'
        verbose_name_plural = 'Reactions'
