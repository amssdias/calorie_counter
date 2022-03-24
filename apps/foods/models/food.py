from django.db import models

from apps.accounts.models.profile import Profile


class Food(models.Model):
    name = models.CharField(max_length=70)
    brand = models.CharField(max_length=70, null=True, blank=True)
    weight = models.IntegerField(default=100)
    calories = models.IntegerField()
    total_fat = models.IntegerField(null=True, blank=True)
    carbs = models.IntegerField(null=True, blank=True)
    fiber = models.IntegerField(null=True, blank=True)
    protein = models.IntegerField(null=True, blank=True)
    salt = models.IntegerField(null=True, blank=True)

    slug = models.SlugField(max_length=250, unique=True, null=True, blank=True)
    created_by = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        related_name="created_foods",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name} - {self.brand}"
