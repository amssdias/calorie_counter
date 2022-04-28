from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView
from django.views.generic.list import ListView
from django.db.models import DateField, Sum
from django.contrib.postgres.aggregates import ArrayAgg, JSONBAgg
from django.db.models.functions import Trunc

from apps.foods.forms import FoodConsumedCreateForm
from apps.foods.models import FoodConsumed
from apps.foods.models.registered_food import RegisteredFood


class FoodConsumedListView(LoginRequiredMixin, ListView):
    model = FoodConsumed
    paginate_by = 20

    def get_queryset(self):
        # I should get the ids of the food consumed correspondent to each day
        # Maybe get a model where we get a day with all nutrition calculated
        queryset = super().get_queryset()
        # grouped_dates = (
        #     queryset.filter(registered_food__user_profile__user=self.request.user)
        #     .annotate(date=Trunc("created", "day", output_field=DateField()))
        #     .values("date")
        #     .annotate(registered=ArrayAgg("registered_food"))
        #     .order_by("date")
        # )

        # days = []
        # # q = queryset.filter(registered_food__user_profile__user=self.request.user).annotate(date=Trunc("created", "day", output_field=DateField())).values("date").annotate(registered=Subquery(RegisteredFood.objects.filter(id__in=OuterRef("registered_food")))).order_by("date").values("date", "registered")

        # for day in grouped_dates:
        #     date, registered_foods_id = day.values()

        #     # Get all foods from registered foods
        #     registered_foods = RegisteredFood.objects.filter(
        #         id__in=registered_foods_id
        #     ).annotate(
        #         # calories=,
        #         # total_fat=Sum("total_fat"),
        #         # carbs=Sum("carbs"),
        #         # fiber=Sum("fiber"),
        #         # protein=Sum("protein"),
        #         # salt=Sum("salt"),
        #     )

        #     # Calculate based on the grams of each food_consumed

        #     days.append(
        #         {
        #             "date": date,
        #             "calories": registered_foods["calories"],
        #             # "total_fat": registered_foods["total_fat"],
        #             # "carbs": registered_foods["carbs"],
        #             # "fiber": registered_foods["fiber"],
        #             # "protein": registered_foods["protein"],
        #             # "salt": registered_foods["salt"],
        #         }
        #     )

        return queryset.filter(registered_food__user_profile__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class FoodConsumedRegisteredListView(LoginRequiredMixin, ListView):
    model = FoodConsumed
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        registered_food_slug = self.kwargs.get("food_registered_slug", "")
        return queryset.filter(
            registered_food__user_profile__user=self.request.user,
            registered_food__slug=registered_food_slug,
        )


class FoodConsumedDetailView(LoginRequiredMixin, DetailView):
    model = FoodConsumed

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["food_consumed_values"] = self.get_food_consumed_values(
            context["object"]
        )
        return context

    def get_food_consumed_values(self, food_consumed: FoodConsumed):
        food_grams = food_consumed.grams
        food = food_consumed.registered_food.food
        food_weight = food.weight

        return {
            "calories": self.rule_of_three(food.calories, food_grams, food_weight),
            "total_fat": self.rule_of_three(food.total_fat, food_grams, food_weight),
            "carbs": self.rule_of_three(food.carbs, food_grams, food_weight),
            "fiber": self.rule_of_three(food.fiber, food_grams, food_weight),
            "protein": self.rule_of_three(food.protein, food_grams, food_weight),
            "salt": self.rule_of_three(food.salt, food_grams, food_weight),
        }

    @staticmethod
    def rule_of_three(nutrition, grams: int, weight: int):
        return (nutrition * grams) / weight


class FoodConsumedCreateView(LoginRequiredMixin, CreateView):
    model = FoodConsumed
    template_name_suffix = "_create"
    form_class = FoodConsumedCreateForm
    success_url = reverse_lazy("foods:food_consumed_list")

    def get_form_kwargs(self):
        """
        Send request to form.__init__ so we can show the form with filtered foods
        """
        kwargs = super(FoodConsumedCreateView, self).get_form_kwargs()
        kwargs.update({"request": self.request})
        return kwargs


class FoodConsumedDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = FoodConsumed
    success_url = reverse_lazy("foods:food_consumed_list")
    success_message = _("Food was delete")

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return self.success_url
