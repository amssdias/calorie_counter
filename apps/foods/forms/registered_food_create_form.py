from django import forms
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from apps.foods.models import RegisteredFood, Food


class RegisteredFoodCreateForm(forms.ModelForm):
    class Meta:
        model = RegisteredFood
        exclude = ["user_profile", "slug"]

        widgets = {
            "food": forms.Select(attrs={"class": "form-control"}),
            "meal": forms.Select(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)
        self.fields["food"].queryset = Food.objects.filter(
            Q(created_by=self.request.user.profile) | Q(created_by__isnull=True)
        )

    def clean(self):
        cleaned_data = super().clean()
        user_profile = self.request.user.profile
        food = cleaned_data.get("food")
        meal = cleaned_data.get("meal")
        queryset = RegisteredFood.objects.filter(
            user_profile=user_profile, food=food, meal=meal
        )
        if queryset.exists():
            raise forms.ValidationError(
                _("User already have this food and meal registered.")
            )
        return cleaned_data
