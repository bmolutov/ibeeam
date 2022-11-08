from django.db import models


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date and time of create'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Date and time of update'
    )

    class Meta:
        abstract = True
