from unicodedata import name
from django.urls import path

from .views import FoodView


app_name = "foods"
urlpatterns = [
    path("all_foods/", FoodView.as_view(), name="list_foods"),
]

