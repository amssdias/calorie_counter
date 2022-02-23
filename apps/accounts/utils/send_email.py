from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from apps.accounts.utils import generate_token


def send_email(user, request, email_subject="Activate your account", email_template_name="accounts/email/activate_account.html"):
    current_site = get_current_site(request)
        
    message = render_to_string(email_template_name, 
    {
        "user": user,
        "domain": current_site.domain,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": generate_token.make_token(user)
    })

    email = EmailMessage(
        subject=email_subject,
        body=message,
        to=[user.email],
    )
    
    email.send()