from django.contrib.auth.views import LoginView

from apps.accounts.forms.login_form import LoginForm

class CustomLoginView(LoginView):
    template_name = "accounts/pages/login.html"
    authentication_form = LoginForm
