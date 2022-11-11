from django.db import models
from django.contrib.auth.models import (
    BaseUserManager
)
from django.conf import settings


class UserManager(BaseUserManager):
    def create_user(self, profile_id, password=None):
        if not profile_id:
            raise ValueError('Users must have a profile_id')

        user = self.model(
            profile_id=profile_id
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, profile_id, password=None):
        user = self.create_user(
            profile_id=profile_id,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


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
