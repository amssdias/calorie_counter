from apps.foods.views.foods_view import (
    FoodListView,
    FoodDetailView,
    FoodUpdateView,
    FoodCreateView,
    FoodDeleteView,
    SessionFoodView,
)

from apps.foods.views.register_food_view import (
    RegisteredFoodListView,
    RegisteredFoodDeleteView, 
)

from apps.foods.views.food_consumed import (
    FoodConsumedListView, 
    FoodConsumedRegisteredListView, 
    FoodConsumedDetailView, 
    FoodConsumedCreateView, 
    FoodConsumedDeleteView, 
)

from apps.foods.views.daily_user_food_stats_view import DailyUserFoodStatsView
