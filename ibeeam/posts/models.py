from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, AbstractUser
)
from django.core.validators import MinValueValidator

from mixins.models import TimestampMixin


class Post(TimestampMixin):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    title = models.CharField(
        max_length=256,
        verbose_name='title'
    )
    content = models.CharField(
        max_length=2048,
        verbose_name='content'
    )
    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name="views count",
        validators=[MinValueValidator(1)]
    )

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class PostTag(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='tags'
    )
    title = models.CharField(
        max_length=256,
        verbose_name='title'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='description'
    )

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
