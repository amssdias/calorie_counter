from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class ProfileView(LoginRequiredMixin, View):
    login_url = reverse_lazy('accounts:login')

    def get(self, request, *args, **kwargs):
        return render(request, "accounts/pages/profile.html")