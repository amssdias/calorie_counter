from django.test import TestCase

from apps.foods.forms import FoodCreateForm
from apps.foods.models import Food


class TestRegistrationForm(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.food = Food.objects.create(name="Rice", brand="Bazmati", calories=350)
        cls.data = {
            "user_profile": "",
            "food": "",
            "meal": "",
            "slug": "",
        }
        return super().setUpTestData()
