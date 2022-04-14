from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from apps.foods.models import FoodConsumed, registered_food


class FoodConsumedListView(LoginRequiredMixin, ListView):
    model = FoodConsumed
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        registered_food_slug = self.kwargs.get("food_registered_slug", "")
        return queryset.filter(
            registered_food__user_profile__user=self.request.user,
            registered_food__slug=registered_food_slug,
        )
