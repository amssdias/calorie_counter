from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic.list import ListView

from apps.foods.models import RegisteredFood


class RegistereFoodListView(LoginRequiredMixin, ListView):
    model = RegisteredFood

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_profile=self.request.user.profile)

