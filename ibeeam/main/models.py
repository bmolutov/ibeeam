from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, AbstractUser
)
from django.conf import settings

from mixins.models import TimestampMixin
from posts.models import Post


# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         """
#         Creates and saves a User with the given email, date of
#         birth and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         user = self.model(
#             email=self.normalize_email(email),
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password=None):
#         """
#         Creates and saves a superuser with the given email, date of
#         birth and password.
#         """
#         user = self.create_user(
#             email,
#             password=password
#         )
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
#

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
