from django.contrib.auth.forms import SetPasswordForm

class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["new_password1"].widget.attrs.update({"class": "form__input form__input-text-align-center margin-bottom-xsmall"})
        self.fields["new_password2"].widget.attrs.update({"class": "form__input form__input-text-align-center margin-bottom-xsmall"})
