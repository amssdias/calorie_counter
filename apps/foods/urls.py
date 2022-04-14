from django.urls import path

from apps.foods.views import ( 
    FoodDetailView, 
    FoodListView, 
    FoodUpdateView, 
    FoodCreateView, 
    FoodDeleteView,
    RegistereFoodListView,
    RegisteredFoodCreateView, 
    RegisteredFoodInitialCreateView, 
    RegisteredFoodDeleteView,
    FoodConsumedListView, 
)


app_name = "foods"
urlpatterns = [
    path("all_foods/", FoodListView.as_view(), name="list_foods"),
    path("create_new_food/", FoodCreateView.as_view(), name="food_create"),
    path("detail/<slug:slug>", FoodDetailView.as_view(), name="food_details"),
    path("update/<slug:slug>", FoodUpdateView.as_view(), name="food_update"),
    path("delete/<slug:slug>", FoodDeleteView.as_view(), name="food_delete"),

    path("registered_foods/", RegistereFoodListView.as_view(), name="registered_foods"),
    path("register_food/", RegisteredFoodCreateView.as_view(), name="register_food_create"),
    path("register_food/<slug:food_slug>", RegisteredFoodInitialCreateView.as_view(), name="register_food_create_initial"),
    path("delete_registered_food/<slug:slug>", RegisteredFoodDeleteView.as_view(), name="register_food_delete"),

    path("food_consumed/<slug:food_registered_slug>", FoodConsumedListView.as_view(), name="food_consumed_list"), 
]
