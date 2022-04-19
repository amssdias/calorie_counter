from django.db import models
from django.urls import reverse

from apps.accounts.models.profile import Profile


class Food(models.Model):
    name = models.CharField(max_length=70)
    brand = models.CharField(max_length=70, null=True, blank=True)
    weight = models.IntegerField(default=100)
    calories = models.DecimalField(max_digits=8, decimal_places=2)
    total_fat = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    carbs = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    fiber = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    protein = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    salt = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True)
    created_by = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="created_foods",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name} - {self.brand}"

    def get_absolute_url(self):
        url = reverse("foods:food_details", kwargs={"slug": self.slug})
        return url
