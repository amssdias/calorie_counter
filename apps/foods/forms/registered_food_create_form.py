from django import forms

from apps.foods.models import RegisteredFood


class RegisteredFoodCreateForm(forms.ModelForm):
    class Meta:
        model = RegisteredFood
        exclude = ["user_profile", "slug"]

        widgets = {
            "food": forms.Select(attrs={"class": "form-control"}),
            "meal": forms.Select(attrs={"class": "form-control"}),
        }