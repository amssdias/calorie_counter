from django import forms

from apps.foods.models import Food


class FoodCreateForm(forms.ModelForm):
    field_order = ["name", "brand", "weight"]
    
    class Meta:
        model = Food
        exclude = ["slug", "created_by"]
        labels = {
            "weight": "Weight (Kg/Ml)",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form__input"}),
            "brand": forms.TextInput(attrs={"class": "form__input"}),
            "weight": forms.NumberInput(attrs={"class": "form__input"}),
            "calories": forms.NumberInput(attrs={"class": "form__input"}),
            "total_fat": forms.NumberInput(attrs={"class": "form__input"}),
            "carbs": forms.NumberInput(attrs={"class": "form__input"}),
            "fiber": forms.NumberInput(attrs={"class": "form__input"}),
            "protein": forms.NumberInput(attrs={"class": "form__input"}),
            "salt": forms.NumberInput(attrs={"class": "form__input"}),
        }
