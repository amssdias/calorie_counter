from re import template
from django.views import View
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = "accounts/pages/login.html"
    success_url = "profile"