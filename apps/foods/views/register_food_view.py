from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from apps.foods.forms import RegisteredFoodCreateForm
from apps.foods.models import Food, RegisteredFood


class RegistereFoodListView(LoginRequiredMixin, ListView):
    model = RegisteredFood

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_profile=self.request.user.profile)


class RegisteredFoodCreateView(LoginRequiredMixin, CreateView):
    template_name_suffix = "_create"
    model = RegisteredFood
    form_class = RegisteredFoodCreateForm
    success_url = reverse_lazy("foods:registered_foods") # Must Redirect to FoodConsumedCreateView

    def form_valid(self, form):
        registered_food = form.save(commit=False)
        registered_food.user_profile = self.request.user.profile
        registered_food.save()
        return super().form_valid(form)


class RegisteredFoodInitialCreateView(RegisteredFoodCreateView):
    def get_initial(self):
        food_slug = self.kwargs.get("food_slug")
        food = Food.objects.get(slug=food_slug)
        initial = {"food": food}
        return initial
