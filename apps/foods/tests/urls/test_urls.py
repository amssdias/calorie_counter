from django.test import TestCase
from django.urls import reverse, resolve

from apps.foods.views import (
    FoodDetailView,
    FoodUpdateView,
    FoodListView,
    FoodCreateView,
    FoofDeleteView,
    RegistereFoodListView, 
    RegisteredFoodCreateView, 
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

    def test_food_create_url_resolves(self):
        url = reverse("foods:food_create")
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, FoodCreateView)
    
    def test_food_delete_url_resolves(self):
        url = reverse("foods:food_delete", kwargs={"slug": "slug-field"})
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, FoofDeleteView)

    def test_list_registered_food_url_resolves(self):
        url = reverse("foods:registered_foods")
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, RegistereFoodListView)
    
    def test_create_registered_food_url_resolves(self):
        url = reverse("foods:register_food_create")
        view_class = resolve(url).func.view_class
        self.assertEqual(view_class, RegisteredFoodCreateView)
