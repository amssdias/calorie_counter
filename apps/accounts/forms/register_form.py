from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from apps.accounts.models.user import User

class RegisterForm(UserCreationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ("email", )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({"class":"form-control"})
        self.fields["password2"].widget.attrs.update({"class":"form-control"})

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_("User with that email already exists."))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        if commit:
            user.save()
        return user
  
    
