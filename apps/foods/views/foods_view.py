from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.foods.models.food import Food


class FoodView(LoginRequiredMixin, ListView):
    # TODO: View to display/list all foods
    # TODO: one button to check food details
        # TODO: Button to update food if its a food created by the user
    # TODO: one button to add food to his register foods
    model = Food
    template_name_suffix = '_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context