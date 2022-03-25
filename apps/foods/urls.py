from unicodedata import name
from django.urls import path

from apps.foods.views.foods_view import FoodDetailView, FoodListView, FoodUpdateView


app_name = "foods"
urlpatterns = [
    path("all_foods/", FoodListView.as_view(), name="list_foods"),
    path("detail/<slug:slug>", FoodDetailView.as_view(), name="food_details"),
    path("update/<slug:slug>", FoodUpdateView.as_view(), name="food_update"),
]
