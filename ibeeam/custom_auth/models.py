from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, AbstractUser
)

from utils.upload import get_user_avatar_path
from mixins.models import TimestampMixin
from posts.models import Post
from main.models import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=256,
        unique=True,
    )
    avatar = models.ImageField(
        upload_to=get_user_avatar_path,
        blank=True,
        null=True,
        verbose_name='avatar'
    )
    gender = models.CharField(
        blank=True,
        null=True,
        choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')],
        max_length=64,
        verbose_name='gender'
    )
    bio = models.TextField(
        blank=True,
        null=True,
        verbose_name='biography'
    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
        verbose_name='date of birth'
    )
    is_active = models.BooleanField(
        default=True,
        help_text='is the user active?'
    )
    is_staff = models.BooleanField(
        verbose_name='staff status',
        default=False,
        help_text='designates whether the user can log into this admin site',
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
