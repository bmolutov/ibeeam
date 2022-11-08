from main.tasks import send_feedback_email_task


def send_email(email):
    send_feedback_email_task.delay(
        email=email
    )
