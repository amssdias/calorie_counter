from celery import shared_task

from apps.accounts.utils import send_email

@shared_task
def send_email_async(*args, **kwargs):
    send_email(*args, **kwargs)
