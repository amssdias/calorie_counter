from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.foods.models import RegisteredFood
from calorie_counter.models.abstracts import TimeStampable


class FoodConsumed(TimeStampable):
    registered_food = models.ForeignKey(RegisteredFood, on_delete=models.CASCADE)
    grams = models.IntegerField(help_text=_("Kg/Ml"))

    class Meta:
        verbose_name = _("Food Consumed")
        verbose_name_plural = _("Foods Consumed")

    def __str__(self):
        return f"{self.registered_food.user_profile} - {self.registered_food.food} ({self.grams} Kg/Ml)"