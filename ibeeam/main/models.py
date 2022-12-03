from django.db import models
from django.conf import settings


class UserSearchHistory(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='history'
    )
    keyword = models.TextField(
        verbose_name='keyword'
    )

    class Meta:
        verbose_name = 'Search history'
        verbose_name_plural = 'Search history'


class Feedback(models.Model):
    email = models.EmailField(
        verbose_name='email address',
        max_length=256
    )
    content = models.CharField(
        max_length=1024,
        verbose_name='feedback content'
    )

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'
