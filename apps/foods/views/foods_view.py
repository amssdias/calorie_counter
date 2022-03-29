from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from apps.foods.models.food import Food


class FoodListView(LoginRequiredMixin, ListView):
    model = Food
    template_name_suffix = "_list"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            Q(created_by=self.request.user.profile) | Q(created_by__isnull=True)
        )


class FoodDetailView(LoginRequiredMixin, DetailView):
    model = Food
    template_name_suffix = "_detail"


class FoodUpdateView(LoginRequiredMixin, UpdateView):
    model = Food
    fields = "__all__"
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return self.object.get_absolute_url()


class FoodCreateView(LoginRequiredMixin, CreateView):
    model = Food
    fields = "__all__"
    form_class = None
    success_url = reverse_lazy("foods:list_foods")

    def form_valid(self, form):
        food = form.save(commit=False)
        food.created_by = self.request.user.profile
        food.save()
        return super().form_valid(form)


class FoofDeleteView(LoginRequiredMixin, DeleteView):
    model = Food
    success_url = reverse_lazy("foods:list_foods")
