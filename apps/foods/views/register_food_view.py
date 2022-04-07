from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from apps.foods.models import RegisteredFood


class RegistereFoodListView(LoginRequiredMixin, ListView):
    model = RegisteredFood

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_profile=self.request.user.profile)


class RegisteredFoodCreateView(LoginRequiredMixin, CreateView):
    template_name_suffix = "_create"
    model = RegisteredFood
    fields = ["food", "meal"]
    success_url = reverse_lazy("foods:registered_foods") # Must Redirect to FoodConsumedCreateView

    def form_valid(self, form):
        registered_food = form.save(commit=False)
        registered_food.user_profile = self.request.user.profile
        registered_food.save()
        return super().form_valid(form)