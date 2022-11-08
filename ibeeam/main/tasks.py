from time import sleep
from celery import shared_task

from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_feedback_email_task(email):
    sleep(5)
    send_mail(
        subject='You left feedback',
        message='We will take into account you suggestions, thank you',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
