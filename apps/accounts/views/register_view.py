from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from apps.accounts.forms.register_form import RegisterForm
from apps.accounts.utils import send_email


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = "accounts/pages/register.html"
    success_url = "/accounts/login/"
    success_message = "User created, check your email to activate your account."

    def form_valid(self, form):
        user = form.save()
        send_email(user=user, request=self.request)
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = 400
        return response
