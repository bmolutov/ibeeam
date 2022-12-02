import os
from celery import Celery

from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ibeeam.settings")
app = Celery("ibeeam")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.broker_url = f'{settings.CELERY_BROKER_URL}/0'
app.conf.result_backend = f'{settings.CELERY_BROKER_URL}/0'
