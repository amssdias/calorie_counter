from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _

from apps.accounts.models.user import User
from apps.accounts.utils import send_email


class LoginForm(AuthenticationForm):
    username = UsernameField(label="Email", widget=forms.TextInput(attrs={'autofocus': True}))

    def clean_username(self):
        email = self.cleaned_data['username']
        user = User.objects.get(email=email)
        if not user.is_active:
            # send_email(
            #     user=user, 
            #     request=self.request,
            # )
            raise forms.ValidationError(_("User is not active, check your inbox for an activation link."))
        return user
