from time import sleep
from celery import shared_task

from django.core.mail import EmailMessage


@shared_task
def send_feedback_email_task(email):
    print('******************************')
    print(f'Feedback from {email}')
    print('******************************')
    sleep(3)
    msg = EmailMessage(
        'You left feedback',
        'We will take into account you suggestions, thank you',
        to=[email],
    )
    msg.send()
