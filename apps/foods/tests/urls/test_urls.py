from django.test import TestCase
from django.urls import reverse, resolve

from apps.foods.views import (
    FoodDetailView,
    FoodUpdateView,
    FoodListView
)


class TestUrls(TestCase):
    
    def test_list_foods_account_url_resolves(self):
        url = reverse("foods:list_foods")
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, FoodListView)

    def test_food_details_url_resolves(self):
        url = reverse("foods:food_details", kwargs={"slug": "slug-field"})
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, FoodDetailView)

    def test_food_update_url_resolves(self):
        url = reverse("foods:food_update", kwargs={"slug": "slug-field"})
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, FoodUpdateView)

