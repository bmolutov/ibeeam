from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)

from main.models import UserManager
from utils.generators import generate_password


class User(AbstractBaseUser, PermissionsMixin):
    profile_id = models.CharField(
        max_length=256,
        unique=True
    )
    password = models.CharField(
        max_length=128,
        default=generate_password(16)
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

    USERNAME_FIELD = 'profile_id'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
