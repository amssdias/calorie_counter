from django.contrib import admin

from apps.foods.models import (
    RegisteredFood,
    BreakfastRegistered,
    LunchRegistered,
    DinnerRegistered,
    DessertRegistered,
    SnacksRegisteredFood,
)


class RegisteredFoodAdminCustom(admin.ModelAdmin):
    list_display = ("get_user", "food", "meal", "date")

    @admin.display(description="User")
    def get_user(self, obj):
        return obj.user.user.username


admin.site.register(RegisteredFood, RegisteredFoodAdminCustom)
admin.site.register(BreakfastRegistered, RegisteredFoodAdminCustom)
admin.site.register(LunchRegistered, RegisteredFoodAdminCustom)
admin.site.register(DinnerRegistered, RegisteredFoodAdminCustom)
admin.site.register(DessertRegistered, RegisteredFoodAdminCustom)
admin.site.register(SnacksRegisteredFood, RegisteredFoodAdminCustom)
