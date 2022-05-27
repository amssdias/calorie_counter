from django import forms
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from apps.foods.models import FoodConsumed, RegisteredFood, Food


class FoodConsumedCreateForm(forms.ModelForm):
    class Meta:
        model = FoodConsumed
        fields = "__all__"
        widgets = {
            "registered_food": forms.Select(attrs={"class": "form-control"}),
            "grams": forms.NumberInput(attrs={"class": "form-control"}),
            "meal": forms.Select(attrs={"class": "form-control"}),
            "created": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)
        self.fields["registered_food"].queryset = Food.objects.filter(
            Q(created_by=self.request.user.profile) | Q(created_by__isnull=True)
        )

    def clean_registered_food(self):
        user_profile = self.request.user.profile
        food = self.cleaned_data.get("registered_food")
        registered_food = RegisteredFood.objects.filter(
            user_profile=user_profile, food=food
        )

        if registered_food.exists():
            return registered_food.get()
        else:
            registered_food = RegisteredFood.objects.create(
                user_profile=user_profile, food=food
            )

        return registered_food
