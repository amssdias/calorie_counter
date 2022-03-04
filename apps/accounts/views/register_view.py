from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.utils.translation import gettext
from django.views.generic.edit import CreateView

from apps.accounts.forms.register_form import RegisterForm
from apps.accounts.tasks.send_email import send_email_async

from calorie_counter.utils.celery import task_celery


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = "accounts/pages/register.html"
    success_url = "/accounts/login/"

    def form_valid(self, form):
        user = form.save()

        current_site = get_current_site(self.request)
        task_celery(send_email_async, user_id=user.id, domain=current_site.domain)

        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        response.status_code = 400
        return response

    def get_success_message(self, cleaned_data):
        return gettext("User created, check your email to activate your account.")
