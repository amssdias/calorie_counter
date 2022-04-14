from django.test import TestCase, RequestFactory
from django.urls import reverse

from apps.foods.forms import RegisteredFoodCreateForm
from apps.accounts.models import User
from apps.foods.models import Food, RegisteredFood


class TestRegistrationForm(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.food = Food.objects.create(name="Rice", brand="Bazmati", calories=350)
        cls.user = User.objects.create_user(
            username="Test", email="test@testing.com", password="testing123"
        )

        cls.factory = RequestFactory()
        cls.request = cls.factory.get(reverse("foods:register_food_create"))
        cls.request.user = cls.user
        
        cls.data = {
            "food": cls.food,
        }
        
        return super().setUpTestData()

    def test_form_valid(self):
        registered_food_form = RegisteredFoodCreateForm(data=self.data, request=self.request)
        self.assertTrue(registered_food_form.is_valid())

    def test_form_invalid_food(self):
        self.data["food"] = "Rice"
        registered_food_form = RegisteredFoodCreateForm(data=self.data, request=self.request)
        self.assertFalse(registered_food_form.is_valid())

    def test_form_no_data(self):
        registered_food_form = RegisteredFoodCreateForm(data={}, request=self.request)
        self.assertFalse(registered_food_form.is_valid())

    def test_registered_food_created(self):
        pass