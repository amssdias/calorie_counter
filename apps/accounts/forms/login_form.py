from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.sites.shortcuts import get_current_site
from django.utils.translation import gettext_lazy as _

from apps.accounts.models.user import User
from apps.accounts.tasks.send_email import send_email_async
from calorie_counter.utils.celery import task_celery


class LoginForm(AuthenticationForm):
    username = UsernameField(label="Email", widget=forms.TextInput(attrs={'autofocus': True}))

    def clean_username(self):
        email = self.cleaned_data['username']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError(_("User does not exist. Register first."))
        else:
            if not user.is_active:

                # Send activation link to user
                current_site = get_current_site(self.request)
                task_celery(send_email_async, user_id=user.id, domain=current_site.domain)

                raise forms.ValidationError(_("User is not active, check your inbox for an activation link."))
            else:
                return user
