from django.core.mail import EmailMessage

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic.edit import CreateView

from apps.accounts.forms.register_form import RegisterForm
from apps.accounts.utils import generate_token


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "accounts/register.html"
    success_url = "/accounts/login/"
    
    # Settings to send email
    email_subject = "Welcome, activate your account!"
    email_template_name = "accounts/activate/activate_account.html"

    def form_valid(self, form):
        user = form.save()
        self.send_email(user=user, request=self.request)
        return super().form_valid(form)

    def send_email(self, user, request):
        current_site = get_current_site(request)
        
        message = render_to_string(self.email_template_name, 
        {
            "user": self,
            "domain": current_site.domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": generate_token.make_token(user)
        })

        email = EmailMessage(
            subject=self.email_subject,
            body=message,
            to=[user.email],
        )
        
        email.send()