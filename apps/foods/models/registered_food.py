from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.accounts.models import Profile
from apps.foods.models.food import Food
from apps.foods.models.managers import RegisteredFoodManager


class RegisteredFood(models.Model):
    BREAKFAST = "BKFT"
    LUNCH = "LNCH"
    DINNER = "DNNR"
    DESSERT = "DSST"
    SNACK = "SNCK"

    MEALS = (
        (BREAKFAST, _("Breakfast")),
        (LUNCH, _("Lunch")),
        (DINNER, _("Dinner")),
        (DESSERT, _("Dessert")),
        (SNACK, _("Snack")),
    )

    user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="registered_foods"
    )
    food = models.ForeignKey(
        Food, on_delete=models.CASCADE, null=True, related_name="registered_by_users"
    )
    meal = models.CharField(max_length=4, choices=MEALS)
    slug = models.SlugField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = _("Registered Food")
        verbose_name_plural = _("Registered Foods")
        constraints = [
            models.UniqueConstraint(fields=["user_profile", "food", "meal"], name="unique_user_food_meal")
        ]

    def __str__(self):
        return f"{self.food.name} - {self.food.brand}"


class BreakfastRegistered(RegisteredFood):
    objects = RegisteredFoodManager(RegisteredFood.BREAKFAST)

    class Meta:
        proxy = True
        verbose_name = _("Breakfast registered")
        verbose_name_plural = _("Breakfasts registered")


class LunchRegistered(RegisteredFood):
    objects = RegisteredFoodManager(RegisteredFood.LUNCH)

    class Meta:
        proxy = True
        verbose_name = _("Lunch registered")
        verbose_name_plural = _("Lunches registered")


class DinnerRegistered(RegisteredFood):
    objects = RegisteredFoodManager(RegisteredFood.DINNER)

    class Meta:
        proxy = True
        verbose_name = _("Dinner registered")
        verbose_name_plural = _("Dinners registered")


class DessertRegistered(RegisteredFood):
    objects = RegisteredFoodManager(RegisteredFood.DESSERT)

    class Meta:
        proxy = True
        verbose_name = _("Dessert registered")
        verbose_name_plural = _("Desserts registered")


class SnacksRegisteredFood(RegisteredFood):
    objects = RegisteredFoodManager(RegisteredFood.SNACK)

    class Meta:
        proxy = True
        verbose_name = _("Snack registered")
        verbose_name_plural = _("Snacks registered")
