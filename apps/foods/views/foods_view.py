from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from apps.foods.models.food import Food


class FoodListView(LoginRequiredMixin, ListView):
    # TODO: View to display/list all foods
    # TODO: one button to check food details
        # TODO: Button to update food if its a food created by the user
    # TODO: one button to add food to his register foods
    model = Food
    template_name_suffix = "_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            Q(created_by=self.request.user.profile) |
            Q(created_by__isnull=True)
        )


class FoodDetailView(LoginRequiredMixin, DetailView):
    model = Food
    template_name_suffix = "_detail"

class FoodUpdateView(LoginRequiredMixin, UpdateView):
    model = Food
    fields = "__all__"
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return self.object.get_absolute_url()
