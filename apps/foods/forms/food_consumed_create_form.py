from django import forms
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from apps.foods.models import FoodConsumed, RegisteredFood


class FoodConsumedCreateForm(forms.ModelForm):
    class Meta:
        model = FoodConsumed
        exclude = ("created",)
        widgets = {
            "registered_food": forms.Select(attrs={"class": "form-control"}),
            "grams": forms.NumberInput(attrs={"class": "form-control"}),
            "meal": forms.Select(attrs={"class": "form-control"})
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)
        self.fields["registered_food"].queryset = RegisteredFood.objects.filter(
            user_profile=self.request.user.profile
        )
