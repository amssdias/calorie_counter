from django.contrib import admin

from apps.foods.models import FoodConsumed

@admin.register(FoodConsumed)
class FoodConsumedAdmin(admin.ModelAdmin):
    list_display = ("id", "registered_food", "grams", "created")
    readonly_fields = ("created", "modified")
