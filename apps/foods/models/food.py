from django.db import models
from django.urls import reverse

from apps.accounts.models.profile import Profile


class Food(models.Model):
    name = models.CharField(max_length=70)
    brand = models.CharField(max_length=70, null=True, blank=True)
    weight = models.IntegerField(default=100)
    calories = models.DecimalField(max_digits=8, decimal_places=2)
    total_fat = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    carbs = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    fiber = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    protein = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    salt = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

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
        url = reverse("foods:food_details", kwargs={'slug': self.slug})
        return url
