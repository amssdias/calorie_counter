import logging

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from apps.accounts.models.user import User
from apps.accounts.utils import generate_token

logger = logging.getLogger("django")


def send_email(user_id, domain):
    if not settings.EMAIL_ENABLED:
        user = User.objects.get(id=user_id)
        user.is_active = True
        user.save()
        return True

    logger.info("Sending email, generating template with token.")

    email_subject = "Activate your account"
    email_template_name = "accounts/email/activate_account.html"

    user = User.objects.get(id=user_id)
    message = render_to_string(
        email_template_name,
        {
            "user": user,
            "domain": domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": generate_token.make_token(user),
        },
    )

    email = EmailMessage(
        subject=email_subject,
        body=message,
        to=[user.email],
    )

    try:
        email.send()
        logger.info(f"Sent email to user: {user_id}")
    except Exception as e:
        logger.warning(f"Couldn't send email to activate account. - {e}")
        return False
    return True
